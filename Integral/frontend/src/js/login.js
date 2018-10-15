var loginmain = new Vue({
    el: "#loginId",
    data: {
        errorInfo: "",
        errorHide: "none",
        object: [],
        username: "",
        password: "",
        Error: "",
    },
    methods: {
        login: function(){
            const that = this
            console.log('login')
            axios.post('/login', {
                "username": username.value,
                "password": password.value
            })
            .then(function (response){
                ret = response.data;
                if(ret['code'] != 0){
                    console.log(ret)
                    that.Error = ret['msg']
                    that.errorHide = "block"
                }else{
                    that.errorHide = "none"
                    window.location.replace("/index")
                }
            })
        }
    }
})
