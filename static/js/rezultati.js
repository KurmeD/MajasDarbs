const ATJAUNOT = 5000;

async function lasiRezultatu(){
    const atbilde = await fetch('/rezultati/lasi');
    const datuObjekts = await atbilde.json();
    //raadiChatuVienkarsi(datuObjekts);
    raadiRezultataRindas(datuObjekts);
    await new Promise(resolve=> setTimeout(resolve, ATJAUNOT));
    await lasiRezultatu();

}

// function  raadiChatuVienkarsi(dati){
//     const jaunaRinda = "</br>";
//     let chats = "";
//     let chataDiv = document.getElementById("chats");

//     for(let rinda of dati['chats']){
//         chats = chats + rinda + jaunaRinda;
//     }

//     chataDiv.innerHTML = chats;

// }
async function suutiRezultatu(rezultats, limenis){
    let autors = document.getElementById('autors').value;
    const atbilde = await fetch('/rezultati/suuti', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({"rezultats": rezultats, "autors":autors, "limenis":limenis})
    });
    
    const datuObjekts = await atbilde.json();

    //raadiChatuVienkarsi(datuObjekts);
    raadiRezultataRindas(datuObjekts);
}

// let ievadesLauks = document.getElementById("zinja");
// ievadesLauks.addEventListener("keyup", function(event){
//     if(event.keyCode === 13){
//         suutiZinju();
//     }
// })



function raadiRezultataRindas(dati) {
    
    const chatUL6 = document.getElementById("pari6rezult");
    const chatUL5 = document.getElementById("pari5rezult");
    const chatUL4 = document.getElementById("pari4rezult");
    // novaacam ieprieksheejo saturu
    while (chatUL6.firstChild) {
        chatUL6.firstChild.remove();
    }
    while (chatUL5.firstChild) {
        chatUL5.firstChild.remove();
    }
    while (chatUL4.firstChild) {
        chatUL4.firstChild.remove();
    }
    for (let rinda of dati["rezultati6"]) {
        chatLI = izveidoJaunuRindu(rinda);
        chatUL6.appendChild(chatLI);
    }
    for (let rinda of dati["rezultati5"]) {
        chatLI = izveidoJaunuRindu(rinda);
        chatUL5.appendChild(chatLI);
    }
    for (let rinda of dati["rezultati4"]) {
        chatLI = izveidoJaunuRindu(rinda);
        chatUL4.appendChild(chatLI);
    }
          // noskrolleejam uz leju pie peedeejaa chata texta
    // var chatScrollBox = chatUL.parentNode;
    // chatScrollBox.scrollTop = chatScrollBox.scrollHeight;
}
  
// async function skatitRezultatus(){
//     const atbilde = await fetch('/chats/lasi');
//     const datuObjekts = await atbilde.json();

//     const chatUL = document.getElementById("chats");
//     // novaacam ieprieksheejo saturu
//     while (chatUL.firstChild) {
//         chatUL.firstChild.remove();
//     }
//     for (let rinda of datuObjekts["chats"]) {
//         if (rinda.startsWith("System")){
//             console.log("jee");
//             chatLI = izveidoJaunuRindu(rinda);
//             chatUL.appendChild(chatLI);      
//         } else {console.log("noooo")}
//     }
//     // noskrolleejam uz leju pie peedeejaa chata texta
//     var chatScrollBox = chatUL.parentNode;
//     chatScrollBox.scrollTop = chatScrollBox.scrollHeight;
// }


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