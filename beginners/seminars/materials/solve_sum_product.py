import asyncio

async def sum(a: list[int], n: int) -> int:
    sum = 0
    for i in range(n):
        sum += a[i]

    return sum

async def product(a: list[int], n: int) -> int:
    product = 1
    for i in range(n):
        product *= a[i]

    return product

async def main():
    n = int(input())

    a = list(map(int, input().split()))

    _sum = asyncio.create_task(sum(a, n))
    _product = asyncio.create_task(product(a, n))

    # ....

    result_sum = await _sum
    result_product = await _product


    print(result_sum, result_product)

asyncio.run(main())