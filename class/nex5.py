"""
5 - Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
Note: There will be one solution for each input and do not use the same element twice.
"""
class nex5:

    def __init__(self, li1, ):
        self.originalList = li1

    def findElement(self, n):
        listNumbers = sorted(self.originalList.copy())

        if listNumbers[0] >= 0:
            listNumbers = list(filter(lambda i: i<=n,listNumbers))

        if listNumbers[-1] + listNumbers[-2] < n or listNumbers[0] > n:
            pass #end

        div = len(listNumbers)//2
        in1 = 0
        in2 = div
        
        # sum = listNumbers[div] + listNumbers[div+1]
        sum = listNumbers[in1] + listNumbers[in2]

        print(sum)



        # if sum > n:
        


        """
        value1 = 0
        value2 = 0

        otherCopy = listNumbers.copy()

        for i in listNumbers:
            del otherCopy[0]
            sum = n-i 
            if sum in otherCopy:
                value1 = i
                value2 = sum
                break

        print(f"{value1}  +  {value2}  =  {n}")

        """
            

            
        

        
        # print(listNumbers)
        print()

    


if __name__ == '__main__':
    n = 50
    # n = int(input("Ingrese número: "))
    list1  = [10,20,10,40,50,60,70]
    
    n1 = nex5(list1)

    n1.findElement(n)

