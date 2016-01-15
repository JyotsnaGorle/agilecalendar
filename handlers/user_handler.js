var User = require('../utils/model_getter').get('user');
var responses = require('../utils/responses');

module.exports.getUser = function* (next) {
    var username = this.params.username;
    var onSuccess = responses.success.bind(this);
    var onFailure = responses.failure.bind(this);

    yield User.find({
        attributes: [
            'name',
            'email'
        ],
        where: {
            username: username
        }
    }).then(function (user) {
        if (user)
            onSuccess(user);
        else
            onFailure({
                response: "No such user found"
            }, 404);
    });
};

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
        onFailure({
            response: "User already exists"
        }, 409);
    });
};
