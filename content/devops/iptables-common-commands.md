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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5da2e1eb-c9ee-47d7-8b26-5710b6c7fa13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVSJL4N7%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIAyqkShpHST%2By3%2FY5oe%2FP7ykzbJVQCMfhJn54%2BqAT6btAiEA1fE0RX9m86cokEpd42gqi%2BDhrTCIlB6gHDx7gMo6u70qiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAk4iJ5K19Dg7ZNR6yrcA8kymOu5fbrXl07p5llkyG8moajo%2FW1koUeg2k3fUZPUZYq28kR%2FwK8IbJhnS3%2FfDlhwSr2q6xGLyxAWsD9HHnF%2FWPvyF5zew%2FsTEz2nAG9PE1CcmLquARqAW25EBeN99nRzrEz3fdHOhFG34FU7U1ZD3mED1%2F%2FqwJ9LsYOI%2FzrPQL455dq09rSdAWaFA3%2F14bF392VTFaWPnr8RDfEMSjiWtH5xNEY9aSbxNh%2FZLGzaEoBUlSLSn0%2F%2FZBflLpko%2Be%2FjF3K9P148MildQp18S29AVUcv%2BMZzzqIvPIt9EhzQ5sg9Qkg%2F22832z4yyC4o%2FP9UGouhAxL%2BMoly5prZurlElUjtNF88M5GYPV%2F%2FZoggw%2FaG3w%2BHjteDWAzS7woNKw%2B2Z3EMb0zcD4aHbrWPGjOgRDKY6d4G8Qf7Qnshlon5iNkV6H8YZCXR0Wp670dOSrR07siJVEbbjS9oFZqc6YD0pDUeFS7FrkYt1VoRVGar5LOkUiuUfUpTJgtwiZO3pd2x9L13ad0yw1KvOdftij7%2FOwzXfDoPJ7BVROEYOne9C3t8Q7AziPE%2FhwcKiyCT%2B%2FIMgvTMOhRQgVmG5uUaAgEjK%2FOqSrFIY%2BzEzbCT0oJNbrSTHBsi%2Bx2pb186MLG%2B3c0GOqUBX2VupLAVyZpXNPk%2BiqOpOwZSis7wRy4X9ISb2zfx2%2Bzl2pksdkWDPTcaGEhnGvPprm3LIwdeEPKCJZfk1NlRKk8Jh2S1%2Fi5gVLorAB%2BX0huXtF3yq0dnHwb5Kg%2F%2BB%2BNgsis0v0hWrpLiY%2FFeO9ktgsMqY8ThjvigS6vDu1Xdvqq4C7sTpVYifEotm5drjbFx%2B7rE2KkxeA0J8etilhYNHc%2FTdyaq&X-Amz-Signature=36f017b6a255913ab71a71708916460d03f7a4db9fdf1591f3c7f138938e7ec9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



