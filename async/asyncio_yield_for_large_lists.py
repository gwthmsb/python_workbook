import asyncio


async def provide_list(page:int = 0):
    l = range(10*page, 10*page+10)
    return l


async def list_all():
    i = 1
    while i:
        l = await provide_list(i)
        if i>5:
            break
        yield l
        i = i+1


async def use_list_all():
    async for y_l in list_all():
        for i in y_l:
            print(i)


def main():
    asyncio.run(use_list_all())


if __name__ == "__main__":
    main()

