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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5da2e1eb-c9ee-47d7-8b26-5710b6c7fa13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FXXBGGQ%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQDYHCXrV6v%2F3Xf4gl97vDpZHNZr%2Feb70ym09XBKqNkIvQIhAKBIUVUoPXeZT5i1WJjM99iBd80COOqlOUAgtbS0tgJiKv8DCAwQABoMNjM3NDIzMTgzODA1Igxd69OxEl%2FcEymsf4gq3AOQhe3ejZCTzUFz54WCt2mEGIYbCfqf4vJS%2ByA3P4r4vxZcbcoJRq2HrDLvpZ3AAvZVdpY7KwFql31cZ%2Fo%2F7IrQ7Ph%2Bx0LtB%2FcLJVxBZXnKQDVTZ2BLWheMDV39kcoFx0v1YdW9iTftyIgM7L5ouI%2BHkznW9JcPGCgDTJS%2FJNFaAksWDPZHzwgJ4zGwMTwuXIDPux0imNwsBbShvgSXCgaaGrCurbiDR9nawxwz8vHdFpxtM0y0%2FmZmqOQkU6L9gkABsYtWfWtvTYFlDPomf7x%2Bq%2B7fXynmjPHyH5cy%2BQg5RrZ8Gs%2BA%2B5ihVSn8TRE1hvrhqnTMhA64wXCMrzOYbPfSnBUmucpI4rcUQb425k5RKEBB7cCRIVvizb6%2BCrw4Mal2ghiNoKXN4Kl6pF0%2Fty4oHgMDpTbLwasqyIDspgfd117ip84AxEyVgDkayjg%2BQRmcc1HanbZxc5Fc%2BYUKQgw8s1ulLeCZa822tkwKRxEUisr9LAuDeTDfmjtvq7SCPFfKqVnn2%2BKCxwYlSgw5jAfNaUj%2BVNR70kcVtpZkpg%2BVLWLzX9Zq5zCvUgQ9VjM7zvyFkDwGuV66QN26ckiQo0sbQuULJ8P91Wq5QCJqSiRNvK4XLMWNCb%2BSCaLLmjCWwrPNBjqkAcJFpfEW%2BKtO01UNEdoucp5g3M9zHmTZaoWHxG%2BNKZI2ssiMrJm7UA1vCE0J837jXf8kvsyhW8Sg4IY8VoIi2NBWEOAKctTb3CJ%2BMWRnaNXQ6%2BOIxm3rGfcgirC2XJM4HcPtSRNuZSrLVjpzUPDtqTl9kBDTMS0XkkWJfspdlpG%2Fc72AfFCxv1fXLN2SqzGdcjw9kPVUz9n2M%2BpcSZydKZk3%2BJ4S&X-Amz-Signature=952f6e56ca7d479b7777a131f09e5e6032b45bb1229c332480509a207d904240&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



