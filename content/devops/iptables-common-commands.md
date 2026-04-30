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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5da2e1eb-c9ee-47d7-8b26-5710b6c7fa13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665O2XQLO6%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIFxG8xDuj6P51sCjSGYwOzU9MgRRx9Uh9z0fnxx%2F4F2sAiBN4Kp9bqd6yOlA%2B6tM19oAdFqh6l9ck3OZvNC2thRyeSr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMQao4ZWw84CbgwnBMKtwDZUlWJuYmv36ZQKTCWrh6M9tg8wGgsRh9DaKbW%2Fh3F0sQUBZtO%2Fh6K5O%2FmaXJmRFmuugB7Ui2xbRAnMd%2FNiVQoW6X2IHhXXR%2F30Ci8RklvIaAxCvMtwV%2FI3Qhg9nZoZcEOc0X85hUxoOvbU%2BqwynJXRqV5Z3%2BkwwxCmcsukmIJkMmWcRtMctSOSgIvHl5Y73SmOeIOOMneavyCsMtwB%2FSbtBQ7cqWpdgOXUZleNm%2BPKzO4GNkOhWNB17mJieSvzjufO0WUHWzttH%2BeRThWA3or7CPnd78oTYQhXXIlLfY9pEHNLWn2%2FOJqczsn74DB6fp24jn2a0zS3jrs15QKS%2F%2FngvHwZkLmlNGY4OMs27WxNQFU2xoAklTctQjVjnA2bHs6qF94VJ%2FGs1xe5weR6EonrIxo0BDHVxzsSKAY0Jx9BdMshBb023U3q4u%2BhsMV%2FIU24ODBWNG8o3zaMAp6eFKauN8TEGC%2BVIT6zvwWMPybuHEF4W%2Flffh2f1V5QTzsjy5sbBvPKN1ZFXC3Cj5RFNcfHrHtCQZageZU0uAiPTaGhBQZq9F%2BNOCXokEX%2B%2FcWzqniIfXSxpTBYXOkzW5kI87XdysdyszLUgnEXux2Ttxm5Wzbe%2FPz2ql0mrbpKMws53MzwY6pgHggvq7BLWytBOcS3gYLtUhcBU1jwBfPknqcse2r8ilE6H7pHoHrd16oNq7TxtAPVqUIZI5ZDxybMoud4v7CYrM5DQQ4PYo8OgV8b9JBi10YOuftXflT6ZvgyNdvLZzh7oVYu6Ftds%2FtafZBM7CH2sD2HN2DhvlOLqa2FzGM1P3CZPpnUG0cTcBCylALiJy2holbmnSx%2BOUzWNT9uWMIGms9I%2BHGMlj&X-Amz-Signature=5cfca749faccdce51e2596e1b53c03ad2e2c4ddfac576cfd2f15b06a59d26e26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



