from flask import Flask
from flask_restful import Resource, Api
from resources.get_puzzle import GetPuzzle
from resources.check_solution import CheckSolution

app = Flask(__name__)
api = Api(app)

api.add_resource(GetPuzzle, '/get_puzzle')
api.add_resource(CheckSolution, '/check_solution')

if __name__ == '__main__':
    app.run(debug=True)
