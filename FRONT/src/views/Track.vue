<template>
    <div>
        <el-card class="box-card mg-bottom-20">
            <el-descriptions title="康复进度" direction="vertical" :column="2" border>
                <el-descriptions-item label="康复计划的总训练次数">{{ info.totalSessions }}</el-descriptions-item>
                <el-descriptions-item label="已完成的训练次数">{{ info.completedSessions }}</el-descriptions-item>
                <el-descriptions-item label="康复进度百分比">{{ info.progressPercentage }}</el-descriptions-item>
                <el-descriptions-item label="下一次训练的日期">{{ info.nextSessionDate }}</el-descriptions-item>
                <el-descriptions-item label="详细进度" :span="2">
                    <div ref="chart1" style="width: 1090px; height: 300px;"></div>
                    <div ref="chart2" style="width: 1090px; height: 300px;"></div>
                </el-descriptions-item>
            </el-descriptions>
        </el-card>

        <el-card class="box-card">
            <el-descriptions title="进度报告" direction="vertical" :column="2" border>
                <el-descriptions-item label="康复进度百分比">{{ report.progressPercentage }}</el-descriptions-item>
                <el-descriptions-item label="进度报告内容">{{ report.report }}</el-descriptions-item>
            </el-descriptions>
        </el-card>
    </div>
</template>
<style scoped lang="scss">
* {
    box-sizing: border-box;
}
</style>
<script>
import { getProgress, getReport, getDetail } from '@/api/track'
import { formatDate } from '@/utils/date'
export default {
    data() {
        return {
            userId: '',
            info: '',
            report: '',
            yAxis: [],
            yAxis2: [],
            yAxisMin: 0,
            yAxisMin2: 0,
        }
    },
    methods: {
        onSubmit() {
            this.query()
        },
        query() {
            getProgress({ userId: this.userId }).then(res => {
                console.log('res: ', res)
                this.info = res.data
            })

            getReport({ userId: this.userId }).then(res => {
                console.log('res: ', res)
                this.report = res.data
            })
        },
        dateFormat(row, column) {
            const daterc = row[column.property]
            return formatDate(new Date(daterc))
        },

        getLineChart() {
            getDetail({ userId: this.userId }).then(res => {
                console.log('res: ', res)
                let yAxis = []
                let yAxis2 = []
                res.data.weight.forEach(item => {
                    yAxis.push(item)
                })
                res.data.O2inblood.forEach(item => {
                    yAxis2.push(item)

                })
                this.yAxis = yAxis
                this.yAxis2 = yAxis2

                this.yAxisMin = Math.min(...this.yAxis) - 3
                this.yAxisMin2 = Math.min(...this.yAxis2) - 3
                this.setLineChart()
                this.setLineChart2()
            })
        },
        setLineChart() {
            let chartDom = this.$refs.chart1;
            let myChart = this.$echarts.init(chartDom);
            let option = {
                color: '#67c23a',
                title: {
                    text: '体重变化趋势',
                    textStyle: {
                        fontSize: '24px'
                    }
                },
                tooltip: {
                    trigger: 'axis'
                },
                legend: {},
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: ['第一周', '第二周', '第三周', '第四周', '第五周', '第六周']
                },
                yAxis: {
                    type: 'value',
                    min: this.yAxisMin,
                    axisLabel: {
                        formatter: '{value}'
                    }
                },
                series: [
                    {
                        name: '体重',
                        type: 'line',
                        data: this.yAxis,   //[10, 11, 13, 11, 12, 12, 9],
                        markPoint: {
                            data: [
                                { type: 'max', name: 'Max', label: { color: '#fff' } },
                                { type: 'min', name: 'Min', label: { color: '#fff' } }
                            ]
                        },
                        markLine: {
                            data: [{ type: 'average', name: 'Avg' }]
                        }
                    }
                ]
            };

            option && myChart.setOption(option);
        },
        setLineChart2() {
            let chartDom = this.$refs.chart2;
            let myChart = this.$echarts.init(chartDom);
            let option = {
                color: '#fc4747',
                title: {
                    text: '血氧含量变化趋势',
                    textStyle: {
                        fontSize: '24px'
                    }
                },
                tooltip: {
                    trigger: 'axis'
                },
                legend: {},
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: ['第一周', '第二周', '第三周', '第四周', '第五周', '第六周']
                },
                yAxis: {
                    type: 'value',
                    min: this.yAxisMin2,
                    axisLabel: {
                        formatter: '{value}'
                    }
                },
                series: [
                    {
                        name: '血氧含量',
                        type: 'line',
                        data: this.yAxis2,   //[10, 11, 13, 11, 12, 12, 9],
                        markPoint: {
                            data: [
                                { type: 'max', name: 'Max', label: { color: '#fff' } },
                                { type: 'min', name: 'Min', label: { color: '#fff' } }
                            ]
                        },
                        markLine: {
                            data: [{ type: 'average', name: 'Avg' }]
                        }
                    },
                ]
            };

            option && myChart.setOption(option);
        },
    },
    created() {
        this.userId = JSON.parse(localStorage.getItem('userInfo')).userId
        console.log('userId: ', this.userId)
    },
    mounted() {
        this.query()
        this.getLineChart()
    }
}
</script>
  