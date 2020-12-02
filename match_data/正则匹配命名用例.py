import re
import datetime

content = '曾振飞_20201130'
a = re.search('^([\u4e00-\u9fa5]{1,4})(\_)(\d.*)', content)
print(a.group(3))
a2 = datetime.datetime.now().strftime("%Y%m%d")
print(type(a2))