from flask import Flask
from flask_restful import Resource, Api
from resources.get_puzzle import GetPuzzle
from resources.check_solution import CheckSolution
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
api = Api(app)

api.add_resource(GetPuzzle, '/get_puzzle')
api.add_resource(CheckSolution, '/check_solution')

if __name__ == '__main__':
    debug = os.getenv("DEBUG")
    if not debug:
        debug = False
    app.run(debug=debug)
