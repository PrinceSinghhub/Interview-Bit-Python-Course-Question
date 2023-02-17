# Return the factorial of the number N

def factorial(N):
    if N == 0:
        return 1
    ans = 1
    for i in range(1, N + 1):
        ans *= i
    return ans

