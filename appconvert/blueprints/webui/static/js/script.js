// Flip card
const cards = document.querySelectorAll('.card');

cards.forEach(card => card.addEventListener('click', event => {
    event.target.classList.toggle('is-flipped');
}));


// Rolar categorias pelo scroll e clicando nos botões
const categories = document.querySelector(".header__lista");
const arrows = document.querySelectorAll(".header__arrow")

// Adiciona eventos aos botoões (setas)
arrows.forEach(arrow => {
    arrow.addEventListener("click", arrow_header);
    categories.addEventListener("wheel", arrow_header);
})

function arrow_header(event) {
    event.preventDefault();
    let scroll_x = categories.scrollLeft;
    let arrow_left = document.querySelector(".arrow-left");
    let arrow_right = document.querySelector(".arrow-right");
    let space_scroll = 50

    if (scroll_x < 50) {
        arrow_left.style.display = 'none';
    }

    else if (scroll_x > 369) {
        arrow_right.style.display = 'none';
    }

    else {
        arrow_left.style.display = 'flex';
        arrow_right.style.display = 'flex';
    }

    if (event.target.classList[1] === 'arrow-left') {
        space_scroll *= -1
    }

    categories.scrollBy({
        left: event.deltaY < 0 ? space_scroll * -1 : space_scroll,
    });

}

// currency converter button

document.getElementById('btn-send').onclick = function () {
    let xhr = new XMLHttpRequest();
    var [token1, token2] = document.querySelectorAll('.choice-btn span');
    var amount = document.querySelector('.token_1 input[name="amount_1"]').value;
    if (amount <= 1) {
        amount = 1
    }
    xhr.responseType = "json"
    xhr.open("GET", "/api/v1/convert/" + token1.innerHTML + "&" + token2.innerHTML + "&" + amount, true);
    xhr.send()
    xhr.onload = function () {
        if (xhr.status === 200) {
            document.querySelector('.token_2 input[name="amount_2"]').value = xhr.response['price']
        }
    }
}