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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQ2BKVL%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGs%2BdljBy8wTXF%2FFzE97ySEjOH%2Fynq6vE0MUNkBeGSyHAiA4LT7gLgnejKKqYEONU7cab2lXlBuniFTZCY1YAHIqliqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqFCq1nGXcT%2FyHqycKtwDTju2CcTEtvoGZayTyvz9FFRB8TkB4XguTsFYEASL9dbgfTR%2BgsNc29sTEdUfEtHq%2BccqVamJsDrxNJoXgEXbx76dTTtGwi93K1einx5WDhlXaWMZl%2FMUPWalkS1GbdD%2BtZiksE4JiPsmHANTBUiEgzmeuYTkfEYu7EFsPcSR%2FTDQ8BLgnZZwGwhVDrABnw0onIqnEePRiWPw1H6BjRW7Un746BBj0x0cU6Dsfx8WdAq23Y2r5bLxhP%2Bfijy48hkU8ktJYDwYQauCvpecbvIsCH5%2F1yneAgccD8gSy9mfXklnC10S40KaYcaeNqCdoZt6%2F%2B5Q0L2MITEu60uqKIkOCtRjbfRVAuQcEq9nrPTiKdatWYwZJdhwf6X7l9Ys5WDlvqRJwpy8fwS%2F5c0uFK6qtUu7qoefP4j%2FkklaxsT3mMu4e76W5I%2FYL%2BnafHMbDJ7TAq7v9UaxzNEKyw%2B5yRZwDA78kFv5N3prxahXbt8ZAFNs6ZgYiTkLlWvfvJRvoU%2Bro2OJj%2BdIs0Bev7iqWJW1gBGbfHUSW2aEXQiB%2BgY9jxiUobE81QuDLx3SceBPfPeQRWKGMoqUiqFozZyNrLY01d6cto8QY%2FP%2BpGNBnfpUN4xJF%2B2ax%2FDxD6jO1XQwn6r8ygY6pgFVNKgV%2FkkznJcBVeMJreI8prQlQvR8X2yMDxw6bqdGeI%2Bdj3zh0QD1aa5xglIVdBHbqvSdfyqhxAeTNIHVkbIz4ziC2xamROZPZPDDTiXBjHpKTIk3c9zYPi3Gh7EhiBsL3J9Q7a6TMF4b2CvzO32rUlbcVCnSaSklQLp7DkIY4K2AQBNjin0%2FsLDI54eGCKL33i0PVgghP1kIM513PYOqhulWnnsu&X-Amz-Signature=08c6ba11827b9e60d7292bdc5e072c260716c0c5071da41fe942abd202f72236&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQ2BKVL%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGs%2BdljBy8wTXF%2FFzE97ySEjOH%2Fynq6vE0MUNkBeGSyHAiA4LT7gLgnejKKqYEONU7cab2lXlBuniFTZCY1YAHIqliqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqFCq1nGXcT%2FyHqycKtwDTju2CcTEtvoGZayTyvz9FFRB8TkB4XguTsFYEASL9dbgfTR%2BgsNc29sTEdUfEtHq%2BccqVamJsDrxNJoXgEXbx76dTTtGwi93K1einx5WDhlXaWMZl%2FMUPWalkS1GbdD%2BtZiksE4JiPsmHANTBUiEgzmeuYTkfEYu7EFsPcSR%2FTDQ8BLgnZZwGwhVDrABnw0onIqnEePRiWPw1H6BjRW7Un746BBj0x0cU6Dsfx8WdAq23Y2r5bLxhP%2Bfijy48hkU8ktJYDwYQauCvpecbvIsCH5%2F1yneAgccD8gSy9mfXklnC10S40KaYcaeNqCdoZt6%2F%2B5Q0L2MITEu60uqKIkOCtRjbfRVAuQcEq9nrPTiKdatWYwZJdhwf6X7l9Ys5WDlvqRJwpy8fwS%2F5c0uFK6qtUu7qoefP4j%2FkklaxsT3mMu4e76W5I%2FYL%2BnafHMbDJ7TAq7v9UaxzNEKyw%2B5yRZwDA78kFv5N3prxahXbt8ZAFNs6ZgYiTkLlWvfvJRvoU%2Bro2OJj%2BdIs0Bev7iqWJW1gBGbfHUSW2aEXQiB%2BgY9jxiUobE81QuDLx3SceBPfPeQRWKGMoqUiqFozZyNrLY01d6cto8QY%2FP%2BpGNBnfpUN4xJF%2B2ax%2FDxD6jO1XQwn6r8ygY6pgFVNKgV%2FkkznJcBVeMJreI8prQlQvR8X2yMDxw6bqdGeI%2Bdj3zh0QD1aa5xglIVdBHbqvSdfyqhxAeTNIHVkbIz4ziC2xamROZPZPDDTiXBjHpKTIk3c9zYPi3Gh7EhiBsL3J9Q7a6TMF4b2CvzO32rUlbcVCnSaSklQLp7DkIY4K2AQBNjin0%2FsLDI54eGCKL33i0PVgghP1kIM513PYOqhulWnnsu&X-Amz-Signature=21f6edcb0e4e118b815655f095201ee6edf5089bcc5285dedce74c74de8deb70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQ2BKVL%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGs%2BdljBy8wTXF%2FFzE97ySEjOH%2Fynq6vE0MUNkBeGSyHAiA4LT7gLgnejKKqYEONU7cab2lXlBuniFTZCY1YAHIqliqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqFCq1nGXcT%2FyHqycKtwDTju2CcTEtvoGZayTyvz9FFRB8TkB4XguTsFYEASL9dbgfTR%2BgsNc29sTEdUfEtHq%2BccqVamJsDrxNJoXgEXbx76dTTtGwi93K1einx5WDhlXaWMZl%2FMUPWalkS1GbdD%2BtZiksE4JiPsmHANTBUiEgzmeuYTkfEYu7EFsPcSR%2FTDQ8BLgnZZwGwhVDrABnw0onIqnEePRiWPw1H6BjRW7Un746BBj0x0cU6Dsfx8WdAq23Y2r5bLxhP%2Bfijy48hkU8ktJYDwYQauCvpecbvIsCH5%2F1yneAgccD8gSy9mfXklnC10S40KaYcaeNqCdoZt6%2F%2B5Q0L2MITEu60uqKIkOCtRjbfRVAuQcEq9nrPTiKdatWYwZJdhwf6X7l9Ys5WDlvqRJwpy8fwS%2F5c0uFK6qtUu7qoefP4j%2FkklaxsT3mMu4e76W5I%2FYL%2BnafHMbDJ7TAq7v9UaxzNEKyw%2B5yRZwDA78kFv5N3prxahXbt8ZAFNs6ZgYiTkLlWvfvJRvoU%2Bro2OJj%2BdIs0Bev7iqWJW1gBGbfHUSW2aEXQiB%2BgY9jxiUobE81QuDLx3SceBPfPeQRWKGMoqUiqFozZyNrLY01d6cto8QY%2FP%2BpGNBnfpUN4xJF%2B2ax%2FDxD6jO1XQwn6r8ygY6pgFVNKgV%2FkkznJcBVeMJreI8prQlQvR8X2yMDxw6bqdGeI%2Bdj3zh0QD1aa5xglIVdBHbqvSdfyqhxAeTNIHVkbIz4ziC2xamROZPZPDDTiXBjHpKTIk3c9zYPi3Gh7EhiBsL3J9Q7a6TMF4b2CvzO32rUlbcVCnSaSklQLp7DkIY4K2AQBNjin0%2FsLDI54eGCKL33i0PVgghP1kIM513PYOqhulWnnsu&X-Amz-Signature=477d09fe1843901660bf70c1daf69cb2de00be65649a07ca6bacd95bb0ac6fc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQ2BKVL%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGs%2BdljBy8wTXF%2FFzE97ySEjOH%2Fynq6vE0MUNkBeGSyHAiA4LT7gLgnejKKqYEONU7cab2lXlBuniFTZCY1YAHIqliqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqFCq1nGXcT%2FyHqycKtwDTju2CcTEtvoGZayTyvz9FFRB8TkB4XguTsFYEASL9dbgfTR%2BgsNc29sTEdUfEtHq%2BccqVamJsDrxNJoXgEXbx76dTTtGwi93K1einx5WDhlXaWMZl%2FMUPWalkS1GbdD%2BtZiksE4JiPsmHANTBUiEgzmeuYTkfEYu7EFsPcSR%2FTDQ8BLgnZZwGwhVDrABnw0onIqnEePRiWPw1H6BjRW7Un746BBj0x0cU6Dsfx8WdAq23Y2r5bLxhP%2Bfijy48hkU8ktJYDwYQauCvpecbvIsCH5%2F1yneAgccD8gSy9mfXklnC10S40KaYcaeNqCdoZt6%2F%2B5Q0L2MITEu60uqKIkOCtRjbfRVAuQcEq9nrPTiKdatWYwZJdhwf6X7l9Ys5WDlvqRJwpy8fwS%2F5c0uFK6qtUu7qoefP4j%2FkklaxsT3mMu4e76W5I%2FYL%2BnafHMbDJ7TAq7v9UaxzNEKyw%2B5yRZwDA78kFv5N3prxahXbt8ZAFNs6ZgYiTkLlWvfvJRvoU%2Bro2OJj%2BdIs0Bev7iqWJW1gBGbfHUSW2aEXQiB%2BgY9jxiUobE81QuDLx3SceBPfPeQRWKGMoqUiqFozZyNrLY01d6cto8QY%2FP%2BpGNBnfpUN4xJF%2B2ax%2FDxD6jO1XQwn6r8ygY6pgFVNKgV%2FkkznJcBVeMJreI8prQlQvR8X2yMDxw6bqdGeI%2Bdj3zh0QD1aa5xglIVdBHbqvSdfyqhxAeTNIHVkbIz4ziC2xamROZPZPDDTiXBjHpKTIk3c9zYPi3Gh7EhiBsL3J9Q7a6TMF4b2CvzO32rUlbcVCnSaSklQLp7DkIY4K2AQBNjin0%2FsLDI54eGCKL33i0PVgghP1kIM513PYOqhulWnnsu&X-Amz-Signature=00830aad022f4c9b697ad1fb73814ee7618a8556d06356ec07193a9a100ef1cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQ2BKVL%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGs%2BdljBy8wTXF%2FFzE97ySEjOH%2Fynq6vE0MUNkBeGSyHAiA4LT7gLgnejKKqYEONU7cab2lXlBuniFTZCY1YAHIqliqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqFCq1nGXcT%2FyHqycKtwDTju2CcTEtvoGZayTyvz9FFRB8TkB4XguTsFYEASL9dbgfTR%2BgsNc29sTEdUfEtHq%2BccqVamJsDrxNJoXgEXbx76dTTtGwi93K1einx5WDhlXaWMZl%2FMUPWalkS1GbdD%2BtZiksE4JiPsmHANTBUiEgzmeuYTkfEYu7EFsPcSR%2FTDQ8BLgnZZwGwhVDrABnw0onIqnEePRiWPw1H6BjRW7Un746BBj0x0cU6Dsfx8WdAq23Y2r5bLxhP%2Bfijy48hkU8ktJYDwYQauCvpecbvIsCH5%2F1yneAgccD8gSy9mfXklnC10S40KaYcaeNqCdoZt6%2F%2B5Q0L2MITEu60uqKIkOCtRjbfRVAuQcEq9nrPTiKdatWYwZJdhwf6X7l9Ys5WDlvqRJwpy8fwS%2F5c0uFK6qtUu7qoefP4j%2FkklaxsT3mMu4e76W5I%2FYL%2BnafHMbDJ7TAq7v9UaxzNEKyw%2B5yRZwDA78kFv5N3prxahXbt8ZAFNs6ZgYiTkLlWvfvJRvoU%2Bro2OJj%2BdIs0Bev7iqWJW1gBGbfHUSW2aEXQiB%2BgY9jxiUobE81QuDLx3SceBPfPeQRWKGMoqUiqFozZyNrLY01d6cto8QY%2FP%2BpGNBnfpUN4xJF%2B2ax%2FDxD6jO1XQwn6r8ygY6pgFVNKgV%2FkkznJcBVeMJreI8prQlQvR8X2yMDxw6bqdGeI%2Bdj3zh0QD1aa5xglIVdBHbqvSdfyqhxAeTNIHVkbIz4ziC2xamROZPZPDDTiXBjHpKTIk3c9zYPi3Gh7EhiBsL3J9Q7a6TMF4b2CvzO32rUlbcVCnSaSklQLp7DkIY4K2AQBNjin0%2FsLDI54eGCKL33i0PVgghP1kIM513PYOqhulWnnsu&X-Amz-Signature=ba4588610e6bf1079444653b7e79f6ce5e4a61aacbe7c0090eaf32f64ba5ac3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQ2BKVL%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGs%2BdljBy8wTXF%2FFzE97ySEjOH%2Fynq6vE0MUNkBeGSyHAiA4LT7gLgnejKKqYEONU7cab2lXlBuniFTZCY1YAHIqliqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqFCq1nGXcT%2FyHqycKtwDTju2CcTEtvoGZayTyvz9FFRB8TkB4XguTsFYEASL9dbgfTR%2BgsNc29sTEdUfEtHq%2BccqVamJsDrxNJoXgEXbx76dTTtGwi93K1einx5WDhlXaWMZl%2FMUPWalkS1GbdD%2BtZiksE4JiPsmHANTBUiEgzmeuYTkfEYu7EFsPcSR%2FTDQ8BLgnZZwGwhVDrABnw0onIqnEePRiWPw1H6BjRW7Un746BBj0x0cU6Dsfx8WdAq23Y2r5bLxhP%2Bfijy48hkU8ktJYDwYQauCvpecbvIsCH5%2F1yneAgccD8gSy9mfXklnC10S40KaYcaeNqCdoZt6%2F%2B5Q0L2MITEu60uqKIkOCtRjbfRVAuQcEq9nrPTiKdatWYwZJdhwf6X7l9Ys5WDlvqRJwpy8fwS%2F5c0uFK6qtUu7qoefP4j%2FkklaxsT3mMu4e76W5I%2FYL%2BnafHMbDJ7TAq7v9UaxzNEKyw%2B5yRZwDA78kFv5N3prxahXbt8ZAFNs6ZgYiTkLlWvfvJRvoU%2Bro2OJj%2BdIs0Bev7iqWJW1gBGbfHUSW2aEXQiB%2BgY9jxiUobE81QuDLx3SceBPfPeQRWKGMoqUiqFozZyNrLY01d6cto8QY%2FP%2BpGNBnfpUN4xJF%2B2ax%2FDxD6jO1XQwn6r8ygY6pgFVNKgV%2FkkznJcBVeMJreI8prQlQvR8X2yMDxw6bqdGeI%2Bdj3zh0QD1aa5xglIVdBHbqvSdfyqhxAeTNIHVkbIz4ziC2xamROZPZPDDTiXBjHpKTIk3c9zYPi3Gh7EhiBsL3J9Q7a6TMF4b2CvzO32rUlbcVCnSaSklQLp7DkIY4K2AQBNjin0%2FsLDI54eGCKL33i0PVgghP1kIM513PYOqhulWnnsu&X-Amz-Signature=dd0ef9671507b6e6504c3ca45ac084b8536f5f3046b2524f8c4739f9627cc2e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQ2BKVL%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGs%2BdljBy8wTXF%2FFzE97ySEjOH%2Fynq6vE0MUNkBeGSyHAiA4LT7gLgnejKKqYEONU7cab2lXlBuniFTZCY1YAHIqliqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqFCq1nGXcT%2FyHqycKtwDTju2CcTEtvoGZayTyvz9FFRB8TkB4XguTsFYEASL9dbgfTR%2BgsNc29sTEdUfEtHq%2BccqVamJsDrxNJoXgEXbx76dTTtGwi93K1einx5WDhlXaWMZl%2FMUPWalkS1GbdD%2BtZiksE4JiPsmHANTBUiEgzmeuYTkfEYu7EFsPcSR%2FTDQ8BLgnZZwGwhVDrABnw0onIqnEePRiWPw1H6BjRW7Un746BBj0x0cU6Dsfx8WdAq23Y2r5bLxhP%2Bfijy48hkU8ktJYDwYQauCvpecbvIsCH5%2F1yneAgccD8gSy9mfXklnC10S40KaYcaeNqCdoZt6%2F%2B5Q0L2MITEu60uqKIkOCtRjbfRVAuQcEq9nrPTiKdatWYwZJdhwf6X7l9Ys5WDlvqRJwpy8fwS%2F5c0uFK6qtUu7qoefP4j%2FkklaxsT3mMu4e76W5I%2FYL%2BnafHMbDJ7TAq7v9UaxzNEKyw%2B5yRZwDA78kFv5N3prxahXbt8ZAFNs6ZgYiTkLlWvfvJRvoU%2Bro2OJj%2BdIs0Bev7iqWJW1gBGbfHUSW2aEXQiB%2BgY9jxiUobE81QuDLx3SceBPfPeQRWKGMoqUiqFozZyNrLY01d6cto8QY%2FP%2BpGNBnfpUN4xJF%2B2ax%2FDxD6jO1XQwn6r8ygY6pgFVNKgV%2FkkznJcBVeMJreI8prQlQvR8X2yMDxw6bqdGeI%2Bdj3zh0QD1aa5xglIVdBHbqvSdfyqhxAeTNIHVkbIz4ziC2xamROZPZPDDTiXBjHpKTIk3c9zYPi3Gh7EhiBsL3J9Q7a6TMF4b2CvzO32rUlbcVCnSaSklQLp7DkIY4K2AQBNjin0%2FsLDI54eGCKL33i0PVgghP1kIM513PYOqhulWnnsu&X-Amz-Signature=c35936a65838f08d21956e1c5e0ecd6bbf632a79800f6f0f34d442a60a1aa7fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

