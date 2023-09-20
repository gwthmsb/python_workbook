import asyncio
import time


async def part1(n):
    print("Inside part1-{}, sleeping".format(n))
    await asyncio.sleep(4)
    print("Inside part1-{}. Done sleeping".format(n))
    return "part1-{}_response".format(n)


async def part2(n, data):
    print("Inside part2-{}, sleeping".format(n))
    await asyncio.sleep(2)
    print("Inside part2-{}, Done sleeping".format(n))
    print("Writing data: {}".format(data))
    return "part2-{}_response".format(n)


async def chain(n):
    print("Inside the chain: {}".format(n))
    p1 = await part1(n)
    p2 = await part2(n, p1)
    print("Inside the chain: {}".format(p2))


async def main():
    await asyncio.gather(*(chain(n) for n in range(2)))


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    print("Total time taken: "+str(time.perf_counter() - s))
    print("End")
