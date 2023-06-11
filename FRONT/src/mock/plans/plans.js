const Mock = require('mockjs');

let data = (params) => {
    console.log('params: ', params)
    return Mock.mock({
        "status": "success",
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
    });
}

Mock.mock('/api/rehabilitation/plans', 'get', data);