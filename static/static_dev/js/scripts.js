$(document).ready(function(){
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit',function(e){
        e.preventDefault();
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn')
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("name");
        var product_price = submit_btn.data("price");
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);

        $('.basket-items ul').append('<li>' + product_name + ', '+ nmb + 'шт. по '+ product_price + ' руб   ' + 
        '<a class="delete-item" href="">x</a>' +
        '</li>');
    });

    function showingBasket(){
        $('.basket-items').toggleClass('hidden');
    };

    $('.basket-container').on('click', function(e){
        e.preventDefault(); 
        showingBasket();
    });

    $('.basket-container').mouseover(function(e){
        e.preventDefault(); 
        showingBasket();
    });

    $('.basket-container').mouseout(function(e){
        e.preventDefault(); 
        showingBasket();
    });

    $(document).on('click', '.delete-item', function(e){
        e.preventDefault(); 
        $(this).closest('li').remove();
    })
});