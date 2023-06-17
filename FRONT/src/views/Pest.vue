<template>
    <div>
        <div class="header">
            <el-button type="primary" @click="addPest">+ 新增</el-button>
        </div>
        <el-table :data="tableData" border style="width: 100%">
            <el-table-column type="index" width="50" label="序号">
            </el-table-column>
            <el-table-column prop="feedbackId" label="反馈ID">
            </el-table-column>
            <el-table-column prop="patientId" label="病人ID">
            </el-table-column>
            <el-table-column prop="feedbackContent" label="反馈内容">
            </el-table-column>
            <el-table-column prop="date" label="反馈日期" :formatter="dateFormat">
            </el-table-column>
        </el-table>

        <el-dialog :title="isEdit ? '编辑' : '新增'" :visible.sync="dialogVisible" width="50%" :before-close="handleClose">

            <el-form ref="editForm" :model="editForm" :rules="rules" label-width="80px">
                <el-form-item label="病人ID" prop="patientId">
                    <el-input placeholder="请输入病人ID" v-model="editForm.patientId"></el-input>
                </el-form-item>
                <el-form-item label="医生ID" prop="doctorId">
                    <el-input placeholder="请输入医生ID" v-model="editForm.doctorId"></el-input>
                </el-form-item>
                <el-form-item label="反馈内容" prop="feedbackContent">
                    <el-input v-model="editForm.feedbackContent"></el-input>
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
import { getPest, addPest, editPest, delPest } from '@/api/pest'
import { formatDate } from '@/utils/date'
export default {
    data() {
        return {
            doctorId: 'doctor456',
            editForm: {
                patientId: '',
                doctorId: '',
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
                feedbackId: [
                    { required: true, message: '请输入反馈ID', trigger: 'blur' }
                ]
            },
            tableData: [],
            dialogVisible: false,
            isEdit: false,
        }
    },
    methods: {
        // 新增农药
        addPest() {
            this.isEdit = false
            this.dialogVisible = true
        },
        //提交表单
        confirmSubmit() {
            this.$refs.editForm.validate((valid) => {
                if (valid) {
                    if (this.isEdit) {
                        let params = Object.assign({}, this.editForm)
                        editPest(params).then(res => {
                            if (res.status == 'success') {
                                this.$message.success('修改成功')
                            } else {
                                this.$message.error(`修改失败：${res.data.message}`)
                            }
                        })
                    } else {
                        addPest(this.editForm).then(res => {
                            console.log('res: ',res)
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
            this.editForm = {
                patientId: '',
                doctorId: '',
                feedbackContent: ''
            }
            this.$refs['editForm'].resetFields()
            this.dialogVisible = false
        },
        query() {
            getPest({
                doctorId: this.doctorId
            }).then(res => {
                this.tableData = res.data
            })
        },
        dateFormat(row, column) {
            const daterc = row[column.property]
            return formatDate(new Date(daterc))
        },
        handleEdit(inds, row) {
            // this.id = row._id
            this.isEdit = true
            this.editForm = JSON.parse(JSON.stringify(row))
            console.log(this.editForm)
            this.dialogVisible = true

        },
        handleDelete(inds, row) {
            // this.id = row._id

            this.$confirm('是否删除该记录？', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                delPest(row._id).then(res => {
                    if (res.status == 'success') {
                        this.$message.success('删除成功')
                    }
                    this.query()
                })
            })
        }
    },
    mounted() {
        this.query()
    }
}
</script>
  