const Mock = require('mockjs');

let typeData = () => {
    return Mock.mock({
        "status": "success",
        'data': [{
            "categoryId": "category123",
            "name": "膝盖疼痛"
        },
        {
            "categoryId": "category456",
            "name": "肩膀损伤"
        }]
    });
}

let data = (params) => {
    console.log('params: ', params)
    return Mock.mock({
        'status': 'success',
        'data|1-9': [{
            'knowledgeId|+1': 1,
            'title|1': ['Exercise Techniques for Knee Rehabilitation'],
            'content|1': ['Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...', '理由太短 是让人不安', '疑信参半 却无比期盼', '你的惯犯 圆满', '别让纠缠 显得 孤单'],
            'source|1': ['National Institute of Health', '试听', '喜欢'],
            'timestamp': '2023-05-31T10:25:42Z'
        }]
    });
}

Mock.mock('/api/rehabilitation/knowledge/categories', 'get', typeData);
Mock.mock('/api/rehabilitation/knowledge', 'get', data);