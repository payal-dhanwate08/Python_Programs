import sys

def main():
    print("Number of commandline argument are :",len(sys.argv))

    print("List of commandline argument are :")

    for value in sys.argv:
        print(value) 

if __name__=="_main__":
    main()