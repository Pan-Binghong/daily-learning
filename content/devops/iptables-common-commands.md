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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5da2e1eb-c9ee-47d7-8b26-5710b6c7fa13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KBXG7VE%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIDotkt6GNZ%2FnGpe7THQ82q81fjM2RXyLmMc52Se3ZNmcAiEAm1nyiRsLLuIdJsxmgplpOZl2Yws8UupOjAkT%2B9cF%2Bd8qiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB%2FSIc6PQskrR3jozyrcA3DvIBMLgqf9xwnW9kgt2N7DCBtti5qM9nlPAVyzcimSIHWFZ%2FDvecQpNNid%2BrRsXia0WDK05sdh7ZC1KNGpqA%2Fmpm6pyNKdByrbV2NVd5KVZ2vOYSinx2jDJoT2H4sg5N%2BdsL7Ii6kAy5f3a2GHa8hAS72etKtINCrKI%2FSaJQI58ZnD3gaUj3aiHOcUPv12%2BycpLj4ZL24EHTP5Ul5eTcmFiK7ZI%2BvpyVrZGTSlbNC%2FokEv0Xbm2%2F6C5ipe59R4tPfHuqX1yQC%2FCUiCJbdtYJ57oN1BQ2FyMoSEITByDce57H1vOK61IsQ1rg53Y3FX41pAJsOoqUFCLvv7tQf6WPXbLxMklaDiapw%2F0EvJE1gOX7Ocrhqs7A8izlAJwW%2FK8uIFqJ1kD5cjzMLPiY%2BTdchTsVkpOIy94USidK544u9HNfj%2Fi4ncj%2B7plBsRgNF8YSAh1MFh9p0st5Y6rB9Gy2brwXe3dsj3ErjhwRuLlGMMjd9iXHlPvnlBgwfVYAPvAELVHmJtlroE75biyJQKyvMGb4bGQJwtJAyvf2vicCm29Sj82w3%2Bo%2F9iLOwwbwPklqKyiLALi7exZyHSDpRyhd0TfB7534QhA9rrK%2Fm5QtuzCzllwTycSrkjZcSYMIXrls4GOqUBothYPDDthnqlHinrDLsHHdiBdrXCQltzUMi2WvvoznsfbH1MoMDA%2FHvXXHRR8dMSC8spSO9pWmqasUTYWKnTv%2FgUGibIloV3%2FQ0Y%2FshaevUQENflMQx9EbIfDzzMjl2fKy7C0U61F3ZiF%2Bvu0akn6r%2BRdLaFATX7gObmIl%2BDDVgUgVspj9QUmNRbiIf0NUASAynVoKXDs0V5iUd%2Fr0QKL6%2FQXS4p&X-Amz-Signature=8687e94a73bbdb6b5602769cd0c66f89a968e78070793104ea22051867643b1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



