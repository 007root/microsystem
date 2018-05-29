function register() {
    var singupObj = $('#signupform')
    var name = singupObj.find('input[name="username"]').val();
    var password = singupObj.find('input[name="password"]').val();
    $.ajax({
        url: "/register",
        data: JSON.stringify({
                    name:name, 
                    password:password}),
        traditional: true,
        type: "POST",
        success:function(callback) {
            if (callback["code"] == 1) {
                var st = $("#signupalert").css("display")
                if (st == "none") {
                    $("#signupalert p").text(callback['msg']);
                    $("#signupalert").css("display", "block");
                } else {
                    $("#signupalert p").text(callback['msg']);    
                }
            } else {
                $("#signupalert").css("display", "none");
            }
        }
    });
}


function login() {
    var singupObj = $('#loginform')
    var name = singupObj.find('input[name="username"]').val();
    var password = singupObj.find('input[name="password"]').val();
    $.ajax({
        url: "/login",
        data: JSON.stringify({
                    name:name, 
                    password:password}),
        traditional: true,
        type: "POST",
        success:function(callback) {
            if (callback["code"] == 1) {
                var st = $("#signupalert").css("display")
                if (st == "none") {
                    $("#loginalert p").text(callback['msg']);
                    $("#loginalert").css("display", "block");
                } else {
                    $("#loginalert p").text(callback['msg']);    
                }
            } else {
                $("#loginalert").css("display", "none");
                window.location.replace("/index")
            }
        }
    });
}


