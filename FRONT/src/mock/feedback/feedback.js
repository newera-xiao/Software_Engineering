const Mock = require('mockjs');

let typeData = (params) => {
    console.log('params: ', params)
    return Mock.mock({
        "status": "success",
        "message": "药物反馈提交成功"
    });
}

let data = (params) => {
    console.log('params: ', params)
    return Mock.mock({
        'status': 'success',
        'data|1-9': [{
            'feedbackId': 'feedback123',
            'patientId': 'patient123',
            'feedbackType|1': ['voice', 'text'],
            'feedbackContent|1': ['Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...', '药物效果良好，疼痛减轻', '疑信参半 却无比期盼', '你的惯犯 圆满', '别让纠缠 显得 孤单'],
            'date': '2023-06-01'
        }]
    });
}

let inquiryAddData = (params) => {
    console.log('params: ', params)
    return Mock.mock({
        "status": "success",
        "message": "问诊反馈提交成功"
    });
}

let inquiryData = (params) => {
    console.log('params: ', params)
    return Mock.mock({
        'status': 'success',
        'data|1-9': [{
            'feedbackId': 'feedback123',
            'patientId': 'patient123',
            'feedbackContent|1': ['非常满意医生的诊断结果，感谢医生的耐心和专业知识', '对医生的诊断结果有疑问，请进一步解释'],
            'date|1': ['2023-06-01', '2023-06-02']
        }]
    });
}

Mock.mock('/api/medication/feedback', 'post', typeData);
Mock.mock('/api/medication/feedbacks', 'get', data);

Mock.mock('/api/inquiry/feedback', 'post', inquiryAddData);
Mock.mock('/api/inquiry/feedbacks', 'get', inquiryData);