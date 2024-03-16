#   完成一个自定义过滤器方法
def ttest1(data, len=2):
    return f"%.{len}f" % data


#   把自定义过滤器放在一个字典到时候注册到内置过滤器内备用
FILTERS = {
    'ttest1': ttest1
}


if __name__ == '__main__':
    print(ttest1(15.5678))