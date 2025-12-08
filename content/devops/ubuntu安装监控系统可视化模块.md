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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRXQH6XC%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHbf6eePJgf4iwmUJVA4%2FW7rEprP6cmmKs8Z2ODfNAzpAiEAxsFgcX2zIj6E94K7AFxWNaSBYYbd075IpKm%2BgpLdtPoqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEr6PhcU0aK6dxP5HSrcAx5Yb2EHyqoeRwytIxhx6G5AHNQiLK5kJuWA8URFuxTRkN%2BdPQ%2BmMXsKZPHOwgSgFEvscEjnCe0RIizDvgTvdYtACWYEuUMai6wc8IJahUB%2Fo2nSAjpO%2BkY4qYY%2FciPHa3i8IlpQhgklBJLbJG0Uai%2FZDVGi%2FhkVrT6Q%2BguUxRj2vm4ssO%2FQ8YFtPeqU%2BR%2FsE9NHbD44Y02FeXB%2Bfe72PuoOxJ8RAci5PTsQO95dFgXGtCQoE278T9GN5oRI7QhaY6HnvHVmTQBRQCE984IdW4YouqrC%2B5NrmZS%2Fp%2B6uO%2BGh6u8B5J0fm1fOMbrRabbfGFJnO5EbCUlKJUtoXUnJTOJAeHVRB1rNCoxQqQEnDFJAhuzLoPfDspMYj%2Bd4%2FfpPtrJE2AiYWNAtzxVbnoPAZ1yfGxgC4IAMsbZh8gxAevwICKcSDttrMExilf%2Flg1AHVbyus95DY%2FP3ElFI4%2ByW9pnRtQ833TbgSsHWuTEqO874qK%2BGY6ZS1Mu5R9girzFPDNofxwrEPu8b%2Fxkd%2F%2FIMcVGoGqS%2FX%2BHY8klr5Gz3aGErnlYdcYFQrTiqtS76rGl%2BEMZYjwBsvsFa2HniEV7SioxxdRxP70bno5lZh3cnnZlwe2yU30FbTUDkCGhHMKfu2MkGOqUBwSnPWd8SMIEQa0nUl7%2FHYUFY0B7POBDUcXiL0JhaCqeSCA0hNRYKrSvq7tt35c3twEHAhDmsrr8kaz0Yss0BEKlKWeoorlWPH2CchKwFjiQ111b8nlwHO8zlUnFVHYOzYfcky%2FWkcRlo25KnbEStPqpYarrJx%2Bs%2Fq5Dwh1ZSGPKD63Plknk70aEcFJZRPDw1M%2BBFi9eP%2FI50fxPTDbU149JGKIUC&X-Amz-Signature=f329bc471f22e77d4a10e7412a4d53672614b12173708d1da90f51e7cb5e73a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRXQH6XC%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHbf6eePJgf4iwmUJVA4%2FW7rEprP6cmmKs8Z2ODfNAzpAiEAxsFgcX2zIj6E94K7AFxWNaSBYYbd075IpKm%2BgpLdtPoqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEr6PhcU0aK6dxP5HSrcAx5Yb2EHyqoeRwytIxhx6G5AHNQiLK5kJuWA8URFuxTRkN%2BdPQ%2BmMXsKZPHOwgSgFEvscEjnCe0RIizDvgTvdYtACWYEuUMai6wc8IJahUB%2Fo2nSAjpO%2BkY4qYY%2FciPHa3i8IlpQhgklBJLbJG0Uai%2FZDVGi%2FhkVrT6Q%2BguUxRj2vm4ssO%2FQ8YFtPeqU%2BR%2FsE9NHbD44Y02FeXB%2Bfe72PuoOxJ8RAci5PTsQO95dFgXGtCQoE278T9GN5oRI7QhaY6HnvHVmTQBRQCE984IdW4YouqrC%2B5NrmZS%2Fp%2B6uO%2BGh6u8B5J0fm1fOMbrRabbfGFJnO5EbCUlKJUtoXUnJTOJAeHVRB1rNCoxQqQEnDFJAhuzLoPfDspMYj%2Bd4%2FfpPtrJE2AiYWNAtzxVbnoPAZ1yfGxgC4IAMsbZh8gxAevwICKcSDttrMExilf%2Flg1AHVbyus95DY%2FP3ElFI4%2ByW9pnRtQ833TbgSsHWuTEqO874qK%2BGY6ZS1Mu5R9girzFPDNofxwrEPu8b%2Fxkd%2F%2FIMcVGoGqS%2FX%2BHY8klr5Gz3aGErnlYdcYFQrTiqtS76rGl%2BEMZYjwBsvsFa2HniEV7SioxxdRxP70bno5lZh3cnnZlwe2yU30FbTUDkCGhHMKfu2MkGOqUBwSnPWd8SMIEQa0nUl7%2FHYUFY0B7POBDUcXiL0JhaCqeSCA0hNRYKrSvq7tt35c3twEHAhDmsrr8kaz0Yss0BEKlKWeoorlWPH2CchKwFjiQ111b8nlwHO8zlUnFVHYOzYfcky%2FWkcRlo25KnbEStPqpYarrJx%2Bs%2Fq5Dwh1ZSGPKD63Plknk70aEcFJZRPDw1M%2BBFi9eP%2FI50fxPTDbU149JGKIUC&X-Amz-Signature=dab748019f80ba6d1f63019ae956d258b198856ef567f4b77b462769cdfa8fd2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRXQH6XC%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHbf6eePJgf4iwmUJVA4%2FW7rEprP6cmmKs8Z2ODfNAzpAiEAxsFgcX2zIj6E94K7AFxWNaSBYYbd075IpKm%2BgpLdtPoqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEr6PhcU0aK6dxP5HSrcAx5Yb2EHyqoeRwytIxhx6G5AHNQiLK5kJuWA8URFuxTRkN%2BdPQ%2BmMXsKZPHOwgSgFEvscEjnCe0RIizDvgTvdYtACWYEuUMai6wc8IJahUB%2Fo2nSAjpO%2BkY4qYY%2FciPHa3i8IlpQhgklBJLbJG0Uai%2FZDVGi%2FhkVrT6Q%2BguUxRj2vm4ssO%2FQ8YFtPeqU%2BR%2FsE9NHbD44Y02FeXB%2Bfe72PuoOxJ8RAci5PTsQO95dFgXGtCQoE278T9GN5oRI7QhaY6HnvHVmTQBRQCE984IdW4YouqrC%2B5NrmZS%2Fp%2B6uO%2BGh6u8B5J0fm1fOMbrRabbfGFJnO5EbCUlKJUtoXUnJTOJAeHVRB1rNCoxQqQEnDFJAhuzLoPfDspMYj%2Bd4%2FfpPtrJE2AiYWNAtzxVbnoPAZ1yfGxgC4IAMsbZh8gxAevwICKcSDttrMExilf%2Flg1AHVbyus95DY%2FP3ElFI4%2ByW9pnRtQ833TbgSsHWuTEqO874qK%2BGY6ZS1Mu5R9girzFPDNofxwrEPu8b%2Fxkd%2F%2FIMcVGoGqS%2FX%2BHY8klr5Gz3aGErnlYdcYFQrTiqtS76rGl%2BEMZYjwBsvsFa2HniEV7SioxxdRxP70bno5lZh3cnnZlwe2yU30FbTUDkCGhHMKfu2MkGOqUBwSnPWd8SMIEQa0nUl7%2FHYUFY0B7POBDUcXiL0JhaCqeSCA0hNRYKrSvq7tt35c3twEHAhDmsrr8kaz0Yss0BEKlKWeoorlWPH2CchKwFjiQ111b8nlwHO8zlUnFVHYOzYfcky%2FWkcRlo25KnbEStPqpYarrJx%2Bs%2Fq5Dwh1ZSGPKD63Plknk70aEcFJZRPDw1M%2BBFi9eP%2FI50fxPTDbU149JGKIUC&X-Amz-Signature=5456f2f2a967f0b424f0fec494910c8cf026032b1f6a892d9b8fb4aa75dbedf1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRXQH6XC%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHbf6eePJgf4iwmUJVA4%2FW7rEprP6cmmKs8Z2ODfNAzpAiEAxsFgcX2zIj6E94K7AFxWNaSBYYbd075IpKm%2BgpLdtPoqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEr6PhcU0aK6dxP5HSrcAx5Yb2EHyqoeRwytIxhx6G5AHNQiLK5kJuWA8URFuxTRkN%2BdPQ%2BmMXsKZPHOwgSgFEvscEjnCe0RIizDvgTvdYtACWYEuUMai6wc8IJahUB%2Fo2nSAjpO%2BkY4qYY%2FciPHa3i8IlpQhgklBJLbJG0Uai%2FZDVGi%2FhkVrT6Q%2BguUxRj2vm4ssO%2FQ8YFtPeqU%2BR%2FsE9NHbD44Y02FeXB%2Bfe72PuoOxJ8RAci5PTsQO95dFgXGtCQoE278T9GN5oRI7QhaY6HnvHVmTQBRQCE984IdW4YouqrC%2B5NrmZS%2Fp%2B6uO%2BGh6u8B5J0fm1fOMbrRabbfGFJnO5EbCUlKJUtoXUnJTOJAeHVRB1rNCoxQqQEnDFJAhuzLoPfDspMYj%2Bd4%2FfpPtrJE2AiYWNAtzxVbnoPAZ1yfGxgC4IAMsbZh8gxAevwICKcSDttrMExilf%2Flg1AHVbyus95DY%2FP3ElFI4%2ByW9pnRtQ833TbgSsHWuTEqO874qK%2BGY6ZS1Mu5R9girzFPDNofxwrEPu8b%2Fxkd%2F%2FIMcVGoGqS%2FX%2BHY8klr5Gz3aGErnlYdcYFQrTiqtS76rGl%2BEMZYjwBsvsFa2HniEV7SioxxdRxP70bno5lZh3cnnZlwe2yU30FbTUDkCGhHMKfu2MkGOqUBwSnPWd8SMIEQa0nUl7%2FHYUFY0B7POBDUcXiL0JhaCqeSCA0hNRYKrSvq7tt35c3twEHAhDmsrr8kaz0Yss0BEKlKWeoorlWPH2CchKwFjiQ111b8nlwHO8zlUnFVHYOzYfcky%2FWkcRlo25KnbEStPqpYarrJx%2Bs%2Fq5Dwh1ZSGPKD63Plknk70aEcFJZRPDw1M%2BBFi9eP%2FI50fxPTDbU149JGKIUC&X-Amz-Signature=40740bbb026b38f1e489445a5d409951d34f4e3fee41b2faf79ce4d1b45188a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRXQH6XC%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHbf6eePJgf4iwmUJVA4%2FW7rEprP6cmmKs8Z2ODfNAzpAiEAxsFgcX2zIj6E94K7AFxWNaSBYYbd075IpKm%2BgpLdtPoqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEr6PhcU0aK6dxP5HSrcAx5Yb2EHyqoeRwytIxhx6G5AHNQiLK5kJuWA8URFuxTRkN%2BdPQ%2BmMXsKZPHOwgSgFEvscEjnCe0RIizDvgTvdYtACWYEuUMai6wc8IJahUB%2Fo2nSAjpO%2BkY4qYY%2FciPHa3i8IlpQhgklBJLbJG0Uai%2FZDVGi%2FhkVrT6Q%2BguUxRj2vm4ssO%2FQ8YFtPeqU%2BR%2FsE9NHbD44Y02FeXB%2Bfe72PuoOxJ8RAci5PTsQO95dFgXGtCQoE278T9GN5oRI7QhaY6HnvHVmTQBRQCE984IdW4YouqrC%2B5NrmZS%2Fp%2B6uO%2BGh6u8B5J0fm1fOMbrRabbfGFJnO5EbCUlKJUtoXUnJTOJAeHVRB1rNCoxQqQEnDFJAhuzLoPfDspMYj%2Bd4%2FfpPtrJE2AiYWNAtzxVbnoPAZ1yfGxgC4IAMsbZh8gxAevwICKcSDttrMExilf%2Flg1AHVbyus95DY%2FP3ElFI4%2ByW9pnRtQ833TbgSsHWuTEqO874qK%2BGY6ZS1Mu5R9girzFPDNofxwrEPu8b%2Fxkd%2F%2FIMcVGoGqS%2FX%2BHY8klr5Gz3aGErnlYdcYFQrTiqtS76rGl%2BEMZYjwBsvsFa2HniEV7SioxxdRxP70bno5lZh3cnnZlwe2yU30FbTUDkCGhHMKfu2MkGOqUBwSnPWd8SMIEQa0nUl7%2FHYUFY0B7POBDUcXiL0JhaCqeSCA0hNRYKrSvq7tt35c3twEHAhDmsrr8kaz0Yss0BEKlKWeoorlWPH2CchKwFjiQ111b8nlwHO8zlUnFVHYOzYfcky%2FWkcRlo25KnbEStPqpYarrJx%2Bs%2Fq5Dwh1ZSGPKD63Plknk70aEcFJZRPDw1M%2BBFi9eP%2FI50fxPTDbU149JGKIUC&X-Amz-Signature=0caa64eab326aef6b0b67aa311a0480adb0b27c16acbbe3bf785a162cafe0c94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRXQH6XC%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHbf6eePJgf4iwmUJVA4%2FW7rEprP6cmmKs8Z2ODfNAzpAiEAxsFgcX2zIj6E94K7AFxWNaSBYYbd075IpKm%2BgpLdtPoqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEr6PhcU0aK6dxP5HSrcAx5Yb2EHyqoeRwytIxhx6G5AHNQiLK5kJuWA8URFuxTRkN%2BdPQ%2BmMXsKZPHOwgSgFEvscEjnCe0RIizDvgTvdYtACWYEuUMai6wc8IJahUB%2Fo2nSAjpO%2BkY4qYY%2FciPHa3i8IlpQhgklBJLbJG0Uai%2FZDVGi%2FhkVrT6Q%2BguUxRj2vm4ssO%2FQ8YFtPeqU%2BR%2FsE9NHbD44Y02FeXB%2Bfe72PuoOxJ8RAci5PTsQO95dFgXGtCQoE278T9GN5oRI7QhaY6HnvHVmTQBRQCE984IdW4YouqrC%2B5NrmZS%2Fp%2B6uO%2BGh6u8B5J0fm1fOMbrRabbfGFJnO5EbCUlKJUtoXUnJTOJAeHVRB1rNCoxQqQEnDFJAhuzLoPfDspMYj%2Bd4%2FfpPtrJE2AiYWNAtzxVbnoPAZ1yfGxgC4IAMsbZh8gxAevwICKcSDttrMExilf%2Flg1AHVbyus95DY%2FP3ElFI4%2ByW9pnRtQ833TbgSsHWuTEqO874qK%2BGY6ZS1Mu5R9girzFPDNofxwrEPu8b%2Fxkd%2F%2FIMcVGoGqS%2FX%2BHY8klr5Gz3aGErnlYdcYFQrTiqtS76rGl%2BEMZYjwBsvsFa2HniEV7SioxxdRxP70bno5lZh3cnnZlwe2yU30FbTUDkCGhHMKfu2MkGOqUBwSnPWd8SMIEQa0nUl7%2FHYUFY0B7POBDUcXiL0JhaCqeSCA0hNRYKrSvq7tt35c3twEHAhDmsrr8kaz0Yss0BEKlKWeoorlWPH2CchKwFjiQ111b8nlwHO8zlUnFVHYOzYfcky%2FWkcRlo25KnbEStPqpYarrJx%2Bs%2Fq5Dwh1ZSGPKD63Plknk70aEcFJZRPDw1M%2BBFi9eP%2FI50fxPTDbU149JGKIUC&X-Amz-Signature=1d22bce03a24e326b76b86158afcdea3c41c85be906c39ccda4ec16d01031fd3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRXQH6XC%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHbf6eePJgf4iwmUJVA4%2FW7rEprP6cmmKs8Z2ODfNAzpAiEAxsFgcX2zIj6E94K7AFxWNaSBYYbd075IpKm%2BgpLdtPoqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEr6PhcU0aK6dxP5HSrcAx5Yb2EHyqoeRwytIxhx6G5AHNQiLK5kJuWA8URFuxTRkN%2BdPQ%2BmMXsKZPHOwgSgFEvscEjnCe0RIizDvgTvdYtACWYEuUMai6wc8IJahUB%2Fo2nSAjpO%2BkY4qYY%2FciPHa3i8IlpQhgklBJLbJG0Uai%2FZDVGi%2FhkVrT6Q%2BguUxRj2vm4ssO%2FQ8YFtPeqU%2BR%2FsE9NHbD44Y02FeXB%2Bfe72PuoOxJ8RAci5PTsQO95dFgXGtCQoE278T9GN5oRI7QhaY6HnvHVmTQBRQCE984IdW4YouqrC%2B5NrmZS%2Fp%2B6uO%2BGh6u8B5J0fm1fOMbrRabbfGFJnO5EbCUlKJUtoXUnJTOJAeHVRB1rNCoxQqQEnDFJAhuzLoPfDspMYj%2Bd4%2FfpPtrJE2AiYWNAtzxVbnoPAZ1yfGxgC4IAMsbZh8gxAevwICKcSDttrMExilf%2Flg1AHVbyus95DY%2FP3ElFI4%2ByW9pnRtQ833TbgSsHWuTEqO874qK%2BGY6ZS1Mu5R9girzFPDNofxwrEPu8b%2Fxkd%2F%2FIMcVGoGqS%2FX%2BHY8klr5Gz3aGErnlYdcYFQrTiqtS76rGl%2BEMZYjwBsvsFa2HniEV7SioxxdRxP70bno5lZh3cnnZlwe2yU30FbTUDkCGhHMKfu2MkGOqUBwSnPWd8SMIEQa0nUl7%2FHYUFY0B7POBDUcXiL0JhaCqeSCA0hNRYKrSvq7tt35c3twEHAhDmsrr8kaz0Yss0BEKlKWeoorlWPH2CchKwFjiQ111b8nlwHO8zlUnFVHYOzYfcky%2FWkcRlo25KnbEStPqpYarrJx%2Bs%2Fq5Dwh1ZSGPKD63Plknk70aEcFJZRPDw1M%2BBFi9eP%2FI50fxPTDbU149JGKIUC&X-Amz-Signature=131ef165a8f734506b67fc6a05822e4ac4aef53c496fdf9fd4b25f2212dd3cd8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

