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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AOV3C3H%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIEEj3tNqcTVkhc7QlAaDV%2BjP%2BifhCqdbeVjBMFbvz9TSAiEA1qoYR%2Bfm1nN3gpBvU7yxeG6x2lc6Q6whhM%2BV0xwzZYAq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIezrm9z9b%2BpoHUmYSrcAwlko6dh1hQ7UjKbOMQJpFrBITUeO50QDGWPP0MajmW2jKBfm%2Fms16M%2BPn4UW40dckltZKQt2VVCzF95P%2BEsThoKIQnE%2FPqF1sUMs4KlRQ0IYMg2TH7%2ByGib37%2FRWfwxgfrys7%2Fple%2B6FLbeO5SFX39KUhmwDN349IscjhHfW7vG7MHifs7CF892yu3Jt5eZw49CsoAIxvgQBXoo3gS9A6aNBM%2FoWYgnjeREM51V%2Fc2Z0c99moL803Ipbs%2FcICKnx6zF7tXsKv3%2FDsc2fpEV93Rtj%2FLUQ5TRTmjX6R3t03PyC9VoHMbK9quAckfU4r0evJyzxhA2ffT7dfw0jv7SStRsTZATEOSnHzmmkvF78GCOTvAYlTqXijLhTz9KzQB7XGcqnz7we6QDDxVCIyrDmbWROU3MhQcivaQQv4z3Q8FePpnceU7XM%2BybawfmCDBdW8ucDFPf5LqqP44%2BCEcUpZ3xVr%2FNthJQswle8Lzl7Hiw0RyeqvChDiWZjLJvUHdE9BPtXy607B%2F3raBh1gr%2BPMYVXWT9IlnYdQMsc8EBqWRUSnPNCi0z8S5eAOe0%2F7g%2BkOeaMCjKN6jfCL4NDoeYsqvqtR7QDpVqlfc21NruAckxJhRNyQzbqBx%2BeOYSMOHTm88GOqUBulVjDip4rrVNBz%2FQK6dEHmQF7m5bVKTKFakIupVaJHcI5e7uhAJkSSZsVAzPVwCeqRPLlLDCKDdKreix2OdC4aBYJpnEAwB50EkpVxlJSYORy9tS%2F3BknzAP%2FXCGp%2Fz6lGMVEdiyHXKbZ5UDtnEwwDYDNJtXw76%2Fkk2l0CKAiJJE20YOXlDDYOQnaAC%2BGzrhO6VFvkENP6MNON2yu1%2Fuld5bPmkt&X-Amz-Signature=dbfd49cb11588ccb3289347c5a8f43bab265aee20f7189ada404de07e7b1af3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AOV3C3H%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIEEj3tNqcTVkhc7QlAaDV%2BjP%2BifhCqdbeVjBMFbvz9TSAiEA1qoYR%2Bfm1nN3gpBvU7yxeG6x2lc6Q6whhM%2BV0xwzZYAq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIezrm9z9b%2BpoHUmYSrcAwlko6dh1hQ7UjKbOMQJpFrBITUeO50QDGWPP0MajmW2jKBfm%2Fms16M%2BPn4UW40dckltZKQt2VVCzF95P%2BEsThoKIQnE%2FPqF1sUMs4KlRQ0IYMg2TH7%2ByGib37%2FRWfwxgfrys7%2Fple%2B6FLbeO5SFX39KUhmwDN349IscjhHfW7vG7MHifs7CF892yu3Jt5eZw49CsoAIxvgQBXoo3gS9A6aNBM%2FoWYgnjeREM51V%2Fc2Z0c99moL803Ipbs%2FcICKnx6zF7tXsKv3%2FDsc2fpEV93Rtj%2FLUQ5TRTmjX6R3t03PyC9VoHMbK9quAckfU4r0evJyzxhA2ffT7dfw0jv7SStRsTZATEOSnHzmmkvF78GCOTvAYlTqXijLhTz9KzQB7XGcqnz7we6QDDxVCIyrDmbWROU3MhQcivaQQv4z3Q8FePpnceU7XM%2BybawfmCDBdW8ucDFPf5LqqP44%2BCEcUpZ3xVr%2FNthJQswle8Lzl7Hiw0RyeqvChDiWZjLJvUHdE9BPtXy607B%2F3raBh1gr%2BPMYVXWT9IlnYdQMsc8EBqWRUSnPNCi0z8S5eAOe0%2F7g%2BkOeaMCjKN6jfCL4NDoeYsqvqtR7QDpVqlfc21NruAckxJhRNyQzbqBx%2BeOYSMOHTm88GOqUBulVjDip4rrVNBz%2FQK6dEHmQF7m5bVKTKFakIupVaJHcI5e7uhAJkSSZsVAzPVwCeqRPLlLDCKDdKreix2OdC4aBYJpnEAwB50EkpVxlJSYORy9tS%2F3BknzAP%2FXCGp%2Fz6lGMVEdiyHXKbZ5UDtnEwwDYDNJtXw76%2Fkk2l0CKAiJJE20YOXlDDYOQnaAC%2BGzrhO6VFvkENP6MNON2yu1%2Fuld5bPmkt&X-Amz-Signature=686af23e9b062d41790330410e21d9c629926832f26fad61211bf9ce71462066&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

