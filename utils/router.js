var Router = require('koa-router');

var userHandler = require('../handlers/user_handler');

var api = new Router();

var status = function* (next) {
    this.type = 'json';
    this.status = 200;
    this.body = {
        'status': 'Flink says Hallo!'
    };
};

api.get('/user/:username', userHandler.getUser);
api.put('/user/:username', userHandler.putUser);
api.get('/status', status);

module.exports.api = api;
