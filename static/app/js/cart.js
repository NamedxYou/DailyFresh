
// 拿到从前端获取的 cart_details 数据
$.get('/app/cart_details/',function (data) {
    console.log(data);
    if(data.code == '200'){
        var count = data.cart_details.length;
        $('.total_count > em').text(count);
        $('.cartIsNone').hide();
    //    计算出所有商品的总价和数量，并放置到相应的标签中
        var total_prices = 0;
        var amount = 0;
        //商品总价等于各个商品总价之和
        for(var i=0; i < data.cart_details.length; i += 1){
            var cart = data.cart_details[i];
            total_prices += parseFloat(cart.sum_price);
        }
        total_prices = parseFloat(total_prices).toFixed(2);
        // 这里的商品数量是以商品种类计算的，不是以商品的数量计算的
        amount = data.cart_details.length;
        // 找到对应标签并将计算的结果填充
        $('#total_prices').text(total_prices);
        $('#amount').text(amount);
    }else{
        $('.total_count').hide();
        $('.cartIsNone').show();
    }
});

// 增减商品数量与购物车数据库数据相一致
function add_goods(id){
    // 拿到当前购物车的商品数量
    var goods_num = parseInt($('#num_show_' + id).val());
    // alert(goods_num);
    goods_num += 1;
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/app/add_goods/',
        type: 'POST',
        dataType: 'json',
        // 返回修改后的商品数量，已经对应的购物车数据id
        data: {'goods_num': goods_num, 'id': id},
        headers: {'X-CSRFToken': csrf},
        success: function (data) {
            if(data.code == '200'){
                // $('#num_show_' + id).val(goods_num);
                // $('#sum_price').val(data.sum_price);
                location.reload();
            }
        },
        error: function (data) {
            alert('增加失败！');
        }
    });
}

// 减少商品数量与购物车数据保持一致
function minus_goods(id){
    // 拿到当前购物车的商品数量
    var goods_num = parseInt($('#num_show_' + id).val());
    // alert(goods_num);
    if(goods_num <= 1){
        goods_num += 0
    }else{
        goods_num -= 1;
    }
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/app/minus_goods/',
        type: 'POST',
        dataType: 'json',
        // 返回修改后的商品数量，已经对应的购物车数据id
        data: {'goods_num': goods_num, 'id': id},
        headers: {'X-CSRFToken': csrf},
        success: function (data) {
            if(data.code == '200'){
                // $('#num_show_' + id).val(goods_num);
                // $('#sum_price').val(data.sum_price);
                location.reload();
            }
        },
        error: function (data) {
            alert('减少失败！');
        }
    });
}




// function show_msg(){
//     var csrf = $('input[name="csrfmiddlewaretoken"]').val();
//     $.ajax({
//         url: '/user/register/',
//         type: 'POST',
//         dataType: 'json',
//         data: {},
//         headers: {'X-CSRFToken': csrf},
//         success: function (data) {
//             $('#username_repetition').val(data.msg);
//         },
//         error: function (data) {
//             // alert('请求失败！');
//         }
//     });
// }


