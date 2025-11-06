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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTRQO2W2%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGr83jGPIznkH0SierwS8z3Zn2sI31fkkizjLnwCKKbcAiEAxxAtGw2pTY7DBlWGhSWrL1WjEmx7Umdt7zJTOrefBIkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOSICemTIcZ%2B9pAgECrcA0Q0FYTQh6lFGOkA2pyAZ%2BY6KQaYihnyUv2Vt6MDVoUzLE6zFvRpvhqLfrtoJR67MTNN%2Fsd4AKhg8viixVyIwdorhmRqiL%2BsYJiJm7CHrNIzx6QbOzirYt9h4%2B2icT9kdi8%2FjOY0o9s8yc4PbDR2ueOVguaB%2F8x2fdLBIgEWv70SzvD3%2FjTci42xddBrzvtFHsiGWsdKgvk1UKZFnBp8LW6Evw7GYGpIY3%2FcHD8tlHFMhk7eDyWB%2B9hFyZh4uanKBJYDenxb4b4grbc0fU5P8A18lL4eG2%2Bu8uSrFvqTvmZYOZ%2Bo4I1kFCN8w70pu6hw0Olxl7RjZzn7HGgUi6R%2FM2crfn174%2FOp6L551b2PcXWhwVJ4y1eU7ES1QcVJptotr3EoFkIkEGodvQXd%2BLDwfWp3KYbKS%2BSbX2ODTBtgws8geJnO55uCYj84po2fAEQ%2F20aMshRvEEpfbNSBJSQiJjkMHxWwC7Cxu30nXm6lTNGffZhxCTN7JJ3MrL8w%2BpbfPKGl55%2BldpfafpzwwJqtXNHT1j4fVjv2kLd8g%2F52zL1l4MmmsyfXf3VzntJyEbAVTE6NKJ7UpIYCxA8dVHinSX6jIWRbq9a5ufTG1rWJ0WiqI3K%2FGQ3KbqyvAUx1MIyWsMgGOqUBGZM%2Bn0y15a%2Bn8pO%2FXOBLHY61gMkr%2B6GCXi8VRh%2FZVRuE%2Fhda7t1x0Y2LcMe6jFdfc8vNgbhuij%2Bq4M6PXfKjaGf1fToHW0s6JIuX4eWSUwRbg0EiTe5NaBsRiAWkT1%2B2ALJfTWiLBH2a5APxq%2FOcg4tYPI1K5vPTI3LNy3ATLxzciRsFaNB5xrRL3dBd2tw7IaZs50sEzaq7qvDybxdGKCRGq5rK&X-Amz-Signature=29e5f68aa8173badb9e97903d936bb1fca8582d7ff4c0cbe88e501fb2c30727c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTRQO2W2%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGr83jGPIznkH0SierwS8z3Zn2sI31fkkizjLnwCKKbcAiEAxxAtGw2pTY7DBlWGhSWrL1WjEmx7Umdt7zJTOrefBIkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOSICemTIcZ%2B9pAgECrcA0Q0FYTQh6lFGOkA2pyAZ%2BY6KQaYihnyUv2Vt6MDVoUzLE6zFvRpvhqLfrtoJR67MTNN%2Fsd4AKhg8viixVyIwdorhmRqiL%2BsYJiJm7CHrNIzx6QbOzirYt9h4%2B2icT9kdi8%2FjOY0o9s8yc4PbDR2ueOVguaB%2F8x2fdLBIgEWv70SzvD3%2FjTci42xddBrzvtFHsiGWsdKgvk1UKZFnBp8LW6Evw7GYGpIY3%2FcHD8tlHFMhk7eDyWB%2B9hFyZh4uanKBJYDenxb4b4grbc0fU5P8A18lL4eG2%2Bu8uSrFvqTvmZYOZ%2Bo4I1kFCN8w70pu6hw0Olxl7RjZzn7HGgUi6R%2FM2crfn174%2FOp6L551b2PcXWhwVJ4y1eU7ES1QcVJptotr3EoFkIkEGodvQXd%2BLDwfWp3KYbKS%2BSbX2ODTBtgws8geJnO55uCYj84po2fAEQ%2F20aMshRvEEpfbNSBJSQiJjkMHxWwC7Cxu30nXm6lTNGffZhxCTN7JJ3MrL8w%2BpbfPKGl55%2BldpfafpzwwJqtXNHT1j4fVjv2kLd8g%2F52zL1l4MmmsyfXf3VzntJyEbAVTE6NKJ7UpIYCxA8dVHinSX6jIWRbq9a5ufTG1rWJ0WiqI3K%2FGQ3KbqyvAUx1MIyWsMgGOqUBGZM%2Bn0y15a%2Bn8pO%2FXOBLHY61gMkr%2B6GCXi8VRh%2FZVRuE%2Fhda7t1x0Y2LcMe6jFdfc8vNgbhuij%2Bq4M6PXfKjaGf1fToHW0s6JIuX4eWSUwRbg0EiTe5NaBsRiAWkT1%2B2ALJfTWiLBH2a5APxq%2FOcg4tYPI1K5vPTI3LNy3ATLxzciRsFaNB5xrRL3dBd2tw7IaZs50sEzaq7qvDybxdGKCRGq5rK&X-Amz-Signature=c7ec67818154f9614db5c3c2e2a817e2c912a76ae59a98cc7ebcabe4f9657d45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



