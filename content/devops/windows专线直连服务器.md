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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QPC4WLI%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIDrLGN6v4Dq0QuEgWAsxjgBVWswI9epVcm%2FXQWvJfySSAiEA%2B218Joi7magAZ%2FMLx7QHYSt1iIBbI3FUYFvOymwSztMq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDLovZFDT44dTCHgfrircA5fwBUlyY%2FoMMP%2Bn6GnMgePR5qw2KVSCqTtZq87dQjCqwQh2AacYisotAY7FKJ5AJ%2BtmZeCyul2HhGvNKEnjRsncEdRLEVfUK1jUmcXvuIP%2BJPsnOEe8Qv%2F9JGCPQ6EaEzYTp4ruNZeWjhi15%2FNQFc%2Fl3bA%2FfEIxl%2FsHTSyMNCGM79UquhMl1YHiHE12%2B6BseIl1CfUtcX%2FIYtUKVYv%2B5F0sQp0mqDZXohxT%2BeuZyJaygalHPtmzdW4SX5lLo2iSrXIJIx9GOFR%2BgtWg67cIKakHQg8Ndc%2FeD82lraFruhi1p1Lvp3sO0PJo8uKnK9hau9w7WwgYVdADn%2Bd1XDD4LWX6QoHHDgLpEJco%2FF9CMxmiDwaUwGzC4wDkg1c4cZHiF2KovM2c410%2FJka2oApYpMWJmQGrnBTXlgZjJV5KDap0J05JQKdE7efXSrTrmkbz9FbXn6Ceg03VbUQB75%2FZcDJW1Djfeep67VCOdZZP%2FmyaBOS2PArxR%2F36NQGTVfKzNCF%2BKrL%2B%2BZgUZkVhPneDsIiCfteAFUzEPrV5Dyiw5sJr9YCnGqWxPAjs%2BFUOWhyMdQY%2FMSVFkkqImYb7XDNBds6tYDTAmvuTfjyXXLfe2pAldtb7RiWxyc54vsrBMPL34coGOqUByqq%2BksOrSerBkBaP2Ewyqe6tdHvQdxF3azyd0%2F8Y6u2ws0DR9pOHhOmeXi%2BWdopxp1TPNDauYWt%2BaYqTcZFuRHHzi1RhT6cZkbJydudQ1dStT1BoyMKE4PJJqwL%2BQ5hsDZcRNAAuZy5AvL%2Bjz0uw3xSLXTBv7IcCKMRzgALCgB3qEfft1lQNjpCIg3dQO28TYAsJBSQXvjzQV2hT5Z4DZT5V5wv%2F&X-Amz-Signature=99e17bf6c88fdd563422809691de0a65722210e275e4b6903a70839d49de35f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

