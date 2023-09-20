import asyncio
import random, time
from os import urandom


async def make_item(size=5):
    return urandom(size).hex()


async def random_sleep(caller=None):
    #i = random.randint(0, 10)
    i = 3
    if caller:
        print("{} is sleeping for {} secs".format(caller, i))
    await asyncio.sleep(i)


async def produce(name: int, q: asyncio.Queue):
    #n = random.randint(0, 3)
    n = 3
    #print("Created producer {}".format(name))
    for _ in range(n):
        #await random_sleep("producer-{}".format(name))
        i = await make_item()
        t = time.perf_counter()
        await q.put((i, t))
        #print("producer-{} added {} to queue".format(name, i))
    return


async def consume(name: int, q: asyncio.Queue):
    print("Created consumer {}".format(name))
    while True:
        await random_sleep("consumer-{}".format(name))
        i, t = await q.get()
        elapsed_time = time.perf_counter() - t
        print("consumer-{} consumed {} in {:0.5f} seconds".format(name, i, elapsed_time))
        q.task_done()


async def main(nprod, ncons):
    q = asyncio.Queue()

    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncons)]
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]

    await asyncio.gather(*producers)
    """
        Here consumers are not needed to gather because they are designed to run indefinitely
        q.join() make sure that queue is exhausted before canceling the consumers
        
        Otherwise, we need to find a mechanism in which we have to make sure, we handle all the messages that are 
        produced
    """

    await q.join()
    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    t = time.perf_counter()
    asyncio.run(main(10, 2))
    elapsed_time = time.perf_counter() - t
    print("All tasks finished in {}".format(elapsed_time))
