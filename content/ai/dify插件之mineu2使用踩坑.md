---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466422TPKZS%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQC4jJJHpDqpeP2lNSvRVDKd8MuYy8WTZLYHmNLnLf73twIgezv9pCekV2QNhhxW%2BVwycz0JslGhLW78nztgcd%2FrSHgq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDEL0G8sDiGH1%2BdGbFSrcA3JBII4YRtSHPmnj0giFkopNAH%2B1UXPNUCxkZRi%2BFgUnH43LXRdtrt2c4UKsjbMlvkNfwKVPf09DSbl6KoDAgbVbgwoxF5v4d2nCSUSI6FYW1hRjF%2BuhuVZ1WU3sVjg6u1aJrFATWx6%2B%2FesNIleO%2ByYEYwG0lV8NLCjvOhFH751kBtvMmHxTCB%2FOkloaDTlvYjuy61FZYTIoEPnZYSvZPiNWizLZ95fYKtgp%2FISSTgPHcpyUs5ci5exdbYvNP64AXzwMtrqDms9Cx8DMWWVFsxjnzGYl4KQ5497cg%2BSzklwmGQ4tChky3fEfHWU0YD%2B08EPj1XeMYwXVLzM3PrZKe1Dln4qFNQ1x%2Bcm5H4zBB8kSQVRQOe8B4367qhCSgUEACJJPKsLue4oi%2F5CDa893h%2BpHR439Ww%2Bv2AfJkiot0CQUP8BnR%2Ft9Oh6amx4bTTqDLWWAoYopr9gzEFbedA3s6zcgXMcZHIg6YRJD%2BWCERTwakGuCXoiCkVub1N%2FTKB4I2yEyT7sB5SoPYEY092%2FX44%2BIHiBerTDhpsb4yrGa%2B4Leo3S5Xkifhrzi%2BEo95tISNwUDRcT8aiyj9MPKxBaSAOGHe3wYWNs9aDzfBt8Qi2547C%2FJi8zEbJxu7NjDMOPfuMkGOqUByVLoZXeI6yRHwrk7WBNTFwgoAcJnJn2VXncd1E53Da0rvfQo6WOLG8pxWLVs2ISzu%2B5xvis2gNvtuyMINL%2Fua3ktUJqpz%2FsBCJSZY%2F9XoYz31yfWZAHWypbG9zqHQVhQOHiOCgumiNvOqC8YmM9B9dkgLVkXdyoFCMd7yotb9Ra6HtgGs9SbMEbynhnmk1K%2F6Gl86Fn%2BqKm2lXkqqlZ1CU8%2FoeRb&X-Amz-Signature=53161c32539e7bb298dc37a7ca203cec49b70bb8a73868a023f0c3acd40a6c06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466422TPKZS%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQC4jJJHpDqpeP2lNSvRVDKd8MuYy8WTZLYHmNLnLf73twIgezv9pCekV2QNhhxW%2BVwycz0JslGhLW78nztgcd%2FrSHgq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDEL0G8sDiGH1%2BdGbFSrcA3JBII4YRtSHPmnj0giFkopNAH%2B1UXPNUCxkZRi%2BFgUnH43LXRdtrt2c4UKsjbMlvkNfwKVPf09DSbl6KoDAgbVbgwoxF5v4d2nCSUSI6FYW1hRjF%2BuhuVZ1WU3sVjg6u1aJrFATWx6%2B%2FesNIleO%2ByYEYwG0lV8NLCjvOhFH751kBtvMmHxTCB%2FOkloaDTlvYjuy61FZYTIoEPnZYSvZPiNWizLZ95fYKtgp%2FISSTgPHcpyUs5ci5exdbYvNP64AXzwMtrqDms9Cx8DMWWVFsxjnzGYl4KQ5497cg%2BSzklwmGQ4tChky3fEfHWU0YD%2B08EPj1XeMYwXVLzM3PrZKe1Dln4qFNQ1x%2Bcm5H4zBB8kSQVRQOe8B4367qhCSgUEACJJPKsLue4oi%2F5CDa893h%2BpHR439Ww%2Bv2AfJkiot0CQUP8BnR%2Ft9Oh6amx4bTTqDLWWAoYopr9gzEFbedA3s6zcgXMcZHIg6YRJD%2BWCERTwakGuCXoiCkVub1N%2FTKB4I2yEyT7sB5SoPYEY092%2FX44%2BIHiBerTDhpsb4yrGa%2B4Leo3S5Xkifhrzi%2BEo95tISNwUDRcT8aiyj9MPKxBaSAOGHe3wYWNs9aDzfBt8Qi2547C%2FJi8zEbJxu7NjDMOPfuMkGOqUByVLoZXeI6yRHwrk7WBNTFwgoAcJnJn2VXncd1E53Da0rvfQo6WOLG8pxWLVs2ISzu%2B5xvis2gNvtuyMINL%2Fua3ktUJqpz%2FsBCJSZY%2F9XoYz31yfWZAHWypbG9zqHQVhQOHiOCgumiNvOqC8YmM9B9dkgLVkXdyoFCMd7yotb9Ra6HtgGs9SbMEbynhnmk1K%2F6Gl86Fn%2BqKm2lXkqqlZ1CU8%2FoeRb&X-Amz-Signature=bd743e245c4dd15a3d51bf329992565296a9e55db3c02fdaef7fbe32389d8d8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



