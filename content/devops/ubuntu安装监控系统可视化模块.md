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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXFWNRM2%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDj6umq9nfs9afM8jUo%2F8hcM%2FzW7dN5lLrMnMBPy%2FRdtgIgBxCkcHiWwIszowlYJsmqB2Y%2FGROxFWqgB2a2pBXl7qIq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDBZmt4x%2Bw6XJ1ElGIircA6HZ%2FuRQnERtPFd%2BwI2RHQIgMGt8ARHqq0sE8N8emyUENmavI06VSTto2oJ0xH2aypUzGEDwJNXXf6D36Iw0AhSSqyc83menISZMCh92s0WVCus8oYNRIbAlVnfBTAu40jkCQUqT2FXV1InuKcKegszGnflhIDC0y8xAZc9D37%2B7IBW94Uv5PkKRUr%2BMVqRoKN1LsYjFp3ZxQfMHKxV9IW%2FInADRsEG%2BfW2YwgJmto6XvILSnGD2%2BAKm7OVCEXa6LSq6SqJbrxBCEtAo1ftttAAScCw6mOon5zUK5q%2BokG0o%2FAy6gClNY0I7dekHnjYPIRl3IGGHUDWcxcMWRsfH5GCTC3c1RQvqORHoEQHvock1q11IrOlEUgk2FQnIQ%2BOhyCm70kJXi%2F5QCI9VVKqEoaElq34%2FXkVwf4%2FyiXeoup7a9sFc81o6k%2FMgwCRD%2B3J8eL205DL6qewpPeYDuFddzBGzof78aaMSUK%2F%2FcwoASGQRvhUeyY0d%2FVmvTmrMD2YvvmCum4%2Fqj2rLWus%2FMEv1bTq%2BOc7GSVXEw0TLSNqwIZUXgzretzKlZAwpdmHfDASqSGIxl%2BsrzU%2FrJYZlDUO3lsYGr5pPoLs0foqShNsMuxBqu91HuqMhtH8a4HhpMMyrlMkGOqUBSnQwEVb0lYlr6bHVks6ThfGGa%2BuAfhUZrGo0rmno0sQKJkemTG46OvWZnx%2FMGtckTojM7nO3hrfT5fd%2FNMKPrg30Zl29DrN3zGgqwEISkUetwZLq2dZu6RSMFMl1TDus0TFa1GX597svSmtuudxIcvfvYhKfi%2FiborcDpfDLG97RJO5nS%2BmICCdGC93dcsA3ASrk9g%2BrbavBnnsXkXx2vlYcL4qa&X-Amz-Signature=615b12d8f8697e3768d6076632b00dd6e2ac30d2b459e75f0b0f4d5df3fce155&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXFWNRM2%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDj6umq9nfs9afM8jUo%2F8hcM%2FzW7dN5lLrMnMBPy%2FRdtgIgBxCkcHiWwIszowlYJsmqB2Y%2FGROxFWqgB2a2pBXl7qIq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDBZmt4x%2Bw6XJ1ElGIircA6HZ%2FuRQnERtPFd%2BwI2RHQIgMGt8ARHqq0sE8N8emyUENmavI06VSTto2oJ0xH2aypUzGEDwJNXXf6D36Iw0AhSSqyc83menISZMCh92s0WVCus8oYNRIbAlVnfBTAu40jkCQUqT2FXV1InuKcKegszGnflhIDC0y8xAZc9D37%2B7IBW94Uv5PkKRUr%2BMVqRoKN1LsYjFp3ZxQfMHKxV9IW%2FInADRsEG%2BfW2YwgJmto6XvILSnGD2%2BAKm7OVCEXa6LSq6SqJbrxBCEtAo1ftttAAScCw6mOon5zUK5q%2BokG0o%2FAy6gClNY0I7dekHnjYPIRl3IGGHUDWcxcMWRsfH5GCTC3c1RQvqORHoEQHvock1q11IrOlEUgk2FQnIQ%2BOhyCm70kJXi%2F5QCI9VVKqEoaElq34%2FXkVwf4%2FyiXeoup7a9sFc81o6k%2FMgwCRD%2B3J8eL205DL6qewpPeYDuFddzBGzof78aaMSUK%2F%2FcwoASGQRvhUeyY0d%2FVmvTmrMD2YvvmCum4%2Fqj2rLWus%2FMEv1bTq%2BOc7GSVXEw0TLSNqwIZUXgzretzKlZAwpdmHfDASqSGIxl%2BsrzU%2FrJYZlDUO3lsYGr5pPoLs0foqShNsMuxBqu91HuqMhtH8a4HhpMMyrlMkGOqUBSnQwEVb0lYlr6bHVks6ThfGGa%2BuAfhUZrGo0rmno0sQKJkemTG46OvWZnx%2FMGtckTojM7nO3hrfT5fd%2FNMKPrg30Zl29DrN3zGgqwEISkUetwZLq2dZu6RSMFMl1TDus0TFa1GX597svSmtuudxIcvfvYhKfi%2FiborcDpfDLG97RJO5nS%2BmICCdGC93dcsA3ASrk9g%2BrbavBnnsXkXx2vlYcL4qa&X-Amz-Signature=548766e92b5a23ff439e86363a7cbfa5da28c0c671331fc1aef626ce98d4ff5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXFWNRM2%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDj6umq9nfs9afM8jUo%2F8hcM%2FzW7dN5lLrMnMBPy%2FRdtgIgBxCkcHiWwIszowlYJsmqB2Y%2FGROxFWqgB2a2pBXl7qIq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDBZmt4x%2Bw6XJ1ElGIircA6HZ%2FuRQnERtPFd%2BwI2RHQIgMGt8ARHqq0sE8N8emyUENmavI06VSTto2oJ0xH2aypUzGEDwJNXXf6D36Iw0AhSSqyc83menISZMCh92s0WVCus8oYNRIbAlVnfBTAu40jkCQUqT2FXV1InuKcKegszGnflhIDC0y8xAZc9D37%2B7IBW94Uv5PkKRUr%2BMVqRoKN1LsYjFp3ZxQfMHKxV9IW%2FInADRsEG%2BfW2YwgJmto6XvILSnGD2%2BAKm7OVCEXa6LSq6SqJbrxBCEtAo1ftttAAScCw6mOon5zUK5q%2BokG0o%2FAy6gClNY0I7dekHnjYPIRl3IGGHUDWcxcMWRsfH5GCTC3c1RQvqORHoEQHvock1q11IrOlEUgk2FQnIQ%2BOhyCm70kJXi%2F5QCI9VVKqEoaElq34%2FXkVwf4%2FyiXeoup7a9sFc81o6k%2FMgwCRD%2B3J8eL205DL6qewpPeYDuFddzBGzof78aaMSUK%2F%2FcwoASGQRvhUeyY0d%2FVmvTmrMD2YvvmCum4%2Fqj2rLWus%2FMEv1bTq%2BOc7GSVXEw0TLSNqwIZUXgzretzKlZAwpdmHfDASqSGIxl%2BsrzU%2FrJYZlDUO3lsYGr5pPoLs0foqShNsMuxBqu91HuqMhtH8a4HhpMMyrlMkGOqUBSnQwEVb0lYlr6bHVks6ThfGGa%2BuAfhUZrGo0rmno0sQKJkemTG46OvWZnx%2FMGtckTojM7nO3hrfT5fd%2FNMKPrg30Zl29DrN3zGgqwEISkUetwZLq2dZu6RSMFMl1TDus0TFa1GX597svSmtuudxIcvfvYhKfi%2FiborcDpfDLG97RJO5nS%2BmICCdGC93dcsA3ASrk9g%2BrbavBnnsXkXx2vlYcL4qa&X-Amz-Signature=6442721e7402e0811057e9689f91122c75a225292b938561b879b4e237c0fafc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXFWNRM2%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDj6umq9nfs9afM8jUo%2F8hcM%2FzW7dN5lLrMnMBPy%2FRdtgIgBxCkcHiWwIszowlYJsmqB2Y%2FGROxFWqgB2a2pBXl7qIq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDBZmt4x%2Bw6XJ1ElGIircA6HZ%2FuRQnERtPFd%2BwI2RHQIgMGt8ARHqq0sE8N8emyUENmavI06VSTto2oJ0xH2aypUzGEDwJNXXf6D36Iw0AhSSqyc83menISZMCh92s0WVCus8oYNRIbAlVnfBTAu40jkCQUqT2FXV1InuKcKegszGnflhIDC0y8xAZc9D37%2B7IBW94Uv5PkKRUr%2BMVqRoKN1LsYjFp3ZxQfMHKxV9IW%2FInADRsEG%2BfW2YwgJmto6XvILSnGD2%2BAKm7OVCEXa6LSq6SqJbrxBCEtAo1ftttAAScCw6mOon5zUK5q%2BokG0o%2FAy6gClNY0I7dekHnjYPIRl3IGGHUDWcxcMWRsfH5GCTC3c1RQvqORHoEQHvock1q11IrOlEUgk2FQnIQ%2BOhyCm70kJXi%2F5QCI9VVKqEoaElq34%2FXkVwf4%2FyiXeoup7a9sFc81o6k%2FMgwCRD%2B3J8eL205DL6qewpPeYDuFddzBGzof78aaMSUK%2F%2FcwoASGQRvhUeyY0d%2FVmvTmrMD2YvvmCum4%2Fqj2rLWus%2FMEv1bTq%2BOc7GSVXEw0TLSNqwIZUXgzretzKlZAwpdmHfDASqSGIxl%2BsrzU%2FrJYZlDUO3lsYGr5pPoLs0foqShNsMuxBqu91HuqMhtH8a4HhpMMyrlMkGOqUBSnQwEVb0lYlr6bHVks6ThfGGa%2BuAfhUZrGo0rmno0sQKJkemTG46OvWZnx%2FMGtckTojM7nO3hrfT5fd%2FNMKPrg30Zl29DrN3zGgqwEISkUetwZLq2dZu6RSMFMl1TDus0TFa1GX597svSmtuudxIcvfvYhKfi%2FiborcDpfDLG97RJO5nS%2BmICCdGC93dcsA3ASrk9g%2BrbavBnnsXkXx2vlYcL4qa&X-Amz-Signature=bdd04be5cadeb6bff71c832c491286307d3a7bcca3422dedf47935af14af1fec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXFWNRM2%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDj6umq9nfs9afM8jUo%2F8hcM%2FzW7dN5lLrMnMBPy%2FRdtgIgBxCkcHiWwIszowlYJsmqB2Y%2FGROxFWqgB2a2pBXl7qIq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDBZmt4x%2Bw6XJ1ElGIircA6HZ%2FuRQnERtPFd%2BwI2RHQIgMGt8ARHqq0sE8N8emyUENmavI06VSTto2oJ0xH2aypUzGEDwJNXXf6D36Iw0AhSSqyc83menISZMCh92s0WVCus8oYNRIbAlVnfBTAu40jkCQUqT2FXV1InuKcKegszGnflhIDC0y8xAZc9D37%2B7IBW94Uv5PkKRUr%2BMVqRoKN1LsYjFp3ZxQfMHKxV9IW%2FInADRsEG%2BfW2YwgJmto6XvILSnGD2%2BAKm7OVCEXa6LSq6SqJbrxBCEtAo1ftttAAScCw6mOon5zUK5q%2BokG0o%2FAy6gClNY0I7dekHnjYPIRl3IGGHUDWcxcMWRsfH5GCTC3c1RQvqORHoEQHvock1q11IrOlEUgk2FQnIQ%2BOhyCm70kJXi%2F5QCI9VVKqEoaElq34%2FXkVwf4%2FyiXeoup7a9sFc81o6k%2FMgwCRD%2B3J8eL205DL6qewpPeYDuFddzBGzof78aaMSUK%2F%2FcwoASGQRvhUeyY0d%2FVmvTmrMD2YvvmCum4%2Fqj2rLWus%2FMEv1bTq%2BOc7GSVXEw0TLSNqwIZUXgzretzKlZAwpdmHfDASqSGIxl%2BsrzU%2FrJYZlDUO3lsYGr5pPoLs0foqShNsMuxBqu91HuqMhtH8a4HhpMMyrlMkGOqUBSnQwEVb0lYlr6bHVks6ThfGGa%2BuAfhUZrGo0rmno0sQKJkemTG46OvWZnx%2FMGtckTojM7nO3hrfT5fd%2FNMKPrg30Zl29DrN3zGgqwEISkUetwZLq2dZu6RSMFMl1TDus0TFa1GX597svSmtuudxIcvfvYhKfi%2FiborcDpfDLG97RJO5nS%2BmICCdGC93dcsA3ASrk9g%2BrbavBnnsXkXx2vlYcL4qa&X-Amz-Signature=67b1a13154e557952359464189f0dcafafddc3aaccacd9b4c99adc5ed54f28d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXFWNRM2%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDj6umq9nfs9afM8jUo%2F8hcM%2FzW7dN5lLrMnMBPy%2FRdtgIgBxCkcHiWwIszowlYJsmqB2Y%2FGROxFWqgB2a2pBXl7qIq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDBZmt4x%2Bw6XJ1ElGIircA6HZ%2FuRQnERtPFd%2BwI2RHQIgMGt8ARHqq0sE8N8emyUENmavI06VSTto2oJ0xH2aypUzGEDwJNXXf6D36Iw0AhSSqyc83menISZMCh92s0WVCus8oYNRIbAlVnfBTAu40jkCQUqT2FXV1InuKcKegszGnflhIDC0y8xAZc9D37%2B7IBW94Uv5PkKRUr%2BMVqRoKN1LsYjFp3ZxQfMHKxV9IW%2FInADRsEG%2BfW2YwgJmto6XvILSnGD2%2BAKm7OVCEXa6LSq6SqJbrxBCEtAo1ftttAAScCw6mOon5zUK5q%2BokG0o%2FAy6gClNY0I7dekHnjYPIRl3IGGHUDWcxcMWRsfH5GCTC3c1RQvqORHoEQHvock1q11IrOlEUgk2FQnIQ%2BOhyCm70kJXi%2F5QCI9VVKqEoaElq34%2FXkVwf4%2FyiXeoup7a9sFc81o6k%2FMgwCRD%2B3J8eL205DL6qewpPeYDuFddzBGzof78aaMSUK%2F%2FcwoASGQRvhUeyY0d%2FVmvTmrMD2YvvmCum4%2Fqj2rLWus%2FMEv1bTq%2BOc7GSVXEw0TLSNqwIZUXgzretzKlZAwpdmHfDASqSGIxl%2BsrzU%2FrJYZlDUO3lsYGr5pPoLs0foqShNsMuxBqu91HuqMhtH8a4HhpMMyrlMkGOqUBSnQwEVb0lYlr6bHVks6ThfGGa%2BuAfhUZrGo0rmno0sQKJkemTG46OvWZnx%2FMGtckTojM7nO3hrfT5fd%2FNMKPrg30Zl29DrN3zGgqwEISkUetwZLq2dZu6RSMFMl1TDus0TFa1GX597svSmtuudxIcvfvYhKfi%2FiborcDpfDLG97RJO5nS%2BmICCdGC93dcsA3ASrk9g%2BrbavBnnsXkXx2vlYcL4qa&X-Amz-Signature=ae9ee0a0bf0a0223daee109309be183ea155a82eaaaabb2bc9714d9168f5e1d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXFWNRM2%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDj6umq9nfs9afM8jUo%2F8hcM%2FzW7dN5lLrMnMBPy%2FRdtgIgBxCkcHiWwIszowlYJsmqB2Y%2FGROxFWqgB2a2pBXl7qIq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDBZmt4x%2Bw6XJ1ElGIircA6HZ%2FuRQnERtPFd%2BwI2RHQIgMGt8ARHqq0sE8N8emyUENmavI06VSTto2oJ0xH2aypUzGEDwJNXXf6D36Iw0AhSSqyc83menISZMCh92s0WVCus8oYNRIbAlVnfBTAu40jkCQUqT2FXV1InuKcKegszGnflhIDC0y8xAZc9D37%2B7IBW94Uv5PkKRUr%2BMVqRoKN1LsYjFp3ZxQfMHKxV9IW%2FInADRsEG%2BfW2YwgJmto6XvILSnGD2%2BAKm7OVCEXa6LSq6SqJbrxBCEtAo1ftttAAScCw6mOon5zUK5q%2BokG0o%2FAy6gClNY0I7dekHnjYPIRl3IGGHUDWcxcMWRsfH5GCTC3c1RQvqORHoEQHvock1q11IrOlEUgk2FQnIQ%2BOhyCm70kJXi%2F5QCI9VVKqEoaElq34%2FXkVwf4%2FyiXeoup7a9sFc81o6k%2FMgwCRD%2B3J8eL205DL6qewpPeYDuFddzBGzof78aaMSUK%2F%2FcwoASGQRvhUeyY0d%2FVmvTmrMD2YvvmCum4%2Fqj2rLWus%2FMEv1bTq%2BOc7GSVXEw0TLSNqwIZUXgzretzKlZAwpdmHfDASqSGIxl%2BsrzU%2FrJYZlDUO3lsYGr5pPoLs0foqShNsMuxBqu91HuqMhtH8a4HhpMMyrlMkGOqUBSnQwEVb0lYlr6bHVks6ThfGGa%2BuAfhUZrGo0rmno0sQKJkemTG46OvWZnx%2FMGtckTojM7nO3hrfT5fd%2FNMKPrg30Zl29DrN3zGgqwEISkUetwZLq2dZu6RSMFMl1TDus0TFa1GX597svSmtuudxIcvfvYhKfi%2FiborcDpfDLG97RJO5nS%2BmICCdGC93dcsA3ASrk9g%2BrbavBnnsXkXx2vlYcL4qa&X-Amz-Signature=a92951f9f6adb2908ffd982530a9e353fc663aa88a72f0fcac2b6fdab1b1ddd8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

