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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KQDMTPW%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHHhqAHg5p6V2YVlywon4UD0U3LvvoUePCU6yt5czOgpAiEAqpLKTwK%2FUGVLWkAeN0m3ZF6sPaTqJHmENKzCzz2Rt%2FwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBHci1mZ3A2ipdxvNSrcAyDykGGTogt9U1CKETjMX3bHroefxMSE9j2mZ%2Bky3PVKdqAskAQ2M8Oa3k8GUfIZE3rkHKZ13wwfYGDXuD1M5JBbhvf%2B5kFm0d5%2BODNqxEDXEyGmo0T32zdJgJ797IbshayIUlaWAk8%2BBhqaymin9FaBS3g3DEMQL18%2FdYGBgzSZGYOaUNcOheWyxPfczREMxubS1vPirKuNT%2FsNgEgAmSsdYb1%2BZh2%2F5o8hOFFdGYTGgNyzHCfnDU4PXM%2BlNBqdLSv5eL48voU4nLIJzhcIRkJWMX1kQohmUBy19YNLGvvCXK3RJXjG%2BwnBdpLEH%2FBqopzEoVvNzvqvoo%2FV7t2LaMluLAmaqgGHHUd6PAWVQycI1cxeLjDbE0SkdZZIB%2FbBLyVM9Ss82BOCPx4vvynsjdtqtHpBRNf3seiuNYuPl80TSX6ZadH2UPzScnlJBO9bc5ntsGkusgTXogrF%2FoKajc2gGK7AaVCz9tY2GPZVkJidMWC%2FbRaI4hTsg%2BQ9SJwJ9MVY3jIoZxhif8UnYqnHjL4MHqVAvccjGz3ionFypEnmQC2QYwyT4mXA0qyJnI6v4d3JqXsGMcD%2FnUpF3sS8iJ5cXSbZbxvniL43w7YHGC%2B%2FjQ%2BqOhQ9sx9Fbf6VMOC2u88GOqUB3YBokhaTpImoE7s1D%2BPzg0Xzx0QK8C7zzTluUx6pfFIklEjiCJU4GfRIxaKI67NofYtByPhj4uPxv%2B2U%2FZY%2FmFpu%2BoDwntFvUERRwYIxDUcoPZyOKgdGdfxRovINQnQf2YSGIAapbxNZhsfLob3cOAG1rEm55svijV3derd48rLb8QyTu4ha%2FK1LI23DQq4pFcmRdVk03Ekv%2BP7z9vIQdfrYVrdJ&X-Amz-Signature=0ebae3186169ee5333655b51041cfbd2ee300c81e86b9d9e00e23a88fefad353&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KQDMTPW%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHHhqAHg5p6V2YVlywon4UD0U3LvvoUePCU6yt5czOgpAiEAqpLKTwK%2FUGVLWkAeN0m3ZF6sPaTqJHmENKzCzz2Rt%2FwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBHci1mZ3A2ipdxvNSrcAyDykGGTogt9U1CKETjMX3bHroefxMSE9j2mZ%2Bky3PVKdqAskAQ2M8Oa3k8GUfIZE3rkHKZ13wwfYGDXuD1M5JBbhvf%2B5kFm0d5%2BODNqxEDXEyGmo0T32zdJgJ797IbshayIUlaWAk8%2BBhqaymin9FaBS3g3DEMQL18%2FdYGBgzSZGYOaUNcOheWyxPfczREMxubS1vPirKuNT%2FsNgEgAmSsdYb1%2BZh2%2F5o8hOFFdGYTGgNyzHCfnDU4PXM%2BlNBqdLSv5eL48voU4nLIJzhcIRkJWMX1kQohmUBy19YNLGvvCXK3RJXjG%2BwnBdpLEH%2FBqopzEoVvNzvqvoo%2FV7t2LaMluLAmaqgGHHUd6PAWVQycI1cxeLjDbE0SkdZZIB%2FbBLyVM9Ss82BOCPx4vvynsjdtqtHpBRNf3seiuNYuPl80TSX6ZadH2UPzScnlJBO9bc5ntsGkusgTXogrF%2FoKajc2gGK7AaVCz9tY2GPZVkJidMWC%2FbRaI4hTsg%2BQ9SJwJ9MVY3jIoZxhif8UnYqnHjL4MHqVAvccjGz3ionFypEnmQC2QYwyT4mXA0qyJnI6v4d3JqXsGMcD%2FnUpF3sS8iJ5cXSbZbxvniL43w7YHGC%2B%2FjQ%2BqOhQ9sx9Fbf6VMOC2u88GOqUB3YBokhaTpImoE7s1D%2BPzg0Xzx0QK8C7zzTluUx6pfFIklEjiCJU4GfRIxaKI67NofYtByPhj4uPxv%2B2U%2FZY%2FmFpu%2BoDwntFvUERRwYIxDUcoPZyOKgdGdfxRovINQnQf2YSGIAapbxNZhsfLob3cOAG1rEm55svijV3derd48rLb8QyTu4ha%2FK1LI23DQq4pFcmRdVk03Ekv%2BP7z9vIQdfrYVrdJ&X-Amz-Signature=53565135e2f4160e22b5a7a2de880ae34db02995810dbea9b94a0fcde3a4340b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

