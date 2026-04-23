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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOEKKSRH%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8yZM%2BkPhoyqxdYkRsWs%2F5VmTwCiZfu2%2Bv0fvNptYsPwIgDtASO5j6dslNj3g8B4GzICfW6bkIX0ssI3F33FWGu%2Bkq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDDt84MXSJbthX8IxYyrcA1bxYe0f7PM9tqZ5aR4wX0J%2BkpgEGEspB3xLE2Q7ffKE68O2GhpSGj0XoqUyt1%2FXaV0m3vmw0GyWL0SIWcdhYl7sUFa95YSqVOZmPy9vqnRpMlcZEyeZorJZe0sdFQIqob1E3Ms2ZLQ2gCv79KUYepw944aV644i0BaQyk8j8QFeidogAIeINhC%2FgTNeeYKQmkraclKED21SPzRl6vIXBKX3P%2Fe9mQn55hphmwpr9j4puhbgLanoyYB%2BiS4ZT6aReesDEIUYQmWW%2FnpGi%2FRUvhQeACaYjEc3cgZh4dHo5i%2FujZWMtDGvCnXODbe96qsZdpuJYow8AIIiQK8auKQ1DeF6EkEWcFkaAt%2FDVKNhSc5NdWtdqYOT8gBapc31%2Fn%2FUdjF%2BUC23f04q6dBbGadLVrZ7fy3QaZaO4sX6PBYWjr0XXTDVOFG1B%2BtHfjwGWzEcGl3HdA3wXEyBr6s8LcVJTNKd3WHPCL3eK3ALE5CHIT8J9KiClUjkGMGpXXK%2BIYXWRzCzwkZBV4ucdlT4PZpK0GZWz9COClOgp%2FRWgplReH0LmB9T0xtFzl%2FtKWGG1M6k4d4AtRDZ%2FI03Ustj3peXaMMOftGG0z7w0Psw14kR9Q2CZtqmdG7CjqD4XCDMMJiGps8GOqUBOvWseSNuIKbdLhWE23vKafWRildzQobbw8DyWhLcjlB3oeSlpflfU0cDoAQRqoWU%2BWMhIbMnafA%2Fz01hQnHwIhWjNjUk8EkY2xBVEhR2Gzzuk9sBa2JJMuLqW0Q2DL%2BdcSaPgW97h2ElUUxbFxaAFZ7SYxHOsQ0kxtDt9j29rQMAtq2BZ%2B42rQDmwxDTDP3OWE4yQQ3OBNqTx8H6kz7HgBEPgdXK&X-Amz-Signature=4a8b0c921bff7bde1c987f535529d24190dc5b40dbd109636347b41acdba9795&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOEKKSRH%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8yZM%2BkPhoyqxdYkRsWs%2F5VmTwCiZfu2%2Bv0fvNptYsPwIgDtASO5j6dslNj3g8B4GzICfW6bkIX0ssI3F33FWGu%2Bkq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDDt84MXSJbthX8IxYyrcA1bxYe0f7PM9tqZ5aR4wX0J%2BkpgEGEspB3xLE2Q7ffKE68O2GhpSGj0XoqUyt1%2FXaV0m3vmw0GyWL0SIWcdhYl7sUFa95YSqVOZmPy9vqnRpMlcZEyeZorJZe0sdFQIqob1E3Ms2ZLQ2gCv79KUYepw944aV644i0BaQyk8j8QFeidogAIeINhC%2FgTNeeYKQmkraclKED21SPzRl6vIXBKX3P%2Fe9mQn55hphmwpr9j4puhbgLanoyYB%2BiS4ZT6aReesDEIUYQmWW%2FnpGi%2FRUvhQeACaYjEc3cgZh4dHo5i%2FujZWMtDGvCnXODbe96qsZdpuJYow8AIIiQK8auKQ1DeF6EkEWcFkaAt%2FDVKNhSc5NdWtdqYOT8gBapc31%2Fn%2FUdjF%2BUC23f04q6dBbGadLVrZ7fy3QaZaO4sX6PBYWjr0XXTDVOFG1B%2BtHfjwGWzEcGl3HdA3wXEyBr6s8LcVJTNKd3WHPCL3eK3ALE5CHIT8J9KiClUjkGMGpXXK%2BIYXWRzCzwkZBV4ucdlT4PZpK0GZWz9COClOgp%2FRWgplReH0LmB9T0xtFzl%2FtKWGG1M6k4d4AtRDZ%2FI03Ustj3peXaMMOftGG0z7w0Psw14kR9Q2CZtqmdG7CjqD4XCDMMJiGps8GOqUBOvWseSNuIKbdLhWE23vKafWRildzQobbw8DyWhLcjlB3oeSlpflfU0cDoAQRqoWU%2BWMhIbMnafA%2Fz01hQnHwIhWjNjUk8EkY2xBVEhR2Gzzuk9sBa2JJMuLqW0Q2DL%2BdcSaPgW97h2ElUUxbFxaAFZ7SYxHOsQ0kxtDt9j29rQMAtq2BZ%2B42rQDmwxDTDP3OWE4yQQ3OBNqTx8H6kz7HgBEPgdXK&X-Amz-Signature=09dae72cead463509889ba7c0ef82847cb00f19144670bbb5fbe18f5509a5ed6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOEKKSRH%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8yZM%2BkPhoyqxdYkRsWs%2F5VmTwCiZfu2%2Bv0fvNptYsPwIgDtASO5j6dslNj3g8B4GzICfW6bkIX0ssI3F33FWGu%2Bkq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDDt84MXSJbthX8IxYyrcA1bxYe0f7PM9tqZ5aR4wX0J%2BkpgEGEspB3xLE2Q7ffKE68O2GhpSGj0XoqUyt1%2FXaV0m3vmw0GyWL0SIWcdhYl7sUFa95YSqVOZmPy9vqnRpMlcZEyeZorJZe0sdFQIqob1E3Ms2ZLQ2gCv79KUYepw944aV644i0BaQyk8j8QFeidogAIeINhC%2FgTNeeYKQmkraclKED21SPzRl6vIXBKX3P%2Fe9mQn55hphmwpr9j4puhbgLanoyYB%2BiS4ZT6aReesDEIUYQmWW%2FnpGi%2FRUvhQeACaYjEc3cgZh4dHo5i%2FujZWMtDGvCnXODbe96qsZdpuJYow8AIIiQK8auKQ1DeF6EkEWcFkaAt%2FDVKNhSc5NdWtdqYOT8gBapc31%2Fn%2FUdjF%2BUC23f04q6dBbGadLVrZ7fy3QaZaO4sX6PBYWjr0XXTDVOFG1B%2BtHfjwGWzEcGl3HdA3wXEyBr6s8LcVJTNKd3WHPCL3eK3ALE5CHIT8J9KiClUjkGMGpXXK%2BIYXWRzCzwkZBV4ucdlT4PZpK0GZWz9COClOgp%2FRWgplReH0LmB9T0xtFzl%2FtKWGG1M6k4d4AtRDZ%2FI03Ustj3peXaMMOftGG0z7w0Psw14kR9Q2CZtqmdG7CjqD4XCDMMJiGps8GOqUBOvWseSNuIKbdLhWE23vKafWRildzQobbw8DyWhLcjlB3oeSlpflfU0cDoAQRqoWU%2BWMhIbMnafA%2Fz01hQnHwIhWjNjUk8EkY2xBVEhR2Gzzuk9sBa2JJMuLqW0Q2DL%2BdcSaPgW97h2ElUUxbFxaAFZ7SYxHOsQ0kxtDt9j29rQMAtq2BZ%2B42rQDmwxDTDP3OWE4yQQ3OBNqTx8H6kz7HgBEPgdXK&X-Amz-Signature=53060f4b0c9028f47999d3f16a6564a810d5e93061853126aebd32ac6e5829e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOEKKSRH%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8yZM%2BkPhoyqxdYkRsWs%2F5VmTwCiZfu2%2Bv0fvNptYsPwIgDtASO5j6dslNj3g8B4GzICfW6bkIX0ssI3F33FWGu%2Bkq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDDt84MXSJbthX8IxYyrcA1bxYe0f7PM9tqZ5aR4wX0J%2BkpgEGEspB3xLE2Q7ffKE68O2GhpSGj0XoqUyt1%2FXaV0m3vmw0GyWL0SIWcdhYl7sUFa95YSqVOZmPy9vqnRpMlcZEyeZorJZe0sdFQIqob1E3Ms2ZLQ2gCv79KUYepw944aV644i0BaQyk8j8QFeidogAIeINhC%2FgTNeeYKQmkraclKED21SPzRl6vIXBKX3P%2Fe9mQn55hphmwpr9j4puhbgLanoyYB%2BiS4ZT6aReesDEIUYQmWW%2FnpGi%2FRUvhQeACaYjEc3cgZh4dHo5i%2FujZWMtDGvCnXODbe96qsZdpuJYow8AIIiQK8auKQ1DeF6EkEWcFkaAt%2FDVKNhSc5NdWtdqYOT8gBapc31%2Fn%2FUdjF%2BUC23f04q6dBbGadLVrZ7fy3QaZaO4sX6PBYWjr0XXTDVOFG1B%2BtHfjwGWzEcGl3HdA3wXEyBr6s8LcVJTNKd3WHPCL3eK3ALE5CHIT8J9KiClUjkGMGpXXK%2BIYXWRzCzwkZBV4ucdlT4PZpK0GZWz9COClOgp%2FRWgplReH0LmB9T0xtFzl%2FtKWGG1M6k4d4AtRDZ%2FI03Ustj3peXaMMOftGG0z7w0Psw14kR9Q2CZtqmdG7CjqD4XCDMMJiGps8GOqUBOvWseSNuIKbdLhWE23vKafWRildzQobbw8DyWhLcjlB3oeSlpflfU0cDoAQRqoWU%2BWMhIbMnafA%2Fz01hQnHwIhWjNjUk8EkY2xBVEhR2Gzzuk9sBa2JJMuLqW0Q2DL%2BdcSaPgW97h2ElUUxbFxaAFZ7SYxHOsQ0kxtDt9j29rQMAtq2BZ%2B42rQDmwxDTDP3OWE4yQQ3OBNqTx8H6kz7HgBEPgdXK&X-Amz-Signature=b2953fafc8bc93c0a62c67bcae5d24e9481c0c3ae54708d8c19d65b1ad4800be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOEKKSRH%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8yZM%2BkPhoyqxdYkRsWs%2F5VmTwCiZfu2%2Bv0fvNptYsPwIgDtASO5j6dslNj3g8B4GzICfW6bkIX0ssI3F33FWGu%2Bkq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDDt84MXSJbthX8IxYyrcA1bxYe0f7PM9tqZ5aR4wX0J%2BkpgEGEspB3xLE2Q7ffKE68O2GhpSGj0XoqUyt1%2FXaV0m3vmw0GyWL0SIWcdhYl7sUFa95YSqVOZmPy9vqnRpMlcZEyeZorJZe0sdFQIqob1E3Ms2ZLQ2gCv79KUYepw944aV644i0BaQyk8j8QFeidogAIeINhC%2FgTNeeYKQmkraclKED21SPzRl6vIXBKX3P%2Fe9mQn55hphmwpr9j4puhbgLanoyYB%2BiS4ZT6aReesDEIUYQmWW%2FnpGi%2FRUvhQeACaYjEc3cgZh4dHo5i%2FujZWMtDGvCnXODbe96qsZdpuJYow8AIIiQK8auKQ1DeF6EkEWcFkaAt%2FDVKNhSc5NdWtdqYOT8gBapc31%2Fn%2FUdjF%2BUC23f04q6dBbGadLVrZ7fy3QaZaO4sX6PBYWjr0XXTDVOFG1B%2BtHfjwGWzEcGl3HdA3wXEyBr6s8LcVJTNKd3WHPCL3eK3ALE5CHIT8J9KiClUjkGMGpXXK%2BIYXWRzCzwkZBV4ucdlT4PZpK0GZWz9COClOgp%2FRWgplReH0LmB9T0xtFzl%2FtKWGG1M6k4d4AtRDZ%2FI03Ustj3peXaMMOftGG0z7w0Psw14kR9Q2CZtqmdG7CjqD4XCDMMJiGps8GOqUBOvWseSNuIKbdLhWE23vKafWRildzQobbw8DyWhLcjlB3oeSlpflfU0cDoAQRqoWU%2BWMhIbMnafA%2Fz01hQnHwIhWjNjUk8EkY2xBVEhR2Gzzuk9sBa2JJMuLqW0Q2DL%2BdcSaPgW97h2ElUUxbFxaAFZ7SYxHOsQ0kxtDt9j29rQMAtq2BZ%2B42rQDmwxDTDP3OWE4yQQ3OBNqTx8H6kz7HgBEPgdXK&X-Amz-Signature=bcec9b69b30a309d9b7d59971f56115bebe4164ff0bc221e6663c25390ef805a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOEKKSRH%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8yZM%2BkPhoyqxdYkRsWs%2F5VmTwCiZfu2%2Bv0fvNptYsPwIgDtASO5j6dslNj3g8B4GzICfW6bkIX0ssI3F33FWGu%2Bkq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDDt84MXSJbthX8IxYyrcA1bxYe0f7PM9tqZ5aR4wX0J%2BkpgEGEspB3xLE2Q7ffKE68O2GhpSGj0XoqUyt1%2FXaV0m3vmw0GyWL0SIWcdhYl7sUFa95YSqVOZmPy9vqnRpMlcZEyeZorJZe0sdFQIqob1E3Ms2ZLQ2gCv79KUYepw944aV644i0BaQyk8j8QFeidogAIeINhC%2FgTNeeYKQmkraclKED21SPzRl6vIXBKX3P%2Fe9mQn55hphmwpr9j4puhbgLanoyYB%2BiS4ZT6aReesDEIUYQmWW%2FnpGi%2FRUvhQeACaYjEc3cgZh4dHo5i%2FujZWMtDGvCnXODbe96qsZdpuJYow8AIIiQK8auKQ1DeF6EkEWcFkaAt%2FDVKNhSc5NdWtdqYOT8gBapc31%2Fn%2FUdjF%2BUC23f04q6dBbGadLVrZ7fy3QaZaO4sX6PBYWjr0XXTDVOFG1B%2BtHfjwGWzEcGl3HdA3wXEyBr6s8LcVJTNKd3WHPCL3eK3ALE5CHIT8J9KiClUjkGMGpXXK%2BIYXWRzCzwkZBV4ucdlT4PZpK0GZWz9COClOgp%2FRWgplReH0LmB9T0xtFzl%2FtKWGG1M6k4d4AtRDZ%2FI03Ustj3peXaMMOftGG0z7w0Psw14kR9Q2CZtqmdG7CjqD4XCDMMJiGps8GOqUBOvWseSNuIKbdLhWE23vKafWRildzQobbw8DyWhLcjlB3oeSlpflfU0cDoAQRqoWU%2BWMhIbMnafA%2Fz01hQnHwIhWjNjUk8EkY2xBVEhR2Gzzuk9sBa2JJMuLqW0Q2DL%2BdcSaPgW97h2ElUUxbFxaAFZ7SYxHOsQ0kxtDt9j29rQMAtq2BZ%2B42rQDmwxDTDP3OWE4yQQ3OBNqTx8H6kz7HgBEPgdXK&X-Amz-Signature=d82f43dbbe959d4a239bd8f82c65c8ec76fa67e29a99dd30b76e25d2317f9442&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOEKKSRH%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8yZM%2BkPhoyqxdYkRsWs%2F5VmTwCiZfu2%2Bv0fvNptYsPwIgDtASO5j6dslNj3g8B4GzICfW6bkIX0ssI3F33FWGu%2Bkq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDDt84MXSJbthX8IxYyrcA1bxYe0f7PM9tqZ5aR4wX0J%2BkpgEGEspB3xLE2Q7ffKE68O2GhpSGj0XoqUyt1%2FXaV0m3vmw0GyWL0SIWcdhYl7sUFa95YSqVOZmPy9vqnRpMlcZEyeZorJZe0sdFQIqob1E3Ms2ZLQ2gCv79KUYepw944aV644i0BaQyk8j8QFeidogAIeINhC%2FgTNeeYKQmkraclKED21SPzRl6vIXBKX3P%2Fe9mQn55hphmwpr9j4puhbgLanoyYB%2BiS4ZT6aReesDEIUYQmWW%2FnpGi%2FRUvhQeACaYjEc3cgZh4dHo5i%2FujZWMtDGvCnXODbe96qsZdpuJYow8AIIiQK8auKQ1DeF6EkEWcFkaAt%2FDVKNhSc5NdWtdqYOT8gBapc31%2Fn%2FUdjF%2BUC23f04q6dBbGadLVrZ7fy3QaZaO4sX6PBYWjr0XXTDVOFG1B%2BtHfjwGWzEcGl3HdA3wXEyBr6s8LcVJTNKd3WHPCL3eK3ALE5CHIT8J9KiClUjkGMGpXXK%2BIYXWRzCzwkZBV4ucdlT4PZpK0GZWz9COClOgp%2FRWgplReH0LmB9T0xtFzl%2FtKWGG1M6k4d4AtRDZ%2FI03Ustj3peXaMMOftGG0z7w0Psw14kR9Q2CZtqmdG7CjqD4XCDMMJiGps8GOqUBOvWseSNuIKbdLhWE23vKafWRildzQobbw8DyWhLcjlB3oeSlpflfU0cDoAQRqoWU%2BWMhIbMnafA%2Fz01hQnHwIhWjNjUk8EkY2xBVEhR2Gzzuk9sBa2JJMuLqW0Q2DL%2BdcSaPgW97h2ElUUxbFxaAFZ7SYxHOsQ0kxtDt9j29rQMAtq2BZ%2B42rQDmwxDTDP3OWE4yQQ3OBNqTx8H6kz7HgBEPgdXK&X-Amz-Signature=7ef193f3ea93f0dc7a2c18bcec242053a8e68f7dac4af8e1f477ea1d74498816&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

