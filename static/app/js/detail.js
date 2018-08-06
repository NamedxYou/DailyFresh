
// 给页面的 + 绑定函数，点击之后商品 显示数量 增加，并且 总价 更新
$('#add_num').click(function () {
    // 拿到商品 当前数量 并将获得的字符串转换成 整型
    var num = parseInt($('#num_show').val());
    num += 1;
    // 将处理后的数量重新赋值给标签
    $('#num_show').val(num);
    // 拿到商品的单价并处理成 浮点数
    var price = parseFloat($('#price').text());
    // 计算总价并将结果处理成包含两位小数的浮点数。
    sum_price = (price * num).toFixed(2);
    // 将计算的总价填充到标签中
    $('#sum_price').text(sum_price);
});

// 给商品的数量输入框绑定状态改变函数， 当输入数字之后自动计算商品价格，并且不允许输入正整数以外的信息
// 拿到商品原有数量，当输入不合乎要求的时候，返回原有值
// onkeyup="this.value=this.value.replace(/\D/g,'')"
// onafterpaste="this.value=this.value.replace(/\D/g,'')"
// 给input标签绑定上面两个属性，可以将输入的或黏贴的非数字字符自动去掉。
var goods_num = $('#num_show').text();
$('#num_show').change(function () {
    // 当状态改变的时候，拿到输入值
    var input_val = parseInt($('#num_show').val());
    if(input_val){
        var price = parseFloat($('#price').text());
        var sum_price = (price * input_val).toFixed(2);
        $('#sum_price').text(sum_price);
    }else{
        $('#num_show').val(goods_num);
    }
});

// 给页面的 - 绑定函数，点击之后商品 显示数量 减少，并且 总价 更新
$('#minus_num').click(function () {
    var num = parseInt($('#num_show').val());
    if(num <= 1){
        num = num
    }else{
        num -= 1
    }
    $('#num_show').val(num);
    var price = parseFloat($('#price').text());
    sum_price = (price * num).toFixed(2);
    $('#sum_price').text(sum_price);
});

var $add_x = $('#add_cart').offset().top;
var $add_y = $('#add_cart').offset().left;

var $to_x = $('#show_count').offset().top;
var $to_y = $('#show_count').offset().left;

// 添加购物车会有一个弹射效果， 并且购物车订单数量也会发生改变
$(".add_jump").css({'left':$add_y+80,'top':$add_x+10,'display':'block'});
var times_control = 0;
$('#add_cart').click(function(){
    if(times_control <1){
       $(".add_jump").stop().animate({
        'left': $to_y+7,
        'top': $to_x+7},
        "fast", function() {
            $(".add_jump").fadeOut('fast',function(){
                var cart_count_old =  parseInt($('#show_count').text());
                cart_count_new = cart_count_old + 1;
                $('#show_count').html(cart_count_new);
                // 在添加购物车的同时将商品的id、商品的数量发送给购物车
                // 将detail页面获取的信息传递给 /app/cart/视图函数
                var goods_num = parseInt($('#num_show').val());
                var goods_id = parseInt(location.search.split('=')[1]);
                var csrf = $('input[name="csrfmiddlewaretoken"]').val();
                $.ajax({
                    url: '/app/cart/',
                    type: 'POST',
                    dataType: 'json',
                    data: {'goods_num': goods_num, 'goods_id': goods_id},
                    headers: {'X-CSRFToken': csrf},
                    success: function (data) {
                    // 这里不需要做处理。
                    },
                    error: function (data) {
                        alert('请求失败！')
                    }
                });
            });
        });
       times_control += 1;
    }else{
        $('#show_msg').show();
        // 引入时间睡眠功能，时间(2s)过后再将 show_msg 隐藏,并且恢复购物车添加功能，
        // 这样做的目的是提醒用户并避免客户不停的点击添加购物车
        setTimeout("$('#show_msg').hide();times_control = 0",2000);
        // var now = new Date();
	    // var exitTime = now.getTime() + 10;
	    // while (true) {
		 //    now = new Date();
		 //    if (now.getTime() > exitTime){
		 //        $('#show_msg').text();
         //    }
		 //    return;
	    // }
    }
});