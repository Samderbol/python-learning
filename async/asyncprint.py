import asyncio
import time


async def func1():
    print(1)
    await asyncio.sleep(3)  # 遇到IO耗时操作，自动化切换到tasks中的其他任务print(3)
    print(2)


async def func2():
    print(time.ctime())
    await asyncio.sleep(3)  # 遇到IO耗时操作，自动化切换到tasks中的其他任务print(2)
    print(time.ctime())


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
