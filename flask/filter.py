import re


#   完成一个自定义过滤器方法
def ttest1(data, len=2):
    return f"%.{len}f" % data


#   这个方法实现了把手机号中间四位加密
def ttest2(data):
    c = re.sub(r"(\d{3})(\d{4})(\d{4})", r"\1****\3", f'{data}')
    if len(c) == 11:
        return c
    raise Exception("err")


#   把自定义过滤器放在一个字典到时候注册到内置过滤器内备用
FILTERS = {
    'ttest1': ttest1,
    'ttest2': ttest2
}

if __name__ == '__main__':
    try:
        print(ttest2("13894732645"))
    except Exception as e:
        print(e)
