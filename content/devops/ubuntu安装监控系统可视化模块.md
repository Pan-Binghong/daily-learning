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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXCDOE5X%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIHvLu196JFGaMFZnZ5Szcg85V%2Bh0bvGdNSdH%2BhaG9TpjAiEAwcPakaMGlrUThU7XGUxQ2PN34LRy2TmqylDOb3vwy2IqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFFNPD4fLw%2BTUAU95yrcA4cKCwLseAWMBzXSqb7%2FWRg9vV2wGx%2BxYEcfxs%2FNYf%2BGBSe3Lv0qXk8qT0CW%2B1vtEV%2Fehk0A8PYqNGLyD7Q1ILGr2qVCYbmCNjRWNqQRNlt4C9WaaJOhCG2%2FBhMhd2bHFx5%2FK1GElq6PfpcitnSv4ezOnrjmwsLFm56N05VM5DPR9%2FS6dcBuf51GSNgZbPg9v0yyEmKUTcY7dMBg4aEhKdwv1H0oG9MGpHGdUF9ZSnM%2B2JPTWrQ14aryFG7EpNkHW0q9JCecRS9CWA6AfFCZqFqRNCukzVSvFgO5I0J%2Bz3bRT0cP1QiXRwNFijBcB5U1Fz3m5C3TF5I4x65jokzOVty0NuAunYhWq6lO2F51PEXDNd4GSwklF8%2FhNf5zdVARa%2B%2FsQsoIIJVp%2BnpHZww7LaORTwIW5g3iXpHAPWkro%2Fes6cicZncUEDZh%2F39wTnPJENyaQ9y1dMjGaQBJpJ8wF1ODP4eyNs5VWU6utKzSKV7xJobXS37p1ykO2q2Shq%2BR70U6UD6tFdgHbPVV13a6n9v%2FdaKqCgixqa0zhJGjTYt4TMrYJn%2B8c9hAAkrAXJT%2Buh5HPIfUdGViiTc6cpthrSNm%2BlIamO0hHCAPTVsI2CtSBXmVMcdqSnktEth1MID00c4GOqUBUUVE3uXUEQpzbmkRrG5DBj%2BwrF3ELRD4ECoFXXBrNa8x5AIKyTwkjWAGHSLj2IEtxu6lIXOJ3gEotDtBcgDw%2FUVO1N8ZfqzEFI6xZirETjGITA5ml7bos2zpyKivq%2F5v0YAzlG8s26rnXFs9Uu1yhf%2FZuZrqDcmBhvDLRbq%2FNcO%2BtC0d2mx4DYfh2CemmaQgy2Pwg7qn%2F8SHf0uRmbbaeKyWPlmi&X-Amz-Signature=d2e269a03fce639c454ab41868c1fc1f424089a66da17674df05b6630cab8c08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXCDOE5X%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIHvLu196JFGaMFZnZ5Szcg85V%2Bh0bvGdNSdH%2BhaG9TpjAiEAwcPakaMGlrUThU7XGUxQ2PN34LRy2TmqylDOb3vwy2IqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFFNPD4fLw%2BTUAU95yrcA4cKCwLseAWMBzXSqb7%2FWRg9vV2wGx%2BxYEcfxs%2FNYf%2BGBSe3Lv0qXk8qT0CW%2B1vtEV%2Fehk0A8PYqNGLyD7Q1ILGr2qVCYbmCNjRWNqQRNlt4C9WaaJOhCG2%2FBhMhd2bHFx5%2FK1GElq6PfpcitnSv4ezOnrjmwsLFm56N05VM5DPR9%2FS6dcBuf51GSNgZbPg9v0yyEmKUTcY7dMBg4aEhKdwv1H0oG9MGpHGdUF9ZSnM%2B2JPTWrQ14aryFG7EpNkHW0q9JCecRS9CWA6AfFCZqFqRNCukzVSvFgO5I0J%2Bz3bRT0cP1QiXRwNFijBcB5U1Fz3m5C3TF5I4x65jokzOVty0NuAunYhWq6lO2F51PEXDNd4GSwklF8%2FhNf5zdVARa%2B%2FsQsoIIJVp%2BnpHZww7LaORTwIW5g3iXpHAPWkro%2Fes6cicZncUEDZh%2F39wTnPJENyaQ9y1dMjGaQBJpJ8wF1ODP4eyNs5VWU6utKzSKV7xJobXS37p1ykO2q2Shq%2BR70U6UD6tFdgHbPVV13a6n9v%2FdaKqCgixqa0zhJGjTYt4TMrYJn%2B8c9hAAkrAXJT%2Buh5HPIfUdGViiTc6cpthrSNm%2BlIamO0hHCAPTVsI2CtSBXmVMcdqSnktEth1MID00c4GOqUBUUVE3uXUEQpzbmkRrG5DBj%2BwrF3ELRD4ECoFXXBrNa8x5AIKyTwkjWAGHSLj2IEtxu6lIXOJ3gEotDtBcgDw%2FUVO1N8ZfqzEFI6xZirETjGITA5ml7bos2zpyKivq%2F5v0YAzlG8s26rnXFs9Uu1yhf%2FZuZrqDcmBhvDLRbq%2FNcO%2BtC0d2mx4DYfh2CemmaQgy2Pwg7qn%2F8SHf0uRmbbaeKyWPlmi&X-Amz-Signature=3e9916a6122c0a824fcabfc0c7ae039266e2dd0dcecd6bb8317139ee40674f40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXCDOE5X%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIHvLu196JFGaMFZnZ5Szcg85V%2Bh0bvGdNSdH%2BhaG9TpjAiEAwcPakaMGlrUThU7XGUxQ2PN34LRy2TmqylDOb3vwy2IqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFFNPD4fLw%2BTUAU95yrcA4cKCwLseAWMBzXSqb7%2FWRg9vV2wGx%2BxYEcfxs%2FNYf%2BGBSe3Lv0qXk8qT0CW%2B1vtEV%2Fehk0A8PYqNGLyD7Q1ILGr2qVCYbmCNjRWNqQRNlt4C9WaaJOhCG2%2FBhMhd2bHFx5%2FK1GElq6PfpcitnSv4ezOnrjmwsLFm56N05VM5DPR9%2FS6dcBuf51GSNgZbPg9v0yyEmKUTcY7dMBg4aEhKdwv1H0oG9MGpHGdUF9ZSnM%2B2JPTWrQ14aryFG7EpNkHW0q9JCecRS9CWA6AfFCZqFqRNCukzVSvFgO5I0J%2Bz3bRT0cP1QiXRwNFijBcB5U1Fz3m5C3TF5I4x65jokzOVty0NuAunYhWq6lO2F51PEXDNd4GSwklF8%2FhNf5zdVARa%2B%2FsQsoIIJVp%2BnpHZww7LaORTwIW5g3iXpHAPWkro%2Fes6cicZncUEDZh%2F39wTnPJENyaQ9y1dMjGaQBJpJ8wF1ODP4eyNs5VWU6utKzSKV7xJobXS37p1ykO2q2Shq%2BR70U6UD6tFdgHbPVV13a6n9v%2FdaKqCgixqa0zhJGjTYt4TMrYJn%2B8c9hAAkrAXJT%2Buh5HPIfUdGViiTc6cpthrSNm%2BlIamO0hHCAPTVsI2CtSBXmVMcdqSnktEth1MID00c4GOqUBUUVE3uXUEQpzbmkRrG5DBj%2BwrF3ELRD4ECoFXXBrNa8x5AIKyTwkjWAGHSLj2IEtxu6lIXOJ3gEotDtBcgDw%2FUVO1N8ZfqzEFI6xZirETjGITA5ml7bos2zpyKivq%2F5v0YAzlG8s26rnXFs9Uu1yhf%2FZuZrqDcmBhvDLRbq%2FNcO%2BtC0d2mx4DYfh2CemmaQgy2Pwg7qn%2F8SHf0uRmbbaeKyWPlmi&X-Amz-Signature=6e1ad0068ac80db1da87ef42f1762cac3989418e528cac68c75c896bc6471aac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXCDOE5X%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIHvLu196JFGaMFZnZ5Szcg85V%2Bh0bvGdNSdH%2BhaG9TpjAiEAwcPakaMGlrUThU7XGUxQ2PN34LRy2TmqylDOb3vwy2IqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFFNPD4fLw%2BTUAU95yrcA4cKCwLseAWMBzXSqb7%2FWRg9vV2wGx%2BxYEcfxs%2FNYf%2BGBSe3Lv0qXk8qT0CW%2B1vtEV%2Fehk0A8PYqNGLyD7Q1ILGr2qVCYbmCNjRWNqQRNlt4C9WaaJOhCG2%2FBhMhd2bHFx5%2FK1GElq6PfpcitnSv4ezOnrjmwsLFm56N05VM5DPR9%2FS6dcBuf51GSNgZbPg9v0yyEmKUTcY7dMBg4aEhKdwv1H0oG9MGpHGdUF9ZSnM%2B2JPTWrQ14aryFG7EpNkHW0q9JCecRS9CWA6AfFCZqFqRNCukzVSvFgO5I0J%2Bz3bRT0cP1QiXRwNFijBcB5U1Fz3m5C3TF5I4x65jokzOVty0NuAunYhWq6lO2F51PEXDNd4GSwklF8%2FhNf5zdVARa%2B%2FsQsoIIJVp%2BnpHZww7LaORTwIW5g3iXpHAPWkro%2Fes6cicZncUEDZh%2F39wTnPJENyaQ9y1dMjGaQBJpJ8wF1ODP4eyNs5VWU6utKzSKV7xJobXS37p1ykO2q2Shq%2BR70U6UD6tFdgHbPVV13a6n9v%2FdaKqCgixqa0zhJGjTYt4TMrYJn%2B8c9hAAkrAXJT%2Buh5HPIfUdGViiTc6cpthrSNm%2BlIamO0hHCAPTVsI2CtSBXmVMcdqSnktEth1MID00c4GOqUBUUVE3uXUEQpzbmkRrG5DBj%2BwrF3ELRD4ECoFXXBrNa8x5AIKyTwkjWAGHSLj2IEtxu6lIXOJ3gEotDtBcgDw%2FUVO1N8ZfqzEFI6xZirETjGITA5ml7bos2zpyKivq%2F5v0YAzlG8s26rnXFs9Uu1yhf%2FZuZrqDcmBhvDLRbq%2FNcO%2BtC0d2mx4DYfh2CemmaQgy2Pwg7qn%2F8SHf0uRmbbaeKyWPlmi&X-Amz-Signature=f658dbf5d32fdb2738a6fa4ad211dbd160ea51e44eccad9ff7277f3f8f4861c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXCDOE5X%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIHvLu196JFGaMFZnZ5Szcg85V%2Bh0bvGdNSdH%2BhaG9TpjAiEAwcPakaMGlrUThU7XGUxQ2PN34LRy2TmqylDOb3vwy2IqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFFNPD4fLw%2BTUAU95yrcA4cKCwLseAWMBzXSqb7%2FWRg9vV2wGx%2BxYEcfxs%2FNYf%2BGBSe3Lv0qXk8qT0CW%2B1vtEV%2Fehk0A8PYqNGLyD7Q1ILGr2qVCYbmCNjRWNqQRNlt4C9WaaJOhCG2%2FBhMhd2bHFx5%2FK1GElq6PfpcitnSv4ezOnrjmwsLFm56N05VM5DPR9%2FS6dcBuf51GSNgZbPg9v0yyEmKUTcY7dMBg4aEhKdwv1H0oG9MGpHGdUF9ZSnM%2B2JPTWrQ14aryFG7EpNkHW0q9JCecRS9CWA6AfFCZqFqRNCukzVSvFgO5I0J%2Bz3bRT0cP1QiXRwNFijBcB5U1Fz3m5C3TF5I4x65jokzOVty0NuAunYhWq6lO2F51PEXDNd4GSwklF8%2FhNf5zdVARa%2B%2FsQsoIIJVp%2BnpHZww7LaORTwIW5g3iXpHAPWkro%2Fes6cicZncUEDZh%2F39wTnPJENyaQ9y1dMjGaQBJpJ8wF1ODP4eyNs5VWU6utKzSKV7xJobXS37p1ykO2q2Shq%2BR70U6UD6tFdgHbPVV13a6n9v%2FdaKqCgixqa0zhJGjTYt4TMrYJn%2B8c9hAAkrAXJT%2Buh5HPIfUdGViiTc6cpthrSNm%2BlIamO0hHCAPTVsI2CtSBXmVMcdqSnktEth1MID00c4GOqUBUUVE3uXUEQpzbmkRrG5DBj%2BwrF3ELRD4ECoFXXBrNa8x5AIKyTwkjWAGHSLj2IEtxu6lIXOJ3gEotDtBcgDw%2FUVO1N8ZfqzEFI6xZirETjGITA5ml7bos2zpyKivq%2F5v0YAzlG8s26rnXFs9Uu1yhf%2FZuZrqDcmBhvDLRbq%2FNcO%2BtC0d2mx4DYfh2CemmaQgy2Pwg7qn%2F8SHf0uRmbbaeKyWPlmi&X-Amz-Signature=bd716f2503265cd84cb55fd17093ae3049ebbc7174642ea41d54fbedb978b2f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXCDOE5X%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIHvLu196JFGaMFZnZ5Szcg85V%2Bh0bvGdNSdH%2BhaG9TpjAiEAwcPakaMGlrUThU7XGUxQ2PN34LRy2TmqylDOb3vwy2IqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFFNPD4fLw%2BTUAU95yrcA4cKCwLseAWMBzXSqb7%2FWRg9vV2wGx%2BxYEcfxs%2FNYf%2BGBSe3Lv0qXk8qT0CW%2B1vtEV%2Fehk0A8PYqNGLyD7Q1ILGr2qVCYbmCNjRWNqQRNlt4C9WaaJOhCG2%2FBhMhd2bHFx5%2FK1GElq6PfpcitnSv4ezOnrjmwsLFm56N05VM5DPR9%2FS6dcBuf51GSNgZbPg9v0yyEmKUTcY7dMBg4aEhKdwv1H0oG9MGpHGdUF9ZSnM%2B2JPTWrQ14aryFG7EpNkHW0q9JCecRS9CWA6AfFCZqFqRNCukzVSvFgO5I0J%2Bz3bRT0cP1QiXRwNFijBcB5U1Fz3m5C3TF5I4x65jokzOVty0NuAunYhWq6lO2F51PEXDNd4GSwklF8%2FhNf5zdVARa%2B%2FsQsoIIJVp%2BnpHZww7LaORTwIW5g3iXpHAPWkro%2Fes6cicZncUEDZh%2F39wTnPJENyaQ9y1dMjGaQBJpJ8wF1ODP4eyNs5VWU6utKzSKV7xJobXS37p1ykO2q2Shq%2BR70U6UD6tFdgHbPVV13a6n9v%2FdaKqCgixqa0zhJGjTYt4TMrYJn%2B8c9hAAkrAXJT%2Buh5HPIfUdGViiTc6cpthrSNm%2BlIamO0hHCAPTVsI2CtSBXmVMcdqSnktEth1MID00c4GOqUBUUVE3uXUEQpzbmkRrG5DBj%2BwrF3ELRD4ECoFXXBrNa8x5AIKyTwkjWAGHSLj2IEtxu6lIXOJ3gEotDtBcgDw%2FUVO1N8ZfqzEFI6xZirETjGITA5ml7bos2zpyKivq%2F5v0YAzlG8s26rnXFs9Uu1yhf%2FZuZrqDcmBhvDLRbq%2FNcO%2BtC0d2mx4DYfh2CemmaQgy2Pwg7qn%2F8SHf0uRmbbaeKyWPlmi&X-Amz-Signature=ae87b5cf3bec00bbf64d539e40f893600581e872b38309437756620efe1682c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXCDOE5X%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIHvLu196JFGaMFZnZ5Szcg85V%2Bh0bvGdNSdH%2BhaG9TpjAiEAwcPakaMGlrUThU7XGUxQ2PN34LRy2TmqylDOb3vwy2IqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFFNPD4fLw%2BTUAU95yrcA4cKCwLseAWMBzXSqb7%2FWRg9vV2wGx%2BxYEcfxs%2FNYf%2BGBSe3Lv0qXk8qT0CW%2B1vtEV%2Fehk0A8PYqNGLyD7Q1ILGr2qVCYbmCNjRWNqQRNlt4C9WaaJOhCG2%2FBhMhd2bHFx5%2FK1GElq6PfpcitnSv4ezOnrjmwsLFm56N05VM5DPR9%2FS6dcBuf51GSNgZbPg9v0yyEmKUTcY7dMBg4aEhKdwv1H0oG9MGpHGdUF9ZSnM%2B2JPTWrQ14aryFG7EpNkHW0q9JCecRS9CWA6AfFCZqFqRNCukzVSvFgO5I0J%2Bz3bRT0cP1QiXRwNFijBcB5U1Fz3m5C3TF5I4x65jokzOVty0NuAunYhWq6lO2F51PEXDNd4GSwklF8%2FhNf5zdVARa%2B%2FsQsoIIJVp%2BnpHZww7LaORTwIW5g3iXpHAPWkro%2Fes6cicZncUEDZh%2F39wTnPJENyaQ9y1dMjGaQBJpJ8wF1ODP4eyNs5VWU6utKzSKV7xJobXS37p1ykO2q2Shq%2BR70U6UD6tFdgHbPVV13a6n9v%2FdaKqCgixqa0zhJGjTYt4TMrYJn%2B8c9hAAkrAXJT%2Buh5HPIfUdGViiTc6cpthrSNm%2BlIamO0hHCAPTVsI2CtSBXmVMcdqSnktEth1MID00c4GOqUBUUVE3uXUEQpzbmkRrG5DBj%2BwrF3ELRD4ECoFXXBrNa8x5AIKyTwkjWAGHSLj2IEtxu6lIXOJ3gEotDtBcgDw%2FUVO1N8ZfqzEFI6xZirETjGITA5ml7bos2zpyKivq%2F5v0YAzlG8s26rnXFs9Uu1yhf%2FZuZrqDcmBhvDLRbq%2FNcO%2BtC0d2mx4DYfh2CemmaQgy2Pwg7qn%2F8SHf0uRmbbaeKyWPlmi&X-Amz-Signature=3202d8069645ad5f300d46364c972bfc6d3f7f0bda6fea0bc486786f46bbcaa4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

