var BCrypt = require('bcrypt');

var settings = require('../config/settings');

module.exports.hash = function (password) {
    var salt = BCrypt.genSaltSync(settings.HASH_SALT_WORK_FACTOR);
    return BCrypt.hashSync(password, salt);
};

module.exports.matchPassword = function (password, hash) {
    return BCrypt.compareSync(password, hash);
};
