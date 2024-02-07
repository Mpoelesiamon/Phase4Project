from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Game(db.Model, SerializerMixin):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    genre = db.Column(db.String)
    platform = db.Column(db.String)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Define the one-to-many relationship with Inventory
    inventories = db.relationship("Inventory", back_populates="game")

    def __repr__(self):
        return f'<Game {self.title} for {self.platform}>'

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())   


    @classmethod
    def find_or_create_user(cls, user_id):
        user = cls.query.get(user_id)
        if user:
            return user
        else:
            # Create a new user with the given ID
            new_user = cls(id=user_id)
            db.session.add(new_user)
            db.session.commit()
            return new_user    

class Inventory(db.Model, SerializerMixin):
    __tablename__ ='inventories'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    quantity = db.Column(db.SmallInteger, nullable=False)
    
    # Relationships
    user = db.relationship("User", backref="inventory")
    game = db.relationship("Game", foreign_keys=[game_id])

    # Define the relationship with Game
    game = db.relationship("Game", back_populates="inventories")

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           "id": self.id, 
           "quantity": self.quantity,
           "user_username": self.user.username,
           "game_title": self.game.title
       }
