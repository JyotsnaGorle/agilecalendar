var app = require('../index.js').app;
var request = require('co-supertest').agent(app.listen(8000));
var expect = require('chai').expect;

describe('GET /api/status', function () {
    it('should return status as {"status":"Flink says Hallo!"}', function *() {
        var res = yield request.get('/api/status').expect(200).end();

        expect(JSON.parse(res.text)).to.deep.equal({
            status: "Flink says Hallo!"
        });
    });
});
