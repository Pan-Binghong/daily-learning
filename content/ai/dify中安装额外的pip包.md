---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMUO36NZ%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICLLCEQnV5tAGZQvWKx4Eu7tVWCTd7AyNI98jB1f%2BxcTAiA7IjHKvKYASRrzeEwmNpzKgqTpo4qAnqlVePsRFNVC%2BSr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMPp8zqQO6g81SQhGCKtwDUtnQgLT9izjeP2T9y6WdqOPKmY4YTo3MUeTrC%2BKisUUH6b2kEe6fXL5Tc2f9dsugXbeA9wO688mRejxbSgXLXliMKQi5gk3LbjAtrEsKgtbFudvds6WtDbYpdkFjcb6Vtz4Qzo%2FS0aD0FEUDnntmxeQPyAHS1mwnBzyAHmZmDAvu5zYazWd6UkkMleafXgR7fuzIHyBpGAN6JzbehM%2B3B9u7kG9bxqZsX5wOt51uL%2Fyukq7uhsxsbu1RPXX%2Bo%2BcvuDuJy%2BscfuKGErqUtODykp2y45ev7TdIgp6I6vErqmgeu9FZVeOTmL7nrNMKwQ1101a0sHV50gcNXbvXfoDY9iI0okJxL85i6pinb8397Pum4hWFXeBQcamhZQUtVvXO9FsOVBi7y%2Bgd0i41lrSBFqaR3WH41hyqOH%2BaOa%2F%2BdgV%2Fc3CIUR94h%2Byc%2BYdddpgwo56HyrIpcOKIOJQL36cHLk7WhgXHyhu19oS5d5cOovUa%2BMQaXK9WQx1MZZGCD7q58k1L%2F71SkjDw9YbRSdyY3o7v2Q3iZzUyMtqbtG2bh%2BfR7T%2F2m78QR9NGkP1cSyMh6PlQ5h%2FLmdnJWAFgtjQahdUQ9D%2FRDcZjcFWj3M0IIjACt8giV2wXnNVW%2Ftgwna2UyQY6pgGxJ24kqneWW66%2BUEQ2%2FpM%2FgyEVGObOYWozeh2pmc5vt%2Fm51GPQWxhY8xi%2BjOxyZ40VxQgitgiaPMJBZG%2FiftTx8qXn96wZ9BbleXTgZaGJzTtGW0hv9KNJ4iHzSNeqf481JqUkczZsA8MySjPR%2FE46pXFZh7l0ALim5lzQi%2Bp5TR6k9RZ39bhBvn5%2Fdy1RCzYLXLedtu0YA7inK3EO91VWIUsPzpJO&X-Amz-Signature=f36313ee2730fdd272c66b1ce53e365ee6b8bad6db8697e437fe6de835798941&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

