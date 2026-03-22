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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLCUIWEO%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGL0kdwNPY0OvIWH9OjnFNYGBzYKxd4Fn4TdLypBhi5DAiEA%2FpU%2FNmPRUlZoWzibI3MQ%2BmhzV68dsUTnk%2FvtWWgoukIq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDPmviTqQj6wjlUps1SrcAxod0fjbQT6qBXmicajbx8XzVHpmJQoVZZqJ%2BxG7u%2BX1cFouQRJz8lDgUXV2mygf8RTiBkBtifs6yRAUm7d85A%2BdPrgpd4fo3Zgu4DZyVv8oS43RsUfjbMM982Q8%2FEb0fJT43kfTUaLWtUb7goUq7Ty8LvTecnZ%2BiYvngcTjG4IDrfb3Ad%2FWf3f7Z3Nrc7Q25p9J2TBIutPjYCqWy9eMCL9mMAkRGMqSU02SzCLJjjc%2BtO4nhErZYcIXhVmLu6cMhJWoIc5hpzUSfGzfYMjjNu2X%2BH6b1HtYXlpCxzni9pN3JN%2FwgcQtrZqQwOVg1cLG4uDNKyjIe1Rfe6s8Dna1lEQA8RomSQUkQxGcMcnnzed%2BQoACSUrz247%2BCJr9PKFQ7pPxCdzs43bqUgDgJVT3tyRwJAyZ%2B%2BwNBYyT5jen5IsuhbsCPQFnpAzrKAGcYGSYS3P%2BQ1fR8Ddo2wDFiuNdthMRQ%2Fi56I8fO0oZJId%2FP3yyycWuTMjzzUZlLawQthVvKtZnSo42LnwjCPpXMYZKSUulQS6Q3Qa8fTOkHk1sJO425hThsT449BTL%2BS35BtO3LvUeBnmTy8ayf3uhOjh57Fj%2BrtjqHuBbj9AlDPraGf%2BaOZP1T5GY73ogyXiVMKus%2Fc0GOqUBLzJcFKTSwh%2F1tValBNDrLUHf90Hxqsf6TK3A%2BtNnZtIvGGuQnuVh123dH6mBaQ9kl7Pgf7cX2k0PGylRgx2EpPFKkJM19XzUXWV2Q%2FRB6%2BlO%2BlMNvmBiI9ME6Q4JYIkm8Z4yppARTUvF0VTMMrr259sh3O6H5kAqf6T0dDJIXZR8nCoZor7PWzLwFRfhA5A0qePuKzRt%2FI7ablGNRILtcP27EhcS&X-Amz-Signature=14b6afed8de8ee9c25f5762e50486137838e8a092bdc4e12ff316eb9a8687313&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLCUIWEO%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGL0kdwNPY0OvIWH9OjnFNYGBzYKxd4Fn4TdLypBhi5DAiEA%2FpU%2FNmPRUlZoWzibI3MQ%2BmhzV68dsUTnk%2FvtWWgoukIq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDPmviTqQj6wjlUps1SrcAxod0fjbQT6qBXmicajbx8XzVHpmJQoVZZqJ%2BxG7u%2BX1cFouQRJz8lDgUXV2mygf8RTiBkBtifs6yRAUm7d85A%2BdPrgpd4fo3Zgu4DZyVv8oS43RsUfjbMM982Q8%2FEb0fJT43kfTUaLWtUb7goUq7Ty8LvTecnZ%2BiYvngcTjG4IDrfb3Ad%2FWf3f7Z3Nrc7Q25p9J2TBIutPjYCqWy9eMCL9mMAkRGMqSU02SzCLJjjc%2BtO4nhErZYcIXhVmLu6cMhJWoIc5hpzUSfGzfYMjjNu2X%2BH6b1HtYXlpCxzni9pN3JN%2FwgcQtrZqQwOVg1cLG4uDNKyjIe1Rfe6s8Dna1lEQA8RomSQUkQxGcMcnnzed%2BQoACSUrz247%2BCJr9PKFQ7pPxCdzs43bqUgDgJVT3tyRwJAyZ%2B%2BwNBYyT5jen5IsuhbsCPQFnpAzrKAGcYGSYS3P%2BQ1fR8Ddo2wDFiuNdthMRQ%2Fi56I8fO0oZJId%2FP3yyycWuTMjzzUZlLawQthVvKtZnSo42LnwjCPpXMYZKSUulQS6Q3Qa8fTOkHk1sJO425hThsT449BTL%2BS35BtO3LvUeBnmTy8ayf3uhOjh57Fj%2BrtjqHuBbj9AlDPraGf%2BaOZP1T5GY73ogyXiVMKus%2Fc0GOqUBLzJcFKTSwh%2F1tValBNDrLUHf90Hxqsf6TK3A%2BtNnZtIvGGuQnuVh123dH6mBaQ9kl7Pgf7cX2k0PGylRgx2EpPFKkJM19XzUXWV2Q%2FRB6%2BlO%2BlMNvmBiI9ME6Q4JYIkm8Z4yppARTUvF0VTMMrr259sh3O6H5kAqf6T0dDJIXZR8nCoZor7PWzLwFRfhA5A0qePuKzRt%2FI7ablGNRILtcP27EhcS&X-Amz-Signature=b013584a35f58eef4f57d3b8f019625ed3a5b2dc6c47c254e76430195dcfa628&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLCUIWEO%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGL0kdwNPY0OvIWH9OjnFNYGBzYKxd4Fn4TdLypBhi5DAiEA%2FpU%2FNmPRUlZoWzibI3MQ%2BmhzV68dsUTnk%2FvtWWgoukIq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDPmviTqQj6wjlUps1SrcAxod0fjbQT6qBXmicajbx8XzVHpmJQoVZZqJ%2BxG7u%2BX1cFouQRJz8lDgUXV2mygf8RTiBkBtifs6yRAUm7d85A%2BdPrgpd4fo3Zgu4DZyVv8oS43RsUfjbMM982Q8%2FEb0fJT43kfTUaLWtUb7goUq7Ty8LvTecnZ%2BiYvngcTjG4IDrfb3Ad%2FWf3f7Z3Nrc7Q25p9J2TBIutPjYCqWy9eMCL9mMAkRGMqSU02SzCLJjjc%2BtO4nhErZYcIXhVmLu6cMhJWoIc5hpzUSfGzfYMjjNu2X%2BH6b1HtYXlpCxzni9pN3JN%2FwgcQtrZqQwOVg1cLG4uDNKyjIe1Rfe6s8Dna1lEQA8RomSQUkQxGcMcnnzed%2BQoACSUrz247%2BCJr9PKFQ7pPxCdzs43bqUgDgJVT3tyRwJAyZ%2B%2BwNBYyT5jen5IsuhbsCPQFnpAzrKAGcYGSYS3P%2BQ1fR8Ddo2wDFiuNdthMRQ%2Fi56I8fO0oZJId%2FP3yyycWuTMjzzUZlLawQthVvKtZnSo42LnwjCPpXMYZKSUulQS6Q3Qa8fTOkHk1sJO425hThsT449BTL%2BS35BtO3LvUeBnmTy8ayf3uhOjh57Fj%2BrtjqHuBbj9AlDPraGf%2BaOZP1T5GY73ogyXiVMKus%2Fc0GOqUBLzJcFKTSwh%2F1tValBNDrLUHf90Hxqsf6TK3A%2BtNnZtIvGGuQnuVh123dH6mBaQ9kl7Pgf7cX2k0PGylRgx2EpPFKkJM19XzUXWV2Q%2FRB6%2BlO%2BlMNvmBiI9ME6Q4JYIkm8Z4yppARTUvF0VTMMrr259sh3O6H5kAqf6T0dDJIXZR8nCoZor7PWzLwFRfhA5A0qePuKzRt%2FI7ablGNRILtcP27EhcS&X-Amz-Signature=090b6ffd4c31689a5d67b651a9943fbc885743987c937ae48d6f7e13cefc8db8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLCUIWEO%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGL0kdwNPY0OvIWH9OjnFNYGBzYKxd4Fn4TdLypBhi5DAiEA%2FpU%2FNmPRUlZoWzibI3MQ%2BmhzV68dsUTnk%2FvtWWgoukIq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDPmviTqQj6wjlUps1SrcAxod0fjbQT6qBXmicajbx8XzVHpmJQoVZZqJ%2BxG7u%2BX1cFouQRJz8lDgUXV2mygf8RTiBkBtifs6yRAUm7d85A%2BdPrgpd4fo3Zgu4DZyVv8oS43RsUfjbMM982Q8%2FEb0fJT43kfTUaLWtUb7goUq7Ty8LvTecnZ%2BiYvngcTjG4IDrfb3Ad%2FWf3f7Z3Nrc7Q25p9J2TBIutPjYCqWy9eMCL9mMAkRGMqSU02SzCLJjjc%2BtO4nhErZYcIXhVmLu6cMhJWoIc5hpzUSfGzfYMjjNu2X%2BH6b1HtYXlpCxzni9pN3JN%2FwgcQtrZqQwOVg1cLG4uDNKyjIe1Rfe6s8Dna1lEQA8RomSQUkQxGcMcnnzed%2BQoACSUrz247%2BCJr9PKFQ7pPxCdzs43bqUgDgJVT3tyRwJAyZ%2B%2BwNBYyT5jen5IsuhbsCPQFnpAzrKAGcYGSYS3P%2BQ1fR8Ddo2wDFiuNdthMRQ%2Fi56I8fO0oZJId%2FP3yyycWuTMjzzUZlLawQthVvKtZnSo42LnwjCPpXMYZKSUulQS6Q3Qa8fTOkHk1sJO425hThsT449BTL%2BS35BtO3LvUeBnmTy8ayf3uhOjh57Fj%2BrtjqHuBbj9AlDPraGf%2BaOZP1T5GY73ogyXiVMKus%2Fc0GOqUBLzJcFKTSwh%2F1tValBNDrLUHf90Hxqsf6TK3A%2BtNnZtIvGGuQnuVh123dH6mBaQ9kl7Pgf7cX2k0PGylRgx2EpPFKkJM19XzUXWV2Q%2FRB6%2BlO%2BlMNvmBiI9ME6Q4JYIkm8Z4yppARTUvF0VTMMrr259sh3O6H5kAqf6T0dDJIXZR8nCoZor7PWzLwFRfhA5A0qePuKzRt%2FI7ablGNRILtcP27EhcS&X-Amz-Signature=c4387ef2e966946ea45625521eeeca00a8eb166ae31004736f2d4e6faf90a8d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLCUIWEO%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGL0kdwNPY0OvIWH9OjnFNYGBzYKxd4Fn4TdLypBhi5DAiEA%2FpU%2FNmPRUlZoWzibI3MQ%2BmhzV68dsUTnk%2FvtWWgoukIq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDPmviTqQj6wjlUps1SrcAxod0fjbQT6qBXmicajbx8XzVHpmJQoVZZqJ%2BxG7u%2BX1cFouQRJz8lDgUXV2mygf8RTiBkBtifs6yRAUm7d85A%2BdPrgpd4fo3Zgu4DZyVv8oS43RsUfjbMM982Q8%2FEb0fJT43kfTUaLWtUb7goUq7Ty8LvTecnZ%2BiYvngcTjG4IDrfb3Ad%2FWf3f7Z3Nrc7Q25p9J2TBIutPjYCqWy9eMCL9mMAkRGMqSU02SzCLJjjc%2BtO4nhErZYcIXhVmLu6cMhJWoIc5hpzUSfGzfYMjjNu2X%2BH6b1HtYXlpCxzni9pN3JN%2FwgcQtrZqQwOVg1cLG4uDNKyjIe1Rfe6s8Dna1lEQA8RomSQUkQxGcMcnnzed%2BQoACSUrz247%2BCJr9PKFQ7pPxCdzs43bqUgDgJVT3tyRwJAyZ%2B%2BwNBYyT5jen5IsuhbsCPQFnpAzrKAGcYGSYS3P%2BQ1fR8Ddo2wDFiuNdthMRQ%2Fi56I8fO0oZJId%2FP3yyycWuTMjzzUZlLawQthVvKtZnSo42LnwjCPpXMYZKSUulQS6Q3Qa8fTOkHk1sJO425hThsT449BTL%2BS35BtO3LvUeBnmTy8ayf3uhOjh57Fj%2BrtjqHuBbj9AlDPraGf%2BaOZP1T5GY73ogyXiVMKus%2Fc0GOqUBLzJcFKTSwh%2F1tValBNDrLUHf90Hxqsf6TK3A%2BtNnZtIvGGuQnuVh123dH6mBaQ9kl7Pgf7cX2k0PGylRgx2EpPFKkJM19XzUXWV2Q%2FRB6%2BlO%2BlMNvmBiI9ME6Q4JYIkm8Z4yppARTUvF0VTMMrr259sh3O6H5kAqf6T0dDJIXZR8nCoZor7PWzLwFRfhA5A0qePuKzRt%2FI7ablGNRILtcP27EhcS&X-Amz-Signature=6e8fc78a58b33095a7f8e639516209ca5583b48eeb55f0321218a7a764d2c2cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLCUIWEO%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGL0kdwNPY0OvIWH9OjnFNYGBzYKxd4Fn4TdLypBhi5DAiEA%2FpU%2FNmPRUlZoWzibI3MQ%2BmhzV68dsUTnk%2FvtWWgoukIq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDPmviTqQj6wjlUps1SrcAxod0fjbQT6qBXmicajbx8XzVHpmJQoVZZqJ%2BxG7u%2BX1cFouQRJz8lDgUXV2mygf8RTiBkBtifs6yRAUm7d85A%2BdPrgpd4fo3Zgu4DZyVv8oS43RsUfjbMM982Q8%2FEb0fJT43kfTUaLWtUb7goUq7Ty8LvTecnZ%2BiYvngcTjG4IDrfb3Ad%2FWf3f7Z3Nrc7Q25p9J2TBIutPjYCqWy9eMCL9mMAkRGMqSU02SzCLJjjc%2BtO4nhErZYcIXhVmLu6cMhJWoIc5hpzUSfGzfYMjjNu2X%2BH6b1HtYXlpCxzni9pN3JN%2FwgcQtrZqQwOVg1cLG4uDNKyjIe1Rfe6s8Dna1lEQA8RomSQUkQxGcMcnnzed%2BQoACSUrz247%2BCJr9PKFQ7pPxCdzs43bqUgDgJVT3tyRwJAyZ%2B%2BwNBYyT5jen5IsuhbsCPQFnpAzrKAGcYGSYS3P%2BQ1fR8Ddo2wDFiuNdthMRQ%2Fi56I8fO0oZJId%2FP3yyycWuTMjzzUZlLawQthVvKtZnSo42LnwjCPpXMYZKSUulQS6Q3Qa8fTOkHk1sJO425hThsT449BTL%2BS35BtO3LvUeBnmTy8ayf3uhOjh57Fj%2BrtjqHuBbj9AlDPraGf%2BaOZP1T5GY73ogyXiVMKus%2Fc0GOqUBLzJcFKTSwh%2F1tValBNDrLUHf90Hxqsf6TK3A%2BtNnZtIvGGuQnuVh123dH6mBaQ9kl7Pgf7cX2k0PGylRgx2EpPFKkJM19XzUXWV2Q%2FRB6%2BlO%2BlMNvmBiI9ME6Q4JYIkm8Z4yppARTUvF0VTMMrr259sh3O6H5kAqf6T0dDJIXZR8nCoZor7PWzLwFRfhA5A0qePuKzRt%2FI7ablGNRILtcP27EhcS&X-Amz-Signature=fc8a7c921a96c0856f0070da29ee9258828b3ce44e758f6fc71adc7a04c291aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLCUIWEO%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGL0kdwNPY0OvIWH9OjnFNYGBzYKxd4Fn4TdLypBhi5DAiEA%2FpU%2FNmPRUlZoWzibI3MQ%2BmhzV68dsUTnk%2FvtWWgoukIq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDPmviTqQj6wjlUps1SrcAxod0fjbQT6qBXmicajbx8XzVHpmJQoVZZqJ%2BxG7u%2BX1cFouQRJz8lDgUXV2mygf8RTiBkBtifs6yRAUm7d85A%2BdPrgpd4fo3Zgu4DZyVv8oS43RsUfjbMM982Q8%2FEb0fJT43kfTUaLWtUb7goUq7Ty8LvTecnZ%2BiYvngcTjG4IDrfb3Ad%2FWf3f7Z3Nrc7Q25p9J2TBIutPjYCqWy9eMCL9mMAkRGMqSU02SzCLJjjc%2BtO4nhErZYcIXhVmLu6cMhJWoIc5hpzUSfGzfYMjjNu2X%2BH6b1HtYXlpCxzni9pN3JN%2FwgcQtrZqQwOVg1cLG4uDNKyjIe1Rfe6s8Dna1lEQA8RomSQUkQxGcMcnnzed%2BQoACSUrz247%2BCJr9PKFQ7pPxCdzs43bqUgDgJVT3tyRwJAyZ%2B%2BwNBYyT5jen5IsuhbsCPQFnpAzrKAGcYGSYS3P%2BQ1fR8Ddo2wDFiuNdthMRQ%2Fi56I8fO0oZJId%2FP3yyycWuTMjzzUZlLawQthVvKtZnSo42LnwjCPpXMYZKSUulQS6Q3Qa8fTOkHk1sJO425hThsT449BTL%2BS35BtO3LvUeBnmTy8ayf3uhOjh57Fj%2BrtjqHuBbj9AlDPraGf%2BaOZP1T5GY73ogyXiVMKus%2Fc0GOqUBLzJcFKTSwh%2F1tValBNDrLUHf90Hxqsf6TK3A%2BtNnZtIvGGuQnuVh123dH6mBaQ9kl7Pgf7cX2k0PGylRgx2EpPFKkJM19XzUXWV2Q%2FRB6%2BlO%2BlMNvmBiI9ME6Q4JYIkm8Z4yppARTUvF0VTMMrr259sh3O6H5kAqf6T0dDJIXZR8nCoZor7PWzLwFRfhA5A0qePuKzRt%2FI7ablGNRILtcP27EhcS&X-Amz-Signature=73a60a125d06e7512ff5c4d0bc60a8f390dc96a4e4f45a3f06aaa5c6da830d42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

