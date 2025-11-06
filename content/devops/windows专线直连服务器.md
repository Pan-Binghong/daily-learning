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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UALXMPJ2%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaowFkyK71WSjFdStN3M7UWL3EfKdPr29P00IvnBl33AIgOktfxw0mfEDhlBKr9GBlcwIulqoa1EEKHYHRsteuG8oqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNFEzRABC2HzvuXkHSrcA%2F2s1hbPXPJG53FCC7X%2FkvdURlARKuIHMSeMmF4qBL%2FpI0rcClCo6Fg0y%2BhTPzidj9QXQKDRpKBiXry6%2BmZfid2VhJdGY9RERgEjp0V%2FeUaw38UAu00u%2FWRIs7bHznZo2OATRMrdCRReGNppGyqDvYusZiprymiLfILcg2t3K3NcHu20T7%2Fp4V2gxtG6rp7Wr8L4mpYgAUKIK6xCOp7W4hUBnnwnplrjwhJUz9QX9hD2ic9thbCs1hvgILoZUT1DsHFCLY%2FM2I9AaICIN4nkwZGsdqVZ3rU4aLI5Am%2Bz6pquQ0MAXs7ZJQVjn9Ezg4qyhpaczk3vj4jjDsXrunv%2F4W8vP99kegUMP7aZ8EwpmHixd9Qf8EpttYMLnISlcpUZvKsWT084xe0DMYyrwER81GKOOd%2Be8siL2cHgrfpewfNALOLW2RZibBxr0J%2FSfryRfgTDFl5kvXkDneKRvwFvY7RHlN9iBvGl7xpFxAtTVI6JeO2ge%2BQxI9FX%2BgEbWD80uH0PG6gT%2F%2FEx3NYYPiPPiYekCE56mG%2B7E9BGkXdySnEFk46MhANN9SRjqTgLo7cntmOaDtUYjSl5wZoTbJJDOeKO7ZsV3dBxcCZ6xv3FrRdqHoFrb2IUtBc3nawNMMvwr8gGOqUBSIO%2Fx2rxeifJmCYJB1YhhO%2BIE5IU1wKvtkVFiavdLEq73Ln4iB8mfw9yj1gnPS7t8AXvyMYA5qHGOFAKQZio39q5OefJFbG0q0LfrDQq7j5ynLIvzW7%2FlLVgQDjh8Hoo0JI4c8tn%2BAPWdiVliG58bZvt9Sl0K%2BRp3iOZrvPTWEefl8TRD5P9W316b7fOBD%2Bd9AeSgG5QeeZL5DKBV44Qn%2BDBto62&X-Amz-Signature=4ece958ca97dc164f0882c0a024b78c9b592bebc305bad2dadf554d1fa42ec81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

