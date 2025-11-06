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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ6XJVJD%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB9QQgTDndiK%2BSyfD%2FDe75CL90dXfYTPBpVBG%2F3IrQhJAiAqY6v%2BVhfpze3i3pTTKa0Is4l5RcKIgbRUJ2vprS4wgCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFLRnSLS6Mh4ZP5%2FWKtwDBEJbM%2FeEsvwsswJEdfPA0%2FxiJRmPQz6BKMrh%2FxsF0mK4wtPJnKHOM9CNtzjd8mQqFdOmnf8VtZuyUm%2FynxUtbR7FeIRqvfKbzrqaTIFTFIu%2BzLhDUuZULMVB3JbcDoep6YqOyesVKRNOUnyliNUAW%2Fj62VpnNXW3tPisLouEm%2B%2BtFGwVAsDQ0qCQBAMOJA%2FVaKNCFwjn5Trot8lZO6CXc7DJC%2Fv%2FG4nUposCimRjzdjJsjAWCWQhbEFmEEinAuM2pRpnUfwZRH4vjdfDFZ9h0525VEG%2BFqvCkxxusMbD7K63QTSYsX6dO7whUu91M8IqxZ4rf7HV3KhNQ5h1CLPB5GA9ulWHLznFGL3inTukhWVFFC%2BX0m%2F7IWg749Q5Lm0UtZIPrzsKwAW4cVS76tBfyrUajeXe9eS4b8cjVSmpjP2saTXV0V6Xs78mBac%2Fb5opu7nRpR3g1gvEoj%2Bhhwyll4XcB9r3pcQlCx6WaW6p6Uvh8%2BSPo%2FXwTWxuEBYYrnpERR6C9GBgLYIErQpO2ROnu6i%2BgoB42%2F7mHnByEsT3XcLq04bbEVIDR8R6RkAFzBsjV%2BfQgorqfIPw6Wbp9S%2BoCX23LJRHqwrX1Jda87N8vFbnpESkH9pKz1XxlyEwofKvyAY6pgHue3sS6egEGFMuIcF8z9z7pxAPk%2BRTUhBASIHbktJI9GV10rVzMRan2o7KH3LFTw54IC52FNjyaRpsxcM1aOBjSY7Dz7BwtR9v7E6UyKX3GDzasB9mNKBTH7bL33XfJDbbDa%2BX5KGbfKPPXuIHE7z1tvMHRF7OsgRQhAEt%2BStK4nQdMp76WGM6ksvn%2BZ9XHQGb%2FX4Ceo6cgCT%2B%2BV915m%2F%2FOkzPFefp&X-Amz-Signature=00c5fabaf2474d476a515fa66ef76690c91861979837c1489975590d9bc51e24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ6XJVJD%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB9QQgTDndiK%2BSyfD%2FDe75CL90dXfYTPBpVBG%2F3IrQhJAiAqY6v%2BVhfpze3i3pTTKa0Is4l5RcKIgbRUJ2vprS4wgCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFLRnSLS6Mh4ZP5%2FWKtwDBEJbM%2FeEsvwsswJEdfPA0%2FxiJRmPQz6BKMrh%2FxsF0mK4wtPJnKHOM9CNtzjd8mQqFdOmnf8VtZuyUm%2FynxUtbR7FeIRqvfKbzrqaTIFTFIu%2BzLhDUuZULMVB3JbcDoep6YqOyesVKRNOUnyliNUAW%2Fj62VpnNXW3tPisLouEm%2B%2BtFGwVAsDQ0qCQBAMOJA%2FVaKNCFwjn5Trot8lZO6CXc7DJC%2Fv%2FG4nUposCimRjzdjJsjAWCWQhbEFmEEinAuM2pRpnUfwZRH4vjdfDFZ9h0525VEG%2BFqvCkxxusMbD7K63QTSYsX6dO7whUu91M8IqxZ4rf7HV3KhNQ5h1CLPB5GA9ulWHLznFGL3inTukhWVFFC%2BX0m%2F7IWg749Q5Lm0UtZIPrzsKwAW4cVS76tBfyrUajeXe9eS4b8cjVSmpjP2saTXV0V6Xs78mBac%2Fb5opu7nRpR3g1gvEoj%2Bhhwyll4XcB9r3pcQlCx6WaW6p6Uvh8%2BSPo%2FXwTWxuEBYYrnpERR6C9GBgLYIErQpO2ROnu6i%2BgoB42%2F7mHnByEsT3XcLq04bbEVIDR8R6RkAFzBsjV%2BfQgorqfIPw6Wbp9S%2BoCX23LJRHqwrX1Jda87N8vFbnpESkH9pKz1XxlyEwofKvyAY6pgHue3sS6egEGFMuIcF8z9z7pxAPk%2BRTUhBASIHbktJI9GV10rVzMRan2o7KH3LFTw54IC52FNjyaRpsxcM1aOBjSY7Dz7BwtR9v7E6UyKX3GDzasB9mNKBTH7bL33XfJDbbDa%2BX5KGbfKPPXuIHE7z1tvMHRF7OsgRQhAEt%2BStK4nQdMp76WGM6ksvn%2BZ9XHQGb%2FX4Ceo6cgCT%2B%2BV915m%2F%2FOkzPFefp&X-Amz-Signature=9f705b397b5bec183a2f33000c72770070770b2bf9e98aca0434dda101c368fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ6XJVJD%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB9QQgTDndiK%2BSyfD%2FDe75CL90dXfYTPBpVBG%2F3IrQhJAiAqY6v%2BVhfpze3i3pTTKa0Is4l5RcKIgbRUJ2vprS4wgCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFLRnSLS6Mh4ZP5%2FWKtwDBEJbM%2FeEsvwsswJEdfPA0%2FxiJRmPQz6BKMrh%2FxsF0mK4wtPJnKHOM9CNtzjd8mQqFdOmnf8VtZuyUm%2FynxUtbR7FeIRqvfKbzrqaTIFTFIu%2BzLhDUuZULMVB3JbcDoep6YqOyesVKRNOUnyliNUAW%2Fj62VpnNXW3tPisLouEm%2B%2BtFGwVAsDQ0qCQBAMOJA%2FVaKNCFwjn5Trot8lZO6CXc7DJC%2Fv%2FG4nUposCimRjzdjJsjAWCWQhbEFmEEinAuM2pRpnUfwZRH4vjdfDFZ9h0525VEG%2BFqvCkxxusMbD7K63QTSYsX6dO7whUu91M8IqxZ4rf7HV3KhNQ5h1CLPB5GA9ulWHLznFGL3inTukhWVFFC%2BX0m%2F7IWg749Q5Lm0UtZIPrzsKwAW4cVS76tBfyrUajeXe9eS4b8cjVSmpjP2saTXV0V6Xs78mBac%2Fb5opu7nRpR3g1gvEoj%2Bhhwyll4XcB9r3pcQlCx6WaW6p6Uvh8%2BSPo%2FXwTWxuEBYYrnpERR6C9GBgLYIErQpO2ROnu6i%2BgoB42%2F7mHnByEsT3XcLq04bbEVIDR8R6RkAFzBsjV%2BfQgorqfIPw6Wbp9S%2BoCX23LJRHqwrX1Jda87N8vFbnpESkH9pKz1XxlyEwofKvyAY6pgHue3sS6egEGFMuIcF8z9z7pxAPk%2BRTUhBASIHbktJI9GV10rVzMRan2o7KH3LFTw54IC52FNjyaRpsxcM1aOBjSY7Dz7BwtR9v7E6UyKX3GDzasB9mNKBTH7bL33XfJDbbDa%2BX5KGbfKPPXuIHE7z1tvMHRF7OsgRQhAEt%2BStK4nQdMp76WGM6ksvn%2BZ9XHQGb%2FX4Ceo6cgCT%2B%2BV915m%2F%2FOkzPFefp&X-Amz-Signature=2136d87de2e51f77fa60b46111d0cafb2826d57f78b4afc6220b039f3f3a1a6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ6XJVJD%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB9QQgTDndiK%2BSyfD%2FDe75CL90dXfYTPBpVBG%2F3IrQhJAiAqY6v%2BVhfpze3i3pTTKa0Is4l5RcKIgbRUJ2vprS4wgCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFLRnSLS6Mh4ZP5%2FWKtwDBEJbM%2FeEsvwsswJEdfPA0%2FxiJRmPQz6BKMrh%2FxsF0mK4wtPJnKHOM9CNtzjd8mQqFdOmnf8VtZuyUm%2FynxUtbR7FeIRqvfKbzrqaTIFTFIu%2BzLhDUuZULMVB3JbcDoep6YqOyesVKRNOUnyliNUAW%2Fj62VpnNXW3tPisLouEm%2B%2BtFGwVAsDQ0qCQBAMOJA%2FVaKNCFwjn5Trot8lZO6CXc7DJC%2Fv%2FG4nUposCimRjzdjJsjAWCWQhbEFmEEinAuM2pRpnUfwZRH4vjdfDFZ9h0525VEG%2BFqvCkxxusMbD7K63QTSYsX6dO7whUu91M8IqxZ4rf7HV3KhNQ5h1CLPB5GA9ulWHLznFGL3inTukhWVFFC%2BX0m%2F7IWg749Q5Lm0UtZIPrzsKwAW4cVS76tBfyrUajeXe9eS4b8cjVSmpjP2saTXV0V6Xs78mBac%2Fb5opu7nRpR3g1gvEoj%2Bhhwyll4XcB9r3pcQlCx6WaW6p6Uvh8%2BSPo%2FXwTWxuEBYYrnpERR6C9GBgLYIErQpO2ROnu6i%2BgoB42%2F7mHnByEsT3XcLq04bbEVIDR8R6RkAFzBsjV%2BfQgorqfIPw6Wbp9S%2BoCX23LJRHqwrX1Jda87N8vFbnpESkH9pKz1XxlyEwofKvyAY6pgHue3sS6egEGFMuIcF8z9z7pxAPk%2BRTUhBASIHbktJI9GV10rVzMRan2o7KH3LFTw54IC52FNjyaRpsxcM1aOBjSY7Dz7BwtR9v7E6UyKX3GDzasB9mNKBTH7bL33XfJDbbDa%2BX5KGbfKPPXuIHE7z1tvMHRF7OsgRQhAEt%2BStK4nQdMp76WGM6ksvn%2BZ9XHQGb%2FX4Ceo6cgCT%2B%2BV915m%2F%2FOkzPFefp&X-Amz-Signature=391a15a4999e04f33c79d6362f50f746dc171b5f433086e6502eaf0d1b74e5bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ6XJVJD%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB9QQgTDndiK%2BSyfD%2FDe75CL90dXfYTPBpVBG%2F3IrQhJAiAqY6v%2BVhfpze3i3pTTKa0Is4l5RcKIgbRUJ2vprS4wgCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFLRnSLS6Mh4ZP5%2FWKtwDBEJbM%2FeEsvwsswJEdfPA0%2FxiJRmPQz6BKMrh%2FxsF0mK4wtPJnKHOM9CNtzjd8mQqFdOmnf8VtZuyUm%2FynxUtbR7FeIRqvfKbzrqaTIFTFIu%2BzLhDUuZULMVB3JbcDoep6YqOyesVKRNOUnyliNUAW%2Fj62VpnNXW3tPisLouEm%2B%2BtFGwVAsDQ0qCQBAMOJA%2FVaKNCFwjn5Trot8lZO6CXc7DJC%2Fv%2FG4nUposCimRjzdjJsjAWCWQhbEFmEEinAuM2pRpnUfwZRH4vjdfDFZ9h0525VEG%2BFqvCkxxusMbD7K63QTSYsX6dO7whUu91M8IqxZ4rf7HV3KhNQ5h1CLPB5GA9ulWHLznFGL3inTukhWVFFC%2BX0m%2F7IWg749Q5Lm0UtZIPrzsKwAW4cVS76tBfyrUajeXe9eS4b8cjVSmpjP2saTXV0V6Xs78mBac%2Fb5opu7nRpR3g1gvEoj%2Bhhwyll4XcB9r3pcQlCx6WaW6p6Uvh8%2BSPo%2FXwTWxuEBYYrnpERR6C9GBgLYIErQpO2ROnu6i%2BgoB42%2F7mHnByEsT3XcLq04bbEVIDR8R6RkAFzBsjV%2BfQgorqfIPw6Wbp9S%2BoCX23LJRHqwrX1Jda87N8vFbnpESkH9pKz1XxlyEwofKvyAY6pgHue3sS6egEGFMuIcF8z9z7pxAPk%2BRTUhBASIHbktJI9GV10rVzMRan2o7KH3LFTw54IC52FNjyaRpsxcM1aOBjSY7Dz7BwtR9v7E6UyKX3GDzasB9mNKBTH7bL33XfJDbbDa%2BX5KGbfKPPXuIHE7z1tvMHRF7OsgRQhAEt%2BStK4nQdMp76WGM6ksvn%2BZ9XHQGb%2FX4Ceo6cgCT%2B%2BV915m%2F%2FOkzPFefp&X-Amz-Signature=755668f05d6893c954912bbe8a8c8ccb26eb72a7ed32e8d653cd877d31ed5056&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ6XJVJD%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB9QQgTDndiK%2BSyfD%2FDe75CL90dXfYTPBpVBG%2F3IrQhJAiAqY6v%2BVhfpze3i3pTTKa0Is4l5RcKIgbRUJ2vprS4wgCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFLRnSLS6Mh4ZP5%2FWKtwDBEJbM%2FeEsvwsswJEdfPA0%2FxiJRmPQz6BKMrh%2FxsF0mK4wtPJnKHOM9CNtzjd8mQqFdOmnf8VtZuyUm%2FynxUtbR7FeIRqvfKbzrqaTIFTFIu%2BzLhDUuZULMVB3JbcDoep6YqOyesVKRNOUnyliNUAW%2Fj62VpnNXW3tPisLouEm%2B%2BtFGwVAsDQ0qCQBAMOJA%2FVaKNCFwjn5Trot8lZO6CXc7DJC%2Fv%2FG4nUposCimRjzdjJsjAWCWQhbEFmEEinAuM2pRpnUfwZRH4vjdfDFZ9h0525VEG%2BFqvCkxxusMbD7K63QTSYsX6dO7whUu91M8IqxZ4rf7HV3KhNQ5h1CLPB5GA9ulWHLznFGL3inTukhWVFFC%2BX0m%2F7IWg749Q5Lm0UtZIPrzsKwAW4cVS76tBfyrUajeXe9eS4b8cjVSmpjP2saTXV0V6Xs78mBac%2Fb5opu7nRpR3g1gvEoj%2Bhhwyll4XcB9r3pcQlCx6WaW6p6Uvh8%2BSPo%2FXwTWxuEBYYrnpERR6C9GBgLYIErQpO2ROnu6i%2BgoB42%2F7mHnByEsT3XcLq04bbEVIDR8R6RkAFzBsjV%2BfQgorqfIPw6Wbp9S%2BoCX23LJRHqwrX1Jda87N8vFbnpESkH9pKz1XxlyEwofKvyAY6pgHue3sS6egEGFMuIcF8z9z7pxAPk%2BRTUhBASIHbktJI9GV10rVzMRan2o7KH3LFTw54IC52FNjyaRpsxcM1aOBjSY7Dz7BwtR9v7E6UyKX3GDzasB9mNKBTH7bL33XfJDbbDa%2BX5KGbfKPPXuIHE7z1tvMHRF7OsgRQhAEt%2BStK4nQdMp76WGM6ksvn%2BZ9XHQGb%2FX4Ceo6cgCT%2B%2BV915m%2F%2FOkzPFefp&X-Amz-Signature=7f379789d88685863cdfc5481b5b8107253f5e372e64b53ff0d8311e463e374b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ6XJVJD%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB9QQgTDndiK%2BSyfD%2FDe75CL90dXfYTPBpVBG%2F3IrQhJAiAqY6v%2BVhfpze3i3pTTKa0Is4l5RcKIgbRUJ2vprS4wgCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFLRnSLS6Mh4ZP5%2FWKtwDBEJbM%2FeEsvwsswJEdfPA0%2FxiJRmPQz6BKMrh%2FxsF0mK4wtPJnKHOM9CNtzjd8mQqFdOmnf8VtZuyUm%2FynxUtbR7FeIRqvfKbzrqaTIFTFIu%2BzLhDUuZULMVB3JbcDoep6YqOyesVKRNOUnyliNUAW%2Fj62VpnNXW3tPisLouEm%2B%2BtFGwVAsDQ0qCQBAMOJA%2FVaKNCFwjn5Trot8lZO6CXc7DJC%2Fv%2FG4nUposCimRjzdjJsjAWCWQhbEFmEEinAuM2pRpnUfwZRH4vjdfDFZ9h0525VEG%2BFqvCkxxusMbD7K63QTSYsX6dO7whUu91M8IqxZ4rf7HV3KhNQ5h1CLPB5GA9ulWHLznFGL3inTukhWVFFC%2BX0m%2F7IWg749Q5Lm0UtZIPrzsKwAW4cVS76tBfyrUajeXe9eS4b8cjVSmpjP2saTXV0V6Xs78mBac%2Fb5opu7nRpR3g1gvEoj%2Bhhwyll4XcB9r3pcQlCx6WaW6p6Uvh8%2BSPo%2FXwTWxuEBYYrnpERR6C9GBgLYIErQpO2ROnu6i%2BgoB42%2F7mHnByEsT3XcLq04bbEVIDR8R6RkAFzBsjV%2BfQgorqfIPw6Wbp9S%2BoCX23LJRHqwrX1Jda87N8vFbnpESkH9pKz1XxlyEwofKvyAY6pgHue3sS6egEGFMuIcF8z9z7pxAPk%2BRTUhBASIHbktJI9GV10rVzMRan2o7KH3LFTw54IC52FNjyaRpsxcM1aOBjSY7Dz7BwtR9v7E6UyKX3GDzasB9mNKBTH7bL33XfJDbbDa%2BX5KGbfKPPXuIHE7z1tvMHRF7OsgRQhAEt%2BStK4nQdMp76WGM6ksvn%2BZ9XHQGb%2FX4Ceo6cgCT%2B%2BV915m%2F%2FOkzPFefp&X-Amz-Signature=7a36b6b4dede70d0d2afba13ff550ad9ba48bea79c86f0622d7f5e6aedb8ade7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

