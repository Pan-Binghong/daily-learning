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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5da2e1eb-c9ee-47d7-8b26-5710b6c7fa13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666W6NKF6T%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T034022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIHLQ1UxJygzfBHpRfUDTo63p%2FzsAjRss%2BRVxO%2BBM4U0CAiEAyzW%2FILbLWXv8IGxvIRXtSseQ%2F0g6Vd9pIsO6UZAIrMEq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDCKsVfWGW9TLt4yL1SrcA14r0%2FM78e2l6Lv1L8BUAT8T6osuDli529y8EXQlGVTzw61Om%2BNNAcE4SE9WDJ126k6WTQAj8%2BbcxAEklon2%2FrtesTpOdoQbM16ajKo8R3%2BUYJTT3AenQF7Rvk9usf5FesQ5d1GXd65y%2BSXuo%2Bv%2BL5lNEDUqQbkSlqfOGQA6TQVdFBku46dd9pAa9LJE17LkWdBBGDJIORj4eQo7UrwBsTxGLCMc3v1U5mF%2FfPl%2Bm8V2cfNtz%2FVWC7Dd1bwo5EpLo72zgbbHpy%2F%2BB1BFxu0tujxwJOvAixsg83ded1mQKa6zciPYija3SX1HocDNKe7DBu5ixtw3%2F4vr6egZDIFPJ9KmkAcHlqR%2Bb2mJrvlzsElgIWJhrlB7WS2Y0SX0zBD0N0JA4JPzLNjn3rD%2BU57P5KHNGF%2FzRGqWGUzflAqnszipYMrUu%2FSZgL71XIzH3Z%2Bwjpsch7V7u9ivQxmF1qzo%2FETcuSHGb8K2wwbWKTs0oUeLfevjZ%2BH0OIvqWTxNGER9gREpnYVV%2BgyMk2EMb1QzpptHqD4CHz%2BGj1ZCpOUFUM3odt6Sms5OVPml0I7ixPPiQIq0iRqPc9HRanQnNyE0D4WHO67a83jzIuYjJKFLVshxXeZnN%2BcJDiGg%2FhXGMIXq5s4GOqUBDoZox8XXFRx5v3%2BXJ4PWfOUUO71ZoCeDme%2FiBZWqefVlMqAhnxGFAgka53F9ZB%2B7RrBWOgfF7q0s5qCee1tIDUuPWprLC%2BV42W516aoyUddpcCOl1npQ0h3KWxnJHUbgMr8d3veBDbUzc40lPEemZ1m%2BvJKJeVS5tNR9pFW44%2F3oG08b2Gs2nkCSg5TGZEL09hX9o74aN6Mp3SS6HppJMujy1hsL&X-Amz-Signature=3aa96551eb47a38e7c7df01a447229d1914a1947326cb43f5334d2488d21a174&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



