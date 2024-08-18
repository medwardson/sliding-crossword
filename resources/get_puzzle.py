import time
from flask_restful import Resource
import os
import random
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)

from firestore_init import db

class GetPuzzle(Resource):
    def get(self):
        date_id = time.strftime("%Y%m%d")
        result = db.collection('daily_puzzles').document(date_id).get().to_dict()
        srcambled_puzzle = scramble_grid(result['solution'])
        result['puzzle'] = srcambled_puzzle
        del result['solution']

        return result

import random

def scramble_grid(grid):
    all_chars = []
    for row in grid:
        all_chars.extend(list(row))
    
    random.shuffle(all_chars)
    
    new_grid = []
    for i in range(5):
        if i == 4:
            new_grid.append(''.join(all_chars[i*5:i*5+4]))
        else:
            new_grid.append(''.join(all_chars[i*5:i*5+5]))
    
    return new_grid