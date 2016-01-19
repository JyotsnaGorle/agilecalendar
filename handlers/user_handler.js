var User = require('../utils/model_getter').get('user');
var responses = require('../utils/responses');
var flinkCrypto = require('../utils/flink_crypto');

module.exports.getUser = function* (next) {
    var succeeded = responses.success.bind(this);
    var failed = responses.failure.bind(this);

    yield User.find({
        attributes: [
            'name',
            'email'
        ],
        where: {
            username: this.params.username
        }
    }).then(function (user) {
        if (user)
            succeeded(user);
        else
            failed({
                response: "No such user found"
            }, 404);
    });
};

module.exports.putUser = function* (next) {
    var succeeded = responses.success.bind(this);
    var failed = responses.failure.bind(this);

    yield User.create({
        name: this.request.body.name,
        email: this.request.body.email,
        username: this.params.username,
        password: flinkCrypto.hash(this.request.body.password)
    }).then(function () {
        succeeded();
    }, function () {
        failed({
            response: "User already exists"
        }, 409);
    });
};

module.exports.updateUser = function* (next) {
    var succeeded = responses.success.bind(this);
    var failed = responses.failure.bind(this);

    var updateFields = {};
    Object.keys(this.request.body).forEach(function(key) {
        updateFields[key] = this.request.body[key];
    }.bind(this));

    yield User.update(updateFields, {
        where: {
            username: this.params.username
        }
    }).then(function (done) {
        if (done[0])
            succeeded();
        else
            failed({
                response: "No such user found"
            }, 404);
    });
};

module.exports.deleteUser = function* (next) {
    var succeeded = responses.success.bind(this);
    var failed = responses.failure.bind(this);

    yield User.destroy({
        where: {
            username: this.params.username
        }
    }).then(function (done) {
        if (done)
            succeeded();
        else
            failed({
                response: "No such user found"
            }, 404);
    });
};
