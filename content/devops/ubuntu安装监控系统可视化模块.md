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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXO3NNNA%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIGEe7vi1NXy2Gs8xFj6upKuYkjs%2Fa1lZzRrMh%2FiulqxDAiAIGMUThkeSPC7mEL891dEvYIRykfJ%2BdSmpBDGRqzRMkiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOpzvbRA6DU4KjKWEKtwD%2B%2BRZ8Gh1V6Rak%2Fpooq6qPCdN2QgtB%2BMPgMEadeujepEM3FIZUscbU6WNNVyVGYvuiEg0v01er%2Fdjw%2FyGlmE0vGFWb0a3C4Ip5NLCQDSO5eeQoZev6V7OqwmicNbWL6%2BPf0DR28mBbOZwTgOwUYj3WYOUbyq74N0W6NmHGzEV%2BSdqxnvEE7j%2BLrs9c0yDjczykrXz2t5jW4GfjU6YSvpnahxxT6wFsbKBbgzPzlntkAhBxKLh9MgoDTxjZVifgtlQBH01GrPgMeGe5k2mT3lSwZgiAHjhjqr11tnVbIqiZNOH7n4%2Fl1K9G9r3pKWB6QT0MT1zMYaq1BJGej55coZe1q6%2BdndKYq4r62BQju6WHD9%2F2cQWTnRogaL0aB8E1BPHJJWaRVq8dKmTMBQyXUYGEFWFcLUYwTo%2FLUOPQNxXSMQ8sX%2BKQRC3j2i21l2M64%2BVFDWTwsxnSeITrojUsvLkdSz98kx1z2OILtTU0p5Mi5N4ih5xq4zms4SqN2xNJdT3JaB4YpmWpc5sceW6qqDyzl%2F7tbyM8Ed%2B%2B5EsNXZHKPYyoe35BSkli2IZEgxdel4o2pivl3SD9GZ18Up21ZBiNdb0pdFgIk6fojlBFAMV1eoBaA8uQwstjJgwHs4wnsr0yAY6pgHnsWpyzcfxh1BVpW5%2B5HNU8GNWqANDpQX%2BspywMD99tC59opU9it1Gt6AS5S3g61jvwJ%2FPhIBiSpW7m5MLtMvJGR3E%2FVLccCzJ6%2FUP5yES84FzJ4izjJkBc%2BXRfLaFIYqNV0ccDkLdEUOAddjKWZHLmDNddpYW7A%2FIH9%2FtnpFMFAwzWXPnr38phVLIBTH5I42wD2aRc%2BvjjbtFWMm8ygyaqEsVtBu2&X-Amz-Signature=bccee5a41a10c35c1dbe4d45bfb1cb6f77325ab977cca1e58546aaad99981d60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXO3NNNA%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIGEe7vi1NXy2Gs8xFj6upKuYkjs%2Fa1lZzRrMh%2FiulqxDAiAIGMUThkeSPC7mEL891dEvYIRykfJ%2BdSmpBDGRqzRMkiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOpzvbRA6DU4KjKWEKtwD%2B%2BRZ8Gh1V6Rak%2Fpooq6qPCdN2QgtB%2BMPgMEadeujepEM3FIZUscbU6WNNVyVGYvuiEg0v01er%2Fdjw%2FyGlmE0vGFWb0a3C4Ip5NLCQDSO5eeQoZev6V7OqwmicNbWL6%2BPf0DR28mBbOZwTgOwUYj3WYOUbyq74N0W6NmHGzEV%2BSdqxnvEE7j%2BLrs9c0yDjczykrXz2t5jW4GfjU6YSvpnahxxT6wFsbKBbgzPzlntkAhBxKLh9MgoDTxjZVifgtlQBH01GrPgMeGe5k2mT3lSwZgiAHjhjqr11tnVbIqiZNOH7n4%2Fl1K9G9r3pKWB6QT0MT1zMYaq1BJGej55coZe1q6%2BdndKYq4r62BQju6WHD9%2F2cQWTnRogaL0aB8E1BPHJJWaRVq8dKmTMBQyXUYGEFWFcLUYwTo%2FLUOPQNxXSMQ8sX%2BKQRC3j2i21l2M64%2BVFDWTwsxnSeITrojUsvLkdSz98kx1z2OILtTU0p5Mi5N4ih5xq4zms4SqN2xNJdT3JaB4YpmWpc5sceW6qqDyzl%2F7tbyM8Ed%2B%2B5EsNXZHKPYyoe35BSkli2IZEgxdel4o2pivl3SD9GZ18Up21ZBiNdb0pdFgIk6fojlBFAMV1eoBaA8uQwstjJgwHs4wnsr0yAY6pgHnsWpyzcfxh1BVpW5%2B5HNU8GNWqANDpQX%2BspywMD99tC59opU9it1Gt6AS5S3g61jvwJ%2FPhIBiSpW7m5MLtMvJGR3E%2FVLccCzJ6%2FUP5yES84FzJ4izjJkBc%2BXRfLaFIYqNV0ccDkLdEUOAddjKWZHLmDNddpYW7A%2FIH9%2FtnpFMFAwzWXPnr38phVLIBTH5I42wD2aRc%2BvjjbtFWMm8ygyaqEsVtBu2&X-Amz-Signature=69e41e4cc8161c3b574de46c46b64b895881c6b72d25270969f787fa9ae42b45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXO3NNNA%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIGEe7vi1NXy2Gs8xFj6upKuYkjs%2Fa1lZzRrMh%2FiulqxDAiAIGMUThkeSPC7mEL891dEvYIRykfJ%2BdSmpBDGRqzRMkiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOpzvbRA6DU4KjKWEKtwD%2B%2BRZ8Gh1V6Rak%2Fpooq6qPCdN2QgtB%2BMPgMEadeujepEM3FIZUscbU6WNNVyVGYvuiEg0v01er%2Fdjw%2FyGlmE0vGFWb0a3C4Ip5NLCQDSO5eeQoZev6V7OqwmicNbWL6%2BPf0DR28mBbOZwTgOwUYj3WYOUbyq74N0W6NmHGzEV%2BSdqxnvEE7j%2BLrs9c0yDjczykrXz2t5jW4GfjU6YSvpnahxxT6wFsbKBbgzPzlntkAhBxKLh9MgoDTxjZVifgtlQBH01GrPgMeGe5k2mT3lSwZgiAHjhjqr11tnVbIqiZNOH7n4%2Fl1K9G9r3pKWB6QT0MT1zMYaq1BJGej55coZe1q6%2BdndKYq4r62BQju6WHD9%2F2cQWTnRogaL0aB8E1BPHJJWaRVq8dKmTMBQyXUYGEFWFcLUYwTo%2FLUOPQNxXSMQ8sX%2BKQRC3j2i21l2M64%2BVFDWTwsxnSeITrojUsvLkdSz98kx1z2OILtTU0p5Mi5N4ih5xq4zms4SqN2xNJdT3JaB4YpmWpc5sceW6qqDyzl%2F7tbyM8Ed%2B%2B5EsNXZHKPYyoe35BSkli2IZEgxdel4o2pivl3SD9GZ18Up21ZBiNdb0pdFgIk6fojlBFAMV1eoBaA8uQwstjJgwHs4wnsr0yAY6pgHnsWpyzcfxh1BVpW5%2B5HNU8GNWqANDpQX%2BspywMD99tC59opU9it1Gt6AS5S3g61jvwJ%2FPhIBiSpW7m5MLtMvJGR3E%2FVLccCzJ6%2FUP5yES84FzJ4izjJkBc%2BXRfLaFIYqNV0ccDkLdEUOAddjKWZHLmDNddpYW7A%2FIH9%2FtnpFMFAwzWXPnr38phVLIBTH5I42wD2aRc%2BvjjbtFWMm8ygyaqEsVtBu2&X-Amz-Signature=b55a2c98d906fa56352efe7b0d4a43e2d453aa593bbc36a9e0b3f419654a8842&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXO3NNNA%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIGEe7vi1NXy2Gs8xFj6upKuYkjs%2Fa1lZzRrMh%2FiulqxDAiAIGMUThkeSPC7mEL891dEvYIRykfJ%2BdSmpBDGRqzRMkiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOpzvbRA6DU4KjKWEKtwD%2B%2BRZ8Gh1V6Rak%2Fpooq6qPCdN2QgtB%2BMPgMEadeujepEM3FIZUscbU6WNNVyVGYvuiEg0v01er%2Fdjw%2FyGlmE0vGFWb0a3C4Ip5NLCQDSO5eeQoZev6V7OqwmicNbWL6%2BPf0DR28mBbOZwTgOwUYj3WYOUbyq74N0W6NmHGzEV%2BSdqxnvEE7j%2BLrs9c0yDjczykrXz2t5jW4GfjU6YSvpnahxxT6wFsbKBbgzPzlntkAhBxKLh9MgoDTxjZVifgtlQBH01GrPgMeGe5k2mT3lSwZgiAHjhjqr11tnVbIqiZNOH7n4%2Fl1K9G9r3pKWB6QT0MT1zMYaq1BJGej55coZe1q6%2BdndKYq4r62BQju6WHD9%2F2cQWTnRogaL0aB8E1BPHJJWaRVq8dKmTMBQyXUYGEFWFcLUYwTo%2FLUOPQNxXSMQ8sX%2BKQRC3j2i21l2M64%2BVFDWTwsxnSeITrojUsvLkdSz98kx1z2OILtTU0p5Mi5N4ih5xq4zms4SqN2xNJdT3JaB4YpmWpc5sceW6qqDyzl%2F7tbyM8Ed%2B%2B5EsNXZHKPYyoe35BSkli2IZEgxdel4o2pivl3SD9GZ18Up21ZBiNdb0pdFgIk6fojlBFAMV1eoBaA8uQwstjJgwHs4wnsr0yAY6pgHnsWpyzcfxh1BVpW5%2B5HNU8GNWqANDpQX%2BspywMD99tC59opU9it1Gt6AS5S3g61jvwJ%2FPhIBiSpW7m5MLtMvJGR3E%2FVLccCzJ6%2FUP5yES84FzJ4izjJkBc%2BXRfLaFIYqNV0ccDkLdEUOAddjKWZHLmDNddpYW7A%2FIH9%2FtnpFMFAwzWXPnr38phVLIBTH5I42wD2aRc%2BvjjbtFWMm8ygyaqEsVtBu2&X-Amz-Signature=325e3c997fe285e8e5fb9df55a8ccded17e3a22f8cdbbbcdacb0e5b7dc16f6d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXO3NNNA%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIGEe7vi1NXy2Gs8xFj6upKuYkjs%2Fa1lZzRrMh%2FiulqxDAiAIGMUThkeSPC7mEL891dEvYIRykfJ%2BdSmpBDGRqzRMkiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOpzvbRA6DU4KjKWEKtwD%2B%2BRZ8Gh1V6Rak%2Fpooq6qPCdN2QgtB%2BMPgMEadeujepEM3FIZUscbU6WNNVyVGYvuiEg0v01er%2Fdjw%2FyGlmE0vGFWb0a3C4Ip5NLCQDSO5eeQoZev6V7OqwmicNbWL6%2BPf0DR28mBbOZwTgOwUYj3WYOUbyq74N0W6NmHGzEV%2BSdqxnvEE7j%2BLrs9c0yDjczykrXz2t5jW4GfjU6YSvpnahxxT6wFsbKBbgzPzlntkAhBxKLh9MgoDTxjZVifgtlQBH01GrPgMeGe5k2mT3lSwZgiAHjhjqr11tnVbIqiZNOH7n4%2Fl1K9G9r3pKWB6QT0MT1zMYaq1BJGej55coZe1q6%2BdndKYq4r62BQju6WHD9%2F2cQWTnRogaL0aB8E1BPHJJWaRVq8dKmTMBQyXUYGEFWFcLUYwTo%2FLUOPQNxXSMQ8sX%2BKQRC3j2i21l2M64%2BVFDWTwsxnSeITrojUsvLkdSz98kx1z2OILtTU0p5Mi5N4ih5xq4zms4SqN2xNJdT3JaB4YpmWpc5sceW6qqDyzl%2F7tbyM8Ed%2B%2B5EsNXZHKPYyoe35BSkli2IZEgxdel4o2pivl3SD9GZ18Up21ZBiNdb0pdFgIk6fojlBFAMV1eoBaA8uQwstjJgwHs4wnsr0yAY6pgHnsWpyzcfxh1BVpW5%2B5HNU8GNWqANDpQX%2BspywMD99tC59opU9it1Gt6AS5S3g61jvwJ%2FPhIBiSpW7m5MLtMvJGR3E%2FVLccCzJ6%2FUP5yES84FzJ4izjJkBc%2BXRfLaFIYqNV0ccDkLdEUOAddjKWZHLmDNddpYW7A%2FIH9%2FtnpFMFAwzWXPnr38phVLIBTH5I42wD2aRc%2BvjjbtFWMm8ygyaqEsVtBu2&X-Amz-Signature=807645530ec053aea85522d65b6239ce1a8dbe4bca48a06301f105cea8390a51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXO3NNNA%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIGEe7vi1NXy2Gs8xFj6upKuYkjs%2Fa1lZzRrMh%2FiulqxDAiAIGMUThkeSPC7mEL891dEvYIRykfJ%2BdSmpBDGRqzRMkiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOpzvbRA6DU4KjKWEKtwD%2B%2BRZ8Gh1V6Rak%2Fpooq6qPCdN2QgtB%2BMPgMEadeujepEM3FIZUscbU6WNNVyVGYvuiEg0v01er%2Fdjw%2FyGlmE0vGFWb0a3C4Ip5NLCQDSO5eeQoZev6V7OqwmicNbWL6%2BPf0DR28mBbOZwTgOwUYj3WYOUbyq74N0W6NmHGzEV%2BSdqxnvEE7j%2BLrs9c0yDjczykrXz2t5jW4GfjU6YSvpnahxxT6wFsbKBbgzPzlntkAhBxKLh9MgoDTxjZVifgtlQBH01GrPgMeGe5k2mT3lSwZgiAHjhjqr11tnVbIqiZNOH7n4%2Fl1K9G9r3pKWB6QT0MT1zMYaq1BJGej55coZe1q6%2BdndKYq4r62BQju6WHD9%2F2cQWTnRogaL0aB8E1BPHJJWaRVq8dKmTMBQyXUYGEFWFcLUYwTo%2FLUOPQNxXSMQ8sX%2BKQRC3j2i21l2M64%2BVFDWTwsxnSeITrojUsvLkdSz98kx1z2OILtTU0p5Mi5N4ih5xq4zms4SqN2xNJdT3JaB4YpmWpc5sceW6qqDyzl%2F7tbyM8Ed%2B%2B5EsNXZHKPYyoe35BSkli2IZEgxdel4o2pivl3SD9GZ18Up21ZBiNdb0pdFgIk6fojlBFAMV1eoBaA8uQwstjJgwHs4wnsr0yAY6pgHnsWpyzcfxh1BVpW5%2B5HNU8GNWqANDpQX%2BspywMD99tC59opU9it1Gt6AS5S3g61jvwJ%2FPhIBiSpW7m5MLtMvJGR3E%2FVLccCzJ6%2FUP5yES84FzJ4izjJkBc%2BXRfLaFIYqNV0ccDkLdEUOAddjKWZHLmDNddpYW7A%2FIH9%2FtnpFMFAwzWXPnr38phVLIBTH5I42wD2aRc%2BvjjbtFWMm8ygyaqEsVtBu2&X-Amz-Signature=65115940e96eb23a270d6998ceaa35a9f45af1a791b80e3efe1d0124791eb778&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXO3NNNA%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIGEe7vi1NXy2Gs8xFj6upKuYkjs%2Fa1lZzRrMh%2FiulqxDAiAIGMUThkeSPC7mEL891dEvYIRykfJ%2BdSmpBDGRqzRMkiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOpzvbRA6DU4KjKWEKtwD%2B%2BRZ8Gh1V6Rak%2Fpooq6qPCdN2QgtB%2BMPgMEadeujepEM3FIZUscbU6WNNVyVGYvuiEg0v01er%2Fdjw%2FyGlmE0vGFWb0a3C4Ip5NLCQDSO5eeQoZev6V7OqwmicNbWL6%2BPf0DR28mBbOZwTgOwUYj3WYOUbyq74N0W6NmHGzEV%2BSdqxnvEE7j%2BLrs9c0yDjczykrXz2t5jW4GfjU6YSvpnahxxT6wFsbKBbgzPzlntkAhBxKLh9MgoDTxjZVifgtlQBH01GrPgMeGe5k2mT3lSwZgiAHjhjqr11tnVbIqiZNOH7n4%2Fl1K9G9r3pKWB6QT0MT1zMYaq1BJGej55coZe1q6%2BdndKYq4r62BQju6WHD9%2F2cQWTnRogaL0aB8E1BPHJJWaRVq8dKmTMBQyXUYGEFWFcLUYwTo%2FLUOPQNxXSMQ8sX%2BKQRC3j2i21l2M64%2BVFDWTwsxnSeITrojUsvLkdSz98kx1z2OILtTU0p5Mi5N4ih5xq4zms4SqN2xNJdT3JaB4YpmWpc5sceW6qqDyzl%2F7tbyM8Ed%2B%2B5EsNXZHKPYyoe35BSkli2IZEgxdel4o2pivl3SD9GZ18Up21ZBiNdb0pdFgIk6fojlBFAMV1eoBaA8uQwstjJgwHs4wnsr0yAY6pgHnsWpyzcfxh1BVpW5%2B5HNU8GNWqANDpQX%2BspywMD99tC59opU9it1Gt6AS5S3g61jvwJ%2FPhIBiSpW7m5MLtMvJGR3E%2FVLccCzJ6%2FUP5yES84FzJ4izjJkBc%2BXRfLaFIYqNV0ccDkLdEUOAddjKWZHLmDNddpYW7A%2FIH9%2FtnpFMFAwzWXPnr38phVLIBTH5I42wD2aRc%2BvjjbtFWMm8ygyaqEsVtBu2&X-Amz-Signature=5d1338acdf7c450092c641366dd50b7465cf455e276e2457d923fc08f87c27b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

