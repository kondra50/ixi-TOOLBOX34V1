import jwt
import base64
import os

from functools import wraps
from flask import Flask, request, jsonify, _request_ctx_stack,make_response
from werkzeug.local import LocalProxy
# from flask.ext.cors import cross_origin


app = Flask(__name__)
# Authentication annotation
current_user = LocalProxy(lambda: _request_ctx_stack.top.current_user)

# Authentication attribute/annotation
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


def setheaderANDreturn():

    resp = make_response()
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    resp.headers['Access-Control-Allow-Headers'] = 'Authorization,Access-Control-Request-Headers'
    resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    resp.headers['Access-Control-Allow-Origin'] = 'http://192.168.3.146:8092'
    return resp

def makeresponseANDreturn(res):

    resp = make_response(jsonify(Resault=res))
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
    resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return resp



