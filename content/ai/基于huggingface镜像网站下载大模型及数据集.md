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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/dc82f140-d63c-44e4-bc53-0bc220caf11f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZANZNRD%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbRoHcXLBKyextECU2d%2Fgwi5sa3YGXmmn%2BrZXZMgJmoAIhAOWoE8uXOMR8IB6cxoubae%2BmXRCjSO%2F6z%2Fc%2Bqt9mSqFhKogECLX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwbfN1xp4O3Wf9Cm44q3AN8%2Fn%2B705h9Fd%2B0GhZkNeLYIWat4bYgbciF7da2d74%2FV4rMgct%2BF45E9r%2BXajVPGHA%2BgGrYmlcgeS8a8F1ajjYEGdP190CrY0X0uUOwmFvQeYyBVLdlAVAK2dr31x2y8Oz1o5oekzwC0syD6XdbXJOxZ1zJJvfQBXSgI7usNfZwVmo7rIxHweYiayH7bW1enhkeRDvfXxcgPSXyN7AbwWkExIfeYT%2FGj4ci%2BaRqiALzyKNO15dUzSGReldL340wPnjOT3GMEDTw1Y2qKvJwfHJBO1Srh7yefd0z5USkIq2zMlep%2BDx2ZUPZjfP9N1cWd8fsFEYURO%2Baj4rSuXo6LaMwZPT1CuyG6scU1v%2F6QVvnLVVYecqBu%2Bza4L5zUSm5HXBsSt%2FUYRdiXDp8CtlsdQ6UvDrbh3QfI4jBo%2BBT2RsCnGITpnK5J7iT%2BeVG25PoMaJEeRcYzREtGRMS52TDnWrdCtgof4Df%2BpKQ8HwcUWcZyyqzgaJCqoLbP3kkXQ3LyXD2CTdS70nbhpRatg%2B%2FH%2BFWZKdfwpNuQVHuCwJlKFXGi0wNm8qPgOfDeisyHhxXJtLpdkAYBAj7YCtTm00RoElzlbGI2%2BXtpaaMvm%2FCHUTfnJTblT8huxz1jtQmzTCqw4HPBjqkAd%2F3Vjcfv8vX9ceL5%2FZii9XN9OV9WMTStQnWn1%2BEsp2BihEktgJ1%2BQpMv1Ps7rAuSyJg%2B38x9D0ZC%2BFydoUWrKos6FDSxhHg5jYpwdOnNkTpmTDvVMXJmdKth%2Fgg%2F6q05ZSxXGe5bzNFfgXYayZIq3S5W8EMz3GzwaDWe%2FEz8AfDMJTDqiDqYLqshcG2yF1Q9BNuv%2FHNRUVKco28v20DXVlj6u9J&X-Amz-Signature=168ef4649ea6d229eb2e16fbd2b62dd8bdaa09573beece578df4bfd245d3ccef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 基于HF镜像网站下载大模型&数据集

### 命令行下载

- 安装Huggingface依赖库
- 下载大模型命令
- 下载数据集命令
---

### 代码下载

- 首先获取Huggingface的Access Tokens
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/22b8dae9-3302-4380-a23f-5402b524f0a9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZANZNRD%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbRoHcXLBKyextECU2d%2Fgwi5sa3YGXmmn%2BrZXZMgJmoAIhAOWoE8uXOMR8IB6cxoubae%2BmXRCjSO%2F6z%2Fc%2Bqt9mSqFhKogECLX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwbfN1xp4O3Wf9Cm44q3AN8%2Fn%2B705h9Fd%2B0GhZkNeLYIWat4bYgbciF7da2d74%2FV4rMgct%2BF45E9r%2BXajVPGHA%2BgGrYmlcgeS8a8F1ajjYEGdP190CrY0X0uUOwmFvQeYyBVLdlAVAK2dr31x2y8Oz1o5oekzwC0syD6XdbXJOxZ1zJJvfQBXSgI7usNfZwVmo7rIxHweYiayH7bW1enhkeRDvfXxcgPSXyN7AbwWkExIfeYT%2FGj4ci%2BaRqiALzyKNO15dUzSGReldL340wPnjOT3GMEDTw1Y2qKvJwfHJBO1Srh7yefd0z5USkIq2zMlep%2BDx2ZUPZjfP9N1cWd8fsFEYURO%2Baj4rSuXo6LaMwZPT1CuyG6scU1v%2F6QVvnLVVYecqBu%2Bza4L5zUSm5HXBsSt%2FUYRdiXDp8CtlsdQ6UvDrbh3QfI4jBo%2BBT2RsCnGITpnK5J7iT%2BeVG25PoMaJEeRcYzREtGRMS52TDnWrdCtgof4Df%2BpKQ8HwcUWcZyyqzgaJCqoLbP3kkXQ3LyXD2CTdS70nbhpRatg%2B%2FH%2BFWZKdfwpNuQVHuCwJlKFXGi0wNm8qPgOfDeisyHhxXJtLpdkAYBAj7YCtTm00RoElzlbGI2%2BXtpaaMvm%2FCHUTfnJTblT8huxz1jtQmzTCqw4HPBjqkAd%2F3Vjcfv8vX9ceL5%2FZii9XN9OV9WMTStQnWn1%2BEsp2BihEktgJ1%2BQpMv1Ps7rAuSyJg%2B38x9D0ZC%2BFydoUWrKos6FDSxhHg5jYpwdOnNkTpmTDvVMXJmdKth%2Fgg%2F6q05ZSxXGe5bzNFfgXYayZIq3S5W8EMz3GzwaDWe%2FEz8AfDMJTDqiDqYLqshcG2yF1Q9BNuv%2FHNRUVKco28v20DXVlj6u9J&X-Amz-Signature=e2524eb2ac8939a968b1781046d8e8a432a5a6ef7a5400d9541953489bf23278&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 下载代码如下:
- 下载数据集代码
---

> References



