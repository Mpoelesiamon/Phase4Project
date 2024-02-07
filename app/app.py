#!/usr/bin/env python3

from flask import Flask, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Game

from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class GameResource(Resource):
    def get(self, game_id):
        game = Game.query.get(game_id)
        if game:
            return game.serialize(), 200
        return {'message': 'Game not found'}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name of the game is required')
        parser.add_argument('developer', type=str, required=True, help='Developer of the game is required')
        args = parser.parse_args()

        new_game = Game(name=args['name'], developer=args['developer'])
        db.session.add(new_game)
        db.session.commit()

        return new_game.serialize(), 201

    def patch(self, game_id):
        game = Game.query.get(game_id)
        if not game:
            return {'message': 'Game not found'}, 404

        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('developer', type=str)
        args = parser.parse_args()

        if 'name' in args:
            game.name = args['name']
        if 'developer' in args:
            game.developer = args['developer']

        db.session.commit()
        return game.serialize(), 200

api.add_resource(GameResource, '/games', '/games/<int:game_id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)