---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNRBV7OL%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCB7h2Ndfn1XplxQhEIPFWiQl255aEaBRdlLPQltDbbmQIgFyjItC%2BCdKzr3cmWx4Trn5c5%2FTxYA9mwYs2PsbpRidAqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH%2FJh6PX4LMHPJrp4SrcAz%2FofO7RRLqjtGOlmdC5OYY%2Bc8DhlpLxP9Bb4m5GuGMTbpuGhSSl63TmB3fSscFSMf5Wf3PWY8KAg2EBt0a3Mq%2FERiW0nFl5wlfMZtN4MAcJweQlF12M8exh21rEe7ID9UAV6s7l%2Fzwsc5jHgZrv6ZVv%2BOkqYVo9boaF9INJNsMpddqqeVc6%2BS0ynEBOZKZvHdSfdlgGjLPpeZn6B9ThdphjZOYR4ttXhGnpieVjgY0FctURy4USpQum38FqBk91tDsZBFIcyMIDlOPImAtkzPGwLrTwVyPGKof%2F9bkNq5%2FAiF7U616e0nYwiCr2Nl3NoPDUPju7EhNAq3tQpi4G%2F0kjg3wV4s9MPk3Wncm543c4JPJlIcDavW%2BAA9QZh5UySm6mziG8r51cIYOLHnYB2Kj1%2B5lp4CXTAWfktDKNUEkxxazDIIf%2BBUpQsGUcb1jrykfH2oX0RfZrsudXvxqVR%2Ft1smtxd%2F%2FELzWLZFXKFTvUW3%2BN8bzOunNyn5OJUhHka3wfOOKTI4Iqa42zaZsynjFDUgT4%2FiGCAP5BRm5shSz7e8ggm7KVAjHLq4vNG5cXKUpqgGv1B1cpskzR7I1IsPtulrTM8vByYgIitLhx4emf95N%2BXe67azsBd2ZKMIrekM8GOqUBZ2COkVb%2BEoa5JTJR3ANmDB166LuNwiOLCOSIR%2BC8ser7f1EiBb6jLDdCnLwd5NH%2BTkRk51h7wWtXpCSxSdHUePx5Kze7kcalZgoW%2B9vD6Fq%2BhtWhbwEZoTjQVAEd3cWNNk%2BM8KQX6CNSj9VwyKXqRG7C%2BT8ugIqkjsnE6%2FihoYL7%2B6sqxaV9iTc12v9SEFSlgrCV7UoewOe%2FqlGm98UsEuV1VdcQ&X-Amz-Signature=d751af76d88e26447e8a99d6dda1495a12efe6f9439f45eec1f827a187971389&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

