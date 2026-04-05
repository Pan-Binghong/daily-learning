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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQVYWJV4%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOstr3uRvZGHnXQyo93N4%2BWZxIJLJyQinJFrXa4GuHuQIgdK5rfIJ5Kp8q8V8AzIXqTvv7FnWgo7BVKt49xltXQssqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHq575%2FUq8XTGRvLYCrcA2gXO7jpc5OEoWpkVVm7sVK2xHAkNOiKz4fCGq63tjmSqXVxJ6DjhXxw0er3fH97qNdYdxAmZ2Ekweuq2F16TKAjPWAsoF%2FdEpTfUKWDlyWBFzNG3x1dbmktZW3jBEz9hWoT4q2y8XFPfG1bcb5Mt60sONORiWovY%2BNgb35yI7Dk3Y8NWc1Das1%2FEooyOFp2JHIbO7wjfx8OQ%2BZOf3ikuq6aOzfPU9zqYMqqOPxdV%2FbzKsg5xYUdYfINx167rEkRX7ESuYq%2BhgwHbCl%2BogyGq0yq77%2FH01%2FeDnAF%2F2XnlTXJ8dbT0vJOSOEJauEXDpQSVrl%2BYyoorkiUlMKIl43BBadyT6lBpYHDAfxZEL6d%2BuKnP4YRlhwJcYEUsBxfU%2B4P%2Fu4%2B3EIvez0%2BlC2ZNre%2FMaPM%2Fdsv2SrhbRy5zwmhsHqfrbQjq%2FjNMDY5mxgyNRCOUTywIeTcLSq0JbPgnR7Nq1fE5dmUxyfuv9CCnEcgiGS1d%2BRnT6KiQsKAHnPiqbjCVp6GAgNIbEtEaaf%2F%2F5th8lIGo3L0FGAOuHTZBKR3G3YpQq2P%2FrdTt5rVe0zYT6fLB%2BmnPw2dXlHlevtOdaRH2e7noxvoZVhLuTubFBaPWBzwRAdhCO40tRVLInZbMLuex84GOqUBwvniKEsN7D7xPe%2FIyH35e10B%2FzFcnxdDk0WfWUmAvSEcCk5dmwoolS0ZBaSwZKi1egXFmIyNyecIDMvkMpa9y11kYcGHeq3vH7yp1J3R6ysbYp3UQPJlNqXdpw2dda32%2BQg%2FW5NEDZfGHqFElriP03bYrCq38wBbSEHSC4RY6vdjobaVHORooMWjASjaZ29MVTC53jI9HV%2Fib4d94jOsXYGo4z%2FI&X-Amz-Signature=d6d162938f0e688b65a8dfab0171b6ed87b6e773d7af37d722441170e8bd5250&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQVYWJV4%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOstr3uRvZGHnXQyo93N4%2BWZxIJLJyQinJFrXa4GuHuQIgdK5rfIJ5Kp8q8V8AzIXqTvv7FnWgo7BVKt49xltXQssqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHq575%2FUq8XTGRvLYCrcA2gXO7jpc5OEoWpkVVm7sVK2xHAkNOiKz4fCGq63tjmSqXVxJ6DjhXxw0er3fH97qNdYdxAmZ2Ekweuq2F16TKAjPWAsoF%2FdEpTfUKWDlyWBFzNG3x1dbmktZW3jBEz9hWoT4q2y8XFPfG1bcb5Mt60sONORiWovY%2BNgb35yI7Dk3Y8NWc1Das1%2FEooyOFp2JHIbO7wjfx8OQ%2BZOf3ikuq6aOzfPU9zqYMqqOPxdV%2FbzKsg5xYUdYfINx167rEkRX7ESuYq%2BhgwHbCl%2BogyGq0yq77%2FH01%2FeDnAF%2F2XnlTXJ8dbT0vJOSOEJauEXDpQSVrl%2BYyoorkiUlMKIl43BBadyT6lBpYHDAfxZEL6d%2BuKnP4YRlhwJcYEUsBxfU%2B4P%2Fu4%2B3EIvez0%2BlC2ZNre%2FMaPM%2Fdsv2SrhbRy5zwmhsHqfrbQjq%2FjNMDY5mxgyNRCOUTywIeTcLSq0JbPgnR7Nq1fE5dmUxyfuv9CCnEcgiGS1d%2BRnT6KiQsKAHnPiqbjCVp6GAgNIbEtEaaf%2F%2F5th8lIGo3L0FGAOuHTZBKR3G3YpQq2P%2FrdTt5rVe0zYT6fLB%2BmnPw2dXlHlevtOdaRH2e7noxvoZVhLuTubFBaPWBzwRAdhCO40tRVLInZbMLuex84GOqUBwvniKEsN7D7xPe%2FIyH35e10B%2FzFcnxdDk0WfWUmAvSEcCk5dmwoolS0ZBaSwZKi1egXFmIyNyecIDMvkMpa9y11kYcGHeq3vH7yp1J3R6ysbYp3UQPJlNqXdpw2dda32%2BQg%2FW5NEDZfGHqFElriP03bYrCq38wBbSEHSC4RY6vdjobaVHORooMWjASjaZ29MVTC53jI9HV%2Fib4d94jOsXYGo4z%2FI&X-Amz-Signature=cf8ad3414c438d29371c5085882ae74aec3bcfe6debb6f12c2a2f75f69d6d07b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQVYWJV4%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOstr3uRvZGHnXQyo93N4%2BWZxIJLJyQinJFrXa4GuHuQIgdK5rfIJ5Kp8q8V8AzIXqTvv7FnWgo7BVKt49xltXQssqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHq575%2FUq8XTGRvLYCrcA2gXO7jpc5OEoWpkVVm7sVK2xHAkNOiKz4fCGq63tjmSqXVxJ6DjhXxw0er3fH97qNdYdxAmZ2Ekweuq2F16TKAjPWAsoF%2FdEpTfUKWDlyWBFzNG3x1dbmktZW3jBEz9hWoT4q2y8XFPfG1bcb5Mt60sONORiWovY%2BNgb35yI7Dk3Y8NWc1Das1%2FEooyOFp2JHIbO7wjfx8OQ%2BZOf3ikuq6aOzfPU9zqYMqqOPxdV%2FbzKsg5xYUdYfINx167rEkRX7ESuYq%2BhgwHbCl%2BogyGq0yq77%2FH01%2FeDnAF%2F2XnlTXJ8dbT0vJOSOEJauEXDpQSVrl%2BYyoorkiUlMKIl43BBadyT6lBpYHDAfxZEL6d%2BuKnP4YRlhwJcYEUsBxfU%2B4P%2Fu4%2B3EIvez0%2BlC2ZNre%2FMaPM%2Fdsv2SrhbRy5zwmhsHqfrbQjq%2FjNMDY5mxgyNRCOUTywIeTcLSq0JbPgnR7Nq1fE5dmUxyfuv9CCnEcgiGS1d%2BRnT6KiQsKAHnPiqbjCVp6GAgNIbEtEaaf%2F%2F5th8lIGo3L0FGAOuHTZBKR3G3YpQq2P%2FrdTt5rVe0zYT6fLB%2BmnPw2dXlHlevtOdaRH2e7noxvoZVhLuTubFBaPWBzwRAdhCO40tRVLInZbMLuex84GOqUBwvniKEsN7D7xPe%2FIyH35e10B%2FzFcnxdDk0WfWUmAvSEcCk5dmwoolS0ZBaSwZKi1egXFmIyNyecIDMvkMpa9y11kYcGHeq3vH7yp1J3R6ysbYp3UQPJlNqXdpw2dda32%2BQg%2FW5NEDZfGHqFElriP03bYrCq38wBbSEHSC4RY6vdjobaVHORooMWjASjaZ29MVTC53jI9HV%2Fib4d94jOsXYGo4z%2FI&X-Amz-Signature=38d34b3dbbaf3fd3761903fc5f021112e842024c0e6b38f335a99c72e57be877&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQVYWJV4%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOstr3uRvZGHnXQyo93N4%2BWZxIJLJyQinJFrXa4GuHuQIgdK5rfIJ5Kp8q8V8AzIXqTvv7FnWgo7BVKt49xltXQssqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHq575%2FUq8XTGRvLYCrcA2gXO7jpc5OEoWpkVVm7sVK2xHAkNOiKz4fCGq63tjmSqXVxJ6DjhXxw0er3fH97qNdYdxAmZ2Ekweuq2F16TKAjPWAsoF%2FdEpTfUKWDlyWBFzNG3x1dbmktZW3jBEz9hWoT4q2y8XFPfG1bcb5Mt60sONORiWovY%2BNgb35yI7Dk3Y8NWc1Das1%2FEooyOFp2JHIbO7wjfx8OQ%2BZOf3ikuq6aOzfPU9zqYMqqOPxdV%2FbzKsg5xYUdYfINx167rEkRX7ESuYq%2BhgwHbCl%2BogyGq0yq77%2FH01%2FeDnAF%2F2XnlTXJ8dbT0vJOSOEJauEXDpQSVrl%2BYyoorkiUlMKIl43BBadyT6lBpYHDAfxZEL6d%2BuKnP4YRlhwJcYEUsBxfU%2B4P%2Fu4%2B3EIvez0%2BlC2ZNre%2FMaPM%2Fdsv2SrhbRy5zwmhsHqfrbQjq%2FjNMDY5mxgyNRCOUTywIeTcLSq0JbPgnR7Nq1fE5dmUxyfuv9CCnEcgiGS1d%2BRnT6KiQsKAHnPiqbjCVp6GAgNIbEtEaaf%2F%2F5th8lIGo3L0FGAOuHTZBKR3G3YpQq2P%2FrdTt5rVe0zYT6fLB%2BmnPw2dXlHlevtOdaRH2e7noxvoZVhLuTubFBaPWBzwRAdhCO40tRVLInZbMLuex84GOqUBwvniKEsN7D7xPe%2FIyH35e10B%2FzFcnxdDk0WfWUmAvSEcCk5dmwoolS0ZBaSwZKi1egXFmIyNyecIDMvkMpa9y11kYcGHeq3vH7yp1J3R6ysbYp3UQPJlNqXdpw2dda32%2BQg%2FW5NEDZfGHqFElriP03bYrCq38wBbSEHSC4RY6vdjobaVHORooMWjASjaZ29MVTC53jI9HV%2Fib4d94jOsXYGo4z%2FI&X-Amz-Signature=a82b222b8a45ae7d3ddb9ab313988bc135df1488980e91f2e2cf52c0f5b0067d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQVYWJV4%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOstr3uRvZGHnXQyo93N4%2BWZxIJLJyQinJFrXa4GuHuQIgdK5rfIJ5Kp8q8V8AzIXqTvv7FnWgo7BVKt49xltXQssqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHq575%2FUq8XTGRvLYCrcA2gXO7jpc5OEoWpkVVm7sVK2xHAkNOiKz4fCGq63tjmSqXVxJ6DjhXxw0er3fH97qNdYdxAmZ2Ekweuq2F16TKAjPWAsoF%2FdEpTfUKWDlyWBFzNG3x1dbmktZW3jBEz9hWoT4q2y8XFPfG1bcb5Mt60sONORiWovY%2BNgb35yI7Dk3Y8NWc1Das1%2FEooyOFp2JHIbO7wjfx8OQ%2BZOf3ikuq6aOzfPU9zqYMqqOPxdV%2FbzKsg5xYUdYfINx167rEkRX7ESuYq%2BhgwHbCl%2BogyGq0yq77%2FH01%2FeDnAF%2F2XnlTXJ8dbT0vJOSOEJauEXDpQSVrl%2BYyoorkiUlMKIl43BBadyT6lBpYHDAfxZEL6d%2BuKnP4YRlhwJcYEUsBxfU%2B4P%2Fu4%2B3EIvez0%2BlC2ZNre%2FMaPM%2Fdsv2SrhbRy5zwmhsHqfrbQjq%2FjNMDY5mxgyNRCOUTywIeTcLSq0JbPgnR7Nq1fE5dmUxyfuv9CCnEcgiGS1d%2BRnT6KiQsKAHnPiqbjCVp6GAgNIbEtEaaf%2F%2F5th8lIGo3L0FGAOuHTZBKR3G3YpQq2P%2FrdTt5rVe0zYT6fLB%2BmnPw2dXlHlevtOdaRH2e7noxvoZVhLuTubFBaPWBzwRAdhCO40tRVLInZbMLuex84GOqUBwvniKEsN7D7xPe%2FIyH35e10B%2FzFcnxdDk0WfWUmAvSEcCk5dmwoolS0ZBaSwZKi1egXFmIyNyecIDMvkMpa9y11kYcGHeq3vH7yp1J3R6ysbYp3UQPJlNqXdpw2dda32%2BQg%2FW5NEDZfGHqFElriP03bYrCq38wBbSEHSC4RY6vdjobaVHORooMWjASjaZ29MVTC53jI9HV%2Fib4d94jOsXYGo4z%2FI&X-Amz-Signature=01955d4c8f487c57a764477b8b0c51682778ef8ee2bb1ca4326434c708449381&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQVYWJV4%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOstr3uRvZGHnXQyo93N4%2BWZxIJLJyQinJFrXa4GuHuQIgdK5rfIJ5Kp8q8V8AzIXqTvv7FnWgo7BVKt49xltXQssqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHq575%2FUq8XTGRvLYCrcA2gXO7jpc5OEoWpkVVm7sVK2xHAkNOiKz4fCGq63tjmSqXVxJ6DjhXxw0er3fH97qNdYdxAmZ2Ekweuq2F16TKAjPWAsoF%2FdEpTfUKWDlyWBFzNG3x1dbmktZW3jBEz9hWoT4q2y8XFPfG1bcb5Mt60sONORiWovY%2BNgb35yI7Dk3Y8NWc1Das1%2FEooyOFp2JHIbO7wjfx8OQ%2BZOf3ikuq6aOzfPU9zqYMqqOPxdV%2FbzKsg5xYUdYfINx167rEkRX7ESuYq%2BhgwHbCl%2BogyGq0yq77%2FH01%2FeDnAF%2F2XnlTXJ8dbT0vJOSOEJauEXDpQSVrl%2BYyoorkiUlMKIl43BBadyT6lBpYHDAfxZEL6d%2BuKnP4YRlhwJcYEUsBxfU%2B4P%2Fu4%2B3EIvez0%2BlC2ZNre%2FMaPM%2Fdsv2SrhbRy5zwmhsHqfrbQjq%2FjNMDY5mxgyNRCOUTywIeTcLSq0JbPgnR7Nq1fE5dmUxyfuv9CCnEcgiGS1d%2BRnT6KiQsKAHnPiqbjCVp6GAgNIbEtEaaf%2F%2F5th8lIGo3L0FGAOuHTZBKR3G3YpQq2P%2FrdTt5rVe0zYT6fLB%2BmnPw2dXlHlevtOdaRH2e7noxvoZVhLuTubFBaPWBzwRAdhCO40tRVLInZbMLuex84GOqUBwvniKEsN7D7xPe%2FIyH35e10B%2FzFcnxdDk0WfWUmAvSEcCk5dmwoolS0ZBaSwZKi1egXFmIyNyecIDMvkMpa9y11kYcGHeq3vH7yp1J3R6ysbYp3UQPJlNqXdpw2dda32%2BQg%2FW5NEDZfGHqFElriP03bYrCq38wBbSEHSC4RY6vdjobaVHORooMWjASjaZ29MVTC53jI9HV%2Fib4d94jOsXYGo4z%2FI&X-Amz-Signature=6b8554745229ea69da6c5d158572392ef4cacc3fa22ae59bada293615f5f5e26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQVYWJV4%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOstr3uRvZGHnXQyo93N4%2BWZxIJLJyQinJFrXa4GuHuQIgdK5rfIJ5Kp8q8V8AzIXqTvv7FnWgo7BVKt49xltXQssqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHq575%2FUq8XTGRvLYCrcA2gXO7jpc5OEoWpkVVm7sVK2xHAkNOiKz4fCGq63tjmSqXVxJ6DjhXxw0er3fH97qNdYdxAmZ2Ekweuq2F16TKAjPWAsoF%2FdEpTfUKWDlyWBFzNG3x1dbmktZW3jBEz9hWoT4q2y8XFPfG1bcb5Mt60sONORiWovY%2BNgb35yI7Dk3Y8NWc1Das1%2FEooyOFp2JHIbO7wjfx8OQ%2BZOf3ikuq6aOzfPU9zqYMqqOPxdV%2FbzKsg5xYUdYfINx167rEkRX7ESuYq%2BhgwHbCl%2BogyGq0yq77%2FH01%2FeDnAF%2F2XnlTXJ8dbT0vJOSOEJauEXDpQSVrl%2BYyoorkiUlMKIl43BBadyT6lBpYHDAfxZEL6d%2BuKnP4YRlhwJcYEUsBxfU%2B4P%2Fu4%2B3EIvez0%2BlC2ZNre%2FMaPM%2Fdsv2SrhbRy5zwmhsHqfrbQjq%2FjNMDY5mxgyNRCOUTywIeTcLSq0JbPgnR7Nq1fE5dmUxyfuv9CCnEcgiGS1d%2BRnT6KiQsKAHnPiqbjCVp6GAgNIbEtEaaf%2F%2F5th8lIGo3L0FGAOuHTZBKR3G3YpQq2P%2FrdTt5rVe0zYT6fLB%2BmnPw2dXlHlevtOdaRH2e7noxvoZVhLuTubFBaPWBzwRAdhCO40tRVLInZbMLuex84GOqUBwvniKEsN7D7xPe%2FIyH35e10B%2FzFcnxdDk0WfWUmAvSEcCk5dmwoolS0ZBaSwZKi1egXFmIyNyecIDMvkMpa9y11kYcGHeq3vH7yp1J3R6ysbYp3UQPJlNqXdpw2dda32%2BQg%2FW5NEDZfGHqFElriP03bYrCq38wBbSEHSC4RY6vdjobaVHORooMWjASjaZ29MVTC53jI9HV%2Fib4d94jOsXYGo4z%2FI&X-Amz-Signature=90a36d48354ed78fa81c9467f8a37ee0fcce4272c5a3997f47008f41b6fbc861&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

