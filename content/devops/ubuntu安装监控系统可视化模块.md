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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5P433HZ%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyLU84wQc6rZ6AXnLQbJm9pYlVf5DP0ppd3JHRtTxvLwIgIVWQGsfXfslk9YEsZvNSJzE9iDw2dytxUlT9tO6KF%2FkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFomce801C2%2F7s1rIyrcA064iezzSUQMw4kSjgR2FIEtO%2F2hdnsKSK4ktrlTHMcgxO9BtN%2FN0jzbruEJzNNQcYZ2NTmF5Qr5d%2BaVMuxGzJCYD8psDn1AM%2FhIs8bOp7Ce0hfXvdPvMLF7uK%2FkiqwbycdZkUZ73bJmxCfNyXB98DHoojHqwmmLHhfls0GyPmZALRxKf8avqU5ADnq8wGDplm9ZV6SSk6wk0YLCXi%2BsGPsjX0pODXaLJppXYUN4nOzdHy43Abw1mu79zx641luWgKrvM9BEgegcxYcs7yPPNM0PjByzR0MnveO7FuwcksbOAeYFV56ilLL%2F7v3BrxRtlmNC8oViY2R4oS8m2KN2KLJL0Y9dM078FCdFzEGN70E6Uke1UL%2BfC2NFuVU03upzlCYYrf1c607gHKYSq91GJtZleB0MmfC%2FJL4I2DlAN33MXW6Ms9P%2B%2FWtGbtib1uDBiBS3MLYQq8xYRHj0NParXioF0D4k7qz5jdmMl6iPXk5ZeNMutuOtxlwEIdsJiUrgNoFb%2FKRLoTAZVF8tRUDRAAz%2Bpcuufu60VzzBZ3%2B4GW%2FXGnwu1PRYi3AuhrMCZGuAJAfjGA56k4NGD3yV6JySz2HTZpGc1h9yxvEWW9jtlXp%2FC41IjiQ7uMhbG6KjMJrDqswGOqUBypCSMl4m5XV%2FbtF4DxBHIlvIDVfkTYCmpi5CHhuz3V2wXZWmKpn0N6H2Lbxk0QANRshtN1NeUwx5oxkMxj0acY1hLcrfoXC%2Bxoua%2FjYnND9PyFq1F1pBOdaJCSVmySpBZghjLv5S37nxfa0r2V4ZvCvtuY9nNxBEnrjnGaFtv0X0B9GDnA8smOeGcDPfIbV6NPFchevFwuKvZ6deuhMwOKIWrTKH&X-Amz-Signature=d842ff34606edf6993d4adbfdfccb240183fe27e5b31de25d770c06471698882&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5P433HZ%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyLU84wQc6rZ6AXnLQbJm9pYlVf5DP0ppd3JHRtTxvLwIgIVWQGsfXfslk9YEsZvNSJzE9iDw2dytxUlT9tO6KF%2FkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFomce801C2%2F7s1rIyrcA064iezzSUQMw4kSjgR2FIEtO%2F2hdnsKSK4ktrlTHMcgxO9BtN%2FN0jzbruEJzNNQcYZ2NTmF5Qr5d%2BaVMuxGzJCYD8psDn1AM%2FhIs8bOp7Ce0hfXvdPvMLF7uK%2FkiqwbycdZkUZ73bJmxCfNyXB98DHoojHqwmmLHhfls0GyPmZALRxKf8avqU5ADnq8wGDplm9ZV6SSk6wk0YLCXi%2BsGPsjX0pODXaLJppXYUN4nOzdHy43Abw1mu79zx641luWgKrvM9BEgegcxYcs7yPPNM0PjByzR0MnveO7FuwcksbOAeYFV56ilLL%2F7v3BrxRtlmNC8oViY2R4oS8m2KN2KLJL0Y9dM078FCdFzEGN70E6Uke1UL%2BfC2NFuVU03upzlCYYrf1c607gHKYSq91GJtZleB0MmfC%2FJL4I2DlAN33MXW6Ms9P%2B%2FWtGbtib1uDBiBS3MLYQq8xYRHj0NParXioF0D4k7qz5jdmMl6iPXk5ZeNMutuOtxlwEIdsJiUrgNoFb%2FKRLoTAZVF8tRUDRAAz%2Bpcuufu60VzzBZ3%2B4GW%2FXGnwu1PRYi3AuhrMCZGuAJAfjGA56k4NGD3yV6JySz2HTZpGc1h9yxvEWW9jtlXp%2FC41IjiQ7uMhbG6KjMJrDqswGOqUBypCSMl4m5XV%2FbtF4DxBHIlvIDVfkTYCmpi5CHhuz3V2wXZWmKpn0N6H2Lbxk0QANRshtN1NeUwx5oxkMxj0acY1hLcrfoXC%2Bxoua%2FjYnND9PyFq1F1pBOdaJCSVmySpBZghjLv5S37nxfa0r2V4ZvCvtuY9nNxBEnrjnGaFtv0X0B9GDnA8smOeGcDPfIbV6NPFchevFwuKvZ6deuhMwOKIWrTKH&X-Amz-Signature=59e4da1fcd8c09cecbfb1e862687ddee3797bb06e1ef74eb923c0136c21b1bc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5P433HZ%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyLU84wQc6rZ6AXnLQbJm9pYlVf5DP0ppd3JHRtTxvLwIgIVWQGsfXfslk9YEsZvNSJzE9iDw2dytxUlT9tO6KF%2FkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFomce801C2%2F7s1rIyrcA064iezzSUQMw4kSjgR2FIEtO%2F2hdnsKSK4ktrlTHMcgxO9BtN%2FN0jzbruEJzNNQcYZ2NTmF5Qr5d%2BaVMuxGzJCYD8psDn1AM%2FhIs8bOp7Ce0hfXvdPvMLF7uK%2FkiqwbycdZkUZ73bJmxCfNyXB98DHoojHqwmmLHhfls0GyPmZALRxKf8avqU5ADnq8wGDplm9ZV6SSk6wk0YLCXi%2BsGPsjX0pODXaLJppXYUN4nOzdHy43Abw1mu79zx641luWgKrvM9BEgegcxYcs7yPPNM0PjByzR0MnveO7FuwcksbOAeYFV56ilLL%2F7v3BrxRtlmNC8oViY2R4oS8m2KN2KLJL0Y9dM078FCdFzEGN70E6Uke1UL%2BfC2NFuVU03upzlCYYrf1c607gHKYSq91GJtZleB0MmfC%2FJL4I2DlAN33MXW6Ms9P%2B%2FWtGbtib1uDBiBS3MLYQq8xYRHj0NParXioF0D4k7qz5jdmMl6iPXk5ZeNMutuOtxlwEIdsJiUrgNoFb%2FKRLoTAZVF8tRUDRAAz%2Bpcuufu60VzzBZ3%2B4GW%2FXGnwu1PRYi3AuhrMCZGuAJAfjGA56k4NGD3yV6JySz2HTZpGc1h9yxvEWW9jtlXp%2FC41IjiQ7uMhbG6KjMJrDqswGOqUBypCSMl4m5XV%2FbtF4DxBHIlvIDVfkTYCmpi5CHhuz3V2wXZWmKpn0N6H2Lbxk0QANRshtN1NeUwx5oxkMxj0acY1hLcrfoXC%2Bxoua%2FjYnND9PyFq1F1pBOdaJCSVmySpBZghjLv5S37nxfa0r2V4ZvCvtuY9nNxBEnrjnGaFtv0X0B9GDnA8smOeGcDPfIbV6NPFchevFwuKvZ6deuhMwOKIWrTKH&X-Amz-Signature=f5648a81481feccf4a39d8c6b405310a3ae8a02179a4d05ea77a5e0ccf30779d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5P433HZ%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyLU84wQc6rZ6AXnLQbJm9pYlVf5DP0ppd3JHRtTxvLwIgIVWQGsfXfslk9YEsZvNSJzE9iDw2dytxUlT9tO6KF%2FkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFomce801C2%2F7s1rIyrcA064iezzSUQMw4kSjgR2FIEtO%2F2hdnsKSK4ktrlTHMcgxO9BtN%2FN0jzbruEJzNNQcYZ2NTmF5Qr5d%2BaVMuxGzJCYD8psDn1AM%2FhIs8bOp7Ce0hfXvdPvMLF7uK%2FkiqwbycdZkUZ73bJmxCfNyXB98DHoojHqwmmLHhfls0GyPmZALRxKf8avqU5ADnq8wGDplm9ZV6SSk6wk0YLCXi%2BsGPsjX0pODXaLJppXYUN4nOzdHy43Abw1mu79zx641luWgKrvM9BEgegcxYcs7yPPNM0PjByzR0MnveO7FuwcksbOAeYFV56ilLL%2F7v3BrxRtlmNC8oViY2R4oS8m2KN2KLJL0Y9dM078FCdFzEGN70E6Uke1UL%2BfC2NFuVU03upzlCYYrf1c607gHKYSq91GJtZleB0MmfC%2FJL4I2DlAN33MXW6Ms9P%2B%2FWtGbtib1uDBiBS3MLYQq8xYRHj0NParXioF0D4k7qz5jdmMl6iPXk5ZeNMutuOtxlwEIdsJiUrgNoFb%2FKRLoTAZVF8tRUDRAAz%2Bpcuufu60VzzBZ3%2B4GW%2FXGnwu1PRYi3AuhrMCZGuAJAfjGA56k4NGD3yV6JySz2HTZpGc1h9yxvEWW9jtlXp%2FC41IjiQ7uMhbG6KjMJrDqswGOqUBypCSMl4m5XV%2FbtF4DxBHIlvIDVfkTYCmpi5CHhuz3V2wXZWmKpn0N6H2Lbxk0QANRshtN1NeUwx5oxkMxj0acY1hLcrfoXC%2Bxoua%2FjYnND9PyFq1F1pBOdaJCSVmySpBZghjLv5S37nxfa0r2V4ZvCvtuY9nNxBEnrjnGaFtv0X0B9GDnA8smOeGcDPfIbV6NPFchevFwuKvZ6deuhMwOKIWrTKH&X-Amz-Signature=54eee0bf0db01d5cecbc31b851dbc2fdeb978eb402a2bbe724399dcc5e97cdf7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5P433HZ%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyLU84wQc6rZ6AXnLQbJm9pYlVf5DP0ppd3JHRtTxvLwIgIVWQGsfXfslk9YEsZvNSJzE9iDw2dytxUlT9tO6KF%2FkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFomce801C2%2F7s1rIyrcA064iezzSUQMw4kSjgR2FIEtO%2F2hdnsKSK4ktrlTHMcgxO9BtN%2FN0jzbruEJzNNQcYZ2NTmF5Qr5d%2BaVMuxGzJCYD8psDn1AM%2FhIs8bOp7Ce0hfXvdPvMLF7uK%2FkiqwbycdZkUZ73bJmxCfNyXB98DHoojHqwmmLHhfls0GyPmZALRxKf8avqU5ADnq8wGDplm9ZV6SSk6wk0YLCXi%2BsGPsjX0pODXaLJppXYUN4nOzdHy43Abw1mu79zx641luWgKrvM9BEgegcxYcs7yPPNM0PjByzR0MnveO7FuwcksbOAeYFV56ilLL%2F7v3BrxRtlmNC8oViY2R4oS8m2KN2KLJL0Y9dM078FCdFzEGN70E6Uke1UL%2BfC2NFuVU03upzlCYYrf1c607gHKYSq91GJtZleB0MmfC%2FJL4I2DlAN33MXW6Ms9P%2B%2FWtGbtib1uDBiBS3MLYQq8xYRHj0NParXioF0D4k7qz5jdmMl6iPXk5ZeNMutuOtxlwEIdsJiUrgNoFb%2FKRLoTAZVF8tRUDRAAz%2Bpcuufu60VzzBZ3%2B4GW%2FXGnwu1PRYi3AuhrMCZGuAJAfjGA56k4NGD3yV6JySz2HTZpGc1h9yxvEWW9jtlXp%2FC41IjiQ7uMhbG6KjMJrDqswGOqUBypCSMl4m5XV%2FbtF4DxBHIlvIDVfkTYCmpi5CHhuz3V2wXZWmKpn0N6H2Lbxk0QANRshtN1NeUwx5oxkMxj0acY1hLcrfoXC%2Bxoua%2FjYnND9PyFq1F1pBOdaJCSVmySpBZghjLv5S37nxfa0r2V4ZvCvtuY9nNxBEnrjnGaFtv0X0B9GDnA8smOeGcDPfIbV6NPFchevFwuKvZ6deuhMwOKIWrTKH&X-Amz-Signature=33a94581c996a1a7c7c2938ec9cf1101a7435af2e4e1ac285de5c922e4d56e47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5P433HZ%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyLU84wQc6rZ6AXnLQbJm9pYlVf5DP0ppd3JHRtTxvLwIgIVWQGsfXfslk9YEsZvNSJzE9iDw2dytxUlT9tO6KF%2FkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFomce801C2%2F7s1rIyrcA064iezzSUQMw4kSjgR2FIEtO%2F2hdnsKSK4ktrlTHMcgxO9BtN%2FN0jzbruEJzNNQcYZ2NTmF5Qr5d%2BaVMuxGzJCYD8psDn1AM%2FhIs8bOp7Ce0hfXvdPvMLF7uK%2FkiqwbycdZkUZ73bJmxCfNyXB98DHoojHqwmmLHhfls0GyPmZALRxKf8avqU5ADnq8wGDplm9ZV6SSk6wk0YLCXi%2BsGPsjX0pODXaLJppXYUN4nOzdHy43Abw1mu79zx641luWgKrvM9BEgegcxYcs7yPPNM0PjByzR0MnveO7FuwcksbOAeYFV56ilLL%2F7v3BrxRtlmNC8oViY2R4oS8m2KN2KLJL0Y9dM078FCdFzEGN70E6Uke1UL%2BfC2NFuVU03upzlCYYrf1c607gHKYSq91GJtZleB0MmfC%2FJL4I2DlAN33MXW6Ms9P%2B%2FWtGbtib1uDBiBS3MLYQq8xYRHj0NParXioF0D4k7qz5jdmMl6iPXk5ZeNMutuOtxlwEIdsJiUrgNoFb%2FKRLoTAZVF8tRUDRAAz%2Bpcuufu60VzzBZ3%2B4GW%2FXGnwu1PRYi3AuhrMCZGuAJAfjGA56k4NGD3yV6JySz2HTZpGc1h9yxvEWW9jtlXp%2FC41IjiQ7uMhbG6KjMJrDqswGOqUBypCSMl4m5XV%2FbtF4DxBHIlvIDVfkTYCmpi5CHhuz3V2wXZWmKpn0N6H2Lbxk0QANRshtN1NeUwx5oxkMxj0acY1hLcrfoXC%2Bxoua%2FjYnND9PyFq1F1pBOdaJCSVmySpBZghjLv5S37nxfa0r2V4ZvCvtuY9nNxBEnrjnGaFtv0X0B9GDnA8smOeGcDPfIbV6NPFchevFwuKvZ6deuhMwOKIWrTKH&X-Amz-Signature=3a00e43fc7bd7db509771d76350c370b5ee73919e0d4205e44618833fd159362&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5P433HZ%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyLU84wQc6rZ6AXnLQbJm9pYlVf5DP0ppd3JHRtTxvLwIgIVWQGsfXfslk9YEsZvNSJzE9iDw2dytxUlT9tO6KF%2FkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFomce801C2%2F7s1rIyrcA064iezzSUQMw4kSjgR2FIEtO%2F2hdnsKSK4ktrlTHMcgxO9BtN%2FN0jzbruEJzNNQcYZ2NTmF5Qr5d%2BaVMuxGzJCYD8psDn1AM%2FhIs8bOp7Ce0hfXvdPvMLF7uK%2FkiqwbycdZkUZ73bJmxCfNyXB98DHoojHqwmmLHhfls0GyPmZALRxKf8avqU5ADnq8wGDplm9ZV6SSk6wk0YLCXi%2BsGPsjX0pODXaLJppXYUN4nOzdHy43Abw1mu79zx641luWgKrvM9BEgegcxYcs7yPPNM0PjByzR0MnveO7FuwcksbOAeYFV56ilLL%2F7v3BrxRtlmNC8oViY2R4oS8m2KN2KLJL0Y9dM078FCdFzEGN70E6Uke1UL%2BfC2NFuVU03upzlCYYrf1c607gHKYSq91GJtZleB0MmfC%2FJL4I2DlAN33MXW6Ms9P%2B%2FWtGbtib1uDBiBS3MLYQq8xYRHj0NParXioF0D4k7qz5jdmMl6iPXk5ZeNMutuOtxlwEIdsJiUrgNoFb%2FKRLoTAZVF8tRUDRAAz%2Bpcuufu60VzzBZ3%2B4GW%2FXGnwu1PRYi3AuhrMCZGuAJAfjGA56k4NGD3yV6JySz2HTZpGc1h9yxvEWW9jtlXp%2FC41IjiQ7uMhbG6KjMJrDqswGOqUBypCSMl4m5XV%2FbtF4DxBHIlvIDVfkTYCmpi5CHhuz3V2wXZWmKpn0N6H2Lbxk0QANRshtN1NeUwx5oxkMxj0acY1hLcrfoXC%2Bxoua%2FjYnND9PyFq1F1pBOdaJCSVmySpBZghjLv5S37nxfa0r2V4ZvCvtuY9nNxBEnrjnGaFtv0X0B9GDnA8smOeGcDPfIbV6NPFchevFwuKvZ6deuhMwOKIWrTKH&X-Amz-Signature=a8792a74e8c94bfd53d3f566235038e65dade9b4a29dd6ea30be6618c3fb7413&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

