# function to return the index  
def getSubArray(arr, n, K): 
    currentSum = 0
    previousDifference = 0
    currentDifference = 0
    result = [-1, -1, abs(K-abs(currentSum))] 
    resultTmp = result 
    i = 0
    j = 0
      
    while(i <= j and j < n): 
        currentSum += arr[j] 
        previousDifference = currentDifference 
        currentDifference = K - abs(currentSum) 
        if(currentDifference <= 0): 
            if abs(currentDifference) < abs(previousDifference): 
                resultTmp = [i, j, currentDifference] 
            else: 
                resultTmp = [i, j-1, previousDifference] 
            currentSum -= (arr[i]+arr[j]) 
            i += 1
        else: 
            resultTmp = [i, j, currentDifference] 
            j += 1
        if(abs(resultTmp[2]) < abs(result[2])): 
            result = resultTmp 
              
    return result 
  
def getCloset(arr, result, K):
    
    sum = 0
    for a in result: 
        sum += arr[a]

    if sum <= K:
        return result
    else: 
        return getCloset(arr, [result[0] - 1, *result[1:]], K)
        
# Driver Code 
def main(): 
    # arr = [7, 12, 12, 13, 14, 28, 29, 29, 30, 32, 32, 34, 41, 45, 46, 56, 61, 61, 62, 63, 65, 68, 76, 77, 77, 92, 93, 94, 97, 103, 113, 114, 114, 120, 135, 145, 145, 149, 156, 157, 160, 169, 172, 179, 184, 185, 189, 194, 195, 195]
    # arr = [2, 5, 6, 7, 8, 9]
    arr = [4, 13, 17, 84, 95]
    n = len(arr)
    # K = 4500
    K = 100
    # K = 17
    # K = 1000000000
    [i, j, minDev] = getSubArray(arr, n, K)


    if(i == -1):
        print("The empty array shows minimum Deviation")
        return 0 

    result = []
    for a in range(i, j+1):
        result.append(a)

    print(getCloset(arr, result, K))
    # sum = 0 
    # for i in final_result: 
    #     sum += arr[i]
    # print(sum)

main()
