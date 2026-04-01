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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2J4K4YX%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFdjQjqB%2F8IZBx8wpA1BKJBGk96Hf8x3pVfiaQwZpAZ3AiAYQz%2FRqN2kAH6LsqxAwUjO%2F8XxgdM4KU%2B36zZBJ8fR%2Bir%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIMT50KZxXOzfTWkG8xKtwD7dcubn9Fe65XcgwLGkFGPc6r8lKGJxuYl6Fjo6YPjYfgREf3a0uK%2Bot%2B3hOPwsFWWxnFEekP%2B9b6oMjw0JhBgsVa87mIkiTtPbF0XR654VR%2Ff1b5AafD%2B%2BPZ%2Ff8pri4UrrwTY3NIeH8pYzusxPoGmj4ZmvvFzc3VXti3%2Bteo6Mg2ZH81jphLC3EBpFgjre1KP66SuXihBsglM7%2BXfOYjoo8wiql4Gc9NxDnRd3fDOfJshv5NP1aFDx8SLTiG%2FJwfJbw7D6nUxwgidO%2FntkLjmmWBub3un%2BEb5dSXEwUnHz8wnCwhnJTrrDSY9jMYQXkrMFZ4lqv7HXmWWG%2FlEkiee0lDYATcXGFxvhiTNHnk%2FZR0LshfXRDTUpjTHKcxoDzlRlq%2FsvtKod7pwSWICmHXRnXrlmPz2LNyBdTGu1eCSea%2BNJTfsK4uHwxjFMl1Ox8%2F660DMxhKtuEbts5booR85v1S1hlsort8opNF843sFr6UqOBOMMeqIWVEUEkTRYmLjsMAsyAxZ6UdkOq4rpMo%2BjxjUpeMrp%2FvGxbP2KuiaQWGJr1SLRXNFDDPHJW285ISHWP83uCY8sSz6OmpPc4tXp753iz62Dqt6E8QpgpsZypQ81h9jrUK90lDi9gwr6GyzgY6pgFrOwMH8OIVNwFZ9VSoHbGTcMRhIQejcBafT7yuzFB6Cy0NKgbip71TsSRH0AHDdPiBDYs5l%2FS8iTSe5LcAVzOJ%2FKFDS8BNIV%2B%2B8N6AxW0nkdzpecZ5gV7qaY%2B45zx5v%2FYccMZ92ldvkiy4Q3vzi6dr2iIV8zcss2X%2Brb0tdKRMD4gz0Q44fn51pq0S%2FRR7SbxNNU2aA8VlxzpRY%2FkrC6%2BU9tOYRMWN&X-Amz-Signature=7e4905be8744f6a33b1d5996653bb969e9b6d16ff8bfbc02ec0ffbbf50444791&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

