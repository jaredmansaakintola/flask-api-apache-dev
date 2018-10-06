# Observatory Service

# Import framework
from flask import Flask
from flask_restful import Resource, Api

class RestfulHandler(object):
  def response(self, request_id, **kwargs):
    payload = {'jsonrpc': '2.0',
                'id': request_id,
                'result': kwargs}
    return json.dumps(payload)

    self.log("Sent: %s" % payload_js)

  def process(self, msg):
    payload = json.loads(msg)
    method_signature = 'handle_%s' % payload['method']
    result = getattr(self, method_signature)(**payload['params'])
    if result:
      return self.response(payload['id'], **result)


def requiresAuth(func):
  def wrapper(self, session_token, **params):
    self.user_id = None
    self.session_token = session_token
    session = {'iLoginID' : 1}
    if session:
      self.user_id = session['iLoginID']
      return func(self, **params)
    else:
      return {'isAuthenticated': False}
  return wrapper

# Instantiate the app
app = Flask(__name__)
api = Api(app)

# class Handler(Resource):
class Handler(RestfulHandler):
    def get(self):
        return {
            'Galaxies': ['Milkyway', 'Andromeda',
            'Large Magellanic Cloud (LMC)']
        }

    @requiresAuth
    def handle_getHelloWorld(self):
        return {'hello_world': 'Hello World'}


# Create routes
api.add_resource(Handler, '/')
# api.add_resource(Handler, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
