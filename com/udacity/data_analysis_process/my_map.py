import numpy as np

t = open('csv_file/my_map.txt', 'r', encoding='UTF-8')
my = list(map(lambda x: x[:-1], t.readlines()))
t.close()

print(my)

print(np.zeros(4))
print(np.zeros((1,4)))
np.dot()