---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IYS6PN7%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIAXiLzrRtNipCQPLuCi0rNHVcrN89W2U%2FzXNu35VQNjaAiEAivgkXKV3uH7m%2FpuKbiNHYcss05SOiDlOAsaW5egCY84q%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDEI70mcvxVPEwbpzpCrcA20%2Fk%2FLLGp36k1ohiX%2B7vfGyEgoK89xQj7KHNOkDoHtMsUBTY8ZcplcIB%2Fo7eN8MV9gcb5ZsB0WE0YfiXie4IzqcYInb5fKc7MMcJWPGB4hU3qYb5r8knnPgMw%2FoMxC2f%2B2nqgXzdwYtVRXhHKUAtKcu0E72SlZX5L3YoPPBZnvorLgwdaB8EcaCjSFTfK5FdWAJF5YIYF0Vht2LFVMWHwv48Ole2%2BAhL5gTmsbaHhhY65WKcK8f%2BZtqv292syQgjMpuZb9a0b%2FaTAyHKXwMYMB5fokL%2FJKWmVRvDD7e1FmpUAEJAvKCRXDL4K8ZcVBjfB7CX4kbw9tl9iKBdOK1pHsHnYgVgeaa4HfGd8kt8e61LU%2BdYsFTn7zyOyDVGJ8Ih4MaBvuQ9F0ErJQOOKs2DcsdfknHN9XAep3CdMn7ekqlwXwQMtbDMTkegRzWvgQmVSAIHOLrOgS%2BsxLcZK7NAmNrTswyBfgj0qsmFRPtg0icoWky87bUa9HBgvrytOvBiUy9%2BgNtNgkdA4K9xGUG2JeShqzb69Te691pdNVax9VXaXH0Q6VAzjN1pnc6%2FCHLvRvKC4xP1PS%2FVQDe3dneIhM7c0yzQlJLw8%2FuObwLnxQuWGAxo5GwUJfKhmp%2FML%2FG7c0GOqUB5F0en%2F321DwLR6bnBCFrpRrx8%2By7jTzmV6yjXfLnjq5pzOGO82%2BM45HYZo9g8UPFmk%2FMOcM8qHjEYNv%2FGxlz4Byjzf6pqNcGD8bXQjo%2FKJgovaDpSgTfDC6l7z%2BzzGjCEhpoFFJilZ6AmHrlo%2FDJEQ%2FUxp8pGca25XinoeKa1k5ThqXOKl02LrPs%2F%2BS%2F1kGSUIQzSJ6dlfrmsC6ATd8xaKs1L6Os&X-Amz-Signature=fdb40ba024a08189beb19ccc341aa6ece50951514229d60fd98a577a95ad4b2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

