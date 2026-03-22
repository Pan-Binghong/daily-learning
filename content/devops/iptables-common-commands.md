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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5da2e1eb-c9ee-47d7-8b26-5710b6c7fa13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FDF4RME%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTPYhmPOhk7fPmtVX%2B2LdItkI5s5f18Vr8qbcZ0XIqVgIhAN8MuEav00DkJFe1dIufM6jBed29c0xiT6y0B0hMdyZAKv8DCFwQABoMNjM3NDIzMTgzODA1IgzgvY%2FJ6RQqvItW%2FFsq3ANBKFEEMBWHH9L61xKh1R2APPiKYkdjPuN2m3HZ5Z2afVbjAAwVir1dj3ZvOILGtv%2F%2FtVAl7ySom4aKGL%2BZCGOfLQ5f9g8UUyxN%2FS8qFNvJe8WO%2FAVqw9EMaUpSDYmIOwJiv3Nv80f3lz9aRLK4kOM3h5EonfCWrUpndtQ0rX7wOCp%2FEKoVBJgJbSXuR%2F%2BUpDoS5TnDWW0jfeHB0oznmg3ksAVBNypC8KSFMZAgWhmY2HeXRgfqjjB7YXeQs5hzmLak%2FbOIW93bxae1Qar0KpKApiYy8ya8q87RO217bdwAAXIN0cx1NLawmsG3CpsjnnyMgXHG5Xd1ERoHx2YL4caMweOgHyB7g53BJXvrfNLlpWafXSVFTkXU4kiEW9Kp8ZXIgY6glMaj5Jt4it%2BvHn8gKjBEtRR43d4GRrFOpgfcw3Cr%2B0Op%2BP8X6S5IpTyEgKLxWBxYYz4m7LYlI4TPsDi8ZWyOUY0WuNzA0uThYO0SxdBirlSZorOGEqwca1OJO%2F8wonyPQUymo%2B9QmawwVl6KoYIA6S9Qhu%2Fyya9VRD%2BaesisRvmRV%2BdJ%2BD7Ev28i0RShc5d60YeFvwfJhsNockSKpaMkbtuAEOfdYT5tna10siapcEjY%2FvRlaO1PNDCxrP3NBjqkASdQQdu5UK%2BO9vorzK0t3onEChiBG3JmO3WezOPuasEJ%2BD1Q3E2yCehGKghQP5n%2BRCAtFMZCgtpKhogjHeYhO%2FH9g7Kc%2FXnh3f674PcEO2ZK3M2IwX3PpNimnbEC3W%2BHUeS%2FMqqLeyzhfQqjj1%2FgssW7SJCssPcr5xZgLOofU23TEkNiT9kF1yTE5DtSz8F3tTAacZIFJ6qbMSDVuNEvbnj9S4Db&X-Amz-Signature=2b42fc224fc652619efb2369ba55e874efe40c2cdcd6c9c2d56f1432880e2eaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



