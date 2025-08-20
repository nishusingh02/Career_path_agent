from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, EmployeeProfile
from recommender import get_recommendations
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/employee', methods=['POST'])
def add_employee():
    data = request.json
    employee = EmployeeProfile(**data)
    db.session.add(employee)
    db.session.commit()
    return jsonify({'message': 'Employee added'}), 201

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    recommendations = get_recommendations(data)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)