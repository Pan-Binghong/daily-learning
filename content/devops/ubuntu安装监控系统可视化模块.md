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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NOISZPO%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyb0Pofk6UpCGGnxJVlxXGOAlRkAzfAdsGnWvRAmVVjQIgIA81WKvCqui9k1CUuowwLZFzjXVcvr2GYuDsdYukslAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDJDaIxQkfUnwJmh9eircA%2F%2FWMy4R3QLWFxupDQ6pP%2FDNaXrKhOfM8LHlO50ms8ood%2Bs%2FKD6ChSXy%2FUCOpHVrR21jZRRZ4vogHtvcQVB3tXsedAdFEE5dIMlzscCMLFdFb8TcHEsny%2FRXoJ9jRrFfT%2BRGTMMF6Jte7Q3pgYyQltiAZ0el0WjTresmsbNuLlrTOIkBPBLlu12TXraQSY3rAw0VMwUo20nLqYsM%2FsotrP6ZwJuKohUcBQf0PKtT2ZnLHGr486AW5a9a5aVr9HE%2FoM52JMZXlxH%2BlBU1DGmLvoVv1nUjg4lNWFCDSx9m7yoeQytTlEEH4%2B6GVa%2FEmGJm2l%2BUs66m%2FEc%2FXicp3cZ5B7xFqWoNExKz8c2CbRxbwwqLGRYvCj2jnVjDBXVV9dSrn7g92beaRNKRygEAEXH1KOaJrg72jjXLLy7VGEaJVk3XD%2B3YpQ27dlzraJPmCyK%2Fm9ZIghpuz3eEe76Llkasnp3DbqMU9rgPPRUvS5%2Btt1ncK5M%2B7uN6d%2FDFa6yx6K%2Fjecm0%2F%2FC0OOtSqYyzkaia6OoXJ4ZlbK2b3sApeXihnqtvuw%2BhipeaBxIq%2Bl3KApvAZLVxugD0ZsXyYXQmIRxIlCSYU9aRa8pBpkECHoOJ1LX6b1d%2FYuJSMIM%2BSurLMMuxiMoGOqUBiwkYvyLKl21X8cbakRFAFOk7HHgU0c0DcUDrqjFi%2BM1jPNPwX6%2FfTYs%2BSJr%2B6YQdXkrkkK6p%2B5ijZ5FKZkCfc4id3PzPB2Jv1TfYsem%2Fu%2BzkTqkhytu4MLZ3CTNAu4pwuYAe2ervd65JFSmGqpuuLH5CYY39DaF1a%2FV0HTVivj75kczX3w5%2FO2OxHkGxiCTT%2FtBQCRjl6B06D0JBd7a2q2jhMkIn&X-Amz-Signature=9066336fe01edb73a036548efe68649462ec76df105130c5fb9e2773c1ec0ab1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NOISZPO%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyb0Pofk6UpCGGnxJVlxXGOAlRkAzfAdsGnWvRAmVVjQIgIA81WKvCqui9k1CUuowwLZFzjXVcvr2GYuDsdYukslAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDJDaIxQkfUnwJmh9eircA%2F%2FWMy4R3QLWFxupDQ6pP%2FDNaXrKhOfM8LHlO50ms8ood%2Bs%2FKD6ChSXy%2FUCOpHVrR21jZRRZ4vogHtvcQVB3tXsedAdFEE5dIMlzscCMLFdFb8TcHEsny%2FRXoJ9jRrFfT%2BRGTMMF6Jte7Q3pgYyQltiAZ0el0WjTresmsbNuLlrTOIkBPBLlu12TXraQSY3rAw0VMwUo20nLqYsM%2FsotrP6ZwJuKohUcBQf0PKtT2ZnLHGr486AW5a9a5aVr9HE%2FoM52JMZXlxH%2BlBU1DGmLvoVv1nUjg4lNWFCDSx9m7yoeQytTlEEH4%2B6GVa%2FEmGJm2l%2BUs66m%2FEc%2FXicp3cZ5B7xFqWoNExKz8c2CbRxbwwqLGRYvCj2jnVjDBXVV9dSrn7g92beaRNKRygEAEXH1KOaJrg72jjXLLy7VGEaJVk3XD%2B3YpQ27dlzraJPmCyK%2Fm9ZIghpuz3eEe76Llkasnp3DbqMU9rgPPRUvS5%2Btt1ncK5M%2B7uN6d%2FDFa6yx6K%2Fjecm0%2F%2FC0OOtSqYyzkaia6OoXJ4ZlbK2b3sApeXihnqtvuw%2BhipeaBxIq%2Bl3KApvAZLVxugD0ZsXyYXQmIRxIlCSYU9aRa8pBpkECHoOJ1LX6b1d%2FYuJSMIM%2BSurLMMuxiMoGOqUBiwkYvyLKl21X8cbakRFAFOk7HHgU0c0DcUDrqjFi%2BM1jPNPwX6%2FfTYs%2BSJr%2B6YQdXkrkkK6p%2B5ijZ5FKZkCfc4id3PzPB2Jv1TfYsem%2Fu%2BzkTqkhytu4MLZ3CTNAu4pwuYAe2ervd65JFSmGqpuuLH5CYY39DaF1a%2FV0HTVivj75kczX3w5%2FO2OxHkGxiCTT%2FtBQCRjl6B06D0JBd7a2q2jhMkIn&X-Amz-Signature=b6d599063b4468194b4f2368d96daa3a2d7e7b74a5c575757abd5ee772db0c67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NOISZPO%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyb0Pofk6UpCGGnxJVlxXGOAlRkAzfAdsGnWvRAmVVjQIgIA81WKvCqui9k1CUuowwLZFzjXVcvr2GYuDsdYukslAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDJDaIxQkfUnwJmh9eircA%2F%2FWMy4R3QLWFxupDQ6pP%2FDNaXrKhOfM8LHlO50ms8ood%2Bs%2FKD6ChSXy%2FUCOpHVrR21jZRRZ4vogHtvcQVB3tXsedAdFEE5dIMlzscCMLFdFb8TcHEsny%2FRXoJ9jRrFfT%2BRGTMMF6Jte7Q3pgYyQltiAZ0el0WjTresmsbNuLlrTOIkBPBLlu12TXraQSY3rAw0VMwUo20nLqYsM%2FsotrP6ZwJuKohUcBQf0PKtT2ZnLHGr486AW5a9a5aVr9HE%2FoM52JMZXlxH%2BlBU1DGmLvoVv1nUjg4lNWFCDSx9m7yoeQytTlEEH4%2B6GVa%2FEmGJm2l%2BUs66m%2FEc%2FXicp3cZ5B7xFqWoNExKz8c2CbRxbwwqLGRYvCj2jnVjDBXVV9dSrn7g92beaRNKRygEAEXH1KOaJrg72jjXLLy7VGEaJVk3XD%2B3YpQ27dlzraJPmCyK%2Fm9ZIghpuz3eEe76Llkasnp3DbqMU9rgPPRUvS5%2Btt1ncK5M%2B7uN6d%2FDFa6yx6K%2Fjecm0%2F%2FC0OOtSqYyzkaia6OoXJ4ZlbK2b3sApeXihnqtvuw%2BhipeaBxIq%2Bl3KApvAZLVxugD0ZsXyYXQmIRxIlCSYU9aRa8pBpkECHoOJ1LX6b1d%2FYuJSMIM%2BSurLMMuxiMoGOqUBiwkYvyLKl21X8cbakRFAFOk7HHgU0c0DcUDrqjFi%2BM1jPNPwX6%2FfTYs%2BSJr%2B6YQdXkrkkK6p%2B5ijZ5FKZkCfc4id3PzPB2Jv1TfYsem%2Fu%2BzkTqkhytu4MLZ3CTNAu4pwuYAe2ervd65JFSmGqpuuLH5CYY39DaF1a%2FV0HTVivj75kczX3w5%2FO2OxHkGxiCTT%2FtBQCRjl6B06D0JBd7a2q2jhMkIn&X-Amz-Signature=93a73226c3442d9874864ad48f6217c947a370295b8a47aa8a784513fc628d21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NOISZPO%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyb0Pofk6UpCGGnxJVlxXGOAlRkAzfAdsGnWvRAmVVjQIgIA81WKvCqui9k1CUuowwLZFzjXVcvr2GYuDsdYukslAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDJDaIxQkfUnwJmh9eircA%2F%2FWMy4R3QLWFxupDQ6pP%2FDNaXrKhOfM8LHlO50ms8ood%2Bs%2FKD6ChSXy%2FUCOpHVrR21jZRRZ4vogHtvcQVB3tXsedAdFEE5dIMlzscCMLFdFb8TcHEsny%2FRXoJ9jRrFfT%2BRGTMMF6Jte7Q3pgYyQltiAZ0el0WjTresmsbNuLlrTOIkBPBLlu12TXraQSY3rAw0VMwUo20nLqYsM%2FsotrP6ZwJuKohUcBQf0PKtT2ZnLHGr486AW5a9a5aVr9HE%2FoM52JMZXlxH%2BlBU1DGmLvoVv1nUjg4lNWFCDSx9m7yoeQytTlEEH4%2B6GVa%2FEmGJm2l%2BUs66m%2FEc%2FXicp3cZ5B7xFqWoNExKz8c2CbRxbwwqLGRYvCj2jnVjDBXVV9dSrn7g92beaRNKRygEAEXH1KOaJrg72jjXLLy7VGEaJVk3XD%2B3YpQ27dlzraJPmCyK%2Fm9ZIghpuz3eEe76Llkasnp3DbqMU9rgPPRUvS5%2Btt1ncK5M%2B7uN6d%2FDFa6yx6K%2Fjecm0%2F%2FC0OOtSqYyzkaia6OoXJ4ZlbK2b3sApeXihnqtvuw%2BhipeaBxIq%2Bl3KApvAZLVxugD0ZsXyYXQmIRxIlCSYU9aRa8pBpkECHoOJ1LX6b1d%2FYuJSMIM%2BSurLMMuxiMoGOqUBiwkYvyLKl21X8cbakRFAFOk7HHgU0c0DcUDrqjFi%2BM1jPNPwX6%2FfTYs%2BSJr%2B6YQdXkrkkK6p%2B5ijZ5FKZkCfc4id3PzPB2Jv1TfYsem%2Fu%2BzkTqkhytu4MLZ3CTNAu4pwuYAe2ervd65JFSmGqpuuLH5CYY39DaF1a%2FV0HTVivj75kczX3w5%2FO2OxHkGxiCTT%2FtBQCRjl6B06D0JBd7a2q2jhMkIn&X-Amz-Signature=6e11a8864028d309b49e933ac2aa05c3a50fcfdd2be393257a924c5c527a6081&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NOISZPO%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyb0Pofk6UpCGGnxJVlxXGOAlRkAzfAdsGnWvRAmVVjQIgIA81WKvCqui9k1CUuowwLZFzjXVcvr2GYuDsdYukslAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDJDaIxQkfUnwJmh9eircA%2F%2FWMy4R3QLWFxupDQ6pP%2FDNaXrKhOfM8LHlO50ms8ood%2Bs%2FKD6ChSXy%2FUCOpHVrR21jZRRZ4vogHtvcQVB3tXsedAdFEE5dIMlzscCMLFdFb8TcHEsny%2FRXoJ9jRrFfT%2BRGTMMF6Jte7Q3pgYyQltiAZ0el0WjTresmsbNuLlrTOIkBPBLlu12TXraQSY3rAw0VMwUo20nLqYsM%2FsotrP6ZwJuKohUcBQf0PKtT2ZnLHGr486AW5a9a5aVr9HE%2FoM52JMZXlxH%2BlBU1DGmLvoVv1nUjg4lNWFCDSx9m7yoeQytTlEEH4%2B6GVa%2FEmGJm2l%2BUs66m%2FEc%2FXicp3cZ5B7xFqWoNExKz8c2CbRxbwwqLGRYvCj2jnVjDBXVV9dSrn7g92beaRNKRygEAEXH1KOaJrg72jjXLLy7VGEaJVk3XD%2B3YpQ27dlzraJPmCyK%2Fm9ZIghpuz3eEe76Llkasnp3DbqMU9rgPPRUvS5%2Btt1ncK5M%2B7uN6d%2FDFa6yx6K%2Fjecm0%2F%2FC0OOtSqYyzkaia6OoXJ4ZlbK2b3sApeXihnqtvuw%2BhipeaBxIq%2Bl3KApvAZLVxugD0ZsXyYXQmIRxIlCSYU9aRa8pBpkECHoOJ1LX6b1d%2FYuJSMIM%2BSurLMMuxiMoGOqUBiwkYvyLKl21X8cbakRFAFOk7HHgU0c0DcUDrqjFi%2BM1jPNPwX6%2FfTYs%2BSJr%2B6YQdXkrkkK6p%2B5ijZ5FKZkCfc4id3PzPB2Jv1TfYsem%2Fu%2BzkTqkhytu4MLZ3CTNAu4pwuYAe2ervd65JFSmGqpuuLH5CYY39DaF1a%2FV0HTVivj75kczX3w5%2FO2OxHkGxiCTT%2FtBQCRjl6B06D0JBd7a2q2jhMkIn&X-Amz-Signature=c509d3309259af8ad453ead1369670c0107c84ee265cca994f070df55567ec28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NOISZPO%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyb0Pofk6UpCGGnxJVlxXGOAlRkAzfAdsGnWvRAmVVjQIgIA81WKvCqui9k1CUuowwLZFzjXVcvr2GYuDsdYukslAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDJDaIxQkfUnwJmh9eircA%2F%2FWMy4R3QLWFxupDQ6pP%2FDNaXrKhOfM8LHlO50ms8ood%2Bs%2FKD6ChSXy%2FUCOpHVrR21jZRRZ4vogHtvcQVB3tXsedAdFEE5dIMlzscCMLFdFb8TcHEsny%2FRXoJ9jRrFfT%2BRGTMMF6Jte7Q3pgYyQltiAZ0el0WjTresmsbNuLlrTOIkBPBLlu12TXraQSY3rAw0VMwUo20nLqYsM%2FsotrP6ZwJuKohUcBQf0PKtT2ZnLHGr486AW5a9a5aVr9HE%2FoM52JMZXlxH%2BlBU1DGmLvoVv1nUjg4lNWFCDSx9m7yoeQytTlEEH4%2B6GVa%2FEmGJm2l%2BUs66m%2FEc%2FXicp3cZ5B7xFqWoNExKz8c2CbRxbwwqLGRYvCj2jnVjDBXVV9dSrn7g92beaRNKRygEAEXH1KOaJrg72jjXLLy7VGEaJVk3XD%2B3YpQ27dlzraJPmCyK%2Fm9ZIghpuz3eEe76Llkasnp3DbqMU9rgPPRUvS5%2Btt1ncK5M%2B7uN6d%2FDFa6yx6K%2Fjecm0%2F%2FC0OOtSqYyzkaia6OoXJ4ZlbK2b3sApeXihnqtvuw%2BhipeaBxIq%2Bl3KApvAZLVxugD0ZsXyYXQmIRxIlCSYU9aRa8pBpkECHoOJ1LX6b1d%2FYuJSMIM%2BSurLMMuxiMoGOqUBiwkYvyLKl21X8cbakRFAFOk7HHgU0c0DcUDrqjFi%2BM1jPNPwX6%2FfTYs%2BSJr%2B6YQdXkrkkK6p%2B5ijZ5FKZkCfc4id3PzPB2Jv1TfYsem%2Fu%2BzkTqkhytu4MLZ3CTNAu4pwuYAe2ervd65JFSmGqpuuLH5CYY39DaF1a%2FV0HTVivj75kczX3w5%2FO2OxHkGxiCTT%2FtBQCRjl6B06D0JBd7a2q2jhMkIn&X-Amz-Signature=f072872ba73bc68548b8d17aa0c7fdb4b3cca2ff35c72c66234dcd205d28f4a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NOISZPO%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyb0Pofk6UpCGGnxJVlxXGOAlRkAzfAdsGnWvRAmVVjQIgIA81WKvCqui9k1CUuowwLZFzjXVcvr2GYuDsdYukslAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDJDaIxQkfUnwJmh9eircA%2F%2FWMy4R3QLWFxupDQ6pP%2FDNaXrKhOfM8LHlO50ms8ood%2Bs%2FKD6ChSXy%2FUCOpHVrR21jZRRZ4vogHtvcQVB3tXsedAdFEE5dIMlzscCMLFdFb8TcHEsny%2FRXoJ9jRrFfT%2BRGTMMF6Jte7Q3pgYyQltiAZ0el0WjTresmsbNuLlrTOIkBPBLlu12TXraQSY3rAw0VMwUo20nLqYsM%2FsotrP6ZwJuKohUcBQf0PKtT2ZnLHGr486AW5a9a5aVr9HE%2FoM52JMZXlxH%2BlBU1DGmLvoVv1nUjg4lNWFCDSx9m7yoeQytTlEEH4%2B6GVa%2FEmGJm2l%2BUs66m%2FEc%2FXicp3cZ5B7xFqWoNExKz8c2CbRxbwwqLGRYvCj2jnVjDBXVV9dSrn7g92beaRNKRygEAEXH1KOaJrg72jjXLLy7VGEaJVk3XD%2B3YpQ27dlzraJPmCyK%2Fm9ZIghpuz3eEe76Llkasnp3DbqMU9rgPPRUvS5%2Btt1ncK5M%2B7uN6d%2FDFa6yx6K%2Fjecm0%2F%2FC0OOtSqYyzkaia6OoXJ4ZlbK2b3sApeXihnqtvuw%2BhipeaBxIq%2Bl3KApvAZLVxugD0ZsXyYXQmIRxIlCSYU9aRa8pBpkECHoOJ1LX6b1d%2FYuJSMIM%2BSurLMMuxiMoGOqUBiwkYvyLKl21X8cbakRFAFOk7HHgU0c0DcUDrqjFi%2BM1jPNPwX6%2FfTYs%2BSJr%2B6YQdXkrkkK6p%2B5ijZ5FKZkCfc4id3PzPB2Jv1TfYsem%2Fu%2BzkTqkhytu4MLZ3CTNAu4pwuYAe2ervd65JFSmGqpuuLH5CYY39DaF1a%2FV0HTVivj75kczX3w5%2FO2OxHkGxiCTT%2FtBQCRjl6B06D0JBd7a2q2jhMkIn&X-Amz-Signature=3857bbccd7fff5c1b6416d8feabc0610bfae28a4d9cd1334f15db5b491fb6b99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

