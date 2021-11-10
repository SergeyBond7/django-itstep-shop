$(function(){$(".dropdown-toggle").dropdown('toggle');})

/* Messages */

$('.message').delay(1000).fadeIn(1500).delay(2000).fadeOut(1000);

$(document.all).ready(function() {
    var form = $('#form-buying-product');
    console.log(form);

    function basketUpdating(product_id, nmb, is_delete){
        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        var csrf_token = $('#form-buying-product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete) {
            data["is_delete"] = true
        }


        var url = form.attr("action");

       console.log(data);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data.products_total_nmb);
                if (data.products_total_nmb || data.products_total_nmb == 0) {
                    $('#basket_total_nmb').text("("+data.products_total_nmb+")");
                    console.log(data.products);
                    $('.basket-items ul').html("");
                    $.each(data.products, function(k, v){
                    $('.basket-items ul').append('<li>'+v.name +
                    '<button style="background-color: #ff0000;' +
                     'color: white; z-index: 99999 !important;" type="button"' +
                      'class="delete-item btn close" data-dismiss="modal" data-product_id="'+v.id+'"' +
                       'aria-label="Close">' +
                      '<span aria-hidden="true"><i class="bi bi-x"></i></span></button>'+
                      '</li><li class="divider"></li>');
                    })
                }
            },
            error: function(){
                console.log("error")
            }
        })

    }

    form.on('submit', function(e){
        e.preventDefault();
        console.log('123');
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn')
        var product_id = submit_btn.data("product_id")
        var product_name = submit_btn.data("name")
        var product_price = submit_btn.data("price")
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);

        basketUpdating(product_id, nmb, is_delete=false)

    });

    function showingBasket() {
        $('.basket-items').toggleClass('hidden');
    }

    $('.basket-container').on('click, hover', function(e){
        e.preventDefault();
        showingBasket;
    })

    $('.basket-container').click(function(){
        showingBasket();
    })

    $(document).on('click', '.delete-item', function(e){
        e.preventDefault();
        product_id = $(this).data("product_id");
        nmb = 0;
        basketUpdating(product_id, nmb, is_delete=true)
        showingBasket();
    })
});



/* Changing input value in Checkout */

jQuery('<div class="quantity-nav"><div class="quantity-button quantity-up">+</div><div class="quantity-button quantity-down">-</div></div>').insertAfter('.quantity input');
    jQuery('.quantity').each(function() {
      var spinner = jQuery(this),
        input = spinner.find('input[type="number"]'),
        btnUp = spinner.find('.quantity-up'),
        btnDown = spinner.find('.quantity-down'),
        min = input.attr('min'),
        max = input.attr('max');

      btnUp.click(function() {
        var oldValue = parseFloat(input.val());
        if (oldValue >= max) {
          var newVal = oldValue;
        } else {
          var newVal = oldValue + 1;
        }
        spinner.find("input").val(newVal);
        spinner.find("input").trigger("change");
      });

      btnDown.click(function() {
        var oldValue = parseFloat(input.val());
        if (oldValue <= min) {
          var newVal = oldValue;
        } else {
          var newVal = oldValue - 1;
        }
        spinner.find("input").val(newVal);
        spinner.find("input").trigger("change");
      });

/* Calculating Basket total price */

    function calculatingBasketAmount() {
        var total_order_amount = 0;
        $('.total-product-in-basket-amount').each(function(){
            total_order_amount = total_order_amount + parseFloat($(this).text());
        });

        $('#total_order_amount').text(total_order_amount.toFixed(2))
        console.log(total_order_amount);
    };

    $(document).on('change', ".product-in-basket-nmb", function() {
        var currentNmb = $(this).val();
        var currentDiv = $(this).closest('div[id]');
        console.log(currentDiv);
        var currentPrice = parseInt(currentDiv.find('.product-price').text());
        var totalAmount = parseFloat(currentNmb*currentPrice).toFixed(2);
        console.log(totalAmount);
        currentDiv.find(".total-product-in-basket-amount").text(totalAmount);
        calculatingBasketAmount();

    })

    calculatingBasketAmount();

});


/* Creating input phone type with country code */

$('document').ready(function() {
var phoneMask = IMask(
  document.getElementById('code'), {
    mask: '+{38} (000) 000-00-00'
  });
})


/* Pop-up */

function popupMessage() {

    var forms = document.getElementById('checkout-form');
    if(forms.checkValidity()){
        forms.submit();
        Swal.fire({
          position: 'inherit',
          icon: 'success',
          title: 'Ваш заказ успешно оформлен',
          showConfirmButton: false,
          timer: 1500
        }),window.location.href = 'list.html';
        }
}

/* Image carousel */

var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

/* Product tabs */

function openTab(evt, tabName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}
