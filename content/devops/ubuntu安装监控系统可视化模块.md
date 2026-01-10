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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662FW3Y42%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUmLzUfK6zvwQqpoTy%2B2W5FNO4FAxr9OmnTW8ER11E2QIhAPSGDAhZRf2CVD%2FFZXWwquPe8tAW6XWJ0g5JgFvcIlS8KogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTQWayTRB8U5Dcwocq3AOufICp%2BwwqZNrg9dH1XMCnbTd2ucicGFUZ0M9d6zEbsOnGMoenW8sonIDjGyXbXhN7ZPr1FRYkRGF8yAuolL152AfqG6kdt5HR7g%2B%2BaaSgjsQhqdB2%2FIRenDwKgt0iGFW73mH1VaGxNtwAqQbY58N4KlygLYCMrkxmKfeKUWH9dqQZTFlfS1nulKixBu8tUpFyhIaOP167oGuwXVuzDIGapVlBaFP88OdQFrK3mwyOsdY8wwQr07jmw8zAFfrSXhgASI122liDn%2Bnjt6h7ohMcK1OOYuNRVp9sUYrWKHd%2BZLLXye0WWeeTMaeXR%2FXCVnwLgF07859IU9aH4GMQlZb55nT4%2BXE6kBVFg4K%2BH6H7Vu6fqQavA7oCMdkOiugVvFpieQkSpbNUapIA%2B%2F235IMsan29kV0fu63WqMkhS06RRWgzcMfHfPRBcaDVtTQV4R6V%2F3nLAobqCMwicQ86RBrpBUabhHdVsnCRmJjdO%2FSteGNzQp9MaXNwdDAxdkrJCA7W0Xhj%2FeN%2B7h8N2OPlXTGqp94eOqZwQKEyF5MBO3VG%2BglkdH46DGf84jGFR9bK%2B8QY3rKOymzqokykTA66CGUEaIRAo0zI%2BfJBRumreL555RjYOwv8fBpCONxZ%2FjCn%2BYbLBjqkAe9ntfMU6doYnp1Z6mOEAM5Lj%2BsGHqD%2F0WFVroTMabda%2BUNu4a%2FHI%2FufQ0DIgJK5z8Lby8lnbOyT7fJf02N6yxoFZbhhlcLzIvvzo1Pyj18ZzWEHITYgBUgt%2BNEw8DdhLHzoPVhtFvXRZ0y8rGktTkuD2VboN81UUGaglcJvdRxLTwoVHbxqNCNdcO9nlfblyF4TBwj25afvm5rDsM4IqMGCuLdR&X-Amz-Signature=e2559747205cad69fb94e44ca8daee4bae957e1c50438eb078adae064cf3fd0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662FW3Y42%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUmLzUfK6zvwQqpoTy%2B2W5FNO4FAxr9OmnTW8ER11E2QIhAPSGDAhZRf2CVD%2FFZXWwquPe8tAW6XWJ0g5JgFvcIlS8KogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTQWayTRB8U5Dcwocq3AOufICp%2BwwqZNrg9dH1XMCnbTd2ucicGFUZ0M9d6zEbsOnGMoenW8sonIDjGyXbXhN7ZPr1FRYkRGF8yAuolL152AfqG6kdt5HR7g%2B%2BaaSgjsQhqdB2%2FIRenDwKgt0iGFW73mH1VaGxNtwAqQbY58N4KlygLYCMrkxmKfeKUWH9dqQZTFlfS1nulKixBu8tUpFyhIaOP167oGuwXVuzDIGapVlBaFP88OdQFrK3mwyOsdY8wwQr07jmw8zAFfrSXhgASI122liDn%2Bnjt6h7ohMcK1OOYuNRVp9sUYrWKHd%2BZLLXye0WWeeTMaeXR%2FXCVnwLgF07859IU9aH4GMQlZb55nT4%2BXE6kBVFg4K%2BH6H7Vu6fqQavA7oCMdkOiugVvFpieQkSpbNUapIA%2B%2F235IMsan29kV0fu63WqMkhS06RRWgzcMfHfPRBcaDVtTQV4R6V%2F3nLAobqCMwicQ86RBrpBUabhHdVsnCRmJjdO%2FSteGNzQp9MaXNwdDAxdkrJCA7W0Xhj%2FeN%2B7h8N2OPlXTGqp94eOqZwQKEyF5MBO3VG%2BglkdH46DGf84jGFR9bK%2B8QY3rKOymzqokykTA66CGUEaIRAo0zI%2BfJBRumreL555RjYOwv8fBpCONxZ%2FjCn%2BYbLBjqkAe9ntfMU6doYnp1Z6mOEAM5Lj%2BsGHqD%2F0WFVroTMabda%2BUNu4a%2FHI%2FufQ0DIgJK5z8Lby8lnbOyT7fJf02N6yxoFZbhhlcLzIvvzo1Pyj18ZzWEHITYgBUgt%2BNEw8DdhLHzoPVhtFvXRZ0y8rGktTkuD2VboN81UUGaglcJvdRxLTwoVHbxqNCNdcO9nlfblyF4TBwj25afvm5rDsM4IqMGCuLdR&X-Amz-Signature=0331130dd43590d75285911ed8b292c404041009204f1c899d1ae9032509c937&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662FW3Y42%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUmLzUfK6zvwQqpoTy%2B2W5FNO4FAxr9OmnTW8ER11E2QIhAPSGDAhZRf2CVD%2FFZXWwquPe8tAW6XWJ0g5JgFvcIlS8KogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTQWayTRB8U5Dcwocq3AOufICp%2BwwqZNrg9dH1XMCnbTd2ucicGFUZ0M9d6zEbsOnGMoenW8sonIDjGyXbXhN7ZPr1FRYkRGF8yAuolL152AfqG6kdt5HR7g%2B%2BaaSgjsQhqdB2%2FIRenDwKgt0iGFW73mH1VaGxNtwAqQbY58N4KlygLYCMrkxmKfeKUWH9dqQZTFlfS1nulKixBu8tUpFyhIaOP167oGuwXVuzDIGapVlBaFP88OdQFrK3mwyOsdY8wwQr07jmw8zAFfrSXhgASI122liDn%2Bnjt6h7ohMcK1OOYuNRVp9sUYrWKHd%2BZLLXye0WWeeTMaeXR%2FXCVnwLgF07859IU9aH4GMQlZb55nT4%2BXE6kBVFg4K%2BH6H7Vu6fqQavA7oCMdkOiugVvFpieQkSpbNUapIA%2B%2F235IMsan29kV0fu63WqMkhS06RRWgzcMfHfPRBcaDVtTQV4R6V%2F3nLAobqCMwicQ86RBrpBUabhHdVsnCRmJjdO%2FSteGNzQp9MaXNwdDAxdkrJCA7W0Xhj%2FeN%2B7h8N2OPlXTGqp94eOqZwQKEyF5MBO3VG%2BglkdH46DGf84jGFR9bK%2B8QY3rKOymzqokykTA66CGUEaIRAo0zI%2BfJBRumreL555RjYOwv8fBpCONxZ%2FjCn%2BYbLBjqkAe9ntfMU6doYnp1Z6mOEAM5Lj%2BsGHqD%2F0WFVroTMabda%2BUNu4a%2FHI%2FufQ0DIgJK5z8Lby8lnbOyT7fJf02N6yxoFZbhhlcLzIvvzo1Pyj18ZzWEHITYgBUgt%2BNEw8DdhLHzoPVhtFvXRZ0y8rGktTkuD2VboN81UUGaglcJvdRxLTwoVHbxqNCNdcO9nlfblyF4TBwj25afvm5rDsM4IqMGCuLdR&X-Amz-Signature=27114dce60ef93aa0bb934ba390ea8d7d851266ca733efb18997b542512d0262&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662FW3Y42%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUmLzUfK6zvwQqpoTy%2B2W5FNO4FAxr9OmnTW8ER11E2QIhAPSGDAhZRf2CVD%2FFZXWwquPe8tAW6XWJ0g5JgFvcIlS8KogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTQWayTRB8U5Dcwocq3AOufICp%2BwwqZNrg9dH1XMCnbTd2ucicGFUZ0M9d6zEbsOnGMoenW8sonIDjGyXbXhN7ZPr1FRYkRGF8yAuolL152AfqG6kdt5HR7g%2B%2BaaSgjsQhqdB2%2FIRenDwKgt0iGFW73mH1VaGxNtwAqQbY58N4KlygLYCMrkxmKfeKUWH9dqQZTFlfS1nulKixBu8tUpFyhIaOP167oGuwXVuzDIGapVlBaFP88OdQFrK3mwyOsdY8wwQr07jmw8zAFfrSXhgASI122liDn%2Bnjt6h7ohMcK1OOYuNRVp9sUYrWKHd%2BZLLXye0WWeeTMaeXR%2FXCVnwLgF07859IU9aH4GMQlZb55nT4%2BXE6kBVFg4K%2BH6H7Vu6fqQavA7oCMdkOiugVvFpieQkSpbNUapIA%2B%2F235IMsan29kV0fu63WqMkhS06RRWgzcMfHfPRBcaDVtTQV4R6V%2F3nLAobqCMwicQ86RBrpBUabhHdVsnCRmJjdO%2FSteGNzQp9MaXNwdDAxdkrJCA7W0Xhj%2FeN%2B7h8N2OPlXTGqp94eOqZwQKEyF5MBO3VG%2BglkdH46DGf84jGFR9bK%2B8QY3rKOymzqokykTA66CGUEaIRAo0zI%2BfJBRumreL555RjYOwv8fBpCONxZ%2FjCn%2BYbLBjqkAe9ntfMU6doYnp1Z6mOEAM5Lj%2BsGHqD%2F0WFVroTMabda%2BUNu4a%2FHI%2FufQ0DIgJK5z8Lby8lnbOyT7fJf02N6yxoFZbhhlcLzIvvzo1Pyj18ZzWEHITYgBUgt%2BNEw8DdhLHzoPVhtFvXRZ0y8rGktTkuD2VboN81UUGaglcJvdRxLTwoVHbxqNCNdcO9nlfblyF4TBwj25afvm5rDsM4IqMGCuLdR&X-Amz-Signature=88c33a4e7c866814b98afc640b9a61cbc27209cd163fa2b8fb802ffaa120e73d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662FW3Y42%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUmLzUfK6zvwQqpoTy%2B2W5FNO4FAxr9OmnTW8ER11E2QIhAPSGDAhZRf2CVD%2FFZXWwquPe8tAW6XWJ0g5JgFvcIlS8KogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTQWayTRB8U5Dcwocq3AOufICp%2BwwqZNrg9dH1XMCnbTd2ucicGFUZ0M9d6zEbsOnGMoenW8sonIDjGyXbXhN7ZPr1FRYkRGF8yAuolL152AfqG6kdt5HR7g%2B%2BaaSgjsQhqdB2%2FIRenDwKgt0iGFW73mH1VaGxNtwAqQbY58N4KlygLYCMrkxmKfeKUWH9dqQZTFlfS1nulKixBu8tUpFyhIaOP167oGuwXVuzDIGapVlBaFP88OdQFrK3mwyOsdY8wwQr07jmw8zAFfrSXhgASI122liDn%2Bnjt6h7ohMcK1OOYuNRVp9sUYrWKHd%2BZLLXye0WWeeTMaeXR%2FXCVnwLgF07859IU9aH4GMQlZb55nT4%2BXE6kBVFg4K%2BH6H7Vu6fqQavA7oCMdkOiugVvFpieQkSpbNUapIA%2B%2F235IMsan29kV0fu63WqMkhS06RRWgzcMfHfPRBcaDVtTQV4R6V%2F3nLAobqCMwicQ86RBrpBUabhHdVsnCRmJjdO%2FSteGNzQp9MaXNwdDAxdkrJCA7W0Xhj%2FeN%2B7h8N2OPlXTGqp94eOqZwQKEyF5MBO3VG%2BglkdH46DGf84jGFR9bK%2B8QY3rKOymzqokykTA66CGUEaIRAo0zI%2BfJBRumreL555RjYOwv8fBpCONxZ%2FjCn%2BYbLBjqkAe9ntfMU6doYnp1Z6mOEAM5Lj%2BsGHqD%2F0WFVroTMabda%2BUNu4a%2FHI%2FufQ0DIgJK5z8Lby8lnbOyT7fJf02N6yxoFZbhhlcLzIvvzo1Pyj18ZzWEHITYgBUgt%2BNEw8DdhLHzoPVhtFvXRZ0y8rGktTkuD2VboN81UUGaglcJvdRxLTwoVHbxqNCNdcO9nlfblyF4TBwj25afvm5rDsM4IqMGCuLdR&X-Amz-Signature=e957ba1306ee3d398c8408e38adfa5dfc79348a4df6e5bcce98608aab32f32ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662FW3Y42%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUmLzUfK6zvwQqpoTy%2B2W5FNO4FAxr9OmnTW8ER11E2QIhAPSGDAhZRf2CVD%2FFZXWwquPe8tAW6XWJ0g5JgFvcIlS8KogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTQWayTRB8U5Dcwocq3AOufICp%2BwwqZNrg9dH1XMCnbTd2ucicGFUZ0M9d6zEbsOnGMoenW8sonIDjGyXbXhN7ZPr1FRYkRGF8yAuolL152AfqG6kdt5HR7g%2B%2BaaSgjsQhqdB2%2FIRenDwKgt0iGFW73mH1VaGxNtwAqQbY58N4KlygLYCMrkxmKfeKUWH9dqQZTFlfS1nulKixBu8tUpFyhIaOP167oGuwXVuzDIGapVlBaFP88OdQFrK3mwyOsdY8wwQr07jmw8zAFfrSXhgASI122liDn%2Bnjt6h7ohMcK1OOYuNRVp9sUYrWKHd%2BZLLXye0WWeeTMaeXR%2FXCVnwLgF07859IU9aH4GMQlZb55nT4%2BXE6kBVFg4K%2BH6H7Vu6fqQavA7oCMdkOiugVvFpieQkSpbNUapIA%2B%2F235IMsan29kV0fu63WqMkhS06RRWgzcMfHfPRBcaDVtTQV4R6V%2F3nLAobqCMwicQ86RBrpBUabhHdVsnCRmJjdO%2FSteGNzQp9MaXNwdDAxdkrJCA7W0Xhj%2FeN%2B7h8N2OPlXTGqp94eOqZwQKEyF5MBO3VG%2BglkdH46DGf84jGFR9bK%2B8QY3rKOymzqokykTA66CGUEaIRAo0zI%2BfJBRumreL555RjYOwv8fBpCONxZ%2FjCn%2BYbLBjqkAe9ntfMU6doYnp1Z6mOEAM5Lj%2BsGHqD%2F0WFVroTMabda%2BUNu4a%2FHI%2FufQ0DIgJK5z8Lby8lnbOyT7fJf02N6yxoFZbhhlcLzIvvzo1Pyj18ZzWEHITYgBUgt%2BNEw8DdhLHzoPVhtFvXRZ0y8rGktTkuD2VboN81UUGaglcJvdRxLTwoVHbxqNCNdcO9nlfblyF4TBwj25afvm5rDsM4IqMGCuLdR&X-Amz-Signature=5f7fed451f69729ed592dc793c323428ab04b412a6b2136310cce99060c4ca72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662FW3Y42%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUmLzUfK6zvwQqpoTy%2B2W5FNO4FAxr9OmnTW8ER11E2QIhAPSGDAhZRf2CVD%2FFZXWwquPe8tAW6XWJ0g5JgFvcIlS8KogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTQWayTRB8U5Dcwocq3AOufICp%2BwwqZNrg9dH1XMCnbTd2ucicGFUZ0M9d6zEbsOnGMoenW8sonIDjGyXbXhN7ZPr1FRYkRGF8yAuolL152AfqG6kdt5HR7g%2B%2BaaSgjsQhqdB2%2FIRenDwKgt0iGFW73mH1VaGxNtwAqQbY58N4KlygLYCMrkxmKfeKUWH9dqQZTFlfS1nulKixBu8tUpFyhIaOP167oGuwXVuzDIGapVlBaFP88OdQFrK3mwyOsdY8wwQr07jmw8zAFfrSXhgASI122liDn%2Bnjt6h7ohMcK1OOYuNRVp9sUYrWKHd%2BZLLXye0WWeeTMaeXR%2FXCVnwLgF07859IU9aH4GMQlZb55nT4%2BXE6kBVFg4K%2BH6H7Vu6fqQavA7oCMdkOiugVvFpieQkSpbNUapIA%2B%2F235IMsan29kV0fu63WqMkhS06RRWgzcMfHfPRBcaDVtTQV4R6V%2F3nLAobqCMwicQ86RBrpBUabhHdVsnCRmJjdO%2FSteGNzQp9MaXNwdDAxdkrJCA7W0Xhj%2FeN%2B7h8N2OPlXTGqp94eOqZwQKEyF5MBO3VG%2BglkdH46DGf84jGFR9bK%2B8QY3rKOymzqokykTA66CGUEaIRAo0zI%2BfJBRumreL555RjYOwv8fBpCONxZ%2FjCn%2BYbLBjqkAe9ntfMU6doYnp1Z6mOEAM5Lj%2BsGHqD%2F0WFVroTMabda%2BUNu4a%2FHI%2FufQ0DIgJK5z8Lby8lnbOyT7fJf02N6yxoFZbhhlcLzIvvzo1Pyj18ZzWEHITYgBUgt%2BNEw8DdhLHzoPVhtFvXRZ0y8rGktTkuD2VboN81UUGaglcJvdRxLTwoVHbxqNCNdcO9nlfblyF4TBwj25afvm5rDsM4IqMGCuLdR&X-Amz-Signature=a542aa906602eac8ee8ac62d053e2079c7834786345a4025fc4e6a33ef987f38&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

