active()


// When cards are loaded
$('.cards').on('click', '.card', function () {
    if (!$(this).hasClass('is-flipped')) {
        $(this)[0].classList.add('is-flipped');
    } else {
        $(this)[0].classList.remove('is-flipped');
    }
})


// category header make request with ajax jquery
$('.header__item').bind('click', function () {
    let elements = document.querySelectorAll('.header__item');
    elements.forEach(element => {
        if (element === $(this)[0]) {
            $(this)[0].classList.toggle('header__item--active');
            if ($(this).hasClass('header__item--active')) {
                $.ajax({
                    type: 'GET',
                    url: '/api/v1/category/' + $(this)[0].innerText,
                    dataType: "json",

                    success: function (response) {
                        if (response['tokens'].length) {
                            var data = ''
                            response['tokens'].forEach(token => {
                                data += `<div class="scene scene--card">
                                        <div class="card">
                                            <div class="card__face card__face--front">
                                                <img src="${token['logo_url']}" alt="">
                                                <span class="card__name">${token['name']}</span>
                                                <div class="card__footer">
                                                    <span>$${token['price']}</span>
                                                </div>
                                            </div>
                            
                                            <div class="card__face card__face--back">
                                                <img src="${token['logo_url']}" alt="">
                                                <div class="card__index">
                                                    <span>Symbol</span>
                                                    <span>Marketcap</span>
                                                    <span>Blockchain</span>
                                                </div>
                            
                                                <div class="card__info">
                                                    <span>${token['currency']}</span>
                                                    <span>${token['marketcap']}</span>
                                                    <span>${token['blockchain']}</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>`
                            })
                            $('.cards').html(data);
                        };
                    },
                    error: function (response) {
                        console.log(response);
                    },
                });
            }
        } else {
            element.classList.toggle('header__item--active', false);
        }
    })
})


// Rolar categorias pelo scroll e clicando nos bot??es
const categories = document.querySelector(".header__lista");
const arrows = document.querySelectorAll(".header__arrow")

// Adiciona eventos aos boto??es do header (setas)
arrows.forEach(arrow => {
    arrow.addEventListener("click", arrowHeader);
    categories.addEventListener("wheel", arrowHeader);
})

function arrowHeader(event) {
    event.preventDefault();
    let scroll_x = parseInt(100 * categories.scrollLeft / (categories.scrollWidth - categories.clientWidth))
    let arrow_left = document.querySelector(".arrow-left");
    let arrow_right = document.querySelector(".arrow-right");
    let space_scroll = 30

    if (scroll_x <= 6) {
        arrow_left.style.display = 'none';
    }

    else if (scroll_x >= 88) {
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


// Bot??o para converter moedas
$('#btn-send').bind('click', function () {
    var [token1, token2] = document.querySelectorAll('.choice-btn img');
    var amount = $("input[name='amount_1']").val();
    if (amount.length != 0) {
        if (amount < 1) {
            amount = 1
        }
        if (token1.title === token2.title) {
            $("input[name='amount_2']").val(amount);
        } else {
            $.ajax({
                type: 'GET',
                url: `/api/v1/convert/${token1.title}&${token2.title}&${amount}`,
                dataType: "json",

                success: function (response) {
                    $("input[name='amount_2']").val(response['price']);
                },
            });
        }
    } else {
        $("input[name='amount_2']").val('insert amount')
    }
})


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
    } else {
        $(this).preventDefault();
    }
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
$('.token_found').bind('click', function () {
    th = $(this);
    el = $(this).closest('.button-dropdown');
    img_link = th.children()[0].src
    img_title = th.children()[0].title

    text_content = $(this).children()[1].textContent;

    el.find('.choice-btn')[0].children[0].src = img_link
    el.find('.choice-btn')[0].children[0].title = img_title

    el.find('.choice-btn')[0].children[1].innerText = text_content
});


// sidebar active
function active() {
    li = document.querySelectorAll('.menu__item a');
    for (let i = 0; i < li.length; i++) {
        if (li[i].pathname == $(this)[0].location.pathname) {
            li[i].classList.add('menu__item--selected')
        } else {
            li[i].classList.remove('menu__item--selected')
        }
    }
}
