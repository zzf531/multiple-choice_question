## 说明

线上地址

49.234.236.218:8009

match_data 是匹配pdf里文字的程序



运行方法
web_question 为单独django项目, 进入web_question

1. Django_Menu/settings.py 里配置数据库

2. pip install -r pipfile.txt
3. python manage.py migrate
4. python manage.py runserver 


match_data ,将pdf转换为文字, 正则匹选择题题目.

题目规律,  题序号, 题目, 题选项, answer, Explanation/Reference

将题目存入数据库. 
