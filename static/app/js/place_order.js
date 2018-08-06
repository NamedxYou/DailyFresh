
$('#order_btn').click(function() {
    localStorage.setItem('order_finish',2);

    $('.popup_con').fadeIn('fast', function() {

        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){
                window.location.href = '/app/user_center_order/';
            });
        },2000);
    });
});

$.get('/app/place_order_data/', function (data) {
    // 设定运费为固定十元
    var freight = 10;
   if(data.code == '200'){
       var total_prices = 0;
       var amount = data.cart_details.length;
       for(var i=0; i < amount; i += 1){
           var cart = data.cart_details[i];
           total_prices += parseFloat(cart.sum_price);
       }
       total_prices = total_prices.toFixed(2);
       var total = (parseFloat(total_prices) + parseFloat(freight)).toFixed(2);
       $('#amount').text(amount);
       $('#total_prices').text(total_prices);
       $('#freight').text(freight.toFixed(2));
       $('#total').text(total);
   }else{
       alert('请求失败！');
   }
});