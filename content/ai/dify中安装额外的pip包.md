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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROIVS23W%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD1G%2BKSUGXTzy%2FcxupsS%2Fs4plqXNnAfMmbKfD5VMUh2jQIhALoy9Ht5W8DIvw8pPWipM%2Blae5NcqzU3J9Iyh8lhqGVZKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4XN%2BmIo38kpzArUkq3AMyPTRu9EocFsK34m5KuAkeXIabPLyiARYxguBwv1T9n1pBqWt9uZvQ%2FiEg7mGJkL2PhG2htOoe%2BLcjSeDQX8BV2Sr5mGt1HJr54AywwLnfSRQfnCyx%2BK%2B6P64%2BNeVZ%2BRAKWLmv2Ook2%2B3GaLHhhMRwyK5RDtUyYiFimWgDNCzbh3se%2BUzwM71NKVhVO64oSGqaSfSKp%2BjqHjXCviMr1XA1kRLHeIR2eOU5GjfjPwWiSOiZK13DnQdqQ94mWGOTriutHhp4HRQYNMcI%2Bdb%2B6O9KfhTl%2BSv9R0VVfT%2BpVkmUH%2FmxKGwJykI1KP0acxxIRVEpuDLJJIXy7k9CMlmZd9Vd53RDOi3E%2FdvcwuP73Xc%2F5YkaDDWmAT2mX%2BxUqfQcmqd09Bxvo88K%2BghxkcCejw%2BDCNfn0FhwgCUXYPi%2B4uvyVtu%2BIHw4kq%2F0uzKQM2KbcCEtqCKwkZ2Cn13aZJUkjXERN7lvOadJwK5PqFCo1Y2S4OwnJpDRa5OeBKR9bmDd%2FFO96m4dEkSNII6qhR7g%2FLDVmlaya3XXys0w70sJflhh9isqe8uBNyu9aYsC6NC5kf1nrIWY7PoMSFegQtxq%2FC4l%2BDsSl8Z6s3eJ5WFD238OLs7YAhPHE%2FitsE5ZyjDhncfOBjqkAbqJtIv29GCOdic2XGTll87LjPXUa17vvrNdf8eWVDxjtoZZox09Orb6uqzQwfXe1rz3jcVIjDtjLaSdNx7A88CO8rSHEkzE93IM2FrXbl%2FHGVGlWxkyi0kJP8vjPMqN6lHo%2B29UMM%2FpQWy7xRVJAmDQWv%2FKcB5u7QCSVURoLDMk2DxAlVzy3SBkDIM7ZCqgmVFmbGXKa2w5dR2tMzugPW16cOWv&X-Amz-Signature=2f00c544e28f1edb3db017cd2145f06b08250df5ea187a5b081b5e81b22a0090&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

