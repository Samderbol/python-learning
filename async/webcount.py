# coding=utf-8
"""
控制用户自动打开浏览器，浏览博客网站URL，刷取阅读量
若遇到会封单个IP的博客网站，可以考虑再拓展动态设置网络代理
每个URL会对应一个独立的访问线程
"""
import random
import webbrowser as web
import time
import threading
import os

# 用于全局统计刷取了访问量总数
count = 0

"""
此方法用于打开博客网站URL，目前此方法是在我本机Mac下跑的，如果是Windows或者Linux的朋友
需要稍作修改，只要修改注册chrome的那一行代码，chrome运行文件路径即可
@:param url                     待刷取博客URL地址
@:param interval_time           自动刷新访问的间隔时间（视个人设备和网络实际情况设定）
@:param open_defalut            默认为True用操作系统设定的默认浏览器打开，False为使用chrome
"""


def open_brower_auto_refresh(url, interval_time, open_default=False):
    browser_path = r'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    # Safari brower
    browser_paths = [r'C:\Program Files\Google\Chrome\Application\chrome.exeC:\Program Files\Google\Chrome\Application\chrome.exe']
    global count
    temp = 1
    while True:
        if open_default:
            brower = web.open(url, new=0, autoraise=False)
        else:
            browser_path = random.choice(browser_paths)  # 随机从浏览器中选择一个路径
            print(browser_path)
            browser_task_name = browser_path.split('/')[-1]  # 结束任务的名字
            print(browser_task_name)
            if browser_task_name == 'Google Chrome':
                browser_task_name = 'Chrome'
            chrome = web.get(browser_task_name)
            # chrome.open(url)
            chrome.open_new_tab(url)
            temp = temp + 1
            if temp > 20:
                temp = 1
                os.system('pkill -9 Chrome')
                web.register(browser_task_name, None, web.BackgroundBrowser(browser_path))
        time.sleep(interval_time)
        count = count + 1


if __name__ == '__main__':
    # 多线程启动浏览器，每个页面一个线程，自动延时的刷新间隔时间
    interval_time = 10
    # 需要刷新的博客列表URL定义在这里
    url_list = ['https://bsd.wiki']
    for url in url_list:
        t2 = threading.Thread(target=open_brower_auto_refresh,
                              args=(url, interval_time + 1))
        t2.start()
        time.sleep(10)
    # for url in url_list:
    #     t4 = threading.Thread(target=open_brower_auto_refresh,
    #                           args=(url, interval_time, False))
    #     t4.start()
    while True:
        print("当前已刷新阅读量总数：" + str(count))
        time.sleep(60)