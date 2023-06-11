import request from '@/utils/request'

export function getPest(data) {
    let url = '/api/inquiry/feedbacks/doctor456'

    return request({
        url: url,
        method: 'get',
        data
    })
}

export function addPest(data) {
    return request({
        url: '/api/inquiry/feedback',
        method: 'post',
        data
    })
}

export function editPest(data) {
    console.log(data._id)
    return request({
        url: `/api/pest/${data._id}`,
        method: 'patch',
        data
    })
}

export function delPest(id) {
    return request({
        url: `/api/pest/${id}`,
        method: 'delete',
        data: {}
    })
}