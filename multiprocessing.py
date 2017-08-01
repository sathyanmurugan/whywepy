#For an explanation, visit: http://whywepy.com/index.php/2017/08/01/multiprocessing-in-python/

import multiprocessing
import datetime,time

def do_something(x):
    start_time = datetime.datetime.now().strftime('%H:%M:%S')
    time.sleep(2)
    return (x,start_time)

list_of_numbers = list(range(0,4))

number_of_cores = multiprocessing.cpu_count()
pool = multiprocessing.Pool(processes=number_of_cores)
results = pool.map(do_something, list_of_numbers)

print (results)
