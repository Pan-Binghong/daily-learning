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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVYFOWVX%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE8helYqzdk5hR84Z1NMV%2FTrnIGcYIWDy4KuMYy9wqwbAiBhLFIZ2SjjfhYuCpenBW1vvfAGrS9zr%2FqTi6uXsnXLgSqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJqJF4%2BzZIDrijfq5KtwDo%2FmRqkNh5cxKJFkK6OFbfwjxGYZz31IW8VW2W%2BvcxAVQk9t8svSSYDx0hWVaF6cMRb1CT8G%2FXc8QLqU%2BXwhtiuDwxUi%2FjfYvhLRI8HmXuReZFPzl2JZ0qW9grC81c1rBqquZFNsW8pBeOXpuzqxO4HAmkORv9Fze%2FRGnDcVOCTjwFdP1KXWjhnL5W6zV6VX7Lseh7OY%2FM3kciBCuu5CyKFiJhaNcy5yvm5nFQjS%2BqoNRrwzUBPjCUxK67u4%2BcjJibU0vah8afI8TdFi0UG0Pz9Lx%2BxjwVvQowXte9c1BeHdmX8JumcCGvJ6pQLaD0XGSg4jvK2jVXIqD6P3wSOc%2FJwW2PW4wO%2Fpp5OY6th4gQQHPoklC07w9AgsL5fGzXCLDsELMA%2F0h1OHE2pWb9wNdemapgxLbqUOALcfobX%2BEo9vu8Rqml9b5TuE4m4IdUrwZMQ2V5QY%2FfFwOkf%2FF2paVNo9SGhaDNfBI3QPbmozVbbmQadRWm67%2BR1UaHbh6B7gTnuTGQF1Jk2qaeX90O1ggKdriNjuVxjGTnTFcfGPILfPMtf836eMD9z29UVd2%2BM4SHEDHy%2BVhRVLt7g5S1H4SEVCR9pXTHGlIrubxAnwcLaav0GyL%2FUSgUlaEaPYwg8SBywY6pgFTSS2Gc3gLBhqWQ7ES5PseVwiY9oxxQwWEqFCCthyArGKzWLuoY1pG7l6leo6nQQb9pn7NeYyc4SrZHmbUeJ3x3RKHemt6xKFEZbmkEIz4R1qK1LRhXHKxotfm%2BywhIMlGGmNue1kUBQGvHpeYxIN%2BpsXWQ9PFHFH4%2FP%2B7JMYajAFgX%2FRENvrj9XMHK7RnF3RqZfXA8pR%2BhR%2FOAITEfQ2WnU2xsicV&X-Amz-Signature=a467ad7ae99da37ea681540f00494572d169990eb6325862739b793c1e289cc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVYFOWVX%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE8helYqzdk5hR84Z1NMV%2FTrnIGcYIWDy4KuMYy9wqwbAiBhLFIZ2SjjfhYuCpenBW1vvfAGrS9zr%2FqTi6uXsnXLgSqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJqJF4%2BzZIDrijfq5KtwDo%2FmRqkNh5cxKJFkK6OFbfwjxGYZz31IW8VW2W%2BvcxAVQk9t8svSSYDx0hWVaF6cMRb1CT8G%2FXc8QLqU%2BXwhtiuDwxUi%2FjfYvhLRI8HmXuReZFPzl2JZ0qW9grC81c1rBqquZFNsW8pBeOXpuzqxO4HAmkORv9Fze%2FRGnDcVOCTjwFdP1KXWjhnL5W6zV6VX7Lseh7OY%2FM3kciBCuu5CyKFiJhaNcy5yvm5nFQjS%2BqoNRrwzUBPjCUxK67u4%2BcjJibU0vah8afI8TdFi0UG0Pz9Lx%2BxjwVvQowXte9c1BeHdmX8JumcCGvJ6pQLaD0XGSg4jvK2jVXIqD6P3wSOc%2FJwW2PW4wO%2Fpp5OY6th4gQQHPoklC07w9AgsL5fGzXCLDsELMA%2F0h1OHE2pWb9wNdemapgxLbqUOALcfobX%2BEo9vu8Rqml9b5TuE4m4IdUrwZMQ2V5QY%2FfFwOkf%2FF2paVNo9SGhaDNfBI3QPbmozVbbmQadRWm67%2BR1UaHbh6B7gTnuTGQF1Jk2qaeX90O1ggKdriNjuVxjGTnTFcfGPILfPMtf836eMD9z29UVd2%2BM4SHEDHy%2BVhRVLt7g5S1H4SEVCR9pXTHGlIrubxAnwcLaav0GyL%2FUSgUlaEaPYwg8SBywY6pgFTSS2Gc3gLBhqWQ7ES5PseVwiY9oxxQwWEqFCCthyArGKzWLuoY1pG7l6leo6nQQb9pn7NeYyc4SrZHmbUeJ3x3RKHemt6xKFEZbmkEIz4R1qK1LRhXHKxotfm%2BywhIMlGGmNue1kUBQGvHpeYxIN%2BpsXWQ9PFHFH4%2FP%2B7JMYajAFgX%2FRENvrj9XMHK7RnF3RqZfXA8pR%2BhR%2FOAITEfQ2WnU2xsicV&X-Amz-Signature=07d6ea950bf304f683d2cbdeb34699e0eaf7db7b2746519389982fe520a447da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVYFOWVX%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE8helYqzdk5hR84Z1NMV%2FTrnIGcYIWDy4KuMYy9wqwbAiBhLFIZ2SjjfhYuCpenBW1vvfAGrS9zr%2FqTi6uXsnXLgSqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJqJF4%2BzZIDrijfq5KtwDo%2FmRqkNh5cxKJFkK6OFbfwjxGYZz31IW8VW2W%2BvcxAVQk9t8svSSYDx0hWVaF6cMRb1CT8G%2FXc8QLqU%2BXwhtiuDwxUi%2FjfYvhLRI8HmXuReZFPzl2JZ0qW9grC81c1rBqquZFNsW8pBeOXpuzqxO4HAmkORv9Fze%2FRGnDcVOCTjwFdP1KXWjhnL5W6zV6VX7Lseh7OY%2FM3kciBCuu5CyKFiJhaNcy5yvm5nFQjS%2BqoNRrwzUBPjCUxK67u4%2BcjJibU0vah8afI8TdFi0UG0Pz9Lx%2BxjwVvQowXte9c1BeHdmX8JumcCGvJ6pQLaD0XGSg4jvK2jVXIqD6P3wSOc%2FJwW2PW4wO%2Fpp5OY6th4gQQHPoklC07w9AgsL5fGzXCLDsELMA%2F0h1OHE2pWb9wNdemapgxLbqUOALcfobX%2BEo9vu8Rqml9b5TuE4m4IdUrwZMQ2V5QY%2FfFwOkf%2FF2paVNo9SGhaDNfBI3QPbmozVbbmQadRWm67%2BR1UaHbh6B7gTnuTGQF1Jk2qaeX90O1ggKdriNjuVxjGTnTFcfGPILfPMtf836eMD9z29UVd2%2BM4SHEDHy%2BVhRVLt7g5S1H4SEVCR9pXTHGlIrubxAnwcLaav0GyL%2FUSgUlaEaPYwg8SBywY6pgFTSS2Gc3gLBhqWQ7ES5PseVwiY9oxxQwWEqFCCthyArGKzWLuoY1pG7l6leo6nQQb9pn7NeYyc4SrZHmbUeJ3x3RKHemt6xKFEZbmkEIz4R1qK1LRhXHKxotfm%2BywhIMlGGmNue1kUBQGvHpeYxIN%2BpsXWQ9PFHFH4%2FP%2B7JMYajAFgX%2FRENvrj9XMHK7RnF3RqZfXA8pR%2BhR%2FOAITEfQ2WnU2xsicV&X-Amz-Signature=74a56c0e111dc81d451a56dbd237fee4a4f6183c1b350c27fb2144e26a5c5c49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVYFOWVX%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE8helYqzdk5hR84Z1NMV%2FTrnIGcYIWDy4KuMYy9wqwbAiBhLFIZ2SjjfhYuCpenBW1vvfAGrS9zr%2FqTi6uXsnXLgSqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJqJF4%2BzZIDrijfq5KtwDo%2FmRqkNh5cxKJFkK6OFbfwjxGYZz31IW8VW2W%2BvcxAVQk9t8svSSYDx0hWVaF6cMRb1CT8G%2FXc8QLqU%2BXwhtiuDwxUi%2FjfYvhLRI8HmXuReZFPzl2JZ0qW9grC81c1rBqquZFNsW8pBeOXpuzqxO4HAmkORv9Fze%2FRGnDcVOCTjwFdP1KXWjhnL5W6zV6VX7Lseh7OY%2FM3kciBCuu5CyKFiJhaNcy5yvm5nFQjS%2BqoNRrwzUBPjCUxK67u4%2BcjJibU0vah8afI8TdFi0UG0Pz9Lx%2BxjwVvQowXte9c1BeHdmX8JumcCGvJ6pQLaD0XGSg4jvK2jVXIqD6P3wSOc%2FJwW2PW4wO%2Fpp5OY6th4gQQHPoklC07w9AgsL5fGzXCLDsELMA%2F0h1OHE2pWb9wNdemapgxLbqUOALcfobX%2BEo9vu8Rqml9b5TuE4m4IdUrwZMQ2V5QY%2FfFwOkf%2FF2paVNo9SGhaDNfBI3QPbmozVbbmQadRWm67%2BR1UaHbh6B7gTnuTGQF1Jk2qaeX90O1ggKdriNjuVxjGTnTFcfGPILfPMtf836eMD9z29UVd2%2BM4SHEDHy%2BVhRVLt7g5S1H4SEVCR9pXTHGlIrubxAnwcLaav0GyL%2FUSgUlaEaPYwg8SBywY6pgFTSS2Gc3gLBhqWQ7ES5PseVwiY9oxxQwWEqFCCthyArGKzWLuoY1pG7l6leo6nQQb9pn7NeYyc4SrZHmbUeJ3x3RKHemt6xKFEZbmkEIz4R1qK1LRhXHKxotfm%2BywhIMlGGmNue1kUBQGvHpeYxIN%2BpsXWQ9PFHFH4%2FP%2B7JMYajAFgX%2FRENvrj9XMHK7RnF3RqZfXA8pR%2BhR%2FOAITEfQ2WnU2xsicV&X-Amz-Signature=925dce1bebbebe5661b96459b1cce0462f59be106809448f734d34b2eabc9f80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVYFOWVX%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE8helYqzdk5hR84Z1NMV%2FTrnIGcYIWDy4KuMYy9wqwbAiBhLFIZ2SjjfhYuCpenBW1vvfAGrS9zr%2FqTi6uXsnXLgSqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJqJF4%2BzZIDrijfq5KtwDo%2FmRqkNh5cxKJFkK6OFbfwjxGYZz31IW8VW2W%2BvcxAVQk9t8svSSYDx0hWVaF6cMRb1CT8G%2FXc8QLqU%2BXwhtiuDwxUi%2FjfYvhLRI8HmXuReZFPzl2JZ0qW9grC81c1rBqquZFNsW8pBeOXpuzqxO4HAmkORv9Fze%2FRGnDcVOCTjwFdP1KXWjhnL5W6zV6VX7Lseh7OY%2FM3kciBCuu5CyKFiJhaNcy5yvm5nFQjS%2BqoNRrwzUBPjCUxK67u4%2BcjJibU0vah8afI8TdFi0UG0Pz9Lx%2BxjwVvQowXte9c1BeHdmX8JumcCGvJ6pQLaD0XGSg4jvK2jVXIqD6P3wSOc%2FJwW2PW4wO%2Fpp5OY6th4gQQHPoklC07w9AgsL5fGzXCLDsELMA%2F0h1OHE2pWb9wNdemapgxLbqUOALcfobX%2BEo9vu8Rqml9b5TuE4m4IdUrwZMQ2V5QY%2FfFwOkf%2FF2paVNo9SGhaDNfBI3QPbmozVbbmQadRWm67%2BR1UaHbh6B7gTnuTGQF1Jk2qaeX90O1ggKdriNjuVxjGTnTFcfGPILfPMtf836eMD9z29UVd2%2BM4SHEDHy%2BVhRVLt7g5S1H4SEVCR9pXTHGlIrubxAnwcLaav0GyL%2FUSgUlaEaPYwg8SBywY6pgFTSS2Gc3gLBhqWQ7ES5PseVwiY9oxxQwWEqFCCthyArGKzWLuoY1pG7l6leo6nQQb9pn7NeYyc4SrZHmbUeJ3x3RKHemt6xKFEZbmkEIz4R1qK1LRhXHKxotfm%2BywhIMlGGmNue1kUBQGvHpeYxIN%2BpsXWQ9PFHFH4%2FP%2B7JMYajAFgX%2FRENvrj9XMHK7RnF3RqZfXA8pR%2BhR%2FOAITEfQ2WnU2xsicV&X-Amz-Signature=01d0b69dd9a5a54bf6529459935439fdbde334fe63cbb16891e0c42362e3aecd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVYFOWVX%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE8helYqzdk5hR84Z1NMV%2FTrnIGcYIWDy4KuMYy9wqwbAiBhLFIZ2SjjfhYuCpenBW1vvfAGrS9zr%2FqTi6uXsnXLgSqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJqJF4%2BzZIDrijfq5KtwDo%2FmRqkNh5cxKJFkK6OFbfwjxGYZz31IW8VW2W%2BvcxAVQk9t8svSSYDx0hWVaF6cMRb1CT8G%2FXc8QLqU%2BXwhtiuDwxUi%2FjfYvhLRI8HmXuReZFPzl2JZ0qW9grC81c1rBqquZFNsW8pBeOXpuzqxO4HAmkORv9Fze%2FRGnDcVOCTjwFdP1KXWjhnL5W6zV6VX7Lseh7OY%2FM3kciBCuu5CyKFiJhaNcy5yvm5nFQjS%2BqoNRrwzUBPjCUxK67u4%2BcjJibU0vah8afI8TdFi0UG0Pz9Lx%2BxjwVvQowXte9c1BeHdmX8JumcCGvJ6pQLaD0XGSg4jvK2jVXIqD6P3wSOc%2FJwW2PW4wO%2Fpp5OY6th4gQQHPoklC07w9AgsL5fGzXCLDsELMA%2F0h1OHE2pWb9wNdemapgxLbqUOALcfobX%2BEo9vu8Rqml9b5TuE4m4IdUrwZMQ2V5QY%2FfFwOkf%2FF2paVNo9SGhaDNfBI3QPbmozVbbmQadRWm67%2BR1UaHbh6B7gTnuTGQF1Jk2qaeX90O1ggKdriNjuVxjGTnTFcfGPILfPMtf836eMD9z29UVd2%2BM4SHEDHy%2BVhRVLt7g5S1H4SEVCR9pXTHGlIrubxAnwcLaav0GyL%2FUSgUlaEaPYwg8SBywY6pgFTSS2Gc3gLBhqWQ7ES5PseVwiY9oxxQwWEqFCCthyArGKzWLuoY1pG7l6leo6nQQb9pn7NeYyc4SrZHmbUeJ3x3RKHemt6xKFEZbmkEIz4R1qK1LRhXHKxotfm%2BywhIMlGGmNue1kUBQGvHpeYxIN%2BpsXWQ9PFHFH4%2FP%2B7JMYajAFgX%2FRENvrj9XMHK7RnF3RqZfXA8pR%2BhR%2FOAITEfQ2WnU2xsicV&X-Amz-Signature=761f3f99b99dc4b4e8184afb42c06bd8eb165d62e58cdda5af47f12dbed82345&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVYFOWVX%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE8helYqzdk5hR84Z1NMV%2FTrnIGcYIWDy4KuMYy9wqwbAiBhLFIZ2SjjfhYuCpenBW1vvfAGrS9zr%2FqTi6uXsnXLgSqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJqJF4%2BzZIDrijfq5KtwDo%2FmRqkNh5cxKJFkK6OFbfwjxGYZz31IW8VW2W%2BvcxAVQk9t8svSSYDx0hWVaF6cMRb1CT8G%2FXc8QLqU%2BXwhtiuDwxUi%2FjfYvhLRI8HmXuReZFPzl2JZ0qW9grC81c1rBqquZFNsW8pBeOXpuzqxO4HAmkORv9Fze%2FRGnDcVOCTjwFdP1KXWjhnL5W6zV6VX7Lseh7OY%2FM3kciBCuu5CyKFiJhaNcy5yvm5nFQjS%2BqoNRrwzUBPjCUxK67u4%2BcjJibU0vah8afI8TdFi0UG0Pz9Lx%2BxjwVvQowXte9c1BeHdmX8JumcCGvJ6pQLaD0XGSg4jvK2jVXIqD6P3wSOc%2FJwW2PW4wO%2Fpp5OY6th4gQQHPoklC07w9AgsL5fGzXCLDsELMA%2F0h1OHE2pWb9wNdemapgxLbqUOALcfobX%2BEo9vu8Rqml9b5TuE4m4IdUrwZMQ2V5QY%2FfFwOkf%2FF2paVNo9SGhaDNfBI3QPbmozVbbmQadRWm67%2BR1UaHbh6B7gTnuTGQF1Jk2qaeX90O1ggKdriNjuVxjGTnTFcfGPILfPMtf836eMD9z29UVd2%2BM4SHEDHy%2BVhRVLt7g5S1H4SEVCR9pXTHGlIrubxAnwcLaav0GyL%2FUSgUlaEaPYwg8SBywY6pgFTSS2Gc3gLBhqWQ7ES5PseVwiY9oxxQwWEqFCCthyArGKzWLuoY1pG7l6leo6nQQb9pn7NeYyc4SrZHmbUeJ3x3RKHemt6xKFEZbmkEIz4R1qK1LRhXHKxotfm%2BywhIMlGGmNue1kUBQGvHpeYxIN%2BpsXWQ9PFHFH4%2FP%2B7JMYajAFgX%2FRENvrj9XMHK7RnF3RqZfXA8pR%2BhR%2FOAITEfQ2WnU2xsicV&X-Amz-Signature=66b167be092c1ae555b65da64cfae671d2e9301c9e4e5f5aa2a1f2a417243f66&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

