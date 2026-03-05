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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO5AN6CA%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACjKfb%2FoF%2F4T0Nw8i6YMb121roU%2F7AwVfeCu31nG981AiBMa8P5qFhcOGAVeNK4taJ3tuABdGqt7aTVla8Jc%2BPLiCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcjnPeUhOwAWAFwAYKtwD9C4OTvLapX1sVYjtov0b0eKxyq7AGQDudu4kTgvhcQcuADmWhVsLvHXnoyINJbjXtG1tLhEEBPSWpozUUkqpjmIKf8iIjzMLDTaWhJogQoCilrvUosjo8zPrZ9d1GerCGRKxb6kd51PqeEjUzB%2F%2FN0UOH9eVWB72O%2FcVef97qTwBij4vsrzxMZa4AM%2B03TB9w2GeB9DwhgsPrAM1XaOjP%2FSvqYWgOLIwEiFiLEqu%2FiKn6bjM89k%2FU2fyISUdMo50kOgczGfNI8giP7JwuH9TQ59CXmcCfXJ%2FsCwLFdJ%2Fv8cRkWb%2BctcZ7w31L43OIZ9LOVFJRi7St2K0VOhiiTVul5Evy18ZxGACygMqCNhSKYGJlVpKDsIr9j6RCCcm9bGzaKLs7B6ejbb%2F%2FdthHhfrVptEudwGHEoez%2FAaxieU0d8cxsPScJm4J%2B6%2FPXWp3Klit0kSlhYfbZy7TKb1B%2BeDtJTasq9fHKgVjuSidpcX0ftrrA1IJ9bEJ9Q5V4mUxdBpIwvUWCJdLACxvTECa3MX4KoiSDZRxvb7gyJneBdaFvdRJ1up5IopENQObIBNzUqWt7WSWfsUvtm%2FIqqLiiMeP%2BawdbhASk6TsoNGvk5sUIUdfVRJiwmxniQMdOswlt%2BjzQY6pgHFR9cx70Y7JOywn%2F9P5Uh7XYyF7otkR26UmMjxYoewwQ4aFNMd%2BBkhrvIRaeYKfFIOGTaCIey2X5t2Y66ZOuzeKs%2BOsALMfKrlcT79Kh42B7nQhPKs3F4R0ZLgojz34D63sp9rBJ4Uysl9lRXDilENdmGLNJCBEOejjl2e7Uhqd8Hody2mlDy2Xle0e%2FDNjd777fY5pQEYfQEZtTMr9ubsu33S%2Fu0v&X-Amz-Signature=9a5cd965f546e4f688eb5c175813bf9a17dbac6b643e4f177c91e21f70438b77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO5AN6CA%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACjKfb%2FoF%2F4T0Nw8i6YMb121roU%2F7AwVfeCu31nG981AiBMa8P5qFhcOGAVeNK4taJ3tuABdGqt7aTVla8Jc%2BPLiCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcjnPeUhOwAWAFwAYKtwD9C4OTvLapX1sVYjtov0b0eKxyq7AGQDudu4kTgvhcQcuADmWhVsLvHXnoyINJbjXtG1tLhEEBPSWpozUUkqpjmIKf8iIjzMLDTaWhJogQoCilrvUosjo8zPrZ9d1GerCGRKxb6kd51PqeEjUzB%2F%2FN0UOH9eVWB72O%2FcVef97qTwBij4vsrzxMZa4AM%2B03TB9w2GeB9DwhgsPrAM1XaOjP%2FSvqYWgOLIwEiFiLEqu%2FiKn6bjM89k%2FU2fyISUdMo50kOgczGfNI8giP7JwuH9TQ59CXmcCfXJ%2FsCwLFdJ%2Fv8cRkWb%2BctcZ7w31L43OIZ9LOVFJRi7St2K0VOhiiTVul5Evy18ZxGACygMqCNhSKYGJlVpKDsIr9j6RCCcm9bGzaKLs7B6ejbb%2F%2FdthHhfrVptEudwGHEoez%2FAaxieU0d8cxsPScJm4J%2B6%2FPXWp3Klit0kSlhYfbZy7TKb1B%2BeDtJTasq9fHKgVjuSidpcX0ftrrA1IJ9bEJ9Q5V4mUxdBpIwvUWCJdLACxvTECa3MX4KoiSDZRxvb7gyJneBdaFvdRJ1up5IopENQObIBNzUqWt7WSWfsUvtm%2FIqqLiiMeP%2BawdbhASk6TsoNGvk5sUIUdfVRJiwmxniQMdOswlt%2BjzQY6pgHFR9cx70Y7JOywn%2F9P5Uh7XYyF7otkR26UmMjxYoewwQ4aFNMd%2BBkhrvIRaeYKfFIOGTaCIey2X5t2Y66ZOuzeKs%2BOsALMfKrlcT79Kh42B7nQhPKs3F4R0ZLgojz34D63sp9rBJ4Uysl9lRXDilENdmGLNJCBEOejjl2e7Uhqd8Hody2mlDy2Xle0e%2FDNjd777fY5pQEYfQEZtTMr9ubsu33S%2Fu0v&X-Amz-Signature=0734b27baa5343062aa60f691e76ab3939bd4f01c142bcab1f2fd0cbff35fcab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO5AN6CA%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACjKfb%2FoF%2F4T0Nw8i6YMb121roU%2F7AwVfeCu31nG981AiBMa8P5qFhcOGAVeNK4taJ3tuABdGqt7aTVla8Jc%2BPLiCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcjnPeUhOwAWAFwAYKtwD9C4OTvLapX1sVYjtov0b0eKxyq7AGQDudu4kTgvhcQcuADmWhVsLvHXnoyINJbjXtG1tLhEEBPSWpozUUkqpjmIKf8iIjzMLDTaWhJogQoCilrvUosjo8zPrZ9d1GerCGRKxb6kd51PqeEjUzB%2F%2FN0UOH9eVWB72O%2FcVef97qTwBij4vsrzxMZa4AM%2B03TB9w2GeB9DwhgsPrAM1XaOjP%2FSvqYWgOLIwEiFiLEqu%2FiKn6bjM89k%2FU2fyISUdMo50kOgczGfNI8giP7JwuH9TQ59CXmcCfXJ%2FsCwLFdJ%2Fv8cRkWb%2BctcZ7w31L43OIZ9LOVFJRi7St2K0VOhiiTVul5Evy18ZxGACygMqCNhSKYGJlVpKDsIr9j6RCCcm9bGzaKLs7B6ejbb%2F%2FdthHhfrVptEudwGHEoez%2FAaxieU0d8cxsPScJm4J%2B6%2FPXWp3Klit0kSlhYfbZy7TKb1B%2BeDtJTasq9fHKgVjuSidpcX0ftrrA1IJ9bEJ9Q5V4mUxdBpIwvUWCJdLACxvTECa3MX4KoiSDZRxvb7gyJneBdaFvdRJ1up5IopENQObIBNzUqWt7WSWfsUvtm%2FIqqLiiMeP%2BawdbhASk6TsoNGvk5sUIUdfVRJiwmxniQMdOswlt%2BjzQY6pgHFR9cx70Y7JOywn%2F9P5Uh7XYyF7otkR26UmMjxYoewwQ4aFNMd%2BBkhrvIRaeYKfFIOGTaCIey2X5t2Y66ZOuzeKs%2BOsALMfKrlcT79Kh42B7nQhPKs3F4R0ZLgojz34D63sp9rBJ4Uysl9lRXDilENdmGLNJCBEOejjl2e7Uhqd8Hody2mlDy2Xle0e%2FDNjd777fY5pQEYfQEZtTMr9ubsu33S%2Fu0v&X-Amz-Signature=ccc4128a4013bc5ab43019f00622fea7133a5a023b4af7f205920b1fa86606f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO5AN6CA%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACjKfb%2FoF%2F4T0Nw8i6YMb121roU%2F7AwVfeCu31nG981AiBMa8P5qFhcOGAVeNK4taJ3tuABdGqt7aTVla8Jc%2BPLiCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcjnPeUhOwAWAFwAYKtwD9C4OTvLapX1sVYjtov0b0eKxyq7AGQDudu4kTgvhcQcuADmWhVsLvHXnoyINJbjXtG1tLhEEBPSWpozUUkqpjmIKf8iIjzMLDTaWhJogQoCilrvUosjo8zPrZ9d1GerCGRKxb6kd51PqeEjUzB%2F%2FN0UOH9eVWB72O%2FcVef97qTwBij4vsrzxMZa4AM%2B03TB9w2GeB9DwhgsPrAM1XaOjP%2FSvqYWgOLIwEiFiLEqu%2FiKn6bjM89k%2FU2fyISUdMo50kOgczGfNI8giP7JwuH9TQ59CXmcCfXJ%2FsCwLFdJ%2Fv8cRkWb%2BctcZ7w31L43OIZ9LOVFJRi7St2K0VOhiiTVul5Evy18ZxGACygMqCNhSKYGJlVpKDsIr9j6RCCcm9bGzaKLs7B6ejbb%2F%2FdthHhfrVptEudwGHEoez%2FAaxieU0d8cxsPScJm4J%2B6%2FPXWp3Klit0kSlhYfbZy7TKb1B%2BeDtJTasq9fHKgVjuSidpcX0ftrrA1IJ9bEJ9Q5V4mUxdBpIwvUWCJdLACxvTECa3MX4KoiSDZRxvb7gyJneBdaFvdRJ1up5IopENQObIBNzUqWt7WSWfsUvtm%2FIqqLiiMeP%2BawdbhASk6TsoNGvk5sUIUdfVRJiwmxniQMdOswlt%2BjzQY6pgHFR9cx70Y7JOywn%2F9P5Uh7XYyF7otkR26UmMjxYoewwQ4aFNMd%2BBkhrvIRaeYKfFIOGTaCIey2X5t2Y66ZOuzeKs%2BOsALMfKrlcT79Kh42B7nQhPKs3F4R0ZLgojz34D63sp9rBJ4Uysl9lRXDilENdmGLNJCBEOejjl2e7Uhqd8Hody2mlDy2Xle0e%2FDNjd777fY5pQEYfQEZtTMr9ubsu33S%2Fu0v&X-Amz-Signature=769386433a91676327d979b8c1ef44368c4014e034dcb87cbbdb10f89efe3222&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO5AN6CA%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACjKfb%2FoF%2F4T0Nw8i6YMb121roU%2F7AwVfeCu31nG981AiBMa8P5qFhcOGAVeNK4taJ3tuABdGqt7aTVla8Jc%2BPLiCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcjnPeUhOwAWAFwAYKtwD9C4OTvLapX1sVYjtov0b0eKxyq7AGQDudu4kTgvhcQcuADmWhVsLvHXnoyINJbjXtG1tLhEEBPSWpozUUkqpjmIKf8iIjzMLDTaWhJogQoCilrvUosjo8zPrZ9d1GerCGRKxb6kd51PqeEjUzB%2F%2FN0UOH9eVWB72O%2FcVef97qTwBij4vsrzxMZa4AM%2B03TB9w2GeB9DwhgsPrAM1XaOjP%2FSvqYWgOLIwEiFiLEqu%2FiKn6bjM89k%2FU2fyISUdMo50kOgczGfNI8giP7JwuH9TQ59CXmcCfXJ%2FsCwLFdJ%2Fv8cRkWb%2BctcZ7w31L43OIZ9LOVFJRi7St2K0VOhiiTVul5Evy18ZxGACygMqCNhSKYGJlVpKDsIr9j6RCCcm9bGzaKLs7B6ejbb%2F%2FdthHhfrVptEudwGHEoez%2FAaxieU0d8cxsPScJm4J%2B6%2FPXWp3Klit0kSlhYfbZy7TKb1B%2BeDtJTasq9fHKgVjuSidpcX0ftrrA1IJ9bEJ9Q5V4mUxdBpIwvUWCJdLACxvTECa3MX4KoiSDZRxvb7gyJneBdaFvdRJ1up5IopENQObIBNzUqWt7WSWfsUvtm%2FIqqLiiMeP%2BawdbhASk6TsoNGvk5sUIUdfVRJiwmxniQMdOswlt%2BjzQY6pgHFR9cx70Y7JOywn%2F9P5Uh7XYyF7otkR26UmMjxYoewwQ4aFNMd%2BBkhrvIRaeYKfFIOGTaCIey2X5t2Y66ZOuzeKs%2BOsALMfKrlcT79Kh42B7nQhPKs3F4R0ZLgojz34D63sp9rBJ4Uysl9lRXDilENdmGLNJCBEOejjl2e7Uhqd8Hody2mlDy2Xle0e%2FDNjd777fY5pQEYfQEZtTMr9ubsu33S%2Fu0v&X-Amz-Signature=0d9cc0afb99020500fc76bf26db9212024774dbd21bec1940049bf8657fc206c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO5AN6CA%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACjKfb%2FoF%2F4T0Nw8i6YMb121roU%2F7AwVfeCu31nG981AiBMa8P5qFhcOGAVeNK4taJ3tuABdGqt7aTVla8Jc%2BPLiCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcjnPeUhOwAWAFwAYKtwD9C4OTvLapX1sVYjtov0b0eKxyq7AGQDudu4kTgvhcQcuADmWhVsLvHXnoyINJbjXtG1tLhEEBPSWpozUUkqpjmIKf8iIjzMLDTaWhJogQoCilrvUosjo8zPrZ9d1GerCGRKxb6kd51PqeEjUzB%2F%2FN0UOH9eVWB72O%2FcVef97qTwBij4vsrzxMZa4AM%2B03TB9w2GeB9DwhgsPrAM1XaOjP%2FSvqYWgOLIwEiFiLEqu%2FiKn6bjM89k%2FU2fyISUdMo50kOgczGfNI8giP7JwuH9TQ59CXmcCfXJ%2FsCwLFdJ%2Fv8cRkWb%2BctcZ7w31L43OIZ9LOVFJRi7St2K0VOhiiTVul5Evy18ZxGACygMqCNhSKYGJlVpKDsIr9j6RCCcm9bGzaKLs7B6ejbb%2F%2FdthHhfrVptEudwGHEoez%2FAaxieU0d8cxsPScJm4J%2B6%2FPXWp3Klit0kSlhYfbZy7TKb1B%2BeDtJTasq9fHKgVjuSidpcX0ftrrA1IJ9bEJ9Q5V4mUxdBpIwvUWCJdLACxvTECa3MX4KoiSDZRxvb7gyJneBdaFvdRJ1up5IopENQObIBNzUqWt7WSWfsUvtm%2FIqqLiiMeP%2BawdbhASk6TsoNGvk5sUIUdfVRJiwmxniQMdOswlt%2BjzQY6pgHFR9cx70Y7JOywn%2F9P5Uh7XYyF7otkR26UmMjxYoewwQ4aFNMd%2BBkhrvIRaeYKfFIOGTaCIey2X5t2Y66ZOuzeKs%2BOsALMfKrlcT79Kh42B7nQhPKs3F4R0ZLgojz34D63sp9rBJ4Uysl9lRXDilENdmGLNJCBEOejjl2e7Uhqd8Hody2mlDy2Xle0e%2FDNjd777fY5pQEYfQEZtTMr9ubsu33S%2Fu0v&X-Amz-Signature=0878f95fd14f7dfe4ea1a82dfadff8c499898a6f9322bf166a0b6892a036da35&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO5AN6CA%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACjKfb%2FoF%2F4T0Nw8i6YMb121roU%2F7AwVfeCu31nG981AiBMa8P5qFhcOGAVeNK4taJ3tuABdGqt7aTVla8Jc%2BPLiCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcjnPeUhOwAWAFwAYKtwD9C4OTvLapX1sVYjtov0b0eKxyq7AGQDudu4kTgvhcQcuADmWhVsLvHXnoyINJbjXtG1tLhEEBPSWpozUUkqpjmIKf8iIjzMLDTaWhJogQoCilrvUosjo8zPrZ9d1GerCGRKxb6kd51PqeEjUzB%2F%2FN0UOH9eVWB72O%2FcVef97qTwBij4vsrzxMZa4AM%2B03TB9w2GeB9DwhgsPrAM1XaOjP%2FSvqYWgOLIwEiFiLEqu%2FiKn6bjM89k%2FU2fyISUdMo50kOgczGfNI8giP7JwuH9TQ59CXmcCfXJ%2FsCwLFdJ%2Fv8cRkWb%2BctcZ7w31L43OIZ9LOVFJRi7St2K0VOhiiTVul5Evy18ZxGACygMqCNhSKYGJlVpKDsIr9j6RCCcm9bGzaKLs7B6ejbb%2F%2FdthHhfrVptEudwGHEoez%2FAaxieU0d8cxsPScJm4J%2B6%2FPXWp3Klit0kSlhYfbZy7TKb1B%2BeDtJTasq9fHKgVjuSidpcX0ftrrA1IJ9bEJ9Q5V4mUxdBpIwvUWCJdLACxvTECa3MX4KoiSDZRxvb7gyJneBdaFvdRJ1up5IopENQObIBNzUqWt7WSWfsUvtm%2FIqqLiiMeP%2BawdbhASk6TsoNGvk5sUIUdfVRJiwmxniQMdOswlt%2BjzQY6pgHFR9cx70Y7JOywn%2F9P5Uh7XYyF7otkR26UmMjxYoewwQ4aFNMd%2BBkhrvIRaeYKfFIOGTaCIey2X5t2Y66ZOuzeKs%2BOsALMfKrlcT79Kh42B7nQhPKs3F4R0ZLgojz34D63sp9rBJ4Uysl9lRXDilENdmGLNJCBEOejjl2e7Uhqd8Hody2mlDy2Xle0e%2FDNjd777fY5pQEYfQEZtTMr9ubsu33S%2Fu0v&X-Amz-Signature=822389301c4e7725aaece3ead59a0894b3e8e622b5f979ae019dde28567495d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

