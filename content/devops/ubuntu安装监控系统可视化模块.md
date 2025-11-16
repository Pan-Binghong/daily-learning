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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQCPGM6C%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T025017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFUWj7SxWaF905UyAeA6xspIIzbtOe9QyIW38xHvNzgAIgJtfljnRkVjidgKv2MFn27lie%2F5Mx2X8wNi2N7T77tZoqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGFx%2FM37O%2BHNeQxPkSrcA%2F088EdZ4GkzjC6Mx%2B7YPiSJXokQmhS0E2ZprOnDE0Ooukb7LXReP1JHB08cqeQv8%2FHJWB0TsmhBpxqiCOCR%2BkwzOqNPFbmjjKR7S4F0vuDVFFYWJzogSajGB2m%2F0NSlVlmX7eHwleweaQEafIc%2Bl1Ox5cnyZxYnYRO1pdxIgPzIWxVQraudlJlqrZhPRLpRiy2%2Fsot2fXBoywYDOmnSlko%2F2f4zoniWYZwAdJULN%2BhTQWznabW7dIJmYQrCieGYMIqy8U%2B6H5qbsoeDtGOKK1Y0fHXq0wLAiqxVYugOx7a%2B5GuKOtdjGYmqHSI6cKexFCSFxNb3ZidaFB9OYRucoAMm2Jzi5CUpW1z6ZDJ6g8XJGk3piHsGZ6wAaXbApbBYQIVNLutrfDDivJZlxRPX6TkkNsXz%2BlvmTDw0X491w8XoiPstYt8BvoYerRCCwVxUigI2DIyEEv%2FcFusUOOn%2BZG0VB4okbPs9f%2FugKr0HybEJ934jbKvC67u70%2BTaySV%2F%2FvPOcoP47WrVyzjBAraGeuabm92IKjedgGkXdzjbxUqnwmLlOeKnGkvKRb2mGGc%2F8INoaL6s9yMrHw9rk20JLCxyk1839IuqELWEMBsMb63%2BrwR1MsXzVSImYnxZMKbh5MgGOqUBYyTeAwjastOjod6Kbsre33F%2FPy2ApkwgtV808MLv7s3W0ilrzr46xVFXsEEnUS%2ByRHsFOiyj%2BIdfMNwasitnure6oAvIUgZaKNnOuP4hBM1K0pF2Zp169fc7qt7xOYMqhZwUBXsO6mz2uTHcsWd5172zStmBVRndLICBNQ7M1%2FXDc5wdO%2FNaQ3N%2BMhb6BXzDCCKbS8lsnwzt1jB46DGqX1Uaqw9r&X-Amz-Signature=776cccc5df853e43ddbd02520ad5b4792ae053b32b5253c518e48d47ed33997b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQCPGM6C%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T025017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFUWj7SxWaF905UyAeA6xspIIzbtOe9QyIW38xHvNzgAIgJtfljnRkVjidgKv2MFn27lie%2F5Mx2X8wNi2N7T77tZoqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGFx%2FM37O%2BHNeQxPkSrcA%2F088EdZ4GkzjC6Mx%2B7YPiSJXokQmhS0E2ZprOnDE0Ooukb7LXReP1JHB08cqeQv8%2FHJWB0TsmhBpxqiCOCR%2BkwzOqNPFbmjjKR7S4F0vuDVFFYWJzogSajGB2m%2F0NSlVlmX7eHwleweaQEafIc%2Bl1Ox5cnyZxYnYRO1pdxIgPzIWxVQraudlJlqrZhPRLpRiy2%2Fsot2fXBoywYDOmnSlko%2F2f4zoniWYZwAdJULN%2BhTQWznabW7dIJmYQrCieGYMIqy8U%2B6H5qbsoeDtGOKK1Y0fHXq0wLAiqxVYugOx7a%2B5GuKOtdjGYmqHSI6cKexFCSFxNb3ZidaFB9OYRucoAMm2Jzi5CUpW1z6ZDJ6g8XJGk3piHsGZ6wAaXbApbBYQIVNLutrfDDivJZlxRPX6TkkNsXz%2BlvmTDw0X491w8XoiPstYt8BvoYerRCCwVxUigI2DIyEEv%2FcFusUOOn%2BZG0VB4okbPs9f%2FugKr0HybEJ934jbKvC67u70%2BTaySV%2F%2FvPOcoP47WrVyzjBAraGeuabm92IKjedgGkXdzjbxUqnwmLlOeKnGkvKRb2mGGc%2F8INoaL6s9yMrHw9rk20JLCxyk1839IuqELWEMBsMb63%2BrwR1MsXzVSImYnxZMKbh5MgGOqUBYyTeAwjastOjod6Kbsre33F%2FPy2ApkwgtV808MLv7s3W0ilrzr46xVFXsEEnUS%2ByRHsFOiyj%2BIdfMNwasitnure6oAvIUgZaKNnOuP4hBM1K0pF2Zp169fc7qt7xOYMqhZwUBXsO6mz2uTHcsWd5172zStmBVRndLICBNQ7M1%2FXDc5wdO%2FNaQ3N%2BMhb6BXzDCCKbS8lsnwzt1jB46DGqX1Uaqw9r&X-Amz-Signature=0fff0bedf39f0482896c097804a09805759ab0ebe1aebef6b5c9a0201f8dc787&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQCPGM6C%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T025017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFUWj7SxWaF905UyAeA6xspIIzbtOe9QyIW38xHvNzgAIgJtfljnRkVjidgKv2MFn27lie%2F5Mx2X8wNi2N7T77tZoqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGFx%2FM37O%2BHNeQxPkSrcA%2F088EdZ4GkzjC6Mx%2B7YPiSJXokQmhS0E2ZprOnDE0Ooukb7LXReP1JHB08cqeQv8%2FHJWB0TsmhBpxqiCOCR%2BkwzOqNPFbmjjKR7S4F0vuDVFFYWJzogSajGB2m%2F0NSlVlmX7eHwleweaQEafIc%2Bl1Ox5cnyZxYnYRO1pdxIgPzIWxVQraudlJlqrZhPRLpRiy2%2Fsot2fXBoywYDOmnSlko%2F2f4zoniWYZwAdJULN%2BhTQWznabW7dIJmYQrCieGYMIqy8U%2B6H5qbsoeDtGOKK1Y0fHXq0wLAiqxVYugOx7a%2B5GuKOtdjGYmqHSI6cKexFCSFxNb3ZidaFB9OYRucoAMm2Jzi5CUpW1z6ZDJ6g8XJGk3piHsGZ6wAaXbApbBYQIVNLutrfDDivJZlxRPX6TkkNsXz%2BlvmTDw0X491w8XoiPstYt8BvoYerRCCwVxUigI2DIyEEv%2FcFusUOOn%2BZG0VB4okbPs9f%2FugKr0HybEJ934jbKvC67u70%2BTaySV%2F%2FvPOcoP47WrVyzjBAraGeuabm92IKjedgGkXdzjbxUqnwmLlOeKnGkvKRb2mGGc%2F8INoaL6s9yMrHw9rk20JLCxyk1839IuqELWEMBsMb63%2BrwR1MsXzVSImYnxZMKbh5MgGOqUBYyTeAwjastOjod6Kbsre33F%2FPy2ApkwgtV808MLv7s3W0ilrzr46xVFXsEEnUS%2ByRHsFOiyj%2BIdfMNwasitnure6oAvIUgZaKNnOuP4hBM1K0pF2Zp169fc7qt7xOYMqhZwUBXsO6mz2uTHcsWd5172zStmBVRndLICBNQ7M1%2FXDc5wdO%2FNaQ3N%2BMhb6BXzDCCKbS8lsnwzt1jB46DGqX1Uaqw9r&X-Amz-Signature=01d4318031e619594b78acfec87a481b748f3aa0c70345359694fe3804b9e700&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQCPGM6C%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T025017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFUWj7SxWaF905UyAeA6xspIIzbtOe9QyIW38xHvNzgAIgJtfljnRkVjidgKv2MFn27lie%2F5Mx2X8wNi2N7T77tZoqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGFx%2FM37O%2BHNeQxPkSrcA%2F088EdZ4GkzjC6Mx%2B7YPiSJXokQmhS0E2ZprOnDE0Ooukb7LXReP1JHB08cqeQv8%2FHJWB0TsmhBpxqiCOCR%2BkwzOqNPFbmjjKR7S4F0vuDVFFYWJzogSajGB2m%2F0NSlVlmX7eHwleweaQEafIc%2Bl1Ox5cnyZxYnYRO1pdxIgPzIWxVQraudlJlqrZhPRLpRiy2%2Fsot2fXBoywYDOmnSlko%2F2f4zoniWYZwAdJULN%2BhTQWznabW7dIJmYQrCieGYMIqy8U%2B6H5qbsoeDtGOKK1Y0fHXq0wLAiqxVYugOx7a%2B5GuKOtdjGYmqHSI6cKexFCSFxNb3ZidaFB9OYRucoAMm2Jzi5CUpW1z6ZDJ6g8XJGk3piHsGZ6wAaXbApbBYQIVNLutrfDDivJZlxRPX6TkkNsXz%2BlvmTDw0X491w8XoiPstYt8BvoYerRCCwVxUigI2DIyEEv%2FcFusUOOn%2BZG0VB4okbPs9f%2FugKr0HybEJ934jbKvC67u70%2BTaySV%2F%2FvPOcoP47WrVyzjBAraGeuabm92IKjedgGkXdzjbxUqnwmLlOeKnGkvKRb2mGGc%2F8INoaL6s9yMrHw9rk20JLCxyk1839IuqELWEMBsMb63%2BrwR1MsXzVSImYnxZMKbh5MgGOqUBYyTeAwjastOjod6Kbsre33F%2FPy2ApkwgtV808MLv7s3W0ilrzr46xVFXsEEnUS%2ByRHsFOiyj%2BIdfMNwasitnure6oAvIUgZaKNnOuP4hBM1K0pF2Zp169fc7qt7xOYMqhZwUBXsO6mz2uTHcsWd5172zStmBVRndLICBNQ7M1%2FXDc5wdO%2FNaQ3N%2BMhb6BXzDCCKbS8lsnwzt1jB46DGqX1Uaqw9r&X-Amz-Signature=a429721c0b976901633ad4d24e6233de73597d3c1507f32312cc9d314220fa80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQCPGM6C%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T025017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFUWj7SxWaF905UyAeA6xspIIzbtOe9QyIW38xHvNzgAIgJtfljnRkVjidgKv2MFn27lie%2F5Mx2X8wNi2N7T77tZoqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGFx%2FM37O%2BHNeQxPkSrcA%2F088EdZ4GkzjC6Mx%2B7YPiSJXokQmhS0E2ZprOnDE0Ooukb7LXReP1JHB08cqeQv8%2FHJWB0TsmhBpxqiCOCR%2BkwzOqNPFbmjjKR7S4F0vuDVFFYWJzogSajGB2m%2F0NSlVlmX7eHwleweaQEafIc%2Bl1Ox5cnyZxYnYRO1pdxIgPzIWxVQraudlJlqrZhPRLpRiy2%2Fsot2fXBoywYDOmnSlko%2F2f4zoniWYZwAdJULN%2BhTQWznabW7dIJmYQrCieGYMIqy8U%2B6H5qbsoeDtGOKK1Y0fHXq0wLAiqxVYugOx7a%2B5GuKOtdjGYmqHSI6cKexFCSFxNb3ZidaFB9OYRucoAMm2Jzi5CUpW1z6ZDJ6g8XJGk3piHsGZ6wAaXbApbBYQIVNLutrfDDivJZlxRPX6TkkNsXz%2BlvmTDw0X491w8XoiPstYt8BvoYerRCCwVxUigI2DIyEEv%2FcFusUOOn%2BZG0VB4okbPs9f%2FugKr0HybEJ934jbKvC67u70%2BTaySV%2F%2FvPOcoP47WrVyzjBAraGeuabm92IKjedgGkXdzjbxUqnwmLlOeKnGkvKRb2mGGc%2F8INoaL6s9yMrHw9rk20JLCxyk1839IuqELWEMBsMb63%2BrwR1MsXzVSImYnxZMKbh5MgGOqUBYyTeAwjastOjod6Kbsre33F%2FPy2ApkwgtV808MLv7s3W0ilrzr46xVFXsEEnUS%2ByRHsFOiyj%2BIdfMNwasitnure6oAvIUgZaKNnOuP4hBM1K0pF2Zp169fc7qt7xOYMqhZwUBXsO6mz2uTHcsWd5172zStmBVRndLICBNQ7M1%2FXDc5wdO%2FNaQ3N%2BMhb6BXzDCCKbS8lsnwzt1jB46DGqX1Uaqw9r&X-Amz-Signature=cdd52ddcd5f75707e2743a21dac6e63d849903e7f488ad709cfd0b946d1a7635&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQCPGM6C%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T025017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFUWj7SxWaF905UyAeA6xspIIzbtOe9QyIW38xHvNzgAIgJtfljnRkVjidgKv2MFn27lie%2F5Mx2X8wNi2N7T77tZoqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGFx%2FM37O%2BHNeQxPkSrcA%2F088EdZ4GkzjC6Mx%2B7YPiSJXokQmhS0E2ZprOnDE0Ooukb7LXReP1JHB08cqeQv8%2FHJWB0TsmhBpxqiCOCR%2BkwzOqNPFbmjjKR7S4F0vuDVFFYWJzogSajGB2m%2F0NSlVlmX7eHwleweaQEafIc%2Bl1Ox5cnyZxYnYRO1pdxIgPzIWxVQraudlJlqrZhPRLpRiy2%2Fsot2fXBoywYDOmnSlko%2F2f4zoniWYZwAdJULN%2BhTQWznabW7dIJmYQrCieGYMIqy8U%2B6H5qbsoeDtGOKK1Y0fHXq0wLAiqxVYugOx7a%2B5GuKOtdjGYmqHSI6cKexFCSFxNb3ZidaFB9OYRucoAMm2Jzi5CUpW1z6ZDJ6g8XJGk3piHsGZ6wAaXbApbBYQIVNLutrfDDivJZlxRPX6TkkNsXz%2BlvmTDw0X491w8XoiPstYt8BvoYerRCCwVxUigI2DIyEEv%2FcFusUOOn%2BZG0VB4okbPs9f%2FugKr0HybEJ934jbKvC67u70%2BTaySV%2F%2FvPOcoP47WrVyzjBAraGeuabm92IKjedgGkXdzjbxUqnwmLlOeKnGkvKRb2mGGc%2F8INoaL6s9yMrHw9rk20JLCxyk1839IuqELWEMBsMb63%2BrwR1MsXzVSImYnxZMKbh5MgGOqUBYyTeAwjastOjod6Kbsre33F%2FPy2ApkwgtV808MLv7s3W0ilrzr46xVFXsEEnUS%2ByRHsFOiyj%2BIdfMNwasitnure6oAvIUgZaKNnOuP4hBM1K0pF2Zp169fc7qt7xOYMqhZwUBXsO6mz2uTHcsWd5172zStmBVRndLICBNQ7M1%2FXDc5wdO%2FNaQ3N%2BMhb6BXzDCCKbS8lsnwzt1jB46DGqX1Uaqw9r&X-Amz-Signature=adaa645c0012f5f4f093657092ecc7336d19487f3739179dc69a21bcd0484ae7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQCPGM6C%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T025017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFUWj7SxWaF905UyAeA6xspIIzbtOe9QyIW38xHvNzgAIgJtfljnRkVjidgKv2MFn27lie%2F5Mx2X8wNi2N7T77tZoqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGFx%2FM37O%2BHNeQxPkSrcA%2F088EdZ4GkzjC6Mx%2B7YPiSJXokQmhS0E2ZprOnDE0Ooukb7LXReP1JHB08cqeQv8%2FHJWB0TsmhBpxqiCOCR%2BkwzOqNPFbmjjKR7S4F0vuDVFFYWJzogSajGB2m%2F0NSlVlmX7eHwleweaQEafIc%2Bl1Ox5cnyZxYnYRO1pdxIgPzIWxVQraudlJlqrZhPRLpRiy2%2Fsot2fXBoywYDOmnSlko%2F2f4zoniWYZwAdJULN%2BhTQWznabW7dIJmYQrCieGYMIqy8U%2B6H5qbsoeDtGOKK1Y0fHXq0wLAiqxVYugOx7a%2B5GuKOtdjGYmqHSI6cKexFCSFxNb3ZidaFB9OYRucoAMm2Jzi5CUpW1z6ZDJ6g8XJGk3piHsGZ6wAaXbApbBYQIVNLutrfDDivJZlxRPX6TkkNsXz%2BlvmTDw0X491w8XoiPstYt8BvoYerRCCwVxUigI2DIyEEv%2FcFusUOOn%2BZG0VB4okbPs9f%2FugKr0HybEJ934jbKvC67u70%2BTaySV%2F%2FvPOcoP47WrVyzjBAraGeuabm92IKjedgGkXdzjbxUqnwmLlOeKnGkvKRb2mGGc%2F8INoaL6s9yMrHw9rk20JLCxyk1839IuqELWEMBsMb63%2BrwR1MsXzVSImYnxZMKbh5MgGOqUBYyTeAwjastOjod6Kbsre33F%2FPy2ApkwgtV808MLv7s3W0ilrzr46xVFXsEEnUS%2ByRHsFOiyj%2BIdfMNwasitnure6oAvIUgZaKNnOuP4hBM1K0pF2Zp169fc7qt7xOYMqhZwUBXsO6mz2uTHcsWd5172zStmBVRndLICBNQ7M1%2FXDc5wdO%2FNaQ3N%2BMhb6BXzDCCKbS8lsnwzt1jB46DGqX1Uaqw9r&X-Amz-Signature=ea59a7bcea596851fe80ab7aabeb5e40719e2448044aefb6c7dfd23b220cd15f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

