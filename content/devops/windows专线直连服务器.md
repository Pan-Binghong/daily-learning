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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZM6R5QZ%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB%2FG8z8Y4tsb0Q4AZMYQBkQacCUPHDAjYUdGqvouQvFkAiEAlwW3yT%2FuSpLx0ajEo6goUt2USBzCErDULKUSvrLlbkkqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2FzhDrpZJPspT5H8yrcA7tyWFOtjoHJoBbrRmy10N7gVSx7Giz21ZLjdKQ%2F%2BjbZlPxzEOIgnTNJCT0ZI1wZp%2BPBKMiWu6k5sYtN%2FjTQi%2FBwvPeGPdcd7joRJyv4ji11SBP%2FFZnI%2BSBzVJw18sqZlDJ%2FJpSii5OILoIw5kjxjrQSa9VQw3wmzAlphjfPmDjZriwtapH%2BQAwWUcVpU30phFaBkPxj%2FX4ShTlR0wicgORBBpBMZUiDL9tpMqi8BECj1cTO5WJxqth%2FbRftLq2FqHhEYk91RsvFMhhM5%2BnnUQdC0IEtOXABR%2FUEWpRvrLlHIoYx5tU7qbn%2B6l7MZMQPz36aJ2gnYECnEUHf4MWbqLVP65DEo8ttgIYJyLW9s0G7WUfX6cnY%2Bj8K7n3GtBRlSunwqERgy399GN%2Fj5tG5xXIoPyh%2Fk%2BR4jZml%2FeunbYv8Dv15EObosJnwmjj1yV5OYnlqcVxAlZxMtifCv6suV0V4mgLOptrfMs4fCjWZNPknTjndZPvM8hxvQ1sX8yF9Hrrjtv4pnsMiJiyhMpYLqhZDiKLpiI1%2FWG4xWOQ7GTnL5MiD4aLK8U6C0ghJvbaS4RzgQDAEPnaGNSzZMHQaa2AGOtAH9Tv5RsDCl%2ByOa7Evev0h0Yz3GNJW5iAVMMqNu8sGOqUBwK0FmBYNHKchS2PzZt5xB7P3zzQg6dLnKUrQzkj%2FqbUvglFVISOVY%2B9zcveB9c5i7lxBK37wMXaJPGMgNSzcfPo5tzTCiEqOcbEuBSRvlKUt9dMR3cyVw5eur6k39nuo3UahT6kZltj8vyUDytWc1Yku3tgms9d1Kj0nGE8zDtFWq%2FML4ssN3MiIGFDcT4Ft%2BCMM4DGG03t9IOrRWaKnPUPHtNDw&X-Amz-Signature=b5ec887992f5d6c842e4142d02a3586b63d2f946ceaf316ef1e7765351ddf0f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

