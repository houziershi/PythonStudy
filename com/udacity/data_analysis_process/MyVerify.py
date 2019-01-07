
import tflearn as tf

tf.input_data(None,10000)

s = set([1, 2, 3])
print(s)
print(list(s))
my = set('12')
print(my)
u=set('1,2,3'.split(','))
print(u)
my = my.update('123')
# my = my.union(u)
print(my)