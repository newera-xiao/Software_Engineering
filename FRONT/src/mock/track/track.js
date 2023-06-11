const Mock = require('mockjs');

let typeData = () => {
    return Mock.mock({
        "status": "success",
        'data': {
            "userId": "user123",
            "progressPercentage": 75,
            "report": "您的康复进度良好，已完成75%的训练计划。请继续保持，下一次训练的日期是2023-06-10。"
        },
    });
}

let data = (params) => {
    console.log('params: ', params)
    return Mock.mock({
        'status': 'success',
        'data': {
            'userId|1': ['user123'],
            'totalSessions|1': [19, 20, 21, 22, 23],
            'completedSessions|1': [15, 16, 17, 14],
            'progressPercentage': 75,
            'nextSessionDate': '2023-06-10'
        }
    });
}

let detailData = (params) => {
    console.log('params: ', params)
    return Mock.mock({
        'status': 'success',
        'data': {
            "userId": "user123",
            "weight": [140.1, 141, 144.3, 142, 145, 147],
            "O2inblood": [93.4, 94, 94.2, 95, 95, 96]
        }
    });
}

Mock.mock('/api/rehabilitation/progress/report', 'get', typeData);
Mock.mock('/api/rehabilitation/progress', 'get', data);
Mock.mock('/api/rehabilitation/progress/detail', 'get', detailData);