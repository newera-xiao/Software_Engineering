# Software_Engineering
We are dedicated to create a full medical system, which contains almost all components you will encounter while seeking for medical asistance.
And this repo. is for the recovery subsystem. 
Happy coding. :)
# Creators
The creators are all students from Zhejiang University Computer Science College.
Creators: Yixiao Zhou, Kairong Han, Tao Pan, Haoming Yu. 
# Date
2023-04-14 -> repo. creation

# doc

[飞书](https://w1bcgpg61v7.feishu.cn/docx/EasvdyapZoRKfJxcjMzcRCIbnFg)

# study

[git&github](https://www.bilibili.com/video/BV1KD4y1S7FL/?spm_id_from=333.788.recommend_more_video.-1&vd_source=601f08ec04999151a4b161c6634f56ff)

[tutorial](https://pku-minic.github.io/online-doc/#/preface/prerequisites?id=%e5%a6%82%e4%bd%95%e4%bd%bf%e7%94%a8-linux)

[SQLite简介|菜鸟教程](https://www.runoob.com/sqlite/sqlite-intro.html)

[SQLite官方文档|英文](https://dormousehole.readthedocs.io/en/latest/)

[欢迎来到Flask的世界——Flask中文文档](https://dormousehole.readthedocs.io/en/latest/)

# 后端编写

把代码`pull`下来后，先在终端中`cd`到`./BACK`文件夹下尝试运行`flask run`，如果成功运行，说明`flask`环境正确，此时按`ctrl+c`终止程序，在终端运行`flask init-db`**（注意：此处为横杠，不是下划线，不要写成`init_db`）**，这个命令会初始化数据库，所以每当你修改`schema.sql`文件后，都应该运行一次这个命令。

如果运行`flask run`失败，在`powershell`中运行这个命令：`$env:FLASK_APP=app.py`，如果此时运行`flask run`还是失败，请求助小组成员。（注意全程保持在`./BACK`文件夹下）