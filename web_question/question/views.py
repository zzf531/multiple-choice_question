from django.shortcuts import render, redirect
from question.models import questions, Fraction
from django.http import HttpResponse
import re
import datetime
import requests

# Create your views here.

def index(request):
    """
    直接渲染index.html页面
    :param request:
    :return:
    """
    return render(request, 'index.html')


def show_exam(request):
    """
    直接渲染exam_explain.html, 考试须知测试页面
    :param request:
    :return:
    """
    return render(request, 'exam_explain.html')


def show_index(request):
    """
    随机选择题页面
    a = 在数据库中随机获取一条数据
    r = 请求舔狗日记api
    choice_list, 根据题目有几个选项数, 生成字母列表[a,b,c,d]
        为选择题选项数量.
    :param request:
    :return:渲染随机选择题页面
    """
    a = questions.objects.order_by('?').first()
    r = requests.get('https://cloud.qqshabi.cn/api/tiangou/api.php')
    tgrj = r.text
    if r.status_code != 200:
        tgrj = ''
    choice_list = [chr(i) for i in range(65, 65 + int(a.option_number))]
    context = {'post': a, 'choice_list': choice_list, 'tgrj': tgrj}
    return render(request, 'show_index.html', context)


def choice(request, pk):
    """
    重定向, 实现随机下一题
    :param request:
    :param pk: 获得复选框值
    :return:
    """
    kbf = ''  # 空白符, 暂时存储, 用于比对正确答案
    check_box_list = request.POST.getlist("c")
    answer = questions.objects.get(pk=pk)
    if answer.answer == kbf.join(check_box_list):
        print('你打对了')
    else:
        print('你错了, 正确答案是', answer.answer)
    return redirect('/2')

def exam(request):
    """
    判断考试须知的分数
    获取考试须知测试中,单选框的值, 正确答案的value值为1
    获取所有value, 加添到列表,判断列表中有几个['1']
    第六题, 正则匹配  文字, _, 日期,判断日期是否为今日.
    如果第六题匹配成功, 存入数据库.
    :param request:
    :return:
    """
    fraction = 0
    qs = []
    q1 = request.POST.getlist("q1")
    q2 = request.POST.getlist("q2")
    q3 = request.POST.getlist("q3")
    q4 = request.POST.getlist("q4")
    q5 = request.POST.getlist("q5")
    q6 = request.POST.getlist("q6")
    qs.append([q1,q2,q3,q4,q5])

    try:
        p = re.search('^(\w{1,4})(\_)(\d.*)', q6[0])
        name = p.group(1)
        data_ = p.group(3)
        d = datetime.datetime.now().strftime("%Y%m%d")
        for i in qs[0]:
            if i == ['1']:
                fraction += 20
        if d != data_:
            fraction = -1
        new_f = Fraction.objects.create()
        new_f.name = name
        new_f.fract = fraction
        new_f.save()
    except:
        pass
    print(fraction)
    return redirect('/')


def show_fraction(request):
    """
    须知测试结果页
    数据库取值就可
    :param request:
    :return:
    """
    all_fraction = Fraction.objects.all()
    context = {'af': all_fraction}
    return render(request, 'show_fraction.html', context)

