import json
import os

def load_test_data(filename):
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, 'testdata', filename)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
