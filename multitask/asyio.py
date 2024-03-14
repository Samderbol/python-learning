import asyncio  # 导入asyncio库，用于实现异步编程。
import time  # 导入time模块，用于计时操作。
import aiohttp  # 导入aiohttp库，用于实现异步的HTTP请求。


def timed(func):  # 定义一个装饰器函数timed，用于计时函数的执行时间。
    async def wrapper():  # 定义一个内部函数wrapper，用于包装被装饰的函数。
        start = time.time()  # 获取当前时间，作为计时的起始点。
        await func()  # 调用被装饰的函数，即main()函数。
        # 打印执行时间，通过计算当前时间与起始时间的差值得出。
        print(f"costs: {time.time() - start:.3f} S")
    return wrapper  # 返回包装后的函数。


async def req(url):  # 定义一个异步函数req，用于发送异步的HTTP请求。
    async with aiohttp.ClientSession() as session:  # 创建一个异步HTTP会话。
        # 发起HTTP GET请求，并使用async with语法自动关闭请求。
        async with session.get(url) as resp:
            return resp.status  # 返回HTTP响应的状态码。


@timed  # 应用timed装饰器到main()函数上，用于计算函数执行时间。
async def main():  # 定义一个异步函数main，作为程序的入口点。
    tasks = [req('http://klpbbs.com/status/200')
             for _ in range(5000)]  # 创建一个包含5000个异步HTTP请求任务的列表。
    # 使用asyncio.gather()函数并发执行所有的HTTP请求任务，并等待它们全部完成。
    result = await asyncio.gather(*tasks)
    print(f"Last response status: {result[-1]}")  # 打印最后一个HTTP响应的状态码。

asyncio.run(main())  # 调用asyncio.run()函数执行异步函数main()。
