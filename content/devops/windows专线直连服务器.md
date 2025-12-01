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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVKSVZ27%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCKbuy7uERm5UsGpXWdnSyayMBBzeol90LjJwBiLTGBXQIgHc4gHIAlaNUvrKSOepGpIGazQ8SCkF5esEakYWPq7mMqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIuGy4VNWoFQy0UCWyrcAwD0ImfyeVsu1D39c6xrxP%2FEg4ycaoX9GX71z3bu7N2T8i92a1GmnT5VZHHCa5r7chnRFz3R37bRlxsnHA%2FKEPbtfhFgqIcT3vfQdg2fyC51A%2Fq330WlNaUlot2y8qvHQI0%2B3NjWMNpDif5EZIrik90wlgxNNyP6Mi5Yxdxo9gaVYxz5BH6UAOx3A8AjORAynP%2Bj9YqaqZFU1mJ5F4Qx1pqSR3BC4vAb%2FR7gKiQ1XeDRDRuiQP%2BBz%2BY7iObHn%2FmnzpLYeIGNwQojejtGcmkqz2Im1asDBTBWipf5qeNk%2BHw9%2Bjnoto6Tl1Dv%2FPDkEjIYtjQoK%2BddmrVvJyi9iQjr1BX%2FxgvRWUfuRO5OWgqtF5CX1y5GlxIXJlosbV%2BmHdH4qEPQgjpTax7c6Eq5JHLNzF%2FAtkdSRH0ecNl5nVi66o4O2TAeTJTkF%2FPLNcoeQJKMeC2KC3rH10zg0%2FjnG5BUAkUbngxjetdms5aCVVzkFk1u7jy87LmcgHYQxWwqAZQIaMUr53M0znYNjK%2B%2FRW0dqnwRc%2BJ%2F537unDtEYb0f0KkhakAlAv85Wu8Sp7JIXajKTBSs2xh%2Bwo6DUHdkDaFlK1sE7Rvff4fImoU74fe%2Fe6Llg7XEGkk%2B0qyZRTyTMO75sskGOqUBJ9xHm07yGsSvfQE5Zv%2F4pGZiTTGduSLsqIAhRvkLxclsf0SSFrZfHAErkgyL0AGKCtexVfqL%2BRFdOpJ1ZD%2FYvibPugHbdzaHC63ZqIQ1b1WtkYdS97pma%2B52ythuxqIOtdfv3LkIhnfEpsp1LGnS5TAVqO9zVuXLvONSp2jLVl0nXCGxC%2BFxCqCzUWxNVu0xp19cQ8bDBraWqFj8AKoCg8C7EMCS&X-Amz-Signature=3e84de152cd0fa2e05447025baa24ee6ae0339e2a023ed97934298037bdd23d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

