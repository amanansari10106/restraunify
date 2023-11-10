document.addEventListener("DOMContentLoaded", ()=>{
    let nav = document.querySelector("#header");
    let atop = document.querySelector(".ptop");

    atop.style.marginTop =  nav.offsetHeight;
    // atop.style.paddingTop =  nav.offsetHeight;

    // document.addEventListener("scrool",()=>{
    //     let nav = document.querySelector("#header");
    //     let atop = document.querySelector(".ptop");
    
    //     atop.style.paddingTop =  nav.offsetHeight;
    // })
})