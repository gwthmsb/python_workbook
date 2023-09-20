import asyncio
import time
import random

big_list = (range(100))


async def list_by_page(size: int = 10, page: int = 0):
    i = random.randint(0, 5)
    print("Sleeping {} seconds for page {}".format(i, page))
    await asyncio.sleep(i)
    return big_list[page*10: page*10+size-1]


async def list_50():
    t = time.perf_counter()
    #r = asyncio.gather(*(list_by_page(page=page) for page in range(5)))
    tasks = [asyncio.create_task(list_by_page(page=page)) for page in range(5)]
    result = await asyncio.gather(*tasks)
    print(time.perf_counter() - t)
    print(result)

    tasks = [asyncio.create_task(list_by_page(page=page)) for page in range(5)]
    t = time.perf_counter()
    for res in asyncio.as_completed(tasks):
        compl = await res
        print(compl)
    print(time.perf_counter() - t)


if __name__ == "__main__":
    asyncio.run(list_50())

