var User = require('../utils/model_getter').get('user');
var responses = require('../utils/responses');

module.exports.putUser = function* (next) {
    var username = this.params.username;
    var name = this.request.body.name;
    var email = this.request.body.email;
    var password = this.request.body.password;
    var onSuccess = responses.success.bind(this);
    var onFailure = responses.failure.bind(this);

    yield User.create({
        name: name,
        email: email,
        username: username,
        password: password
    }).then(function () {
        onSuccess();
    }, function () {
        onFailure(409, "User already exists");
    });
};
