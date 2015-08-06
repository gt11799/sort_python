#! coding=utf8

import time
l = [1,25,5,5,6,6,5,8,2,1,4,525,5,8,2,2,58,7,2,58,7,2,5,5,2,5,58,5,2,2,585,2,9,5,52,2,]


def recordTime(func):
    def wrapper(*args, **kwargs):
        print args, kwargs
        # print *args
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("run: %s"%(end-start))
        return result
    return wrapper

@recordTime
def quick_sort(l):
    
    if len(l) < 2:
        return l
    
    key = l[len(l)/2]
    left = [ item for item in l if item < key]
    middle = [ item for item in l if item == key]
    right = [ item for item in l if item > key]
    return quick_sort(left) + middle + quick_sort(right)
    

    
if __name__ == "__main__":
    print quick_sort(l)   
