import threading
import time

def SumEnven(no):
    Sum=0
    for i in range(2,no+1,2):
        Sum=Sum+i
    print(Sum)

def SumOdd(no):
    Sum=0
    for i in range(1,no+1,2):
        Sum=Sum+i
    print(Sum)

def main():
    print("Demonstration of parallel execution")

    start_time=time.time()
    T1=threading.Thread(target=SumEnven,args=(900000000,))
    T2=threading.Thread(target=SumOdd,args=(900000000,))
    T1.start()
    T2.start()
    T1.join()
    T2.join()

    end_time=time.time()

    print("Time required execution is:",end_time-start_time)
    print("end of main")

    
if __name__=="__main__":
    main()