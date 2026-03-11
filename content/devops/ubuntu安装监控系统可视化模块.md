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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4JNWOIS%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHpqQablvtTjdgreY%2FPE%2BUNDudppdxQDb75uc3GGD3ZxAiEApEfTnszE9jH%2BUOHGOhNa9MloocP%2BYpLNduxIoygPBvIq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNy1qDiVFGSdqWzhdircA1%2BBosEaQX4%2BgiAdMbJXuSVvyTq2r1MtmzJfVA0tfgBKUjDjdlh48PXRKWG13A%2FFAXcbl95dRtSEaRzqOsrSps5l6B2yi6WN9Paa%2FahSukmP4Pl1QIn6EgyLx2tSMgpZ5oRZR9EumOqcSsUu2dr%2BBpNKaYtdFqyz%2FPxfcat%2B2UMl%2BldhHMs7sM%2BSfD1NIH8ggow%2BZP%2FP%2FfhniY5ip6Sd0tXQlRKrP3PpTfxO3brmf4zOJ%2B49FpzeutkEsI8fOgaxbzuuBNLE06KdHdKcZsroE2KErNnXTbfVoOhaT4%2BsKp2ZDy9MHE3HWahMiGLPQiD6SdJorHDrxRY69ePBlrehDGTDiXWFHR3nqUqtiDX7XccoPCoZOTiG4zf7yezD%2Fb28Q84flzSbPQksShIYfPTMUNfr1Hxs%2B%2Bi8EFvX9n6uiPhNRx9O4DVIRgD4RifdG68OWgRNXi65Q1hTdtmpx0dzFX3bENVKavpmiQae%2BP5Drp822nkOEnKBnAEjj%2FiAagEvOdgxHKYbCr3PS7iM0nXTwFG2IKEfmtjnVTGvdF5a7G4O4GvKsOoXFw41Rr8K5QnFY5vZ3ft%2BpxD4%2B2XMt3caPQHjnQPMY1qg5K5BrG0V3E1ggdM04Qr3DJ6FWTw8MOvxws0GOqUBQFwqSRM%2B8OWvWJd%2BQ0urkwCXi875YkHjaLi4m7QmskDjVe1y1v3FcUvfPzKmn5vVq5cBz62IsSqfW939M1t3sBXS2d3XOfeMPt6VaftNSrtXHEDd51lb5UGfLxt1KGlYxzRns2Qs984NmEp8MdsmyVZeRNXmFDapH0n7CHzUn%2Fl0OsKSfy%2Fuc7uiOrwUk8i1V1HolCJM0EZd7olHK6zkOcFXgQG8&X-Amz-Signature=df4206cdac1e014417dbe6e0381d326948706a536ea1a5ca18b278835057f028&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4JNWOIS%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHpqQablvtTjdgreY%2FPE%2BUNDudppdxQDb75uc3GGD3ZxAiEApEfTnszE9jH%2BUOHGOhNa9MloocP%2BYpLNduxIoygPBvIq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNy1qDiVFGSdqWzhdircA1%2BBosEaQX4%2BgiAdMbJXuSVvyTq2r1MtmzJfVA0tfgBKUjDjdlh48PXRKWG13A%2FFAXcbl95dRtSEaRzqOsrSps5l6B2yi6WN9Paa%2FahSukmP4Pl1QIn6EgyLx2tSMgpZ5oRZR9EumOqcSsUu2dr%2BBpNKaYtdFqyz%2FPxfcat%2B2UMl%2BldhHMs7sM%2BSfD1NIH8ggow%2BZP%2FP%2FfhniY5ip6Sd0tXQlRKrP3PpTfxO3brmf4zOJ%2B49FpzeutkEsI8fOgaxbzuuBNLE06KdHdKcZsroE2KErNnXTbfVoOhaT4%2BsKp2ZDy9MHE3HWahMiGLPQiD6SdJorHDrxRY69ePBlrehDGTDiXWFHR3nqUqtiDX7XccoPCoZOTiG4zf7yezD%2Fb28Q84flzSbPQksShIYfPTMUNfr1Hxs%2B%2Bi8EFvX9n6uiPhNRx9O4DVIRgD4RifdG68OWgRNXi65Q1hTdtmpx0dzFX3bENVKavpmiQae%2BP5Drp822nkOEnKBnAEjj%2FiAagEvOdgxHKYbCr3PS7iM0nXTwFG2IKEfmtjnVTGvdF5a7G4O4GvKsOoXFw41Rr8K5QnFY5vZ3ft%2BpxD4%2B2XMt3caPQHjnQPMY1qg5K5BrG0V3E1ggdM04Qr3DJ6FWTw8MOvxws0GOqUBQFwqSRM%2B8OWvWJd%2BQ0urkwCXi875YkHjaLi4m7QmskDjVe1y1v3FcUvfPzKmn5vVq5cBz62IsSqfW939M1t3sBXS2d3XOfeMPt6VaftNSrtXHEDd51lb5UGfLxt1KGlYxzRns2Qs984NmEp8MdsmyVZeRNXmFDapH0n7CHzUn%2Fl0OsKSfy%2Fuc7uiOrwUk8i1V1HolCJM0EZd7olHK6zkOcFXgQG8&X-Amz-Signature=22c53cab0743ef14468c964f9bef1712e9fbc4227b11e99780d1e7e58ad5b18a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4JNWOIS%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHpqQablvtTjdgreY%2FPE%2BUNDudppdxQDb75uc3GGD3ZxAiEApEfTnszE9jH%2BUOHGOhNa9MloocP%2BYpLNduxIoygPBvIq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNy1qDiVFGSdqWzhdircA1%2BBosEaQX4%2BgiAdMbJXuSVvyTq2r1MtmzJfVA0tfgBKUjDjdlh48PXRKWG13A%2FFAXcbl95dRtSEaRzqOsrSps5l6B2yi6WN9Paa%2FahSukmP4Pl1QIn6EgyLx2tSMgpZ5oRZR9EumOqcSsUu2dr%2BBpNKaYtdFqyz%2FPxfcat%2B2UMl%2BldhHMs7sM%2BSfD1NIH8ggow%2BZP%2FP%2FfhniY5ip6Sd0tXQlRKrP3PpTfxO3brmf4zOJ%2B49FpzeutkEsI8fOgaxbzuuBNLE06KdHdKcZsroE2KErNnXTbfVoOhaT4%2BsKp2ZDy9MHE3HWahMiGLPQiD6SdJorHDrxRY69ePBlrehDGTDiXWFHR3nqUqtiDX7XccoPCoZOTiG4zf7yezD%2Fb28Q84flzSbPQksShIYfPTMUNfr1Hxs%2B%2Bi8EFvX9n6uiPhNRx9O4DVIRgD4RifdG68OWgRNXi65Q1hTdtmpx0dzFX3bENVKavpmiQae%2BP5Drp822nkOEnKBnAEjj%2FiAagEvOdgxHKYbCr3PS7iM0nXTwFG2IKEfmtjnVTGvdF5a7G4O4GvKsOoXFw41Rr8K5QnFY5vZ3ft%2BpxD4%2B2XMt3caPQHjnQPMY1qg5K5BrG0V3E1ggdM04Qr3DJ6FWTw8MOvxws0GOqUBQFwqSRM%2B8OWvWJd%2BQ0urkwCXi875YkHjaLi4m7QmskDjVe1y1v3FcUvfPzKmn5vVq5cBz62IsSqfW939M1t3sBXS2d3XOfeMPt6VaftNSrtXHEDd51lb5UGfLxt1KGlYxzRns2Qs984NmEp8MdsmyVZeRNXmFDapH0n7CHzUn%2Fl0OsKSfy%2Fuc7uiOrwUk8i1V1HolCJM0EZd7olHK6zkOcFXgQG8&X-Amz-Signature=9a44dd569c0e7e47ee69827842d2b02c6c15c47de2a4fb327c46c703b1b35d39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4JNWOIS%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHpqQablvtTjdgreY%2FPE%2BUNDudppdxQDb75uc3GGD3ZxAiEApEfTnszE9jH%2BUOHGOhNa9MloocP%2BYpLNduxIoygPBvIq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNy1qDiVFGSdqWzhdircA1%2BBosEaQX4%2BgiAdMbJXuSVvyTq2r1MtmzJfVA0tfgBKUjDjdlh48PXRKWG13A%2FFAXcbl95dRtSEaRzqOsrSps5l6B2yi6WN9Paa%2FahSukmP4Pl1QIn6EgyLx2tSMgpZ5oRZR9EumOqcSsUu2dr%2BBpNKaYtdFqyz%2FPxfcat%2B2UMl%2BldhHMs7sM%2BSfD1NIH8ggow%2BZP%2FP%2FfhniY5ip6Sd0tXQlRKrP3PpTfxO3brmf4zOJ%2B49FpzeutkEsI8fOgaxbzuuBNLE06KdHdKcZsroE2KErNnXTbfVoOhaT4%2BsKp2ZDy9MHE3HWahMiGLPQiD6SdJorHDrxRY69ePBlrehDGTDiXWFHR3nqUqtiDX7XccoPCoZOTiG4zf7yezD%2Fb28Q84flzSbPQksShIYfPTMUNfr1Hxs%2B%2Bi8EFvX9n6uiPhNRx9O4DVIRgD4RifdG68OWgRNXi65Q1hTdtmpx0dzFX3bENVKavpmiQae%2BP5Drp822nkOEnKBnAEjj%2FiAagEvOdgxHKYbCr3PS7iM0nXTwFG2IKEfmtjnVTGvdF5a7G4O4GvKsOoXFw41Rr8K5QnFY5vZ3ft%2BpxD4%2B2XMt3caPQHjnQPMY1qg5K5BrG0V3E1ggdM04Qr3DJ6FWTw8MOvxws0GOqUBQFwqSRM%2B8OWvWJd%2BQ0urkwCXi875YkHjaLi4m7QmskDjVe1y1v3FcUvfPzKmn5vVq5cBz62IsSqfW939M1t3sBXS2d3XOfeMPt6VaftNSrtXHEDd51lb5UGfLxt1KGlYxzRns2Qs984NmEp8MdsmyVZeRNXmFDapH0n7CHzUn%2Fl0OsKSfy%2Fuc7uiOrwUk8i1V1HolCJM0EZd7olHK6zkOcFXgQG8&X-Amz-Signature=03f47d1e8f510bc6e4a59b68845dd4913e5540d43de51516555b8c4a761645cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4JNWOIS%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHpqQablvtTjdgreY%2FPE%2BUNDudppdxQDb75uc3GGD3ZxAiEApEfTnszE9jH%2BUOHGOhNa9MloocP%2BYpLNduxIoygPBvIq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNy1qDiVFGSdqWzhdircA1%2BBosEaQX4%2BgiAdMbJXuSVvyTq2r1MtmzJfVA0tfgBKUjDjdlh48PXRKWG13A%2FFAXcbl95dRtSEaRzqOsrSps5l6B2yi6WN9Paa%2FahSukmP4Pl1QIn6EgyLx2tSMgpZ5oRZR9EumOqcSsUu2dr%2BBpNKaYtdFqyz%2FPxfcat%2B2UMl%2BldhHMs7sM%2BSfD1NIH8ggow%2BZP%2FP%2FfhniY5ip6Sd0tXQlRKrP3PpTfxO3brmf4zOJ%2B49FpzeutkEsI8fOgaxbzuuBNLE06KdHdKcZsroE2KErNnXTbfVoOhaT4%2BsKp2ZDy9MHE3HWahMiGLPQiD6SdJorHDrxRY69ePBlrehDGTDiXWFHR3nqUqtiDX7XccoPCoZOTiG4zf7yezD%2Fb28Q84flzSbPQksShIYfPTMUNfr1Hxs%2B%2Bi8EFvX9n6uiPhNRx9O4DVIRgD4RifdG68OWgRNXi65Q1hTdtmpx0dzFX3bENVKavpmiQae%2BP5Drp822nkOEnKBnAEjj%2FiAagEvOdgxHKYbCr3PS7iM0nXTwFG2IKEfmtjnVTGvdF5a7G4O4GvKsOoXFw41Rr8K5QnFY5vZ3ft%2BpxD4%2B2XMt3caPQHjnQPMY1qg5K5BrG0V3E1ggdM04Qr3DJ6FWTw8MOvxws0GOqUBQFwqSRM%2B8OWvWJd%2BQ0urkwCXi875YkHjaLi4m7QmskDjVe1y1v3FcUvfPzKmn5vVq5cBz62IsSqfW939M1t3sBXS2d3XOfeMPt6VaftNSrtXHEDd51lb5UGfLxt1KGlYxzRns2Qs984NmEp8MdsmyVZeRNXmFDapH0n7CHzUn%2Fl0OsKSfy%2Fuc7uiOrwUk8i1V1HolCJM0EZd7olHK6zkOcFXgQG8&X-Amz-Signature=ea155556bf073c685575c2351ef5113df5865720c967c2457a65285c3ce3d6b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4JNWOIS%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHpqQablvtTjdgreY%2FPE%2BUNDudppdxQDb75uc3GGD3ZxAiEApEfTnszE9jH%2BUOHGOhNa9MloocP%2BYpLNduxIoygPBvIq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNy1qDiVFGSdqWzhdircA1%2BBosEaQX4%2BgiAdMbJXuSVvyTq2r1MtmzJfVA0tfgBKUjDjdlh48PXRKWG13A%2FFAXcbl95dRtSEaRzqOsrSps5l6B2yi6WN9Paa%2FahSukmP4Pl1QIn6EgyLx2tSMgpZ5oRZR9EumOqcSsUu2dr%2BBpNKaYtdFqyz%2FPxfcat%2B2UMl%2BldhHMs7sM%2BSfD1NIH8ggow%2BZP%2FP%2FfhniY5ip6Sd0tXQlRKrP3PpTfxO3brmf4zOJ%2B49FpzeutkEsI8fOgaxbzuuBNLE06KdHdKcZsroE2KErNnXTbfVoOhaT4%2BsKp2ZDy9MHE3HWahMiGLPQiD6SdJorHDrxRY69ePBlrehDGTDiXWFHR3nqUqtiDX7XccoPCoZOTiG4zf7yezD%2Fb28Q84flzSbPQksShIYfPTMUNfr1Hxs%2B%2Bi8EFvX9n6uiPhNRx9O4DVIRgD4RifdG68OWgRNXi65Q1hTdtmpx0dzFX3bENVKavpmiQae%2BP5Drp822nkOEnKBnAEjj%2FiAagEvOdgxHKYbCr3PS7iM0nXTwFG2IKEfmtjnVTGvdF5a7G4O4GvKsOoXFw41Rr8K5QnFY5vZ3ft%2BpxD4%2B2XMt3caPQHjnQPMY1qg5K5BrG0V3E1ggdM04Qr3DJ6FWTw8MOvxws0GOqUBQFwqSRM%2B8OWvWJd%2BQ0urkwCXi875YkHjaLi4m7QmskDjVe1y1v3FcUvfPzKmn5vVq5cBz62IsSqfW939M1t3sBXS2d3XOfeMPt6VaftNSrtXHEDd51lb5UGfLxt1KGlYxzRns2Qs984NmEp8MdsmyVZeRNXmFDapH0n7CHzUn%2Fl0OsKSfy%2Fuc7uiOrwUk8i1V1HolCJM0EZd7olHK6zkOcFXgQG8&X-Amz-Signature=9c4991694bd8c0f2c722319b51ff9d956e21b58f5c5baccde2292a92ffb37695&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4JNWOIS%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHpqQablvtTjdgreY%2FPE%2BUNDudppdxQDb75uc3GGD3ZxAiEApEfTnszE9jH%2BUOHGOhNa9MloocP%2BYpLNduxIoygPBvIq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNy1qDiVFGSdqWzhdircA1%2BBosEaQX4%2BgiAdMbJXuSVvyTq2r1MtmzJfVA0tfgBKUjDjdlh48PXRKWG13A%2FFAXcbl95dRtSEaRzqOsrSps5l6B2yi6WN9Paa%2FahSukmP4Pl1QIn6EgyLx2tSMgpZ5oRZR9EumOqcSsUu2dr%2BBpNKaYtdFqyz%2FPxfcat%2B2UMl%2BldhHMs7sM%2BSfD1NIH8ggow%2BZP%2FP%2FfhniY5ip6Sd0tXQlRKrP3PpTfxO3brmf4zOJ%2B49FpzeutkEsI8fOgaxbzuuBNLE06KdHdKcZsroE2KErNnXTbfVoOhaT4%2BsKp2ZDy9MHE3HWahMiGLPQiD6SdJorHDrxRY69ePBlrehDGTDiXWFHR3nqUqtiDX7XccoPCoZOTiG4zf7yezD%2Fb28Q84flzSbPQksShIYfPTMUNfr1Hxs%2B%2Bi8EFvX9n6uiPhNRx9O4DVIRgD4RifdG68OWgRNXi65Q1hTdtmpx0dzFX3bENVKavpmiQae%2BP5Drp822nkOEnKBnAEjj%2FiAagEvOdgxHKYbCr3PS7iM0nXTwFG2IKEfmtjnVTGvdF5a7G4O4GvKsOoXFw41Rr8K5QnFY5vZ3ft%2BpxD4%2B2XMt3caPQHjnQPMY1qg5K5BrG0V3E1ggdM04Qr3DJ6FWTw8MOvxws0GOqUBQFwqSRM%2B8OWvWJd%2BQ0urkwCXi875YkHjaLi4m7QmskDjVe1y1v3FcUvfPzKmn5vVq5cBz62IsSqfW939M1t3sBXS2d3XOfeMPt6VaftNSrtXHEDd51lb5UGfLxt1KGlYxzRns2Qs984NmEp8MdsmyVZeRNXmFDapH0n7CHzUn%2Fl0OsKSfy%2Fuc7uiOrwUk8i1V1HolCJM0EZd7olHK6zkOcFXgQG8&X-Amz-Signature=aa622e4f51fa06e58fa4d8a747c207ccf9a7c61d710e6b20edb19eb61e9cdf0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

