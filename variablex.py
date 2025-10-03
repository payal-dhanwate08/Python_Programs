def Display(*A):
    print("inside display",A)
   

def main():
    Display(11,21,51,101)
    Display(11,21,51,101,111)
    Display(11,21,51)
    Display(11)
    Display()
if __name__ == "__main":
    main()
