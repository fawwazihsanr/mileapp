// import {describe} from "mocha";

const chai = require('chai')
const chaiHttpRequest = require('chai-http')
const expect = chai.expect
const baseUrl = "http://localhost:8000/"

const {
    dataToSend,
    updateData,
    updateSomeColumn,
} = require('./strings')

chai.use(chaiHttpRequest)
describe('mileapp rest api unit test', function () {
    let orderId = 4;
    it('get all packages', (done) => {
        chai.request(baseUrl)
            .get('api/package')
            .end(function (err, res) {
                expect(res).to.have.status(200)
                done()
            })
    })

    it('get a package', (done) => {
        chai.request(baseUrl)
            .get(`api/package/${orderId}`)
            .end((err, res)=>{
                expect(res).to.have.status(200)
                expect(res.body).to.have.property("data")
                done()
            })
    })

    it('create a package', (done) => {
        chai.request(baseUrl)
            .post('api/package')
            .send(dataToSend)
            .end((err, res)=>{
                expect(res).to.have.status(201)
                expect(res.body.message).to.equal('Created!')
                done()
            })
    })

    it('update a package (PUT)', (done) => {
        chai.request(baseUrl)
            .put(`api/package/${orderId}`)
            .send(updateData)
            .end((err, res) => {
                expect(res).to.have.status(201)
                expect(res.body.message).to.equal('Created!')
                done()
            })
    })

    it('update a package based on column (PATCH)', (done) => {
        chai.request(baseUrl)
            .put(`api/package/${orderId}`)
            .send(updateSomeColumn)
            .end((err, res) => {
                expect(res).to.have.status(201)
                expect(res.body.message).to.equal('Created!')
                done()
            })
    })

    it('delete a package', (done) => {
        chai.request(baseUrl)
            .delete(`api/package/${orderId}`)
            .end((err, res) => {
                expect(res).to.have.status(204)
                expect(res.body.message).to.equal('deleted')
                done()
            })
    })
})

