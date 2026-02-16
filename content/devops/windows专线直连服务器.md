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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUDWEGHR%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCIvoQPKp9sSxKWSRq5p2zPAHx1Wacj6GQtpCBfoIyhvQIgNIvjo9osqpLOY0pyWWD8PWdbVy4k7SKtbnn0ytgIFPcq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDMsekmxWLFON%2BdJp9yrcA30l79%2FajZWKvYEsS41UKVf%2FBJVBTEy%2FsVSW6lxzQYEvoQiDNL04Rjcm62SqU8QBCIXteTWRV%2FChUREq83fLQtkfeT0kl2T6ki9fp73v4ZwhifF9O%2F9dZPfgjDOkD2qrpaJgzKiZdTQsoAuIxk5wFDMq12I4kQAhGWowEkIz4%2FBwEvwwHBVZyaOumdPzPjb5VX1w8XuiamebfjLzBYVMsQYDgukTv6ckMXMPONYPC4hpwd5jTMgoA1l6jKxQYIxRjYdft91nuPw%2B0jQdS%2Fvn0a3wlZu9UUkXYl777OJpT3gcC4Zvgqf3T%2FBZQPuXrK75%2FN4R%2F3SbCgFyqDSiToHskL32WXcbzY803IJnw3%2BDHfHrSaQxD0JP86wGnpxP1qah5mMO0MAklD%2BV88wvJ9V8uMS%2BoMtWyCv5PyoYFFrQxD%2BlYedVVry7O1RdGcH2MR7TBE4CqqFXykLDofRgYfeTPVsnFXH9GlH7x1Pac0TwSbER1okaRn1sLdDL6uOdlqCTNT0nWttulh%2Bf6%2BQlCIYo0X65qx9ReuvtYz0o3UNvSSTzw2IOahqwDv3s6kk3hZ3nAsDTyqBoOyCQuGeYih1FqJcYR2DGN6qHRGddbtAe%2FKobbKz5UdRf0qTOmc3eMOiUyswGOqUB27Oc39%2FPzQiir%2B%2FzvI38nWwsxSGCNEc9ib67prhAz3T2wosnYEEIDHgIikxvIc8NekZ3gv5kloTqttZvBsKb%2Fkl8%2B6kLp8C3nT1B%2BA01A0ZJxTadJQ%2F%2FXnQuefF5c4yxm6XvtL8WZp8%2FBli2WE3TYyhOeYH7aqAvbRWcY3Qi%2FkHxgpVHKaIqe%2FIAqH41uji6WZf3TDRoNYovqiulnwh%2BBGjhJ5jo&X-Amz-Signature=30ca3334462487eb2337a96bcf9be6ce195af4b74cc8ebc8bb66bbcbca3b21d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

