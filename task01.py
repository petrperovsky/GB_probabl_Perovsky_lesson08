'''Провести дисперсионный анализ для определения того,
есть ли различия среднего роста среди взрослых футболистов,
хоккеистов и штангистов. Даны значения роста в трех группах
случайно выбранных спортсменов:
Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.'''

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

f = np.array([173, 175, 180, 178, 177, 185, 183, 182])
h = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
sh = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
n1 = len(f)
n2 = len(h)
n3 = len(sh)
print(n1 + n2 + n3 - 3)  # 28 измерений, 3 группы
f_mean = np.mean(f)
print(f_mean)
h_mean = np.mean(h)
print(h_mean)
sh_mean = np.mean(sh)
print(sh_mean)
y = np.concatenate([f, h, sh])
y_mean = np.mean(y)

stats.probplot(f, plot=plt)
stats.probplot(h, plot=plt)
stats.probplot(sh, plot=plt)
plt.show()  # штангисты по среднему будут пониже

s2 = np.sum((y - y_mean) ** 2)
print(s2)
s2f = ((f_mean - y_mean) ** 2) * n1 + ((h_mean - y_mean) ** 2) * n2 + ((sh_mean - y_mean) ** 2) * n3
print(s2f)
s2res = np.sum((f - f_mean) ** 2) + np.sum((h - h_mean) ** 2) + np.sum((sh - sh_mean) ** 2)
print(s2res, s2f + s2res) # фактическое 253.9 + остаточное 577.1 = сумме квадратичных отклонений от общего среднего 831

sigma_f = s2f / (3 - 1)
sigma_res = s2res / (n1 + n2 + n3 - 3)
F = sigma_f / sigma_res
print(F)
'''Значение критерия фактическое 5.5, что больше табличного для альфа 0.05 и степеней свободы 2 и 25 = 3.38
Т.о. с вероятностью ошибки в 5% можем сказать, что есть достоверные различия в росте между группами спортсменов'''

print(stats.f_oneway(f, h, sh)) #F_onewayResult(statistic=5.500053450812596, pvalue=0.010482206918698694)
print(stats.ttest_ind(f, h), stats.ttest_ind(f, sh), stats.ttest_ind(sh, h)) # в попарных сравнениях штангисты достоверно ниже

