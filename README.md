# FUND_allfund

[Purpose]:
collect and analysis all the public fund and select the most stable one

[data acquisition]:
From: http://fund.eastmoney.com/allfund.html#0
By: Scrapy
Content: allfund

[data storage]:
Mysql: Dfcf_allfund

[data analysis]:
By: Jupyter notebook
Content: EastMoney_Fund.ipynb


目的：
获取所有开放式基金不同周期（1月，3月，6月，1年，3年，成立以来）的收益数据，筛选稳定收益的目标。

数据获取：
scrapy抓取 东方财富 基金收益信息(http://fund.eastmoney.com/allfund.html#0)
文件名：allfund

数据存储:
Mysql: Dfcf_allfund

数据分析：jupyter
文件名：EastMoney_Fund.ipynb
