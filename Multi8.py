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
    print("Demonstration of serial execution")

    start_time=time.time()

    SumEnven(900000000)
    SumOdd(900000000)

    end_time=time.time()

    print("Time required execution is:",end_time-start_time())
    print("end of main")

    
if __name__=="__main__":
    main()