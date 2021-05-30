# -*- coding: utf-8 -*-
'''
作者 : 丁毅
开发时间 : 2021/5/29 11:46
'''
from lxml import etree
import asyncio
import aiohttp
import pandas as pd
from pathlib import Path

current_path = Path.cwd()

def get_url_list():
    url_list = []
    # 默认排序
    url = 'https://wh.lianjia.com/ershoufang/pg%d/'
    # 最新发布
    url_new = 'https://wh.lianjia.com/ershoufang/pg%dco32/'
    for i in range(1, 101):
        url_list.append(url%i)
        url_list.append(url_new%i)
    return url_list


async def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    }
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), trust_env=True) as session:
        while True:
            try:
                async with session.get(url=url, headers=headers, timeout=8) as response:
                    # 更改相应数据的编码格式
                    response.encoding = 'utf-8'
                    # 遇到IO请求挂起当前任务，等IO操作完成执行之后的代码，当协程挂起时，事件循环可以去执行其他任务。
                    page_text = await response.text()
                    # 未成功获取数据时，更换ip继续请求
                    if response.status != 200:
                        continue
                    print(f"{url}爬取完成!")
                    break
            except Exception as e:
                print(e)
                # 捕获异常，继续请求
                continue
    return get_detail_url(page_text)


def get_detail_url(page_text):
    tree = etree.HTML(page_text)

    li_list = tree.xpath('//*[@id="content"]/div[1]/ul/li')
    detail_url_list = []
    for li in li_list:
        detail_url_list.append(li.xpath('./div[1]/div[1]/a/@href')[0])

    df = pd.DataFrame({'detail_url': detail_url_list})
    header = False if Path.exists(Path(current_path, 'detail_page_url.csv')) else True
    df.to_csv(Path(current_path, 'detail_page_url.csv'), index=False, mode='a', header=header)


async def main(loop):
    # 获取url列表
    url_list = get_url_list()
    # 创建任务对象并添加到任务列表中
    tasks = [loop.create_task(get_page(url)) for url in url_list]
    # 挂起任务列表
    await asyncio.wait(tasks)


if __name__=='__main__':
    # 修改事件循环的策略
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # 创建事件循环对象
    loop = asyncio.get_event_loop()
    # 将任务添加到事件循环中并运行循环直至完成
    loop.run_until_complete(main(loop))
    # 关闭事件循环对象
    loop.close()
