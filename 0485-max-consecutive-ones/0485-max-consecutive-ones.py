class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # intalize the max count of consecutive 1s to 0
        max_count = 0
        
        # intalize the current count of consecutive 1s to 0
        current_count = 0
        
        #iterate through each number in the list
        for num in nums:
            
            #if thr current number is 1
            if num ==1:
                
                #increment the current count
                current_count +=1
                
            #if the current number is not 1
            else: 
                
                #update max_count if current_count is greater
                max_count = max(max_count, current_count)
                
                #reset current-count to 0
                current_count = 0
        
        #check one last time after loop ends to accout for sequences at the end of the list
        max_count = max(max_count, current_count)
            
        #return the max coubnt of consecutive 1s
        return max_count
        
        