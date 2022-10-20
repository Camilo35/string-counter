'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target'''

def two_and_sum2(nums, target):
    for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]


'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target'''


def two_and_sum2(nums, target):
    result2 =[]
    for i in nums:
        for j in nums:            
            x = i + j
            if x == target and i != j:          
                            
                index_1 = nums.index(i)                    
                index_2 = nums.index(j)
                
                result2.append(index_1)                    
                result2.append(index_2)
                return result2 
                
            elif x == target and i == j:
                index_1 = nums.index(i)
                index_2 = nums.index(j, index_1+1)
                result2.append(index_1)                    
                result2.append(index_2)
                return result2 



    

nums = [3,2,3]
target = 6

result2 = two_and_sum2(nums, target)
print(result2)