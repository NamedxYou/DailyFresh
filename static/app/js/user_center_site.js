
// 当用户点击添加新地址按钮的时候，将地址编辑文本框展示出来
function show_edit_area(){
    $('.common_title2').show();
    $('.site_con').show();
}

// 当用户点击使用选中地址的时候，获取用户选中的收货人的id
function submit_receiver(){
    var receiver_id = $('#receiver option:selected').val();
    location.href = '/app/place_order/?rec_id=' + receiver_id;
}

// 当用户提交新编辑的地址后，调用下面的函数
function new_adress(){
    var name = $("input[name='receiver']").val();
    var address = $('.form_group .site_area').val();
    var email_num = $("input[name='email_num']").val();
    var tel = $("input[name='phone_num']").val();
    data = {'name': name,'address': address, 'email_num': email_num, 'tel': tel};
    // $.post('/app/user_center_site/', data, function (data) {
    //     location.href = '/app/place_order/?rec_id=' + data.receiver_id;
    // })
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/app/user_center_site/',
        type: 'POST',
        dataType: 'json',
        data: data,
        headers: {'X-CSRFToken': csrf},
        success: function (data) {
            alert(data);
            location.href = '/app/place_order/?rec_id=' + data.receiver_id;
        },
        error: function (data) {
            alert('请求失败！');
        }
    })
}