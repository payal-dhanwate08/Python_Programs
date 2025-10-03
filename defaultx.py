
def calculatepercentage(obtained =400,total=500):
    result = ((obtained/total)*100)
    return result


             
def main():
    result = calculatepercentage(350,450)
    print("percentage is:",result)
    result = calculatepercentage(350)
    print("percentage is:",result)
    result = calculatepercentage()
    print("percentage is:",result)
 
if __name__=="__main__":
    main()