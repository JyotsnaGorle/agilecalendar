var Sequelize = require('sequelize');

var dbConfig = require('../config/db')[global.appMode];

var orm = new Sequelize(dbConfig.name, dbConfig.username, dbConfig.password, {
    host: dbConfig.host,
    dialect: dbConfig.dialect,
    storage: dbConfig.storage,
    logging: () => global.appMode === 'development'
});

module.exports.get = function (model) {
    return require('../models/' + model)(orm, Sequelize[dbConfig.dialect]);
};
