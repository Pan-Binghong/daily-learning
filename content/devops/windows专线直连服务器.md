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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466327SY257%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCaKOjgwkT24NEzfdoPdOWqJbVHOmeeV29zBoCrywD1eAIgFfn2ZW3EB4LadkLy6iM738IaMAvowwvSoc88SPBVCXcqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEa1l9JxnqKYI%2F%2BQfyrcA3Ewth%2Fg4GTCnJm5tYPe3F1wjnid6k6dUaEPmg%2Fhz3gKUjg0s%2FQ6Cv%2FdZp%2FQxa6g2zIuptnAvGYs49Y%2FGwN%2BkGE35P7RDcGuuL%2BRKTzo%2BWhPEkOsbvG1WvA2DXd1S5eD0EittBG8oAhUKmAnTXenZihwr8VLRLyDd4oRBt3avxjLQj44dHKAOhus0IkpiGkldndc%2B99nivSG%2FWG9UfwT43g8oqrE0MJEjjnPCjzDaVmRWQwwePHcN5HX9YQAkqGg2ExoAvFDPl%2FJwafpIXvTQ%2B9o3QVWNU%2F8zlXZ1PAPMMDHcjJ%2Ffdo0gLu%2FE7QBMULXyh7YlgpiadGeyYhjsbRmnAjnoH8fz7ECAXXTbHu3nZZm8%2BDQELrRQ%2B1%2Fo0atSsfX%2Bpyg4RfDs0730kXsKg9bCNMmUYkgolv5op9EaLzM%2FHw0VChDjVErSrA9Sf7FVxw2cHzybG7%2FSbQc000MMcJgolPKY7Shs1dP2TBG671qS0tqw0zDsPUbRFqjfUtCGXom7cjk22RmKkMrGpXs2xIQc9q48FEJydMOanSGdOeFh7qCBytk27zsnr6VK6glP5MATjmSFYmSy29T3zDmPq6MYQMIFxf9rBkYcQL2fSLjkk34VfjuCVDfFQOoT%2FHxMKe%2F3c0GOqUBM8CpDNfQg7ov8R%2BqasJFirkAJ67Gg1NPNhcMRLULDX2hyGeR5R2%2FVIWPfw61ffILNmnDIdp5p9Ef9ohkEkC5qt%2B6%2FFvJhIr%2BEEcXuO2BicEObo6c6o2Mb%2BNYy2YrMco6xIvuYziBTCqW20blw%2BX04zR5q7wxwZwvJfd%2FMik9S%2Fsm7XnIZHihus6cnTyHbFdjibiELgA%2FDqlnooLqCEaOZnZJkDyb&X-Amz-Signature=72350567d92cc068136b786fe75a834df8bf02275774393370b67e132222fd8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

