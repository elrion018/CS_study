memo = {0:1,1:1}
def fib(n):
    if n in memo:
        result = memo[n]
        return result
    else:
        result = fib(n-1) + fib(n-2)
        memo[n] = result

        return result
print(fib(int(input())-1))
