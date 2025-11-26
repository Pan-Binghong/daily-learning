---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ5K3POZ%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNLo72zxF5eLrkDO8o%2Blt4hKUHJ%2FEgMLhCFn8fthpcZwIgGj3SajBM5Blz8avuVMIVOvBvmy9Kzjg9mqJRHXu3tuMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDIFUp1ECVc4OJ0Zj4SrcAztj17c%2Ba3MvZj1o5HnxvmvtpPbFy1FkdwNDOTcrXgQyN%2Bd9b%2FhWKeq89Qm8uc2fIY773HIH2pyLZBc4fQRzvcNNFtI%2B6AbDYJ77WeQ2x6%2BwUqwvB0K1V5wPH6A3ZJHdup6%2BPMXC8ymgOHdYuuxrhLe39B9U0kvNgZYuzJccKMmEfyxccvxVcw0Y8qXwFIM9Aq6EGR0waY3m32d8wIYNi8qahpsf1Rhdxc4Je%2Fiqj7qKGWJKVQ6f293H8Bnrq1%2BA1pRxOXjtDILsQ4cF8QbezxBCL6t4ZWo1uvXCrO%2FqYXDeFW34gL83Gldnn941hIqg55R6M2CCy5Odsectv9ODCvIgI8ohdHrDJsW6j6ECIoltvOiUSmFliVSWAI%2BqG9dy61nEwJDS6ODAqKsbM2PBcTJa8ajS68OSHZ0OBNttVL3Zh4yU1v5a1dQrGHAfqcZkIhZG0eGUdWh6k8Onj5sycci8QT0%2B%2F0nWXoWt8P6xOiUt%2BagRUvFLi0QEpv%2Bgpw7tgZBUZHCWoUwtn3XoYqM63ppvTc928%2B%2BMYQ7x1V%2FxVlJGJcryAMfkJSi8ziN%2F%2FE1RK5ImNCZmD6m5FWweZyMO5GoGmIY1gU7J8TBrVEOmHASPwz70m0BV0sldgm1%2BMPuymckGOqUBDnxnoa4DV66uy4o3eE64I4DJvcjrYztFKQRd2a3oFLSOo%2F5sAmPLtfTLNyr0JdVQDfi4MFcj76qTOLQClNXKcVu4QEUC6pKvXm8v7iwNxp3wU9orJVwzQoSsUgGs6xCG89FqCyN7xO2u9hSkZzdGktMTz%2B8oXsnu7yOwe3VV0kPKvEe92wB87MqNw4sLtpwzsgkZuU%2Fr1us1bX603UOJLDETNTO7&X-Amz-Signature=2f62603b0ac9b6397e657a9bd9b8cff6099ecadca9ade41b81a464f5941299f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ5K3POZ%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNLo72zxF5eLrkDO8o%2Blt4hKUHJ%2FEgMLhCFn8fthpcZwIgGj3SajBM5Blz8avuVMIVOvBvmy9Kzjg9mqJRHXu3tuMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDIFUp1ECVc4OJ0Zj4SrcAztj17c%2Ba3MvZj1o5HnxvmvtpPbFy1FkdwNDOTcrXgQyN%2Bd9b%2FhWKeq89Qm8uc2fIY773HIH2pyLZBc4fQRzvcNNFtI%2B6AbDYJ77WeQ2x6%2BwUqwvB0K1V5wPH6A3ZJHdup6%2BPMXC8ymgOHdYuuxrhLe39B9U0kvNgZYuzJccKMmEfyxccvxVcw0Y8qXwFIM9Aq6EGR0waY3m32d8wIYNi8qahpsf1Rhdxc4Je%2Fiqj7qKGWJKVQ6f293H8Bnrq1%2BA1pRxOXjtDILsQ4cF8QbezxBCL6t4ZWo1uvXCrO%2FqYXDeFW34gL83Gldnn941hIqg55R6M2CCy5Odsectv9ODCvIgI8ohdHrDJsW6j6ECIoltvOiUSmFliVSWAI%2BqG9dy61nEwJDS6ODAqKsbM2PBcTJa8ajS68OSHZ0OBNttVL3Zh4yU1v5a1dQrGHAfqcZkIhZG0eGUdWh6k8Onj5sycci8QT0%2B%2F0nWXoWt8P6xOiUt%2BagRUvFLi0QEpv%2Bgpw7tgZBUZHCWoUwtn3XoYqM63ppvTc928%2B%2BMYQ7x1V%2FxVlJGJcryAMfkJSi8ziN%2F%2FE1RK5ImNCZmD6m5FWweZyMO5GoGmIY1gU7J8TBrVEOmHASPwz70m0BV0sldgm1%2BMPuymckGOqUBDnxnoa4DV66uy4o3eE64I4DJvcjrYztFKQRd2a3oFLSOo%2F5sAmPLtfTLNyr0JdVQDfi4MFcj76qTOLQClNXKcVu4QEUC6pKvXm8v7iwNxp3wU9orJVwzQoSsUgGs6xCG89FqCyN7xO2u9hSkZzdGktMTz%2B8oXsnu7yOwe3VV0kPKvEe92wB87MqNw4sLtpwzsgkZuU%2Fr1us1bX603UOJLDETNTO7&X-Amz-Signature=6f6cfab3379079a19f19e5937eef8a63ab464e29ef32c382e6514e180217954e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

