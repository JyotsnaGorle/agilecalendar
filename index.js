var koa = require('koa');
var router = require("./app/router");
var ports = require("./config/ports");
var mount = require('koa-mount');

var app = koa();
var api = router.api;

app.use(mount('/api', api.middleware()));

app.listen(ports.app_port);
