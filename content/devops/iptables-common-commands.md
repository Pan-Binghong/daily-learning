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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5da2e1eb-c9ee-47d7-8b26-5710b6c7fa13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466424NJYKZ%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4CeaCuTtA3RPljD9OxgfMxzc%2FQz79iftQ3JH8DlvBZgIgGzNFSyeP62M2TG5P8%2BbgVIGhJ5HbRxChdMGJJEFmQekq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDD7T2elR4g5Pj7e7LircA2wmyyewJrwJhpUPZMONJfW6PyCzhEYAHbToJn4m0RolwxJ2bNI9Hq1LZ7yuGpp6BIIMO%2FofaB6ZWrRlhCrUj1AJrE7hOTrFfmsRYqMvgSvPW%2Bxl9tf%2Fpw5PUUnC6v%2BnfVWgT58Z1FXuBOl8xBNY%2Ba6Gg5c0E7a%2FM5iB%2BzmnvTzpvlqmftHOSsYT9THzVYqB%2Fqq0dSjq19BHXmJZT04K07IOjzRjDeo1BwEj51GdYeo6N6yhLxK8PRzZZtedl2XyzldEFgD%2F5H%2Bj%2F486w7y9wDv7MvJ7So5DjleQtaAeW0wDWAJrj4QzgcmuNoWxJnM4JAP9QtBKXW0Cx2bNGvAviXKvUi222%2FH5OofBeCSnciXNGeuxDmUnfS7xCqSU2zx75QjCgOxmq9He8IGum3G%2FOiuDmtWyW9V2QhviOUxt30VII3xAhb9FY0b%2FldI90ZH9MFwEo3DK0Kf6kYCzRPdNyMUx66b7KXrmwgEXedIfVDh5yIiw7oG6Vdr6YKa2%2F%2FFXT1wErflXaBPJoBXf%2BCvxiqtv1DlLcGBfN4fXzCU8XUzqPMtoKNKeKZE98lkeVdWSuFEvOD%2BHFeFCpdkuwt6rsBZmKkxLNdx89LDf22pm4GQ76kI%2F9vQLndImpvr2MJWMyMkGOqUB38gWQyt09cZwR7JGqvOQUuGk20dCXESLlB8DtXTv0XTMkEP0DNH6%2FCZAxfbWMdVftVDUOVVdXZSCOB06MfCBkYc6%2BVggUyBCZc3Ihr5alX%2BDSgbIBFK2WnSwNX9I27hF8%2F4fOojdZtGfDvx3w9nRW20XtvG1FqoakCfVcy5Ej5D%2BUK7u0myEk4Ix517x6RncERPTCIjU9LkAxmF5E%2BmDlKoqFd6q&X-Amz-Signature=859787c8e771ced730249dc0efd0e01dd1f2f7d8ead9e6da251288169d2f34c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



