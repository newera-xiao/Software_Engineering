<template>
    <div>
        <div class="header">
            <el-button type="primary" @click="addWater">+ 新增</el-button>
        </div>
        <el-table :data="tableData" border style="width: 100%">
            <el-table-column type="index" width="50" label="序号">
            </el-table-column>
            <el-table-column prop="feedbackId" label="反馈ID">
            </el-table-column>
            <el-table-column prop="patientId" label="病人ID">
            </el-table-column>
            <!-- <el-table-column prop="feedbackType" label="反馈类型">
            </el-table-column> -->
            <el-table-column prop="feedbackContent" label="反馈内容">
            </el-table-column>
            <el-table-column prop="date" label="反馈日期">
            </el-table-column>
        </el-table>

        <el-dialog :title="isEdit ? '编辑' : '新增'" :visible.sync="dialogVisible" width="50%" :before-close="handleClose">

            <el-form ref="form" :model="form" :rules="rules" label-width="80px">
                <el-form-item label="患者ID" prop="patientId">
                    <el-input placeholder="请输入患者ID" v-model="form.patientId"></el-input>
                </el-form-item>
                <el-form-item label="药物ID" prop="medicationId">
                    <el-input placeholder="请输入药物ID" v-model="form.medicationId"></el-input>
                </el-form-item>
                <!-- <el-form-item label="反馈类型" prop="feedbackType">
                    <el-input placeholder="选择反馈类型" v-model="form.feedbackType"></el-input>
                </el-form-item> -->
                <el-form-item label="反馈内容" prop="feedbackContent">
                    <el-input placeholder="请输入反馈内容" v-model="form.feedbackContent"></el-input>
                </el-form-item>
            </el-form>

            <span slot="footer" class="dialog-footer">
                <el-button @click="handleClose">取 消</el-button>
                <el-button type="primary" @click="confirmSubmit">确 定</el-button>
            </span>
        </el-dialog>
    </div>
</template>
<style scoped lang="scss">
* {
    box-sizing: border-box;
}

.header {
    margin-bottom: 20px;
}
</style>
<script>
import { getFeedback, addFeedback, editWater, delWater } from '@/api/water'
import { formatDate } from '@/utils/date'
export default {
    data() {
        return {
            medicationId: 'medication456',
            form: {
                patientId: '',
                medicationId: '',
                feedbackType: '',
                feedbackContent: ''
            },
            pickerOptions: {
                shortcuts: [{
                    text: '今天',
                    onClick(picker) {
                        picker.$emit('pick', new Date());
                    }
                }, {
                    text: '昨天',
                    onClick(picker) {
                        const date = new Date();
                        date.setTime(date.getTime() - 3600 * 1000 * 24);
                        picker.$emit('pick', date);
                    }
                }, {
                    text: '一周前',
                    onClick(picker) {
                        const date = new Date();
                        date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
                        picker.$emit('pick', date);
                    }
                }]
            },
            rules: {
                patientId: [
                    { required: true, message: '请输入患者ID', trigger: 'blur' }
                ],
                medicationId: [
                    { required: true, message: '请输入药物ID', trigger: 'blur' }
                ],
                feedbackContent: [
                    { required: true, message: '请输入反馈内容', trigger: 'blur' }
                ]
            },
            tableData: [],
            dialogVisible: false,
            isEdit: false,
        }
    },
    methods: {
        // 新增温度
        addWater() {
            this.isEdit = false
            this.dialogVisible = true
        },
        //提交表单
        confirmSubmit() {
            this.$refs.form.validate((valid) => {
                if (valid) {
                    if (this.isEdit) {
                        let params = Object.assign({}, this.form)
                        editWater(params).then(res => {
                            if (res.status == 'success') {
                                this.$message.success('修改成功')
                            }
                        })
                    } else {
                        addFeedback(this.form).then(res => {
                            console.log('res: ', res)
                            if (res.status == 'success') {
                                this.$message.success('添加成功')
                            }
                        })
                    }


                    this.query()
                    this.handleClose()
                }
            })
        },
        //弹窗关闭的时候
        handleClose() {
            this.form = {
                patientId: '',
                medicationId: '',
                feedbackType: '',
                feedbackContent: ''
            }
            this.$refs.form.resetFields()
            this.dialogVisible = false
        },
        query() {
            getFeedback({ medicationId: this.medicationId }).then(res => {
                this.tableData = res.data
            })
        },
        dateFormat(row, column) {
            const daterc = row[column.property]
            return formatDate(new Date(daterc))
        },
    },
    mounted() {
        this.query()
    }
}
</script>
  