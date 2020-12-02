# from crawl_data.question import content
# from crawl_data.匹配题目 import data_back, get_single_question
import re

content = """
QUESTION  420 
客户的两台路由器MSR-1、MSR-2  的⼴域⽹链路采⽤PPP  协议，同时要求MSR-1  作为主验证⽅，通过 
CHAP  ⽅式验证MSR-2，那么如下哪些配置是MSR-2  可能需要的？（选择⼀项或多项） 
 
A.  [MSR-2]ppp  chap  user  user 
B.  [MSR-2]ppp  chap  password  simple  password 
C.  [MSR-2-Serial1/0]  ip  address  ppp-negotiate 
D.  [MSR-2-Serial1/0]  ip  address  10.10.10.1  22 
 
Correct  Answer:  CD 
Explanation 
 
Explanation/Reference: 

"""


def data_back(c):
    result = re.search('([0-9]{1,3})(.*?)A\. (.*?)Correct.*?Answer: (.*?)Explanation.*?Reference:(.*?)$', content, re.S)
    option_number = 0
    words = ['A.  ', 'B.  ', 'C.  ', 'D.  ', 'E.  ', 'F.  ', 'G.  ', 'H.  ', 'I.  ', 'J.  ']
    for i in words:
        if i in c:
            option_number += 1
            continue
        else:
            break
    # print(option_number)

    numbers = '华三杯1卷 题号:' + result.group(1)
    context = result.group(2)
    pic = None
    options = 'A. ' + result.group(3)
    reference = result.group(5)
    if '\n' == reference[0]:
        print(11)
    answer = result.group(4).strip()
    return [numbers, context, pic, options, answer, option_number, reference]


t = data_back(content)
print(t[0], '\n' + t[1], '\n', t[2], '\n', t[3], '\n', t[4], '\n', t[5], '\n', t[6])
