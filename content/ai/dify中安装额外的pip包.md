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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNLTFKLJ%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAF1DagWSGAk4rPYY9FGPVydtB7DhI1CxV5Lm4ZbkLDcAiA3MkviYxNlJf4%2F6oTghfAOhM%2FOM9yrL9%2FTAE4QP7kaQyqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvz%2FiQnQ1%2B50hTBT%2BKtwDGUuiW1dxfLvgS83xRdo306bn4HGujS94uHbEkU7gYhO6xd1G%2BL7urJS5p2WmqyODTHgHR8OTZoeMkBddqzmDlPpaEUeWQ6TPYCjxZev2nTRoVuVPo4STiVlrCdGzjh4hzRg336If6sXJNCXzgHMs1gQwwwMXjGT3hkVl4yg%2Bch6xnC%2BXZ%2F4jShNHhSFPFsPs3jEd%2BHuynvLkZgRMJKAR%2FkpE7pZrfZqxjk52pa9Ebbnm61Yu9xlZPMHVwXA8mreNgpR%2BXAbNbZyPXPi3cuCggUoEHhJkW1TmGIzdQEX3FmIR2O3J50B%2BSwhyQGDacPjFcet2P0WAtaFomtB8cW9mL2vmCFDQBm0HW5YymLvd8pznjsuUQ5Aa5Jm2SNJOdRpALLbBb%2B7JBPbH4xtoTR7asb2Nk0E8TEdD1HeRRPmsX0sdjj4tBDgltbFyO9QnlTQuUoVLwyxj9kg%2F6eLU1Dm4bzDVJfln3Qn%2FMAL7RM6fYIfm8pORtyDavg87xIwgA%2B2EWEsNz4NImzoB02uvg4GG63Rjc1ISYXD6auz3HvveKTpvKYmmQ6zqzbxMvV52BN%2BM%2BCzC7%2FgXVZCZo0bElH9XDxJ5XImKw1hiX5mDzJBjkzHq9SUkfLzRSaRuYUgwvNXMygY6pgH5HkhJREDPrnNhdCeaSVxLkU9oRFFW5MfxeDg5DYmuFnCmZ4gBFmNAwmqXwl%2Bc8RdD4YGpE%2B2jk4Egr9AaT1zB86u7s%2B0%2F0lNipUpFPwf5iQwwYIfgbnjC5IlOUcemeXG0p9RtLsmvFG3rEuwJBn2c%2B5FbSvrWZkmbu1zbVgMysW2BLLMVCFn6VmqNOYgQdB7CzK48j6xbSACpiVe2UoJxDWu4DwX0&X-Amz-Signature=c8d148c4cce688bd29479778bcc6db2b499af52da6a4c39c5cad9961455dcd36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

