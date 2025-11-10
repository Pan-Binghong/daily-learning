---
title: Iptables Common commands
date: '2025-03-12T05:46:00.000Z'
lastmod: '2025-05-20T01:41:00.000Z'
draft: false
tags:
- Linux
- Iptables
categories:
- DevOps
---

> 💡 iptables 全称为：netfilter/iptables 是一个IP数据包过滤系统。

---

## iptables工作流程

采用数据包过滤机制工作的，所以它会对请求的数据包的包头进行分析，并根据我们预先设定的规则进行匹配来决定是否可以进入主机。

1. 防火墙是一层一层过滤的。实际是按照配置规则的顺序从上到下，从前到后进行filter。
1. 如果匹配上规则，表明阻止还是通过，此时数据包就不再向下匹配新规则。
1. 如果规则中，没有表明阻止还是通过，即等同于没有匹配上规则，按照默认策略处理。
1. 防火墙的默认规则是对应的链的所有规则执行完成后才会执行。
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5da2e1eb-c9ee-47d7-8b26-5710b6c7fa13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFSELROG%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIGVc%2B5PzvjBHeL6AsrYk%2BoIf2KMNU3oC4bh6CBre0ifHAiEA7ewrsn4FC9WM8A6MyKTVdfD0GOZ82I8U1AyHDXsu7vYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKrU6%2B5XOl%2FMwh8pzCrcA3lp37r5DvrU1wORQh3KLEORh%2BfXeB53qf2HP5FDT85l1rVEdXtn8JgMALJpDy2WvVl46fbkeVqhwwg17POgg2EkenT2HlwJbjcKs78nEO5Pxp3XzXMAZBaYOqTaxzizGZoAFMo1id6VgOHzTihLVLGhcXh%2Fs9cgDf0gNatYtY8YbDQAAyJ9SvvC76BigmDoiSTy2F2zAwcyk5CCajy3epdEe06aEMKp9%2FG2hokc6erk60OrrpXVEA2ydyN6iJtvaB5riXLLxSq6SHKW3b7JCejJLYm%2B183yqefQhusbXWzh5KhvIAz%2BrJtSJZrKIQzlYO8boMPzRFWiPiWcqO8Px6v964DRSYL6AL9pURXoh7PYBIFctW5DLVP8lxr0bLv6WPvAMkezHEcyDI8fXyK81dcG1Ekv5bXr%2FCM%2FBHkUrfXwYTEppHQZqp0XPCzpzBVG%2Fd5vs1arS1YltZ5UXngIw%2B3sHaT%2FURTybD%2Bmgw7Vy3IKcXRLAT7tdjWq89MlprO1RV%2BFA6gfFonuDxw%2FyJjxXCApNumMpMvEXaIpMfMfSqs26%2FTFBQbwrVr9pNI7s9h9emLw8lUoQocgykbzUlKW1WOoYKrdXruGKfOIGNlND0K%2BdSlNWSKrjwjC%2BCG0MNS3xMgGOqUBXtn7n0ds9nVqQRCqG5ZvxdUiAvll%2Bx%2F1KOKM089%2BNbh6%2Be6BPU2k%2FI5rKZOcSZIHONc7SWAv4KD7R8xxRO93sKLMHzIBnj1IUg5p%2B%2F8J%2BO%2BKA8eMlcMcofGDCoEbE%2B1FmfvcdvW6atY9ZyfR4GGIsPqr99pDDashamz2O7z96ZZF%2FoqJThNmk2NStc%2FnwUgxdMphLvepbdVYvLMJ%2Bx6tsx9opFkC&X-Amz-Signature=f68161889da03e1f457f4e34183d83a88bd7f12ccb54e6f7d56c1022a56b3e9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据包基本结构</summary>

</details>

---

## 四表五链

- 链就是位置：共有5个，进路由（PREROUTING)、进系统（INPUT）、转发（FORWARD)、出系统（OUTPUT）、出路由（POSTROUTING)。
- 表就是存储的规则：数据包到了该链处，会去对应表中查询设置的规则，然后决定是否放行、丢弃、转发还是修改等操作。
---

## 四表

1. filter表：过滤数据包。
1. nat表：用于网络地址转化（IP、端口）。
1. mangle表：修改数据包的服务类型、TTL、并且可以配置路由实现QOS。
1. raw表：主要用来决定是否对数据包进行状态跟踪。
---

## 五链

1. INPUT链——进来的数据包应用此规则链中的策略
1. OUTPUT链——外出的数据包应用此规则链中的策略
1. FORWARD链——转发数据包时应用此规则链中的策略
1. PREROUTING链——对数据包作路由选择前应用此链中的规则（所有的数据包进来的时侯都先由这个链处理）
1. POSTROUTING链——对数据包作路由选择后应用此链中的规则（所有的数据包出来的时侯都先由这个链处理）
---

## iptables常用选项与参数

```bash
iptables [-t 表名] 管理选项 [链名] [匹配条件] [-j 控制类型]
```

- 表名、链名：指定iptables命令所操作的表和链，未指定表名时将默认使用filter表；
- 管理选项：表示iptables规则的操作方式，比如：插入、增加、删除、查看等；
- 匹配条件：指定要处理的数据包的特征，不符合指定条件的数据包不处理；
- 控制类型：指数据包的处理方式，比如：允许accept、拒绝reject、丢弃drop、日志LOG等；
<details><summary>管理选项</summary>

</details>

<details><summary>完整版本</summary>

</details>

---

### 常用命令

更多详细的命令见：https://www.cnblogs.com/zhujingzhi/p/9706664.html

---

## 实际案例

```bash
# 添加新的DNAT规则
iptables -t nat -A PREROUTING -p tcp --dport 18083 -j DNAT --to-destination 192.168.0.89:8003

# 添加新的MASQUERADE规则，保证数据包能正确返回
iptables -t nat -A POSTROUTING -p tcp -d 192.168.0.89 --dport 8003 -j MASQUERADE

# 删除规则
iptables -t nat -D PREROUTING 1
iptables -t nat -D POSTROUTING 1

# 查看
iptables -t nat -L -n -v
```

---

> References



