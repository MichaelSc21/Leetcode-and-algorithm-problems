class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        
        def function(dividend, divisor):
            temp = 0
            division_amount=0
            while dividend- (divisor<<division_amount) >= 0:
                while dividend- (divisor<<division_amount) >= 0:
                    division_amount += 1
                division_amount -= 1
                temp += 2**division_amount
                dividend = dividend - (divisor<<division_amount)
                division_amount = 0
            return temp
        
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        if dividend < 0 and divisor < 0:
            quotient =  function(abs_dividend, abs_divisor)
        elif (dividend <0 and divisor > 0 ) or (dividend > 0 and divisor<0):
            quotient= -function(abs_dividend, abs_divisor)
        else:
            quotient= function(abs_dividend, abs_divisor)

        if quotient > 2**31 -1:
            return 2**31 - 1
        elif quotient < -(2**31):
            return -(2**31)
        else:
            return quotient
solution = Solution()
print(solution.divide(dividend =-2147483648,divisor = -1))


