var User = require('../utils/model_getter').get('user');

module.exports.putUser = function* (next) {
    var username = this.params.username;
    var name = this.request.body.name;
    var email = this.request.body.email;
    var password = this.request.body.password;

    var success = function() {
        this.type = 'json';
        this.status = 200;
        this.body = {
            'status': 'Ok!'
        };
    }.bind(this);

    var failure = function () {
        this.type = 'json';
        this.status = 409;
        this.body = {
            'status': 'Username exists'
        };
    }.bind(this);

    yield User.create({
        name: name,
        email: email,
        username: username,
        password: password
    }).then(function() {
        success();
    }, function() {
        failure();
    });
};
