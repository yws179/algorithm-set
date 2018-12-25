# coding=utf-8

import time


def timer(func):
    """
    使用装饰器计算func运行耗时
    """
    def wrapper(*args, **kw):
        t_start = time.time()
        result = func(*args, **kw)
        t_end = time.time()
        print('运行 %s 消耗 %f 秒' % (func.__name__, t_end - t_start))
        return result
    return wrapper
