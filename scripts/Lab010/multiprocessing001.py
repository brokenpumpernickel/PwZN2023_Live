import time
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing

def fibon(n):
    if n < 2:
        return n
    return fibon(n-1) + fibon(n-2)

def fibon_job(n):
    val = fibon(n)
    return n, val

if __name__ == '__main__':
    start = time.time()
    for i in range(35):
        print(i, fibon(i))
    end = time.time()
    print(end - start)

    # start = time.time()
    # with ProcessPoolExecutor(multiprocessing.cpu_count()) as ex:
    #     futures = [ex.submit(fibon, i) for i in range(35)]
    #     for future in futures:
    #         print(future.result())
    # end = time.time()    
    # print(end - start)

    start = time.time()
    with ProcessPoolExecutor(multiprocessing.cpu_count()) as ex:
        futures = [ex.submit(fibon_job, i) for i in range(35, 0, -1)]
        for future in as_completed(futures):
            print(future.result())
    end = time.time()    
    print(end - start)    
    
