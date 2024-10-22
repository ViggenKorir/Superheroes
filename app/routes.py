from flask import jsonify, request, render_template
from .models import db, Hero, Power, HeroPower
from . import create_app  

app = create_app()  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all() 
    return jsonify([{'id': hero.id, 'name': hero.name} for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get_or_404(id)
    return jsonify({'id': hero.id, 'name': hero.name})

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([{'id': power.id, 'description': power.description} for power in powers])

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get_or_404(id)
    return jsonify({'id': power.id, 'description': power.description})

@app.route('/hero_powers', methods=['POST'])
def add_hero_power():
    data = request.get_json()
    new_hero_power = HeroPower(
        strength=data['strength'],
        power_id=data['power_id'],
        hero_id=data['hero_id']
    )
    db.session.add(new_hero_power)
    db.session.commit()
    return jsonify({'message': 'Hero Power added'}), 201

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get_or_404(id)
    data = request.get_json()
    power.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Power updated'})
