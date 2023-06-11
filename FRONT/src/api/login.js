import request from '@/utils/request'

export function login(data) {
    return request({
        url: '/api/auth/login',
        method: 'post',
        data
    })
}

export function register(data) {
    return request({
        url: '/api/auth/register',
        method: 'post',
        data
    })
}

export function logout(data) {
    return request({
        url: '/api/auth/logout',
        method: 'post',
        data
    })
}

export function password(data) {
    return request({
        url: '/api/auth/user/password',
        method: 'put',
        data
    })
}