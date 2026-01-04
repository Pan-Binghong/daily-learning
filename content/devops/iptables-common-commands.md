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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5da2e1eb-c9ee-47d7-8b26-5710b6c7fa13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JFU5HZ2%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDkx8Tyq%2BhYuKeHhJo%2F6eENfk2WEd3%2Bh1OqedPlT6JurQIgK3WgD7FvjeRHQbGDJ5iyldTAHP%2FJyGO62%2BKr2BH0NRkq%2FwMIIRAAGgw2Mzc0MjMxODM4MDUiDHeiB7%2BlMdskkXKHTSrcA34eubJKKgtGlnW6Qw0W9wrGXVhcvPZEHxULUtlR%2Ftsb5b6rm%2F2zXTRmbBsv3jpxIobpQiQZJZdmt5V3oantEToSJPJ93P8ZDkjgEaZdzHhHV97uk%2FP5nLsfz654tWqJkm2%2FFlraSYeKHQU7jBJc7qXmF3GswEwiptxzzgoIAERud1g3Fe6Q6jtTL2VLDrOOw4MftMk%2FvsQ%2FILj2tkDyn2BW6wiuqkEabCHVF8bTShExytXjLE8S5F%2Bi75pEEGOM0tFiaAX4wdSo7F%2Fvs0HAi6yNUtC4lejVGPaCgQqXsq9EfXfnELKvl70zcQjPaozLR8a93abSqNjao7Zjhuc1zLCocINTrcs6A5qMWP0FCrVlAvrm7yqfmJcy9TxuHf%2FP8G4TG9TaYd3oQ4gs%2F%2F%2BmK4GJmAo9FLGZXdMVZMyZabPTu4x%2BDiOyYKoBLwhmFyhKiTONIWVJSsTOQDgU0CsgpY3R0KJ2rPhrpb1QbJcObbJYueBh1C5bYVB68Y%2BkaFCPkYFDyz8jp404Fb1zpLGhlVG8o4uu2y84leyK1tA8fuFEPVZfieC4mp49t9rXK0M6NPEFhaAZfJOd060axLaulWkKMdOf8DsQEKVA90mjaBsZryujUJJDTOg41Xc3MODg5soGOqUBtfg%2FagBQrMB8SVRGm3k0ssX7aap4kZmMTBCB11gkvFJPEYKvN91olgS%2F4bSWYB4j6khge%2BE1yZsxmEXzirRHmEHqfY6cyLYxcOyfTgfWozBrLVYG8B9e0m1ugO6NkqjIfWxjCKNxYmOAgX9l3vX9ZMrFSoSx%2Bh%2FNAJq9kjb9grnMNmNVD6NfDxNXrVm8S4FZMde91toS%2BqrADUX3yXe%2BfhFzhJS4&X-Amz-Signature=1f2897a5d03f311e662824a19a468499d4b4ec0a2a1dcf7f8a818d64791acbc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



