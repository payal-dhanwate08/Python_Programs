def calculatepercentage(obtained,total=500):
    result = ((obtained/total)*100)
    return result


def main():
    
    print("enter obtained marks:")
    value2 = int(input())
    output = calculatepercentage(value2) #default arguments
    print("percentage is:",output)

if __name__=="__main__":
    main()