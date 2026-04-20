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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5da2e1eb-c9ee-47d7-8b26-5710b6c7fa13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663G7VB7VK%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQC5p3NVGu7jYriSLJ0kEQQJ%2FtTnVIrmV%2BzOkypIwHOh9QIhANjzdY9Hqx%2BpQVnx4y6tzzhMezD%2B3%2Bpn6CW6wCg%2BMXbxKv8DCBMQABoMNjM3NDIzMTgzODA1IgwIIFEGzXcXF1in0XAq3AOEnrLepFL%2B4E5NDSfOlQRvN7GYInnwkYtC%2BpD9X850grPqSOtuWWg9eD9QH0r7sdq5l3YpNxmmuOa9uIBXlbFj41mXkeUnT3tPPg%2BlEe3b8PijcieYjolJChmusDEHlWU4%2BenvDv2TnmdvjMejCWAyn5jKOJP32cGCYlqtt0BnQQoZkLWa1gtHGJbs47jrn9idhMLGdFQn4sMQA6%2B%2BRrV9hDGigEDlBigd7Ru552u4l%2BEVzNIX6RAL0kCnivIJNjQOVZFbQCroa9bDVQ%2BK6VFmLReKduSmGF4VRq6KxEZr%2FWCytplIhOC36lsZJyDwc2CzvPLLXjcegdb6tyiffl8pgyf5J3luogXwyTxSnoARPMscoLE6qRBze0LMPzdQ%2FcHpFSuqGZ6t7DOSeFerr%2FbY%2Bc0WVKDodXjIuIquuLizAB3msUqJ5aeZJzDSV2JM74XGYc8wbM1y51w21Rc4GrYmu1Iqbx7dc1FWCabHnhgz115bgDOSxjSEYfer4RerncP1QAMu6C0mUPycudOqzFp3BBqFGcq4%2BqU8UpFlxuM6hk%2By3be0uKRnJ8WsZMKUFT4FUuU7vYcCYvqJ3WbLQsut17%2Bskt1S5wBRhPc%2B0tjTXwjpwNHLmA9ouWdO%2BDDdmJbPBjqkAUUkXGLu%2FpsAeResPNaTJm%2FhaxQWzpVGgh5WZJJUQnsV95pLmvtQZbRkwynnpFncp9jHk4Xav6fFdTNOeU2UtV%2BQ5DNctPXZNS%2FhrA1HZTBGF%2FXc1GeL5K9IuRNkwMw6e64UXilF1VJE4uARVNafCA2mAshLMqmAIkCFH6nvaID3JSHK8axnDP5sF3o%2BHQMLlriLKC4in92cjFpVqMUledo2FmVr&X-Amz-Signature=43e1ff0e354f2ad8e5d0bc920dae09986d79e158f9ce24763c195db8949bb39e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



