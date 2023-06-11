<template>
    <div style="position: relative">
        <el-row :gutter="20">
            <el-col :span="24">
                <el-card class="box-card">
                    <el-descriptions title="康复计划详情" direction="vertical" :column="2" border>
                        <el-descriptions-item label="康复计划名称">{{ infoData.planName }}</el-descriptions-item>
                        <el-descriptions-item label="康复计划描述">{{ infoData.description }}</el-descriptions-item>
                        <el-descriptions-item label="康复锻炼项目数组" :span="2">
                            <el-table :data="infoData.exercises" stripe style="width: 100%">
                                <el-table-column prop="name" label="锻炼项目名称" width="180">
                                </el-table-column>
                                <el-table-column prop="description" label="锻炼项目描述" width="180">
                                </el-table-column>
                                <el-table-column prop="sets" label="组数">
                                </el-table-column>
                                <el-table-column prop="repetitions" label="每组次数">
                                </el-table-column>
                            </el-table>
                        </el-descriptions-item>
                    </el-descriptions>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>
<style scoped lang="scss" scoped>
.el-row {
    margin-bottom: 20px;
}

.box-card {
    .icon {
        width: 90px;
        height: 90px;
        font-size: 30px;
        text-align: center;
        line-height: 80px;
        color: #fff;
        background-color: #67c23a;
    }

    .detail {
        display: flex;
        flex-direction: column;
        justify-content: center;
        margin-left: 15px;

        .num {
            font-size: 26px;
            margin-bottom: 10px;
            line-height: 30px;
        }

        .text {
            font-size: 14px;
            text-align: center;
            color: #999;
        }
    }
}

.img-block {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 434px;

    .img {
        height: 400px;
    }
}
</style>
<script>
import { getPlans } from "@/api/plans"
import { formatDate } from "@/utils/date"

export default {
    data() {
        return {
            infoData: '',
            planId: '',
        }
    },
    methods: {
        getDetail() {
            // this.tableData = [{
            //     name: 'Exercise 1',
            //     description: 'Example exercise 1',
            //     sets: '3',
            //     repetitions: '10',
            // }, {
            //     name: 'Exercise 2',
            //     description: 'Example exercise 2',
            //     sets: '2',
            //     repetitions: '12',
            // }]

            getPlans({
                planId: this.planId
            }).then(res => {
                console.log('res: ', res)
                this.infoData = res.data
            })
        },
    },
    mounted() {
        this.getDetail()
    }
}
</script>
  