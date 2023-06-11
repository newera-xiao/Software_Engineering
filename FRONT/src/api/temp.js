import request from '@/utils/request'

export function getTemp(data) {
    let url = '/api/rehabilitation/knowledge?'
    if (data && data.hasOwnProperty('category') && data.category != '') {
        url = url.indexOf('?') == url.length - 1 ? `${url}category=${data.category}` : `${url}&category=${data.category}`
    }
    return request({
        url: url,
        method: 'get',
        data
    })
}

export function getType(data) {
    return request({
        url: '/api/rehabilitation/knowledge/categories',
        method: 'get',
        data
    })
}