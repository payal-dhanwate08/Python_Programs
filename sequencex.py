PI = 3.14
def circlearea(Rad):
    Area = PI *Rad*Rad
    return Area

def main():
    print("enter radius of circle:")
    radius = float(input())
    result = circlearea(radius)
    print("Area of circle is:",radius)
      



if __name__ =="__main__":
    main()

