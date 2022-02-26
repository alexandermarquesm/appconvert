// Flip card
const cards = document.querySelectorAll('.card');

cards.forEach(card => card.addEventListener('click', event => {
    event.target.classList.toggle('is-flipped');
}));


// Rolar categorias pelo scroll e clicando nos botões
const categories = document.querySelector(".header__lista");
const arrows = document.querySelectorAll(".header__arrow")

// Adiciona eventos aos botoões do header (setas)
arrows.forEach(arrow => {
    arrow.addEventListener("click", arrowHeader);
    categories.addEventListener("wheel", arrowHeader);
})

function arrowHeader(event) {
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

// Botão para converter moedas
document.getElementById('btn-send').onclick = function () {
    var [token1, token2] = document.querySelectorAll('.choice-btn img');
    var amount = $("input[name='amount_1']").val();
    if (amount < 1) {
        amount = 1
    }

    $.ajax({
        type: 'GET',
        url: `/api/v1/convert/${token1.title}&${token2.title}&${amount}`,
        dataType: "json",

        success: function (response) {
            $("input[name='amount_2']").val(response['price']);
        },
    });

}

// Input de pesquisa de tokens
$('#search input').bind("keyup", function () {
    var regex = new RegExp("^[a-zA-Z\b]+$");
    var result = $(this).closest('.dropdown').find('.result');
    result.empty();
    if ($(this).val().length >= 3 && regex.test($(this).val())) {
        $.ajax({
            type: 'GET',
            url: '/api/v1/isvalid/' + $(this).val(),
            dataType: "json",

            success: function (response) {
                if (response['tokens'].length) {
                    var data = ''

                    response['tokens'].forEach(token => {
                        data += `
                        <span class="token_found">
                            <img src="${token['logo_url']}" title="${token['id']}">
                            <span>${token['symbol']}</span>
                        </span>
                    `
                    });
                    result.html(data);
                };
            },
            error: function (response) {
                console.log(response);
            },
        });
        return false;
    };
})

// Resultado da pesquisa
$('.result').on('click', '.token_found', function () {
    th = $(this);
    el = $(this).closest('.button-dropdown');
    img_link = th.children()[0].src
    img_title = th.children()[0].title

    text_content = $(this).children()[1].textContent;

    el.find('.choice-btn')[0].children[0].src = img_link
    el.find('.choice-btn')[0].children[0].title = img_title

    el.find('.choice-btn')[0].children[1].innerText = text_content
});

// Tokens iniciais
$('.token_found').bind('click', '.token_found', function () {
    th = $(this);
    el = $(this).closest('.button-dropdown');
    img_link = th.children()[0].src
    img_title = th.children()[0].title

    text_content = $(this).children()[1].textContent;

    el.find('.choice-btn')[0].children[0].src = img_link
    el.find('.choice-btn')[0].children[0].title = img_title

    el.find('.choice-btn')[0].children[1].innerText = text_content
});