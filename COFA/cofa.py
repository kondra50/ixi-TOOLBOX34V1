from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from COFA import model
from flask.ext.jsonpify import jsonpify
from SECURITY import auth
from flask.ext.restful.utils import cors

class list(Resource):

    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @auth.requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        res=model.list()
        return auth.makeresponseANDreturn(res)

    def options(self):
      return auth.setheaderANDreturn()



class Report(Resource):

    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @auth.requires_auth
    def get(self):
         parser = reqparse.RequestParser()
         parser.add_argument('mpartid', required=True)
         parser.add_argument('mlotid', required=True)
         res = model.list()
         args = parser.parse_args()
         mpartid = args['mpartid']
         mlotid = args['mlotid']
         res = model.report(mpartid, mlotid)
         return auth.makeresponseANDreturn(res)


    def options(self):
        return auth.setheaderANDreturn()