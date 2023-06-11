import request from '@/utils/request'

export function getPlans(data) {
    let url = '/api/rehabilitation/plans'
    return request({
        url: url,
        method: 'get',
        data
    })
}