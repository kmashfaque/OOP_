def permutation(arr):
    result = []
    

    def backtack(index):
          if index == len(arr):
               result.append(arr.copy())
               return 
          
          for i in range(index, len(arr)):
                arr[index], arr[i] = arr[i], arr[index]
                backtack(index + 1)
                arr[index], arr[i] = arr[i], arr[index]
                
    backtack(0)
    
    return result

arr = [1,2,3] 
print(permutation(arr))