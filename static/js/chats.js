
async function lasiChatu(){
    const atbilde = await fetch('/chats/lasi');
    const datuObjekts = await atbilde.json();
    //raadiChatuVienkarsi(datuObjekts);
    raadiChataRindas(datuObjekts);
    await new Promise(resolve=> setTimeout(resolve, ATJAUNOT));
    await lasiChatu();

}

function  raadiChatuVienkarsi(dati){
    const jaunaRinda = "</br>";
    let chats = "";
    let chataDiv = document.getElementById("chats");

    for(let rinda of dati['chats']){
        chats = chats + rinda + jaunaRinda;
    }

    chataDiv.innerHTML = chats;

}
async function suutiZinju(){
    let zinjasElements = document.getElementById('zinja');
    let zinja = zinjasElements.value;
    let autors = document.getElementById('autors').value;

    zinjasElements.value = "";

    const atbilde = await fetch('/chats/suuti', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"chats": zinja, "autors":autors})
    });
    
    const datuObjekts = await atbilde.json();

    //raadiChatuVienkarsi(datuObjekts);
    raadiChataRindas(datuObjekts);
}

let ievadesLauks = document.getElementById("zinja");
ievadesLauks.addEventListener("keyup", function(event){
    if(event.keyCode === 13){
        suutiZinju();
    }
})



function raadiChataRindas(dati) {
    
    const chatUL = document.getElementById("chats");
    // novaacam ieprieksheejo saturu
    while (chatUL.firstChild) {
        chatUL.firstChild.remove();
    }
    for (let rinda of dati["chats"]) {
      chatLI = izveidoJaunuRindu(rinda);
      chatUL.appendChild(chatLI);
    }
    // noskrolleejam uz leju pie peedeejaa chata texta
    var chatScrollBox = chatUL.parentNode;
    chatScrollBox.scrollTop = chatScrollBox.scrollHeight;
}
  
async function skatitRezultatus(){
    const atbilde = await fetch('/chats/lasi');
    const datuObjekts = await atbilde.json();

    const chatUL = document.getElementById("chats");
    // novaacam ieprieksheejo saturu
    while (chatUL.firstChild) {
        chatUL.firstChild.remove();
    }
    for (let rinda of datuObjekts["chats"]) {
        if (rinda.startsWith("System")){
            console.log("jee");
            chatLI = izveidoJaunuRindu(rinda);
            chatUL.appendChild(chatLI);      
        } else {console.log("noooo")}
    }
    // noskrolleejam uz leju pie peedeejaa chata texta
    var chatScrollBox = chatUL.parentNode;
    chatScrollBox.scrollTop = chatScrollBox.scrollHeight;
}


function izveidoJaunuRindu(zinja) { 
    let newLI = document.createElement("li");
    newLI.className = "left clearfix"
    let newDiv = document.createElement("div"); 
    newDiv.className = "chat-body clearfix"
    let newContent = document.createTextNode(zinja); 
    newLI.appendChild(newDiv); 
    newDiv.appendChild(newContent); 
    return newLI;
}