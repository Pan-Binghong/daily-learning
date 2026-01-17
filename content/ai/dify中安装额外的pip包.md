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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FSUETNL%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQktEGmzq73dxXfqZVfEiEp2jo1qr2VZlX3EwvYeyESgIhAIxp9FmTgHcDwzkmV97bz2eGByYVvAM4AaJprrXoqVZIKv8DCFsQABoMNjM3NDIzMTgzODA1IgzOQOFX69m4r72RfWoq3AMYSo4YCkcubb1KVijopJYfUgRAhZfik8%2FNZUqCdgJrgaq2eJ%2Fjc8kD%2BKvkH%2FwRsKL0AMpZWJjVHfwVFxk0V6daDBoGnLT4S6tx1gQWZR3cvdG8isJwsax3CWvVU4yI3RKf54IJra2v8lmi%2BjkzYMbd79QEiP2ZHEEZAvRVGF1JRzTTbYOMXXgyMG4b3ThqmFKxpW6sSO2A%2BnQtk3kuTFuY1Ecs19%2F72IvU9CGh8zGkW5NT97VZFq2F6hNR9Wc37v7upbeu%2F1%2BQYIdfYvUw0FVcbCHCl5yxxvJDGqlCH%2BbGB%2B3S24S3dVeB2Rk1dsgdQNzqK98pE6G8dALaERjI%2BoT%2B5Q1RNcQK6hrUO5p7JdtiqNLoBw%2BvO9BWHhuw4iAq6bQ5zqmujR9YiiK1rY5vt64axdeUlUA8%2BAT%2BIIUHl8pnkfqy2SpifJdTztLQSR7Yju9Cuo1kIriPB7%2BJF3U88CA6b3o10aIZy2uV19a8o51Ez%2FCihO6wLUojQVci4bVaz5S6d9F0t3LRkda3aBYpCw6qvj5ohfzd2aKF2TNTE8KTU%2Bh1feZ8JOmRFEYFBcpppLlhClEBZbpz6KTNsUm7rUlixUR98tp1HlHsSCmd7TMLgroyh2uSXizBSynBBjCa0qvLBjqkAfhS2XtMVgyeoYl1MLrQQYANkmi%2FLU0enGsQnrF%2BiPr3DBaX3RKxss5XPOFQyJeBRFezM5UA6vWCdKCQJtx7Hpyn%2F9Idb6ba2V9eljxn80KBE5ISLa8cGP92vJTwq2eVChn%2B1ovf15aN7y6rpe6jDGRFbRt7gs0CVbmkQVu6npKx32CS5cFpdwlh24pp2iPreskzUDdd%2F%2BB7ck2MBTEXkyzCWwIq&X-Amz-Signature=af73918d8c86ff02b3444e3943fdfc847cae95d891616df763c867c51b7c13e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

