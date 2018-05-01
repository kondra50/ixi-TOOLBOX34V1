from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from EXPANDABLE import model
from flask.ext.jsonpify import jsonpify
from flask.ext.restful.utils import cors

import jwt
import base64
import os

from functools import wraps
from flask import Flask, request, jsonify, _request_ctx_stack
#from authorization_helper import requires_auth

from flask_cors import CORS, cross_origin

from werkzeug.local import LocalProxy
# from app import  api


def authenticate(error):
  resp = jsonify(error)

  resp.status_code = 401
  resp.headers['Access-Control-Allow-Credentials'] = 'true'
  resp.headers['Access-Control-Allow-Headers'] = ' Authorization'
  resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
  resp.headers['Access-Control-Allow-Origin'] = '*'

  return resp

def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.headers.get('Authorization', None)
    if not auth:
      return authenticate({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'})

    parts = auth.split()

    if parts[0].lower() != 'bearer':
      return {'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'}
    elif len(parts) == 1:
      return {'code': 'invalid_header', 'description': 'Token not found'}
    elif len(parts) > 2:
      return {'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}

    token = parts[1]
    try:
        payload = jwt.decode(
            token,
            base64.b64decode('cdcphbR1OlchK2ELr7Uyqb_MNVDJVG_Kr3aY5WiBEUqAHEdCvtbq5iz3drsa1xv8'.replace("_","/").replace("-","+")),
            audience='rIkEgfZmLrVZX1flqjGlkZtizsYXoU1P'
        )
    except jwt.ExpiredSignature:
        return authenticate({'code': 'token_expired', 'description': 'token is expired'})
    except jwt.InvalidAudienceError:
        return authenticate({'code': 'invalid_audience', 'description': 'incorrect audience, expected: rIkEgfZmLrVZX1flqjGlkZtizsYXoU1P'})
    except jwt.DecodeError:
        return authenticate({'code': 'token_invalid_signature', 'description': 'token signature is invalid'})

    _request_ctx_stack.top.current_user = user = payload
    return f(*args, **kwargs)

  return decorated

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
    @requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('callback', required=False)
        args=parser.parse_args()
        callback = args['callback']
        res = model.sofiguers()
        resp = make_response(jsonpify(Resault=res))
        return resp

    def options(self):
        resp = make_response()
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        resp.headers['Access-Control-Allow-Headers'] = 'Authorization'
        resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
        # resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp



class SODASHLIST(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @requires_auth
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
        res = model.sodashlist(alert, number, version)
        resp = make_response(jsonpify(Resault=res))
        return resp

    def options(self):
        resp = make_response()
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        resp.headers['Access-Control-Allow-Headers'] = 'Authorization'
        resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
        # resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

class SODASHBACKLOCKEDSHORT(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('version', required=False)
        parser.add_argument('callback', required=False)
        args=parser.parse_args()
        version = args['version']
        callback = args['callback']
        res = model.sodashbacklockedshort(version)
        resp = make_response(jsonpify(Resault=res))
        return resp

    def options(self):
        resp = make_response()
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        resp.headers['Access-Control-Allow-Headers'] = 'Authorization'
        resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
        return resp


class SODASHSHIPMENTSHORT(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('version', required=False)
        parser.add_argument('callback', required=False)
        args=parser.parse_args()
        version = args['version']
        callback = args['callback']
        res = model.sodashshipmentshort(version)
        resp = make_response(jsonpify(Resault=res))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    def options(self):
        resp = make_response()
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        resp.headers['Access-Control-Allow-Headers'] = 'Authorization'
        resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
        return resp

class NOTIFICATIONS(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @requires_auth
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
        resp = make_response(jsonpify(Resault=res))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    def options(self):
        resp = make_response()
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        resp.headers['Access-Control-Allow-Headers'] = 'Authorization'
        resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
        return resp

class NOTIFICATIONSBYSO(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @requires_auth
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
        resp = make_response(jsonpify(Resault=res))
        return resp

    def options(self):
        resp = make_response()
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        resp.headers['Access-Control-Allow-Headers'] = 'Authorization'
        resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
        # resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

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
    @requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('gtype', required=False)
        parser.add_argument('callback', required=False)
        args=parser.parse_args()
        gtype = args['gtype']
        callback = args['callback']
        res = model.graphs(gtype)
        resp = make_response(jsonpify(Resault=res))
        return resp
    def options(self):
        resp = make_response()
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        resp.headers['Access-Control-Allow-Headers'] = 'Authorization'
        resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
        return resp


class SPECIALNOTIFICATIONS(Resource):
    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('alert', required=False)
        parser.add_argument('callback', required=False)
        args=parser.parse_args()
        alert = args['alert']
        callback = args['callback']
        res = model.specialnotifications(alert)
        resp = make_response(jsonpify(Resault=res))
        return resp

    def options(self):
        resp = make_response()
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        resp.headers['Access-Control-Allow-Headers'] = 'Authorization,Access-Control-Request-Headers'
        resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
        # resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp




# @app.before_request
# def option_autoreply():
#     """ Always reply 200 on OPTIONS request """
#
#     if request.method == 'OPTIONS':
#         resp = app.make_default_options_response()
#
#         headers = None
#         if 'ACCESS_CONTROL_REQUEST_HEADERS' in request.headers:
#             headers = request.headers['ACCESS_CONTROL_REQUEST_HEADERS']
#
#         h = resp.headers
#
#         # Allow the origin which made the XHR
#         h['Access-Control-Allow-Origin'] = request.headers['Origin']
#         # Allow the actual method
#         h['Access-Control-Allow-Methods'] = request.headers['Access-Control-Request-Method']
#         # Allow for 10 seconds
#         h['Access-Control-Max-Age'] = "10"
#
#         # We also keep current headers
#         if headers is not None:
#             h['Access-Control-Allow-Headers'] = headers
#
#         return resp
#
#
# @app.after_request
# def set_allow_origin(resp):
#     """ Set origin for GET, POST, PUT, DELETE requests """
#
#     h = resp.headers
#
#     # Allow crossdomain for other HTTP Verbs
#     if request.method != 'OPTIONS' and 'Origin' in request.headers:
#         h['Access-Control-Allow-Origin'] = request.headers['Origin']
#
#
#     return resp


def setheaderANDreturn():

    resp = make_response()
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    resp.headers['Access-Control-Allow-Headers'] = 'Authorization,Access-Control-Request-Headers'
    resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
    return resp