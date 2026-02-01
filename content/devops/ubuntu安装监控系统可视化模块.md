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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCIZVRU%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFL4aGhej0yNwUj4RexSi1zItPJhT7IM8tF5EicLNGkIAiAan4V5BT8MqePJsNjiJPl3MT2b3aYPXehipA5MZ95tNiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMD10EZGV36jTvbULWKtwDEgxArdKCLsarzqzpxHvt%2Bv8YKRhaywDN8ZZsvTNF0zVUG2d9CCOJwcqKOPXMEvq%2BqNKYBb5%2FXIaJw0%2FOrESow6Q6ro%2Br0AfcI6HXBFdO48cG1C%2Flt%2FOr7zKH8qub5bmWtrgQVVscc88X3ZRI88XETaIyWEj0vErTbC6ZM5%2BZU5TtVvWXm2K017WS%2BYUBEemO4hw0YktOQAW7qDUEhIH1OtLmqENfW%2FjxMy5zXZXSJw0s8Y9ISlUhxSyyXVJD44xfYinLxYG7e%2BQUnIfY1Ws2hbf%2FySkRcJafWLHAghM2BMvp4K%2Ff9HNeg6Vj4s%2BM%2BkshsXF1qXpm8H1NTSNu2SX8HLAb49hKabuDCShXfdId16ib8%2FsJ5QRaalqH77XFakWNyvBkbx6WvJ3KvRIG2J5okz57sbC0bSeHN%2BnVvQLB7Rq2xxAkUBD0aEIK3uYZvxtKncZPi9TuWQ8V%2FHrneeCH7tZyj9eTocEmU22wOE5iU%2FSGx4iYOFB22UjZye7jL%2BZYF2RtI%2Bo59bZrTXAPf7bTMdK%2F%2BvR7tuBVxn3TP%2BmdE904DrloelHULa7b1idECSg5V%2BCr3wCp4reuDnhqDfaUrDGrRUXzJjf%2B48s8QbcLvyqzi5xW%2BNHzhI%2B24tYwrZL7ywY6pgGPv1RWQihs1UFUGDQqPiWw8tprT5t6wMiIFsZLi9GAZTizjh1mip1VIlOdP8D2zXR3V5YMzmd1CgjSUQB0WY9FTp0MbA9Yzal2DvIIMrobH94olEx5qYXv%2B60SIQa8AyWS5AAfiDc6dnxgR0OEjj4RO6YufedtOZIYegL80dd71SGi6nht0ppeCKpBI8QBrNE8zCtjP2Sm7Xq04kaBvG7aPa%2B%2FAKyU&X-Amz-Signature=df8d9345e577dce3941f46c3ffeaee5ed20726d97b9a318f917e9c0107b51a85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCIZVRU%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFL4aGhej0yNwUj4RexSi1zItPJhT7IM8tF5EicLNGkIAiAan4V5BT8MqePJsNjiJPl3MT2b3aYPXehipA5MZ95tNiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMD10EZGV36jTvbULWKtwDEgxArdKCLsarzqzpxHvt%2Bv8YKRhaywDN8ZZsvTNF0zVUG2d9CCOJwcqKOPXMEvq%2BqNKYBb5%2FXIaJw0%2FOrESow6Q6ro%2Br0AfcI6HXBFdO48cG1C%2Flt%2FOr7zKH8qub5bmWtrgQVVscc88X3ZRI88XETaIyWEj0vErTbC6ZM5%2BZU5TtVvWXm2K017WS%2BYUBEemO4hw0YktOQAW7qDUEhIH1OtLmqENfW%2FjxMy5zXZXSJw0s8Y9ISlUhxSyyXVJD44xfYinLxYG7e%2BQUnIfY1Ws2hbf%2FySkRcJafWLHAghM2BMvp4K%2Ff9HNeg6Vj4s%2BM%2BkshsXF1qXpm8H1NTSNu2SX8HLAb49hKabuDCShXfdId16ib8%2FsJ5QRaalqH77XFakWNyvBkbx6WvJ3KvRIG2J5okz57sbC0bSeHN%2BnVvQLB7Rq2xxAkUBD0aEIK3uYZvxtKncZPi9TuWQ8V%2FHrneeCH7tZyj9eTocEmU22wOE5iU%2FSGx4iYOFB22UjZye7jL%2BZYF2RtI%2Bo59bZrTXAPf7bTMdK%2F%2BvR7tuBVxn3TP%2BmdE904DrloelHULa7b1idECSg5V%2BCr3wCp4reuDnhqDfaUrDGrRUXzJjf%2B48s8QbcLvyqzi5xW%2BNHzhI%2B24tYwrZL7ywY6pgGPv1RWQihs1UFUGDQqPiWw8tprT5t6wMiIFsZLi9GAZTizjh1mip1VIlOdP8D2zXR3V5YMzmd1CgjSUQB0WY9FTp0MbA9Yzal2DvIIMrobH94olEx5qYXv%2B60SIQa8AyWS5AAfiDc6dnxgR0OEjj4RO6YufedtOZIYegL80dd71SGi6nht0ppeCKpBI8QBrNE8zCtjP2Sm7Xq04kaBvG7aPa%2B%2FAKyU&X-Amz-Signature=d7f77593bb4041ebd35572c94224c83ace894a23d6b61195f7ca3ebb0fab2764&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCIZVRU%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFL4aGhej0yNwUj4RexSi1zItPJhT7IM8tF5EicLNGkIAiAan4V5BT8MqePJsNjiJPl3MT2b3aYPXehipA5MZ95tNiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMD10EZGV36jTvbULWKtwDEgxArdKCLsarzqzpxHvt%2Bv8YKRhaywDN8ZZsvTNF0zVUG2d9CCOJwcqKOPXMEvq%2BqNKYBb5%2FXIaJw0%2FOrESow6Q6ro%2Br0AfcI6HXBFdO48cG1C%2Flt%2FOr7zKH8qub5bmWtrgQVVscc88X3ZRI88XETaIyWEj0vErTbC6ZM5%2BZU5TtVvWXm2K017WS%2BYUBEemO4hw0YktOQAW7qDUEhIH1OtLmqENfW%2FjxMy5zXZXSJw0s8Y9ISlUhxSyyXVJD44xfYinLxYG7e%2BQUnIfY1Ws2hbf%2FySkRcJafWLHAghM2BMvp4K%2Ff9HNeg6Vj4s%2BM%2BkshsXF1qXpm8H1NTSNu2SX8HLAb49hKabuDCShXfdId16ib8%2FsJ5QRaalqH77XFakWNyvBkbx6WvJ3KvRIG2J5okz57sbC0bSeHN%2BnVvQLB7Rq2xxAkUBD0aEIK3uYZvxtKncZPi9TuWQ8V%2FHrneeCH7tZyj9eTocEmU22wOE5iU%2FSGx4iYOFB22UjZye7jL%2BZYF2RtI%2Bo59bZrTXAPf7bTMdK%2F%2BvR7tuBVxn3TP%2BmdE904DrloelHULa7b1idECSg5V%2BCr3wCp4reuDnhqDfaUrDGrRUXzJjf%2B48s8QbcLvyqzi5xW%2BNHzhI%2B24tYwrZL7ywY6pgGPv1RWQihs1UFUGDQqPiWw8tprT5t6wMiIFsZLi9GAZTizjh1mip1VIlOdP8D2zXR3V5YMzmd1CgjSUQB0WY9FTp0MbA9Yzal2DvIIMrobH94olEx5qYXv%2B60SIQa8AyWS5AAfiDc6dnxgR0OEjj4RO6YufedtOZIYegL80dd71SGi6nht0ppeCKpBI8QBrNE8zCtjP2Sm7Xq04kaBvG7aPa%2B%2FAKyU&X-Amz-Signature=7c3a084b88fec57aa811de4419a2bf88c1a21d065289638451766de89770a926&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCIZVRU%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFL4aGhej0yNwUj4RexSi1zItPJhT7IM8tF5EicLNGkIAiAan4V5BT8MqePJsNjiJPl3MT2b3aYPXehipA5MZ95tNiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMD10EZGV36jTvbULWKtwDEgxArdKCLsarzqzpxHvt%2Bv8YKRhaywDN8ZZsvTNF0zVUG2d9CCOJwcqKOPXMEvq%2BqNKYBb5%2FXIaJw0%2FOrESow6Q6ro%2Br0AfcI6HXBFdO48cG1C%2Flt%2FOr7zKH8qub5bmWtrgQVVscc88X3ZRI88XETaIyWEj0vErTbC6ZM5%2BZU5TtVvWXm2K017WS%2BYUBEemO4hw0YktOQAW7qDUEhIH1OtLmqENfW%2FjxMy5zXZXSJw0s8Y9ISlUhxSyyXVJD44xfYinLxYG7e%2BQUnIfY1Ws2hbf%2FySkRcJafWLHAghM2BMvp4K%2Ff9HNeg6Vj4s%2BM%2BkshsXF1qXpm8H1NTSNu2SX8HLAb49hKabuDCShXfdId16ib8%2FsJ5QRaalqH77XFakWNyvBkbx6WvJ3KvRIG2J5okz57sbC0bSeHN%2BnVvQLB7Rq2xxAkUBD0aEIK3uYZvxtKncZPi9TuWQ8V%2FHrneeCH7tZyj9eTocEmU22wOE5iU%2FSGx4iYOFB22UjZye7jL%2BZYF2RtI%2Bo59bZrTXAPf7bTMdK%2F%2BvR7tuBVxn3TP%2BmdE904DrloelHULa7b1idECSg5V%2BCr3wCp4reuDnhqDfaUrDGrRUXzJjf%2B48s8QbcLvyqzi5xW%2BNHzhI%2B24tYwrZL7ywY6pgGPv1RWQihs1UFUGDQqPiWw8tprT5t6wMiIFsZLi9GAZTizjh1mip1VIlOdP8D2zXR3V5YMzmd1CgjSUQB0WY9FTp0MbA9Yzal2DvIIMrobH94olEx5qYXv%2B60SIQa8AyWS5AAfiDc6dnxgR0OEjj4RO6YufedtOZIYegL80dd71SGi6nht0ppeCKpBI8QBrNE8zCtjP2Sm7Xq04kaBvG7aPa%2B%2FAKyU&X-Amz-Signature=2a11e46f5f44f1be7d553161f491c3f2e2b2dfa7a1e770c67454eb2766d2355e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCIZVRU%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFL4aGhej0yNwUj4RexSi1zItPJhT7IM8tF5EicLNGkIAiAan4V5BT8MqePJsNjiJPl3MT2b3aYPXehipA5MZ95tNiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMD10EZGV36jTvbULWKtwDEgxArdKCLsarzqzpxHvt%2Bv8YKRhaywDN8ZZsvTNF0zVUG2d9CCOJwcqKOPXMEvq%2BqNKYBb5%2FXIaJw0%2FOrESow6Q6ro%2Br0AfcI6HXBFdO48cG1C%2Flt%2FOr7zKH8qub5bmWtrgQVVscc88X3ZRI88XETaIyWEj0vErTbC6ZM5%2BZU5TtVvWXm2K017WS%2BYUBEemO4hw0YktOQAW7qDUEhIH1OtLmqENfW%2FjxMy5zXZXSJw0s8Y9ISlUhxSyyXVJD44xfYinLxYG7e%2BQUnIfY1Ws2hbf%2FySkRcJafWLHAghM2BMvp4K%2Ff9HNeg6Vj4s%2BM%2BkshsXF1qXpm8H1NTSNu2SX8HLAb49hKabuDCShXfdId16ib8%2FsJ5QRaalqH77XFakWNyvBkbx6WvJ3KvRIG2J5okz57sbC0bSeHN%2BnVvQLB7Rq2xxAkUBD0aEIK3uYZvxtKncZPi9TuWQ8V%2FHrneeCH7tZyj9eTocEmU22wOE5iU%2FSGx4iYOFB22UjZye7jL%2BZYF2RtI%2Bo59bZrTXAPf7bTMdK%2F%2BvR7tuBVxn3TP%2BmdE904DrloelHULa7b1idECSg5V%2BCr3wCp4reuDnhqDfaUrDGrRUXzJjf%2B48s8QbcLvyqzi5xW%2BNHzhI%2B24tYwrZL7ywY6pgGPv1RWQihs1UFUGDQqPiWw8tprT5t6wMiIFsZLi9GAZTizjh1mip1VIlOdP8D2zXR3V5YMzmd1CgjSUQB0WY9FTp0MbA9Yzal2DvIIMrobH94olEx5qYXv%2B60SIQa8AyWS5AAfiDc6dnxgR0OEjj4RO6YufedtOZIYegL80dd71SGi6nht0ppeCKpBI8QBrNE8zCtjP2Sm7Xq04kaBvG7aPa%2B%2FAKyU&X-Amz-Signature=989e1ea657b841a06047ef25bba6d30262cf6204854bc26f93c0ef191be030cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCIZVRU%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFL4aGhej0yNwUj4RexSi1zItPJhT7IM8tF5EicLNGkIAiAan4V5BT8MqePJsNjiJPl3MT2b3aYPXehipA5MZ95tNiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMD10EZGV36jTvbULWKtwDEgxArdKCLsarzqzpxHvt%2Bv8YKRhaywDN8ZZsvTNF0zVUG2d9CCOJwcqKOPXMEvq%2BqNKYBb5%2FXIaJw0%2FOrESow6Q6ro%2Br0AfcI6HXBFdO48cG1C%2Flt%2FOr7zKH8qub5bmWtrgQVVscc88X3ZRI88XETaIyWEj0vErTbC6ZM5%2BZU5TtVvWXm2K017WS%2BYUBEemO4hw0YktOQAW7qDUEhIH1OtLmqENfW%2FjxMy5zXZXSJw0s8Y9ISlUhxSyyXVJD44xfYinLxYG7e%2BQUnIfY1Ws2hbf%2FySkRcJafWLHAghM2BMvp4K%2Ff9HNeg6Vj4s%2BM%2BkshsXF1qXpm8H1NTSNu2SX8HLAb49hKabuDCShXfdId16ib8%2FsJ5QRaalqH77XFakWNyvBkbx6WvJ3KvRIG2J5okz57sbC0bSeHN%2BnVvQLB7Rq2xxAkUBD0aEIK3uYZvxtKncZPi9TuWQ8V%2FHrneeCH7tZyj9eTocEmU22wOE5iU%2FSGx4iYOFB22UjZye7jL%2BZYF2RtI%2Bo59bZrTXAPf7bTMdK%2F%2BvR7tuBVxn3TP%2BmdE904DrloelHULa7b1idECSg5V%2BCr3wCp4reuDnhqDfaUrDGrRUXzJjf%2B48s8QbcLvyqzi5xW%2BNHzhI%2B24tYwrZL7ywY6pgGPv1RWQihs1UFUGDQqPiWw8tprT5t6wMiIFsZLi9GAZTizjh1mip1VIlOdP8D2zXR3V5YMzmd1CgjSUQB0WY9FTp0MbA9Yzal2DvIIMrobH94olEx5qYXv%2B60SIQa8AyWS5AAfiDc6dnxgR0OEjj4RO6YufedtOZIYegL80dd71SGi6nht0ppeCKpBI8QBrNE8zCtjP2Sm7Xq04kaBvG7aPa%2B%2FAKyU&X-Amz-Signature=1a0693f10020794bc196979dc35adfadb902b6a3bca04c8f1e52b5a4c542f65d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCIZVRU%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFL4aGhej0yNwUj4RexSi1zItPJhT7IM8tF5EicLNGkIAiAan4V5BT8MqePJsNjiJPl3MT2b3aYPXehipA5MZ95tNiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMD10EZGV36jTvbULWKtwDEgxArdKCLsarzqzpxHvt%2Bv8YKRhaywDN8ZZsvTNF0zVUG2d9CCOJwcqKOPXMEvq%2BqNKYBb5%2FXIaJw0%2FOrESow6Q6ro%2Br0AfcI6HXBFdO48cG1C%2Flt%2FOr7zKH8qub5bmWtrgQVVscc88X3ZRI88XETaIyWEj0vErTbC6ZM5%2BZU5TtVvWXm2K017WS%2BYUBEemO4hw0YktOQAW7qDUEhIH1OtLmqENfW%2FjxMy5zXZXSJw0s8Y9ISlUhxSyyXVJD44xfYinLxYG7e%2BQUnIfY1Ws2hbf%2FySkRcJafWLHAghM2BMvp4K%2Ff9HNeg6Vj4s%2BM%2BkshsXF1qXpm8H1NTSNu2SX8HLAb49hKabuDCShXfdId16ib8%2FsJ5QRaalqH77XFakWNyvBkbx6WvJ3KvRIG2J5okz57sbC0bSeHN%2BnVvQLB7Rq2xxAkUBD0aEIK3uYZvxtKncZPi9TuWQ8V%2FHrneeCH7tZyj9eTocEmU22wOE5iU%2FSGx4iYOFB22UjZye7jL%2BZYF2RtI%2Bo59bZrTXAPf7bTMdK%2F%2BvR7tuBVxn3TP%2BmdE904DrloelHULa7b1idECSg5V%2BCr3wCp4reuDnhqDfaUrDGrRUXzJjf%2B48s8QbcLvyqzi5xW%2BNHzhI%2B24tYwrZL7ywY6pgGPv1RWQihs1UFUGDQqPiWw8tprT5t6wMiIFsZLi9GAZTizjh1mip1VIlOdP8D2zXR3V5YMzmd1CgjSUQB0WY9FTp0MbA9Yzal2DvIIMrobH94olEx5qYXv%2B60SIQa8AyWS5AAfiDc6dnxgR0OEjj4RO6YufedtOZIYegL80dd71SGi6nht0ppeCKpBI8QBrNE8zCtjP2Sm7Xq04kaBvG7aPa%2B%2FAKyU&X-Amz-Signature=4e76779cb90b0622f5c1a1306a32fe2f7daea9630e9921b2057dbcfe2f10b228&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

