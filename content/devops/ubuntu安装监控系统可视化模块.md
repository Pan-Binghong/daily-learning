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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EHL5X3E%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIFk4Qw94bekW4qj3DirbwrYpKws6RUZ7gpf%2B5UAwwz4tAiEAn8HoRMzXVs26lfvYnN4d9YLfJNw53CtFCl%2FONOFFWUQq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDDXpVLFQXESLsO0%2B2ircA8lDA5WT4PhpPpwKk2tfaktsNr9AVX37kVulsasjAGTURoX5cn1My%2ByIp15lmMEKoa3ep6%2FQT8r%2BANO7orlV8T4jK%2F9YKxUXLwDmnxwEXOqqerIKGCmYup4g6MtdOepky3%2FgC%2Bh%2FEBbkauZTb1%2BFE8rwFAyHgZ2gozz99PZIUruSI4zS05F8k2Rd6hdm6inCV%2BV5kgmmpgfBNONzUvjUjJsr%2Bihtdc2hpKGPDXCDLptvUHEyH6k0joNydQxb%2BJBMh%2ByEtD6s3GKlWtcmknR5nehcAwR%2FOIvKs2vpMifxNrCf%2BQcs9cSwE74ouF21EV8r8lHkYR%2FB2qy1DmpEA2ea8zsiHr4fi8GN2uDmznI74KqU8Z3eOGpahhQvsNl1wea%2FkjRo2VczqPa3b8EYCTZrFdX5%2BlKfrNIHK9TqZWdXo0sr2RvNiXzSII%2FX%2Byp%2FOxo5kGKY25emZ07R3jB9uTc5y3OAOh0UjADewX2AVp0uHlZ8wGJUJyhqmOD7J8p11l%2FpZdFT8YWPPWpOflAkeecYSLUKE877cfLyGK5Fx1M5SgVvgN5KsSegGp07HwTj1u4PjfahBFtU6s1%2FydcYMCpkk2OKzdi%2FUNcojGtAnUatXsevTYcKsEaBViO8WjxKMPm%2Bos4GOqUBtE9gMW38tVQbU9jUKMWdeDKyaA03%2BONu%2BXFBHVbQ%2F1ISgrpsFEV547%2Fdsl0gWjpRPUqrc1KLddwz4l83YZv9X4OHlQQ4mK6NCnvFAQzZ85NTzzQ5eVHHcZ2zeC9scpcW%2BJ%2B%2BunLrrS7jrUKcKAXaehL81Gzl%2B2Mgzt8zcgk0AscyGUDsFhiLlVAShQ198lF129ZUwGJYJcj27MX71Gr7KLR6nUWh&X-Amz-Signature=60af7fd412f7c694ebb7da32ac0cb8d89bf54974dec932a7916fac249aea4cfb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EHL5X3E%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIFk4Qw94bekW4qj3DirbwrYpKws6RUZ7gpf%2B5UAwwz4tAiEAn8HoRMzXVs26lfvYnN4d9YLfJNw53CtFCl%2FONOFFWUQq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDDXpVLFQXESLsO0%2B2ircA8lDA5WT4PhpPpwKk2tfaktsNr9AVX37kVulsasjAGTURoX5cn1My%2ByIp15lmMEKoa3ep6%2FQT8r%2BANO7orlV8T4jK%2F9YKxUXLwDmnxwEXOqqerIKGCmYup4g6MtdOepky3%2FgC%2Bh%2FEBbkauZTb1%2BFE8rwFAyHgZ2gozz99PZIUruSI4zS05F8k2Rd6hdm6inCV%2BV5kgmmpgfBNONzUvjUjJsr%2Bihtdc2hpKGPDXCDLptvUHEyH6k0joNydQxb%2BJBMh%2ByEtD6s3GKlWtcmknR5nehcAwR%2FOIvKs2vpMifxNrCf%2BQcs9cSwE74ouF21EV8r8lHkYR%2FB2qy1DmpEA2ea8zsiHr4fi8GN2uDmznI74KqU8Z3eOGpahhQvsNl1wea%2FkjRo2VczqPa3b8EYCTZrFdX5%2BlKfrNIHK9TqZWdXo0sr2RvNiXzSII%2FX%2Byp%2FOxo5kGKY25emZ07R3jB9uTc5y3OAOh0UjADewX2AVp0uHlZ8wGJUJyhqmOD7J8p11l%2FpZdFT8YWPPWpOflAkeecYSLUKE877cfLyGK5Fx1M5SgVvgN5KsSegGp07HwTj1u4PjfahBFtU6s1%2FydcYMCpkk2OKzdi%2FUNcojGtAnUatXsevTYcKsEaBViO8WjxKMPm%2Bos4GOqUBtE9gMW38tVQbU9jUKMWdeDKyaA03%2BONu%2BXFBHVbQ%2F1ISgrpsFEV547%2Fdsl0gWjpRPUqrc1KLddwz4l83YZv9X4OHlQQ4mK6NCnvFAQzZ85NTzzQ5eVHHcZ2zeC9scpcW%2BJ%2B%2BunLrrS7jrUKcKAXaehL81Gzl%2B2Mgzt8zcgk0AscyGUDsFhiLlVAShQ198lF129ZUwGJYJcj27MX71Gr7KLR6nUWh&X-Amz-Signature=8363f6dac023da2d8944fc930ff0c37be8f3661808c776df593e6616bc4440d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EHL5X3E%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIFk4Qw94bekW4qj3DirbwrYpKws6RUZ7gpf%2B5UAwwz4tAiEAn8HoRMzXVs26lfvYnN4d9YLfJNw53CtFCl%2FONOFFWUQq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDDXpVLFQXESLsO0%2B2ircA8lDA5WT4PhpPpwKk2tfaktsNr9AVX37kVulsasjAGTURoX5cn1My%2ByIp15lmMEKoa3ep6%2FQT8r%2BANO7orlV8T4jK%2F9YKxUXLwDmnxwEXOqqerIKGCmYup4g6MtdOepky3%2FgC%2Bh%2FEBbkauZTb1%2BFE8rwFAyHgZ2gozz99PZIUruSI4zS05F8k2Rd6hdm6inCV%2BV5kgmmpgfBNONzUvjUjJsr%2Bihtdc2hpKGPDXCDLptvUHEyH6k0joNydQxb%2BJBMh%2ByEtD6s3GKlWtcmknR5nehcAwR%2FOIvKs2vpMifxNrCf%2BQcs9cSwE74ouF21EV8r8lHkYR%2FB2qy1DmpEA2ea8zsiHr4fi8GN2uDmznI74KqU8Z3eOGpahhQvsNl1wea%2FkjRo2VczqPa3b8EYCTZrFdX5%2BlKfrNIHK9TqZWdXo0sr2RvNiXzSII%2FX%2Byp%2FOxo5kGKY25emZ07R3jB9uTc5y3OAOh0UjADewX2AVp0uHlZ8wGJUJyhqmOD7J8p11l%2FpZdFT8YWPPWpOflAkeecYSLUKE877cfLyGK5Fx1M5SgVvgN5KsSegGp07HwTj1u4PjfahBFtU6s1%2FydcYMCpkk2OKzdi%2FUNcojGtAnUatXsevTYcKsEaBViO8WjxKMPm%2Bos4GOqUBtE9gMW38tVQbU9jUKMWdeDKyaA03%2BONu%2BXFBHVbQ%2F1ISgrpsFEV547%2Fdsl0gWjpRPUqrc1KLddwz4l83YZv9X4OHlQQ4mK6NCnvFAQzZ85NTzzQ5eVHHcZ2zeC9scpcW%2BJ%2B%2BunLrrS7jrUKcKAXaehL81Gzl%2B2Mgzt8zcgk0AscyGUDsFhiLlVAShQ198lF129ZUwGJYJcj27MX71Gr7KLR6nUWh&X-Amz-Signature=3941426e227fe7519f897194091accef3725f39c4f1ac9561bb20413bd6e2ecc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EHL5X3E%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIFk4Qw94bekW4qj3DirbwrYpKws6RUZ7gpf%2B5UAwwz4tAiEAn8HoRMzXVs26lfvYnN4d9YLfJNw53CtFCl%2FONOFFWUQq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDDXpVLFQXESLsO0%2B2ircA8lDA5WT4PhpPpwKk2tfaktsNr9AVX37kVulsasjAGTURoX5cn1My%2ByIp15lmMEKoa3ep6%2FQT8r%2BANO7orlV8T4jK%2F9YKxUXLwDmnxwEXOqqerIKGCmYup4g6MtdOepky3%2FgC%2Bh%2FEBbkauZTb1%2BFE8rwFAyHgZ2gozz99PZIUruSI4zS05F8k2Rd6hdm6inCV%2BV5kgmmpgfBNONzUvjUjJsr%2Bihtdc2hpKGPDXCDLptvUHEyH6k0joNydQxb%2BJBMh%2ByEtD6s3GKlWtcmknR5nehcAwR%2FOIvKs2vpMifxNrCf%2BQcs9cSwE74ouF21EV8r8lHkYR%2FB2qy1DmpEA2ea8zsiHr4fi8GN2uDmznI74KqU8Z3eOGpahhQvsNl1wea%2FkjRo2VczqPa3b8EYCTZrFdX5%2BlKfrNIHK9TqZWdXo0sr2RvNiXzSII%2FX%2Byp%2FOxo5kGKY25emZ07R3jB9uTc5y3OAOh0UjADewX2AVp0uHlZ8wGJUJyhqmOD7J8p11l%2FpZdFT8YWPPWpOflAkeecYSLUKE877cfLyGK5Fx1M5SgVvgN5KsSegGp07HwTj1u4PjfahBFtU6s1%2FydcYMCpkk2OKzdi%2FUNcojGtAnUatXsevTYcKsEaBViO8WjxKMPm%2Bos4GOqUBtE9gMW38tVQbU9jUKMWdeDKyaA03%2BONu%2BXFBHVbQ%2F1ISgrpsFEV547%2Fdsl0gWjpRPUqrc1KLddwz4l83YZv9X4OHlQQ4mK6NCnvFAQzZ85NTzzQ5eVHHcZ2zeC9scpcW%2BJ%2B%2BunLrrS7jrUKcKAXaehL81Gzl%2B2Mgzt8zcgk0AscyGUDsFhiLlVAShQ198lF129ZUwGJYJcj27MX71Gr7KLR6nUWh&X-Amz-Signature=10243db14eb73d5d55d4b7a422274465cac94b3a5a80349268c89280a6244f44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EHL5X3E%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIFk4Qw94bekW4qj3DirbwrYpKws6RUZ7gpf%2B5UAwwz4tAiEAn8HoRMzXVs26lfvYnN4d9YLfJNw53CtFCl%2FONOFFWUQq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDDXpVLFQXESLsO0%2B2ircA8lDA5WT4PhpPpwKk2tfaktsNr9AVX37kVulsasjAGTURoX5cn1My%2ByIp15lmMEKoa3ep6%2FQT8r%2BANO7orlV8T4jK%2F9YKxUXLwDmnxwEXOqqerIKGCmYup4g6MtdOepky3%2FgC%2Bh%2FEBbkauZTb1%2BFE8rwFAyHgZ2gozz99PZIUruSI4zS05F8k2Rd6hdm6inCV%2BV5kgmmpgfBNONzUvjUjJsr%2Bihtdc2hpKGPDXCDLptvUHEyH6k0joNydQxb%2BJBMh%2ByEtD6s3GKlWtcmknR5nehcAwR%2FOIvKs2vpMifxNrCf%2BQcs9cSwE74ouF21EV8r8lHkYR%2FB2qy1DmpEA2ea8zsiHr4fi8GN2uDmznI74KqU8Z3eOGpahhQvsNl1wea%2FkjRo2VczqPa3b8EYCTZrFdX5%2BlKfrNIHK9TqZWdXo0sr2RvNiXzSII%2FX%2Byp%2FOxo5kGKY25emZ07R3jB9uTc5y3OAOh0UjADewX2AVp0uHlZ8wGJUJyhqmOD7J8p11l%2FpZdFT8YWPPWpOflAkeecYSLUKE877cfLyGK5Fx1M5SgVvgN5KsSegGp07HwTj1u4PjfahBFtU6s1%2FydcYMCpkk2OKzdi%2FUNcojGtAnUatXsevTYcKsEaBViO8WjxKMPm%2Bos4GOqUBtE9gMW38tVQbU9jUKMWdeDKyaA03%2BONu%2BXFBHVbQ%2F1ISgrpsFEV547%2Fdsl0gWjpRPUqrc1KLddwz4l83YZv9X4OHlQQ4mK6NCnvFAQzZ85NTzzQ5eVHHcZ2zeC9scpcW%2BJ%2B%2BunLrrS7jrUKcKAXaehL81Gzl%2B2Mgzt8zcgk0AscyGUDsFhiLlVAShQ198lF129ZUwGJYJcj27MX71Gr7KLR6nUWh&X-Amz-Signature=8b7789bd98d5e7858220d46f924b2f25ae2c3bd74b1e1715d5a72855fb30bffd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EHL5X3E%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIFk4Qw94bekW4qj3DirbwrYpKws6RUZ7gpf%2B5UAwwz4tAiEAn8HoRMzXVs26lfvYnN4d9YLfJNw53CtFCl%2FONOFFWUQq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDDXpVLFQXESLsO0%2B2ircA8lDA5WT4PhpPpwKk2tfaktsNr9AVX37kVulsasjAGTURoX5cn1My%2ByIp15lmMEKoa3ep6%2FQT8r%2BANO7orlV8T4jK%2F9YKxUXLwDmnxwEXOqqerIKGCmYup4g6MtdOepky3%2FgC%2Bh%2FEBbkauZTb1%2BFE8rwFAyHgZ2gozz99PZIUruSI4zS05F8k2Rd6hdm6inCV%2BV5kgmmpgfBNONzUvjUjJsr%2Bihtdc2hpKGPDXCDLptvUHEyH6k0joNydQxb%2BJBMh%2ByEtD6s3GKlWtcmknR5nehcAwR%2FOIvKs2vpMifxNrCf%2BQcs9cSwE74ouF21EV8r8lHkYR%2FB2qy1DmpEA2ea8zsiHr4fi8GN2uDmznI74KqU8Z3eOGpahhQvsNl1wea%2FkjRo2VczqPa3b8EYCTZrFdX5%2BlKfrNIHK9TqZWdXo0sr2RvNiXzSII%2FX%2Byp%2FOxo5kGKY25emZ07R3jB9uTc5y3OAOh0UjADewX2AVp0uHlZ8wGJUJyhqmOD7J8p11l%2FpZdFT8YWPPWpOflAkeecYSLUKE877cfLyGK5Fx1M5SgVvgN5KsSegGp07HwTj1u4PjfahBFtU6s1%2FydcYMCpkk2OKzdi%2FUNcojGtAnUatXsevTYcKsEaBViO8WjxKMPm%2Bos4GOqUBtE9gMW38tVQbU9jUKMWdeDKyaA03%2BONu%2BXFBHVbQ%2F1ISgrpsFEV547%2Fdsl0gWjpRPUqrc1KLddwz4l83YZv9X4OHlQQ4mK6NCnvFAQzZ85NTzzQ5eVHHcZ2zeC9scpcW%2BJ%2B%2BunLrrS7jrUKcKAXaehL81Gzl%2B2Mgzt8zcgk0AscyGUDsFhiLlVAShQ198lF129ZUwGJYJcj27MX71Gr7KLR6nUWh&X-Amz-Signature=aa08a87a5de3bcc137ccc9931d54fd86a769f52cbe0bcaeb6dffc24946a9d133&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EHL5X3E%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIFk4Qw94bekW4qj3DirbwrYpKws6RUZ7gpf%2B5UAwwz4tAiEAn8HoRMzXVs26lfvYnN4d9YLfJNw53CtFCl%2FONOFFWUQq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDDXpVLFQXESLsO0%2B2ircA8lDA5WT4PhpPpwKk2tfaktsNr9AVX37kVulsasjAGTURoX5cn1My%2ByIp15lmMEKoa3ep6%2FQT8r%2BANO7orlV8T4jK%2F9YKxUXLwDmnxwEXOqqerIKGCmYup4g6MtdOepky3%2FgC%2Bh%2FEBbkauZTb1%2BFE8rwFAyHgZ2gozz99PZIUruSI4zS05F8k2Rd6hdm6inCV%2BV5kgmmpgfBNONzUvjUjJsr%2Bihtdc2hpKGPDXCDLptvUHEyH6k0joNydQxb%2BJBMh%2ByEtD6s3GKlWtcmknR5nehcAwR%2FOIvKs2vpMifxNrCf%2BQcs9cSwE74ouF21EV8r8lHkYR%2FB2qy1DmpEA2ea8zsiHr4fi8GN2uDmznI74KqU8Z3eOGpahhQvsNl1wea%2FkjRo2VczqPa3b8EYCTZrFdX5%2BlKfrNIHK9TqZWdXo0sr2RvNiXzSII%2FX%2Byp%2FOxo5kGKY25emZ07R3jB9uTc5y3OAOh0UjADewX2AVp0uHlZ8wGJUJyhqmOD7J8p11l%2FpZdFT8YWPPWpOflAkeecYSLUKE877cfLyGK5Fx1M5SgVvgN5KsSegGp07HwTj1u4PjfahBFtU6s1%2FydcYMCpkk2OKzdi%2FUNcojGtAnUatXsevTYcKsEaBViO8WjxKMPm%2Bos4GOqUBtE9gMW38tVQbU9jUKMWdeDKyaA03%2BONu%2BXFBHVbQ%2F1ISgrpsFEV547%2Fdsl0gWjpRPUqrc1KLddwz4l83YZv9X4OHlQQ4mK6NCnvFAQzZ85NTzzQ5eVHHcZ2zeC9scpcW%2BJ%2B%2BunLrrS7jrUKcKAXaehL81Gzl%2B2Mgzt8zcgk0AscyGUDsFhiLlVAShQ198lF129ZUwGJYJcj27MX71Gr7KLR6nUWh&X-Amz-Signature=3d70e61bfd634fcc63d4f961645ebaa1a80820a65cf4f621817564fb08034e1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

