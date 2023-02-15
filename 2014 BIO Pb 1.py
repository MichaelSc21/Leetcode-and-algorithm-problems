"""
Question 1: Lucky Numbers
The lucky numbers are produced by taking a list of all the odd numbers and systematically removing
some of the numbers. Our first lucky number is 1. We now repeatedly take the next highest number n
that is still in the list, mark it as a lucky number and then remove every nth number from the list.
For example, with lucky numbers underlined as we progress:
• Initially we have: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, ...
• The next lucky number is 3, giving us: 1, 3, 7, 9, 13, 15, 19, 21, 25, 27, 31, ...
• Next is 7: 1, 3, 7, 9, 13, 15, 21, 25, 27, 31, ...
• Next is 9: 1, 3, 7, 9, 13, 15, 21, 25, 31, ...



1(a) [ 25 marks ]
Write a program which reads in a single integer between 2 and 10,000 inclusive.
You should output two numbers. Firstly the closest lucky number that is less than the
input, followed by the closest lucky number that is greater than the input."""


list = [i for i in range(1, 10004, 2)]
print(list)
lucky=[]
def lucky_def(list=[], lucky=[1]): 
    try:
        for i in range(1,len(list)):
            lucky.append(list[i])
            print(list[i])

            del list[list[i]-1::list[i]]
    except:
        return list, lucky

list, lucky = lucky_def(list)
num = int(input("number please: "))


def partA(lucky, num):
    max, min = 0, 0
    for i, val in enumerate(lucky):
        if val < num:

            min = val
            max = lucky[i+1]
            print(f"""Index {i}: 
            value {val}""")
        if val == num:
            min = lucky[i-1]
            max = lucky[i+1]
    return min, max
min, max = partA(lucky, num)
print(min,    max)


def partB(lucky):
    count = 0
    for i in lucky:
        if i < 100:
            count+= 1
        else:
            break
    return count
print(partB(lucky))
sum = 0
for i in range(15,21):
    sum+= i
print(sum)