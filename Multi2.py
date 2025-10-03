import os

def main():
    print("PID of procees is:",os.getpid())
    print("PID if parent process is :",os.getppid())

if __name__=="__main__":
    main()