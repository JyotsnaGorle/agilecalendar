module.exports.success = function (response, status) {
    this.type = 'json';
    this.status = status || 200;
    this.body = response || {
            response: "Ok"
        };
};

module.exports.failure = function (response, status) {
    this.type = 'json';
    this.status = status;
    this.body = response;
};
