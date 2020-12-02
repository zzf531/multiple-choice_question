## 说明

match_data 是匹配pdf里文字的程序



运行方法
web_question 为单独django项目, 进入web_question

Django_Menu/settings.py 里配置数据库
pip install -r pipfile.txt
python manage.py migrate
python manage.py runserver 


match_data ,将pdf转换为文字, 正则匹选择题题目.
题目规律,  题序号, 题目, 题选项, answer, Explanation/Reference
将题目存入数据库. 
