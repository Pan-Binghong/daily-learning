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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJ43L24L%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgV6cmNVXhOq03J8YtMw8FKdqDgck3VsQkspvPTsqAYQIgAkoGF0OYjJ2QLHYd3Dq%2BcPMiZeiOsD32kciAnkcXrasqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJA1vfqmK8h8rwAZmSrcAzalTF9wRusYXjbaqYbX%2FJeMWk6mrQoIQWwvC0iwATQzzmldSRTSTAWGbONlfarPcv33ISJDoHQxp6yaeLAQeUrxa0d8tv6Gxvd5Ccg3xJwuTuSgvLieS8IR0Q7hIA4bfsYRA%2FiIFUt97M5prG1gdTwAgZRLxLy5lZ4jS4OVQawLKQOGxicMVXwjLusjGEqqQFWrTV7bYEC4vAACs6eGjD8O0woNmSLg%2FRPLOPj4UCu0O%2BEClVtj6e%2B2pJJ8LoNYl38jpHpE4t7RkUSnRfEs5bfK0%2BWboIhNzt1EGBwySQibGhTtqhu%2F2ci5j05fiiytWto%2FsMtIMoppdx9BrqRtjZNSydbXXisrUw7PayE8D2qLVW7yz9kP9Mjzre%2Bk4IekXLMT5HzvDkUBn7gTERfxHz39CtjMCehHSd8v1hz3kwa4E0KKEzCRXCNlonig%2FtTsvnWU09ZhIN8WmnPE%2BYbstaNV86sQ1EqOpSLuLYaQpc6ifSBxSpCpeL1UyjjQ9MHYm%2FtkLPoyDFZzYLmM6JNEUwaBNgr9Qmq0lClzZ17YI0q3trJcQXXNllJKDWF90pB2%2BrpxXENCda9Y84ykXQJNBKyCEiIgClpGSf%2F5ckQzW9hlyqLwCkQbxnQS0CwPMIyU%2FM4GOqUBD503M%2BvYR27oxcb6y0iyA7S3JVP0AVZmQGT9iY%2BVifQcUpe16KnHjSOeLIDyijft%2Fe8bzw8T1%2FV34vkqYJFomEXY8q0J0ne9Xe%2B%2Fkgq%2FlG3xsPIaROID6mPJIvgZQnWNWS4kgZp4Qx%2FT4hn1iWscCFOsoZyn8IJMqOwKcaU0HrPVaKvl%2FtmJzoR6VDKxGMxbxQ7PZCRw0Vv8ZONzlrc4cM2x1jig&X-Amz-Signature=ab304a154a1828ba9eea7a0bfb9177cdee68a30ad63b72e4bd2f16f938cca2ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJ43L24L%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgV6cmNVXhOq03J8YtMw8FKdqDgck3VsQkspvPTsqAYQIgAkoGF0OYjJ2QLHYd3Dq%2BcPMiZeiOsD32kciAnkcXrasqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJA1vfqmK8h8rwAZmSrcAzalTF9wRusYXjbaqYbX%2FJeMWk6mrQoIQWwvC0iwATQzzmldSRTSTAWGbONlfarPcv33ISJDoHQxp6yaeLAQeUrxa0d8tv6Gxvd5Ccg3xJwuTuSgvLieS8IR0Q7hIA4bfsYRA%2FiIFUt97M5prG1gdTwAgZRLxLy5lZ4jS4OVQawLKQOGxicMVXwjLusjGEqqQFWrTV7bYEC4vAACs6eGjD8O0woNmSLg%2FRPLOPj4UCu0O%2BEClVtj6e%2B2pJJ8LoNYl38jpHpE4t7RkUSnRfEs5bfK0%2BWboIhNzt1EGBwySQibGhTtqhu%2F2ci5j05fiiytWto%2FsMtIMoppdx9BrqRtjZNSydbXXisrUw7PayE8D2qLVW7yz9kP9Mjzre%2Bk4IekXLMT5HzvDkUBn7gTERfxHz39CtjMCehHSd8v1hz3kwa4E0KKEzCRXCNlonig%2FtTsvnWU09ZhIN8WmnPE%2BYbstaNV86sQ1EqOpSLuLYaQpc6ifSBxSpCpeL1UyjjQ9MHYm%2FtkLPoyDFZzYLmM6JNEUwaBNgr9Qmq0lClzZ17YI0q3trJcQXXNllJKDWF90pB2%2BrpxXENCda9Y84ykXQJNBKyCEiIgClpGSf%2F5ckQzW9hlyqLwCkQbxnQS0CwPMIyU%2FM4GOqUBD503M%2BvYR27oxcb6y0iyA7S3JVP0AVZmQGT9iY%2BVifQcUpe16KnHjSOeLIDyijft%2Fe8bzw8T1%2FV34vkqYJFomEXY8q0J0ne9Xe%2B%2Fkgq%2FlG3xsPIaROID6mPJIvgZQnWNWS4kgZp4Qx%2FT4hn1iWscCFOsoZyn8IJMqOwKcaU0HrPVaKvl%2FtmJzoR6VDKxGMxbxQ7PZCRw0Vv8ZONzlrc4cM2x1jig&X-Amz-Signature=ae91ca5e9530a91398b8eeea7f91886a64e0b62afc1774d928755f72652632bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJ43L24L%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgV6cmNVXhOq03J8YtMw8FKdqDgck3VsQkspvPTsqAYQIgAkoGF0OYjJ2QLHYd3Dq%2BcPMiZeiOsD32kciAnkcXrasqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJA1vfqmK8h8rwAZmSrcAzalTF9wRusYXjbaqYbX%2FJeMWk6mrQoIQWwvC0iwATQzzmldSRTSTAWGbONlfarPcv33ISJDoHQxp6yaeLAQeUrxa0d8tv6Gxvd5Ccg3xJwuTuSgvLieS8IR0Q7hIA4bfsYRA%2FiIFUt97M5prG1gdTwAgZRLxLy5lZ4jS4OVQawLKQOGxicMVXwjLusjGEqqQFWrTV7bYEC4vAACs6eGjD8O0woNmSLg%2FRPLOPj4UCu0O%2BEClVtj6e%2B2pJJ8LoNYl38jpHpE4t7RkUSnRfEs5bfK0%2BWboIhNzt1EGBwySQibGhTtqhu%2F2ci5j05fiiytWto%2FsMtIMoppdx9BrqRtjZNSydbXXisrUw7PayE8D2qLVW7yz9kP9Mjzre%2Bk4IekXLMT5HzvDkUBn7gTERfxHz39CtjMCehHSd8v1hz3kwa4E0KKEzCRXCNlonig%2FtTsvnWU09ZhIN8WmnPE%2BYbstaNV86sQ1EqOpSLuLYaQpc6ifSBxSpCpeL1UyjjQ9MHYm%2FtkLPoyDFZzYLmM6JNEUwaBNgr9Qmq0lClzZ17YI0q3trJcQXXNllJKDWF90pB2%2BrpxXENCda9Y84ykXQJNBKyCEiIgClpGSf%2F5ckQzW9hlyqLwCkQbxnQS0CwPMIyU%2FM4GOqUBD503M%2BvYR27oxcb6y0iyA7S3JVP0AVZmQGT9iY%2BVifQcUpe16KnHjSOeLIDyijft%2Fe8bzw8T1%2FV34vkqYJFomEXY8q0J0ne9Xe%2B%2Fkgq%2FlG3xsPIaROID6mPJIvgZQnWNWS4kgZp4Qx%2FT4hn1iWscCFOsoZyn8IJMqOwKcaU0HrPVaKvl%2FtmJzoR6VDKxGMxbxQ7PZCRw0Vv8ZONzlrc4cM2x1jig&X-Amz-Signature=064771a6fba052b5164044c9a00130fb11632de05cca9f6f05af795c21b9d53f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJ43L24L%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgV6cmNVXhOq03J8YtMw8FKdqDgck3VsQkspvPTsqAYQIgAkoGF0OYjJ2QLHYd3Dq%2BcPMiZeiOsD32kciAnkcXrasqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJA1vfqmK8h8rwAZmSrcAzalTF9wRusYXjbaqYbX%2FJeMWk6mrQoIQWwvC0iwATQzzmldSRTSTAWGbONlfarPcv33ISJDoHQxp6yaeLAQeUrxa0d8tv6Gxvd5Ccg3xJwuTuSgvLieS8IR0Q7hIA4bfsYRA%2FiIFUt97M5prG1gdTwAgZRLxLy5lZ4jS4OVQawLKQOGxicMVXwjLusjGEqqQFWrTV7bYEC4vAACs6eGjD8O0woNmSLg%2FRPLOPj4UCu0O%2BEClVtj6e%2B2pJJ8LoNYl38jpHpE4t7RkUSnRfEs5bfK0%2BWboIhNzt1EGBwySQibGhTtqhu%2F2ci5j05fiiytWto%2FsMtIMoppdx9BrqRtjZNSydbXXisrUw7PayE8D2qLVW7yz9kP9Mjzre%2Bk4IekXLMT5HzvDkUBn7gTERfxHz39CtjMCehHSd8v1hz3kwa4E0KKEzCRXCNlonig%2FtTsvnWU09ZhIN8WmnPE%2BYbstaNV86sQ1EqOpSLuLYaQpc6ifSBxSpCpeL1UyjjQ9MHYm%2FtkLPoyDFZzYLmM6JNEUwaBNgr9Qmq0lClzZ17YI0q3trJcQXXNllJKDWF90pB2%2BrpxXENCda9Y84ykXQJNBKyCEiIgClpGSf%2F5ckQzW9hlyqLwCkQbxnQS0CwPMIyU%2FM4GOqUBD503M%2BvYR27oxcb6y0iyA7S3JVP0AVZmQGT9iY%2BVifQcUpe16KnHjSOeLIDyijft%2Fe8bzw8T1%2FV34vkqYJFomEXY8q0J0ne9Xe%2B%2Fkgq%2FlG3xsPIaROID6mPJIvgZQnWNWS4kgZp4Qx%2FT4hn1iWscCFOsoZyn8IJMqOwKcaU0HrPVaKvl%2FtmJzoR6VDKxGMxbxQ7PZCRw0Vv8ZONzlrc4cM2x1jig&X-Amz-Signature=4dd1cb6270c5e8ab41a9e52d2cc0ce840327354539c46edf3b72c7f86428c533&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJ43L24L%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgV6cmNVXhOq03J8YtMw8FKdqDgck3VsQkspvPTsqAYQIgAkoGF0OYjJ2QLHYd3Dq%2BcPMiZeiOsD32kciAnkcXrasqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJA1vfqmK8h8rwAZmSrcAzalTF9wRusYXjbaqYbX%2FJeMWk6mrQoIQWwvC0iwATQzzmldSRTSTAWGbONlfarPcv33ISJDoHQxp6yaeLAQeUrxa0d8tv6Gxvd5Ccg3xJwuTuSgvLieS8IR0Q7hIA4bfsYRA%2FiIFUt97M5prG1gdTwAgZRLxLy5lZ4jS4OVQawLKQOGxicMVXwjLusjGEqqQFWrTV7bYEC4vAACs6eGjD8O0woNmSLg%2FRPLOPj4UCu0O%2BEClVtj6e%2B2pJJ8LoNYl38jpHpE4t7RkUSnRfEs5bfK0%2BWboIhNzt1EGBwySQibGhTtqhu%2F2ci5j05fiiytWto%2FsMtIMoppdx9BrqRtjZNSydbXXisrUw7PayE8D2qLVW7yz9kP9Mjzre%2Bk4IekXLMT5HzvDkUBn7gTERfxHz39CtjMCehHSd8v1hz3kwa4E0KKEzCRXCNlonig%2FtTsvnWU09ZhIN8WmnPE%2BYbstaNV86sQ1EqOpSLuLYaQpc6ifSBxSpCpeL1UyjjQ9MHYm%2FtkLPoyDFZzYLmM6JNEUwaBNgr9Qmq0lClzZ17YI0q3trJcQXXNllJKDWF90pB2%2BrpxXENCda9Y84ykXQJNBKyCEiIgClpGSf%2F5ckQzW9hlyqLwCkQbxnQS0CwPMIyU%2FM4GOqUBD503M%2BvYR27oxcb6y0iyA7S3JVP0AVZmQGT9iY%2BVifQcUpe16KnHjSOeLIDyijft%2Fe8bzw8T1%2FV34vkqYJFomEXY8q0J0ne9Xe%2B%2Fkgq%2FlG3xsPIaROID6mPJIvgZQnWNWS4kgZp4Qx%2FT4hn1iWscCFOsoZyn8IJMqOwKcaU0HrPVaKvl%2FtmJzoR6VDKxGMxbxQ7PZCRw0Vv8ZONzlrc4cM2x1jig&X-Amz-Signature=3de5121ce3aece2f768573939a90940a6b36e69d40d88c58864b8f842e4c4377&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJ43L24L%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgV6cmNVXhOq03J8YtMw8FKdqDgck3VsQkspvPTsqAYQIgAkoGF0OYjJ2QLHYd3Dq%2BcPMiZeiOsD32kciAnkcXrasqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJA1vfqmK8h8rwAZmSrcAzalTF9wRusYXjbaqYbX%2FJeMWk6mrQoIQWwvC0iwATQzzmldSRTSTAWGbONlfarPcv33ISJDoHQxp6yaeLAQeUrxa0d8tv6Gxvd5Ccg3xJwuTuSgvLieS8IR0Q7hIA4bfsYRA%2FiIFUt97M5prG1gdTwAgZRLxLy5lZ4jS4OVQawLKQOGxicMVXwjLusjGEqqQFWrTV7bYEC4vAACs6eGjD8O0woNmSLg%2FRPLOPj4UCu0O%2BEClVtj6e%2B2pJJ8LoNYl38jpHpE4t7RkUSnRfEs5bfK0%2BWboIhNzt1EGBwySQibGhTtqhu%2F2ci5j05fiiytWto%2FsMtIMoppdx9BrqRtjZNSydbXXisrUw7PayE8D2qLVW7yz9kP9Mjzre%2Bk4IekXLMT5HzvDkUBn7gTERfxHz39CtjMCehHSd8v1hz3kwa4E0KKEzCRXCNlonig%2FtTsvnWU09ZhIN8WmnPE%2BYbstaNV86sQ1EqOpSLuLYaQpc6ifSBxSpCpeL1UyjjQ9MHYm%2FtkLPoyDFZzYLmM6JNEUwaBNgr9Qmq0lClzZ17YI0q3trJcQXXNllJKDWF90pB2%2BrpxXENCda9Y84ykXQJNBKyCEiIgClpGSf%2F5ckQzW9hlyqLwCkQbxnQS0CwPMIyU%2FM4GOqUBD503M%2BvYR27oxcb6y0iyA7S3JVP0AVZmQGT9iY%2BVifQcUpe16KnHjSOeLIDyijft%2Fe8bzw8T1%2FV34vkqYJFomEXY8q0J0ne9Xe%2B%2Fkgq%2FlG3xsPIaROID6mPJIvgZQnWNWS4kgZp4Qx%2FT4hn1iWscCFOsoZyn8IJMqOwKcaU0HrPVaKvl%2FtmJzoR6VDKxGMxbxQ7PZCRw0Vv8ZONzlrc4cM2x1jig&X-Amz-Signature=69ee03e2f37e2cbd43def491bc7273b9f2c5218a44117030ea364e32a256156c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJ43L24L%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgV6cmNVXhOq03J8YtMw8FKdqDgck3VsQkspvPTsqAYQIgAkoGF0OYjJ2QLHYd3Dq%2BcPMiZeiOsD32kciAnkcXrasqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJA1vfqmK8h8rwAZmSrcAzalTF9wRusYXjbaqYbX%2FJeMWk6mrQoIQWwvC0iwATQzzmldSRTSTAWGbONlfarPcv33ISJDoHQxp6yaeLAQeUrxa0d8tv6Gxvd5Ccg3xJwuTuSgvLieS8IR0Q7hIA4bfsYRA%2FiIFUt97M5prG1gdTwAgZRLxLy5lZ4jS4OVQawLKQOGxicMVXwjLusjGEqqQFWrTV7bYEC4vAACs6eGjD8O0woNmSLg%2FRPLOPj4UCu0O%2BEClVtj6e%2B2pJJ8LoNYl38jpHpE4t7RkUSnRfEs5bfK0%2BWboIhNzt1EGBwySQibGhTtqhu%2F2ci5j05fiiytWto%2FsMtIMoppdx9BrqRtjZNSydbXXisrUw7PayE8D2qLVW7yz9kP9Mjzre%2Bk4IekXLMT5HzvDkUBn7gTERfxHz39CtjMCehHSd8v1hz3kwa4E0KKEzCRXCNlonig%2FtTsvnWU09ZhIN8WmnPE%2BYbstaNV86sQ1EqOpSLuLYaQpc6ifSBxSpCpeL1UyjjQ9MHYm%2FtkLPoyDFZzYLmM6JNEUwaBNgr9Qmq0lClzZ17YI0q3trJcQXXNllJKDWF90pB2%2BrpxXENCda9Y84ykXQJNBKyCEiIgClpGSf%2F5ckQzW9hlyqLwCkQbxnQS0CwPMIyU%2FM4GOqUBD503M%2BvYR27oxcb6y0iyA7S3JVP0AVZmQGT9iY%2BVifQcUpe16KnHjSOeLIDyijft%2Fe8bzw8T1%2FV34vkqYJFomEXY8q0J0ne9Xe%2B%2Fkgq%2FlG3xsPIaROID6mPJIvgZQnWNWS4kgZp4Qx%2FT4hn1iWscCFOsoZyn8IJMqOwKcaU0HrPVaKvl%2FtmJzoR6VDKxGMxbxQ7PZCRw0Vv8ZONzlrc4cM2x1jig&X-Amz-Signature=36a2334f4841c7cba6f2a937f77a47ed118c2e2c4518f42f9d92a520b90d421f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

