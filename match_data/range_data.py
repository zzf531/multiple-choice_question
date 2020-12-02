import re
from question import content

def get_single_q(c):
    result = re.findall('TION(.*?)QUES', c, re.S)
    for i in result:
        yield i

for i in get_single_q(content):
    print(i)