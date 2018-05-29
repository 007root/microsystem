/**
 * Created by shuai on 5/26/2018.
 */


var addIntegral = new Vue({
    el: "#addError",
    data: {
        errorInfo: "",
        hideError: "none",
        hideName: "none"
    },
    methods: {
        addjifen: function(){
            var _this = this
            var phone = $('#addPhone').val()
            var price = $('#addPrice').val()
            var name = $('#addName').val()
            axios.post('/manage/integral/add', {
            phone: phone,
            name: name,
            price: price
            })
            .then(function (response) {
                ret = response.data;
                if (ret['code'] == 404){
                    _this.hideName = "inline-block"
                }
                if (ret['code'] == 503){
                    window.location.replace('/')
                }
                if (ret['code'] == 0){
                    _this.hideError = 'none'
                    alert('积分录入成功,累计积分: ' + ret['msg'])
                    location.reload()
                } else {
                    _this.errorInfo = ret['msg']
                    _this.hideError = 'block'
                }
            })
            .catch(function (error) {
                console.log(error);
            });
        }
    }
})


var costIngetral = new Vue({
    el: "#costError",
    data: {
        errorInfo: "",
        hideError: "none",
    },
    methods: {
        convertintegral: function(){
            var _this = this
            var phone = $('#costPhone').val()
            var cost = $('#cost').val()
            axios.post('/manage/integral/cost', {
            phone: phone,
            cost: cost
            })
            .then(function (response) {
                ret = response.data;
                if (ret['code'] == 503){
                    window.location.replace('/')
                }
                if (ret['code'] == 0){
                    _this.hideError = 'none'
                    alert('账户剩余积分: ' + ret['msg'])
                    location.reload()
                } else {
                    _this.errorInfo = ret['msg']
                    _this.hideError = 'block'
                }
            })
            .catch(function (error) {
                console.log(error);
            });
        }
    }
})


var saleExchange = new Vue({
    el: "#exchangeError",
    data: {
        errorInfo: "",
        hideError: "none",
    },
    methods: {
        saleexchange: function(){
            var _this = this
            var phone = $('#exchangePhone').val()
            var ori_price = $('#oriPrice').val()
            var cur_price = $('#curPrice').val()
            axios.post('/manage/sale/exchange', {
            phone: phone,
            ori_price: ori_price,
            cur_price: cur_price
            })
            .then(function (response) {
                ret = response.data;
                if (ret['code'] == 503){
                    window.location.replace('/')
                }
                if (ret['code'] == 0){
                    _this.hideError = 'none'
                    alert('本次产生积分: ' + ret['msg'][0] +
                          ', 账户剩余积分: ' + ret['msg'][1])
                    location.reload()
                } else {
                    _this.errorInfo = ret['msg']
                    _this.hideError = 'block'
                }
            })
            .catch(function (error) {
                console.log(error);
            });
        }
    }
})


var saleBack = new Vue({
    el: "#backError",
    data: {
        errorInfo: "",
        hideError: "none",
    },
    methods: {
        saleback: function(){
            var _this = this
            var phone = $('#backPhone').val()
            var price = $('#backPrice').val()
            axios.post('/manage/sale/back', {
            phone: phone,
            price: price,
            })
            .then(function (response) {
                ret = response.data;
                if (ret['code'] == 503){
                    window.location.replace('/')
                }
                if (ret['code'] == 0){
                    _this.hideError = 'none'
                    alert('本次扣除积分: ' + ret['msg'][0] +
                          ', 账户剩余积分: ' + ret['msg'][1])
                    location.reload()
                } else {
                    _this.errorInfo = ret['msg']
                    _this.hideError = 'block'
                }
            })
            .catch(function (error) {
                console.log(error);
            });
        }
    }
})


var selectInfo = new Vue({
    el: "#selectError",
    data: {
        errorInfo: "",
        hideError: "none",
        object: [],
    },
    methods: {
        selectinfo: function(){
            var _this = this
            var phone = $('#selectPhone').val()
            axios.post('/manage/integral/info', {
            phone: phone,
            })
            .then(function (response) {
                ret = response.data;
                if (ret['code'] == 503){
                    window.location.replace('/')
                }
                if (ret['code'] == 0){
                    _this.object.push(ret['msg'])
                    _this.hideError = 'none'
                } else {
                    _this.errorInfo = ret['msg']
                    _this.hideError = 'block'
                }
            })
            .catch(function (error) {
                console.log(error);
            });
        }
    }
})


function logout(){
    axios.get('/logout')
    .then(function (res){
        window.location.replace('/')
    })    
}
