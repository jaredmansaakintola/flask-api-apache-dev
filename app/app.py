# Import framework
from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify

# Your Auth Technique Here
def requiresAuth(func):
  def wrapper(self, session_token, **params):
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

# Your Restful Micro Service Here
class Handler(Resource):
    @requiresAuth
    @app.route('/')
    def get():
        # return "Hello World"
        animals = {
            'Animals': [
                'Wolf',
                'Bat',
                'Cat',
                'Minotaur'
            ]
        }

        return jsonify(animals)

api.add_resource(Handler, '/') # Route_1

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
