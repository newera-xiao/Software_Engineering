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
    # English version
    # res = {
    #     "status": "success",
    #     "data": {
    #         "planId": "plan123",
    #         "planName": "Rehabilitation Plan",
    #         "description": "This is a comprehensive rehabilitation plan for your recovery.",
    #         "exercises": [
    #             {
    #                 "name": "Quadriceps Strengthening",
    #                 "description": "Perform quadriceps strengthening exercises to improve muscle strength and stability in the front of your thigh.",
    #                 "sets": 3,
    #                 "repetitions": 10
    #             },
    #             {
    #                 "name": "Shoulder Range of Motion",
    #                 "description": "Perform shoulder range of motion exercises to improve flexibility and mobility in your shoulder joint.",
    #                 "sets": 2,
    #                 "repetitions": 12
    #             },
    #             {
    #                 "name": "Core Stability Training",
    #                 "description": "Engage in core stability exercises to strengthen your abdominal and back muscles, improving stability and reducing the risk of injury.",
    #                 "sets": 3,
    #                 "repetitions": 15
    #             },
    #             {
    #                 "name": "Balance and Proprioception",
    #                 "description": "Practice balance and proprioception exercises to enhance your body's sense of position and control, reducing the risk of falls and improving coordination.",
    #                 "sets": 2,
    #                 "repetitions": 10
    #             },
    #             {
    #                 "name": "Cardiovascular Endurance",
    #                 "description": "Engage in cardiovascular exercises, such as brisk walking or cycling, to improve your overall endurance and cardiovascular health.",
    #                 "sets": 1,
    #                 "repetitions": "20 minutes"
    #             },
    #             {
    #                 "name": "Ankle Strengthening",
    #                 "description": "Perform ankle strengthening exercises to improve stability and strength in your ankle joint.",
    #                 "sets": 3,
    #                 "repetitions": 12
    #             },
    #             {
    #                 "name": "Hip Flexor Stretch",
    #                 "description": "Stretch your hip flexor muscles to improve flexibility and reduce tightness in your hip area.",
    #                 "sets": 2,
    #                 "repetitions": 10
    #             },
    #             {
    #                 "name": "Posture Correction",
    #                 "description": "Practice exercises and techniques to improve your posture and alignment, reducing strain on your muscles and joints.",
    #                 "sets": 2,
    #                 "repetitions": 10
    #             },
    #             {
    #                 "name": "Spinal Mobility Exercises",
    #                 "description": "Perform spinal mobility exercises to improve flexibility and range of motion in your spine.",
    #                 "sets": 3,
    #                 "repetitions": 12
    #             },
    #             {
    #                 "name": "Wrist Strengthening",
    #                 "description": "Engage in wrist strengthening exercises to improve grip strength and stability in your wrist joint.",
    #                 "sets": 3,
    #                 "repetitions": 10
    #             },
    #             {
    #                 "name": "Neck Stretching",
    #                 "description": "Stretch your neck muscles to relieve tension, improve flexibility, and reduce neck pain.",
    #                 "sets": 2,
    #                 "repetitions": 10
    #             },
    #             {
    #                 "name": "Hamstring Strengthening",
    #                 "description": "Perform hamstring strengthening exercises to improve strength and flexibility in the back of your thigh.",
    #                 "sets": 3,
    #                 "repetitions": 12
    #             },
    #             {
    #                 "name": "Rotator Cuff Exercises",
    #                 "description": "Engage in rotator cuff exercises to strengthen the muscles and tendons around your shoulder joint, improving stability and preventing injury.",
    #                 "sets": 3,
    #                 "repetitions": 12
    #             },
    #             {
    #                 "name": "Glute Activation",
    #                 "description": "Activate and strengthen your gluteal muscles to improve hip stability and reduce the risk of lower body injuries.",
    #                 "sets": 3,
    #                 "repetitions": 10
    #             },
    #             {
    #                 "name": "Lower Back Stretch",
    #                 "description": "Stretch your lower back muscles to relieve tension, improve flexibility, and alleviate lower back pain.",
    #                 "sets": 2,
    #                 "repetitions": 10
    #             },
    #             {
    #                 "name": "Calf Strengthening",
    #                 "description": "Perform calf strengthening exercises to improve strength and stability in your calf muscles.",
    #                 "sets": 3,
    #                 "repetitions": 12
    #             },
    #             {
    #                 "name": "Pectoral Stretch",
    #                 "description": "Stretch your pectoral muscles to improve flexibility and reduce tightness in your chest area.",
    #                 "sets": 2,
    #                 "repetitions": 10
    #             },
    #             {
    #                 "name": "Lateral Band Walk",
    #                 "description": "Perform lateral band walks to activate and strengthen your hip abductor muscles, improving hip stability and reducing the risk of knee injuries.",
    #                 "sets": 2,
    #                 "repetitions": 10
    #             },
    #             {
    #                 "name": "Tricep Dips",
    #                 "description": "Engage in tricep dips to strengthen and tone your tricep muscles, improving arm strength and stability.",
    #                 "sets": 3,
    #                 "repetitions": 12
    #             },
    #             {
    #                 "name": "Ankle Mobility Exercises",
    #                 "description": "Perform ankle mobility exercises to improve flexibility and range of motion in your ankle joint.",
    #                 "sets": 2,
    #                 "repetitions": 10
    #             }
    #         ]
    #     }
    # }

    res = {
        "status": "success",
        "data": {
            "planId": "plan123",
            "planName": "康复计划",
            "description": "这是一个综合性的康复计划，旨在帮助您进行康复训练。",
            "exercises": [
                {
                    "name": "股四头肌强化",
                    "description": "进行股四头肌强化运动，以改善大腿前侧肌肉的力量和稳定性。",
                    "sets": 3,
                    "repetitions": 10
                },
                {
                    "name": "肩关节活动",
                    "description": "进行肩关节活动运动，以改善肩关节的灵活性和活动范围。",
                    "sets": 2,
                    "repetitions": 12
                },
                {
                    "name": "核心稳定性训练",
                    "description": "进行核心稳定性训练，以加强腹部和背部肌肉，提高稳定性，减少受伤风险。",
                    "sets": 3,
                    "repetitions": 15
                },
                {
                    "name": "平衡和本体感知",
                    "description": "进行平衡和本体感知训练，增强身体的位置感知和控制能力，减少摔倒风险，提高协调性。",
                    "sets": 2,
                    "repetitions": 10
                },
                {
                    "name": "心血管耐力",
                    "description": "进行心血管运动，如快走或骑车，以提高整体耐力和心血管健康。",
                    "sets": 1,
                    "repetitions": "20分钟"
                },
                {
                    "name": "踝关节强化",
                    "description": "进行踝关节强化运动，以增强踝关节的稳定性和力量。",
                    "sets": 3,
                    "repetitions": 12
                },
                {
                    "name": "髋屈肌伸展",
                    "description": "进行髋屈肌伸展运动，以改善髋部区域的灵活性，减少紧张感。",
                    "sets": 2,
                    "repetitions": 10
                },
                {
                    "name": "姿势矫正",
                    "description": "练习姿势矫正的运动和技巧，改善姿势和对齐，减少肌肉和关节的负担。",
                    "sets": 2,
                    "repetitions": 10
                },
                {
                    "name": "脊柱活动性训练",
                    "description": "进行脊柱活动性训练，以提高脊柱的灵活性和活动范围。",
                    "sets": 3,
                    "repetitions": 12
                },
                {
                    "name": "腕部强化",
                    "description": "进行腕部强化运动，以提高握力和腕关节的稳定性。",
                    "sets": 3,
                    "repetitions": 10
                },
                {
                    "name": "颈部伸展",
                    "description": "进行颈部伸展运动，缓解紧张感，改善颈部的灵活性，减少颈部疼痛。",
                    "sets": 2,
                    "repetitions": 10
                },
                {
                    "name": "腿后肌群强化",
                    "description": "进行腿后肌群强化运动，以增强大腿后侧的力量和灵活性。",
                    "sets": 3,
                    "repetitions": 12
                },
                {
                    "name": "旋转袖肌训练",
                    "description": "进行旋转袖肌训练，以增强肩关节周围的肌肉和肌腱，提高稳定性，预防受伤。",
                    "sets": 3,
                    "repetitions": 12
                },
                {
                    "name": "臀部激活",
                    "description": "激活和强化臀部肌肉，以改善髋部稳定性，降低下肢受伤风险。",
                    "sets": 3,
                    "repetitions": 10
                },
                {
                    "name": "腰部伸展",
                    "description": "进行腰部伸展运动，缓解紧张感，改善腰部的灵活性，缓解腰背疼痛。",
                    "sets": 2,
                    "repetitions": 10
                },
                {
                    "name": "小腿肌群强化",
                    "description": "进行小腿肌群强化运动，以增强小腿肌肉的稳定性和力量。",
                    "sets": 3,
                    "repetitions": 12
                },
                {
                    "name": "胸肌伸展",
                    "description": "进行胸肌伸展运动，以改善胸部区域的灵活性，减少紧张感。",
                    "sets": 2,
                    "repetitions": 10
                },
                {
                    "name": "侧面橡皮筋行走",
                    "description": "进行侧面橡皮筋行走，激活和强化髋部外展肌群，提高髋部稳定性，减少膝关节受伤风险。",
                    "sets": 2,
                    "repetitions": 10
                },
                {
                    "name": "三头肌屈臂伸展",
                    "description": "进行三头肌屈臂伸展，增强和塑造三头肌肌肉，提高手臂力量和稳定性。",
                    "sets": 3,
                    "repetitions": 12
                },
                {
                    "name": "踝关节活动性训练",
                    "description": "进行踝关节活动性训练，以提高踝关节的灵活性和活动范围。",
                    "sets": 2,
                    "repetitions": 10
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