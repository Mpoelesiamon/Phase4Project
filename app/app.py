#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify, url_for
from flask_migrate import Migrate
#from flask_restful import Api, Resource
from flask import abort
from flask_cors import CORS
from models import db, Game, User, Inventory

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Disable Strict-Transport-Security header
app.config['SESSION_COOKIE_SECURE'] = False  # Uncomment this line if needed
app.config['SESSION_COOKIE_HTTPONLY'] = False  # Uncomment this line if needed

CORS(app, resources={r"/signup": {"origins": ["http://localhost:5554", "https://localhost:5554"]}})


#CORS(app)
migrate = Migrate(app, db)

db.init_app(app)


#api = Api(app)

@app.route('/')
def index():
    return "Game APP"

@app.route('/games')
def games():

    games = []
    for game in Game.query.all():
        game_dict = {
            "id" : game.id, 
            "title": game.title,
            "genre": game.genre,
            "platform": game.platform,
            "price": game.price,
        }
        games.append(game_dict)

    response = make_response(
        jsonify(games),
        200
    )
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/games_by_title')
def games_by_title():
    games_by_title = Game.query.order_by(Game.title).all()

    game_titles = [game.title for game in games_by_title]

    response = make_response(
        jsonify(game_titles),
        200
    )

    return response    

@app.route('/games/<int:id>')
def game_by_id(id):
    game = Game.query.filter_by(id=id).first()

    game_dict = game.to_dict()
    {
        "title": game.title,
        "genre": game.genre,
        "platform": game.platform,
        "price": game.price,

    }
    response = make_response(jsonify(game_dict), 200)
    return response

@app.route('/users')
def users():

    users = []
    for user in User.query.all():
        user_dict = {
            "username": user.username,
            "password": user.password,
        }
        users.append(user_dict)

    response = make_response(
        jsonify(users),
        200
    )
    response.headers["Content-Type"] = "application/json"
    return response    


@app.route("/games/<int:id>/inventory")
def get_game_inventory(id):
    game = Game.query.filter_by(id=id).first()
    if not game:
        abort(404)

    inventories = [inv.serialize for inv in game.inventories]
    response = make_response(
        jsonify(inventories),
        200
    )
    response.headers["Content-Type"] = "application/json"
    return response

@app.route("/inventory/add", methods=["POST"])
def add_game_to_inventory():
    # Get data from the request
    data = request.json
    user_id = data.get("user_id")
    game_id = data.get("game_id")
    quantity = data.get("quantity", 1)  

    # Check if all required data is provided
    if not user_id or not game_id:
        return jsonify({"error": "Both user_id and game_id are required"}), 400

    # Check if the user and game exist
    user = User.query.get(user_id)
    game = Game.query.get(game_id)
    if not user or not game:
        return jsonify({"error": "User or game not found"}), 404

    # Add the game to the user's inventory
    #inventory_entry = Invehttp://127.0.0.1/
@app.route("/signup", methods=["GET", "POST", "OPTIONS"])
def signup():
# Get data from the request
    data = request.get_json(force=True)

    email = data.get("email")
    username = data.get("username")
    birthdate = data.get("birthdate")
    password = data.get("password")
    gender = data.get("gender")

    # Check if all required data is provided
    if not email or not username or not birthdate or not password:
        return jsonify({"error": "Email, username, birthdate, and password are required"}), 400

    # Check if the user already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "User with this email already exists"}), 400

    # Create a new user
    new_user = User(email=email, username=username, birthdate=birthdate, password=password, gender=gender)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


if __name__ == '__main__':
    app.run(port=5554, debug=True)