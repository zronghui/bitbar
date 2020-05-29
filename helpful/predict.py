#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import scipy.optimize as optimization

data_day = [1, 2, 3]
data_ltv = [1.159, 1.166, 1.163]

xdata = np.array(data_day)
ydata = np.array(data_ltv)


# 定义使用的公式
def lnFunction(x, a, b, c):
    return a * x ** 2 + b * x + c


guess = [1, 1, 1]  # 定义初始A、B|initialize a and b
params, params_covariance = optimization.curve_fit(lnFunction, xdata, ydata, guess)  # 拟合，A、B结果存入params
print(params)
a, b, c = params
print(round(lnFunction(4, a, b, c), 2))
