import re
from question import content
from question2 import content2

def get_single_question(c):
    results = re.findall('ON(.*?)QUES', c, re.S)

    for s_l in results:
        yield s_l


def data_back(c):
    result = re.search('([0-9]{1,3})(.*?)A\. (.*?)Correct.*?Answer: (.*?)Explanation.*?Reference:(.*?)$', c, re.S)
    option_number = 0
    words = ['A. ', 'B. ', 'C. ', 'D. ', 'E. ', 'F. ', 'G. ', 'H. ', 'I. ', 'J. ']
    for i in words:
        if i in c:
            option_number += 1
            continue
        else:
            break
    try:
        numbers = '华三杯1卷 题号:'+ result.group(1)
        context = result.group(2)
        pic = None
        options = 'A. ' + result.group(3)
        answer = result.group(4).strip()
        reference = result.group(5) + '.'
        return [numbers, context, pic, options, answer, option_number, reference]
    except (AttributeError, TypeError):
        pass

# t = data_back(content)
# print(t[0],'\n'+ t[1], '\n', t[2], '\n', t[3], '\n', t[4], '\n', t[5])


# for i in get_single_question(content2):
#     t = data_back(i)
#     try:
#         print(t[0],'\n'+ t[1], '\n', t[2], '\n', t[3], '\n', t[4], '\n', t[5], '\n', t[6])
#     except:
#         pass
#     print('------------------------------------------')