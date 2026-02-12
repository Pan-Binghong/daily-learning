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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGL6T4VY%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCICQxABEZzrEUPtkpMCdoZkQojl11rsRK%2FmB5PR0W6jq8AiEA9EueCgOSDbh%2BeAySWdeSq4yderFP0GzyDSyNMLGia6AqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNOpt2umIAoYv1Dg9CrcAypR7BTuqLDpL4doB5uJhlNp3ayyRIoFPG%2BMASRPPmHGv6cmbZoOvC3Uaptww8KGcs6firpP%2Bz8cMfvf6efEjvHtyVvK8zR5CqmxiXj3PB9cVKjvODhWsfF1mLoL14wWkCtADbKoz0WG8nozFVnC51%2FIDrjEVBDB7yUv1ZHf0RFIIZxDZF2F1b%2BVszMnzA0oXM7%2BwDtI1bOAuIrwiHRQSW4jp4Whn6ImG2MXU7O%2FoQWngPj4PbhCWd5HlrUl2mmLMUSgNY7%2FMXhv5A7SXKfTDzS1%2FUP0t4%2Fm6mCBcA0aJWvpDbFw583KTZc4prYSvqVn7LJpwuoMBFttnx50xjSpl9iakeON0MnAJPn2AdEU4q6OpCBsC6zu0wCOmy%2FegyRCeDUtWA3%2FNOWITObtKqdfD%2FTg%2FPrTwMBnszCNvGE3z79dWI9tUYWpjWP%2Fgau8oVBU4wBsAPqUAy8CvwSVWRf%2B3eayZx141zPq2mZ6Y1gWozKwjMWDWBKtnMtXsSdy4vLP7Swa5OXQ2UNfDH%2F5ie9ylDCLVxs2o6yYE%2FaUqr%2Bv4lnHnWfkqZg8C%2Bu1ygQXVd8oemse4UeFZsWHzrbWQVVJ6uPlg4NWIo8OHQMz4A%2FKdG7UfIPOc1Y1ccZRGqvgMO6RtcwGOqUB1zBmJvAOqxW8z6sCJOLtehkjzlg0vAPYQ2Ws%2FuOoAr4w7UBkq%2BvUdaiMnsgMIOQMBk5Zx8tLiUyoOPbvVa2jY3G%2BoVDTeSzD%2BX7itZEjmcF1wkRCGavZqqepyfFvpILGauFGtJSPpb1K9cpypigMruZrKVVyJQRknTxhfyicXy8qOksYZywPLChxMuy08jiltThkpur%2F%2FI2B02kR0u5OmZxld%2Fn0&X-Amz-Signature=28bede37a93a6ceaa75278bfd60b7c6e1e4a13f4ff30dcbd9d7e08491582cb59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

