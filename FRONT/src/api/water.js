import request from '@/utils/request'

export function getFeedback(data) {
    let url = '/api/medication/feedbacks/medication456'
    return request({
        url: url,
        method: 'get',
        data
    })
}

export function addFeedback(data) {
    return request({
        url: '/api/medication/feedback',
        method: 'post',
        data
    })
}