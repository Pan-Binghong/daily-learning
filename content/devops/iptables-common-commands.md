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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5da2e1eb-c9ee-47d7-8b26-5710b6c7fa13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKVMWKJK%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQC%2F8zC1IoGXzvs%2BeeorPMa56Ss9Fs1r2LiSG75fQpeEyAIhAOcj6kYVgWeos83ae%2BfgHHaSy7R4yodEJfpZd2KLytGBKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzzHhK%2B8rGl5M5LWEEq3AOhqGtUfwrqP5rHjJ%2B%2FWgTUShRVMq5Y9e5sVGSUSwaFHEdFLGdI%2FLgzm0AFEnsUKn1fRXP0i04uzBkb8xGx3VLouqgAhWqVx3A5Zx%2FPLxTYeUPL2DoDnonGKCxmdnzZMajWjWAz5eK7wnw%2FHtVclhceX9RRjyrvFAe%2FaYjyGx9sU7fDl%2F0jYcmurZmJ0zbrVRExP6dAjTb5nt8ZMl4O505PqD0FdLhhEx3iav0nl9YZW9%2FhCJsSACjTsKv6Bzww8GAsX%2B92Q%2BlvLgpqrKHX4J0QnBDVJGQoNPEV%2BwuGfMi18%2BxPggdRoZsjaSMsoOzoVMzjF6imjh%2ByWdlFSE6JfuA0SYbWE%2Bitnu8H%2BpQiBVIZrXzy55LKfoUhIpvBv4r5WcXJ1N0hQY3C%2BVEBd9k7%2Bng9j9jnZnpyKTG6aG9N%2F3vT9DawsEyQJI0p8E2BVxFNHGrcQw5X%2FFvgkbj0WWz3sm63xepT%2BjGBuiWs%2BP9%2BZWhYzrVltFrqaxNDnf0MsWGgcl6JT7NhAy3vcWiG42n7%2Fl6Nco2ExnKyCaIVZjqbz4TCrfLQf2VIaR9G6AlOtlquRdRst8nQVkIRnNBBGwqitkm5S%2B4RuSzxQr4HYe%2BQSus3lCRuieHyJRBIPe%2BhLDCr7MDPBjqkAQZ9UfStyP4R3K31QTD%2B%2B8GGUoLxm%2Fcuhv%2FexnOI9aO0p4fIhCNWTpVI6qHceYhcd7LO%2BVEaZo5SyTcai4Lhsi1N2sIgG391YaJrl5z3912GXR%2B%2FkyncV34ZM7uDEf4M06fAMe1oU5ZeFfCMvmmuXT6e80C%2FGvMVijuvlfHUZmyXLtnNccv9K6avRj24HfCeT%2BGBH%2BzMyxkUGKyc76Wjv17BMHu4&X-Amz-Signature=bc6b6e42ddbc41b74137c3964328e5834fe1de481fed2a24489bf18271fb1d14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



