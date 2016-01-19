'use strict';

module.exports = {
    up: function (queryInterface, Sequelize) {
        return queryInterface.bulkInsert('Users', [{
            name: 'Walter White',
            email: 'imtheonewhoknocks@amc.com',
            username: 'heisenberg',
            password: 'saymyname',
            createdAt: Date.now(),
            updatedAt: Date.now()
        }], {});
    },

    down: function (queryInterface, Sequelize) {
         return queryInterface.bulkDelete('Users', null, {});
    }
};
