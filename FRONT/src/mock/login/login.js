const Mock = require('mockjs');

let loginData = (params) => {
    console.log('params: ', params)
    return Mock.mock({
        "userId": "123456",
        "username": "example_user",
        "accessToken": "example_token"
    });
}

let registerData = (params) => {
    console.log('params: ', params)
    return Mock.mock({
        "status": "success",
        "data": {
            "message": "Registration successful"
        }
    });
}

let logoutData = (params) => {
    console.log('params: ', params)
    return Mock.mock({
        "status": "success",
        "data": {
            "message": "Logout successful"
        }
    });
}

let passwordData = (params) => {
    console.log('params: ', params)
    return Mock.mock({
        "status": "success",
        "data": {
            "message": "Password updated successfully"
        }
    });
}

Mock.mock('/api/auth/login', 'post', loginData);
Mock.mock('/api/auth/register', 'post', registerData);
Mock.mock('/api/auth/logout', 'post', logoutData);
Mock.mock('/api/auth/user/password', 'put', passwordData);