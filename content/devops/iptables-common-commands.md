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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5da2e1eb-c9ee-47d7-8b26-5710b6c7fa13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VAWVFKP%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025826Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQDpVn3Tv04PMBtaJH1q4ur43i%2FyHr2AkpHNqYBukCFgIQIgWHcmiNFk9s6hh8%2BMYVkOzBCz4oaMayhMdh%2FOZi6CPYoq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDD2O5qXzZ1MokAp5ByrcA0N%2B97Dnd%2FjBFWnHeM%2FIjAa4I4SBtvy2FshMGSHCpzNbEXBbbIVkSW4fEyhfim5VGU%2B5ZOv2mj2Gz1SNN4pOcK5GLPyIL2JSjWyrGmaRWdWNsqQnkSu7Dd%2B5LJTVF48zesC8jUBmu3%2FPewFIQwNPdM%2BmfcmRn8p5XR%2BAxXvVh5tKVdHQMVKo1txcgB3gkbkBES4GjKddUx3z5pOsJy7sN2Eco69wiUh%2BskBQxOI7u36d0TfsKb9n1tGLVlXAXEZOYPcBKCF6jn6lukNdrvM401gvzrlxiO33P4Uzd0Oek1in3m4x%2FkSA7uru7uBYeZEwHeDH2vDUIKKLQV%2BGskTcIANdwp5eSpPkm1z5Jqi%2FTUlbQX5dv3la%2FWkg6HrKw%2Brnw48VAXmzUoSSPgfVemspNriqARYBOtyU0b93rhtRDHA9dDoMFUDBlFXb1Djap5DyJoqKEzMLQmNK8T4SiE1XmLiwcoyrlFqjPsFHnoc1ZGOp8Idaix0x5Oqw5GL8wDKRWSTSL09Xz5Os8KURIseuNN%2F2e%2FSIaahwYGLWIHYrdPTPRsBU8oeAEDO67txGZLhdBsavI7YQbKs4SF%2BLuD1ENEGBKO8kaEBIldP%2FNvHTzGNFdmNIz55z8hsm9Dt3MJigssoGOqUBDQ6X3Fm%2F%2B6ICQNclBBhylpTnuKXxVeTw1P271%2BmQAao0fv5MKSDB38LxvldvWeLCLPPzH%2FrhUAPZTr4NgT8thnr1TBNbW7%2FqfL1tVdvDoiHnsiigntcDNEUUwU1Y3ohVFsLfq3gyhsSr7ZGhHoSfh9uPGqtW%2BpFlzi%2FDWQt2Ng087S25uaCNJwAUlxhuCRu4Efs6lFWMKkEaz3m33QjcLcxf%2FXWC&X-Amz-Signature=fd0f97a5720f0b318cf731faf04ac1461173bbd4c6ea33cebd95901232197de3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



