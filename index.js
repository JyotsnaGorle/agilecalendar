var koa = require('koa');
var mount = require('koa-mount');
var bodyParser = require('koa-body-parser');
var program = require('commander');

program
    .version('1.0.0')
    .description('Flink your life!')
    .option('-e, --env', 'Specify running environment: [development]|test|production')
    .parse(process.argv);

global.appMode = program.env
&& program.args.length
&& ['production', 'development', 'test'].indexOf(program.args) > -1 ? program.args[0] : 'development';

console.log(global.appMode);
process.exit();

var router = require("./utils/router");
var ports = require("./config/ports");

var app = koa();
var api = router.api;

app.use(bodyParser());
app.use(mount('/api', api.middleware()));

app.listen(ports.app_port);
