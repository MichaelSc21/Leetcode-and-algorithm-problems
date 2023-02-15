class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(': 0, '[': 0, '{': 0}
        for i in s:
            for key, val in dict:
                if val < 0:
                    return False
            if key == '(':
                dict[key] += 1
            elif key == ')':
                dict['('] -= 1
            if key == '[':
                dict[key] += 1
            elif key == ']':
                dict['['] -= 1
            if key == '{':
                dict[key] += 1
            elif key == '}':
                dict['{'] -= 1
            


solution = Solution()
solution.isValid("(]")
solution.isValid("""()[]{}""")
