---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKNV67RW%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF5vgO7Zebe4FZfJG6H3AssX%2Bz8oVNanrpH9PIbqZ22SAiEApYvD%2F%2FZ3ebU9%2FHl%2F4PcqgSIGyFE6FT19tk2iXG3G8BYqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI36a2yhrxhxcu5W%2FCrcAyoBG3jqtX2q9wsKvc2lRQqpu1yVvgBCl9%2FCXDHvLRECOsF4C8dDyPK7g2F1U0zTJzOd7YlDuSuQhGm8HPi9GvrxKFL4L6uzKePeH%2BAzBupWm1Cbq2U8AZiGwX%2FftI6YaTxqxMcbcW%2FOkxfPqXIAvyS6iOdVhOjknyTlW8mzQ5T6iEX12zo0ZvGG4bSYwb1th2DFziUlY6S7IdJ0fs1nrX3iOdDPfCY4RVc47pXlF28qdZV3ikPqwG7ba17viX7%2BEX%2Fjse3uiQiH4CAIwTubSmH4os%2BRdvBkF1LEVNvaB7omun%2BPTx%2BKiwrHZbpynGJnTjXeCYlvFrOlmnMeyGq7XGf5XNNxHXitXwXlxDlYKdDPMsBKMjbhUtaIbr4wV6x80GK9x59b9Ib7Xj8rIRYlMlezqc5pw0et4K98F%2BcSdOPIKQlN2YslRQa4luU5LBnbw6NENhyWEt%2Bkh4nUnjPC9mZYzkONjXxyDALfb%2BTJ2suDW7WcZUSGjvzBGAUpG94DWiDFSwn8qDh9B29rm%2FVvbGf0pFAyx6WQW84InS6CTt9OhydLakFVgmhsB6on4TcUcSDSKUyw8DmD2JWhC%2BJGuFFCVCvjpLcfLsZIrbRb1FbT4av0qIS9CFo%2BjbVTMPSU%2B8sGOqUB%2BtpMTwui%2FXk%2F2M%2FQ8Va%2Bj%2FWEBhntlWSJzZyqhJOtdoPg%2Fr35FSrOsDjmT1QT%2BQHnQ%2BgkogpJq3lTn9WpCZ%2Fyvs2i2HPRyf02HHYS5j4UIh4%2FG5zooO5tySgcQf2wZ9CWSqhDr9QSiqyj7CWdSjOSg4CFTwh4g%2BcBZua%2BnWA%2BBe43YzzT1XQ31wakHAPYNzzY8ahXNhjdRSEYrJl5DSLx9BkhZjwi&X-Amz-Signature=a93fcae7c3f5694b4f8e572748da46568bb2ad0e8e739f1873eaa67e139d41dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

