from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from EXPANDABLE import model
from flask.ext.jsonpify import jsonpify
from flask.ext.restful.utils import cors

import jwt
import base64
import os


from flask import Flask, request, jsonify, _request_ctx_stack
from SECURITY import  auth

class Fedxshipment(Resource):
      def get(self):
         parser = reqparse.RequestParser()
         parser.add_argument('startdate', required=False)
         parser.add_argument('enddate', required=False)
         parser.add_argument('callback', required=False)
         #res=model.list()
         args = parser.parse_args()
         startdate = args['startdate']
         enddate = args['enddate']
         callback = args['callback']
         res=model.list(startdate, enddate)
         if (callback is None): return jsonify(Resault=res)
         if (callback is not None):
             resp = make_response(jsonpify(Resault=res))
             resp.headers['Access-Control-Allow-Origin'] = '*'
             return resp


class SODASH(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @auth.requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        res = model.sofiguers()
        return auth.makeresponseANDreturn(res)
        # resp = make_response(jsonpify(Resault=res))
        # resp.headers['Access-Control-Allow-Credentials'] = 'true'
        # resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
        # resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        # return resp

    def options(self):
      return auth.setheaderANDreturn()
        # resp = make_response()
        # resp.headers['Access-Control-Allow-Credentials'] = 'true'
        # resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
        # resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        # resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
        # return resp



class SODASHLIST(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @auth.requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('alert', required=False)
        parser.add_argument('number', required=False)
        parser.add_argument('version', required=False)
        args=parser.parse_args()
        alert = args['alert']
        number = args['number']
        version = args['version']
        res = model.sodashlist(alert, number, version)
        return auth.makeresponseANDreturn(res)
        # resp = make_response(jsonpify(Resault=res))
        # resp.headers['Access-Control-Allow-Credentials'] = 'true'
        # resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
        # resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        # return resp

    def options(self):
      return auth.setheaderANDreturn()
        # resp = make_response()
        # resp.headers['Access-Control-Allow-Credentials'] = 'true'
        # resp.headers['Access-Control-Allow-Headers'] = 'Authorization,Access-Control-Request-Headers'
        # resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        # resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
        # return resp

class SODASHBACKLOCKEDSHORT(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @auth.requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('version', required=False)
        parser.add_argument('callback', required=False)
        args=parser.parse_args()
        version = args['version']
        callback = args['callback']
        res = model.sodashbacklockedshort(version)
        return auth.makeresponseANDreturn(res)
        # resp = make_response(jsonpify(Resault=res))
        # return resp

    def options(self):
      return auth.setheaderANDreturn()
        # resp = make_response()
        # resp.headers['Access-Control-Allow-Credentials'] = 'true'
        # resp.headers['Access-Control-Allow-Headers'] = 'Authorization,Access-Control-Request-Headers'
        # resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        # resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
        # return resp


class SODASHSHIPMENTSHORT(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @auth.requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('version', required=False)
        parser.add_argument('callback', required=False)
        args=parser.parse_args()
        version = args['version']
        callback = args['callback']
        res = model.sodashshipmentshort(version)
        return auth.makeresponseANDreturn(res)
        # resp = make_response(jsonpify(Resault=res))
        # resp.headers['Access-Control-Allow-Origin'] = '*'
        # return resp

    def options(self):
      return auth.setheaderANDreturn()
        # resp = make_response()
        # resp.headers['Access-Control-Allow-Credentials'] = 'true'
        # resp.headers['Access-Control-Allow-Headers'] = 'Authorization,Access-Control-Request-Headers'
        # resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        # resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
        # return resp

class NOTIFICATIONS(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @auth.requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('alert', required=False)
        parser.add_argument('number', required=False)
        parser.add_argument('version', required=False)
        parser.add_argument('callback', required=False)
        args=parser.parse_args()
        alert = args['alert']
        number = args['number']
        version = args['version']
        callback = args['callback']
        res = model.notifications(alert, number, version)
        return auth.makeresponseANDreturn(res)
        # resp = make_response(jsonpify(Resault=res))
        # resp.headers['Access-Control-Allow-Credentials'] = 'true'
        # resp.headers['Access-Control-Allow-Headers'] = 'Authorization,Access-Control-Request-Headers'
        # resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        # return resp

    def options(self):
      return auth.setheaderANDreturn()
        # resp = make_response()
        # resp.headers['Access-Control-Allow-Credentials'] = 'true'
        # resp.headers['Access-Control-Allow-Headers'] = 'Authorization,Access-Control-Request-Headers'
        # resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        # resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
        # return resp

class NOTIFICATIONSBYSO(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @auth.requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('soid', required=False)
        parser.add_argument('alert', required=False)
        parser.add_argument('callback', required=False)
        args=parser.parse_args()
        soid = args['soid']
        alert = args['alert']
        callback = args['callback']
        res = model.notificationsbyso(soid, alert)
        return auth.makeresponseANDreturn(res)
        # resp = make_response(jsonpify(Resault=res))
        # return resp

    def options(self):
      return auth.setheaderANDreturn()
        # resp = make_response()
        # resp.headers['Access-Control-Allow-Credentials'] = 'true'
        # resp.headers['Access-Control-Allow-Headers'] = 'Authorization,Access-Control-Request-Headers'
        # resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        # resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
        # return resp

# class GRAPHS(Resource):
#     def get(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('gtype', required=False)
#         parser.add_argument('callback', required=False)
#         args=parser.parse_args()
#         gtype = args['gtype']
#         callback = args['callback']
#         res = model.graphs(gtype)
#         if (callback is None): return jsonify(Resault=res)
#         if (callback is not None):
#              resp = make_response(jsonpify(Resault=res))
#              resp.headers['Access-Control-Allow-Origin'] = '*'
#              return resp


class GRAPHS(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @auth.requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('gtype', required=False)
        parser.add_argument('callback', required=False)
        args=parser.parse_args()
        gtype = args['gtype']
        callback = args['callback']
        res = model.graphs(gtype)
        # resp = make_response(jsonpify(Resault=res))
        # return resp
        return auth.makeresponseANDreturn(res)
    def options(self):
      return auth.setheaderANDreturn()
        # resp = make_response()
        # resp.headers['Access-Control-Allow-Credentials'] = 'true'
        # resp.headers['Access-Control-Allow-Headers'] = 'Authorization,Access-Control-Request-Headers'
        # resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        # resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
        # return resp


class SPECIALNOTIFICATIONS(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @auth.requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('alert', required=False)
        parser.add_argument('callback', required=False)
        args=parser.parse_args()
        alert = args['alert']
        callback = args['callback']
        res = model.specialnotifications(alert)
        return auth.makeresponseANDreturn(res)
        # resp = make_response(jsonpify(Resault=res))
        # return resp

    def options(self):
      return auth.setheaderANDreturn()
        # resp = make_response()
        # resp.headers['Access-Control-Allow-Credentials'] = 'true'
        # resp.headers['Access-Control-Allow-Headers'] = 'Authorization,Access-Control-Request-Headers'
        # resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        # resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
        # return resp



class EEPROMLIST(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @auth.requires_auth
    def get(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument('alert', required=False)
        # parser.add_argument('callback', required=False)
        # args=parser.parse_args()
        # alert = args['alert']
        # callback = args['callback']
        res = model.eepromlist()
        return auth.makeresponseANDreturn(res)
        # resp = make_response(jsonpify(Resault=res))
        # return resp

    def options(self):
      return auth.setheaderANDreturn()


class EEPROMDETAIL(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @auth.requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('jobid', required=False)
        # parser.add_argument('callback', required=False)
        args=parser.parse_args()
        jobid = args['jobid']
        # callback = args['callback']
        res = model.eepromdetail(jobid)
        return auth.makeresponseANDreturn(res)
        # resp = make_response(jsonpify(Resault=res))
        # return resp

    def options(self):
      return auth.setheaderANDreturn()
        # resp = make_response()
        # resp.headers['Access-Control-Allow-Credentials'] = 'true'
        # resp.headers['Access-Control-Allow-Headers'] = 'Authorization,Access-Control-Request-Headers'
        # resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        # resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
        # return resp



class SO(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @auth.requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('soid', required=True)
        args=parser.parse_args()
        soid = args['soid']
        res = model.so(soid)
        return auth.makeresponseANDreturn(res)


    def options(self):
      return auth.setheaderANDreturn()


class SOPICKLIST(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @auth.requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('soid', required=True)
        parser.add_argument('beforedate', required=True)
        args=parser.parse_args()
        soid = args['soid']
        beforedate = args['beforedate']
        res = model.sopicklist(soid,beforedate)
        return auth.makeresponseANDreturn(res)


    def options(self):
      return auth.setheaderANDreturn()


class BOM(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @auth.requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('assemblyid', required=True)
        args=parser.parse_args()

        assemblyid = args['assemblyid']
        res = model.bom(assemblyid)
        return auth.makeresponseANDreturn(res)


    def options(self):
      return auth.setheaderANDreturn()

class SOASSEMBLY(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @auth.requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('assemblyid', required=True)
        args=parser.parse_args()
        assemblyid = args['assemblyid']
        res = model.soassembly(assemblyid)
        return auth.makeresponseANDreturn(res)
        try:
            for item in res:
                print(item)
                print(item['SO_LIST'])
                res2 = model.so(item['SO_LIST'])
                return auth.makeresponseANDreturn(res2)


        except Exception as e:
             print (e)




    def options(self):
      return auth.setheaderANDreturn()


