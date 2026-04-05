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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HU4VTME%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYEYLhyU21NjQBC8TH0cO2fJkRh3oqNzXN4G%2BfGk5cBAIhALeeD5VW2o0q3%2BumtmxHJI%2Fx%2BCVGPqTLR7X0JRTHnraaKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzdP0WzN3jzjdSOZ3kq3AMrqkgc4Ro5UOMIr7bcnx1DWZYfhjGSnNDkoG1FPYR%2F9P170d0NUqBN0IJMeyTU3YI0ovcmve%2FQyhwT6YGoZfaSjNQayODAsejPeawwpaMHOMfYkHis7kA6k6PvYGOQYqTDLIAhQs05QCprbwDheWL2iDdXCnj12tDyMxfKhjBRcCnB8sLWKjSNfAbRr4GUVEiuTAvidmzZPS1HRW3rif%2BCfP47LKZB1ImcOop00ebfpXlbSnJEpZJnnhhLwIDD2ntzJjVlIuhji5MaWh0%2BIXRFAg0EOx9jjfHkooNdqYZBiib2W9QaPCDdZmWv4o%2BcJ9qtDuHSfUaWgV7Ubo4p08iEs62LcE%2Frt%2BNzEqTXOoZSOX4G8q0%2Bg7nPnXyBuyoBj0PV3bR9mudhN0SJb8FTEzniUJMs1HUSSrGUYW1le7bTghqgfKiXlpsf7ZwOJlahsi%2Bv9xeQ%2FVdEr0ZkAbu0TSX%2FbYyv%2FHz9ObqugMi1fql4JvYGbCl5%2BXltg9IWiKu5AtffIgfmUIHAKuSZU6g7ROZgog5padUO2qtm1p%2BFm7cdidp95DIatabmAwJl767lSQQ464kI0nX8sTedpO%2BZDayz0R4IkEohVHA8neLbhsOZh0F9YRus85960x4H4zDyn8fOBjqkAXHoQqGevuzWgxia2a5zdXmCUZh5Bhti9UOKqYlwYJ5B7Xty9SBt6F6SVHpZ%2FxsIFMuQO9BgXS2gleAY16cE%2F1eQOMAQfsPFCj52hYuI1bTNqMlQ3w%2Fe6dR0RpGuaY5sq360Pl9wCnnhA%2BihSnGZxMCngzaIYPPvXYZ7jN%2B9jGQLiu5gVg6hAB6IBCNV4nyF8jKcc7v5chg0O6MWbpHimKGzWFGB&X-Amz-Signature=5214ffd1f2028d598c388c40509ca885495444e7839fb7abe3892b5847b1c7ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

