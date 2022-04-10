const onClick = function() {
    localStorage.setItem("idActive", this.id);
    this.classList.add("active");
}

const homeOnClick = function() {
    localStorage.removeItem("idActive");
}

if(localStorage.getItem("idActive")){
    idActive = localStorage.getItem("idActive")
    document.getElementById(idActive).classList.add("active")
}

document.getElementById('BTC').onclick = onClick;
document.getElementById('BNB').onclick = onClick;
document.getElementById('ETH').onclick = onClick;
document.getElementById('LTC').onclick = onClick;
document.getElementById('NEO').onclick = onClick;
document.getElementById('nav_crypto').onclick = onClick;