var koa = require('koa');
var mount = require('koa-mount');
var bodyParser = require('koa-body-parser');
var program = require('commander');

program
    .version('1.0.0')
    .description('Flink your life!')
    .option('-e, --env', 'Specify db: [development]|test|production')
    .parse(process.argv);

global.db = program.env
&& program.args.length
&& ['production', 'development', 'test'].indexOf(program.args) > -1 ? program.args[0] : 'development';

var router = require("./utils/router");
var ports = require("./config/ports");

var app = koa();
var api = router.api;

app.use(bodyParser());
app.use(mount('/api', api.middleware()));

console.log("Flink is listening on 0.0.0.0:" + ports.app_port)
app.listen(ports.app_port);
