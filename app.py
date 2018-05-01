#from flask import Flask
from flask_restful import Resource, Api
# from flask.ext import restful
#from flask.ext.cors import CORS
import types

from COFA import cofa
from SFDC import sfdc
from EXPANDABLE import expandable
from SECURITY import  RBAC



from functools import wraps
from flask import Flask, request, jsonify, _request_ctx_stack
# from werkzeug.local import LocalProxy
# from flask.ext.cors import cross_origin



app=Flask(__name__)

#CORS(app)


# def api_route(self, *args, **kwargs):
#     def wrapper(cls):
#         self.add_resource(cls, *args, **kwargs)
#         return cls
#     return wrapper
#
# app.route = types.MethodType(api_route, app)






# def hello_word():
#     return "hi"

api = Api(app)



api.add_resource(cofa.list, '/cofa/list')
api.add_resource(cofa.Report, '/cofa/report')


api.add_resource(sfdc.SFDC_EXP_DESCREPENCY, '/sfdc/descrepency')


api.add_resource(expandable.Fedxshipment, '/exp/st')
api.add_resource(expandable.SODASH, '/exp/sodash')
api.add_resource(expandable.SODASHLIST, '/exp/sodashlists')
api.add_resource(expandable.SODASHBACKLOCKEDSHORT, '/exp/sodashblshort')
api.add_resource(expandable.SODASHSHIPMENTSHORT, '/exp/sodashshipshort')
api.add_resource(expandable.NOTIFICATIONS, '/exp/notifications')
api.add_resource(expandable.NOTIFICATIONSBYSO, '/exp/notificationsbyso')
api.add_resource(expandable.SPECIALNOTIFICATIONS, '/exp/specialnotifications')
api.add_resource(expandable.GRAPHS, '/exp/graph')
api.add_resource(expandable.EEPROMLIST, '/exp/eepromlist')
api.add_resource(expandable.EEPROMDETAIL, '/exp/eepromdetail')
api.add_resource(expandable.BOM, '/exp/bomcc')
api.add_resource(expandable.SOASSEMBLY, '/exp/soassembly')



api.add_resource(expandable.SO, '/rpt/so')

api.add_resource(expandable.SOPICKLIST, '/rpt/sopicklist')

api.add_resource(RBAC.AccessList, '/sec/accesslist')