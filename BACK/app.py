import os
import json
import db
from flask import Flask, Response, request, session
# from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

app = Flask(__name__)
app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'database.sqlite'),
    )
db.init_app(app)

#--------------------------------------------------------------
#                          1.登录模块                          |
#--------------------------------------------------------------
@app.route('/api/auth/login', methods=["POST"])
def login() -> Response | str:
    '''
    用户登录接口
    '''
    error = None
    status = 'fail'
    username = request.get_json()['username']
    password = request.get_json()['password']
    database = db.get_db()
    user = database.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
    ).fetchone()

    if user is None:
        error = '用户' + str(username) + '未注册'
    # elif not check_password_hash(user['password'], password):
    #     error = '密码错误'
    elif user['password'] != password:
        error = '密码错误'

    if error is None:
        session.clear()
        session['userId'] = user['id']
        session['userName'] = user['username']
        status = 'success'
    
    if status == 'success':
        res = {
            'status': status,
            'data': {
                'userId': user['id'],
                'username': user['username'],
                'accessToken': ''
            }
        }
    elif status == 'fail':
        res = {
            'status': status,
            'data': {
                'userId': '',
                'username': '',
                'accessToken': error
            }
        }

    return json.dumps(res)

@app.route('/api/auth/register', methods=["POST"])
def register() -> Response | str:
    '''
    用户注册接口
    '''
    error = None
    status = 'fail'
    # print(request.get_json())
    username = request.get_json()['username']
    password = request.get_json()['password']
    database = db.get_db()

    if not username:
        error = '用户名不能为空'
    elif not password:
        error = '密码不能为空'

    if error is None:
        try:
            # database.execute(
            #     "INSERT INTO user (username, password) VALUES (?, ?)",
            #     (username, generate_password_hash(password))
            # )
            database.execute(
                "INSERT INTO user (username, password) VALUES (?, ?)",
                (username, password)
            )
            database.commit()
            status = 'success'
        except database.IntegrityError:
            error = '用户名已被注册'
    
    if status == 'success':
        res = {
            'status': status,
            'data': {
                "message": 'Registration successful'
            }
        }
    elif status == 'fail':
        res = {
            'status': status,
            'data': {
                "message": error
            }
        }
    return json.dumps(res)

@app.route('/api/auth/logout', methods=["POST"])
def logout() -> Response | str:
    '''
    用户注销接口
    '''
    res = {
        'status': 'success',
        'data': {
            "message": "已退出登录"
        }
    }
    return json.dumps(res)

@app.route('/api/auth/user/password', methods=["PUT"])
def password() -> Response | str:
    '''
    修改用户密码接口
    '''
    error = None
    status = 'error'
    old_password = request.get_json()['old_password']
    new_password = request.get_json()['new_password']
    database = db.get_db()

    userId = session['userId']
    user = database.execute(
        'SELECT * FROM user WHERE id = ?', (userId,)
    ).fetchone()

    if not old_password:
        error = '请输入旧密码'
    elif not new_password:
        error = '请输入新密码'
    # elif not check_password_hash(user['password'], old_password):
    #     error = '旧密码错误'
    elif user['password'] != old_password:
        error = '旧密码错误'
    elif old_password == new_password:
        error = '新密码不能与旧密码相同'

    if error is None:
        # database.execute(
        #     'UPDATE user SET password = ? WHERE id = ?',
        #     (generate_password_hash(new_password), userId)
        # )
        database.execute(
            'UPDATE user SET password = ? WHERE id = ?',
            (new_password, userId)
        )
        database.commit()
        status = 'success'

    user = database.execute('SELECT * FROM user').fetchall()
    for row in user:
        print(f"ID: {row['id']}, Username: {row['username']}, Password: {row['password']}")

    if status == 'success':
        res = {
            'status': status,
            'data': {
                "message": "修改密码成功"
            }
        }
    elif status == 'error':
        res = {
            'status': status,
            'data': {
                "message": error
            }
        }

    return json.dumps(res)

#--------------------------------------------------------------
#                 2.1 康复计划管理模块                          |
#--------------------------------------------------------------
@app.route('/api/rehabilitation/plans', methods=["POST"])
def create_plans() -> Response | str:
    '''
    手动创建康复计划接口
    '''
    user_info = request.get_json()
    print(user_info)
    res = {
        "status": "success", # success or error
        "data": {
            "planId": "plan123",
            "message": "Rehabilitation plan created successfully"
        }
    }
    return json.dumps(res)

@app.route('/api/rehabilitation/plans', methods=["PUT"])
def update_plans() -> Response | str:
    '''
    更新康复计划接口
    '''
    user_info = request.get_json()
    print(user_info)
    res = {
        "status": "success", # success or error
        "data": {
            "message": "Rehabilitation plan updated successfully"
        }
    }
    return json.dumps(res)

@app.route('/api/rehabilitation/plans', methods=["GET"])
def get_plans() -> Response | str:
    '''
    获取康复计划详情接口
    返回参数说明：
    - status (string): 请求状态，值为 "success" 或 "error"
    - data (object): 返回的数据对象
    - planId (string): 康复计划ID
    - planName (string): 康复计划名称
    - description (string): 康复计划描述
    - exercises (array): 康复锻炼项目数组
    - name (string): 锻炼项目名称
    - description (string): 锻炼项目描述
    - sets (integer): 组数
    - repetitions (integer): 每组次数
    '''
    # user_info = request.get_json()
    # print(user_info)
    res = {
        "status": "success", # success or error
        "data": {
            "planId": "plan123",
            "planName": "Example Plan",
            "description": "This is an example rehabilitation plan.",
            "exercises": [
                {
                    "name": "Exercise 1",
                    "description": "Example exercise 1",
                    "sets": 3,
                    "repetitions": 10
                },
                {
                    "name": "Exercise 2",
                    "description": "Example exercise 2",
                    "sets": 2,
                    "repetitions": 12
                }
            ]
        }
    }
    return json.dumps(res)

@app.route('/api/rehabilitation/plans', methods=["DELETE"])
def delete_plans() -> Response | str:
    '''
    删除康复计划接口
    '''
    # user_info = request.get_json()
    # print(user_info)
    res = {
        "status": "success", # success or error
        "data": {
            "message": "Rehabilitation plan deleted successfully"
        }
    }
    return json.dumps(res)

@app.route('/api/rehabilitation/generate-plan', methods=["POST"])
def generate_plans() -> Response | str:
    '''
    自动生成康复训练计划接口
    '''
    user_info = request.get_json()
    print(user_info)
    res = {
        "status": "success", # success or error
        "data": {
            "planId": "plan123",
            "planName": "Generated Plan",
            "description": "This is a generated rehabilitation plan for knee pain.",
            "exercises": [
                {
                    "name": "Exercise 1",
                    "description": "Example exercise 1",
                    "sets": 3,
                    "repetitions": 10
                },
                {
                    "name": "Exercise 2",
                    "description": "Example exercise 2",
                    "sets": 2,
                    "repetitions": 12
                }
            ]
        }
    }
    return json.dumps(res)

#--------------------------------------------------------------
#                 2.2 康复知识库模块                            |
#--------------------------------------------------------------
@app.route('/api/rehabilitation/knowledge/categories', methods=["GET"])
def get_categories() -> Response | str:
    '''
    获取康复知识分类列表接口
    '''
    database = db.get_db()
    res_data = []
    res_status = "fail"
    category_list = database.execute(
        'SELECT * FROM rehabilitation_categories'
    ).fetchall()
    print(type(category_list[0]['categoryId'])) # test the format of the result from fetchall function
    print(type(category_list))
    for i in range(len(category_list)):
        tmp_dic = {}
        tmp_dic["categoryId"] = category_list[i]['categoryId']
        tmp_dic["name"] = category_list[i]['name']
        res_data.append(tmp_dic)
    res_status = "success"
    res = {}
    res["status"] = "success"
    res["data"] = res_data
    # The structure samples of return data are as follows:
    # res = {
    #     "status": "success", # success or error
    #     "data": [
    #         {
    #             "categoryId": "category123",
    #             "name": "膝盖疼痛"
    #         },
    #         {
    #             "categoryId": "category456",
    #             "name": "肩膀损伤"
    #         }
    #     ]
    # }
    return json.dumps(res)

@app.route('/api/rehabilitation/knowledge', methods=["GET"])
def get_knowledge() -> Response | str:
    '''
    获取康复知识列表接口
    '''
    category_id = request.args.get('category', '')
    database = db.get_db()
    knowledge_all_list = database.execute(
        "SELECT * FROM rehabilitation_knowledge"
    ).fetchall()
    # This is an example returned data
    # res = {
    #     "status": "success",
    #     "data": [
    #         {
    #             "knowledgeId": "knowledge123",
    #             "title": "Exercise Techniques for Knee Rehabilitation",
    #             "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...",
    #             "image": "https://example.com/image.jpg",
    #             "video": "https://example.com/video.mp4",
    #             "source": "National Institute of Health",
    #             "timestamp": "2023-05-31T10:25:42Z"
    #         },
    #         {
    #             "knowledgeId": "knowledge456",
    #             "title": "Dietary Recommendations for Knee Pain",
    #             "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...",
    #             "image": None,
    #             "video": None,
    #             "source": "American Dietetic Association",
    #             "timestamp": "2023-05-29T16:40:12Z"
    #         }
    #     ]
    # }
    res = {}
    res_all_data = []
    for i in range(len(knowledge_all_list)):
        tmp_dic = {}
        tmp_dic["knowledgeId"] = knowledge_all_list[i]["knowledgeId"]
        tmp_dic["title"] = knowledge_all_list[i]["title"]
        tmp_dic["content"] = knowledge_all_list[i]["content"]
        tmp_dic["image"] = None
        tmp_dic["video"] = None
        tmp_dic["source"] = knowledge_all_list[i]["source"]
        tmp_dic["timestamp"] = str(knowledge_all_list[i]["timestamp"])
        res_all_data.append(tmp_dic)
    if len(category_id) == 0:
        # for now we should return whole data
        res["status"] = "success"
        res["data"] = res_all_data
    else:
        # for now we should only return required data
        res["status"] = "fail"
        knowledge_required_list = database.execute(
            "SELECT * FROM rehabilitation_knowledge WHERE categoryId = ?", (category_id,)
        ).fetchall()
        res_required_data = []
        for i in range(len(knowledge_required_list)):
            tmp_dic = {}
            tmp_dic["knowledgeId"] = knowledge_required_list[i]["knowledgeId"]
            tmp_dic["title"] = knowledge_required_list[i]["title"]
            tmp_dic["content"] = knowledge_required_list[i]["content"]
            tmp_dic["image"] = None
            tmp_dic["video"] = None
            tmp_dic["source"] = knowledge_required_list[i]["source"]
            tmp_dic["timestamp"] = str(knowledge_required_list[i]["timestamp"])
            res_required_data.append(tmp_dic)
        res["data"] = res_required_data
        res["status"] = "success"
    return json.dumps(res)

#--------------------------------------------------------------
#                      2.3 进度跟踪模块                        |
#--------------------------------------------------------------
@app.route('/api/rehabilitation/progress/<string:userId>', methods=["GET"])
def get_progress_data(userId) -> Response | str:
    '''
    获取康复进度数据接口
    '''
    # user_info = request.get_json()
    # print(user_info)
    res = {
        "status": "success", 
        "data": { 
            "userId": "user123", 
            "totalSessions": 20, 
            "completedSessions": 15, 
            "progressPercentage": 75, 
            "nextSessionDate": "2023-06-10" 
        }
    }
    return json.dumps(res)

@app.route('/api/rehabilitation/progress/report/<string:userId>', methods=["GET"])
def get_progress_report(userId) -> Response | str:
    '''
    获取进度报告接口
    '''
    # user_info = request.get_json()
    # print(user_info)
    res = {
        "status": "success", 
        "data": { 
            "userId": "user123", 
            "progressPercentage": "75%", 
            "report": "您的康复进度良好，已完成75%的训练计划。请继续保持，下一次训练的日期是2023-06-10。" 
        }
    }
    return json.dumps(res)

@app.route('/api/rehabilitation/progress/update', methods=["PUT"])
def update_progress() -> Response | str:
    '''
    更新康复进度接口
    '''
    user_info = request.get_json()
    print(user_info)
    res = {
        "status": "success", 
        "message": "康复进度更新成功"
    }
    return json.dumps(res)

@app.route('/api/rehabilitation/progress/detail/<string:userId>', methods=["GET"])
def get_progress_detail(userId) -> Response | str:
    '''
    获取详细进度数据
    '''
    # user_info = request.get_json()
    # print(user_info)
    res = {
        "status": "success", 
        "data": {
            "userId": "user123",
            "weight": [140.1, 141, 144.3, 142, 145, 147],
            "O2inblood": [93.4, 94, 94.2, 95, 95, 96]
        }
    }
    return json.dumps(res)

#--------------------------------------------------------------
#                      3.1 药物反馈模块                        |
#--------------------------------------------------------------
@app.route('/api/medication/feedback', methods=["POST"])
def submit_medication_feedback() -> Response | str:
    '''
    提交药物反馈接口
    '''
    user_info = request.get_json()

    patient = user_info['patientId']
    medication = user_info['medicationId']
    feedbackContent = user_info['feedbackContent']

    print(patient, medication, feedbackContent)

    # 获取当前时间
    current_time = datetime.now()

    # 将时间格式化为字符串
    time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # 存储到数据库中
    database = db.get_db()
    database.execute(
        "INSERT INTO medicine_feedback (patient, medicine, feedbackContent, feedbackDate) VALUES (?, ?, ?, ?)",
        (patient, medication, feedbackContent, time_string)
    )
    database.commit()

    res = {
        "status": "success", # success or error
        "message": "药物反馈提交成功"
    }
    return json.dumps(res)

@app.route('/api/medication/feedbacks/<string:medicationId>', methods=["GET"])
def get_medication_feedback(medicationId) -> Response | str:
    '''
    获取药物反馈列表接口
    '''
    database = db.get_db()

    user_feedback = database.execute(
        'SELECT * FROM medicine_feedback WHERE patient = ?', (session['userName'],)
    ).fetchall()

    if len(user_feedback) != 0:
        data = []
        for u in user_feedback:
            u_data = {
                    "feedbackId": u['feedbackId'],
                    "patientId": u['patient'],
                    "feedbackType": "text",
                    "feedbackContent": u['feedbackContent'],
                    "date": u['feedbackDate']
                    }
            data.append(u_data)

        res = {
            "status": "success",
            "data": data
        }
    else:
        res = {
            "status": "success",
            "data": [
                {
                    "feedbackId": "/",
                    "patientId": "/",
                    "feedbackType": "/",
                    "feedbackContent": "/",
                    "date": "/"
                }
            ]
        }
    return json.dumps(res)

#--------------------------------------------------------------
#                      3.2 问诊反馈模块                        |
#--------------------------------------------------------------
@app.route('/api/inquiry/feedback', methods=["POST"])
def submit_inquiry_feedback() -> Response | str:
    '''
    提交问诊反馈接口
    '''
    user_info = request.get_json()
    print(user_info)

    user_info = request.get_json()

    patient = user_info['patientId']
    doctor = user_info['doctorId']
    feedbackContent = user_info['feedbackContent']

    # 获取当前时间
    current_time = datetime.now()

    # 将时间格式化为字符串
    time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # 存储到数据库中
    database = db.get_db()
    database.execute(
        "INSERT INTO diagnose_feedback (patient, doctor, feedbackContent, feedbackDate) VALUES (?, ?, ?, ?)",
        (patient, doctor, feedbackContent, time_string)
    )
    database.commit()

    res =  {
        "status": "success",
        "message": "问诊反馈提交成功"
    }
    return json.dumps(res)

@app.route('/api/inquiry/feedbacks/<string:doctorId>', methods=["GET"])
def get_inquiry_feedback(doctorId) -> Response | str:
    '''
    获取问诊反馈列表接口
    '''
    database = db.get_db()

    user_feedback = database.execute(
        'SELECT * FROM diagnose_feedback WHERE patient = ?', (session['userName'],)
    ).fetchall()

    if len(user_feedback) != 0:
        data = []
        for u in user_feedback:
            u_data = {
                "feedbackId": u['feedbackId'],
                "patientId": u['patient'],
                "feedbackContent": u['feedbackContent'],
                "date": u['feedbackDate']
            }
            data.append(u_data)

        res = {
            "status": "success",
            "data": data
        }
    else:
        res = {
            "status": "success",
            "data": [
                {
                    "feedbackId": "/",
                    "patientId": "/",
                    "feedbackContent": "/",
                    "date": "/"
                }
            ]
        }
    return json.dumps(res)

if __name__ == "__main__":
    app.run(threaded=True, host="127.0.0.1", port=3001, debug=True)