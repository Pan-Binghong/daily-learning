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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EEDKGDH%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIAKnMaCh%2FW6lN1Pml3TYUJuYDV4ObyGHBxODgAieNkILAiA7D6RZ8G%2FyIAKPo6TJGy4Wtxu8XX7zJZXb3eyzYg0ogCr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMT1rb6WiGnPqEUdkmKtwDZUJGZIbOJT%2BBWwgoSpMwltS9GEGspmeW29%2FMRt3l5hWJIzS2z0UFYxEaVwHIfqsqcmGbSbgkqxTCty6r%2Bn0wBaNT3%2BGF5gl19uC3auxJRAPABv%2BISJceY0f8RRcRJD7%2BKvFz1D6aud%2FEUSHrvC0OnFgNoU1tlzsvMcYiL5CPYELcBbEc3DSfdSJwVx3qVcD1wiS24NXPvUKAa5w%2FMYeJlG%2B%2BscL9Rt48ER4GdYaTdxxEM5EwhLl4q9gra5bQbeiCb1BLvp%2FjzM8Zocpq5oe%2BOLgYbWqYA4p9muArRofJN5UqV4Bbhiy5toX0UY47s6tjZeTHIrFCRZI%2Bh16na%2BqHYzGGhVb1EpqgoZNvJlRLPpwDhKFtK9Pfyfs0q5vsF61YlyeBHQ4U%2Fewg3qnTZ%2BM5Ec%2Ff3Cq9dfWEqNs%2B5oD%2FOUc%2BKqpm%2BagVvRu3y8gzhQHFowZtB%2Bmdw8N4JRMR9ggtS2N3fSjeOGicpMzsC9%2FY%2BDVXv4RM0WAHVemlTNfZExEnWrnncWxM0qEKSOcJkmkihKkaep1E%2B5RiZ61bbDnt3GqaN2TH3eab9%2BWqMfllTZw%2FsWJeuzMcBnaLMU6YdLCXNFowXFmp753FLvA9hALljr%2BzTQ0XV2n5HMM2IPswgZyhywY6pgHtzUWHj9cFW98CveWyDP4YcAvQsEhjH7fLhKBYg8pR8Uwja90WWki50nsxKVeP7wpUo9VQV%2F0t58QQIgnO%2BKV3K%2Be9KrrGx%2BUgn1M02vDO0dKGcCcvXuzvgDGcfr3H6XOPnC%2FQC9H7dSFS8eOftSoI%2Biz6HU8H9rVkCr4IqoSjZFM5VhnIlwKL3C11vadm90lbSQZExim%2BityDDULP1shJmRGdkwTo&X-Amz-Signature=adba80849648aa9d2bb386ac880ddbae2b980fbd3182342c800ea7fc47fc9cfd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EEDKGDH%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIAKnMaCh%2FW6lN1Pml3TYUJuYDV4ObyGHBxODgAieNkILAiA7D6RZ8G%2FyIAKPo6TJGy4Wtxu8XX7zJZXb3eyzYg0ogCr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMT1rb6WiGnPqEUdkmKtwDZUJGZIbOJT%2BBWwgoSpMwltS9GEGspmeW29%2FMRt3l5hWJIzS2z0UFYxEaVwHIfqsqcmGbSbgkqxTCty6r%2Bn0wBaNT3%2BGF5gl19uC3auxJRAPABv%2BISJceY0f8RRcRJD7%2BKvFz1D6aud%2FEUSHrvC0OnFgNoU1tlzsvMcYiL5CPYELcBbEc3DSfdSJwVx3qVcD1wiS24NXPvUKAa5w%2FMYeJlG%2B%2BscL9Rt48ER4GdYaTdxxEM5EwhLl4q9gra5bQbeiCb1BLvp%2FjzM8Zocpq5oe%2BOLgYbWqYA4p9muArRofJN5UqV4Bbhiy5toX0UY47s6tjZeTHIrFCRZI%2Bh16na%2BqHYzGGhVb1EpqgoZNvJlRLPpwDhKFtK9Pfyfs0q5vsF61YlyeBHQ4U%2Fewg3qnTZ%2BM5Ec%2Ff3Cq9dfWEqNs%2B5oD%2FOUc%2BKqpm%2BagVvRu3y8gzhQHFowZtB%2Bmdw8N4JRMR9ggtS2N3fSjeOGicpMzsC9%2FY%2BDVXv4RM0WAHVemlTNfZExEnWrnncWxM0qEKSOcJkmkihKkaep1E%2B5RiZ61bbDnt3GqaN2TH3eab9%2BWqMfllTZw%2FsWJeuzMcBnaLMU6YdLCXNFowXFmp753FLvA9hALljr%2BzTQ0XV2n5HMM2IPswgZyhywY6pgHtzUWHj9cFW98CveWyDP4YcAvQsEhjH7fLhKBYg8pR8Uwja90WWki50nsxKVeP7wpUo9VQV%2F0t58QQIgnO%2BKV3K%2Be9KrrGx%2BUgn1M02vDO0dKGcCcvXuzvgDGcfr3H6XOPnC%2FQC9H7dSFS8eOftSoI%2Biz6HU8H9rVkCr4IqoSjZFM5VhnIlwKL3C11vadm90lbSQZExim%2BityDDULP1shJmRGdkwTo&X-Amz-Signature=e7bd50dd670491837cc637ae27012dfcedda6d02e80d6a7dc47e676fb078543e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EEDKGDH%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIAKnMaCh%2FW6lN1Pml3TYUJuYDV4ObyGHBxODgAieNkILAiA7D6RZ8G%2FyIAKPo6TJGy4Wtxu8XX7zJZXb3eyzYg0ogCr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMT1rb6WiGnPqEUdkmKtwDZUJGZIbOJT%2BBWwgoSpMwltS9GEGspmeW29%2FMRt3l5hWJIzS2z0UFYxEaVwHIfqsqcmGbSbgkqxTCty6r%2Bn0wBaNT3%2BGF5gl19uC3auxJRAPABv%2BISJceY0f8RRcRJD7%2BKvFz1D6aud%2FEUSHrvC0OnFgNoU1tlzsvMcYiL5CPYELcBbEc3DSfdSJwVx3qVcD1wiS24NXPvUKAa5w%2FMYeJlG%2B%2BscL9Rt48ER4GdYaTdxxEM5EwhLl4q9gra5bQbeiCb1BLvp%2FjzM8Zocpq5oe%2BOLgYbWqYA4p9muArRofJN5UqV4Bbhiy5toX0UY47s6tjZeTHIrFCRZI%2Bh16na%2BqHYzGGhVb1EpqgoZNvJlRLPpwDhKFtK9Pfyfs0q5vsF61YlyeBHQ4U%2Fewg3qnTZ%2BM5Ec%2Ff3Cq9dfWEqNs%2B5oD%2FOUc%2BKqpm%2BagVvRu3y8gzhQHFowZtB%2Bmdw8N4JRMR9ggtS2N3fSjeOGicpMzsC9%2FY%2BDVXv4RM0WAHVemlTNfZExEnWrnncWxM0qEKSOcJkmkihKkaep1E%2B5RiZ61bbDnt3GqaN2TH3eab9%2BWqMfllTZw%2FsWJeuzMcBnaLMU6YdLCXNFowXFmp753FLvA9hALljr%2BzTQ0XV2n5HMM2IPswgZyhywY6pgHtzUWHj9cFW98CveWyDP4YcAvQsEhjH7fLhKBYg8pR8Uwja90WWki50nsxKVeP7wpUo9VQV%2F0t58QQIgnO%2BKV3K%2Be9KrrGx%2BUgn1M02vDO0dKGcCcvXuzvgDGcfr3H6XOPnC%2FQC9H7dSFS8eOftSoI%2Biz6HU8H9rVkCr4IqoSjZFM5VhnIlwKL3C11vadm90lbSQZExim%2BityDDULP1shJmRGdkwTo&X-Amz-Signature=c61adfee44b17f78d9b691ce3a5e0c22a3e4d59aec0dcc6d842b51e7813918ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EEDKGDH%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIAKnMaCh%2FW6lN1Pml3TYUJuYDV4ObyGHBxODgAieNkILAiA7D6RZ8G%2FyIAKPo6TJGy4Wtxu8XX7zJZXb3eyzYg0ogCr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMT1rb6WiGnPqEUdkmKtwDZUJGZIbOJT%2BBWwgoSpMwltS9GEGspmeW29%2FMRt3l5hWJIzS2z0UFYxEaVwHIfqsqcmGbSbgkqxTCty6r%2Bn0wBaNT3%2BGF5gl19uC3auxJRAPABv%2BISJceY0f8RRcRJD7%2BKvFz1D6aud%2FEUSHrvC0OnFgNoU1tlzsvMcYiL5CPYELcBbEc3DSfdSJwVx3qVcD1wiS24NXPvUKAa5w%2FMYeJlG%2B%2BscL9Rt48ER4GdYaTdxxEM5EwhLl4q9gra5bQbeiCb1BLvp%2FjzM8Zocpq5oe%2BOLgYbWqYA4p9muArRofJN5UqV4Bbhiy5toX0UY47s6tjZeTHIrFCRZI%2Bh16na%2BqHYzGGhVb1EpqgoZNvJlRLPpwDhKFtK9Pfyfs0q5vsF61YlyeBHQ4U%2Fewg3qnTZ%2BM5Ec%2Ff3Cq9dfWEqNs%2B5oD%2FOUc%2BKqpm%2BagVvRu3y8gzhQHFowZtB%2Bmdw8N4JRMR9ggtS2N3fSjeOGicpMzsC9%2FY%2BDVXv4RM0WAHVemlTNfZExEnWrnncWxM0qEKSOcJkmkihKkaep1E%2B5RiZ61bbDnt3GqaN2TH3eab9%2BWqMfllTZw%2FsWJeuzMcBnaLMU6YdLCXNFowXFmp753FLvA9hALljr%2BzTQ0XV2n5HMM2IPswgZyhywY6pgHtzUWHj9cFW98CveWyDP4YcAvQsEhjH7fLhKBYg8pR8Uwja90WWki50nsxKVeP7wpUo9VQV%2F0t58QQIgnO%2BKV3K%2Be9KrrGx%2BUgn1M02vDO0dKGcCcvXuzvgDGcfr3H6XOPnC%2FQC9H7dSFS8eOftSoI%2Biz6HU8H9rVkCr4IqoSjZFM5VhnIlwKL3C11vadm90lbSQZExim%2BityDDULP1shJmRGdkwTo&X-Amz-Signature=bbb4dacf98ea4b3625c2d0233bd5ed7c9a513e14f67926aca46c8bf045694fb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EEDKGDH%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIAKnMaCh%2FW6lN1Pml3TYUJuYDV4ObyGHBxODgAieNkILAiA7D6RZ8G%2FyIAKPo6TJGy4Wtxu8XX7zJZXb3eyzYg0ogCr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMT1rb6WiGnPqEUdkmKtwDZUJGZIbOJT%2BBWwgoSpMwltS9GEGspmeW29%2FMRt3l5hWJIzS2z0UFYxEaVwHIfqsqcmGbSbgkqxTCty6r%2Bn0wBaNT3%2BGF5gl19uC3auxJRAPABv%2BISJceY0f8RRcRJD7%2BKvFz1D6aud%2FEUSHrvC0OnFgNoU1tlzsvMcYiL5CPYELcBbEc3DSfdSJwVx3qVcD1wiS24NXPvUKAa5w%2FMYeJlG%2B%2BscL9Rt48ER4GdYaTdxxEM5EwhLl4q9gra5bQbeiCb1BLvp%2FjzM8Zocpq5oe%2BOLgYbWqYA4p9muArRofJN5UqV4Bbhiy5toX0UY47s6tjZeTHIrFCRZI%2Bh16na%2BqHYzGGhVb1EpqgoZNvJlRLPpwDhKFtK9Pfyfs0q5vsF61YlyeBHQ4U%2Fewg3qnTZ%2BM5Ec%2Ff3Cq9dfWEqNs%2B5oD%2FOUc%2BKqpm%2BagVvRu3y8gzhQHFowZtB%2Bmdw8N4JRMR9ggtS2N3fSjeOGicpMzsC9%2FY%2BDVXv4RM0WAHVemlTNfZExEnWrnncWxM0qEKSOcJkmkihKkaep1E%2B5RiZ61bbDnt3GqaN2TH3eab9%2BWqMfllTZw%2FsWJeuzMcBnaLMU6YdLCXNFowXFmp753FLvA9hALljr%2BzTQ0XV2n5HMM2IPswgZyhywY6pgHtzUWHj9cFW98CveWyDP4YcAvQsEhjH7fLhKBYg8pR8Uwja90WWki50nsxKVeP7wpUo9VQV%2F0t58QQIgnO%2BKV3K%2Be9KrrGx%2BUgn1M02vDO0dKGcCcvXuzvgDGcfr3H6XOPnC%2FQC9H7dSFS8eOftSoI%2Biz6HU8H9rVkCr4IqoSjZFM5VhnIlwKL3C11vadm90lbSQZExim%2BityDDULP1shJmRGdkwTo&X-Amz-Signature=f7bb914eca00c4e7ff9bbdfc99d77cca59c1ef4ca3e8c2c341997126f2ba6bc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EEDKGDH%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIAKnMaCh%2FW6lN1Pml3TYUJuYDV4ObyGHBxODgAieNkILAiA7D6RZ8G%2FyIAKPo6TJGy4Wtxu8XX7zJZXb3eyzYg0ogCr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMT1rb6WiGnPqEUdkmKtwDZUJGZIbOJT%2BBWwgoSpMwltS9GEGspmeW29%2FMRt3l5hWJIzS2z0UFYxEaVwHIfqsqcmGbSbgkqxTCty6r%2Bn0wBaNT3%2BGF5gl19uC3auxJRAPABv%2BISJceY0f8RRcRJD7%2BKvFz1D6aud%2FEUSHrvC0OnFgNoU1tlzsvMcYiL5CPYELcBbEc3DSfdSJwVx3qVcD1wiS24NXPvUKAa5w%2FMYeJlG%2B%2BscL9Rt48ER4GdYaTdxxEM5EwhLl4q9gra5bQbeiCb1BLvp%2FjzM8Zocpq5oe%2BOLgYbWqYA4p9muArRofJN5UqV4Bbhiy5toX0UY47s6tjZeTHIrFCRZI%2Bh16na%2BqHYzGGhVb1EpqgoZNvJlRLPpwDhKFtK9Pfyfs0q5vsF61YlyeBHQ4U%2Fewg3qnTZ%2BM5Ec%2Ff3Cq9dfWEqNs%2B5oD%2FOUc%2BKqpm%2BagVvRu3y8gzhQHFowZtB%2Bmdw8N4JRMR9ggtS2N3fSjeOGicpMzsC9%2FY%2BDVXv4RM0WAHVemlTNfZExEnWrnncWxM0qEKSOcJkmkihKkaep1E%2B5RiZ61bbDnt3GqaN2TH3eab9%2BWqMfllTZw%2FsWJeuzMcBnaLMU6YdLCXNFowXFmp753FLvA9hALljr%2BzTQ0XV2n5HMM2IPswgZyhywY6pgHtzUWHj9cFW98CveWyDP4YcAvQsEhjH7fLhKBYg8pR8Uwja90WWki50nsxKVeP7wpUo9VQV%2F0t58QQIgnO%2BKV3K%2Be9KrrGx%2BUgn1M02vDO0dKGcCcvXuzvgDGcfr3H6XOPnC%2FQC9H7dSFS8eOftSoI%2Biz6HU8H9rVkCr4IqoSjZFM5VhnIlwKL3C11vadm90lbSQZExim%2BityDDULP1shJmRGdkwTo&X-Amz-Signature=82de3dd30126019300b6f818b31aa997bf547ea2d28c59b991597a34acb3aefb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EEDKGDH%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIAKnMaCh%2FW6lN1Pml3TYUJuYDV4ObyGHBxODgAieNkILAiA7D6RZ8G%2FyIAKPo6TJGy4Wtxu8XX7zJZXb3eyzYg0ogCr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMT1rb6WiGnPqEUdkmKtwDZUJGZIbOJT%2BBWwgoSpMwltS9GEGspmeW29%2FMRt3l5hWJIzS2z0UFYxEaVwHIfqsqcmGbSbgkqxTCty6r%2Bn0wBaNT3%2BGF5gl19uC3auxJRAPABv%2BISJceY0f8RRcRJD7%2BKvFz1D6aud%2FEUSHrvC0OnFgNoU1tlzsvMcYiL5CPYELcBbEc3DSfdSJwVx3qVcD1wiS24NXPvUKAa5w%2FMYeJlG%2B%2BscL9Rt48ER4GdYaTdxxEM5EwhLl4q9gra5bQbeiCb1BLvp%2FjzM8Zocpq5oe%2BOLgYbWqYA4p9muArRofJN5UqV4Bbhiy5toX0UY47s6tjZeTHIrFCRZI%2Bh16na%2BqHYzGGhVb1EpqgoZNvJlRLPpwDhKFtK9Pfyfs0q5vsF61YlyeBHQ4U%2Fewg3qnTZ%2BM5Ec%2Ff3Cq9dfWEqNs%2B5oD%2FOUc%2BKqpm%2BagVvRu3y8gzhQHFowZtB%2Bmdw8N4JRMR9ggtS2N3fSjeOGicpMzsC9%2FY%2BDVXv4RM0WAHVemlTNfZExEnWrnncWxM0qEKSOcJkmkihKkaep1E%2B5RiZ61bbDnt3GqaN2TH3eab9%2BWqMfllTZw%2FsWJeuzMcBnaLMU6YdLCXNFowXFmp753FLvA9hALljr%2BzTQ0XV2n5HMM2IPswgZyhywY6pgHtzUWHj9cFW98CveWyDP4YcAvQsEhjH7fLhKBYg8pR8Uwja90WWki50nsxKVeP7wpUo9VQV%2F0t58QQIgnO%2BKV3K%2Be9KrrGx%2BUgn1M02vDO0dKGcCcvXuzvgDGcfr3H6XOPnC%2FQC9H7dSFS8eOftSoI%2Biz6HU8H9rVkCr4IqoSjZFM5VhnIlwKL3C11vadm90lbSQZExim%2BityDDULP1shJmRGdkwTo&X-Amz-Signature=69844dae67dde5020dc53f7e0af4fa71883a05852af04a47fda4263695962465&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

