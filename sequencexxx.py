
def circlearea(Rad,PI = 3.14):
    Area = PI *Rad*Rad
    return Area

def main():
    print("enter radius of circle:")
    radius = float(input())
    result = circlearea(radius,7.12)
    print("Area of circle is:",radius)
      



if __name__ =="__main__":
    main()

