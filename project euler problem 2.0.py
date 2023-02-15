"""import time
def timer(func):
    
    def wrapper(*args, **kwargs):
        print('Function started')
        start = time.time()
        rv = func(*args, **kwargs)
        print(f"Time taken: {time.time() - start}")
        return rv
    
    return wrapper



def fib(n, dict={}, c=0, sum=0):

    #    
    if n in dict:
        c = c+1
        print(c)
        return dict[n]
    if n == 2 or n == 1:
        c = c+1
        print(c)
        return 1
        
    dict[n] = fib(n-1, dict, c, sum) + fib(n-2, dict, c, sum)

    return dict[n]

timed_fib = timer(fib)

print(timed_fib(5, dict={}, c=0, sum=0))

#print(x)"""


def fib2(n):
    dict= {}
    c=0
    sum=0
    for i in range(1, n+1):   
        c+=1 
        if i<=2:
            dict[i] =1
        else:
            dict[i] = dict[i-1] + dict[i-2]
        if dict[i] > 4_000_000:
            break

        if c%3==0:

            sum += dict[i]
        print(f"{c}: --{dict[i]}")

    print(dict)
    print(sum)

fib2(253)
# correct answer is 4613732