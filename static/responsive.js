const onClick = function() {
    localStorage.setItem("idActive", this.id);
    this.classList.add("active");
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