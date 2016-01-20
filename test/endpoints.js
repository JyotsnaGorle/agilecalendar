var app = require('../index.js').app;
var request = require('co-supertest').agent(app.listen(8000));
var expect = require('chai').expect;

var User = require('../utils/model_getter').get('user');
var flinkCrypto = require('../utils/flink_crypto');

describe('GET /api/status', function () {
    it('should return status as {"status":"Flink says Hallo!"}', function* () {
        var res = yield request.get('/api/status').expect(200).end();

        expect(JSON.parse(res.text)).to.deep.equal({
            status: "Flink says Hallo!"
        });
    });
});

describe('GET /api/user/:username', function () {
    beforeEach(function() {
        User.destroy({
            where: {
                username: 'heisenberg'
            }
        }).then(function () {
            User.create({
                name: 'Walter White',
                email: 'imtheonewhoknocks@amc.com',
                username: 'heisenberg',
                password: flinkCrypto.hash('saymyname')
            });
        });
    });

    it('should get user details for a given username', function* () {
        var res = yield request.get('/api/user/heisenberg').expect(200).end();

        expect(JSON.parse(res.text)).to.deep.equal({
            name: "Walter White",
            email: "imtheonewhoknocks@amc.com"
        });
    });

    it('should respond 404 for a non existent username', function* () {
        var res = yield request.get('/api/user/non_user').expect(404).end();

        expect(JSON.parse(res.text)).to.deep.equal({
            response: "No such user found"
        });
    });
});
