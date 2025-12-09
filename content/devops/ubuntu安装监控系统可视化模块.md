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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEYQ2TTZ%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqzPeMm08Noxd38GMWlsuFnP2z24fmXYDmQnwPTjmykwIhAMmTko5zfXqqA1jrsAoavYSsXCZ5v%2Fw%2Bhoz6PfEzse8mKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzRMLwMQJxs8CzrphYq3AMgNl1dxG9ne6joqhGc%2F%2BqAYd%2BGHnZTPvvORlZjHknj26DTNij8Zk7QY%2BZw%2B6xPQjPRxq8sIM5LSXtSVorLBeXsr9tRLzu%2F00gp024LEj2cPkaVl3tIB7sNBBHb4jQ0KaMAUsu0lWxpDhzEFdAXWgiPSGZXxi4uL80HVIpyIJHNEGqv7hZS45g88Xgcz8pjbSo9VP%2B0xMRQeMvw06m6%2FkD9SP4c9ThpNeP6O534voJ1%2FdO7xxrPqYRANb9FWk00lO1AMjr1OK9xPZQT%2FvaQzhlUY8DUw6f%2F5J11s79GWTWzSOlnWVJ5pCz%2F4aULXmMkt3EKdbOWRB3K%2BIgyz0AZBo6wPXjHWTggZNinWk6xC7iR9573ma3oJ4dw39nQQU8jxhSN3nomwLAQkmsIUqFujTSayO18nv52C0TTMjX7OPQ5xRCyF14UNDCgVVzpceo1z4g%2FQC%2FFGd4Hao6vOQi6aMjAH5AxkLafCBVQV8%2BX8apUQrB2OmS1O2NOsFrDrfas4DlImNJ%2BDks6ga35iqLPFu%2FqZW79zzsTDblw6qeN5na039tSyMFJWV1KRS%2FzUC%2BjOGMgNS%2FDsvUKRwWv9EHdtp3es8C2XP4zMDDJP%2FHo06A4T4ocssFxhxyRs1YSdTDDkN7JBjqkARkj0YMCCDnwQD6e7QysqHlggs7AyLibKPSWOGayer%2FL4lV9jjqPiupyxuRe3MTJimXGxH8l8nU8gCC%2BgyosK1jjdI%2FzdWMKhAelzOGm9FD2BmAZIG9TnPcTRB2Uypo5to10ricXrPiVLfpPyPMQuIX76JA7DIhnyS0JC619Kxjwv5ecZPloeEmZxeKK31rCAfXsUWddah%2BNfmREv6MtrwjIu1uN&X-Amz-Signature=0a112f3b38dde06c33842b175a88ad1724f231658c1f0ffd5e42fa3011132aa6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEYQ2TTZ%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqzPeMm08Noxd38GMWlsuFnP2z24fmXYDmQnwPTjmykwIhAMmTko5zfXqqA1jrsAoavYSsXCZ5v%2Fw%2Bhoz6PfEzse8mKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzRMLwMQJxs8CzrphYq3AMgNl1dxG9ne6joqhGc%2F%2BqAYd%2BGHnZTPvvORlZjHknj26DTNij8Zk7QY%2BZw%2B6xPQjPRxq8sIM5LSXtSVorLBeXsr9tRLzu%2F00gp024LEj2cPkaVl3tIB7sNBBHb4jQ0KaMAUsu0lWxpDhzEFdAXWgiPSGZXxi4uL80HVIpyIJHNEGqv7hZS45g88Xgcz8pjbSo9VP%2B0xMRQeMvw06m6%2FkD9SP4c9ThpNeP6O534voJ1%2FdO7xxrPqYRANb9FWk00lO1AMjr1OK9xPZQT%2FvaQzhlUY8DUw6f%2F5J11s79GWTWzSOlnWVJ5pCz%2F4aULXmMkt3EKdbOWRB3K%2BIgyz0AZBo6wPXjHWTggZNinWk6xC7iR9573ma3oJ4dw39nQQU8jxhSN3nomwLAQkmsIUqFujTSayO18nv52C0TTMjX7OPQ5xRCyF14UNDCgVVzpceo1z4g%2FQC%2FFGd4Hao6vOQi6aMjAH5AxkLafCBVQV8%2BX8apUQrB2OmS1O2NOsFrDrfas4DlImNJ%2BDks6ga35iqLPFu%2FqZW79zzsTDblw6qeN5na039tSyMFJWV1KRS%2FzUC%2BjOGMgNS%2FDsvUKRwWv9EHdtp3es8C2XP4zMDDJP%2FHo06A4T4ocssFxhxyRs1YSdTDDkN7JBjqkARkj0YMCCDnwQD6e7QysqHlggs7AyLibKPSWOGayer%2FL4lV9jjqPiupyxuRe3MTJimXGxH8l8nU8gCC%2BgyosK1jjdI%2FzdWMKhAelzOGm9FD2BmAZIG9TnPcTRB2Uypo5to10ricXrPiVLfpPyPMQuIX76JA7DIhnyS0JC619Kxjwv5ecZPloeEmZxeKK31rCAfXsUWddah%2BNfmREv6MtrwjIu1uN&X-Amz-Signature=d6256ecaae8c5d506adc64c96943f67456d3358fe676a41e337f2106d749eaaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEYQ2TTZ%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqzPeMm08Noxd38GMWlsuFnP2z24fmXYDmQnwPTjmykwIhAMmTko5zfXqqA1jrsAoavYSsXCZ5v%2Fw%2Bhoz6PfEzse8mKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzRMLwMQJxs8CzrphYq3AMgNl1dxG9ne6joqhGc%2F%2BqAYd%2BGHnZTPvvORlZjHknj26DTNij8Zk7QY%2BZw%2B6xPQjPRxq8sIM5LSXtSVorLBeXsr9tRLzu%2F00gp024LEj2cPkaVl3tIB7sNBBHb4jQ0KaMAUsu0lWxpDhzEFdAXWgiPSGZXxi4uL80HVIpyIJHNEGqv7hZS45g88Xgcz8pjbSo9VP%2B0xMRQeMvw06m6%2FkD9SP4c9ThpNeP6O534voJ1%2FdO7xxrPqYRANb9FWk00lO1AMjr1OK9xPZQT%2FvaQzhlUY8DUw6f%2F5J11s79GWTWzSOlnWVJ5pCz%2F4aULXmMkt3EKdbOWRB3K%2BIgyz0AZBo6wPXjHWTggZNinWk6xC7iR9573ma3oJ4dw39nQQU8jxhSN3nomwLAQkmsIUqFujTSayO18nv52C0TTMjX7OPQ5xRCyF14UNDCgVVzpceo1z4g%2FQC%2FFGd4Hao6vOQi6aMjAH5AxkLafCBVQV8%2BX8apUQrB2OmS1O2NOsFrDrfas4DlImNJ%2BDks6ga35iqLPFu%2FqZW79zzsTDblw6qeN5na039tSyMFJWV1KRS%2FzUC%2BjOGMgNS%2FDsvUKRwWv9EHdtp3es8C2XP4zMDDJP%2FHo06A4T4ocssFxhxyRs1YSdTDDkN7JBjqkARkj0YMCCDnwQD6e7QysqHlggs7AyLibKPSWOGayer%2FL4lV9jjqPiupyxuRe3MTJimXGxH8l8nU8gCC%2BgyosK1jjdI%2FzdWMKhAelzOGm9FD2BmAZIG9TnPcTRB2Uypo5to10ricXrPiVLfpPyPMQuIX76JA7DIhnyS0JC619Kxjwv5ecZPloeEmZxeKK31rCAfXsUWddah%2BNfmREv6MtrwjIu1uN&X-Amz-Signature=b9c9a6c2f5158e947a7d857d7d4b2714790a7b339b5b67adef3d0df1d044a1ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEYQ2TTZ%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqzPeMm08Noxd38GMWlsuFnP2z24fmXYDmQnwPTjmykwIhAMmTko5zfXqqA1jrsAoavYSsXCZ5v%2Fw%2Bhoz6PfEzse8mKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzRMLwMQJxs8CzrphYq3AMgNl1dxG9ne6joqhGc%2F%2BqAYd%2BGHnZTPvvORlZjHknj26DTNij8Zk7QY%2BZw%2B6xPQjPRxq8sIM5LSXtSVorLBeXsr9tRLzu%2F00gp024LEj2cPkaVl3tIB7sNBBHb4jQ0KaMAUsu0lWxpDhzEFdAXWgiPSGZXxi4uL80HVIpyIJHNEGqv7hZS45g88Xgcz8pjbSo9VP%2B0xMRQeMvw06m6%2FkD9SP4c9ThpNeP6O534voJ1%2FdO7xxrPqYRANb9FWk00lO1AMjr1OK9xPZQT%2FvaQzhlUY8DUw6f%2F5J11s79GWTWzSOlnWVJ5pCz%2F4aULXmMkt3EKdbOWRB3K%2BIgyz0AZBo6wPXjHWTggZNinWk6xC7iR9573ma3oJ4dw39nQQU8jxhSN3nomwLAQkmsIUqFujTSayO18nv52C0TTMjX7OPQ5xRCyF14UNDCgVVzpceo1z4g%2FQC%2FFGd4Hao6vOQi6aMjAH5AxkLafCBVQV8%2BX8apUQrB2OmS1O2NOsFrDrfas4DlImNJ%2BDks6ga35iqLPFu%2FqZW79zzsTDblw6qeN5na039tSyMFJWV1KRS%2FzUC%2BjOGMgNS%2FDsvUKRwWv9EHdtp3es8C2XP4zMDDJP%2FHo06A4T4ocssFxhxyRs1YSdTDDkN7JBjqkARkj0YMCCDnwQD6e7QysqHlggs7AyLibKPSWOGayer%2FL4lV9jjqPiupyxuRe3MTJimXGxH8l8nU8gCC%2BgyosK1jjdI%2FzdWMKhAelzOGm9FD2BmAZIG9TnPcTRB2Uypo5to10ricXrPiVLfpPyPMQuIX76JA7DIhnyS0JC619Kxjwv5ecZPloeEmZxeKK31rCAfXsUWddah%2BNfmREv6MtrwjIu1uN&X-Amz-Signature=3de8cd815a6d351b9e9c2f77513f88834db81cc594c6f9619d585879e93f5135&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEYQ2TTZ%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqzPeMm08Noxd38GMWlsuFnP2z24fmXYDmQnwPTjmykwIhAMmTko5zfXqqA1jrsAoavYSsXCZ5v%2Fw%2Bhoz6PfEzse8mKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzRMLwMQJxs8CzrphYq3AMgNl1dxG9ne6joqhGc%2F%2BqAYd%2BGHnZTPvvORlZjHknj26DTNij8Zk7QY%2BZw%2B6xPQjPRxq8sIM5LSXtSVorLBeXsr9tRLzu%2F00gp024LEj2cPkaVl3tIB7sNBBHb4jQ0KaMAUsu0lWxpDhzEFdAXWgiPSGZXxi4uL80HVIpyIJHNEGqv7hZS45g88Xgcz8pjbSo9VP%2B0xMRQeMvw06m6%2FkD9SP4c9ThpNeP6O534voJ1%2FdO7xxrPqYRANb9FWk00lO1AMjr1OK9xPZQT%2FvaQzhlUY8DUw6f%2F5J11s79GWTWzSOlnWVJ5pCz%2F4aULXmMkt3EKdbOWRB3K%2BIgyz0AZBo6wPXjHWTggZNinWk6xC7iR9573ma3oJ4dw39nQQU8jxhSN3nomwLAQkmsIUqFujTSayO18nv52C0TTMjX7OPQ5xRCyF14UNDCgVVzpceo1z4g%2FQC%2FFGd4Hao6vOQi6aMjAH5AxkLafCBVQV8%2BX8apUQrB2OmS1O2NOsFrDrfas4DlImNJ%2BDks6ga35iqLPFu%2FqZW79zzsTDblw6qeN5na039tSyMFJWV1KRS%2FzUC%2BjOGMgNS%2FDsvUKRwWv9EHdtp3es8C2XP4zMDDJP%2FHo06A4T4ocssFxhxyRs1YSdTDDkN7JBjqkARkj0YMCCDnwQD6e7QysqHlggs7AyLibKPSWOGayer%2FL4lV9jjqPiupyxuRe3MTJimXGxH8l8nU8gCC%2BgyosK1jjdI%2FzdWMKhAelzOGm9FD2BmAZIG9TnPcTRB2Uypo5to10ricXrPiVLfpPyPMQuIX76JA7DIhnyS0JC619Kxjwv5ecZPloeEmZxeKK31rCAfXsUWddah%2BNfmREv6MtrwjIu1uN&X-Amz-Signature=00710e8ed020ce75d160fc1342d6eeefe737f5839bfe365965d43dc75c8b046e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEYQ2TTZ%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqzPeMm08Noxd38GMWlsuFnP2z24fmXYDmQnwPTjmykwIhAMmTko5zfXqqA1jrsAoavYSsXCZ5v%2Fw%2Bhoz6PfEzse8mKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzRMLwMQJxs8CzrphYq3AMgNl1dxG9ne6joqhGc%2F%2BqAYd%2BGHnZTPvvORlZjHknj26DTNij8Zk7QY%2BZw%2B6xPQjPRxq8sIM5LSXtSVorLBeXsr9tRLzu%2F00gp024LEj2cPkaVl3tIB7sNBBHb4jQ0KaMAUsu0lWxpDhzEFdAXWgiPSGZXxi4uL80HVIpyIJHNEGqv7hZS45g88Xgcz8pjbSo9VP%2B0xMRQeMvw06m6%2FkD9SP4c9ThpNeP6O534voJ1%2FdO7xxrPqYRANb9FWk00lO1AMjr1OK9xPZQT%2FvaQzhlUY8DUw6f%2F5J11s79GWTWzSOlnWVJ5pCz%2F4aULXmMkt3EKdbOWRB3K%2BIgyz0AZBo6wPXjHWTggZNinWk6xC7iR9573ma3oJ4dw39nQQU8jxhSN3nomwLAQkmsIUqFujTSayO18nv52C0TTMjX7OPQ5xRCyF14UNDCgVVzpceo1z4g%2FQC%2FFGd4Hao6vOQi6aMjAH5AxkLafCBVQV8%2BX8apUQrB2OmS1O2NOsFrDrfas4DlImNJ%2BDks6ga35iqLPFu%2FqZW79zzsTDblw6qeN5na039tSyMFJWV1KRS%2FzUC%2BjOGMgNS%2FDsvUKRwWv9EHdtp3es8C2XP4zMDDJP%2FHo06A4T4ocssFxhxyRs1YSdTDDkN7JBjqkARkj0YMCCDnwQD6e7QysqHlggs7AyLibKPSWOGayer%2FL4lV9jjqPiupyxuRe3MTJimXGxH8l8nU8gCC%2BgyosK1jjdI%2FzdWMKhAelzOGm9FD2BmAZIG9TnPcTRB2Uypo5to10ricXrPiVLfpPyPMQuIX76JA7DIhnyS0JC619Kxjwv5ecZPloeEmZxeKK31rCAfXsUWddah%2BNfmREv6MtrwjIu1uN&X-Amz-Signature=b570fb613790267823844eb64d74f3831f07209058a2c1ad00c51a7d057153b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEYQ2TTZ%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqzPeMm08Noxd38GMWlsuFnP2z24fmXYDmQnwPTjmykwIhAMmTko5zfXqqA1jrsAoavYSsXCZ5v%2Fw%2Bhoz6PfEzse8mKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzRMLwMQJxs8CzrphYq3AMgNl1dxG9ne6joqhGc%2F%2BqAYd%2BGHnZTPvvORlZjHknj26DTNij8Zk7QY%2BZw%2B6xPQjPRxq8sIM5LSXtSVorLBeXsr9tRLzu%2F00gp024LEj2cPkaVl3tIB7sNBBHb4jQ0KaMAUsu0lWxpDhzEFdAXWgiPSGZXxi4uL80HVIpyIJHNEGqv7hZS45g88Xgcz8pjbSo9VP%2B0xMRQeMvw06m6%2FkD9SP4c9ThpNeP6O534voJ1%2FdO7xxrPqYRANb9FWk00lO1AMjr1OK9xPZQT%2FvaQzhlUY8DUw6f%2F5J11s79GWTWzSOlnWVJ5pCz%2F4aULXmMkt3EKdbOWRB3K%2BIgyz0AZBo6wPXjHWTggZNinWk6xC7iR9573ma3oJ4dw39nQQU8jxhSN3nomwLAQkmsIUqFujTSayO18nv52C0TTMjX7OPQ5xRCyF14UNDCgVVzpceo1z4g%2FQC%2FFGd4Hao6vOQi6aMjAH5AxkLafCBVQV8%2BX8apUQrB2OmS1O2NOsFrDrfas4DlImNJ%2BDks6ga35iqLPFu%2FqZW79zzsTDblw6qeN5na039tSyMFJWV1KRS%2FzUC%2BjOGMgNS%2FDsvUKRwWv9EHdtp3es8C2XP4zMDDJP%2FHo06A4T4ocssFxhxyRs1YSdTDDkN7JBjqkARkj0YMCCDnwQD6e7QysqHlggs7AyLibKPSWOGayer%2FL4lV9jjqPiupyxuRe3MTJimXGxH8l8nU8gCC%2BgyosK1jjdI%2FzdWMKhAelzOGm9FD2BmAZIG9TnPcTRB2Uypo5to10ricXrPiVLfpPyPMQuIX76JA7DIhnyS0JC619Kxjwv5ecZPloeEmZxeKK31rCAfXsUWddah%2BNfmREv6MtrwjIu1uN&X-Amz-Signature=f68067fb1fb22b67549c81bf9991195082f60c7dfb7ee94ddfff30c7ffd7cdf9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

