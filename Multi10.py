import multiprocessing
import time
import os

def SumEnven(no):
    print("PID of sumeven task is:",os.getpid) .....  
    print("PPID of sumeven task is:",os.getppid())  #101
    Sum=0
    for i in range(2,no+1,2):
        Sum=Sum+i
    print(Sum)

def SumOdd(no):
    print("PID of sumodd task is:",os.getpid())  
    print("PPID of sumodd task is:",os.getppid())    #101
    Sum=0
    for i in range(1,no+1,2):
        Sum=Sum+i
    print(Sum)

def main():
    print("Demonstration of parallel execution")
    print("PID of main process is:",os.getpid()) #101

    start_time=time.time()

    T1=multiprocessing.Process(target=SumEnven,args=(900000000,))
    T2=multiprocessing.Process(target=SumOdd,args=(900000000,))
    T1.start()
    T2.start()
    T1.join()
    T2.join()
    end_time=time.time()
    print("Time required execution is:",end_time-start_time)
    print("end of main")
    
if __name__=="__main__":
    main()