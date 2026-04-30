---
title: Open WebUI私有化部署|vLLM
date: '2025-03-17T01:36:00.000Z'
lastmod: '2025-03-21T02:48:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 在裸金属上对DeepSeek系列模型进行指标测试后，有点无聊。随便部署一个WebUI玩玩。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KQJKFU6%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIFPh63mVUdSBDFIMqKfUolW2GObg6tKaIuEs%2Btcv2y%2BmAiEAmmCGDKKlDeahZE4qZo7EWEP%2BHcoTRYlGgIzNu4PjbG4q%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDHPfRVPTRbua4zekdSrcAxgcqo%2Fbhdhu5J57KcYsQz3JYrt3F34zUB8u6tunXDEod1TlYiubpBKMnj%2FJQBSYVz0QH5Ng1FTkQ5%2FXYfDbQ9utxkybfjZ%2BN0StCKJ0mpYUripqPdXMhEIjFilvRG4%2BrVPtR0Fx9MHFuY%2BJOvVmT%2F0VAtC2U6LFd2G%2FzqxqGBQNZ%2BYzB8LzAG6ie5LZ3EZMuNZx2%2FFDrc4cSy0IZMk4qV2629BB%2F7ogwvZBJqdidpj%2BbDxzsIB%2BrgLYgmtm4iTcG8xNJhOZ5USOl4Q8FNHu8jqtpBU6dD4BjtJ1xS2jK9dG0lIxJT6FBNFt3iZQDF%2FIBcl%2FZlG49BQzES4xc3Kj39vXA9XlnpOj1UwEyeCRyGjC19xOCf17Zp4UlfwpyJGyopZtVIonJl4wVwmsWBUjEmY2qu%2BPClNTe4QZj%2B2O0gXb3hzALmbnyb1aS9vsK31nUXyzjhS%2BsRQe1JF6rJr%2FjwkA9jAKPyeZHlymKS%2F%2B0PPeMUMXJPMJMFdMvnIMkCh5FjtgRO5AkDb4onKzaRkhOLdn3BDJQ97ywhYYnjKzjB7lBCWq4NSwx1p5%2BOV5vTrqe%2Bx6p6tLdZCkm7RyeXb4C9lXCEfD%2BS9Pasf%2Ff8RPU6bGh0hnQ6rAAZoLKVP2MPedzM8GOqUBh7iQDYWsxqasSRdMTEuXHK3YvEtxUT6MeqHLj0V4pEcxY%2Fc1qp8KvggUY1WjU56MRQeH5ukPz1uWb09NIlvN9QfuByxVaKqsz9OM%2FxCWBTM3sVf7d7OaMFWXomlKegQpDSGEaqL%2FSk1g8x3kxPI%2B2yLzlVQKbpJ%2BVWkkZHoTvpeTwvsyYov2mAuV1qJZuL%2BOUUPjaQzw2IGLK6hvzU%2Bbd8yL9OkQ&X-Amz-Signature=1f339d215732df7dc79a9ecc675f23f63cf77e0c977217542eda50aa549fcc95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 安装

该前端框架采用docker镜像部署，模型采用vllm镜像单独发布。

1. 拉取最新版本镜像
1. 启动容器
1. 打开浏览器查看8000端口 
---

## 踩坑

- 模型URL地址要写V1 
- 使用openai api进行链接一直报503的错，进到backend/open_webui/utils/model.py，注释以下代码即可。
---

> References



