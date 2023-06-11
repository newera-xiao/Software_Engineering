<template>
    <div>
        <div class="header">
            <el-form :inline="true" :model="form" class="demo-form-inline">
                <el-form-item label="知识类型">
                    <el-select v-model="form.category" placeholder="请选择知识分类">
                        <el-option v-for="(item, inds) in options" :key="inds" :label="item.name" :value="item.categoryId">
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit">查询</el-button>
                </el-form-item>
            </el-form>
        </div>
        <el-table :data="tableData" border style="width: 100%">
            <el-table-column type="index" width="50" label="序号">
            </el-table-column>
            <el-table-column prop="title" label="康复知识标题">
            </el-table-column>
            <el-table-column prop="content" label="康复知识内容">
            </el-table-column>
            <el-table-column prop="source" label="康复知识来源">
            </el-table-column>
            <el-table-column prop="timestamp" label="发布时间" :formatter="dateFormat">
            </el-table-column>
        </el-table>
    </div>
</template>
<style scoped lang="scss">
* {
    box-sizing: border-box;
}
</style>
<script>
import { getTemp, getType } from '@/api/temp'
import { formatDate } from '@/utils/date'
export default {
    data() {
        return {
            form: {
                category: ''
            },
            options: [],
            tableData: [],
        }
    },
    methods: {
        getType() {
            getType().then(res => {
                console.log('res: ', res)
                this.options = res.data
            })
        },
        onSubmit() {
            this.query()
        },
        query() {
            let params = Object.assign({}, this.form)
            getTemp(params).then(res => {
                console.log('res: ', res)
                this.tableData = res.data
            })
        },
        dateFormat(row, column) {
            const daterc = row[column.property]
            return formatDate(new Date(daterc))
        },
    },
    mounted() {
        this.getType()
        this.query()
    }
}
</script>
  