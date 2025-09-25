#import sys
#import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from tasks.task1 import Dictionary
from tasks.task2 import get_total
from tasks.task3 import word_creator

app = Flask(__name__)
api = Api(app, version="1.0", title="Tasks API", description="API for Dictionary, Costs, and Word Creator tasks")

ns1 = api.namespace('task1', description='Dictionary operations')
ns2 = api.namespace('task2', description='Cost operations')
ns3 = api.namespace('task3', description='Word creator operations')

dictionary = Dictionary()
costs = {}

# Models for documentation
entry_model = api.model('Entry', {
    'word': fields.String(required=True, description='The word'),
    'definition': fields.String(required=True, description='The definition')
})

entries_model = api.model('Entries', {
    'entries': fields.List(fields.Nested(entry_model), required=True)
})

costs_model = api.model('Costs', {
    'costs': fields.Raw(required=True, description='Dictionary of item costs')
})

# Task 1: Dictionary lookup
@ns1.route('/<string:word>')
@ns1.param('word', 'The word to look up')
class DictionaryLookup(Resource):
    @ns1.response(200, 'Success')
    def get(self, word):
        """Look up a word in the dictionary"""
        result = dictionary.look(word)
        return {"status": 200, "result": result}, 200

# Task 1: Add baseline entries via POST
@ns1.route('/baseline')
class DictionaryBaseline(Resource):
    @ns1.expect(entries_model)
    @ns1.response(201, 'Entries added')
    def post(self):
        """Add baseline entries to the dictionary"""
        data = request.get_json()
        entries = data.get('entries', [])
        for entry in entries:
            word = entry.get('word')
            definition = entry.get('definition')
            if word and definition:
                dictionary.newentry(word, definition)
        return {"status": 201, "message": "Entries added", "count": len(entries)}, 201

# Task 2: Add or update item costs via POST
@ns2.route('/costs')
class Costs(Resource):
    @ns2.expect(costs_model)
    @ns2.response(201, 'Costs updated')
    def post(self):
        """Add or update item costs"""
        data = request.get_json()
        new_costs = data.get('costs', {})
        if not isinstance(new_costs, dict):
            return {"status": 400, "message": "Invalid format for costs"}, 400
        costs.update(new_costs)
        return {"status": 201, "message": "Costs updated", "costs": costs}, 201

# Task 2: Get total cost
@ns2.route('')
class TotalCost(Resource):
    @ns2.param('items', 'Comma-separated list of items')
    @ns2.param('tax', 'Tax as a decimal (e.g., 0.09)')
    @ns2.response(200, 'Success')
    def get(self):
        """Get total cost for items with tax"""
        items = request.args.get('items', '')
        tax = float(request.args.get('tax', 0))
        items_list = items.split(',') if items else []
        result = get_total(costs, items_list, tax)
        return {"status": 200, "result": result}, 200

# Task 3: Word creator
@ns3.route('')
class WordCreator(Resource):
    @ns3.param('words', 'Comma-separated list of words')
    @ns3.response(200, 'Success')
    def get(self):
        """Create a word from a list of words"""
        words = request.args.get('words', '')
        words_list = words.split(',') if words else []
        result = word_creator(words_list)
        return {"status": 200, "result": result}, 200

if __name__ == '__main__':
    app.run(debug=True)