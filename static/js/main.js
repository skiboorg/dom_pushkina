
console.log("ready!");

let modal = document.getElementById('myModal');

let btn = document.getElementById("header-order-btn");

let span = document.getElementsByClassName("close")[0];
let divs = document.getElementsByClassName('how-it-works-circle')
btn.onclick = function () {
    modal.style.display = "block";
}

span.onclick = function () {
    modal.style.display = "none";
}
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
for (let div in divs) {
    divs[div].addEventListener('mouseover',function(){
        let circle = this.getElementsByClassName('circle-grey')[0]
        let dash = this.getElementsByClassName('dash-grey')[0]
        let head = this.getElementsByClassName('how-it-works-item-head')[0]
        let desc = this.getElementsByClassName('how-it-works-item-description')[0]
        let time = this.getElementsByClassName('how-it-works-item-time')[0]
        circle.classList.remove('circle-grey')
        circle.classList.add('circle-pink')
        head.classList.remove('color-grey')
        head.classList.add('color-pink')
        desc.classList.remove('color-grey')
        time.classList.remove('color-grey')

        if (dash) {
            dash.classList.remove('dash-grey')
            dash.classList.add('dash-pink')
        }


    })
    divs[div].addEventListener('mouseout',function(){
        let circle = this.getElementsByClassName('circle-pink')[0]
        let dash = this.getElementsByClassName('dash-pink')[0]
        let head = this.getElementsByClassName('how-it-works-item-head')[0]
        let desc = this.getElementsByClassName('how-it-works-item-description')[0]
        let time = this.getElementsByClassName('how-it-works-item-time')[0]
        circle.classList.remove('circle-pink')
        circle.classList.add('circle-grey')
        head.classList.remove('color-pink')
        head.classList.add('color-grey')
        desc.classList.add('color-grey')
        time.classList.add('color-grey')
        if (dash){
            dash.classList.remove('dash-pink')
            dash.classList.add('dash-grey')
        }
    })
}


