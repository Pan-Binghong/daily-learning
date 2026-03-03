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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5da2e1eb-c9ee-47d7-8b26-5710b6c7fa13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAU2TCKK%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID4oSm7D9B3UgSJr3pZOHqBjfFqO1dQFuHBObEiLOcp4AiAM731OUHX4RBbgcgDj%2BaVhq9JA48PKoHlagJtE59TlcCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgktRIgsSY1Zs2fYMKtwDH7Qjw3BPa8Y8mbQnXV8v6GeQnuMQU4hZpNhJfI7tD4XSL%2FhJMVgtMifZW66siIN2MvkUg%2BGI599zQ%2BmxV2rudo0Gt1LnZYpJ2Dik%2Bl2kwpEViaZfTYZ0Y5tqApADwl9tOSHjFhJPHunCOQQYVwwT188jZ5%2FA%2BORSNtJsBwOs7XZlThI%2Bh8U3M2iTvOM4lF2geC5lUKYgFXjiuGGb1nnXGdwHZwlwIKAFfSCl3hXGcKUKju2E41w%2FLGsv%2B5jT4YwuaCG6FxIu1EZE9iwcCGBHyIGVDED88bYgpobhf8kk%2B2DKPTn8hahha%2F0kTF5CQq%2F%2F8kdlRyoYiNtGmNgl2pVPewJP1TuK3IRgFGBDtHpTIsJGwJaLx1bk929AYZCceadm0llRbhBSYDPLcRZ5tGZn4SKOWbb5spwtBFAFDmIAx7xKv9ybjHNYs%2FWux56BwxnGtIaQEgHFRJUntd70rHIj6QUF0abmP1YvExakSORPtF%2BC8R4ADTvu4vckWygCh0EnMiLeakqLgoHZqDaxu3rExvkqUA5enbfYZvhUKsllubfANwEYoeE2Jot38H%2F3KxnCv6d5P4MFM5TDNNFf%2BOAA12ei0UeQ3cPznl%2BBxVEH0ZjLpYBqS7XaapeAFdQwk7aYzQY6pgGH%2F4vVAV3XkpU5SEquApDWBE5K8ZoAEKXyJC%2BLV3cUdGhaVnjGwrSe%2FMFlg0q7bxfpF%2BAyRQY%2FVMCFRXuR%2Fg%2Bzo5AFN04eNavwte%2B0cqZmVubwshMY9T8cimUVNaC7fNbC331GK1i3z1YYV58T5le6BcFpsUyllqvwXtg0ENNBl0jhazHNtpbNht8GszcN%2FWGq5yL8C03gzNVhE5eexwLVbotqNU7j&X-Amz-Signature=21648a286fde42838b31cf0e89d8a5c03c704b0cbad2399eedf5162d1a68572f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



