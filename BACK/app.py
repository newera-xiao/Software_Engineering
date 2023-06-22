import os
import json
import db
from flask import Flask, Response, request, session
# from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'database.sqlite'),
    )
db.init_app(app)

def init_knowledge_base():
    database = db.get_db()
    database.execute(
        "INSERT INTO rehabilitation_categories (categoryId, name) VALUES ('category1', '膝盖疼痛'), ('category2', '肩膀损伤'), ('category3', '脊柱问题'), ('category4', '康复理论'), ('category5', '骨折康复')"
    )
    database.commit()
    database.execute(
        "INSERT INTO rehabilitation_knowledge (knowledgeId, categoryId, title, content, image, video, source, timestamp) VALUES \
        ('knowledge1', 'category1', '常见膝盖疼痛问题及处理方法', '在康复过程中，膝盖疼痛是常见问题之一。本文介绍了膝盖疼痛的常见原因及相应的处理方法。', NULL, NULL, '医学杂志A', '2023-06-01 09:30:00'), \
        ('knowledge2', 'category1', '膝盖疼痛康复运动示例', '这是一份膝盖疼痛康复运动示例，包括了针对不同类型膝盖疼痛的运动方法和注意事项。', NULL, NULL, '康复学会B', '2023-06-02 14:15:00'), \
        ('knowledge3', 'category1', '膝关节保护指南', '如何保护膝关节，预防膝关节损伤？本文提供了一些建议和指南，帮助您更好地保护您的膝关节。', NULL, NULL, '健康杂志C', '2023-06-03 16:45:00'), \
        ('knowledge4', 'category1', '膝关节炎的饮食建议', '膝关节炎患者在日常饮食中应该注意哪些事项？本文提供了一些膝关节炎患者的饮食建议和禁忌。', NULL, NULL, '饮食杂志D', '2023-06-04 10:10:00'), \
        ('knowledge5', 'category1', '膝盖疼痛的常见治疗方法', '膝盖疼痛的治疗方法多种多样，本文总结了常见的治疗方法，帮助患者找到适合自己的治疗方案。', NULL, NULL, '医学杂志E', '2023-06-05 12:20:00'), \
        ('knowledge6', 'category2', '肩膀损伤的症状和诊断', '肩膀损伤有哪些常见的症状和诊断方法？本文介绍了肩膀损伤常见的症状和诊断技术。', NULL, NULL, '医学杂志F', '2023-06-06 09:30:00'), \
        ('knowledge7', 'category2', '肩膀损伤的康复训练', '针对不同类型的肩膀损伤，康复训练是非常重要的一部分。本文提供了一些肩膀损伤康复训练的示例。', NULL, NULL, '康复学会G', '2023-06-07 14:15:00'), \
        ('knowledge8', 'category2', '肩袖损伤的手术治疗', '肩袖损伤需要进行手术治疗的情况较多，本文介绍了肩袖损伤手术治疗的方法和注意事项。', NULL, NULL, '外科杂志H', '2023-06-08 16:45:00'), \
        ('knowledge9', 'category2', '肩膀损伤的康复护理', '肩膀损伤患者在康复过程中需要注意哪些护理事项？本文提供了一些建议和指导。', NULL, NULL, '护理杂志I', '2023-06-09 10:10:00'), \
        ('knowledge10', 'category2', '肩膀损伤的康复辅助器具', '在肩膀损伤康复过程中，一些辅助器具可以起到帮助和支持的作用。本文介绍了常见的康复辅助器具。', NULL, NULL, '康复学报J', '2023-06-10 12:20:00')"
    )
    database.commit()
    database.execute(
        "INSERT INTO rehabilitation_knowledge (knowledgeId, categoryId, title, content, image, video, source, timestamp) VALUES \
        ('knowledge11', 'category3', '脊柱问题的常见症状和治疗', '脊柱问题可能导致背部疼痛和其他症状。本文介绍了常见的脊柱问题症状和治疗方法。', NULL, NULL, '医学杂志K', '2023-06-11 09:30:00'), \
        ('knowledge12', 'category3', '脊柱问题的物理疗法', '物理疗法在脊柱问题的康复中起到重要作用。本文介绍了常见的脊柱问题物理疗法方法和注意事项。', NULL, NULL, '康复学会L', '2023-06-12 14:15:00'), \
        ('knowledge13', 'category3', '脊柱问题的手术治疗', '一些严重的脊柱问题可能需要进行手术治疗。本文介绍了脊柱问题手术治疗的方法和风险。', NULL, NULL, '外科杂志M', '2023-06-13 16:45:00'), \
        ('knowledge14', 'category3', '脊柱问题的康复体操', '脊柱问题的康复体操可以帮助增强脊柱肌肉和改善姿势。本文提供了一些脊柱问题康复体操示例。', NULL, NULL, '康复学报N', '2023-06-14 10:10:00'), \
        ('knowledge15', 'category3', '预防脊柱问题的方法', '如何预防脊柱问题的发生？本文提供了一些预防脊柱问题的方法和建议。', NULL, NULL, '健康杂志O', '2023-06-15 12:20:00')"
    )
    database.commit()
    database.execute(
        "INSERT INTO rehabilitation_knowledge (knowledgeId, categoryId, title, content, image, video, source, timestamp) VALUES \
        ('knowledge16', 'category4', '康复理论概述', '康复理论是康复医学的基础，本文对康复理论的基本概念和原则进行了介绍。', NULL, NULL, '医学杂志P', '2023-06-16 09:30:00'), \
        ('knowledge17', 'category4', '康复评估与测量', '康复评估和测量是确定患者康复进程和效果的重要手段。本文介绍了常用的康复评估和测量方法。', NULL, NULL, '康复学会Q', '2023-06-17 14:15:00'), \
        ('knowledge18', 'category4', '康复计划制定与执行', '康复计划的制定和执行是康复治疗的核心步骤。本文介绍了康复计划的制定和执行策略。', NULL, NULL, '康复学报R', '2023-06-18 16:45:00'), \
        ('knowledge19', 'category4', '康复研究与进展', '康复研究不断推动康复医学的发展。本文概述了近期康复研究的一些重要进展和成果。', NULL, NULL, '医学杂志S', '2023-06-19 10:10:00'), \
        ('knowledge20', 'category4', '康复专家的角色与责任', '康复专家在康复治疗中起着重要的角色。本文探讨了康复专家的角色与责任。', NULL, NULL, '康复学会T', '2023-06-20 12:20:00')"
    )
    database.commit()
    database.execute(
        "INSERT INTO rehabilitation_knowledge (knowledgeId, categoryId, title, content, image, video, source, timestamp) VALUES \
        ('knowledge21', 'category5', '骨折康复的基本原则', '骨折康复的基本原则是保护骨折部位并促进骨折愈合。本文介绍了骨折康复的基本原则和注意事项。', NULL, NULL, '医学杂志U', '2023-06-21 09:30:00'), \
        ('knowledge22', 'category5', '骨折康复的康复训练', '骨折康复训练有助于恢复骨折部位的功能和力量。本文提供了一些骨折康复训练的示例和指导。', NULL, NULL, '康复学会V', '2023-06-22 14:15:00'), \
        ('knowledge23', 'category5', '骨折康复的日常护理', '骨折康复期间需要注意一些日常护理事项，以促进骨折愈合。本文提供了一些建议和指导。', NULL, NULL, '护理杂志W', '2023-06-23 16:45:00'), \
        ('knowledge24', 'category5', '骨折康复的营养建议', '合理的营养摄入对于骨折康复至关重要。本文介绍了骨折康复期间的营养建议和饮食指导。', NULL, NULL, '营养学刊X', '2023-06-24 10:10:00'), \
        ('knowledge25', 'category5', '骨折康复的心理支持', '骨折康复期间的心理支持对于患者的康复非常重要。本文提供了一些心理支持的方法和建议。', NULL, NULL, '心理学杂志Y', '2023-06-25 12:20:00')"
    )
    database.commit()

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
    print(user_info)
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
    # user_info = request.get_json()
    # print(user_info)
    res =  {
        "status": "success",
        "data": [
            {
                "feedbackId": "feedback123",
                "patientId": "patient123",
                "feedbackType": "text",
                "feedbackContent": "药物效果良好，疼痛减轻",
                "date": "2023-06-01"
            },
            {
                "feedbackId": "feedback456",
                "patientId": "patient456",
                "feedbackType": "voice",
                "feedbackContent": "语音反馈的文本转录内容",
                "date": "2023-06-02"
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
    # user_info = request.get_json()
    # print(user_info)
    res =   {
        "status": "success",
        "data": [
            {
                "feedbackId": "feedback123",
                "patientId": "patient123",
                "feedbackContent": "非常满意医生的诊断结果，感谢医生的耐心和专业知识",
                "date": "2023-06-01"
            },
            {
                "feedbackId": "feedback456",
                "patientId": "patient456",
                "feedbackContent": "对医生的诊断结果有疑问，请进一步解释",
                "date": "2023-06-02"
            }
        ]
    }
    return json.dumps(res)

if __name__ == "__main__":
    app.run(threaded=True, host="127.0.0.1", port=3001, debug=True)