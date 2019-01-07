import numpy as np

learnrate = 10
hidden_error_term = [2,4]
x=[ 0.5 , 0.1, -0.2]
print(type(x))
print(type(np.array(hidden_error_term)))
print(np.array(hidden_error_term))
print(np.array(x)[:,None])


delta_w_i_h = learnrate * np.array(hidden_error_term) *np.array(x)[:,None]
print(delta_w_i_h)

a = np.array([[1, 1], [2, 2], [3, 3]])
np.insert(a, 1, 5)
print(np.insert(a, 1, 5))

b=np.array([7])
temp = np.insert(b,b.size,5)
for i in range(4):
    temp = np.insert(temp,temp.size,5)
    print('temp====', temp)


print(np.append(np.array([7]), np.array([7])))