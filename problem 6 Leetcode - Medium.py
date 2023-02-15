import time

class Solution:

    def time_is(func):
        def wrap(self, s, numRows):
            start = time.time()
            result  = func(self, s, numRows)
            end = time.time()
            print(f"function executed in: {end-start}")
            return result
        return wrap
    @time_is
    def convert(self, s: str, numRows: int):
        if numRows == 1:
            return s
        if numRows >= len(s):
            return s
        ret_str = ""
        cyclelen = numRows * 2 - 2
        top = cyclelen
        bottom = 0
        for i in range(numRows):
            curr_idx = i
            ret_str += s[curr_idx]
            while curr_idx + top <= len(s)-1: 
                if top != 0:
                    curr_idx += top
                    ret_str += s[curr_idx]
                curr_idx += bottom
                if bottom != 0:
                    if curr_idx <= len(s)-1:
                        ret_str += s[curr_idx]
            top -= 2
            bottom += 2
        
        return ret_str

    


solution = Solution()
print(solution.convert("A", 2))