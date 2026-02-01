from multipledispatch import dispatch


@dispatch(int, int)
def mx(a, b) -> int:
    """Return the maximum of two integers."""
    if a > b:
        return a
    else:
        return b

@dispatch(int, list)
def mx(n, a) -> int:
    """Return the maximum element in a list of integers."""
    maximum = a[0]
    for i in range(1, n):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


print(mx(3, 5))
print(mx(5, [1, 3, 7, 0, 4]))
