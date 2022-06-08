#!/usr/bin/env python
# coding: utf-8

# In[54]:


import numpy as np
import matplotlib.pyplot as plt
from os import path, makedirs

A = 10
l_b = -5.12                                 #левая граница
r_b = 5.12                                  # правая граница
n = 1025                                    #число шагов
r = 5                                       #До скольки знаков мы округляем число?
x = np.linspace(l_b, r_b, n)
y = A + x**2 - A * np.cos(2 * np.pi * x)

if not path.exists('results'):              #Проверка нужного пути, для создания файлов
    makedirs('results')                     #Создание путь, в случае если его нет
  
file = open('results/Rec.txt','w')          #Открываем файл для записи

for i in range(n-1):                        #Цикл для записи значений
    file.write(str(round(x[i],r)))
    file.write("    ")
    file.write(str(round(y[i],r)))
    file.write("\n")

file.close()                                #Закрываем файл, чтобы с ним ничего нельзя было больше делать, и освобождаем место

plt.plot(x, y)                              #Строим и выводим график
plt.show()


# In[ ]:




