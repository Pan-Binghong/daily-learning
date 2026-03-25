---
title: 基于Easy DataSet创建自定义数据集
date: '2025-03-27T03:06:00.000Z'
lastmod: '2025-03-27T05:53:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 前几天看视频发现一个开源的构建数据集项目，打算复现玩一下。这里记录全流程。

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS5HDBOG%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFkHLXp4s8yOUTFy3KQrhBJbofit4EPCa2BAb4bzUOmhAiBl%2B1CydWPB1jU6gJC6GWuNgL5%2BowOdJW3O7XB4oVF%2FISqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi8ax6Un32bq7Dfz4KtwDAKhzVWzhOW1pU9b19Cb8OLm6U5LhLYVt2%2FTPPY2XcJV77d30Kax10L2YDCKlGqxk%2BGwI7vnQQPQUOptxzMmJU8RJ%2BkAmxV2jbiUVylGsXJGmORbI3yQpoZl8ffCIXy%2Bf3ed8tgR6dow0D0kCJDoEOgI3sAEdnjuiN1kmM9rorDu7s6ErDcHVKiFkzL%2BZJ%2BHUMJvczmpLyhFDEPjRFZSVyEomBxOhANQqpLLB3UHJURsGQFQD9h0mFkl2tIVKDsVsuzAY8hIvNt5nx6wmbyBIdV3h5XYAr7JWkez8l%2Btc3l%2F22PPFEnf811jSmQrVo%2FN5WH2s5SbyBoQvQahCQ4ZZIp7CZnv8XLlilCcYbn2O4pJVmi%2FBJNuHLvlkXR0nBEQUiH3HKcZUynb2c6tZ5M0LKr%2FpP4PrM03oqRG1AjdFaHbfE7G4BazYkfYKWTe0pAw7OWK6swkKkCv9Qur6bGpkyxATFtvyCD2a7e9vFD238iDdpKiGbeLNPAW3BICtHtqS%2BcWWOaVq3KSPtKVENOTDB6tkDjUkKCd8Y%2FH%2FbWXOXX6MaSUkfv%2F8w5DX6%2FzVgkNjB6gNjjmQLBgmm0GPDm%2BXxa4o7uo1UHvqt5Ph45qPPHHOgxFPc2%2BfuX1Fvgcw3daOzgY6pgExvYlljgsMRYWLdIF3N6lHYaAOzJrgR5hRAuGGIquHCMgUuScJhBcHFeFnNqYXFnsyNbnlYUm1BF%2Bego%2FMPLFhU0k%2B7q3Esi%2FwKllOHZso8WFMBKRp4LQOW7HvKYMy69jQR8LIQp6kDmvUASe9XaNzxZ6TIOf%2FNsKKtFaYPHcBWBEpFapICsQ1vcuU9KNwdVaH3kl5uKwafZqxcFWexzzvj0rnBUeT&X-Amz-Signature=647f00ab0e3fc95f1e8af156d9b1ed5d200168b044f537db223e98d4955d96f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 环境安装

本人使用Ubuntu系统。首先安装node.js以及npm。

1. 使用nvm，安装nodejs以及npm
1. 安装pnpm
1. 检查安装是否正确
---

# Easy DataSet平台安装

1. 使用github下载源代码
1. 安装代码所需依赖包
> 使用pnpm的特点:

---

# Easy DataSet启动

1. 基于代码构建项目
1. 启动应用程序
---

# 怎么使用Easy DataSet

1. 新建项目
1. 配置大模型
1. 上传数据
1. 基于分割的文本，构建问题
1. 构建数据集
1. 导出数据集
---

> References

