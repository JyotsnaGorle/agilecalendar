module.exports.success = function (status, message) {
    this.type = 'json';
    this.status = status || 200;
    this.body = {
        'status': message || "Ok"
    };
};

module.exports.failure = function (status, message) {
    this.type = 'json';
    this.status = status;
    this.body = {
        'status': message
    };
};
