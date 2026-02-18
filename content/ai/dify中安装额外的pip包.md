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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX2AEEYX%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEBFHCG3moKomz6t8y7RuXDzB7VE%2Bzo0A2bL7qNDPJTYAiEA4zx9TTTxvy9C%2BvAKbLFeRGpArR5%2F6edrlozIoYkkkbUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOR9T2BdUxWaFc9rnSrcA%2Fei4XUemILM44sOr0%2B%2FIBbE1gNLFPWKEF%2F5fAi1rssROwTJIz9JrQ9SoRKm%2BIiWS0aM259s9MIhFkQO%2F4PR6vMEor%2BhanB1d57nxwZVWcmDobG6ctl5phIeH3kZCwDgYp%2Fg3X6FnRRJwfGHGelAZN3%2FyQi2XIuRw2ZiBQvJ8cZAO4UKB3iYGjEmAA%2Bmwg5Kyri9%2BlrwodvPIzMo7BB5BhW6j5qpy8cYNqkBHZtnJHO9MHT47yd75CX4fFBsuDOh1lnT65vV7p0wlA4X5X5G8Rxshts7j%2F8%2BZVDvKvA7cFSwCubAuio%2FURStEZlVg%2FKM8x8vqGHh7BVF9FT%2Bzf7xOQwEurYtnsvUJ5gOsQH3gKrGH6ZYuqlEzxfwzg4Ra%2FhaNne7dLM4oN8BM%2FGiF7ojl9Wc1Nk2Sh0pbqypAvEBrqoL71sSj1PZg3CeBQZiIOh0rfEc0H20%2FGCi%2Fowb%2FTnI6L49TlON7LZRTT4mQ7lM9AmUMSBDb9%2FsYPxBzG8CGVNJsEjpDBqJyWaNRPnUmGq2Ak8sL%2FvJRKbXjS%2B%2Fd0vtXQQbrqCIA4USCYMbSfaBQqEwa9nvLRdJlgoZY4%2FdaHNIFPSwzQ8phYNDqm9ayGtFwKJ1ZvRySC5u7MNE2dlJMPWf1MwGOqUBx5wVs%2F8%2FRJ522h2Tdrbi2rXF%2Blj0m1JZOAQ4yx0MIi3aL3GoadidG0V6cDQieU6UYFxXaYmmo6cZNFd5YXRqW9zinWC8Y%2FQl3GMSZUkbM5u1C0w9eVGXGAHTd%2FusjFNxbrVVRkDDLk7MYGwmGLG6xHWZedTwpfbAliGFm4YMN1Q3r5kf1V9W%2FZj0DuJBhutv6FKcAN%2FFbgGvMwxeHKMyguycEw7G&X-Amz-Signature=95e768c7b5ce32be417fded9878dd089a00c96de8e395b7b339d01cea3b279e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

