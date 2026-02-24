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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWMSTFDW%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIGX85MUnKwboqckCI%2FbisJEOLcAsGZWrUoyDYi2%2F0%2BVVAiAwH%2FoOM6CQx6SXhHd1ORYnHGuHWrf0m%2B7sHwwLuHmI%2BCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzt64UhbS7fQL4VK5KtwDTGgoLRZ4xeTtULTtTMYa06UawE6DH5vQzEGgb%2BOxdnrG1W1F3aEe5stOglSL%2BOM8HYAX4yK3%2BhfDsI%2F8jficmVuo9JxYvBp%2BMYfMSNlkgohMQMvvzrLJYQDaLS7ZwmzPFVX508VlG6%2BbHADm5JUX9EBT6SRJIZMZmzCDmF9VBGPjkcgqiR7IvWyiFYLJojhwDwjE9kWSO2anwOmUWT5TCEhTNu3Ol3DnJ%2B5ZFgh%2FgHZ%2BtvMfAXGR6UclX8xpRwAYqV3J21g3xkvf9Tq%2BhMv5mXvlidJkX27Eq%2F6rWeWyryz557wd1TIyWvlImIHkXeN7Igj1kCfBi8wgq9SCjviz12Un5yv1BarIBs%2FOATucigKy5%2BRQo45BR%2BYPh9kRrEs13kCWB%2BTIijxMlKfwWSBF5%2BhQSjBYUKfF461MAx%2F73a%2BXfDoqn7ifYQ%2F0ZsxEEG8z%2FE1sZgzjiIyjrd50ok3w77Nb1MSuV5Cz1xdMwCqtsXa4hGVVfJ%2BY2qJ8B7QdpAilunluZLA0VR9WSJ3BEySp0qE9qLJyfmWD3%2B5y8efAByKLcOA8oPtQWThbAwNTN9mrsfzcChUx6ZG56Mg%2Bg0J42JqHquhgkbGtgNIL0Pd7f%2F5cyUv%2Bhd8MYfUE6sAw4Lb0zAY6pgHjGgOtMiOTCcExR3bqV5EPnZUgnBApxEwUDW93MK6A3PaVaAE2WxPM3373ti%2BEfCNVKrvGZYyC3gyWl7gGN4VyRs7p2AKbhSWw943DMxU9CYcL3FnPWxEeQRMwgWXTedjjK6VvD9lNWo92rObIDOKHCGQqhMR8MxdlqCNJdv9DjXLFBPtrg4ZiYiUbUuL1340%2FSKuMMx0B09Ofv7MT6y7iCSOOiZUA&X-Amz-Signature=727018292289876545f47d31016dce9eb7ad115e0d5a4a260390bcdc46ab304b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

