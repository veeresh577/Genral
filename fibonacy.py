import time
def fib():
     start = time.time()
     a, b = 0, 1
     while 1:
         yield a
         a, b =b, a+b
     end = time.time()
i= fib()
for f in range(10):
    print(next(i))

try:
    var=bad_var

except Exception as e:
    print(e)
finally:
    print("fibonaci serise stopped at ")