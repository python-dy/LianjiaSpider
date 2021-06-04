# LianjiaSpider
asyncio异步协程的方式爬取链家二手房信息，包括子页面基本属性和交易属性。

---
<br>

## get_detail_url.py
爬取主页面中各房屋详情页面的url，保存到detail_page_url.csv文件中。

---
<br>

## get_detail_info.py
爬取详情页面中的以下信息。
<center><img src="https://img-blog.csdnimg.cn/20210530142749561.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTY1NzA4,size_16,color_FFFFFF,t_70" width=50%></center>
<center><img src="https://img-blog.csdnimg.cn/20210530142957853.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTY1NzA4,size_16,color_FFFFFF,t_70" width=50%></center>
将爬取的房屋信息保存到house_info.csv中。

## 武汉二手房可视化.ipynb
对爬取的数据进行分析及可视化。
可视化图形：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210604092709907.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTY1NzA4,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210604094930106.gif#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210604101022297.gif#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210604151833749.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTY1NzA4,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210604105242100.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTY1NzA4,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210604111251379.gif#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210604112809258.gif?#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2021060411374613.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTY1NzA4,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210604141358276.gif#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210604142107512.gif#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210604142757311.gif#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210604150023996.gif#pic_center)
