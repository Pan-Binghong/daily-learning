---
title: 基于Huggingface镜像网站下载大模型及数据集
date: '2024-10-29T01:52:00.000Z'
lastmod: '2025-03-20T00:51:00.000Z'
draft: false
tags:
- LLMs
- HuggingFace
categories:
- AI
---

使用镜像网站下载大模型及数据集, 以及配置下载参数(本地路径等)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/dc82f140-d63c-44e4-bc53-0bc220caf11f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4P6YWX5%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICxcjJKadpO8PcR%2B4JGG5%2BYzUviI4882qgLbiShfk%2BXDAiEA%2B%2Fb3L7IHIWNX5bZZIqa0YNdFIhIJIcal%2FXA4lZUAGQ8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDgX1XWQ2tUQ%2FYPufircA3VP%2BQcQe5cIsAfxlXjUWihmf8zKyLveekU%2FCd8xzKZN5CFFvdIjrcNFrC7Wj4ulRB6OnfUGWtdhLRNpSQrbCIun7qf%2Bv%2B2lD7zGJQI%2BCd68BmcrYVTMvzrPvyT2rIO5Z%2F%2FCcNjvXIGIv6nAi40brNfiadruijsJaNsu%2FZqEjgzGORZFvyItKotMswudCU6tWqyppjn2%2FGgwlJSfySKI5l9F3LCeSa3Hri3qYyS%2Fh1tvj%2BdWRFOJjzXLA3I7g96wLPAZ76pGxtKDd%2FYYfT9iNX0YXApzV7yJGHgbLI4AX2G%2FUmRrSxe4eQshQ82sGUwEW7FaPXtxsQAdjCCWYGJwsHZXLnz%2FLaBvxRmx7nTxw3rgY3LGEtLwiAX8abQTYseaOb%2FMEWctmgyzkFZSLjnEXeZZmmHdExHzR1wj7t%2FHkKJmU8vO%2FwC5xI1pimbpSmCSM0HOwsTe%2BGxdd%2BO505b9T4EJ6cljUg3MC9md327S0zdZK1D9omdaDYO6N8QMikSIo3J4mho6iwam1lBDWe3k%2BKk1rLdPRoMzgV1vKUGmk9OKuazJz%2FTZpVOHRJI0Nvi7mOliZUE1q2dXmpCbCgU%2F1dK76hfbhlXmuPgz5XI5ofKzhBrmFw3DBYIbSQI5MPmXpcwGOqUBpHlvr3vXc40%2FCaAP5%2BT00bzZRgeEQCLgSOu2zqPVGJPue5ydmJB1ytwuXnAEfjnuGFZS%2Bx3L3g%2B%2FuKLq6oXZSyeZ6l1R32HC37qlYwsS4nahbk%2FVXwgHmyUZWgnl1UeVKmn5%2FjjYnmXPpE%2BoPH%2FlGNPlyqgZljfk3cCCXhVQ6JrJrdUasXCIsB2UrsK31ySCQRBOM9BabW%2Fy%2FEbGqqxjIngsOmEq&X-Amz-Signature=0a3749c1fdbe4df552d8905dc1974a3d53f625d83c8f4ee6126f6d12d2543f70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 基于HF镜像网站下载大模型&数据集

### 命令行下载

- 安装Huggingface依赖库
- 下载大模型命令
- 下载数据集命令
---

### 代码下载

- 首先获取Huggingface的Access Tokens
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/22b8dae9-3302-4380-a23f-5402b524f0a9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4P6YWX5%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICxcjJKadpO8PcR%2B4JGG5%2BYzUviI4882qgLbiShfk%2BXDAiEA%2B%2Fb3L7IHIWNX5bZZIqa0YNdFIhIJIcal%2FXA4lZUAGQ8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDgX1XWQ2tUQ%2FYPufircA3VP%2BQcQe5cIsAfxlXjUWihmf8zKyLveekU%2FCd8xzKZN5CFFvdIjrcNFrC7Wj4ulRB6OnfUGWtdhLRNpSQrbCIun7qf%2Bv%2B2lD7zGJQI%2BCd68BmcrYVTMvzrPvyT2rIO5Z%2F%2FCcNjvXIGIv6nAi40brNfiadruijsJaNsu%2FZqEjgzGORZFvyItKotMswudCU6tWqyppjn2%2FGgwlJSfySKI5l9F3LCeSa3Hri3qYyS%2Fh1tvj%2BdWRFOJjzXLA3I7g96wLPAZ76pGxtKDd%2FYYfT9iNX0YXApzV7yJGHgbLI4AX2G%2FUmRrSxe4eQshQ82sGUwEW7FaPXtxsQAdjCCWYGJwsHZXLnz%2FLaBvxRmx7nTxw3rgY3LGEtLwiAX8abQTYseaOb%2FMEWctmgyzkFZSLjnEXeZZmmHdExHzR1wj7t%2FHkKJmU8vO%2FwC5xI1pimbpSmCSM0HOwsTe%2BGxdd%2BO505b9T4EJ6cljUg3MC9md327S0zdZK1D9omdaDYO6N8QMikSIo3J4mho6iwam1lBDWe3k%2BKk1rLdPRoMzgV1vKUGmk9OKuazJz%2FTZpVOHRJI0Nvi7mOliZUE1q2dXmpCbCgU%2F1dK76hfbhlXmuPgz5XI5ofKzhBrmFw3DBYIbSQI5MPmXpcwGOqUBpHlvr3vXc40%2FCaAP5%2BT00bzZRgeEQCLgSOu2zqPVGJPue5ydmJB1ytwuXnAEfjnuGFZS%2Bx3L3g%2B%2FuKLq6oXZSyeZ6l1R32HC37qlYwsS4nahbk%2FVXwgHmyUZWgnl1UeVKmn5%2FjjYnmXPpE%2BoPH%2FlGNPlyqgZljfk3cCCXhVQ6JrJrdUasXCIsB2UrsK31ySCQRBOM9BabW%2Fy%2FEbGqqxjIngsOmEq&X-Amz-Signature=8adaa1bce96063b0a50b50812181e2978cd38acdafcdf1b42b0e05ff1dbbf1bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 下载代码如下:
- 下载数据集代码
---

> References



