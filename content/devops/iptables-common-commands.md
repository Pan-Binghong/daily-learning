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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5da2e1eb-c9ee-47d7-8b26-5710b6c7fa13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S4AA75M%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDU51NPeD%2FUlUcP%2BPtCsDYTIY8pqk1xNUqhW9bTyvTJ3QIgWEaDHuYRxFf6QCggEPupq3IlUU9quJb6JZKfN51pUAAq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDIE9Ee8FtrJJMMqTYyrcA1poX4Yo7UU2sed16eoSAncHGpKMwyUW5SGmdkv1jI0NqNcABi4kPAZ77ThgbuDt42R0xbq6v58zeJWvX0qocTxaZxyeGMm6WDEgENo2EjrX5Qa2KVBTOkv35bfEZkmH1imLeu%2Blh1RnGCtGQXcNbzlTidIvnR%2FK4EKBLxWkjFXuQnJ1ExkQ4BMOrOsw3P2IX8HUghLONHY6zbE1MT7nrg%2B23PXEFeQq8nklKYMt%2BwOsbNCTZAs3xaYnK%2FRO3UUbK5SaTJDS%2BmMYwu%2BlNCVePIGJ4CRLAyVdf62S8J%2FivC5880nd0COAX09V4%2FYghVrgiA1k09iUzL1G22R7d3k27tRriC%2B5dm%2BfeLp4dgc0Gbu4GX2fMUBt5Y%2FnHfNlVrony4zXn2e7UdXUt7YCiAIv73fRpQUzPiMrY7M32d%2BGTWJbdJtIMUmdI0rhtI25MkH%2FbHtnqvOzSX5TFiLJNomwgqE1pDS%2FPB0jyUn4gtO4XZyLqVADmwmsE%2F%2FaKlttBehzPPj9mPdbcA889hAT1RktlMUGVL60RdChWU149XeFxN4no8bCnL03fqnDnJXA9i6Ks%2FY2eo6%2FiFfhjDkYO11fyI%2Bq%2BT3WnlwdosrZhc1CWDr3AEnEfkiIMuDUQ0N3MP%2B%2FpssGOqUB7kgJ%2BqlFAOPaSmiz7Cty%2FWnpnCw3zm6ucB0MUFPp0Mvmnt1VYCAYnOVgyJ4znzT5IyLwUAjGSuwjZeCKyjaCX7gi%2FTXKOKY1Yxo%2B8g14hmnnxfLAWVOCBiZSGmxuCdmQHCjasIRm9yi7gJgimxEZOwy7Vnxsn5rCUf7xiyEZLI%2FNKL3nbPlwZb1amBSPxWeRxeK%2FjZSmZBtTotQ1KDJQrfnVvtaG&X-Amz-Signature=784bfb4b041ff11ed0f90c075ea31a42cffafb00aaf460755cda479166724ab9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



