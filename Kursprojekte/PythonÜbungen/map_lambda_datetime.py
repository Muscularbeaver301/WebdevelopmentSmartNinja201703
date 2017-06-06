import datetime
import time

if __name__ == '__main__':
    print datetime.datetime.now()
    print datetime.datetime.utcnow()
    print time.time()
    print datetime.datetime.fromtimestamp(time.time())

    my_list = [1,2,3,4,5,6]
    my_big_list = [10,20,30,40,50]
    print map(str, my_list)
    print map(str, my_big_list)
    print map(lambda x:x**2,my_list)



