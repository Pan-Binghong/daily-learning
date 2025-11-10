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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NTSTLLZ%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIDdr020ELCj4VDsmNSvjDqRRpyP8PDqc%2Bv5agMHBu%2BYbAiEAn3zddY81qh1HYC6t%2Fxp7bKrGuql%2BOeWDDX4tCph1buoqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG672To1%2FmU5wvPvXircA%2Fy1kKOv%2F4sJu63190fnihplG8v7J5zOHSsmLRZWDtw5ixDhW8SYF4QvCV453OTHRzAsNjVOSi3lnv1tS5iQvkuMQVm03FGxYGCGFTu%2BeHZxahKmPVppFtPIPF8TFfcQhh0xvO9OYlee%2B4CMIN1g5quuo7xh0Ynf4u7cdAwg6%2F%2BkltIuEJkqIz3RfyoRid8NH7oeXEuHjfXHvpd70oX1SLAJVzDKQbE247RZjaVnH51SYg0SIM7qJJZPgyVQIETxRh8yKNXYiTi8XSv2uSJEtJgZT15biPNHYR6FAdlGouiu6gNkCAaGaZL8Y5GwXQV174p9qOXmKFER6O2RzOdKB3NGhD9zbNdhB0MW4Dc%2FprwhVEfAlgMY%2F0ab1co9XULzMUnVHjNcREQH85qKX9ZozcufrFz7EcWsKItvMPOSllTQPDMZKoCmgtHGCdeYVzy%2B%2B8ncc4XTWtlPnrXU1meLf5giQ4eSr1K2sEUv8QZIOuG6tZdk4%2BPI6zuhX5K8Ow%2B%2Fq3KHCum1NKY%2BhTszpq3PKrkZRBEzfTafMjS5azL02Ienoy7SxDpfz85knkwDeABFHu8oyN8Q5Aa83R4nxY%2FufFt%2FVqjdVNQJDXe7cI3PJIQgGUTQRK9cbqntiAmZMLe5xMgGOqUB6lNB51Mnnde6nlyoxWFXBZIvU%2B8jD6G70Yntql9EOUqHiZXGU2UlhnVXFCldjsK6VUGQ9QwuGNEewTrpHimh%2FprThGvx5oyRLoh4jexqhiFLUyqFxTa%2B7UmUXwJlmZeCFEHQULaKUg%2BjwK29QI2D3iurJ1xgyAs7KfwkB1aRcuEV7Z7opIqFD%2FEE2cSN9WUd1HYDL2ca%2BApYvwREaGaWTgO135NE&X-Amz-Signature=efe598de8fd8ba77d653aa914ac3852620bb927d7958509bccb0cbae75b4db03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NTSTLLZ%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIDdr020ELCj4VDsmNSvjDqRRpyP8PDqc%2Bv5agMHBu%2BYbAiEAn3zddY81qh1HYC6t%2Fxp7bKrGuql%2BOeWDDX4tCph1buoqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG672To1%2FmU5wvPvXircA%2Fy1kKOv%2F4sJu63190fnihplG8v7J5zOHSsmLRZWDtw5ixDhW8SYF4QvCV453OTHRzAsNjVOSi3lnv1tS5iQvkuMQVm03FGxYGCGFTu%2BeHZxahKmPVppFtPIPF8TFfcQhh0xvO9OYlee%2B4CMIN1g5quuo7xh0Ynf4u7cdAwg6%2F%2BkltIuEJkqIz3RfyoRid8NH7oeXEuHjfXHvpd70oX1SLAJVzDKQbE247RZjaVnH51SYg0SIM7qJJZPgyVQIETxRh8yKNXYiTi8XSv2uSJEtJgZT15biPNHYR6FAdlGouiu6gNkCAaGaZL8Y5GwXQV174p9qOXmKFER6O2RzOdKB3NGhD9zbNdhB0MW4Dc%2FprwhVEfAlgMY%2F0ab1co9XULzMUnVHjNcREQH85qKX9ZozcufrFz7EcWsKItvMPOSllTQPDMZKoCmgtHGCdeYVzy%2B%2B8ncc4XTWtlPnrXU1meLf5giQ4eSr1K2sEUv8QZIOuG6tZdk4%2BPI6zuhX5K8Ow%2B%2Fq3KHCum1NKY%2BhTszpq3PKrkZRBEzfTafMjS5azL02Ienoy7SxDpfz85knkwDeABFHu8oyN8Q5Aa83R4nxY%2FufFt%2FVqjdVNQJDXe7cI3PJIQgGUTQRK9cbqntiAmZMLe5xMgGOqUB6lNB51Mnnde6nlyoxWFXBZIvU%2B8jD6G70Yntql9EOUqHiZXGU2UlhnVXFCldjsK6VUGQ9QwuGNEewTrpHimh%2FprThGvx5oyRLoh4jexqhiFLUyqFxTa%2B7UmUXwJlmZeCFEHQULaKUg%2BjwK29QI2D3iurJ1xgyAs7KfwkB1aRcuEV7Z7opIqFD%2FEE2cSN9WUd1HYDL2ca%2BApYvwREaGaWTgO135NE&X-Amz-Signature=6a4642e654c0b9b018a88963f3eab817e859b1ae7378605e26fcc070f6550959&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NTSTLLZ%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIDdr020ELCj4VDsmNSvjDqRRpyP8PDqc%2Bv5agMHBu%2BYbAiEAn3zddY81qh1HYC6t%2Fxp7bKrGuql%2BOeWDDX4tCph1buoqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG672To1%2FmU5wvPvXircA%2Fy1kKOv%2F4sJu63190fnihplG8v7J5zOHSsmLRZWDtw5ixDhW8SYF4QvCV453OTHRzAsNjVOSi3lnv1tS5iQvkuMQVm03FGxYGCGFTu%2BeHZxahKmPVppFtPIPF8TFfcQhh0xvO9OYlee%2B4CMIN1g5quuo7xh0Ynf4u7cdAwg6%2F%2BkltIuEJkqIz3RfyoRid8NH7oeXEuHjfXHvpd70oX1SLAJVzDKQbE247RZjaVnH51SYg0SIM7qJJZPgyVQIETxRh8yKNXYiTi8XSv2uSJEtJgZT15biPNHYR6FAdlGouiu6gNkCAaGaZL8Y5GwXQV174p9qOXmKFER6O2RzOdKB3NGhD9zbNdhB0MW4Dc%2FprwhVEfAlgMY%2F0ab1co9XULzMUnVHjNcREQH85qKX9ZozcufrFz7EcWsKItvMPOSllTQPDMZKoCmgtHGCdeYVzy%2B%2B8ncc4XTWtlPnrXU1meLf5giQ4eSr1K2sEUv8QZIOuG6tZdk4%2BPI6zuhX5K8Ow%2B%2Fq3KHCum1NKY%2BhTszpq3PKrkZRBEzfTafMjS5azL02Ienoy7SxDpfz85knkwDeABFHu8oyN8Q5Aa83R4nxY%2FufFt%2FVqjdVNQJDXe7cI3PJIQgGUTQRK9cbqntiAmZMLe5xMgGOqUB6lNB51Mnnde6nlyoxWFXBZIvU%2B8jD6G70Yntql9EOUqHiZXGU2UlhnVXFCldjsK6VUGQ9QwuGNEewTrpHimh%2FprThGvx5oyRLoh4jexqhiFLUyqFxTa%2B7UmUXwJlmZeCFEHQULaKUg%2BjwK29QI2D3iurJ1xgyAs7KfwkB1aRcuEV7Z7opIqFD%2FEE2cSN9WUd1HYDL2ca%2BApYvwREaGaWTgO135NE&X-Amz-Signature=9100528eeb35c9a784ad449fa478bafb0a1f72178ee0e7b044260c1650d894bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NTSTLLZ%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIDdr020ELCj4VDsmNSvjDqRRpyP8PDqc%2Bv5agMHBu%2BYbAiEAn3zddY81qh1HYC6t%2Fxp7bKrGuql%2BOeWDDX4tCph1buoqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG672To1%2FmU5wvPvXircA%2Fy1kKOv%2F4sJu63190fnihplG8v7J5zOHSsmLRZWDtw5ixDhW8SYF4QvCV453OTHRzAsNjVOSi3lnv1tS5iQvkuMQVm03FGxYGCGFTu%2BeHZxahKmPVppFtPIPF8TFfcQhh0xvO9OYlee%2B4CMIN1g5quuo7xh0Ynf4u7cdAwg6%2F%2BkltIuEJkqIz3RfyoRid8NH7oeXEuHjfXHvpd70oX1SLAJVzDKQbE247RZjaVnH51SYg0SIM7qJJZPgyVQIETxRh8yKNXYiTi8XSv2uSJEtJgZT15biPNHYR6FAdlGouiu6gNkCAaGaZL8Y5GwXQV174p9qOXmKFER6O2RzOdKB3NGhD9zbNdhB0MW4Dc%2FprwhVEfAlgMY%2F0ab1co9XULzMUnVHjNcREQH85qKX9ZozcufrFz7EcWsKItvMPOSllTQPDMZKoCmgtHGCdeYVzy%2B%2B8ncc4XTWtlPnrXU1meLf5giQ4eSr1K2sEUv8QZIOuG6tZdk4%2BPI6zuhX5K8Ow%2B%2Fq3KHCum1NKY%2BhTszpq3PKrkZRBEzfTafMjS5azL02Ienoy7SxDpfz85knkwDeABFHu8oyN8Q5Aa83R4nxY%2FufFt%2FVqjdVNQJDXe7cI3PJIQgGUTQRK9cbqntiAmZMLe5xMgGOqUB6lNB51Mnnde6nlyoxWFXBZIvU%2B8jD6G70Yntql9EOUqHiZXGU2UlhnVXFCldjsK6VUGQ9QwuGNEewTrpHimh%2FprThGvx5oyRLoh4jexqhiFLUyqFxTa%2B7UmUXwJlmZeCFEHQULaKUg%2BjwK29QI2D3iurJ1xgyAs7KfwkB1aRcuEV7Z7opIqFD%2FEE2cSN9WUd1HYDL2ca%2BApYvwREaGaWTgO135NE&X-Amz-Signature=5ac288dcb314cb3855fb6a6b85395f7a9b7460826cdf1e2aeb154d39084fe35f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NTSTLLZ%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIDdr020ELCj4VDsmNSvjDqRRpyP8PDqc%2Bv5agMHBu%2BYbAiEAn3zddY81qh1HYC6t%2Fxp7bKrGuql%2BOeWDDX4tCph1buoqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG672To1%2FmU5wvPvXircA%2Fy1kKOv%2F4sJu63190fnihplG8v7J5zOHSsmLRZWDtw5ixDhW8SYF4QvCV453OTHRzAsNjVOSi3lnv1tS5iQvkuMQVm03FGxYGCGFTu%2BeHZxahKmPVppFtPIPF8TFfcQhh0xvO9OYlee%2B4CMIN1g5quuo7xh0Ynf4u7cdAwg6%2F%2BkltIuEJkqIz3RfyoRid8NH7oeXEuHjfXHvpd70oX1SLAJVzDKQbE247RZjaVnH51SYg0SIM7qJJZPgyVQIETxRh8yKNXYiTi8XSv2uSJEtJgZT15biPNHYR6FAdlGouiu6gNkCAaGaZL8Y5GwXQV174p9qOXmKFER6O2RzOdKB3NGhD9zbNdhB0MW4Dc%2FprwhVEfAlgMY%2F0ab1co9XULzMUnVHjNcREQH85qKX9ZozcufrFz7EcWsKItvMPOSllTQPDMZKoCmgtHGCdeYVzy%2B%2B8ncc4XTWtlPnrXU1meLf5giQ4eSr1K2sEUv8QZIOuG6tZdk4%2BPI6zuhX5K8Ow%2B%2Fq3KHCum1NKY%2BhTszpq3PKrkZRBEzfTafMjS5azL02Ienoy7SxDpfz85knkwDeABFHu8oyN8Q5Aa83R4nxY%2FufFt%2FVqjdVNQJDXe7cI3PJIQgGUTQRK9cbqntiAmZMLe5xMgGOqUB6lNB51Mnnde6nlyoxWFXBZIvU%2B8jD6G70Yntql9EOUqHiZXGU2UlhnVXFCldjsK6VUGQ9QwuGNEewTrpHimh%2FprThGvx5oyRLoh4jexqhiFLUyqFxTa%2B7UmUXwJlmZeCFEHQULaKUg%2BjwK29QI2D3iurJ1xgyAs7KfwkB1aRcuEV7Z7opIqFD%2FEE2cSN9WUd1HYDL2ca%2BApYvwREaGaWTgO135NE&X-Amz-Signature=90d066c2d5ad24e4b6495881b5c851636c32ddb46c7f0121e5e128d85f2f4fdf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NTSTLLZ%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIDdr020ELCj4VDsmNSvjDqRRpyP8PDqc%2Bv5agMHBu%2BYbAiEAn3zddY81qh1HYC6t%2Fxp7bKrGuql%2BOeWDDX4tCph1buoqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG672To1%2FmU5wvPvXircA%2Fy1kKOv%2F4sJu63190fnihplG8v7J5zOHSsmLRZWDtw5ixDhW8SYF4QvCV453OTHRzAsNjVOSi3lnv1tS5iQvkuMQVm03FGxYGCGFTu%2BeHZxahKmPVppFtPIPF8TFfcQhh0xvO9OYlee%2B4CMIN1g5quuo7xh0Ynf4u7cdAwg6%2F%2BkltIuEJkqIz3RfyoRid8NH7oeXEuHjfXHvpd70oX1SLAJVzDKQbE247RZjaVnH51SYg0SIM7qJJZPgyVQIETxRh8yKNXYiTi8XSv2uSJEtJgZT15biPNHYR6FAdlGouiu6gNkCAaGaZL8Y5GwXQV174p9qOXmKFER6O2RzOdKB3NGhD9zbNdhB0MW4Dc%2FprwhVEfAlgMY%2F0ab1co9XULzMUnVHjNcREQH85qKX9ZozcufrFz7EcWsKItvMPOSllTQPDMZKoCmgtHGCdeYVzy%2B%2B8ncc4XTWtlPnrXU1meLf5giQ4eSr1K2sEUv8QZIOuG6tZdk4%2BPI6zuhX5K8Ow%2B%2Fq3KHCum1NKY%2BhTszpq3PKrkZRBEzfTafMjS5azL02Ienoy7SxDpfz85knkwDeABFHu8oyN8Q5Aa83R4nxY%2FufFt%2FVqjdVNQJDXe7cI3PJIQgGUTQRK9cbqntiAmZMLe5xMgGOqUB6lNB51Mnnde6nlyoxWFXBZIvU%2B8jD6G70Yntql9EOUqHiZXGU2UlhnVXFCldjsK6VUGQ9QwuGNEewTrpHimh%2FprThGvx5oyRLoh4jexqhiFLUyqFxTa%2B7UmUXwJlmZeCFEHQULaKUg%2BjwK29QI2D3iurJ1xgyAs7KfwkB1aRcuEV7Z7opIqFD%2FEE2cSN9WUd1HYDL2ca%2BApYvwREaGaWTgO135NE&X-Amz-Signature=571378a7e04552f7735b4d966789fb571901194cfa1898cbef3c21ac824f9a29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NTSTLLZ%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIDdr020ELCj4VDsmNSvjDqRRpyP8PDqc%2Bv5agMHBu%2BYbAiEAn3zddY81qh1HYC6t%2Fxp7bKrGuql%2BOeWDDX4tCph1buoqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG672To1%2FmU5wvPvXircA%2Fy1kKOv%2F4sJu63190fnihplG8v7J5zOHSsmLRZWDtw5ixDhW8SYF4QvCV453OTHRzAsNjVOSi3lnv1tS5iQvkuMQVm03FGxYGCGFTu%2BeHZxahKmPVppFtPIPF8TFfcQhh0xvO9OYlee%2B4CMIN1g5quuo7xh0Ynf4u7cdAwg6%2F%2BkltIuEJkqIz3RfyoRid8NH7oeXEuHjfXHvpd70oX1SLAJVzDKQbE247RZjaVnH51SYg0SIM7qJJZPgyVQIETxRh8yKNXYiTi8XSv2uSJEtJgZT15biPNHYR6FAdlGouiu6gNkCAaGaZL8Y5GwXQV174p9qOXmKFER6O2RzOdKB3NGhD9zbNdhB0MW4Dc%2FprwhVEfAlgMY%2F0ab1co9XULzMUnVHjNcREQH85qKX9ZozcufrFz7EcWsKItvMPOSllTQPDMZKoCmgtHGCdeYVzy%2B%2B8ncc4XTWtlPnrXU1meLf5giQ4eSr1K2sEUv8QZIOuG6tZdk4%2BPI6zuhX5K8Ow%2B%2Fq3KHCum1NKY%2BhTszpq3PKrkZRBEzfTafMjS5azL02Ienoy7SxDpfz85knkwDeABFHu8oyN8Q5Aa83R4nxY%2FufFt%2FVqjdVNQJDXe7cI3PJIQgGUTQRK9cbqntiAmZMLe5xMgGOqUB6lNB51Mnnde6nlyoxWFXBZIvU%2B8jD6G70Yntql9EOUqHiZXGU2UlhnVXFCldjsK6VUGQ9QwuGNEewTrpHimh%2FprThGvx5oyRLoh4jexqhiFLUyqFxTa%2B7UmUXwJlmZeCFEHQULaKUg%2BjwK29QI2D3iurJ1xgyAs7KfwkB1aRcuEV7Z7opIqFD%2FEE2cSN9WUd1HYDL2ca%2BApYvwREaGaWTgO135NE&X-Amz-Signature=94d1e16246578e7e68e65ab086bf1698a449816d4f7cf9a0c52cb09e7dffbba7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

