---
title: Ubuntu安装监控系统可视化模块
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-20T03:10:00.000Z'
draft: false
tags:
- Linux
- Ubuntu
categories:
- DevOps
---

Prometheus是一个开放性的监控解决方案，用户可以非常方便的安装和使用Prometheus并且能够非常方便的对其进行扩展。为了能够更加直观的了解Prometheus Server，接下来我们将在本地部署并运行一个Prometheus Server实例，通过Node Exporter采集当前主机的系统资源使用情况。 并通过Grafana创建一个简单的可视化仪表盘。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664APDZPIL%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIFWIojTR0%2FDWe2QM%2B5E40A9RI%2BC9eqR6Z57qknxT2EOgAiAzOm29dbJT737d6PWssd2z0dreqMyr4Jy%2F6Nv%2FAHmp2SqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIJXdHbQaePv5oXERKtwDX%2F9aFzRfBpZP4Q28%2BegRYXY%2BMJu07dDcoT5a5QlcnjPf3pGyRPg2oSLBh1diwner937CTW%2B5cxhAdoyB26R8khEM1kEzPLDmTmwQnhzAKPF371YvXGEJlprBvX2JDSvCYiN8bkMr7aqJEcsul%2F4Uln29z8AZT1Lz6VaLvmxG7fnXGh4WZATTaU9sEI%2B48i8LboODkxr%2B%2FCtX38ygj6z8Nh6qvRzqprPA%2FIP15oseIhiKl%2FuSgNdxpQ8q52jUfzHlG4QIIs%2B0lFH4PFOEJsvpXWEXUoHTKRXIw%2BiFXr0U01R7hGjTwYGI9DW2ITNJ1qRwYAHaHL2yPsC0ytonYrMmyGom8Oqhh4gtoyDb3lrbob4cA5SM7e44wVUS4rx0kNf7qHjHUjJWFUj0h3Im2CExYB2djL9czY3AAss08xpYfyLEFG75hUDkcOBiGBjHhF408d%2F0%2F3m0Pv1MO7Y1ff1K8zcBeYdGcvkyxugf7hct3%2BugC7TAFWJY74VBN7fma1tWadt99j%2BKnH68YL%2FIFa1Ivy9VKPCBi5%2BVK7BlZwnw7W10%2F%2B78P9B9RBm0RP9ZUHapjtg9pkTvojsfMZ8cifDXRVfQiLpoEWj0LsMAJ9dHvuOgU7BYo7z2CSZfxH0wkru6zAY6pgGOc4oLba194PRSemWU%2Bgj%2FqY%2FMAtVergsIkH0Hm3F4PTij2%2FC2V67zBOQ3AsDUGfQCpBGZqys3IduY8foqcMaxveiceC57iEPj5UGSQwPLS%2Bh3blKECr26L5GbDGxVIGDb1e57AMGlHyti%2BzNyk5HINPFh7INGXgru3TLkuA9Er7hwL%2Bf1SphSf4WEdvrYS2gkCDdiTcYbnqGOWcY26Mb6%2BkOXaTHl&X-Amz-Signature=77393a1b69f24e14f8a8bb95246cfd588f7259c023c5c453bc8af59de67b411c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> Prometheus是什么？

### 下载Prometheus

- 下载链接
### 安装Prometheus

- 解压
### 修改Prometheus配置

- 进入文件目标, 并修改配置
- 将以下内容放置在配置文件内
- 启动服务
### 在web浏览器查看

- localhost:9090
---

> Monitoring Linux host metrics with the Node Exporter

### 下载Node Exporter

- 下载地址
### 安装 & RUN

```shell
tar xvfz node_exporter-*.*-amd64.tar.gz
cd node_exporter-*.*-amd64
./node_exporter
```

### 在web浏览器查看

- http://localhost:9100/
---

> What is Grafana

### 安装Grafana

### Ubuntu安装流程

```shell
# 更新apt-getsudo apt-get install -y adduser libfontconfig1 musl
# 下载软件wget https://dl.grafana.com/enterprise/release/grafana-enterprise_10.0.0_amd64.deb
# 安装sudo dpkg -i grafana-enterprise_10.0.0_amd64.deb
```

- 操作系统不是Ubuntu则查看上面的链接, 根据自身系统进行安装
### RUN Grafana

- 运行Grafana可视化服务
```shell
sudo /bin/systemctl start grafana-server
```

### 在web浏览器查看

- http://localhost:3000/
- 设置流程如下:
step-1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664APDZPIL%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIFWIojTR0%2FDWe2QM%2B5E40A9RI%2BC9eqR6Z57qknxT2EOgAiAzOm29dbJT737d6PWssd2z0dreqMyr4Jy%2F6Nv%2FAHmp2SqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIJXdHbQaePv5oXERKtwDX%2F9aFzRfBpZP4Q28%2BegRYXY%2BMJu07dDcoT5a5QlcnjPf3pGyRPg2oSLBh1diwner937CTW%2B5cxhAdoyB26R8khEM1kEzPLDmTmwQnhzAKPF371YvXGEJlprBvX2JDSvCYiN8bkMr7aqJEcsul%2F4Uln29z8AZT1Lz6VaLvmxG7fnXGh4WZATTaU9sEI%2B48i8LboODkxr%2B%2FCtX38ygj6z8Nh6qvRzqprPA%2FIP15oseIhiKl%2FuSgNdxpQ8q52jUfzHlG4QIIs%2B0lFH4PFOEJsvpXWEXUoHTKRXIw%2BiFXr0U01R7hGjTwYGI9DW2ITNJ1qRwYAHaHL2yPsC0ytonYrMmyGom8Oqhh4gtoyDb3lrbob4cA5SM7e44wVUS4rx0kNf7qHjHUjJWFUj0h3Im2CExYB2djL9czY3AAss08xpYfyLEFG75hUDkcOBiGBjHhF408d%2F0%2F3m0Pv1MO7Y1ff1K8zcBeYdGcvkyxugf7hct3%2BugC7TAFWJY74VBN7fma1tWadt99j%2BKnH68YL%2FIFa1Ivy9VKPCBi5%2BVK7BlZwnw7W10%2F%2B78P9B9RBm0RP9ZUHapjtg9pkTvojsfMZ8cifDXRVfQiLpoEWj0LsMAJ9dHvuOgU7BYo7z2CSZfxH0wkru6zAY6pgGOc4oLba194PRSemWU%2Bgj%2FqY%2FMAtVergsIkH0Hm3F4PTij2%2FC2V67zBOQ3AsDUGfQCpBGZqys3IduY8foqcMaxveiceC57iEPj5UGSQwPLS%2Bh3blKECr26L5GbDGxVIGDb1e57AMGlHyti%2BzNyk5HINPFh7INGXgru3TLkuA9Er7hwL%2Bf1SphSf4WEdvrYS2gkCDdiTcYbnqGOWcY26Mb6%2BkOXaTHl&X-Amz-Signature=5f1d86e69233b8513dad0f33bd34b57b54385c59d7e21e326acc2a264d7527d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664APDZPIL%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIFWIojTR0%2FDWe2QM%2B5E40A9RI%2BC9eqR6Z57qknxT2EOgAiAzOm29dbJT737d6PWssd2z0dreqMyr4Jy%2F6Nv%2FAHmp2SqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIJXdHbQaePv5oXERKtwDX%2F9aFzRfBpZP4Q28%2BegRYXY%2BMJu07dDcoT5a5QlcnjPf3pGyRPg2oSLBh1diwner937CTW%2B5cxhAdoyB26R8khEM1kEzPLDmTmwQnhzAKPF371YvXGEJlprBvX2JDSvCYiN8bkMr7aqJEcsul%2F4Uln29z8AZT1Lz6VaLvmxG7fnXGh4WZATTaU9sEI%2B48i8LboODkxr%2B%2FCtX38ygj6z8Nh6qvRzqprPA%2FIP15oseIhiKl%2FuSgNdxpQ8q52jUfzHlG4QIIs%2B0lFH4PFOEJsvpXWEXUoHTKRXIw%2BiFXr0U01R7hGjTwYGI9DW2ITNJ1qRwYAHaHL2yPsC0ytonYrMmyGom8Oqhh4gtoyDb3lrbob4cA5SM7e44wVUS4rx0kNf7qHjHUjJWFUj0h3Im2CExYB2djL9czY3AAss08xpYfyLEFG75hUDkcOBiGBjHhF408d%2F0%2F3m0Pv1MO7Y1ff1K8zcBeYdGcvkyxugf7hct3%2BugC7TAFWJY74VBN7fma1tWadt99j%2BKnH68YL%2FIFa1Ivy9VKPCBi5%2BVK7BlZwnw7W10%2F%2B78P9B9RBm0RP9ZUHapjtg9pkTvojsfMZ8cifDXRVfQiLpoEWj0LsMAJ9dHvuOgU7BYo7z2CSZfxH0wkru6zAY6pgGOc4oLba194PRSemWU%2Bgj%2FqY%2FMAtVergsIkH0Hm3F4PTij2%2FC2V67zBOQ3AsDUGfQCpBGZqys3IduY8foqcMaxveiceC57iEPj5UGSQwPLS%2Bh3blKECr26L5GbDGxVIGDb1e57AMGlHyti%2BzNyk5HINPFh7INGXgru3TLkuA9Er7hwL%2Bf1SphSf4WEdvrYS2gkCDdiTcYbnqGOWcY26Mb6%2BkOXaTHl&X-Amz-Signature=1148aa414dbccbd309d0b57b1a99ec5336bd93742a016a3039bbd2c0c5db26c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664APDZPIL%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIFWIojTR0%2FDWe2QM%2B5E40A9RI%2BC9eqR6Z57qknxT2EOgAiAzOm29dbJT737d6PWssd2z0dreqMyr4Jy%2F6Nv%2FAHmp2SqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIJXdHbQaePv5oXERKtwDX%2F9aFzRfBpZP4Q28%2BegRYXY%2BMJu07dDcoT5a5QlcnjPf3pGyRPg2oSLBh1diwner937CTW%2B5cxhAdoyB26R8khEM1kEzPLDmTmwQnhzAKPF371YvXGEJlprBvX2JDSvCYiN8bkMr7aqJEcsul%2F4Uln29z8AZT1Lz6VaLvmxG7fnXGh4WZATTaU9sEI%2B48i8LboODkxr%2B%2FCtX38ygj6z8Nh6qvRzqprPA%2FIP15oseIhiKl%2FuSgNdxpQ8q52jUfzHlG4QIIs%2B0lFH4PFOEJsvpXWEXUoHTKRXIw%2BiFXr0U01R7hGjTwYGI9DW2ITNJ1qRwYAHaHL2yPsC0ytonYrMmyGom8Oqhh4gtoyDb3lrbob4cA5SM7e44wVUS4rx0kNf7qHjHUjJWFUj0h3Im2CExYB2djL9czY3AAss08xpYfyLEFG75hUDkcOBiGBjHhF408d%2F0%2F3m0Pv1MO7Y1ff1K8zcBeYdGcvkyxugf7hct3%2BugC7TAFWJY74VBN7fma1tWadt99j%2BKnH68YL%2FIFa1Ivy9VKPCBi5%2BVK7BlZwnw7W10%2F%2B78P9B9RBm0RP9ZUHapjtg9pkTvojsfMZ8cifDXRVfQiLpoEWj0LsMAJ9dHvuOgU7BYo7z2CSZfxH0wkru6zAY6pgGOc4oLba194PRSemWU%2Bgj%2FqY%2FMAtVergsIkH0Hm3F4PTij2%2FC2V67zBOQ3AsDUGfQCpBGZqys3IduY8foqcMaxveiceC57iEPj5UGSQwPLS%2Bh3blKECr26L5GbDGxVIGDb1e57AMGlHyti%2BzNyk5HINPFh7INGXgru3TLkuA9Er7hwL%2Bf1SphSf4WEdvrYS2gkCDdiTcYbnqGOWcY26Mb6%2BkOXaTHl&X-Amz-Signature=db5e66d7ed92dfdcba40acbb603c2bad4befe4d25aedb67145d69136a0c5172e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664APDZPIL%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIFWIojTR0%2FDWe2QM%2B5E40A9RI%2BC9eqR6Z57qknxT2EOgAiAzOm29dbJT737d6PWssd2z0dreqMyr4Jy%2F6Nv%2FAHmp2SqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIJXdHbQaePv5oXERKtwDX%2F9aFzRfBpZP4Q28%2BegRYXY%2BMJu07dDcoT5a5QlcnjPf3pGyRPg2oSLBh1diwner937CTW%2B5cxhAdoyB26R8khEM1kEzPLDmTmwQnhzAKPF371YvXGEJlprBvX2JDSvCYiN8bkMr7aqJEcsul%2F4Uln29z8AZT1Lz6VaLvmxG7fnXGh4WZATTaU9sEI%2B48i8LboODkxr%2B%2FCtX38ygj6z8Nh6qvRzqprPA%2FIP15oseIhiKl%2FuSgNdxpQ8q52jUfzHlG4QIIs%2B0lFH4PFOEJsvpXWEXUoHTKRXIw%2BiFXr0U01R7hGjTwYGI9DW2ITNJ1qRwYAHaHL2yPsC0ytonYrMmyGom8Oqhh4gtoyDb3lrbob4cA5SM7e44wVUS4rx0kNf7qHjHUjJWFUj0h3Im2CExYB2djL9czY3AAss08xpYfyLEFG75hUDkcOBiGBjHhF408d%2F0%2F3m0Pv1MO7Y1ff1K8zcBeYdGcvkyxugf7hct3%2BugC7TAFWJY74VBN7fma1tWadt99j%2BKnH68YL%2FIFa1Ivy9VKPCBi5%2BVK7BlZwnw7W10%2F%2B78P9B9RBm0RP9ZUHapjtg9pkTvojsfMZ8cifDXRVfQiLpoEWj0LsMAJ9dHvuOgU7BYo7z2CSZfxH0wkru6zAY6pgGOc4oLba194PRSemWU%2Bgj%2FqY%2FMAtVergsIkH0Hm3F4PTij2%2FC2V67zBOQ3AsDUGfQCpBGZqys3IduY8foqcMaxveiceC57iEPj5UGSQwPLS%2Bh3blKECr26L5GbDGxVIGDb1e57AMGlHyti%2BzNyk5HINPFh7INGXgru3TLkuA9Er7hwL%2Bf1SphSf4WEdvrYS2gkCDdiTcYbnqGOWcY26Mb6%2BkOXaTHl&X-Amz-Signature=3408f5621d5d784cda95f5a481be6caa9cebd1c6efe2572f8f82a41fec3302f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664APDZPIL%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIFWIojTR0%2FDWe2QM%2B5E40A9RI%2BC9eqR6Z57qknxT2EOgAiAzOm29dbJT737d6PWssd2z0dreqMyr4Jy%2F6Nv%2FAHmp2SqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIJXdHbQaePv5oXERKtwDX%2F9aFzRfBpZP4Q28%2BegRYXY%2BMJu07dDcoT5a5QlcnjPf3pGyRPg2oSLBh1diwner937CTW%2B5cxhAdoyB26R8khEM1kEzPLDmTmwQnhzAKPF371YvXGEJlprBvX2JDSvCYiN8bkMr7aqJEcsul%2F4Uln29z8AZT1Lz6VaLvmxG7fnXGh4WZATTaU9sEI%2B48i8LboODkxr%2B%2FCtX38ygj6z8Nh6qvRzqprPA%2FIP15oseIhiKl%2FuSgNdxpQ8q52jUfzHlG4QIIs%2B0lFH4PFOEJsvpXWEXUoHTKRXIw%2BiFXr0U01R7hGjTwYGI9DW2ITNJ1qRwYAHaHL2yPsC0ytonYrMmyGom8Oqhh4gtoyDb3lrbob4cA5SM7e44wVUS4rx0kNf7qHjHUjJWFUj0h3Im2CExYB2djL9czY3AAss08xpYfyLEFG75hUDkcOBiGBjHhF408d%2F0%2F3m0Pv1MO7Y1ff1K8zcBeYdGcvkyxugf7hct3%2BugC7TAFWJY74VBN7fma1tWadt99j%2BKnH68YL%2FIFa1Ivy9VKPCBi5%2BVK7BlZwnw7W10%2F%2B78P9B9RBm0RP9ZUHapjtg9pkTvojsfMZ8cifDXRVfQiLpoEWj0LsMAJ9dHvuOgU7BYo7z2CSZfxH0wkru6zAY6pgGOc4oLba194PRSemWU%2Bgj%2FqY%2FMAtVergsIkH0Hm3F4PTij2%2FC2V67zBOQ3AsDUGfQCpBGZqys3IduY8foqcMaxveiceC57iEPj5UGSQwPLS%2Bh3blKECr26L5GbDGxVIGDb1e57AMGlHyti%2BzNyk5HINPFh7INGXgru3TLkuA9Er7hwL%2Bf1SphSf4WEdvrYS2gkCDdiTcYbnqGOWcY26Mb6%2BkOXaTHl&X-Amz-Signature=cc865e9ffddf7194b77be339db986762e06df54b47769484f9c1f6ccb79d3926&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664APDZPIL%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIFWIojTR0%2FDWe2QM%2B5E40A9RI%2BC9eqR6Z57qknxT2EOgAiAzOm29dbJT737d6PWssd2z0dreqMyr4Jy%2F6Nv%2FAHmp2SqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIJXdHbQaePv5oXERKtwDX%2F9aFzRfBpZP4Q28%2BegRYXY%2BMJu07dDcoT5a5QlcnjPf3pGyRPg2oSLBh1diwner937CTW%2B5cxhAdoyB26R8khEM1kEzPLDmTmwQnhzAKPF371YvXGEJlprBvX2JDSvCYiN8bkMr7aqJEcsul%2F4Uln29z8AZT1Lz6VaLvmxG7fnXGh4WZATTaU9sEI%2B48i8LboODkxr%2B%2FCtX38ygj6z8Nh6qvRzqprPA%2FIP15oseIhiKl%2FuSgNdxpQ8q52jUfzHlG4QIIs%2B0lFH4PFOEJsvpXWEXUoHTKRXIw%2BiFXr0U01R7hGjTwYGI9DW2ITNJ1qRwYAHaHL2yPsC0ytonYrMmyGom8Oqhh4gtoyDb3lrbob4cA5SM7e44wVUS4rx0kNf7qHjHUjJWFUj0h3Im2CExYB2djL9czY3AAss08xpYfyLEFG75hUDkcOBiGBjHhF408d%2F0%2F3m0Pv1MO7Y1ff1K8zcBeYdGcvkyxugf7hct3%2BugC7TAFWJY74VBN7fma1tWadt99j%2BKnH68YL%2FIFa1Ivy9VKPCBi5%2BVK7BlZwnw7W10%2F%2B78P9B9RBm0RP9ZUHapjtg9pkTvojsfMZ8cifDXRVfQiLpoEWj0LsMAJ9dHvuOgU7BYo7z2CSZfxH0wkru6zAY6pgGOc4oLba194PRSemWU%2Bgj%2FqY%2FMAtVergsIkH0Hm3F4PTij2%2FC2V67zBOQ3AsDUGfQCpBGZqys3IduY8foqcMaxveiceC57iEPj5UGSQwPLS%2Bh3blKECr26L5GbDGxVIGDb1e57AMGlHyti%2BzNyk5HINPFh7INGXgru3TLkuA9Er7hwL%2Bf1SphSf4WEdvrYS2gkCDdiTcYbnqGOWcY26Mb6%2BkOXaTHl&X-Amz-Signature=ae29f99295dac8eef7d7f0db1b4487422700617e0a3808607470bc510e3523b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> 参考链接

### 拓展代码

- 安装Prometheus
```shell
# 下载export VERSION=2.13.0
curl -LO  https://github.com/prometheus/prometheus/releases/download/v$VERSION/prometheus-$VERSION.darwin-amd64.tar.gz
# 解压tar -xzf prometheus-${VERSION}.darwin-amd64.tar.gz
cd prometheus-${VERSION}.darwin-amd64
# 配置promethes.ymlvim promethes.yml
# 运行./prometheus
```

- 安装Node Exporter
```shell
# 下载curl -OL https://github.com/prometheus/node_exporter/releases/download/v0.17.0/node_exporter-0.17.0.linux-amd64.tar.gz
# 解压tar -xzf node_exporter-0.17.0.linux-amd64.tar.gz
# 将 node_exporter 工具安装到系统中，使其可以被全局访问和使用。cd node_exporter-0.17.0.linux-amd64/
mv node_exporter /usr/local/bin/
# 运行service node_exporter start
```

