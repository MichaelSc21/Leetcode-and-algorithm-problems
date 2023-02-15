# creating 2 sum for number 1 problem Leetcode
"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]"""

class twoSum():
    def __init__(self, target: int, arrayl: list[int]):
        self.target = target
        self.arrayl= arrayl

    def solution(self) -> list[int]:
        #the hash map 
        self.dict = {}
        #creating the dictionary with the numbers that work with the algorithm
        self.dict2 = {}
        for i, val in enumerate(self.arrayl):
            res = self.target - val

            if res in self.dict:
                print(i, self.dict[res])
                #one is only allowed to look up an element in a dictionary by using its key, but not value
                #therefore the element of the list is stored as the key in the dictionary and the index of the list is stored as the value in the dictionary
                #which allows us to look up the values of the dictionary using the phrase "if res in self.dict" on line 16
                self.dict2[self.dict[res]] = res
                self.dict2[i] = val
                
            self.dict[val] = i



            


a = twoSum(9, [2,7,11,15])
a.solution()
##for i, val in a.dict.items():
#    print(f"{i} : {val}")
print(a.dict2)
