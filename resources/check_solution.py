import time
from flask import request
from flask_restful import Resource
import os
import random
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)

from firestore_init import db

class CheckSolution(Resource):
    def post(self):
        data = request.get_json()
        date_id = time.strftime("%Y%m%d")
        result = db.collection('daily_puzzles').document(date_id).get().to_dict()
        solution = result['solution']

        try:
          if data['solution'] == solution:
              return {'result': 'correct'}
          else:
              return {'result': 'incorrect'}
        except:
          return {'error': 'invalid data format'}, 400

