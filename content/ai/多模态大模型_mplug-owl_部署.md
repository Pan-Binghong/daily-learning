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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FHYQ2UZ%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLlPsmSpxeA87YtBasm3UHAsO8W6cuS7PuUuksEMX%2FgAiA5%2B%2F5WFYsxkhZTe9ssMa0M4Z8OYjsdBLJF8hXfp9k4Jyr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMZCaA6izG6tVMKSrhKtwDr7GGviS42v206B9GsuiOOJYCB48sWSkdz07XFrHv3VS06xo65TIkvhgcgRd3ePleOLixr2AJ6g%2Fh4vI%2FcpR3yuGjzHlh86aLDc1B3Yby5EfracpSNkH2UUBLwo2hOmPt81oNKf7R8Z106eGHOJ9zRIQ7nGsHDOldQKuhV%2FVaxhNXLACeb7iCjC9pt6CUlqdTEkfz7QdAiQIJPWETTlsVpFJAvX7RGOUFEADv%2BDAUZiBX7%2FA4wBq%2BfX%2B2RAT9Y3JriSg3o5gJG5gOkJhuwveTC7kptHr09T1b8OMT7ZO05hGEKTqbLCJrlAigshl3dHerY7TA63OyQY%2BdOXA9pHEi81PTPbcZF4exAjpsI%2Bw5FHw%2BPragFQAvXxkEciFWliMB6P2e2CGuVYXes5rX1Ekglw6xIZ1tMuZko9Zmjo5eGTgVsn24OdrkS5XAInB75eS22uLAm3DBePAzocIugQb6IGsQmHKW3XOvuzCTIwamWGQhB%2Fu68fW9TfyxpCFcnsaIy8fGprRCNAazutzR9zRtHuI8wrNlJqeLmmByksDbPw1D4rt%2BqecuV94gP8JJT9%2FzZUKsMLjjxIZWI155gDEw8h6rnaPu37MOJkYt8uftNwcwrqyrjqEp%2Bncw%2Fs4w46arzwY6pgHeS1Q1%2FmvoYWigbThTnUae73LRB8xXf%2BqasFEsK7W8iCQV9UVgelKM1kIrXi8lkyFUJs0sYN%2BOxuFy6Te6GqwkDgnVRfvKeJ8i3kXHxypKY72Z%2Bf2orT5UFRnXQ0jAFwWnJLOD1wxNqU78x9B%2F3bC%2F2Uc8y451mtSbnMdjBGwXM2njR9EjQpmwTmrJbrBI3xzCG0mjYom7X4uQr9QMHfq0Bf144HFm&X-Amz-Signature=a24aff8eda9f72549a5f3fdb7dcc0b73ed73eb8a2236eda7bd1ba414b40aa13c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FHYQ2UZ%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLlPsmSpxeA87YtBasm3UHAsO8W6cuS7PuUuksEMX%2FgAiA5%2B%2F5WFYsxkhZTe9ssMa0M4Z8OYjsdBLJF8hXfp9k4Jyr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMZCaA6izG6tVMKSrhKtwDr7GGviS42v206B9GsuiOOJYCB48sWSkdz07XFrHv3VS06xo65TIkvhgcgRd3ePleOLixr2AJ6g%2Fh4vI%2FcpR3yuGjzHlh86aLDc1B3Yby5EfracpSNkH2UUBLwo2hOmPt81oNKf7R8Z106eGHOJ9zRIQ7nGsHDOldQKuhV%2FVaxhNXLACeb7iCjC9pt6CUlqdTEkfz7QdAiQIJPWETTlsVpFJAvX7RGOUFEADv%2BDAUZiBX7%2FA4wBq%2BfX%2B2RAT9Y3JriSg3o5gJG5gOkJhuwveTC7kptHr09T1b8OMT7ZO05hGEKTqbLCJrlAigshl3dHerY7TA63OyQY%2BdOXA9pHEi81PTPbcZF4exAjpsI%2Bw5FHw%2BPragFQAvXxkEciFWliMB6P2e2CGuVYXes5rX1Ekglw6xIZ1tMuZko9Zmjo5eGTgVsn24OdrkS5XAInB75eS22uLAm3DBePAzocIugQb6IGsQmHKW3XOvuzCTIwamWGQhB%2Fu68fW9TfyxpCFcnsaIy8fGprRCNAazutzR9zRtHuI8wrNlJqeLmmByksDbPw1D4rt%2BqecuV94gP8JJT9%2FzZUKsMLjjxIZWI155gDEw8h6rnaPu37MOJkYt8uftNwcwrqyrjqEp%2Bncw%2Fs4w46arzwY6pgHeS1Q1%2FmvoYWigbThTnUae73LRB8xXf%2BqasFEsK7W8iCQV9UVgelKM1kIrXi8lkyFUJs0sYN%2BOxuFy6Te6GqwkDgnVRfvKeJ8i3kXHxypKY72Z%2Bf2orT5UFRnXQ0jAFwWnJLOD1wxNqU78x9B%2F3bC%2F2Uc8y451mtSbnMdjBGwXM2njR9EjQpmwTmrJbrBI3xzCG0mjYom7X4uQr9QMHfq0Bf144HFm&X-Amz-Signature=3dad9b947fc4187d35bf2ba9de09385851eb424a34ff12a3de2fb4f4cba04879&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

