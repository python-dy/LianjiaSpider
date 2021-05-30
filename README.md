# LianjiaSpider
异步协程的方式爬取链家二手房信息，包括子页面基本属性和交易属性。

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
