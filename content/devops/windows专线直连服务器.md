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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BPCCJOA%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD9iUHzwOhNQ8wa%2BhVJnQK1lESsUOETjyklf1%2BmdRL15AIhAPYZ%2F%2FVcQ34DNK8E339mWpBgh73CqitVABHE3HHByEJkKv8DCGQQABoMNjM3NDIzMTgzODA1IgxZ3YFo5QX%2BVzPv%2BDAq3AOlTJ7wS47PFoxPnVvGDmSmAVgOtmzBMz3kvwAVgVcM6MOwBqd6QOe7MHg63mo%2BV6lASc%2FXhtiDM64ausl%2BY3IowpPercsYwsMQ4TAJKF21pS5sY1FHlW4%2FLxGPymJOlp4JnxLozlRFSIhf6XL9IgZl%2B4Dtf0iiaTL%2FsjXzDM2v237rj4f49a%2BfCNgMBX8wcKdc3kKZNPMzXjqUBDyWmjv27Q5n96NwL3q0850YeqXa0TZSlSBXMhJ2ypQM%2FLcGHvcgi9KeYumlyocvtjFJoWsBfqQkdVUifaWcS1%2FrEMpNKkoV2rqUctd%2F3N2igxqCIxEJxwklT2TZqXyXqB1D95DE8zmJcrMK%2BsHWEG6GOHvhyprtuyFgShMCnU2dU3w%2FOwiCflx3JuZvx%2FoEiJFxzzUjC%2FLfKbBaYEQkncmof9ikY%2Bw5PV3S4dvReWu%2B83bAJSQLm2xPxTUI8Z33LYGWpOCkl1pu%2FRG25hPhoQB7vb3cdERJQOqOvPhBi7yDXF9Dwb7rhsQSUrWdbmuzEeE06pDMNpKz%2FrxA8O%2BSKyBk5rIh7YoxwM1nLlybOWJSA6PySd%2B%2B3pL4Gf6nHJLubqQhNmP0bQTw%2BjdZ6jJmi9ipnc4T6E4uIBXZ2eB1mQhtRTD3rbfOBjqkAXefW9DB2CELDFaSzGutQEZn77P5ALg8ZZ3LhdCupvxE3ISty73z7i06Ce3Rrkg%2BGM8NwqHxSaVYLMfoyJYB1cUFnhZkMgBrQBDtlXlNxDa1uTWMWia4ykXgS0ZhasRveI4J%2F4JCtGMSFxH3QZcpdOouUQWqxVkLHqil03PucUamRo3Lxr86YRA2XgUgrK4RWQaHFKHggK3rS55eo5XTE6TB%2Fxvf&X-Amz-Signature=f4c05e9baf62afaf987d17cf25f1871412194a0defc8a747c063bd7c26cc7e98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

