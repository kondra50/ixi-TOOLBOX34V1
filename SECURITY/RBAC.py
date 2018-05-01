from flask_restful import Resource, reqparse
from SECURITY import auth,model
from flask.ext.restful.utils import cors


class AccessList(Resource):

    @cors.crossdomain(origin='http://192.168.3.146:8092')
    @auth.requires_auth
    def get(self):
         parser = reqparse.RequestParser()
         parser.add_argument('group', required=True)
         args = parser.parse_args()
         group = args['group']
         res=model.Accesslist(group)
         return auth.makeresponseANDreturn(res)

    def options(self):
      return auth.setheaderANDreturn()