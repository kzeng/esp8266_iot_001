import datetime
import time
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Replace with your database URI
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    mobile = db.Column(db.String(20))
    address = db.Column(db.String(200))

class InstData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # api_key = db.Column(db.String(100))
    inst_name = db.Column(db.String(100))
    sensor_name = db.Column(db.String(100))
    temp1 = db.Column(db.Float)
    humidity1 = db.Column(db.Float)
    temp2 = db.Column(db.Float)
    humidity2 = db.Column(db.Float)
    temp3 = db.Column(db.Float)
    humidity3 = db.Column(db.Float)
    temp4 = db.Column(db.Float)
    humidity4 = db.Column(db.Float)
    record_time = db.Column(db.DateTime)


class InstRawData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # api_key = db.Column(db.String(100))
    raw_data = db.Column(db.String(1024))



with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return "inst data api"

# CRUD operations for User
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    # userd = jsonify([{'id': user.id, 'name': user.name, 'mobile': user.mobile, 'address': user.address} for user in users])
    return render_template('users.html', users=users)


@app.route('/users', methods=['POST'])
def create_user():
    # data = request.get_json()
    name = request.form.get('name')
    mobile = request.form.get('mobile')
    address = request.form.get('address')

    user = User(name=name, mobile=mobile, address=address)
    db.session.add(user)
    db.session.commit()
    # return jsonify({'message': 'User created successfully'})
    # return redirect(url_for('get_users'))
    return "OK"

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({'id': user.id, 'name': user.name, 'mobile': user.mobile, 'address': user.address})
    else:
        return jsonify({'message': 'User not found'})

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user:
        data = request.get_json()
        user.name = data['name']
        user.mobile = data['mobile']
        user.address = data['address']
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'message': 'User not found'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'message': 'User not found'})


#-------------------------------
# CRUD operations for User
@app.route('/inst_data', methods=['GET'])
def get_inst_data():
    inst_data = InstData.query.all()
    return render_template('inst_data.html', inst_data=inst_data)


@app.route('/inst_data', methods=['POST'])
def inst_curr_data():
    print("post data to database")
    # data = request.get_json()
    api_key = request.form.get('api_key')
    print(api_key)

    if api_key != '123456':
        return "Invalid API Key"
    
    inst_name = request.form.get('inst_name')
    sensor_name = request.form.get('sensor_name')
    temp1 = request.form.get('temp1')
    humidity1 = request.form.get('humidity1')
    temp2 = request.form.get('temp2')
    humidity2 = request.form.get('humidity2')
    temp3 = request.form.get('temp3')
    humidity3 = request.form.get('humidity3')
    temp4 = request.form.get('temp4')
    humidity4 = request.form.get('humidity4')
    # dt = datetime.datetime.now()
    # record_time = dt.strftime("%Y-%m-%d %H:%M:%S")
    record_time = datetime.datetime.now()
    inst_data_item = InstData(inst_name=inst_name, sensor_name=sensor_name, temp1=temp1, humidity1=humidity1, temp2=temp2, humidity2=humidity2, temp3=temp3, humidity3=humidity3, temp4=temp4, humidity4=humidity4, record_time=record_time)
    db.session.add(inst_data_item)
    db.session.commit()
    return "OK"



#-------------------------------------------------
@app.route('/inst_raw_data', methods=['GET'])
def get_inst_raw_data():
    inst_raw_data = InstRawData.query.all()
    return render_template('inst_raw_data.html', inst_raw_data=inst_raw_data)


@app.route('/inst_raw_data', methods=['POST'])
def inst_curr_raw_data():
    print("post raw data to database")
    # data = request.get_json()
    api_key = request.form.get('api_key')
    print(api_key)

    if api_key != '123456':
        return "Invalid API Key"
    
    raw_data = request.form.get('raw_data')
    inst_raw_data_item = InstRawData(raw_data=raw_data)
    db.session.add(inst_raw_data_item)
    db.session.commit()
    return "OK"



if __name__ == '__main__':
    app.run()
