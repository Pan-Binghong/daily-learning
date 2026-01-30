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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Z7IZVHD%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDv4bdCo7YaY2vFK3bhVM2GR%2FzysBpJuIaIVTBfr4kI1AiBHBVqw5gKuhzt6lX8InXbCri9BSyUVnVCXZEflirrkiiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZrmCP1yLprvs%2FNsqKtwDAGB4V28bES12ceS67vUrdKx1WhZ6HQewkSrZ7Z9FwBLs3hUBlKCWigSeIQYFtL8Wg%2FHG61FPWoMlIgizkWC%2FMKkvT8%2Fm2G2So6gEgm2444oN7LQKORetPDJuSlmJfqelSok8TUDx%2FnbP7Sxk98EHo0A17bDAnO%2FEJ%2Bq3yoO2T%2BPfAbad%2BeVjxx%2Bv%2Flf4WLfbTLfCyfxTd8Mib1DyVEmj6ipm%2FlFBtPLkHQ2%2BYVsY%2BhtI0htz5Bx7mdD8fvnidPQRHGShFQZP5NXlY4bVZakwt9vyJ5j%2FtyTvdOh3DdZs%2B492iSnL3kYGMkCfCDL3hSTQuKfxkItUCwDFt2aQq0Xg%2Byb7WflG4ERAAnDBV5NOZyw2rGN0XHQGQyelSpGQSIjg6xyM6eS0L7MnFtY4LU55dBtUGBXP61C5ClbEayM1O3bhTYLTXUUMsyQITzUieYjI05D93CGYF2qNgR9lenJ%2BIk2s%2Fpq0pw9o8pIbgxPt1sjRiFrYWdgPYO%2BW3LpXXKQrTU4y4KrrlxJoX4cHZJ1hJinW1Y8JS%2FH3udBnYSi%2FFhM7FyEQNIxzWoUKcMtW7s63Ru1B7%2Bpixx5fkM5CaD8PyBfFT%2Fk%2Bd0TlKPen7nR1WRf9loDwCTEZ3KezXyww2sjwywY6pgG2irO%2BA5Mrp0vuqizHQxD9xtqfjZGUBwDcmwBZi6suO3D%2BePx5l%2BUYNhvTIkzq%2FKTtCXR0qWyFzCn0iQS3AP3ABalvMSW7DD%2BxFsjMFAa4h9BDTTATGixTl7aTXvhmKbt86H1WtPnFCjLRoc4WUCxh1N4HQlGJEyZM2o52ZkRFTbo%2FTiS9T2FJqqNiyC2HLtFHHQ%2FXAvwvHD2FumaFWivFBP9yK7XC&X-Amz-Signature=ae8d8744df925a80a81765cb4a5871f181737ce22ed364203ad81f4bd386cc6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Z7IZVHD%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDv4bdCo7YaY2vFK3bhVM2GR%2FzysBpJuIaIVTBfr4kI1AiBHBVqw5gKuhzt6lX8InXbCri9BSyUVnVCXZEflirrkiiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZrmCP1yLprvs%2FNsqKtwDAGB4V28bES12ceS67vUrdKx1WhZ6HQewkSrZ7Z9FwBLs3hUBlKCWigSeIQYFtL8Wg%2FHG61FPWoMlIgizkWC%2FMKkvT8%2Fm2G2So6gEgm2444oN7LQKORetPDJuSlmJfqelSok8TUDx%2FnbP7Sxk98EHo0A17bDAnO%2FEJ%2Bq3yoO2T%2BPfAbad%2BeVjxx%2Bv%2Flf4WLfbTLfCyfxTd8Mib1DyVEmj6ipm%2FlFBtPLkHQ2%2BYVsY%2BhtI0htz5Bx7mdD8fvnidPQRHGShFQZP5NXlY4bVZakwt9vyJ5j%2FtyTvdOh3DdZs%2B492iSnL3kYGMkCfCDL3hSTQuKfxkItUCwDFt2aQq0Xg%2Byb7WflG4ERAAnDBV5NOZyw2rGN0XHQGQyelSpGQSIjg6xyM6eS0L7MnFtY4LU55dBtUGBXP61C5ClbEayM1O3bhTYLTXUUMsyQITzUieYjI05D93CGYF2qNgR9lenJ%2BIk2s%2Fpq0pw9o8pIbgxPt1sjRiFrYWdgPYO%2BW3LpXXKQrTU4y4KrrlxJoX4cHZJ1hJinW1Y8JS%2FH3udBnYSi%2FFhM7FyEQNIxzWoUKcMtW7s63Ru1B7%2Bpixx5fkM5CaD8PyBfFT%2Fk%2Bd0TlKPen7nR1WRf9loDwCTEZ3KezXyww2sjwywY6pgG2irO%2BA5Mrp0vuqizHQxD9xtqfjZGUBwDcmwBZi6suO3D%2BePx5l%2BUYNhvTIkzq%2FKTtCXR0qWyFzCn0iQS3AP3ABalvMSW7DD%2BxFsjMFAa4h9BDTTATGixTl7aTXvhmKbt86H1WtPnFCjLRoc4WUCxh1N4HQlGJEyZM2o52ZkRFTbo%2FTiS9T2FJqqNiyC2HLtFHHQ%2FXAvwvHD2FumaFWivFBP9yK7XC&X-Amz-Signature=f68e345346fd4a1db47255eaab3e906291840ac3cd7a1c4c3ba4a93b6fe12bde&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Z7IZVHD%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDv4bdCo7YaY2vFK3bhVM2GR%2FzysBpJuIaIVTBfr4kI1AiBHBVqw5gKuhzt6lX8InXbCri9BSyUVnVCXZEflirrkiiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZrmCP1yLprvs%2FNsqKtwDAGB4V28bES12ceS67vUrdKx1WhZ6HQewkSrZ7Z9FwBLs3hUBlKCWigSeIQYFtL8Wg%2FHG61FPWoMlIgizkWC%2FMKkvT8%2Fm2G2So6gEgm2444oN7LQKORetPDJuSlmJfqelSok8TUDx%2FnbP7Sxk98EHo0A17bDAnO%2FEJ%2Bq3yoO2T%2BPfAbad%2BeVjxx%2Bv%2Flf4WLfbTLfCyfxTd8Mib1DyVEmj6ipm%2FlFBtPLkHQ2%2BYVsY%2BhtI0htz5Bx7mdD8fvnidPQRHGShFQZP5NXlY4bVZakwt9vyJ5j%2FtyTvdOh3DdZs%2B492iSnL3kYGMkCfCDL3hSTQuKfxkItUCwDFt2aQq0Xg%2Byb7WflG4ERAAnDBV5NOZyw2rGN0XHQGQyelSpGQSIjg6xyM6eS0L7MnFtY4LU55dBtUGBXP61C5ClbEayM1O3bhTYLTXUUMsyQITzUieYjI05D93CGYF2qNgR9lenJ%2BIk2s%2Fpq0pw9o8pIbgxPt1sjRiFrYWdgPYO%2BW3LpXXKQrTU4y4KrrlxJoX4cHZJ1hJinW1Y8JS%2FH3udBnYSi%2FFhM7FyEQNIxzWoUKcMtW7s63Ru1B7%2Bpixx5fkM5CaD8PyBfFT%2Fk%2Bd0TlKPen7nR1WRf9loDwCTEZ3KezXyww2sjwywY6pgG2irO%2BA5Mrp0vuqizHQxD9xtqfjZGUBwDcmwBZi6suO3D%2BePx5l%2BUYNhvTIkzq%2FKTtCXR0qWyFzCn0iQS3AP3ABalvMSW7DD%2BxFsjMFAa4h9BDTTATGixTl7aTXvhmKbt86H1WtPnFCjLRoc4WUCxh1N4HQlGJEyZM2o52ZkRFTbo%2FTiS9T2FJqqNiyC2HLtFHHQ%2FXAvwvHD2FumaFWivFBP9yK7XC&X-Amz-Signature=8f5020212fab36606d230bd3a39b96312fae96d343451c1e12e1b19c780566b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Z7IZVHD%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDv4bdCo7YaY2vFK3bhVM2GR%2FzysBpJuIaIVTBfr4kI1AiBHBVqw5gKuhzt6lX8InXbCri9BSyUVnVCXZEflirrkiiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZrmCP1yLprvs%2FNsqKtwDAGB4V28bES12ceS67vUrdKx1WhZ6HQewkSrZ7Z9FwBLs3hUBlKCWigSeIQYFtL8Wg%2FHG61FPWoMlIgizkWC%2FMKkvT8%2Fm2G2So6gEgm2444oN7LQKORetPDJuSlmJfqelSok8TUDx%2FnbP7Sxk98EHo0A17bDAnO%2FEJ%2Bq3yoO2T%2BPfAbad%2BeVjxx%2Bv%2Flf4WLfbTLfCyfxTd8Mib1DyVEmj6ipm%2FlFBtPLkHQ2%2BYVsY%2BhtI0htz5Bx7mdD8fvnidPQRHGShFQZP5NXlY4bVZakwt9vyJ5j%2FtyTvdOh3DdZs%2B492iSnL3kYGMkCfCDL3hSTQuKfxkItUCwDFt2aQq0Xg%2Byb7WflG4ERAAnDBV5NOZyw2rGN0XHQGQyelSpGQSIjg6xyM6eS0L7MnFtY4LU55dBtUGBXP61C5ClbEayM1O3bhTYLTXUUMsyQITzUieYjI05D93CGYF2qNgR9lenJ%2BIk2s%2Fpq0pw9o8pIbgxPt1sjRiFrYWdgPYO%2BW3LpXXKQrTU4y4KrrlxJoX4cHZJ1hJinW1Y8JS%2FH3udBnYSi%2FFhM7FyEQNIxzWoUKcMtW7s63Ru1B7%2Bpixx5fkM5CaD8PyBfFT%2Fk%2Bd0TlKPen7nR1WRf9loDwCTEZ3KezXyww2sjwywY6pgG2irO%2BA5Mrp0vuqizHQxD9xtqfjZGUBwDcmwBZi6suO3D%2BePx5l%2BUYNhvTIkzq%2FKTtCXR0qWyFzCn0iQS3AP3ABalvMSW7DD%2BxFsjMFAa4h9BDTTATGixTl7aTXvhmKbt86H1WtPnFCjLRoc4WUCxh1N4HQlGJEyZM2o52ZkRFTbo%2FTiS9T2FJqqNiyC2HLtFHHQ%2FXAvwvHD2FumaFWivFBP9yK7XC&X-Amz-Signature=944c879f3cd078cf9684bc8125a1cb88383cccfc59f748ed2f702bc88a04faab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Z7IZVHD%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDv4bdCo7YaY2vFK3bhVM2GR%2FzysBpJuIaIVTBfr4kI1AiBHBVqw5gKuhzt6lX8InXbCri9BSyUVnVCXZEflirrkiiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZrmCP1yLprvs%2FNsqKtwDAGB4V28bES12ceS67vUrdKx1WhZ6HQewkSrZ7Z9FwBLs3hUBlKCWigSeIQYFtL8Wg%2FHG61FPWoMlIgizkWC%2FMKkvT8%2Fm2G2So6gEgm2444oN7LQKORetPDJuSlmJfqelSok8TUDx%2FnbP7Sxk98EHo0A17bDAnO%2FEJ%2Bq3yoO2T%2BPfAbad%2BeVjxx%2Bv%2Flf4WLfbTLfCyfxTd8Mib1DyVEmj6ipm%2FlFBtPLkHQ2%2BYVsY%2BhtI0htz5Bx7mdD8fvnidPQRHGShFQZP5NXlY4bVZakwt9vyJ5j%2FtyTvdOh3DdZs%2B492iSnL3kYGMkCfCDL3hSTQuKfxkItUCwDFt2aQq0Xg%2Byb7WflG4ERAAnDBV5NOZyw2rGN0XHQGQyelSpGQSIjg6xyM6eS0L7MnFtY4LU55dBtUGBXP61C5ClbEayM1O3bhTYLTXUUMsyQITzUieYjI05D93CGYF2qNgR9lenJ%2BIk2s%2Fpq0pw9o8pIbgxPt1sjRiFrYWdgPYO%2BW3LpXXKQrTU4y4KrrlxJoX4cHZJ1hJinW1Y8JS%2FH3udBnYSi%2FFhM7FyEQNIxzWoUKcMtW7s63Ru1B7%2Bpixx5fkM5CaD8PyBfFT%2Fk%2Bd0TlKPen7nR1WRf9loDwCTEZ3KezXyww2sjwywY6pgG2irO%2BA5Mrp0vuqizHQxD9xtqfjZGUBwDcmwBZi6suO3D%2BePx5l%2BUYNhvTIkzq%2FKTtCXR0qWyFzCn0iQS3AP3ABalvMSW7DD%2BxFsjMFAa4h9BDTTATGixTl7aTXvhmKbt86H1WtPnFCjLRoc4WUCxh1N4HQlGJEyZM2o52ZkRFTbo%2FTiS9T2FJqqNiyC2HLtFHHQ%2FXAvwvHD2FumaFWivFBP9yK7XC&X-Amz-Signature=2d3d5e0e6d4a2f3d7b1dd5ebb31d43390081514b45807548963210102b007282&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Z7IZVHD%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDv4bdCo7YaY2vFK3bhVM2GR%2FzysBpJuIaIVTBfr4kI1AiBHBVqw5gKuhzt6lX8InXbCri9BSyUVnVCXZEflirrkiiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZrmCP1yLprvs%2FNsqKtwDAGB4V28bES12ceS67vUrdKx1WhZ6HQewkSrZ7Z9FwBLs3hUBlKCWigSeIQYFtL8Wg%2FHG61FPWoMlIgizkWC%2FMKkvT8%2Fm2G2So6gEgm2444oN7LQKORetPDJuSlmJfqelSok8TUDx%2FnbP7Sxk98EHo0A17bDAnO%2FEJ%2Bq3yoO2T%2BPfAbad%2BeVjxx%2Bv%2Flf4WLfbTLfCyfxTd8Mib1DyVEmj6ipm%2FlFBtPLkHQ2%2BYVsY%2BhtI0htz5Bx7mdD8fvnidPQRHGShFQZP5NXlY4bVZakwt9vyJ5j%2FtyTvdOh3DdZs%2B492iSnL3kYGMkCfCDL3hSTQuKfxkItUCwDFt2aQq0Xg%2Byb7WflG4ERAAnDBV5NOZyw2rGN0XHQGQyelSpGQSIjg6xyM6eS0L7MnFtY4LU55dBtUGBXP61C5ClbEayM1O3bhTYLTXUUMsyQITzUieYjI05D93CGYF2qNgR9lenJ%2BIk2s%2Fpq0pw9o8pIbgxPt1sjRiFrYWdgPYO%2BW3LpXXKQrTU4y4KrrlxJoX4cHZJ1hJinW1Y8JS%2FH3udBnYSi%2FFhM7FyEQNIxzWoUKcMtW7s63Ru1B7%2Bpixx5fkM5CaD8PyBfFT%2Fk%2Bd0TlKPen7nR1WRf9loDwCTEZ3KezXyww2sjwywY6pgG2irO%2BA5Mrp0vuqizHQxD9xtqfjZGUBwDcmwBZi6suO3D%2BePx5l%2BUYNhvTIkzq%2FKTtCXR0qWyFzCn0iQS3AP3ABalvMSW7DD%2BxFsjMFAa4h9BDTTATGixTl7aTXvhmKbt86H1WtPnFCjLRoc4WUCxh1N4HQlGJEyZM2o52ZkRFTbo%2FTiS9T2FJqqNiyC2HLtFHHQ%2FXAvwvHD2FumaFWivFBP9yK7XC&X-Amz-Signature=4dfc9da6a2c5ff805846b73c345f3ae27901ff9bf91b496e023bdd8fbf47c612&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Z7IZVHD%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDv4bdCo7YaY2vFK3bhVM2GR%2FzysBpJuIaIVTBfr4kI1AiBHBVqw5gKuhzt6lX8InXbCri9BSyUVnVCXZEflirrkiiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZrmCP1yLprvs%2FNsqKtwDAGB4V28bES12ceS67vUrdKx1WhZ6HQewkSrZ7Z9FwBLs3hUBlKCWigSeIQYFtL8Wg%2FHG61FPWoMlIgizkWC%2FMKkvT8%2Fm2G2So6gEgm2444oN7LQKORetPDJuSlmJfqelSok8TUDx%2FnbP7Sxk98EHo0A17bDAnO%2FEJ%2Bq3yoO2T%2BPfAbad%2BeVjxx%2Bv%2Flf4WLfbTLfCyfxTd8Mib1DyVEmj6ipm%2FlFBtPLkHQ2%2BYVsY%2BhtI0htz5Bx7mdD8fvnidPQRHGShFQZP5NXlY4bVZakwt9vyJ5j%2FtyTvdOh3DdZs%2B492iSnL3kYGMkCfCDL3hSTQuKfxkItUCwDFt2aQq0Xg%2Byb7WflG4ERAAnDBV5NOZyw2rGN0XHQGQyelSpGQSIjg6xyM6eS0L7MnFtY4LU55dBtUGBXP61C5ClbEayM1O3bhTYLTXUUMsyQITzUieYjI05D93CGYF2qNgR9lenJ%2BIk2s%2Fpq0pw9o8pIbgxPt1sjRiFrYWdgPYO%2BW3LpXXKQrTU4y4KrrlxJoX4cHZJ1hJinW1Y8JS%2FH3udBnYSi%2FFhM7FyEQNIxzWoUKcMtW7s63Ru1B7%2Bpixx5fkM5CaD8PyBfFT%2Fk%2Bd0TlKPen7nR1WRf9loDwCTEZ3KezXyww2sjwywY6pgG2irO%2BA5Mrp0vuqizHQxD9xtqfjZGUBwDcmwBZi6suO3D%2BePx5l%2BUYNhvTIkzq%2FKTtCXR0qWyFzCn0iQS3AP3ABalvMSW7DD%2BxFsjMFAa4h9BDTTATGixTl7aTXvhmKbt86H1WtPnFCjLRoc4WUCxh1N4HQlGJEyZM2o52ZkRFTbo%2FTiS9T2FJqqNiyC2HLtFHHQ%2FXAvwvHD2FumaFWivFBP9yK7XC&X-Amz-Signature=74c04b5254923baaf7b3f872223b5cd345caf891019601b93bd84e6788c4b306&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

