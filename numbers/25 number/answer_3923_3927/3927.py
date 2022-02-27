from functions import *
import time
import math
print(math.factorial(8))

t0 = time.time()
count = 512
prostos = set_prosto(100)[:8] # массив простых чисел нужных нам

t = proiz(prostos)*2**3*3**3
print('prostos: ', prostos)
print('ANSWER = ', t, prostos[-1])
print('len =', len(delim(t)[0]))


t1 = time.time()
print('Времени затрачено =', int(t1-t0), 'секунд')
