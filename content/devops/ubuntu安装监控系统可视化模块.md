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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCVXNNTM%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCeDqzxbYYCY0Tbc%2FqHhv4j3bnSS92qn6O79SUYUHr%2FnwIge%2FPs%2BftB4JW%2FYSp6okG8WqLlrc87ObH8SrS6PUg9hBsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMCd0Q9Exv49vG5gIyrcA60qYyL4fAaBzTKFm5k3vHhLSV4RG6uZL8f%2F48S9PXhw0CxdGOlk7qGcrDfXBalmkAN3bCSq8ZWt258ZYmdcIX2pVzbNNXqcxYBVHU%2F8%2BNKME6gKK2gscHAGjcbzcLim7zUpORKJKWVWdYC0i1d%2FTPS4Tl8rTssYUZH4WYFRSy81lC2OD0COKWHGMxjNY1IVqI7rxw%2FX%2FB4tZm6%2BPyg%2FQjYjCgZ0kpwZ%2B3kmxIgGCoqBDAeBL4uS4Hx%2BqYzNSU%2Fd1UOZW3GWNp10MP3VXFdEg13wRSq%2BpX2OZo5ntHMPFdHTKpeUzubFwhoWZ6NaMbaScz4NHdbgLEEcV%2BR8xvtLWwjNXPFIZC0dKI3LCSwpiYSxbFLckmDBxiRU%2FRpXJgFI7wTqUCidHO9Ah4W5Xl3erbL%2BhcpPaItIe1FHLRr2VQ5%2F7jK79Gt3AZCSzxA4Lqvrgz6Iucs4vWa%2FNVcI2AjNZp2KVFAxe0fmzaJ54NpVBhVp4Vl%2B0bqzkJQM4jNUH%2B3uu%2BRzmKBAA2OxF%2F78r8AWkad91UqvKBVpu1axgcp1cFg%2F15nfvmVGZmj7ReoOQ%2BttbxdrwwiDUuj3jIW%2BUyaS6%2BJNxpWq5NNVtmtIWB%2Bqna5FMD83ZmPUyggKVT5qMO7a%2FMkGOqUB5NI1bC6Yd5KOz8Lw8GKFkyKpTj1BHHxO%2FAZxj2t7EvdYXizvAYsGXZrtsX33FhFPuo7Bri7CGPa%2BDeLwtc1qm7Ui%2FmC9kxy%2FeBIGxf72xcKQObeRERuAk31rlgy08zTcvfQVNH1LYyYUO4LoVq5su4k84bJvu5xRmz1tuQk1jAKSrwrsCox3ukZIXnRt38o0WwPxGJuSdJ7WIgLS9wFKIPUARUZw&X-Amz-Signature=4356065780a5ae348589ad5ee2c15341456112cc59df4b864a26a06dd1caf392&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCVXNNTM%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCeDqzxbYYCY0Tbc%2FqHhv4j3bnSS92qn6O79SUYUHr%2FnwIge%2FPs%2BftB4JW%2FYSp6okG8WqLlrc87ObH8SrS6PUg9hBsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMCd0Q9Exv49vG5gIyrcA60qYyL4fAaBzTKFm5k3vHhLSV4RG6uZL8f%2F48S9PXhw0CxdGOlk7qGcrDfXBalmkAN3bCSq8ZWt258ZYmdcIX2pVzbNNXqcxYBVHU%2F8%2BNKME6gKK2gscHAGjcbzcLim7zUpORKJKWVWdYC0i1d%2FTPS4Tl8rTssYUZH4WYFRSy81lC2OD0COKWHGMxjNY1IVqI7rxw%2FX%2FB4tZm6%2BPyg%2FQjYjCgZ0kpwZ%2B3kmxIgGCoqBDAeBL4uS4Hx%2BqYzNSU%2Fd1UOZW3GWNp10MP3VXFdEg13wRSq%2BpX2OZo5ntHMPFdHTKpeUzubFwhoWZ6NaMbaScz4NHdbgLEEcV%2BR8xvtLWwjNXPFIZC0dKI3LCSwpiYSxbFLckmDBxiRU%2FRpXJgFI7wTqUCidHO9Ah4W5Xl3erbL%2BhcpPaItIe1FHLRr2VQ5%2F7jK79Gt3AZCSzxA4Lqvrgz6Iucs4vWa%2FNVcI2AjNZp2KVFAxe0fmzaJ54NpVBhVp4Vl%2B0bqzkJQM4jNUH%2B3uu%2BRzmKBAA2OxF%2F78r8AWkad91UqvKBVpu1axgcp1cFg%2F15nfvmVGZmj7ReoOQ%2BttbxdrwwiDUuj3jIW%2BUyaS6%2BJNxpWq5NNVtmtIWB%2Bqna5FMD83ZmPUyggKVT5qMO7a%2FMkGOqUB5NI1bC6Yd5KOz8Lw8GKFkyKpTj1BHHxO%2FAZxj2t7EvdYXizvAYsGXZrtsX33FhFPuo7Bri7CGPa%2BDeLwtc1qm7Ui%2FmC9kxy%2FeBIGxf72xcKQObeRERuAk31rlgy08zTcvfQVNH1LYyYUO4LoVq5su4k84bJvu5xRmz1tuQk1jAKSrwrsCox3ukZIXnRt38o0WwPxGJuSdJ7WIgLS9wFKIPUARUZw&X-Amz-Signature=29c0875b8993e9472fa0805b09c687ee9ec12261301f44851bbeaff0f91baef4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCVXNNTM%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCeDqzxbYYCY0Tbc%2FqHhv4j3bnSS92qn6O79SUYUHr%2FnwIge%2FPs%2BftB4JW%2FYSp6okG8WqLlrc87ObH8SrS6PUg9hBsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMCd0Q9Exv49vG5gIyrcA60qYyL4fAaBzTKFm5k3vHhLSV4RG6uZL8f%2F48S9PXhw0CxdGOlk7qGcrDfXBalmkAN3bCSq8ZWt258ZYmdcIX2pVzbNNXqcxYBVHU%2F8%2BNKME6gKK2gscHAGjcbzcLim7zUpORKJKWVWdYC0i1d%2FTPS4Tl8rTssYUZH4WYFRSy81lC2OD0COKWHGMxjNY1IVqI7rxw%2FX%2FB4tZm6%2BPyg%2FQjYjCgZ0kpwZ%2B3kmxIgGCoqBDAeBL4uS4Hx%2BqYzNSU%2Fd1UOZW3GWNp10MP3VXFdEg13wRSq%2BpX2OZo5ntHMPFdHTKpeUzubFwhoWZ6NaMbaScz4NHdbgLEEcV%2BR8xvtLWwjNXPFIZC0dKI3LCSwpiYSxbFLckmDBxiRU%2FRpXJgFI7wTqUCidHO9Ah4W5Xl3erbL%2BhcpPaItIe1FHLRr2VQ5%2F7jK79Gt3AZCSzxA4Lqvrgz6Iucs4vWa%2FNVcI2AjNZp2KVFAxe0fmzaJ54NpVBhVp4Vl%2B0bqzkJQM4jNUH%2B3uu%2BRzmKBAA2OxF%2F78r8AWkad91UqvKBVpu1axgcp1cFg%2F15nfvmVGZmj7ReoOQ%2BttbxdrwwiDUuj3jIW%2BUyaS6%2BJNxpWq5NNVtmtIWB%2Bqna5FMD83ZmPUyggKVT5qMO7a%2FMkGOqUB5NI1bC6Yd5KOz8Lw8GKFkyKpTj1BHHxO%2FAZxj2t7EvdYXizvAYsGXZrtsX33FhFPuo7Bri7CGPa%2BDeLwtc1qm7Ui%2FmC9kxy%2FeBIGxf72xcKQObeRERuAk31rlgy08zTcvfQVNH1LYyYUO4LoVq5su4k84bJvu5xRmz1tuQk1jAKSrwrsCox3ukZIXnRt38o0WwPxGJuSdJ7WIgLS9wFKIPUARUZw&X-Amz-Signature=bad39211b6025469a3ddf76cfe38d1962aa60404fd10af2d6d5c6e9bba4833c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCVXNNTM%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCeDqzxbYYCY0Tbc%2FqHhv4j3bnSS92qn6O79SUYUHr%2FnwIge%2FPs%2BftB4JW%2FYSp6okG8WqLlrc87ObH8SrS6PUg9hBsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMCd0Q9Exv49vG5gIyrcA60qYyL4fAaBzTKFm5k3vHhLSV4RG6uZL8f%2F48S9PXhw0CxdGOlk7qGcrDfXBalmkAN3bCSq8ZWt258ZYmdcIX2pVzbNNXqcxYBVHU%2F8%2BNKME6gKK2gscHAGjcbzcLim7zUpORKJKWVWdYC0i1d%2FTPS4Tl8rTssYUZH4WYFRSy81lC2OD0COKWHGMxjNY1IVqI7rxw%2FX%2FB4tZm6%2BPyg%2FQjYjCgZ0kpwZ%2B3kmxIgGCoqBDAeBL4uS4Hx%2BqYzNSU%2Fd1UOZW3GWNp10MP3VXFdEg13wRSq%2BpX2OZo5ntHMPFdHTKpeUzubFwhoWZ6NaMbaScz4NHdbgLEEcV%2BR8xvtLWwjNXPFIZC0dKI3LCSwpiYSxbFLckmDBxiRU%2FRpXJgFI7wTqUCidHO9Ah4W5Xl3erbL%2BhcpPaItIe1FHLRr2VQ5%2F7jK79Gt3AZCSzxA4Lqvrgz6Iucs4vWa%2FNVcI2AjNZp2KVFAxe0fmzaJ54NpVBhVp4Vl%2B0bqzkJQM4jNUH%2B3uu%2BRzmKBAA2OxF%2F78r8AWkad91UqvKBVpu1axgcp1cFg%2F15nfvmVGZmj7ReoOQ%2BttbxdrwwiDUuj3jIW%2BUyaS6%2BJNxpWq5NNVtmtIWB%2Bqna5FMD83ZmPUyggKVT5qMO7a%2FMkGOqUB5NI1bC6Yd5KOz8Lw8GKFkyKpTj1BHHxO%2FAZxj2t7EvdYXizvAYsGXZrtsX33FhFPuo7Bri7CGPa%2BDeLwtc1qm7Ui%2FmC9kxy%2FeBIGxf72xcKQObeRERuAk31rlgy08zTcvfQVNH1LYyYUO4LoVq5su4k84bJvu5xRmz1tuQk1jAKSrwrsCox3ukZIXnRt38o0WwPxGJuSdJ7WIgLS9wFKIPUARUZw&X-Amz-Signature=473479c1e1b8004d14f7cb2fc419922f7c27241fcb82d5bf84042edbe33c34c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCVXNNTM%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCeDqzxbYYCY0Tbc%2FqHhv4j3bnSS92qn6O79SUYUHr%2FnwIge%2FPs%2BftB4JW%2FYSp6okG8WqLlrc87ObH8SrS6PUg9hBsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMCd0Q9Exv49vG5gIyrcA60qYyL4fAaBzTKFm5k3vHhLSV4RG6uZL8f%2F48S9PXhw0CxdGOlk7qGcrDfXBalmkAN3bCSq8ZWt258ZYmdcIX2pVzbNNXqcxYBVHU%2F8%2BNKME6gKK2gscHAGjcbzcLim7zUpORKJKWVWdYC0i1d%2FTPS4Tl8rTssYUZH4WYFRSy81lC2OD0COKWHGMxjNY1IVqI7rxw%2FX%2FB4tZm6%2BPyg%2FQjYjCgZ0kpwZ%2B3kmxIgGCoqBDAeBL4uS4Hx%2BqYzNSU%2Fd1UOZW3GWNp10MP3VXFdEg13wRSq%2BpX2OZo5ntHMPFdHTKpeUzubFwhoWZ6NaMbaScz4NHdbgLEEcV%2BR8xvtLWwjNXPFIZC0dKI3LCSwpiYSxbFLckmDBxiRU%2FRpXJgFI7wTqUCidHO9Ah4W5Xl3erbL%2BhcpPaItIe1FHLRr2VQ5%2F7jK79Gt3AZCSzxA4Lqvrgz6Iucs4vWa%2FNVcI2AjNZp2KVFAxe0fmzaJ54NpVBhVp4Vl%2B0bqzkJQM4jNUH%2B3uu%2BRzmKBAA2OxF%2F78r8AWkad91UqvKBVpu1axgcp1cFg%2F15nfvmVGZmj7ReoOQ%2BttbxdrwwiDUuj3jIW%2BUyaS6%2BJNxpWq5NNVtmtIWB%2Bqna5FMD83ZmPUyggKVT5qMO7a%2FMkGOqUB5NI1bC6Yd5KOz8Lw8GKFkyKpTj1BHHxO%2FAZxj2t7EvdYXizvAYsGXZrtsX33FhFPuo7Bri7CGPa%2BDeLwtc1qm7Ui%2FmC9kxy%2FeBIGxf72xcKQObeRERuAk31rlgy08zTcvfQVNH1LYyYUO4LoVq5su4k84bJvu5xRmz1tuQk1jAKSrwrsCox3ukZIXnRt38o0WwPxGJuSdJ7WIgLS9wFKIPUARUZw&X-Amz-Signature=a2fdb99dcf9353ee2a5a49d26eed9fb7191d6403e8136ae30c5d65e420f7155e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCVXNNTM%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCeDqzxbYYCY0Tbc%2FqHhv4j3bnSS92qn6O79SUYUHr%2FnwIge%2FPs%2BftB4JW%2FYSp6okG8WqLlrc87ObH8SrS6PUg9hBsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMCd0Q9Exv49vG5gIyrcA60qYyL4fAaBzTKFm5k3vHhLSV4RG6uZL8f%2F48S9PXhw0CxdGOlk7qGcrDfXBalmkAN3bCSq8ZWt258ZYmdcIX2pVzbNNXqcxYBVHU%2F8%2BNKME6gKK2gscHAGjcbzcLim7zUpORKJKWVWdYC0i1d%2FTPS4Tl8rTssYUZH4WYFRSy81lC2OD0COKWHGMxjNY1IVqI7rxw%2FX%2FB4tZm6%2BPyg%2FQjYjCgZ0kpwZ%2B3kmxIgGCoqBDAeBL4uS4Hx%2BqYzNSU%2Fd1UOZW3GWNp10MP3VXFdEg13wRSq%2BpX2OZo5ntHMPFdHTKpeUzubFwhoWZ6NaMbaScz4NHdbgLEEcV%2BR8xvtLWwjNXPFIZC0dKI3LCSwpiYSxbFLckmDBxiRU%2FRpXJgFI7wTqUCidHO9Ah4W5Xl3erbL%2BhcpPaItIe1FHLRr2VQ5%2F7jK79Gt3AZCSzxA4Lqvrgz6Iucs4vWa%2FNVcI2AjNZp2KVFAxe0fmzaJ54NpVBhVp4Vl%2B0bqzkJQM4jNUH%2B3uu%2BRzmKBAA2OxF%2F78r8AWkad91UqvKBVpu1axgcp1cFg%2F15nfvmVGZmj7ReoOQ%2BttbxdrwwiDUuj3jIW%2BUyaS6%2BJNxpWq5NNVtmtIWB%2Bqna5FMD83ZmPUyggKVT5qMO7a%2FMkGOqUB5NI1bC6Yd5KOz8Lw8GKFkyKpTj1BHHxO%2FAZxj2t7EvdYXizvAYsGXZrtsX33FhFPuo7Bri7CGPa%2BDeLwtc1qm7Ui%2FmC9kxy%2FeBIGxf72xcKQObeRERuAk31rlgy08zTcvfQVNH1LYyYUO4LoVq5su4k84bJvu5xRmz1tuQk1jAKSrwrsCox3ukZIXnRt38o0WwPxGJuSdJ7WIgLS9wFKIPUARUZw&X-Amz-Signature=9e9bfd4833b11e9a9b8f925b08b92f8beecccb70e34c03bab01278de07093995&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCVXNNTM%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCeDqzxbYYCY0Tbc%2FqHhv4j3bnSS92qn6O79SUYUHr%2FnwIge%2FPs%2BftB4JW%2FYSp6okG8WqLlrc87ObH8SrS6PUg9hBsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMCd0Q9Exv49vG5gIyrcA60qYyL4fAaBzTKFm5k3vHhLSV4RG6uZL8f%2F48S9PXhw0CxdGOlk7qGcrDfXBalmkAN3bCSq8ZWt258ZYmdcIX2pVzbNNXqcxYBVHU%2F8%2BNKME6gKK2gscHAGjcbzcLim7zUpORKJKWVWdYC0i1d%2FTPS4Tl8rTssYUZH4WYFRSy81lC2OD0COKWHGMxjNY1IVqI7rxw%2FX%2FB4tZm6%2BPyg%2FQjYjCgZ0kpwZ%2B3kmxIgGCoqBDAeBL4uS4Hx%2BqYzNSU%2Fd1UOZW3GWNp10MP3VXFdEg13wRSq%2BpX2OZo5ntHMPFdHTKpeUzubFwhoWZ6NaMbaScz4NHdbgLEEcV%2BR8xvtLWwjNXPFIZC0dKI3LCSwpiYSxbFLckmDBxiRU%2FRpXJgFI7wTqUCidHO9Ah4W5Xl3erbL%2BhcpPaItIe1FHLRr2VQ5%2F7jK79Gt3AZCSzxA4Lqvrgz6Iucs4vWa%2FNVcI2AjNZp2KVFAxe0fmzaJ54NpVBhVp4Vl%2B0bqzkJQM4jNUH%2B3uu%2BRzmKBAA2OxF%2F78r8AWkad91UqvKBVpu1axgcp1cFg%2F15nfvmVGZmj7ReoOQ%2BttbxdrwwiDUuj3jIW%2BUyaS6%2BJNxpWq5NNVtmtIWB%2Bqna5FMD83ZmPUyggKVT5qMO7a%2FMkGOqUB5NI1bC6Yd5KOz8Lw8GKFkyKpTj1BHHxO%2FAZxj2t7EvdYXizvAYsGXZrtsX33FhFPuo7Bri7CGPa%2BDeLwtc1qm7Ui%2FmC9kxy%2FeBIGxf72xcKQObeRERuAk31rlgy08zTcvfQVNH1LYyYUO4LoVq5su4k84bJvu5xRmz1tuQk1jAKSrwrsCox3ukZIXnRt38o0WwPxGJuSdJ7WIgLS9wFKIPUARUZw&X-Amz-Signature=a87b4452bf1661cdf4ee3bcfee5fd20f5a77b01c7bc902546612bbb81fae379d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

