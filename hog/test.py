def num_factors(n):
    """Return the number of factors of N, including 1 and N itself."""

    sum_factors = 0
    for i in range(1,n+1):
        if n % i == 0:
            sum_factors += 1
    return sum_factors
print(num_factors(97))