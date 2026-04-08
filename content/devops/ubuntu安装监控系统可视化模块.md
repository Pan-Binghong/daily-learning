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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OSZKTTJ%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCICbraUFMw4wWeEoAy%2FlfZU5c5qhrvjbInznYshHQLgJWAiBCPD2SEGWHCkUeCZpR6z4jk9gsf7cLQ8VF6Gm6aQDqyiqIBAj0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1VoJmRC%2F%2BFEwCVyFKtwDuqaMn0oGmq30dvmoG%2F5KmAjhv%2FZE2O7tuxoHy1AtmqA%2Full2O8Qeb2xDPToyEUjVW0aSQFC7UW8xAFQe5ar1r1u75sgZLFQ7KjUvb50PKElNOSNPEZc1%2BJfYUaSQyY8rGrD2s0GA4gHPzPI6Xe4GSVzOH8WMjo1O6ozrOstNPKbwOjJjjrWN%2BKPyOlL%2BN%2BZVNAtXlDw8P1Ae2qujBwpPnr%2FjgxeWVtlDexCtXsF88NcY8bR0rsehvrdvarOVFxmzWFgy0dd2%2F%2Bw75O7mLd1ovlQRrJdA5rF1CZPimavgXgs96x2Vpvej38T2msOGXG14caWrvaq7HVPHS7WkMPFj7UtSbqg1dDWk3Mu9g1fxFA5i4ra0DeOSG%2B90HRR8%2B06MvRxcGCcihoJuW1A3yttyaRAAlnP01mVTqALMEp7WWAfOaa9qok13yR0dSFk2Zk7D76%2F5OjR48BxgrOLgiAB1e9u1UNxeB%2FWgqefxdfa12WHQSNLjFdiDivYr%2BN58RrVLz5%2BIMFWiRvD3B7rOGmD4cNJcJD3bLU%2Bi3DLP1qkPctUPxSnyR3xRbfq%2F20EfmHuSt3LR9wiIOiUytH5%2BhxK9XkcPeYzRyNxQ%2BRjmg4LT3iwoD4JN7D%2Fezu697uYwmYrXzgY6pgHwpnaGmkgJ15RICP5I0tq%2BLNq4PNX3qx2MxM%2Baay%2FGjbJ8%2BgYfzopc1Es%2FkVOQAL%2FT%2FsfAffwxNuxUKYokGOa21LEsQG4w4bpz%2FEnTSmY1x0HZLW3e9lC698dC%2F%2Ff5E0vsr2pl4Yx2NOqP9CuCnU1WIcOImuMMcG4SiKkhlouwvkMcARlOno6TSHHL%2FtYa5r8hhyR9iZryql2Q8j7FxsCsN4DCauU4&X-Amz-Signature=82ced66755325211189f799fe2b53028d5aff0f77da90357daf6155edf9cea68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OSZKTTJ%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCICbraUFMw4wWeEoAy%2FlfZU5c5qhrvjbInznYshHQLgJWAiBCPD2SEGWHCkUeCZpR6z4jk9gsf7cLQ8VF6Gm6aQDqyiqIBAj0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1VoJmRC%2F%2BFEwCVyFKtwDuqaMn0oGmq30dvmoG%2F5KmAjhv%2FZE2O7tuxoHy1AtmqA%2Full2O8Qeb2xDPToyEUjVW0aSQFC7UW8xAFQe5ar1r1u75sgZLFQ7KjUvb50PKElNOSNPEZc1%2BJfYUaSQyY8rGrD2s0GA4gHPzPI6Xe4GSVzOH8WMjo1O6ozrOstNPKbwOjJjjrWN%2BKPyOlL%2BN%2BZVNAtXlDw8P1Ae2qujBwpPnr%2FjgxeWVtlDexCtXsF88NcY8bR0rsehvrdvarOVFxmzWFgy0dd2%2F%2Bw75O7mLd1ovlQRrJdA5rF1CZPimavgXgs96x2Vpvej38T2msOGXG14caWrvaq7HVPHS7WkMPFj7UtSbqg1dDWk3Mu9g1fxFA5i4ra0DeOSG%2B90HRR8%2B06MvRxcGCcihoJuW1A3yttyaRAAlnP01mVTqALMEp7WWAfOaa9qok13yR0dSFk2Zk7D76%2F5OjR48BxgrOLgiAB1e9u1UNxeB%2FWgqefxdfa12WHQSNLjFdiDivYr%2BN58RrVLz5%2BIMFWiRvD3B7rOGmD4cNJcJD3bLU%2Bi3DLP1qkPctUPxSnyR3xRbfq%2F20EfmHuSt3LR9wiIOiUytH5%2BhxK9XkcPeYzRyNxQ%2BRjmg4LT3iwoD4JN7D%2Fezu697uYwmYrXzgY6pgHwpnaGmkgJ15RICP5I0tq%2BLNq4PNX3qx2MxM%2Baay%2FGjbJ8%2BgYfzopc1Es%2FkVOQAL%2FT%2FsfAffwxNuxUKYokGOa21LEsQG4w4bpz%2FEnTSmY1x0HZLW3e9lC698dC%2F%2Ff5E0vsr2pl4Yx2NOqP9CuCnU1WIcOImuMMcG4SiKkhlouwvkMcARlOno6TSHHL%2FtYa5r8hhyR9iZryql2Q8j7FxsCsN4DCauU4&X-Amz-Signature=66dcc97e9ce2fe91fe8c5a9023ec7d927d4e44633b0d6070e5b8c36ac71f04aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OSZKTTJ%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCICbraUFMw4wWeEoAy%2FlfZU5c5qhrvjbInznYshHQLgJWAiBCPD2SEGWHCkUeCZpR6z4jk9gsf7cLQ8VF6Gm6aQDqyiqIBAj0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1VoJmRC%2F%2BFEwCVyFKtwDuqaMn0oGmq30dvmoG%2F5KmAjhv%2FZE2O7tuxoHy1AtmqA%2Full2O8Qeb2xDPToyEUjVW0aSQFC7UW8xAFQe5ar1r1u75sgZLFQ7KjUvb50PKElNOSNPEZc1%2BJfYUaSQyY8rGrD2s0GA4gHPzPI6Xe4GSVzOH8WMjo1O6ozrOstNPKbwOjJjjrWN%2BKPyOlL%2BN%2BZVNAtXlDw8P1Ae2qujBwpPnr%2FjgxeWVtlDexCtXsF88NcY8bR0rsehvrdvarOVFxmzWFgy0dd2%2F%2Bw75O7mLd1ovlQRrJdA5rF1CZPimavgXgs96x2Vpvej38T2msOGXG14caWrvaq7HVPHS7WkMPFj7UtSbqg1dDWk3Mu9g1fxFA5i4ra0DeOSG%2B90HRR8%2B06MvRxcGCcihoJuW1A3yttyaRAAlnP01mVTqALMEp7WWAfOaa9qok13yR0dSFk2Zk7D76%2F5OjR48BxgrOLgiAB1e9u1UNxeB%2FWgqefxdfa12WHQSNLjFdiDivYr%2BN58RrVLz5%2BIMFWiRvD3B7rOGmD4cNJcJD3bLU%2Bi3DLP1qkPctUPxSnyR3xRbfq%2F20EfmHuSt3LR9wiIOiUytH5%2BhxK9XkcPeYzRyNxQ%2BRjmg4LT3iwoD4JN7D%2Fezu697uYwmYrXzgY6pgHwpnaGmkgJ15RICP5I0tq%2BLNq4PNX3qx2MxM%2Baay%2FGjbJ8%2BgYfzopc1Es%2FkVOQAL%2FT%2FsfAffwxNuxUKYokGOa21LEsQG4w4bpz%2FEnTSmY1x0HZLW3e9lC698dC%2F%2Ff5E0vsr2pl4Yx2NOqP9CuCnU1WIcOImuMMcG4SiKkhlouwvkMcARlOno6TSHHL%2FtYa5r8hhyR9iZryql2Q8j7FxsCsN4DCauU4&X-Amz-Signature=66e87bc1c1a36154380d820360a554267e2cf8063b385d3672ee62feda256a5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OSZKTTJ%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCICbraUFMw4wWeEoAy%2FlfZU5c5qhrvjbInznYshHQLgJWAiBCPD2SEGWHCkUeCZpR6z4jk9gsf7cLQ8VF6Gm6aQDqyiqIBAj0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1VoJmRC%2F%2BFEwCVyFKtwDuqaMn0oGmq30dvmoG%2F5KmAjhv%2FZE2O7tuxoHy1AtmqA%2Full2O8Qeb2xDPToyEUjVW0aSQFC7UW8xAFQe5ar1r1u75sgZLFQ7KjUvb50PKElNOSNPEZc1%2BJfYUaSQyY8rGrD2s0GA4gHPzPI6Xe4GSVzOH8WMjo1O6ozrOstNPKbwOjJjjrWN%2BKPyOlL%2BN%2BZVNAtXlDw8P1Ae2qujBwpPnr%2FjgxeWVtlDexCtXsF88NcY8bR0rsehvrdvarOVFxmzWFgy0dd2%2F%2Bw75O7mLd1ovlQRrJdA5rF1CZPimavgXgs96x2Vpvej38T2msOGXG14caWrvaq7HVPHS7WkMPFj7UtSbqg1dDWk3Mu9g1fxFA5i4ra0DeOSG%2B90HRR8%2B06MvRxcGCcihoJuW1A3yttyaRAAlnP01mVTqALMEp7WWAfOaa9qok13yR0dSFk2Zk7D76%2F5OjR48BxgrOLgiAB1e9u1UNxeB%2FWgqefxdfa12WHQSNLjFdiDivYr%2BN58RrVLz5%2BIMFWiRvD3B7rOGmD4cNJcJD3bLU%2Bi3DLP1qkPctUPxSnyR3xRbfq%2F20EfmHuSt3LR9wiIOiUytH5%2BhxK9XkcPeYzRyNxQ%2BRjmg4LT3iwoD4JN7D%2Fezu697uYwmYrXzgY6pgHwpnaGmkgJ15RICP5I0tq%2BLNq4PNX3qx2MxM%2Baay%2FGjbJ8%2BgYfzopc1Es%2FkVOQAL%2FT%2FsfAffwxNuxUKYokGOa21LEsQG4w4bpz%2FEnTSmY1x0HZLW3e9lC698dC%2F%2Ff5E0vsr2pl4Yx2NOqP9CuCnU1WIcOImuMMcG4SiKkhlouwvkMcARlOno6TSHHL%2FtYa5r8hhyR9iZryql2Q8j7FxsCsN4DCauU4&X-Amz-Signature=435fb4c3ba6e67b2ae9e6b0ea9f2982714ad0e68399f2c14892977b785463a5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OSZKTTJ%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCICbraUFMw4wWeEoAy%2FlfZU5c5qhrvjbInznYshHQLgJWAiBCPD2SEGWHCkUeCZpR6z4jk9gsf7cLQ8VF6Gm6aQDqyiqIBAj0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1VoJmRC%2F%2BFEwCVyFKtwDuqaMn0oGmq30dvmoG%2F5KmAjhv%2FZE2O7tuxoHy1AtmqA%2Full2O8Qeb2xDPToyEUjVW0aSQFC7UW8xAFQe5ar1r1u75sgZLFQ7KjUvb50PKElNOSNPEZc1%2BJfYUaSQyY8rGrD2s0GA4gHPzPI6Xe4GSVzOH8WMjo1O6ozrOstNPKbwOjJjjrWN%2BKPyOlL%2BN%2BZVNAtXlDw8P1Ae2qujBwpPnr%2FjgxeWVtlDexCtXsF88NcY8bR0rsehvrdvarOVFxmzWFgy0dd2%2F%2Bw75O7mLd1ovlQRrJdA5rF1CZPimavgXgs96x2Vpvej38T2msOGXG14caWrvaq7HVPHS7WkMPFj7UtSbqg1dDWk3Mu9g1fxFA5i4ra0DeOSG%2B90HRR8%2B06MvRxcGCcihoJuW1A3yttyaRAAlnP01mVTqALMEp7WWAfOaa9qok13yR0dSFk2Zk7D76%2F5OjR48BxgrOLgiAB1e9u1UNxeB%2FWgqefxdfa12WHQSNLjFdiDivYr%2BN58RrVLz5%2BIMFWiRvD3B7rOGmD4cNJcJD3bLU%2Bi3DLP1qkPctUPxSnyR3xRbfq%2F20EfmHuSt3LR9wiIOiUytH5%2BhxK9XkcPeYzRyNxQ%2BRjmg4LT3iwoD4JN7D%2Fezu697uYwmYrXzgY6pgHwpnaGmkgJ15RICP5I0tq%2BLNq4PNX3qx2MxM%2Baay%2FGjbJ8%2BgYfzopc1Es%2FkVOQAL%2FT%2FsfAffwxNuxUKYokGOa21LEsQG4w4bpz%2FEnTSmY1x0HZLW3e9lC698dC%2F%2Ff5E0vsr2pl4Yx2NOqP9CuCnU1WIcOImuMMcG4SiKkhlouwvkMcARlOno6TSHHL%2FtYa5r8hhyR9iZryql2Q8j7FxsCsN4DCauU4&X-Amz-Signature=15aeee6877ed0ee2e7d233ef8654649e0dd39b7aa826810a99f43c6813ebf1b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OSZKTTJ%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCICbraUFMw4wWeEoAy%2FlfZU5c5qhrvjbInznYshHQLgJWAiBCPD2SEGWHCkUeCZpR6z4jk9gsf7cLQ8VF6Gm6aQDqyiqIBAj0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1VoJmRC%2F%2BFEwCVyFKtwDuqaMn0oGmq30dvmoG%2F5KmAjhv%2FZE2O7tuxoHy1AtmqA%2Full2O8Qeb2xDPToyEUjVW0aSQFC7UW8xAFQe5ar1r1u75sgZLFQ7KjUvb50PKElNOSNPEZc1%2BJfYUaSQyY8rGrD2s0GA4gHPzPI6Xe4GSVzOH8WMjo1O6ozrOstNPKbwOjJjjrWN%2BKPyOlL%2BN%2BZVNAtXlDw8P1Ae2qujBwpPnr%2FjgxeWVtlDexCtXsF88NcY8bR0rsehvrdvarOVFxmzWFgy0dd2%2F%2Bw75O7mLd1ovlQRrJdA5rF1CZPimavgXgs96x2Vpvej38T2msOGXG14caWrvaq7HVPHS7WkMPFj7UtSbqg1dDWk3Mu9g1fxFA5i4ra0DeOSG%2B90HRR8%2B06MvRxcGCcihoJuW1A3yttyaRAAlnP01mVTqALMEp7WWAfOaa9qok13yR0dSFk2Zk7D76%2F5OjR48BxgrOLgiAB1e9u1UNxeB%2FWgqefxdfa12WHQSNLjFdiDivYr%2BN58RrVLz5%2BIMFWiRvD3B7rOGmD4cNJcJD3bLU%2Bi3DLP1qkPctUPxSnyR3xRbfq%2F20EfmHuSt3LR9wiIOiUytH5%2BhxK9XkcPeYzRyNxQ%2BRjmg4LT3iwoD4JN7D%2Fezu697uYwmYrXzgY6pgHwpnaGmkgJ15RICP5I0tq%2BLNq4PNX3qx2MxM%2Baay%2FGjbJ8%2BgYfzopc1Es%2FkVOQAL%2FT%2FsfAffwxNuxUKYokGOa21LEsQG4w4bpz%2FEnTSmY1x0HZLW3e9lC698dC%2F%2Ff5E0vsr2pl4Yx2NOqP9CuCnU1WIcOImuMMcG4SiKkhlouwvkMcARlOno6TSHHL%2FtYa5r8hhyR9iZryql2Q8j7FxsCsN4DCauU4&X-Amz-Signature=be1e7b9ea3459bf0b49e0e58ea856450cda8bf45db82ca489fb7d7aa5591fa55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OSZKTTJ%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCICbraUFMw4wWeEoAy%2FlfZU5c5qhrvjbInznYshHQLgJWAiBCPD2SEGWHCkUeCZpR6z4jk9gsf7cLQ8VF6Gm6aQDqyiqIBAj0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1VoJmRC%2F%2BFEwCVyFKtwDuqaMn0oGmq30dvmoG%2F5KmAjhv%2FZE2O7tuxoHy1AtmqA%2Full2O8Qeb2xDPToyEUjVW0aSQFC7UW8xAFQe5ar1r1u75sgZLFQ7KjUvb50PKElNOSNPEZc1%2BJfYUaSQyY8rGrD2s0GA4gHPzPI6Xe4GSVzOH8WMjo1O6ozrOstNPKbwOjJjjrWN%2BKPyOlL%2BN%2BZVNAtXlDw8P1Ae2qujBwpPnr%2FjgxeWVtlDexCtXsF88NcY8bR0rsehvrdvarOVFxmzWFgy0dd2%2F%2Bw75O7mLd1ovlQRrJdA5rF1CZPimavgXgs96x2Vpvej38T2msOGXG14caWrvaq7HVPHS7WkMPFj7UtSbqg1dDWk3Mu9g1fxFA5i4ra0DeOSG%2B90HRR8%2B06MvRxcGCcihoJuW1A3yttyaRAAlnP01mVTqALMEp7WWAfOaa9qok13yR0dSFk2Zk7D76%2F5OjR48BxgrOLgiAB1e9u1UNxeB%2FWgqefxdfa12WHQSNLjFdiDivYr%2BN58RrVLz5%2BIMFWiRvD3B7rOGmD4cNJcJD3bLU%2Bi3DLP1qkPctUPxSnyR3xRbfq%2F20EfmHuSt3LR9wiIOiUytH5%2BhxK9XkcPeYzRyNxQ%2BRjmg4LT3iwoD4JN7D%2Fezu697uYwmYrXzgY6pgHwpnaGmkgJ15RICP5I0tq%2BLNq4PNX3qx2MxM%2Baay%2FGjbJ8%2BgYfzopc1Es%2FkVOQAL%2FT%2FsfAffwxNuxUKYokGOa21LEsQG4w4bpz%2FEnTSmY1x0HZLW3e9lC698dC%2F%2Ff5E0vsr2pl4Yx2NOqP9CuCnU1WIcOImuMMcG4SiKkhlouwvkMcARlOno6TSHHL%2FtYa5r8hhyR9iZryql2Q8j7FxsCsN4DCauU4&X-Amz-Signature=a1dce655386ac34f5e4983b872e5e0e57c09d54b3fdd0b9ebcd3dbab776e2fa9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

