import request from '@/utils/request'

export function getProgress(data) {
    let url = '/api/rehabilitation/progress/'+data.userId
    // if (data && data.hasOwnProperty('category')) {
    //     url = url.indexOf('?') == url.length - 1 ? `${url}category=${data.category}` : `${url}&category=${data.category}`
    // }
    return request({
        url: url,
        method: 'get',
        data
    })
}

export function getReport(data) {
    return request({
        url: '/api/rehabilitation/progress/report/'+data.userId,
        method: 'get',
        data
    })
}

export function getDetail(data) {
    console.log('data: ',data)
    return request({
        // url: '/api/rehabilitation/progress/detail',
        url: '/api/rehabilitation/progress/detail/'+data.userId,
        method: 'get',
        data
    })
}