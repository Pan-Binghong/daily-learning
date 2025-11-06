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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJAKEAWK%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Fd7Ilc5CsBfobsjSOZKLGGwf%2F5XD%2BfBhlMb7HQRh2HQIgD51%2BhoxakX7A3a5Vs3aszkVpdgkap8j6VzrIVkdYrvUqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJpqNbkiIYuuOAERxyrcA%2FF1mAmffwfka3ySAxhu21njN5eZe6%2BrZL%2BYVVgR9hZ4oExoKyZeepomPCZNI7kGYwFs6YWieQYPAiKV6jYBR5xSd%2Fq95bSuNx6RAV6DTk2UE%2Fhh5Jv%2F0wGN97JQURm%2BPzswXIbFTMtsac8BhnXkBqMC0udW%2BL2vpdGyIOMFJbc%2B7ngJTbgQYYSTgMCbaE7Z6%2B2INO8fmO094zU%2BHEMP%2FezNT8rXIIadNKZmEjH%2F3bORCY138QcFdzDk4MB02jLx6Y62aLJlGGHSV2dM8n7Y%2FlaOdp7Bq7AIgIGSYEuABTdr90MAr6ZRzsFMaKgvuF4nWW5pmRCg3f%2BDVkNZApobbmntklXnAxYmq0yFCg84AP0udwG4lNkW1i24smaUKdZPrr0ULippBDb3V%2B1UqnC2IWbSrsSO6%2BEZ4Ob8qLC1Mw3z4PgqqDFut%2BTJ8dhq2B82IVIZWvx6IUKJgPqTq18lceZEAtdQLivjAb43ppKNRqDPXhLhxgW0DwToWXPV0sIyIYmSMI7Hkn3DOOs2lIm%2FIET8cLcaq888qEH%2B1qmp5W6h4JfybAP%2F2tg9WYUFbb1EUiGMHZmXmgTRMWVfoMJWTiEvzXgxJARzSu193WFwPPP25lhb8rm%2BVRrSRcnaMIqWsMgGOqUBohYrxOQCl4eTs%2FSwiS3wLe5BSBoXIrVQR2o30Jo0xJWUkKyq9C7ESjVYuTOjglIY%2B6YkPvojjtKX6ubd10wkaiQntC6SEEfq9SKL4bWtOmA5MpA48t%2BbCN%2BMOY5VYadEdpFq4V2Ps%2BHw5Xm6MmbHYAGlIvRMMGXLh0KzvOjXp%2BLeShjDsXPXWfJYur7Uj5NJ1wUKnd%2BQQg7NipuNA%2B1JXLp19vB4&X-Amz-Signature=ddd78bbdb0418113b2ba4f37c2c882fbf8b8be747e63fff64ae7cb3fac63c414&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJAKEAWK%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Fd7Ilc5CsBfobsjSOZKLGGwf%2F5XD%2BfBhlMb7HQRh2HQIgD51%2BhoxakX7A3a5Vs3aszkVpdgkap8j6VzrIVkdYrvUqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJpqNbkiIYuuOAERxyrcA%2FF1mAmffwfka3ySAxhu21njN5eZe6%2BrZL%2BYVVgR9hZ4oExoKyZeepomPCZNI7kGYwFs6YWieQYPAiKV6jYBR5xSd%2Fq95bSuNx6RAV6DTk2UE%2Fhh5Jv%2F0wGN97JQURm%2BPzswXIbFTMtsac8BhnXkBqMC0udW%2BL2vpdGyIOMFJbc%2B7ngJTbgQYYSTgMCbaE7Z6%2B2INO8fmO094zU%2BHEMP%2FezNT8rXIIadNKZmEjH%2F3bORCY138QcFdzDk4MB02jLx6Y62aLJlGGHSV2dM8n7Y%2FlaOdp7Bq7AIgIGSYEuABTdr90MAr6ZRzsFMaKgvuF4nWW5pmRCg3f%2BDVkNZApobbmntklXnAxYmq0yFCg84AP0udwG4lNkW1i24smaUKdZPrr0ULippBDb3V%2B1UqnC2IWbSrsSO6%2BEZ4Ob8qLC1Mw3z4PgqqDFut%2BTJ8dhq2B82IVIZWvx6IUKJgPqTq18lceZEAtdQLivjAb43ppKNRqDPXhLhxgW0DwToWXPV0sIyIYmSMI7Hkn3DOOs2lIm%2FIET8cLcaq888qEH%2B1qmp5W6h4JfybAP%2F2tg9WYUFbb1EUiGMHZmXmgTRMWVfoMJWTiEvzXgxJARzSu193WFwPPP25lhb8rm%2BVRrSRcnaMIqWsMgGOqUBohYrxOQCl4eTs%2FSwiS3wLe5BSBoXIrVQR2o30Jo0xJWUkKyq9C7ESjVYuTOjglIY%2B6YkPvojjtKX6ubd10wkaiQntC6SEEfq9SKL4bWtOmA5MpA48t%2BbCN%2BMOY5VYadEdpFq4V2Ps%2BHw5Xm6MmbHYAGlIvRMMGXLh0KzvOjXp%2BLeShjDsXPXWfJYur7Uj5NJ1wUKnd%2BQQg7NipuNA%2B1JXLp19vB4&X-Amz-Signature=b17dbb3fa3fb94f357cd0a66e3434b7cf3bef7c8d124aebce01a32f22f0a6f09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJAKEAWK%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Fd7Ilc5CsBfobsjSOZKLGGwf%2F5XD%2BfBhlMb7HQRh2HQIgD51%2BhoxakX7A3a5Vs3aszkVpdgkap8j6VzrIVkdYrvUqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJpqNbkiIYuuOAERxyrcA%2FF1mAmffwfka3ySAxhu21njN5eZe6%2BrZL%2BYVVgR9hZ4oExoKyZeepomPCZNI7kGYwFs6YWieQYPAiKV6jYBR5xSd%2Fq95bSuNx6RAV6DTk2UE%2Fhh5Jv%2F0wGN97JQURm%2BPzswXIbFTMtsac8BhnXkBqMC0udW%2BL2vpdGyIOMFJbc%2B7ngJTbgQYYSTgMCbaE7Z6%2B2INO8fmO094zU%2BHEMP%2FezNT8rXIIadNKZmEjH%2F3bORCY138QcFdzDk4MB02jLx6Y62aLJlGGHSV2dM8n7Y%2FlaOdp7Bq7AIgIGSYEuABTdr90MAr6ZRzsFMaKgvuF4nWW5pmRCg3f%2BDVkNZApobbmntklXnAxYmq0yFCg84AP0udwG4lNkW1i24smaUKdZPrr0ULippBDb3V%2B1UqnC2IWbSrsSO6%2BEZ4Ob8qLC1Mw3z4PgqqDFut%2BTJ8dhq2B82IVIZWvx6IUKJgPqTq18lceZEAtdQLivjAb43ppKNRqDPXhLhxgW0DwToWXPV0sIyIYmSMI7Hkn3DOOs2lIm%2FIET8cLcaq888qEH%2B1qmp5W6h4JfybAP%2F2tg9WYUFbb1EUiGMHZmXmgTRMWVfoMJWTiEvzXgxJARzSu193WFwPPP25lhb8rm%2BVRrSRcnaMIqWsMgGOqUBohYrxOQCl4eTs%2FSwiS3wLe5BSBoXIrVQR2o30Jo0xJWUkKyq9C7ESjVYuTOjglIY%2B6YkPvojjtKX6ubd10wkaiQntC6SEEfq9SKL4bWtOmA5MpA48t%2BbCN%2BMOY5VYadEdpFq4V2Ps%2BHw5Xm6MmbHYAGlIvRMMGXLh0KzvOjXp%2BLeShjDsXPXWfJYur7Uj5NJ1wUKnd%2BQQg7NipuNA%2B1JXLp19vB4&X-Amz-Signature=8d20229613b8391a8e01e5fbd14a4d6ef4d65564f538cb8954b1160bdbf4b970&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJAKEAWK%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Fd7Ilc5CsBfobsjSOZKLGGwf%2F5XD%2BfBhlMb7HQRh2HQIgD51%2BhoxakX7A3a5Vs3aszkVpdgkap8j6VzrIVkdYrvUqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJpqNbkiIYuuOAERxyrcA%2FF1mAmffwfka3ySAxhu21njN5eZe6%2BrZL%2BYVVgR9hZ4oExoKyZeepomPCZNI7kGYwFs6YWieQYPAiKV6jYBR5xSd%2Fq95bSuNx6RAV6DTk2UE%2Fhh5Jv%2F0wGN97JQURm%2BPzswXIbFTMtsac8BhnXkBqMC0udW%2BL2vpdGyIOMFJbc%2B7ngJTbgQYYSTgMCbaE7Z6%2B2INO8fmO094zU%2BHEMP%2FezNT8rXIIadNKZmEjH%2F3bORCY138QcFdzDk4MB02jLx6Y62aLJlGGHSV2dM8n7Y%2FlaOdp7Bq7AIgIGSYEuABTdr90MAr6ZRzsFMaKgvuF4nWW5pmRCg3f%2BDVkNZApobbmntklXnAxYmq0yFCg84AP0udwG4lNkW1i24smaUKdZPrr0ULippBDb3V%2B1UqnC2IWbSrsSO6%2BEZ4Ob8qLC1Mw3z4PgqqDFut%2BTJ8dhq2B82IVIZWvx6IUKJgPqTq18lceZEAtdQLivjAb43ppKNRqDPXhLhxgW0DwToWXPV0sIyIYmSMI7Hkn3DOOs2lIm%2FIET8cLcaq888qEH%2B1qmp5W6h4JfybAP%2F2tg9WYUFbb1EUiGMHZmXmgTRMWVfoMJWTiEvzXgxJARzSu193WFwPPP25lhb8rm%2BVRrSRcnaMIqWsMgGOqUBohYrxOQCl4eTs%2FSwiS3wLe5BSBoXIrVQR2o30Jo0xJWUkKyq9C7ESjVYuTOjglIY%2B6YkPvojjtKX6ubd10wkaiQntC6SEEfq9SKL4bWtOmA5MpA48t%2BbCN%2BMOY5VYadEdpFq4V2Ps%2BHw5Xm6MmbHYAGlIvRMMGXLh0KzvOjXp%2BLeShjDsXPXWfJYur7Uj5NJ1wUKnd%2BQQg7NipuNA%2B1JXLp19vB4&X-Amz-Signature=9000842c5cca82490f5f22179c385c5aaafb49cbee003b90c68f3f46e2c69484&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJAKEAWK%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Fd7Ilc5CsBfobsjSOZKLGGwf%2F5XD%2BfBhlMb7HQRh2HQIgD51%2BhoxakX7A3a5Vs3aszkVpdgkap8j6VzrIVkdYrvUqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJpqNbkiIYuuOAERxyrcA%2FF1mAmffwfka3ySAxhu21njN5eZe6%2BrZL%2BYVVgR9hZ4oExoKyZeepomPCZNI7kGYwFs6YWieQYPAiKV6jYBR5xSd%2Fq95bSuNx6RAV6DTk2UE%2Fhh5Jv%2F0wGN97JQURm%2BPzswXIbFTMtsac8BhnXkBqMC0udW%2BL2vpdGyIOMFJbc%2B7ngJTbgQYYSTgMCbaE7Z6%2B2INO8fmO094zU%2BHEMP%2FezNT8rXIIadNKZmEjH%2F3bORCY138QcFdzDk4MB02jLx6Y62aLJlGGHSV2dM8n7Y%2FlaOdp7Bq7AIgIGSYEuABTdr90MAr6ZRzsFMaKgvuF4nWW5pmRCg3f%2BDVkNZApobbmntklXnAxYmq0yFCg84AP0udwG4lNkW1i24smaUKdZPrr0ULippBDb3V%2B1UqnC2IWbSrsSO6%2BEZ4Ob8qLC1Mw3z4PgqqDFut%2BTJ8dhq2B82IVIZWvx6IUKJgPqTq18lceZEAtdQLivjAb43ppKNRqDPXhLhxgW0DwToWXPV0sIyIYmSMI7Hkn3DOOs2lIm%2FIET8cLcaq888qEH%2B1qmp5W6h4JfybAP%2F2tg9WYUFbb1EUiGMHZmXmgTRMWVfoMJWTiEvzXgxJARzSu193WFwPPP25lhb8rm%2BVRrSRcnaMIqWsMgGOqUBohYrxOQCl4eTs%2FSwiS3wLe5BSBoXIrVQR2o30Jo0xJWUkKyq9C7ESjVYuTOjglIY%2B6YkPvojjtKX6ubd10wkaiQntC6SEEfq9SKL4bWtOmA5MpA48t%2BbCN%2BMOY5VYadEdpFq4V2Ps%2BHw5Xm6MmbHYAGlIvRMMGXLh0KzvOjXp%2BLeShjDsXPXWfJYur7Uj5NJ1wUKnd%2BQQg7NipuNA%2B1JXLp19vB4&X-Amz-Signature=b4bf1b5f9b114d471788d8f9dbe36fa473b856c76ce00e1857ed18b462937fd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJAKEAWK%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Fd7Ilc5CsBfobsjSOZKLGGwf%2F5XD%2BfBhlMb7HQRh2HQIgD51%2BhoxakX7A3a5Vs3aszkVpdgkap8j6VzrIVkdYrvUqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJpqNbkiIYuuOAERxyrcA%2FF1mAmffwfka3ySAxhu21njN5eZe6%2BrZL%2BYVVgR9hZ4oExoKyZeepomPCZNI7kGYwFs6YWieQYPAiKV6jYBR5xSd%2Fq95bSuNx6RAV6DTk2UE%2Fhh5Jv%2F0wGN97JQURm%2BPzswXIbFTMtsac8BhnXkBqMC0udW%2BL2vpdGyIOMFJbc%2B7ngJTbgQYYSTgMCbaE7Z6%2B2INO8fmO094zU%2BHEMP%2FezNT8rXIIadNKZmEjH%2F3bORCY138QcFdzDk4MB02jLx6Y62aLJlGGHSV2dM8n7Y%2FlaOdp7Bq7AIgIGSYEuABTdr90MAr6ZRzsFMaKgvuF4nWW5pmRCg3f%2BDVkNZApobbmntklXnAxYmq0yFCg84AP0udwG4lNkW1i24smaUKdZPrr0ULippBDb3V%2B1UqnC2IWbSrsSO6%2BEZ4Ob8qLC1Mw3z4PgqqDFut%2BTJ8dhq2B82IVIZWvx6IUKJgPqTq18lceZEAtdQLivjAb43ppKNRqDPXhLhxgW0DwToWXPV0sIyIYmSMI7Hkn3DOOs2lIm%2FIET8cLcaq888qEH%2B1qmp5W6h4JfybAP%2F2tg9WYUFbb1EUiGMHZmXmgTRMWVfoMJWTiEvzXgxJARzSu193WFwPPP25lhb8rm%2BVRrSRcnaMIqWsMgGOqUBohYrxOQCl4eTs%2FSwiS3wLe5BSBoXIrVQR2o30Jo0xJWUkKyq9C7ESjVYuTOjglIY%2B6YkPvojjtKX6ubd10wkaiQntC6SEEfq9SKL4bWtOmA5MpA48t%2BbCN%2BMOY5VYadEdpFq4V2Ps%2BHw5Xm6MmbHYAGlIvRMMGXLh0KzvOjXp%2BLeShjDsXPXWfJYur7Uj5NJ1wUKnd%2BQQg7NipuNA%2B1JXLp19vB4&X-Amz-Signature=6d406c61d9324d3fada72d913bc97eeeb0e9550f4c86f041f87f71ad9c2c7970&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJAKEAWK%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Fd7Ilc5CsBfobsjSOZKLGGwf%2F5XD%2BfBhlMb7HQRh2HQIgD51%2BhoxakX7A3a5Vs3aszkVpdgkap8j6VzrIVkdYrvUqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJpqNbkiIYuuOAERxyrcA%2FF1mAmffwfka3ySAxhu21njN5eZe6%2BrZL%2BYVVgR9hZ4oExoKyZeepomPCZNI7kGYwFs6YWieQYPAiKV6jYBR5xSd%2Fq95bSuNx6RAV6DTk2UE%2Fhh5Jv%2F0wGN97JQURm%2BPzswXIbFTMtsac8BhnXkBqMC0udW%2BL2vpdGyIOMFJbc%2B7ngJTbgQYYSTgMCbaE7Z6%2B2INO8fmO094zU%2BHEMP%2FezNT8rXIIadNKZmEjH%2F3bORCY138QcFdzDk4MB02jLx6Y62aLJlGGHSV2dM8n7Y%2FlaOdp7Bq7AIgIGSYEuABTdr90MAr6ZRzsFMaKgvuF4nWW5pmRCg3f%2BDVkNZApobbmntklXnAxYmq0yFCg84AP0udwG4lNkW1i24smaUKdZPrr0ULippBDb3V%2B1UqnC2IWbSrsSO6%2BEZ4Ob8qLC1Mw3z4PgqqDFut%2BTJ8dhq2B82IVIZWvx6IUKJgPqTq18lceZEAtdQLivjAb43ppKNRqDPXhLhxgW0DwToWXPV0sIyIYmSMI7Hkn3DOOs2lIm%2FIET8cLcaq888qEH%2B1qmp5W6h4JfybAP%2F2tg9WYUFbb1EUiGMHZmXmgTRMWVfoMJWTiEvzXgxJARzSu193WFwPPP25lhb8rm%2BVRrSRcnaMIqWsMgGOqUBohYrxOQCl4eTs%2FSwiS3wLe5BSBoXIrVQR2o30Jo0xJWUkKyq9C7ESjVYuTOjglIY%2B6YkPvojjtKX6ubd10wkaiQntC6SEEfq9SKL4bWtOmA5MpA48t%2BbCN%2BMOY5VYadEdpFq4V2Ps%2BHw5Xm6MmbHYAGlIvRMMGXLh0KzvOjXp%2BLeShjDsXPXWfJYur7Uj5NJ1wUKnd%2BQQg7NipuNA%2B1JXLp19vB4&X-Amz-Signature=926a0e58e8372a4610cfa8186f2f3e2401c55d230244ec7a40c80eccdbf99402&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

