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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5da2e1eb-c9ee-47d7-8b26-5710b6c7fa13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQKQSI3S%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIAdLCb2wLpRplLQv6cXWt0liEjfsRfaT%2FzdKBrWwcQzyAiAeKAQWYnIJTAtZ7hwY92DpX7Ok46BX2a4vOOPSZGEQUCr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMZIuSNv4Z16qEIHk6KtwD0fK6DZhPyJ9aqOuNN7btpimjZvsRFDrQXgSw%2BxVBJQT9fO9EUw%2BbXeR%2BVxhiw1EeoCufk9x7oGdPbTSUHKeSBc4PARzIl0rOpWpaKadmgZN8FvFIJoKAkKYOsJspcjRAMbGc5nqIVqd%2FqMHwlDHHeMtlyc%2Bq65jfFGAgMFLPPo9jc19E%2F3xKe8R5i6hQFw38ENYo1Fp7jbrUj6NjMrYnXIZvh0Lz20cRU2GyTJ2uq3dAFmYhpPEk7t8%2BAhix8attPCB%2BfH3z8iPOkiPTsYOcV%2Fnbv4YQL%2FgFBliWk%2BypjdRvocJde0o0LzNRGocKe%2BY6vnOZEc3eOSOIz0IlighH5sqIpEjOfsDH%2FunrNM9u48F6Mr65TY84JSQwu7En4FRitJUjjHNIsytvHUhbVvP0YaG9560sphj39%2Be5pyck1K6PRUbX8bwnBWXAM6EUN0Y9uf%2BfhoWiy2Qt2HdndyvpZeAkx%2Bc9OIANyfY66EbSKQdZvm8q7FLMMnf%2BH%2Fkmz6ikiPSP4D2Z7WNhxKRt89l2MebDrnti77LcSVJTVgQ4l3Tq6lW8N6EtNNTrtka7wj8K28TxSXYES07pM%2FTgAAO5fcIK120cvNijeIMiApB%2BJuIZPxQp%2Bqs%2FfmWdR4EwwL7KyAY6pgEvMo1u1oeZlN2OQD6kTFVfYDiI2ESPf3hV3Fh62%2FXCLguskBIh3o0JmFuszOakhpXS56%2B8IaN1c6uZVyx6QX%2BePz56MtmoHHIlXH9Iy57gCQUdaEyOR73JRxu5gU7CWNBYWaG7VCrMic14kJFG0KVIe4JvdSxrfs1RwJInYvIEFvnT3QBljBgl1YFXyI3eG3IZUImNXRVh259lkD%2FK4ng%2BOXOoAb%2BD&X-Amz-Signature=fe6bffb26770449ca6c2c8ece5d748baaf660b34e9407b44edee7e5e69c9fda4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



