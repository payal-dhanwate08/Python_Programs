def calculatepercentage(total,obtained):
    result = ((obtained/total)*100)
    return result


def main():
    print("enter total marks:")
    value1 = int(input())
    print("enter obtained marks:")
    value2 = int(input())
    output = calculatepercentage(obtained=value2,total=value1) #keyword arguments
    print("percentage is:",output)

if __name__=="__main__":
    main()