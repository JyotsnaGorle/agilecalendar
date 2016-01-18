var Sequelize = require('sequelize');

var dbConfig = require('../config/db')[global.db];

var orm = new Sequelize(dbConfig.name, dbConfig.username, dbConfig.password, {
    host: dbConfig.host,
    dialect: dbConfig.dialect,
    storage: dbConfig.storage,
    logging: global.db === 'development',
    omitNull: true
});

module.exports.get = function (model) {
    return require('../models/' + model)(orm, Sequelize[dbConfig.dialect]);
};
