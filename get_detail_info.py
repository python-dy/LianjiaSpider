# -*- coding: utf-8 -*-
'''
作者 : 丁毅
开发时间 : 2021/5/29 14:37
'''
from lxml import etree
import asyncio
import aiohttp
import pandas as pd
from pathlib import Path

current_path = Path.cwd()

def get_url_list():
    df = pd.read_csv(Path(current_path, 'detail_page_url.csv'))
    df.drop_duplicates(keep='first', inplace=True)
    url_list = df['detail_url'].values.tolist()
    # 取url_list中的前5500条
    return url_list[: 5500]


async def get_detail_page(url, semaphore):
    async with semaphore:
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
        return parse_page_text(page_text)


def parse_page_text(page_text):
    tree = etree.HTML(page_text)

    house_info_dict = {}

    house_info_dict['title'] = tree.xpath('/html/body/div[3]/div/div/div[1]/h1/text()')[0]    # 标题
    house_info_dict['follower_numbers'] = int(tree.xpath('//*[@id="favCount"]/text()')[0])    # 关注人数
    div = tree.xpath('/html/body/div[5]/div[2]/div')

    house_info_dict['total_price'] = float(div[2].xpath('./span[1]/text()')[0])    # 房价（万）
    house_info_dict['unit_price'] = int(div[2].xpath('./div[1]/div[1]/span//text()')[0])    # 单位房价（元/平米）
    house_info_dict['build_time'] = div[3].xpath('./div[3]/div[2]/text()')[0][:4]    # 建造时间
    house_info_dict['region'] = div[4].xpath('./div[2]/span[2]/a[1]/text()')[0]    # 房屋地区

    # 基本信息提取
    li_list1 = tree.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li')
    info_name1 = ['house_type', 'floor', 'house_area', 'house_type_structure', 'inside_area', 'building_type',
                  'orientation', 'building_structure', 'decoration', 'users/elevator', 'elevator']
    for i in range(len(li_list1)):
        house_info_dict[info_name1[i]] = li_list1[i].xpath('./text()')[0]

    # 交易信息提取
    li_list2 = tree.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li')
    info_name2 = ['listing_time', 'transaction_ownership', 'last_transaction_time', 'house_use', 'house_years',
                  'ownership', 'mortgage_info', 'room_spare_parts', 'house_verification_code']
    for i in range(len(li_list2)):
        house_info_dict[info_name2[i]] = li_list2[i].xpath('./span[2]/text()')[0]

    # 去除抵押贷款信息中的换行符和两边的空格
    house_info_dict['mortgage_info'] = house_info_dict['mortgage_info'].replace('\n', '')
    house_info_dict['mortgage_info'] = house_info_dict['mortgage_info'].strip()

    house_label_list = []
    div_list = tree.xpath('/html/body/div[7]/div[1]/div[2]/div/div[1]/div[2]/a')
    for div in div_list:
        house_label = div.xpath('./text()')[0]
        house_label = house_label.replace('\n', '')    # 去换行符
        house_label = house_label.strip()    # 去除两边空格
        house_label_list.append(house_label)
    house_info_dict['house_label'] = ','.join(house_label_list)

    df = pd.DataFrame(house_info_dict, index=[0])
    header = False if Path.exists(Path(current_path, 'house_info.csv')) else True
    df.to_csv(Path(current_path, 'house_info.csv'), index=False, mode='a', header=header)


async def main(loop):
    # 获取url列表
    url_list = get_url_list()
    # 限制并发量
    semaphore = asyncio.Semaphore(500)
    # 创建任务对象并添加到任务列表中
    tasks = [loop.create_task(get_detail_page(url, semaphore)) for url in url_list]
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