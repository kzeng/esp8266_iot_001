import datetime
import time
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Replace with your database URI
# db = SQLAlchemy(app)

## app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@hostname/database'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zk010823@118.31.36.131/esp8266-xds'
db = SQLAlchemy(app)

g_dashboard_get_info1_dict = {'system_time': '0000年00月00日 星期五 00:00', 'device_id': '00', 'run_status': "<i class='fa fa-circle red'> 运行中", ' run_time': '243', 'record_interval': '1', 'update_time': '更新于: 0000-0-0 00:00:00', 'temp_1': '35.4', 'hum_1': '61.7',  'control_mode_1': "自动 ", 'control_method_1': "节能 ", 'temp_status_info_1': "制冷 ", 'humi_status_info_1': " 加湿 ", 'target_temp_1': '16.0', 'control_temp_1': '0.5', 'target_hum_1': '90.0' , 'control_hum_1': '9.0', 'temp_2': '--', 'hum_2': '--', 'control_mode_2': '--', 'control_method_2': '--', 'temp_sta tus_info_2': '', 'humi_status_info_2': '', 'target_temp_2': '20.0', 'control_temp_2': '1.0', 'target_hum_2': '96.0', 'co ntrol_hum_2': '5.0', 'temp_3': '36.0', 'hum_3': '51.0', 'control_mode_3': "自动 ", 'control_method_3': '--', 'temp_status_info_3': "制冷 ", 'humi_stat us_info_3': "加湿 ", 'target_temp_3': '20.0', 'control_temp_3': '1.0', 'target_h um_3': '96.0', 'control_hum_3': '5.0', 'temp_4': '--', 'hum_4': '--', 'control_mode_4': '--', 'control_method_4': 'hid e', 'temp_status_info_4': '', 'humi_status_info_4': '', 'target_temp_4': '20.0', 'control_temp_4': '3.0', 'target_hum_4' : '97.8', 'control_hum_4': '5.1', 'temp_5': '35.7', 'hum_5': '56.3', 'control_mode_5': "自动 ", 'control_method_5': "节能 ", 'accm_1': "<i class='fa fa-circ le accm1'></i>", 'accm_2': "<i class='fa fa-circle accm2'></i>", 'accm_3': "<i class='fa fa-circle accm2'></i>", 'accm_4 ': "<i class='fa fa-circle accm2'></i>", 'temp_status_info_5': "制冷 ", 'hum i_status_info_5': "加湿 ", 'target_temp_5': '16.0', 'control_temp_5': '0.5', 'target_hum_5': '90.0', 'control_hum_5': '9.0'}

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

    temp1 = db.Column(db.String(32))
    humidity1 = db.Column(db.String(32))
    target_temp1 = db.Column(db.String(32))
    target_hum1 = db.Column(db.String(32))
    control_temp1 = db.Column(db.String(32))
    control_hum1 = db.Column(db.String(32))
    control_mode1 = db.Column(db.String(32))
    control_method1 = db.Column(db.String(32))
    temp_status_info1 = db.Column(db.String(32))
    humi_status_info1 = db.Column(db.String(32))

    temp2 = db.Column(db.String(32))
    humidity2 = db.Column(db.String(32))
    target_temp2 = db.Column(db.String(32))
    target_hum2 = db.Column(db.String(32))
    control_temp2 = db.Column(db.String(32))
    control_hum2 = db.Column(db.String(32))
    control_mode2 = db.Column(db.String(32))
    control_method2 = db.Column(db.String(32))
    temp_status_info2 = db.Column(db.String(32))
    humi_status_info2 = db.Column(db.String(32))
    
    temp3 = db.Column(db.String(32))
    humidity3 = db.Column(db.String(32))
    target_temp3 = db.Column(db.String(32))
    target_hum3 = db.Column(db.String(32))
    control_temp3 = db.Column(db.String(32))
    control_hum3 = db.Column(db.String(32))
    control_mode3 = db.Column(db.String(32))
    control_method3 = db.Column(db.String(32))
    temp_status_info3 = db.Column(db.String(32))
    humi_status_info3 = db.Column(db.String(32))

    temp4 = db.Column(db.String(32))
    humidity4 = db.Column(db.String(32))
    target_temp4 = db.Column(db.String(32))
    target_hum4 = db.Column(db.String(32))
    control_temp4 = db.Column(db.String(32))
    control_hum4 = db.Column(db.String(32))
    control_mode4 = db.Column(db.String(32))
    control_method4 = db.Column(db.String(32))
    temp_status_info4 = db.Column(db.String(32))
    humi_status_info4 = db.Column(db.String(32))

    temp5 = db.Column(db.String(32))
    humidity5 = db.Column(db.String(32))
    target_temp5 = db.Column(db.String(32))
    target_hum5 = db.Column(db.String(32))
    control_temp5 = db.Column(db.String(32))
    control_hum5 = db.Column(db.String(32))
    control_mode5 = db.Column(db.String(32))
    control_method5 = db.Column(db.String(32))
    temp_status_info5 = db.Column(db.String(32))
    humi_status_info5 = db.Column(db.String(32))
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
    page = request.args.get('page', 1, type=int)
    per_page = 25
    inst_data = InstData.query.order_by(InstData.record_time.desc()).paginate(page=page, per_page=per_page, error_out=False)  
    records_count = InstData.query.count()
    return render_template('inst_data.html', inst_data=inst_data, records_count=records_count)



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

    # parse raw data and save to inst_data table
    raw_data_list =  [raw_data[i:i+2] for i in range(0, len(raw_data), 2)]
    print(raw_data_list)

    dashboard_get_info1_dict = {}
    # 系统时间
    # t1,t2,t3,t4,t5,t6 表示当时间，按年，月，日，周，时，分依次
    # data = b.dashboard_info
    # data_list = data.split(" ")
    data_list = raw_data_list
    year = int('0x' + data_list[9], 16)
    month = int('0x' + data_list[10], 16)
    day = int('0x' + data_list[11], 16)
    week_str = ['日', '一', '二', '三', '四', '五', '六', '---' ]
    week = int('0x' + data_list[12], 16)

    hour = int('0x' + data_list[13], 16)
    mins = int('0x' + data_list[14], 16)
    dashboard_get_info1_dict.update({"system_time" : "20{:0>2d}年{:0>2d}月{:0>2d}日 星期{} {:0>2d}:{:0>2d}".format(year, month,day, week_str[week], hour, mins) })
    dashboard_get_info1_dict.update({"device_id" : str( int('0x' + data_list[3], 16) ) })

    if int('0x' + data_list[5], 16) == 1:
        run_status = "<i class='fa fa-circle red'> 运行中"
    else:
        run_status = "<i class='fa fa-circle gray'> 已停止"

    dashboard_get_info1_dict.update({"run_status" : run_status })
    dashboard_get_info1_dict.update({"run_time" : str( int('0x' + data_list[6] + data_list[7], 16)) })
    dashboard_get_info1_dict.update({"record_interval" : str( round(int('0x' + data_list[8], 16))) })
    dt_utc = time.localtime()
    dashboard_get_info1_dict.update({"update_time" : '更新于: {}-{}-{} {}:{}:{}'.format(dt_utc.tm_year, dt_utc.tm_mon, dt_utc.tm_mday, dt_utc.tm_hour, dt_utc.tm_min, dt_utc.tm_sec) })
    
    # 01  00 C8 03 26  00 C8  00 0A  03 C0  00 32  01 00 00 00 00 	  第一通道数据
    # 第1字节，表示传感器存在与否（1表示存在，0表示不存在），不存在时，温湿度上传数据为0，在界面上显示为“――――”
    # 第2，3字节为温度数据，高位在前，低位在后。实际显示时应缩小10位，取得一位小数。如本次收到00C8，实际显示为20.0.
    # 第4，5字节为湿度数据，高位在前，低位在后。实际显示时应缩小10位，取得一位小数。如本次收到0326，实际显示为80.6.


    ch = 1
    for idx in (15,33,51,69,87): #各通道数据起始地址在整个响应数据中的位置
        temp_status_info = ''
        humi_status_info = ''
        if int('0x' + data_list[idx], 16) == 0:
            dashboard_get_info1_dict.update({"temp_" + str(ch) : "--" })
            dashboard_get_info1_dict.update({"hum_" + str(ch) : "--" })
            dashboard_get_info1_dict.update({"control_mode_" + str(ch) : "hide" })
            dashboard_get_info1_dict.update({"control_method_" + str(ch) : "hide" })

            # dashboard_get_info1_dict.update({"air_protect_status_" + str(ch) : "hide" })
            # dashboard_get_info1_dict.update({"control_output_status_" + str(ch) : "hide" })
            dashboard_get_info1_dict.update({"temp_status_info_" + str(ch) : temp_status_info })
            dashboard_get_info1_dict.update({"humi_status_info_" + str(ch) : humi_status_info })
        else:
            # 这里做一个温湿度数据校验，不在下面区间的，反复上次的保存的数据
            # t= [5.0, 45.0]
            # h=[20.0, 99.9]
            t_val = int('0x' + data_list[idx+1] + data_list[idx+2], 16)/10.0
            h_val = int('0x' + data_list[idx+3] + data_list[idx+4], 16)/10.0

            if t_val < 5.0 or t_val > 45.0:
                return json.dumps(g_dashboard_get_info1_dict)
            
            if h_val < 20.0 or h_val > 99.9:
                return json.dumps(dashboard_get_info1_dict)

            dashboard_get_info1_dict.update({"temp_" + str(ch) : str(int('0x' + data_list[idx+1] + data_list[idx+2], 16)/10.0) })
            dashboard_get_info1_dict.update({"hum_" + str(ch) : str(int('0x' + data_list[idx+3] + data_list[idx+4], 16)/10.0) })
            if int('0x' + data_list[idx+13], 16) == 1:
                dashboard_get_info1_dict.update({"control_mode_" + str(ch) : "循环 " })
            else:
                dashboard_get_info1_dict.update({"control_mode_" + str(ch) : "自动 " })
            
            if int('0x' + data_list[idx+14], 16) == 1:
                dashboard_get_info1_dict.update({"control_method_" + str(ch) : "节能 " })
            else:
                dashboard_get_info1_dict.update({"control_method_" + str(ch) : "--" })

            if int('0x' + data_list[idx+15], 16) == 0: #00
                temp_status_info = ''
            elif int('0x' + data_list[idx+15], 16) == 2: #10
                temp_status_info = "制冷保护 "
            elif int('0x' + data_list[idx+15], 16) == 1: #01
                temp_status_info = "加热保护 "
            else:
                temp_status_info = ''

            # bin_str="{:>08}".format(bin(int('0x' + data_list[31], 16))[2:])
            bin_str="{:>08}".format(bin(int('0x' + data_list[idx+16], 16))[2:])
            print('---------------------------------------')
            print(bin_str)
            print('----------------------------------------')
            bin_str_list = list(bin_str)
            # cos_str = ''

            # ['0', '0', '0', '0', '0', '1', '0', '1']
            # 从低到高每个状态为：加热，制冷，化霜，加湿，抽湿.
            if bin_str_list[7] == '1':
                # cos_str += "加热 "
                temp_status_info += "加热 "
            if bin_str_list[6] == '1':
                # cos_str += "制冷 "
                temp_status_info += "制冷 "
            if bin_str_list[5] == '1':
                # cos_str += "化霜 "
                temp_status_info += "化霜 "
            if bin_str_list[4] == '1':
                # cos_str += "加湿 "      
                humi_status_info += "加湿 "  
            if bin_str_list[3] == '1':
                # cos_str += "抽湿 " 
                humi_status_info += "抽湿 "
            # if cos_str == '':
            #     cos_str = "hide"
            # dashboard_get_info1_dict.update({"control_output_status_" + str(ch) : cos_str })

            #判断CH5, 即综合通道第18字节，显示当前通道有无空调控制模块(为0时表示没有,为1时表示CH1存在‘绿色’ 其他值为不存在‘红色’)
            if ch == 5:
                print("CH:{} ACCM:{}".format(ch, int('0x' + data_list[idx+17], 16) ))
                if int('0x' + data_list[idx+17], 16) != 0:
                    dashboard_get_info1_dict.update({"accm_1" : "<i class='fa fa-circle accm1'></i>" })
                    dashboard_get_info1_dict.update({"accm_2" : "<i class='fa fa-circle accm2'></i>" })
                    dashboard_get_info1_dict.update({"accm_3" : "<i class='fa fa-circle accm2'></i>" })
                    dashboard_get_info1_dict.update({"accm_4" : "<i class='fa fa-circle accm2'></i>" })
                else:
                    dashboard_get_info1_dict.update({"accm_1" : "<i class='fa fa-circle accm2'></i>" })
                    dashboard_get_info1_dict.update({"accm_2" : "<i class='fa fa-circle accm2'></i>" })
                    dashboard_get_info1_dict.update({"accm_3" : "<i class='fa fa-circle accm2'></i>" })
                    dashboard_get_info1_dict.update({"accm_4" : "<i class='fa fa-circle accm2'></i>" })


        dashboard_get_info1_dict.update({"temp_status_info_" + str(ch) : temp_status_info })
        dashboard_get_info1_dict.update({"humi_status_info_" + str(ch) : humi_status_info })

        dashboard_get_info1_dict.update({"target_temp_" + str(ch) : str(int('0x' + data_list[idx+5] + data_list[idx+6], 16)/10.0) })
        dashboard_get_info1_dict.update({"control_temp_" + str(ch) : str(int('0x' + data_list[idx+7] + data_list[idx+8], 16)/10.0) })
        dashboard_get_info1_dict.update({"target_hum_" + str(ch) : str(int('0x' + data_list[idx+9] + data_list[idx+10], 16)/10.0) })
        dashboard_get_info1_dict.update({"control_hum_" + str(ch) : str(int('0x' + data_list[idx+11] + data_list[idx+12], 16)/10.0) })

        ch = ch + 1

    # print(dashboard_get_info1_dict)    

    inst_name = "GuanShan Lab"
    sensor_name = "Esp8266"

    temp1 = dashboard_get_info1_dict["temp_1"]
    humidity1 = dashboard_get_info1_dict["hum_1"]
    target_temp1 =  dashboard_get_info1_dict["target_temp_1"]
    target_hum1 =  dashboard_get_info1_dict["target_hum_1"]
    control_temp1 =  dashboard_get_info1_dict["control_temp_1"]
    control_hum1 =  dashboard_get_info1_dict["control_hum_1"]
    control_mode1 =  dashboard_get_info1_dict["control_mode_1"]
    control_method1 =  dashboard_get_info1_dict["control_method_1"]
    temp_status_info1 =  dashboard_get_info1_dict["temp_status_info_1"]
    humi_status_info1 =  dashboard_get_info1_dict["humi_status_info_1"]

    temp2 = dashboard_get_info1_dict["temp_2"]
    humidity2 = dashboard_get_info1_dict["hum_2"]
    target_temp2 =  dashboard_get_info1_dict["target_temp_2"]
    target_hum2 =  dashboard_get_info1_dict["target_hum_2"]
    control_temp2 =  dashboard_get_info1_dict["control_temp_2"]
    control_hum2 =  dashboard_get_info1_dict["control_hum_2"]
    control_mode2 =  dashboard_get_info1_dict["control_mode_2"]
    control_method2 =  dashboard_get_info1_dict["control_method_2"]
    temp_status_info2 =  dashboard_get_info1_dict["temp_status_info_2"]
    humi_status_info2 =  dashboard_get_info1_dict["humi_status_info_2"]
    
    temp3 = dashboard_get_info1_dict["temp_3"]
    humidity3 = dashboard_get_info1_dict["hum_3"]
    target_temp3 =  dashboard_get_info1_dict["target_temp_3"]
    target_hum3 =  dashboard_get_info1_dict["target_hum_3"]
    control_temp3 =  dashboard_get_info1_dict["control_temp_3"]
    control_hum3 =  dashboard_get_info1_dict["control_hum_3"]
    control_mode3 =  dashboard_get_info1_dict["control_mode_3"]
    control_method3 =  dashboard_get_info1_dict["control_method_3"]
    temp_status_info3 =  dashboard_get_info1_dict["temp_status_info_3"]
    humi_status_info3 =  dashboard_get_info1_dict["humi_status_info_3"]

    temp4 = dashboard_get_info1_dict["temp_4"]
    humidity4 = dashboard_get_info1_dict["hum_4"]
    target_temp4 =  dashboard_get_info1_dict["target_temp_4"]
    target_hum4 =  dashboard_get_info1_dict["target_hum_4"]
    control_temp4 =  dashboard_get_info1_dict["control_temp_4"]
    control_hum4 =  dashboard_get_info1_dict["control_hum_4"]
    control_mode4 =  dashboard_get_info1_dict["control_mode_4"]
    control_method4 =  dashboard_get_info1_dict["control_method_4"]
    temp_status_info4 =  dashboard_get_info1_dict["temp_status_info_4"]
    humi_status_info4 =  dashboard_get_info1_dict["humi_status_info_4"]

    temp5 = dashboard_get_info1_dict["temp_5"]
    humidity5 = dashboard_get_info1_dict["hum_5"]
    target_temp5 =  dashboard_get_info1_dict["target_temp_5"]
    target_hum5 =  dashboard_get_info1_dict["target_hum_5"]
    control_temp5 =  dashboard_get_info1_dict["control_temp_5"]
    control_hum5 =  dashboard_get_info1_dict["control_hum_5"]
    control_mode5 =  dashboard_get_info1_dict["control_mode_5"]
    control_method5 =  dashboard_get_info1_dict["control_method_5"]
    temp_status_info5 =  dashboard_get_info1_dict["temp_status_info_5"]
    humi_status_info5 =  dashboard_get_info1_dict["humi_status_info_5"]

    record_time = datetime.datetime.now()

    inst_data_item = InstData(inst_name=inst_name, sensor_name=sensor_name, 
                            temp1=temp1, humidity1=humidity1, target_temp1=target_temp1, target_hum1=target_hum1, control_temp1=control_temp1, control_hum1=control_hum1, control_mode1=control_mode1, control_method1=control_method1, temp_status_info1=temp_status_info1, humi_status_info1=humi_status_info1,
                            temp2=temp2, humidity2=humidity2, target_temp2=target_temp2, target_hum2=target_hum2, control_temp2=control_temp2, control_hum2=control_hum2, control_mode2=control_mode2, control_method2=control_method2, temp_status_info2=temp_status_info2, humi_status_info2=humi_status_info2,                              
                            temp3=temp3, humidity3=humidity3, target_temp3=target_temp3, target_hum3=target_hum3, control_temp3=control_temp3, control_hum3=control_hum3, control_mode3=control_mode3, control_method3=control_method3, temp_status_info3=temp_status_info3, humi_status_info3=humi_status_info3,
                            temp4=temp4, humidity4=humidity4, target_temp4=target_temp4, target_hum4=target_hum4, control_temp4=control_temp4, control_hum4=control_hum4, control_mode4=control_mode4, control_method4=control_method4, temp_status_info4=temp_status_info4, humi_status_info4=humi_status_info4,
                            temp5=temp5, humidity5=humidity5, target_temp5=target_temp5, target_hum5=target_hum5, control_temp5=control_temp5, control_hum5=control_hum5, control_mode5=control_mode5, control_method5=control_method5, temp_status_info5=temp_status_info5, humi_status_info5=humi_status_info5,
                            record_time=record_time)
    db.session.add(inst_data_item)
    db.session.commit()
    return "OK"



if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=55555, debug=False)
