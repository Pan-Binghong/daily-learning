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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPGAYJVW%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIDDWMgx%2FsVswY2KOSrE0cIAmQSucX3Uk7fAJv3Q1oqLVAiEAkdO5u%2BLmDxS7q1th%2F4dF7oaRBh09i5ulNCnJuSM7Lrkq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDKq92odCYwiXZSPGESrcA0D3ogYvAn8f7KuXtgiX55PxOZ7ckxnGwqLhaz18o2qkhcFfegA6UeowrvmddTPPWdD19rS4d7upa%2FsgaNbukvyYoMpwQXb3c3qIWC5pZU53DvVJ4rO6SKXVMW3vvpiHOrUcNNIcrNY36F9m1nV4SPEBb7WIjT9qsepiGmIoI1a6CMfovZJU3T04qwZuWJRYShJVwjqp79UEnVLfYmgDXHwfOFcevBzfQfEICIGq2346rFJjF%2BnpaN5yX7t4Hi3UESc6iLTwMQpBeB2c%2Bw7vDUYHuA9JGAoDKOVSGk3EIimoWfGjARsCXnoPROEWCJrtcAT%2Fxev3Ce51q4kXnM6Ch%2FNsB8Q93NrkhhAPPLw%2BiAZvH5O7AkA5xcR48AGu%2BAYd1uxlfFEJ9YUvI343glpHxounL5aUTwIPEu9JpSwfOwfOGuGE1z79Kwf4vfzs7rRK11E50sS7Tt6SXMcr0QSpGPolHRPGG%2BafP%2FoHQEr789wkNijaW3y2mo5nzeVSbBmTY%2Fiitff0GDVKTBQ%2FQ2WUmdQDFYcrJ%2B8w4FuABNMNsFhXcYBvRQ04a8AK6ahj%2BXQck91z6K%2Bb5onYpOwyKUgrcm5eigWo9eorRhJkvKcQel8CnY0h28%2FVfVPqcmXjMMaSkMwGOqUBtjjYKSk1O3UlR7IG%2BWFyxsv8Q8nzTjoa7LdITCp%2B%2FzFatIZgsGgW8lCL2RgSPcBLGFUdpmJyrYgC4w1TYCn7m6F55H%2F1cXcR95VID1Ddmz7S1%2B33ohnv%2Fdlr4NO6IGetC3Vok8rfwntKvKStkb%2BdoXBnRTdX%2BN7rmf%2BeH7VpuhD1day6x6AZe%2FpuGYw2zLPRUY2X0o1WPPmFbI1b9yiBKh0qEjNv&X-Amz-Signature=8d7783f6954453e1aeaa074fcce451b53672029fe04af1888bfec0e444309881&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

