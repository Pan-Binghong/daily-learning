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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EYSJRUP%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T030026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGL%2F8AkTxqBBX3%2BrE%2BvbbSI8qzg0rLpSsrIs79cqMzEoAiEAhULBSTvdmw4emCqBZOEJCLgRYI4Q1ZJsGfBYj7e9yIgq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDJscnv4QHqF6xHoNSircA2o0KayxmLcnzqr8fdWxqugsSsx3rtoPhL4tJ%2BPy0N1gKb%2Fy38t166UoYeWbOszszuBNiN5L86HAbTfC9YN18VAIHrwZ8hh1p47GggQVVhC%2FMZenh76MJSnoK3%2BNRs1buabhbwy9yIT62HRhwhaoeNlNi1Ttygsa2zDTPfaduO7dBXjzsl6s8Vpp3eNV%2BWVMdWAe9Ltw%2F%2FX9ox2ky70BpZ3qJvk8ZjfApQS0mk%2B9XWZFbSgWXEFCXJ5mWDUy3zucUsHtiJb%2BeBqP4tJJan3Wst%2FKQMdeUfxiLWFsxqOBvmqepld7yLrfDAVTG0GFKe3mZ7m3nxje9Zu0CLxKjhSRUo2jsit4GwiGdEAdZqHiJrweIG6Vph4Xsu8U%2BCeqHq69UUJw0uT6ivdINiDIaqDhzwoRyrrQqhET2z1c9wK45H9WtkyDJ%2FtshWN8k9wXpz8XiZsBY6WLSsHFX%2FYVhYBhNhyl5ZzZHwj5p2nnBBbJBH1ebH0b26PZH%2FLB%2F8j39qamG15Bvsq2RHjQqfb1utvQmbs5Gd37z0J5kGTewH%2FVJlVpjRIVWCmjiXA2AeZXMu5EErAtrbRMAEZIlEJBRnGCNLJGHnGZALAZEkdCwhSjLqepGHT0VZQU0V5osdB2MObl8coGOqUByIV2jCkkt%2FUmZmTgN1DsgLGXfki6z6aAe8faL4xICli%2BkIuL0Bje%2BnE67XBNisWNvyIaW04AdbOA6NX8TG2S9RAfYdu6M1H2rKu%2FadaOhUjJGe5vVTFSX9OYr2HmvIfKz0Wm4joWuYE7Ze1W8D%2Fld9G8eUj9ACdWa3n88RQzuC8qfyXy8fCetWFuY5MXdyLgvyANuTg07NHicLa7YN%2F7UDc5IXd8&X-Amz-Signature=c5e3e8757b45a6bc27bc658792b75e8ca5a072cd0425c5bd723cf8513b5e1fc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

