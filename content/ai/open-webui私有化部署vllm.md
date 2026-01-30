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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6MAKO4U%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3ohvozBrnBMj3PbX0H0jg5UfIuqlaTqWH%2FL%2BJ4zaWZQIhANlPf77oE%2F0L%2F9h2XEuzD56q5GQIdsc2bFEDr3j1GEKXKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzK%2FQCUBgRHyA9i%2FNYq3AN0YjjugkPGkefRHW5O8zxp3uLsC0edEmuZv0pIcZyKU7QdGd9h89DmIxR7UYU6Zek2TeiOOFz6cS%2F7zGeVScmpfjXi4%2BryvQSmVNHzc79M5p8552xRevKJJvcm%2FbE9jpizOLMIdy4Wa7tFXsSBFYtLtWCcucPZUQEMw4KmGYfjL0%2BRv3WebPwAsNbpePFqhkpzF09AA4gcomoZn2jn90egbl55sTpV0CR8DVyyCA5XrSN755CBviebEFqHtNt36D51Jjd%2FO4E760j8xcu93TxiZ%2FAuaEBK%2BL%2BNjzHBtw4%2F9jLiiG8xE5zQK04mCa0UwJo7pCrP4Di6qHSnEYm2nrK7f5UZzwFo7uFtOMmlCVFyJ2CDboSASzktIw1seBXliyqoGNIP%2FIPs7uU7XYF%2FVMpD%2FpQ%2Fm4EFMJuC4iay3u5iSLoFdNr39eHFhp9rRBpC2nSeUMnsSEQoRlnqJsYzhWluXpxEShOi498qaTKVczVP2rjEEiaHiAcTG6YQljkoDPedUyVXCM4tUJvVQRuRLDDLn31vKZntO8pIhGPXMjNv4EItC9cTOeU%2BYGXMyw9gEFqANzL47XPZZDnNLVG3nAy6%2F0oa%2FbkwO2gsaq25EdLwRDAg7DtpJ48EmktqfjD3yPDLBjqkAXfJZTih5p2zhMhcxsTPGGDsW%2Fa3mwj1HEwB9tXEr9Dodvyr%2BybdBKxTQq%2BoQJgh%2FIMayZ2%2F2oIlZCYd0vknDjU0zwyAkc8zp3slnbzexoHGOYEYX43XqTuiLaqQfcplSzJJhIBpE2oOvoKACvhXvn9e8XaLL6%2F%2B1DXqV2RZy8YQ%2BBAVMk1TNlrDaznmCgmZbX938v6GHdrMNmHC6OW5xRVDnaDj&X-Amz-Signature=174019d724e42c9ba7bfde1fc34282230e245358fc6e62c6f8bb3e156b11bd20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



