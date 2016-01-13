var Router = require('koa-router');

var api = new Router();

var status = function* (next) {
    this.type = 'json';
    this.status = 200;
    this.body = {
        'status': 'Flink says Hallo!'
    };
};

api.get('/status', status);

module.exports.api = api;
