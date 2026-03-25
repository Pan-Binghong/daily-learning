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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5da2e1eb-c9ee-47d7-8b26-5710b6c7fa13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVDBL247%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCrHNgUCTjK6fLSO3MpWkMinQDeJhyABoL%2ByjHdwGJuWQIgVhIBtZtw6Hv9%2BQRJEVSN8EYC1ytQ%2FnQbDS5EICWtVFEqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAebOqLymhwTGIOVzCrcA%2FmjaQGyVBS%2B1GNBYO%2BqtWzUqsuzMYN%2F0U39kuZf1dMvfXMHWtoXiGJLiOQNNXRWBYnU5tOH%2Btt%2FnH6oFgwTijn8pabGBO%2F6DsKMc%2FEErwhUv3XsBA%2BiDupK89me%2BaXPLAuvyECBmCQn5sjAuDXGosKVBz%2F0Yz72S6ioHLi%2Bsxf3YHwD1QOo1My3Smxu%2BzONSU0TNysiHnVO90r6BjcRnyN3cZPUpZweaEm2ZX%2B6Y8HNRWS9aTF79DefAlZOBrCYMXKGrcKsws8%2F7f3OIGNW75koItvigAhX8qx%2B11J5wrrBRja457rqqXej8iFW4Pb%2Bcf7JxgJ3BSkCOin7jDEWr6FGSxktnvxpZvhRnkMu0p%2F4qABkHp8dBtmaCym0uL97L0QAo7L65HSV44PgNNSS55mqeqbIjNuG4150t6CeCMewgin1ZTS5yLaDb4C%2BFUBDzv8790CY5fmm6shD5u0ZiY1dcM33gQQOByUEsy3axa%2Bk6lTZGCARNSwOL9rVFwsy8k2DejbeEj9bjE7wbgK6D7ZG4V4%2BsP3OaQuABy%2FZc4K0GPoyxFi584s4Bmk97SYEGzukhNQbLkojit%2Fzsm1AJsEUeF6b0mEiacJJgdKOQYgRQa7E7buOCWZOz%2FUmMK2ljc4GOqUBabEsYuQdJBO3jB5C3EjjLZPZqsFYvY668IqrOtcKB6XHXOFZg9he4Rp0eODJKl%2BpggBPU9w%2BgSfUDL%2B3zP3q0Kw6sXZ9FWnURhc5h0uQJ2WfS9ynBKWjZQHJQr8iwkLNZlMQch6grWFoFlmdidlo6ZZw8GNygeKfrfHBplw92WXhIoZvVi3tMasubuBvq7P1IIU7oVZ5ExmI%2FHU28XAcu%2BqcmZiv&X-Amz-Signature=12c19bec164aa623893c66f54a501568fa98aadf47efb28df0eb774a7e345af5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



