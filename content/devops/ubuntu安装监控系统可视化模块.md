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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BFKHO42%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKBo4TGxRrnwf57YBCMwWo5%2F8Ik9mv2%2BR%2FZmJTuy%2FBwQIhAM6agogSvY3j%2BMwTkfv7pRq2jOvE%2FLfXiCn0XLf%2FuPuhKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FTG%2B%2BUtTSjVt3ADMq3AOp3%2FRLDMFHbdJnRpneBVwP%2BRwqugzm5OrH9AFu76Ddh2gc1dvYkHVD2qG8kKH%2FOyRnXvQsVLjdixJ8WL9Df8u4tbitM%2FyfY15f5%2BfeMqm5HSNPkUosTvUqubUrVCRy7YJ9Z7K5dGEMz4o8%2FiK4vpQVQkatTO%2FiT2HWjGAlPsa%2BxuXS%2F2igke7AmqgnrQycHX547rKE9qHp%2Bs8IxWSf%2Fd1vbj%2Fhosisos69VPIaBIyveXL%2FSKIgrRsjUdRdelUkx9cfOo3247kib3I0DTGaHrtIx%2F3ZZ1smietNng2ePkw0BS1YZm2Q3V9kRuhtV4aekU5Bi2BtT9ftdWLWk0hXmalIJYZZYLgsH6SeqDMu9m%2Bdr4dw4Bbn1QPMS1JNd%2Fv9VKFY7vd36Q3QQlRSkBfjTj19PO4k8I9y52VAH4zrSh4gZ6cZZdESKo5DLziNrrOaS9UabYMElZVrI%2BZOQzSYNjCKcyHX%2Bt%2BHr711Fv%2BNYoBZP3bmSIpUyfDNZbYGVCmhXKj3WLaXgV80sSftJRiM%2B1R4ePkfK5bLPViX7gWMd8d3MBnB1abHWJdttm5A9eO7a5U6lRZaeCCfQxop%2Bt%2BMgyY6fJ3AUCv6vmKBhuJVx213i2vOzofbky%2BAVRa8GjCc%2B6PJBjqkAeGMxCBUXUIpYcMNn6PVLtkWhFnfN%2Fnpwj3TV2fOfaN%2B%2FpWF8Q27rgSitden8DUU%2B5cMgTMaz2p3d8u906aZz%2BL9gRNyNELU8GqVo5Z6XV98nliYKQ9KfxiGW%2FYMgIyggVgw%2FAW%2FwXC6nNtq6cr1TgODLVXK29FmKlEAOvkllhWT5sTQY7%2Fh%2Be2dUokv1tZSEPwAdSsQJa9%2B3d6Z%2Fglf0zYsed7V&X-Amz-Signature=bf7e179f7894420960d79d87a58794251160d9de6e23c7e2b20a53c13819ea4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BFKHO42%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKBo4TGxRrnwf57YBCMwWo5%2F8Ik9mv2%2BR%2FZmJTuy%2FBwQIhAM6agogSvY3j%2BMwTkfv7pRq2jOvE%2FLfXiCn0XLf%2FuPuhKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FTG%2B%2BUtTSjVt3ADMq3AOp3%2FRLDMFHbdJnRpneBVwP%2BRwqugzm5OrH9AFu76Ddh2gc1dvYkHVD2qG8kKH%2FOyRnXvQsVLjdixJ8WL9Df8u4tbitM%2FyfY15f5%2BfeMqm5HSNPkUosTvUqubUrVCRy7YJ9Z7K5dGEMz4o8%2FiK4vpQVQkatTO%2FiT2HWjGAlPsa%2BxuXS%2F2igke7AmqgnrQycHX547rKE9qHp%2Bs8IxWSf%2Fd1vbj%2Fhosisos69VPIaBIyveXL%2FSKIgrRsjUdRdelUkx9cfOo3247kib3I0DTGaHrtIx%2F3ZZ1smietNng2ePkw0BS1YZm2Q3V9kRuhtV4aekU5Bi2BtT9ftdWLWk0hXmalIJYZZYLgsH6SeqDMu9m%2Bdr4dw4Bbn1QPMS1JNd%2Fv9VKFY7vd36Q3QQlRSkBfjTj19PO4k8I9y52VAH4zrSh4gZ6cZZdESKo5DLziNrrOaS9UabYMElZVrI%2BZOQzSYNjCKcyHX%2Bt%2BHr711Fv%2BNYoBZP3bmSIpUyfDNZbYGVCmhXKj3WLaXgV80sSftJRiM%2B1R4ePkfK5bLPViX7gWMd8d3MBnB1abHWJdttm5A9eO7a5U6lRZaeCCfQxop%2Bt%2BMgyY6fJ3AUCv6vmKBhuJVx213i2vOzofbky%2BAVRa8GjCc%2B6PJBjqkAeGMxCBUXUIpYcMNn6PVLtkWhFnfN%2Fnpwj3TV2fOfaN%2B%2FpWF8Q27rgSitden8DUU%2B5cMgTMaz2p3d8u906aZz%2BL9gRNyNELU8GqVo5Z6XV98nliYKQ9KfxiGW%2FYMgIyggVgw%2FAW%2FwXC6nNtq6cr1TgODLVXK29FmKlEAOvkllhWT5sTQY7%2Fh%2Be2dUokv1tZSEPwAdSsQJa9%2B3d6Z%2Fglf0zYsed7V&X-Amz-Signature=ab7ef8bd1d69b41f2d37fcc8d4e6e24378c75ef43568f18ffb0f21bc604d3621&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BFKHO42%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKBo4TGxRrnwf57YBCMwWo5%2F8Ik9mv2%2BR%2FZmJTuy%2FBwQIhAM6agogSvY3j%2BMwTkfv7pRq2jOvE%2FLfXiCn0XLf%2FuPuhKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FTG%2B%2BUtTSjVt3ADMq3AOp3%2FRLDMFHbdJnRpneBVwP%2BRwqugzm5OrH9AFu76Ddh2gc1dvYkHVD2qG8kKH%2FOyRnXvQsVLjdixJ8WL9Df8u4tbitM%2FyfY15f5%2BfeMqm5HSNPkUosTvUqubUrVCRy7YJ9Z7K5dGEMz4o8%2FiK4vpQVQkatTO%2FiT2HWjGAlPsa%2BxuXS%2F2igke7AmqgnrQycHX547rKE9qHp%2Bs8IxWSf%2Fd1vbj%2Fhosisos69VPIaBIyveXL%2FSKIgrRsjUdRdelUkx9cfOo3247kib3I0DTGaHrtIx%2F3ZZ1smietNng2ePkw0BS1YZm2Q3V9kRuhtV4aekU5Bi2BtT9ftdWLWk0hXmalIJYZZYLgsH6SeqDMu9m%2Bdr4dw4Bbn1QPMS1JNd%2Fv9VKFY7vd36Q3QQlRSkBfjTj19PO4k8I9y52VAH4zrSh4gZ6cZZdESKo5DLziNrrOaS9UabYMElZVrI%2BZOQzSYNjCKcyHX%2Bt%2BHr711Fv%2BNYoBZP3bmSIpUyfDNZbYGVCmhXKj3WLaXgV80sSftJRiM%2B1R4ePkfK5bLPViX7gWMd8d3MBnB1abHWJdttm5A9eO7a5U6lRZaeCCfQxop%2Bt%2BMgyY6fJ3AUCv6vmKBhuJVx213i2vOzofbky%2BAVRa8GjCc%2B6PJBjqkAeGMxCBUXUIpYcMNn6PVLtkWhFnfN%2Fnpwj3TV2fOfaN%2B%2FpWF8Q27rgSitden8DUU%2B5cMgTMaz2p3d8u906aZz%2BL9gRNyNELU8GqVo5Z6XV98nliYKQ9KfxiGW%2FYMgIyggVgw%2FAW%2FwXC6nNtq6cr1TgODLVXK29FmKlEAOvkllhWT5sTQY7%2Fh%2Be2dUokv1tZSEPwAdSsQJa9%2B3d6Z%2Fglf0zYsed7V&X-Amz-Signature=16009dfe23669a1e70fe4397063a91dd0b2e0c4b34c918a4cb655235137ef767&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BFKHO42%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKBo4TGxRrnwf57YBCMwWo5%2F8Ik9mv2%2BR%2FZmJTuy%2FBwQIhAM6agogSvY3j%2BMwTkfv7pRq2jOvE%2FLfXiCn0XLf%2FuPuhKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FTG%2B%2BUtTSjVt3ADMq3AOp3%2FRLDMFHbdJnRpneBVwP%2BRwqugzm5OrH9AFu76Ddh2gc1dvYkHVD2qG8kKH%2FOyRnXvQsVLjdixJ8WL9Df8u4tbitM%2FyfY15f5%2BfeMqm5HSNPkUosTvUqubUrVCRy7YJ9Z7K5dGEMz4o8%2FiK4vpQVQkatTO%2FiT2HWjGAlPsa%2BxuXS%2F2igke7AmqgnrQycHX547rKE9qHp%2Bs8IxWSf%2Fd1vbj%2Fhosisos69VPIaBIyveXL%2FSKIgrRsjUdRdelUkx9cfOo3247kib3I0DTGaHrtIx%2F3ZZ1smietNng2ePkw0BS1YZm2Q3V9kRuhtV4aekU5Bi2BtT9ftdWLWk0hXmalIJYZZYLgsH6SeqDMu9m%2Bdr4dw4Bbn1QPMS1JNd%2Fv9VKFY7vd36Q3QQlRSkBfjTj19PO4k8I9y52VAH4zrSh4gZ6cZZdESKo5DLziNrrOaS9UabYMElZVrI%2BZOQzSYNjCKcyHX%2Bt%2BHr711Fv%2BNYoBZP3bmSIpUyfDNZbYGVCmhXKj3WLaXgV80sSftJRiM%2B1R4ePkfK5bLPViX7gWMd8d3MBnB1abHWJdttm5A9eO7a5U6lRZaeCCfQxop%2Bt%2BMgyY6fJ3AUCv6vmKBhuJVx213i2vOzofbky%2BAVRa8GjCc%2B6PJBjqkAeGMxCBUXUIpYcMNn6PVLtkWhFnfN%2Fnpwj3TV2fOfaN%2B%2FpWF8Q27rgSitden8DUU%2B5cMgTMaz2p3d8u906aZz%2BL9gRNyNELU8GqVo5Z6XV98nliYKQ9KfxiGW%2FYMgIyggVgw%2FAW%2FwXC6nNtq6cr1TgODLVXK29FmKlEAOvkllhWT5sTQY7%2Fh%2Be2dUokv1tZSEPwAdSsQJa9%2B3d6Z%2Fglf0zYsed7V&X-Amz-Signature=8faa15a8f8676a23c4711460a5e5cc5f4584411b687077cc7b41c9d86c3775dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BFKHO42%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKBo4TGxRrnwf57YBCMwWo5%2F8Ik9mv2%2BR%2FZmJTuy%2FBwQIhAM6agogSvY3j%2BMwTkfv7pRq2jOvE%2FLfXiCn0XLf%2FuPuhKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FTG%2B%2BUtTSjVt3ADMq3AOp3%2FRLDMFHbdJnRpneBVwP%2BRwqugzm5OrH9AFu76Ddh2gc1dvYkHVD2qG8kKH%2FOyRnXvQsVLjdixJ8WL9Df8u4tbitM%2FyfY15f5%2BfeMqm5HSNPkUosTvUqubUrVCRy7YJ9Z7K5dGEMz4o8%2FiK4vpQVQkatTO%2FiT2HWjGAlPsa%2BxuXS%2F2igke7AmqgnrQycHX547rKE9qHp%2Bs8IxWSf%2Fd1vbj%2Fhosisos69VPIaBIyveXL%2FSKIgrRsjUdRdelUkx9cfOo3247kib3I0DTGaHrtIx%2F3ZZ1smietNng2ePkw0BS1YZm2Q3V9kRuhtV4aekU5Bi2BtT9ftdWLWk0hXmalIJYZZYLgsH6SeqDMu9m%2Bdr4dw4Bbn1QPMS1JNd%2Fv9VKFY7vd36Q3QQlRSkBfjTj19PO4k8I9y52VAH4zrSh4gZ6cZZdESKo5DLziNrrOaS9UabYMElZVrI%2BZOQzSYNjCKcyHX%2Bt%2BHr711Fv%2BNYoBZP3bmSIpUyfDNZbYGVCmhXKj3WLaXgV80sSftJRiM%2B1R4ePkfK5bLPViX7gWMd8d3MBnB1abHWJdttm5A9eO7a5U6lRZaeCCfQxop%2Bt%2BMgyY6fJ3AUCv6vmKBhuJVx213i2vOzofbky%2BAVRa8GjCc%2B6PJBjqkAeGMxCBUXUIpYcMNn6PVLtkWhFnfN%2Fnpwj3TV2fOfaN%2B%2FpWF8Q27rgSitden8DUU%2B5cMgTMaz2p3d8u906aZz%2BL9gRNyNELU8GqVo5Z6XV98nliYKQ9KfxiGW%2FYMgIyggVgw%2FAW%2FwXC6nNtq6cr1TgODLVXK29FmKlEAOvkllhWT5sTQY7%2Fh%2Be2dUokv1tZSEPwAdSsQJa9%2B3d6Z%2Fglf0zYsed7V&X-Amz-Signature=a5e8490ad5c51e6271d88036d77aa2e6e7cc53d29ace2c7cf26b6399f74e5579&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BFKHO42%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKBo4TGxRrnwf57YBCMwWo5%2F8Ik9mv2%2BR%2FZmJTuy%2FBwQIhAM6agogSvY3j%2BMwTkfv7pRq2jOvE%2FLfXiCn0XLf%2FuPuhKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FTG%2B%2BUtTSjVt3ADMq3AOp3%2FRLDMFHbdJnRpneBVwP%2BRwqugzm5OrH9AFu76Ddh2gc1dvYkHVD2qG8kKH%2FOyRnXvQsVLjdixJ8WL9Df8u4tbitM%2FyfY15f5%2BfeMqm5HSNPkUosTvUqubUrVCRy7YJ9Z7K5dGEMz4o8%2FiK4vpQVQkatTO%2FiT2HWjGAlPsa%2BxuXS%2F2igke7AmqgnrQycHX547rKE9qHp%2Bs8IxWSf%2Fd1vbj%2Fhosisos69VPIaBIyveXL%2FSKIgrRsjUdRdelUkx9cfOo3247kib3I0DTGaHrtIx%2F3ZZ1smietNng2ePkw0BS1YZm2Q3V9kRuhtV4aekU5Bi2BtT9ftdWLWk0hXmalIJYZZYLgsH6SeqDMu9m%2Bdr4dw4Bbn1QPMS1JNd%2Fv9VKFY7vd36Q3QQlRSkBfjTj19PO4k8I9y52VAH4zrSh4gZ6cZZdESKo5DLziNrrOaS9UabYMElZVrI%2BZOQzSYNjCKcyHX%2Bt%2BHr711Fv%2BNYoBZP3bmSIpUyfDNZbYGVCmhXKj3WLaXgV80sSftJRiM%2B1R4ePkfK5bLPViX7gWMd8d3MBnB1abHWJdttm5A9eO7a5U6lRZaeCCfQxop%2Bt%2BMgyY6fJ3AUCv6vmKBhuJVx213i2vOzofbky%2BAVRa8GjCc%2B6PJBjqkAeGMxCBUXUIpYcMNn6PVLtkWhFnfN%2Fnpwj3TV2fOfaN%2B%2FpWF8Q27rgSitden8DUU%2B5cMgTMaz2p3d8u906aZz%2BL9gRNyNELU8GqVo5Z6XV98nliYKQ9KfxiGW%2FYMgIyggVgw%2FAW%2FwXC6nNtq6cr1TgODLVXK29FmKlEAOvkllhWT5sTQY7%2Fh%2Be2dUokv1tZSEPwAdSsQJa9%2B3d6Z%2Fglf0zYsed7V&X-Amz-Signature=7e3cbb92c2123325fb34dc0fcbee708430560eb181e0d720120f2b26cd2e2a15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BFKHO42%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKBo4TGxRrnwf57YBCMwWo5%2F8Ik9mv2%2BR%2FZmJTuy%2FBwQIhAM6agogSvY3j%2BMwTkfv7pRq2jOvE%2FLfXiCn0XLf%2FuPuhKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FTG%2B%2BUtTSjVt3ADMq3AOp3%2FRLDMFHbdJnRpneBVwP%2BRwqugzm5OrH9AFu76Ddh2gc1dvYkHVD2qG8kKH%2FOyRnXvQsVLjdixJ8WL9Df8u4tbitM%2FyfY15f5%2BfeMqm5HSNPkUosTvUqubUrVCRy7YJ9Z7K5dGEMz4o8%2FiK4vpQVQkatTO%2FiT2HWjGAlPsa%2BxuXS%2F2igke7AmqgnrQycHX547rKE9qHp%2Bs8IxWSf%2Fd1vbj%2Fhosisos69VPIaBIyveXL%2FSKIgrRsjUdRdelUkx9cfOo3247kib3I0DTGaHrtIx%2F3ZZ1smietNng2ePkw0BS1YZm2Q3V9kRuhtV4aekU5Bi2BtT9ftdWLWk0hXmalIJYZZYLgsH6SeqDMu9m%2Bdr4dw4Bbn1QPMS1JNd%2Fv9VKFY7vd36Q3QQlRSkBfjTj19PO4k8I9y52VAH4zrSh4gZ6cZZdESKo5DLziNrrOaS9UabYMElZVrI%2BZOQzSYNjCKcyHX%2Bt%2BHr711Fv%2BNYoBZP3bmSIpUyfDNZbYGVCmhXKj3WLaXgV80sSftJRiM%2B1R4ePkfK5bLPViX7gWMd8d3MBnB1abHWJdttm5A9eO7a5U6lRZaeCCfQxop%2Bt%2BMgyY6fJ3AUCv6vmKBhuJVx213i2vOzofbky%2BAVRa8GjCc%2B6PJBjqkAeGMxCBUXUIpYcMNn6PVLtkWhFnfN%2Fnpwj3TV2fOfaN%2B%2FpWF8Q27rgSitden8DUU%2B5cMgTMaz2p3d8u906aZz%2BL9gRNyNELU8GqVo5Z6XV98nliYKQ9KfxiGW%2FYMgIyggVgw%2FAW%2FwXC6nNtq6cr1TgODLVXK29FmKlEAOvkllhWT5sTQY7%2Fh%2Be2dUokv1tZSEPwAdSsQJa9%2B3d6Z%2Fglf0zYsed7V&X-Amz-Signature=de4276270a913fde24a78f33d15aa40ea483d4a716479861677a02d1aa6aa165&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

