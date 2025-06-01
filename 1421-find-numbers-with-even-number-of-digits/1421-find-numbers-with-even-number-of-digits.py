class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        count = 0  # Initialize a counter for numbers with even digits
        for num in nums:  # Iterate through each number in the input list
            num_str = str(num)  # Convert the number to a string to easily find its length
            if len(num_str) % 2 == 0:  # Check if the length of the string (number of digits) is even
                count += 1  # Increment the counter if the number of digits is even
        return count  # Return the final count of numbers with even digits


        