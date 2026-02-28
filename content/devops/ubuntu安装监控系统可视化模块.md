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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKLIWXRH%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKWRwOLtiSAv4k%2FXgz1DVnV4gySHJHekOHdyey0cmofgIgP%2B%2F78JsYAkkqRrEkr2%2FoKxjF659qKonMetnelyyPqa0q%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDF1wvFNeM1BIxjBVOyrcAw2kMcDl6XVGhx3ylH07XHISwUTIAzNTAhhLBawokeIkmpO6bctljApbuKeJ6LQ26dExn2DDG88Mqm%2FB1E0qsVaqeafWalm%2Buz38GLWzvdWChsdnOPOcO4Z6QGRzj1Y9n8Tr4yGoVMyH%2B4XKicUodv4mAJdeuuajvdOlJp1%2BSA0EuiLmxaZ1tnUNIV4f5ajIIwxMwR1bu4Mj7ahYigO1M%2Bx%2Bcl9elHOTpq%2BFvMFIUyA92XpYlcXoAZMRdid%2F%2Bq12o%2F0X7sAXzv1zPJ3L1T2dq%2FJcecdJR3VGUVfADcEjx%2FII6zHZOp82a71uiKJodndihyyKuHSWpAvHZvQdwJy99azr0FzmnWO%2F%2BYP9JAY5B0%2FRIRmVN9e0xUQgMnEAgYMMSeV1qbbTLpQaGMIpg69T%2BkdDOhvqaBn7xm%2BVNyeSYaHi4kYsX1NUES8ZmeRY%2Fc5gcIQn3QlKRhCYmHnJCdaJdWh4W6Bo7cfpJ8v2Uozhld8CvW9DL8SkNkgZnsdbR5XM4h%2FB7yB9dG5iQoAzl7ziZoOsBaciGpOfIUKTc5UAWduF1gPitEdGw%2FCRlpzZ60ZSzU7wqZKyHr78y6yuXBKBEe%2FPS7nbyybeBng5d4QYUZuMiArb9HTxImWxhDY0MLWWic0GOqUBNChuVOWkmsRhqf9CostwCn%2FAf6%2Bs6Y0FjioIo74Tzf2vMwLF0VfcQ%2BpnRCKH7%2B9z2z5UEQsyHkrUjkrwrOGKYzxNz5RuY8DPJugn5uYu1b7DjxT8deULdtZOHRj0RmUA%2FeiVgWXxdfTpGsz%2Fq49zalG7YorAuhEkp5EpmiSvsFHBZZL2omZKBm2mm%2BhECN0ULXlFtQbDMHbGk%2FdclPa2%2BA1PyW%2Fc&X-Amz-Signature=4572da5f723714c0088d4c9697b79f1e59d768a56053b5de1180753e6ca791ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKLIWXRH%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKWRwOLtiSAv4k%2FXgz1DVnV4gySHJHekOHdyey0cmofgIgP%2B%2F78JsYAkkqRrEkr2%2FoKxjF659qKonMetnelyyPqa0q%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDF1wvFNeM1BIxjBVOyrcAw2kMcDl6XVGhx3ylH07XHISwUTIAzNTAhhLBawokeIkmpO6bctljApbuKeJ6LQ26dExn2DDG88Mqm%2FB1E0qsVaqeafWalm%2Buz38GLWzvdWChsdnOPOcO4Z6QGRzj1Y9n8Tr4yGoVMyH%2B4XKicUodv4mAJdeuuajvdOlJp1%2BSA0EuiLmxaZ1tnUNIV4f5ajIIwxMwR1bu4Mj7ahYigO1M%2Bx%2Bcl9elHOTpq%2BFvMFIUyA92XpYlcXoAZMRdid%2F%2Bq12o%2F0X7sAXzv1zPJ3L1T2dq%2FJcecdJR3VGUVfADcEjx%2FII6zHZOp82a71uiKJodndihyyKuHSWpAvHZvQdwJy99azr0FzmnWO%2F%2BYP9JAY5B0%2FRIRmVN9e0xUQgMnEAgYMMSeV1qbbTLpQaGMIpg69T%2BkdDOhvqaBn7xm%2BVNyeSYaHi4kYsX1NUES8ZmeRY%2Fc5gcIQn3QlKRhCYmHnJCdaJdWh4W6Bo7cfpJ8v2Uozhld8CvW9DL8SkNkgZnsdbR5XM4h%2FB7yB9dG5iQoAzl7ziZoOsBaciGpOfIUKTc5UAWduF1gPitEdGw%2FCRlpzZ60ZSzU7wqZKyHr78y6yuXBKBEe%2FPS7nbyybeBng5d4QYUZuMiArb9HTxImWxhDY0MLWWic0GOqUBNChuVOWkmsRhqf9CostwCn%2FAf6%2Bs6Y0FjioIo74Tzf2vMwLF0VfcQ%2BpnRCKH7%2B9z2z5UEQsyHkrUjkrwrOGKYzxNz5RuY8DPJugn5uYu1b7DjxT8deULdtZOHRj0RmUA%2FeiVgWXxdfTpGsz%2Fq49zalG7YorAuhEkp5EpmiSvsFHBZZL2omZKBm2mm%2BhECN0ULXlFtQbDMHbGk%2FdclPa2%2BA1PyW%2Fc&X-Amz-Signature=1e047cfa9cb4a1c46712e3397b31dfdf49ee7a08a57d7d1537ca8feaba6ec6a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKLIWXRH%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKWRwOLtiSAv4k%2FXgz1DVnV4gySHJHekOHdyey0cmofgIgP%2B%2F78JsYAkkqRrEkr2%2FoKxjF659qKonMetnelyyPqa0q%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDF1wvFNeM1BIxjBVOyrcAw2kMcDl6XVGhx3ylH07XHISwUTIAzNTAhhLBawokeIkmpO6bctljApbuKeJ6LQ26dExn2DDG88Mqm%2FB1E0qsVaqeafWalm%2Buz38GLWzvdWChsdnOPOcO4Z6QGRzj1Y9n8Tr4yGoVMyH%2B4XKicUodv4mAJdeuuajvdOlJp1%2BSA0EuiLmxaZ1tnUNIV4f5ajIIwxMwR1bu4Mj7ahYigO1M%2Bx%2Bcl9elHOTpq%2BFvMFIUyA92XpYlcXoAZMRdid%2F%2Bq12o%2F0X7sAXzv1zPJ3L1T2dq%2FJcecdJR3VGUVfADcEjx%2FII6zHZOp82a71uiKJodndihyyKuHSWpAvHZvQdwJy99azr0FzmnWO%2F%2BYP9JAY5B0%2FRIRmVN9e0xUQgMnEAgYMMSeV1qbbTLpQaGMIpg69T%2BkdDOhvqaBn7xm%2BVNyeSYaHi4kYsX1NUES8ZmeRY%2Fc5gcIQn3QlKRhCYmHnJCdaJdWh4W6Bo7cfpJ8v2Uozhld8CvW9DL8SkNkgZnsdbR5XM4h%2FB7yB9dG5iQoAzl7ziZoOsBaciGpOfIUKTc5UAWduF1gPitEdGw%2FCRlpzZ60ZSzU7wqZKyHr78y6yuXBKBEe%2FPS7nbyybeBng5d4QYUZuMiArb9HTxImWxhDY0MLWWic0GOqUBNChuVOWkmsRhqf9CostwCn%2FAf6%2Bs6Y0FjioIo74Tzf2vMwLF0VfcQ%2BpnRCKH7%2B9z2z5UEQsyHkrUjkrwrOGKYzxNz5RuY8DPJugn5uYu1b7DjxT8deULdtZOHRj0RmUA%2FeiVgWXxdfTpGsz%2Fq49zalG7YorAuhEkp5EpmiSvsFHBZZL2omZKBm2mm%2BhECN0ULXlFtQbDMHbGk%2FdclPa2%2BA1PyW%2Fc&X-Amz-Signature=c60d4c30797421aa2a3cbed3727078e5534aefdcf746bde6da8bf1e0d6b3fa3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKLIWXRH%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKWRwOLtiSAv4k%2FXgz1DVnV4gySHJHekOHdyey0cmofgIgP%2B%2F78JsYAkkqRrEkr2%2FoKxjF659qKonMetnelyyPqa0q%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDF1wvFNeM1BIxjBVOyrcAw2kMcDl6XVGhx3ylH07XHISwUTIAzNTAhhLBawokeIkmpO6bctljApbuKeJ6LQ26dExn2DDG88Mqm%2FB1E0qsVaqeafWalm%2Buz38GLWzvdWChsdnOPOcO4Z6QGRzj1Y9n8Tr4yGoVMyH%2B4XKicUodv4mAJdeuuajvdOlJp1%2BSA0EuiLmxaZ1tnUNIV4f5ajIIwxMwR1bu4Mj7ahYigO1M%2Bx%2Bcl9elHOTpq%2BFvMFIUyA92XpYlcXoAZMRdid%2F%2Bq12o%2F0X7sAXzv1zPJ3L1T2dq%2FJcecdJR3VGUVfADcEjx%2FII6zHZOp82a71uiKJodndihyyKuHSWpAvHZvQdwJy99azr0FzmnWO%2F%2BYP9JAY5B0%2FRIRmVN9e0xUQgMnEAgYMMSeV1qbbTLpQaGMIpg69T%2BkdDOhvqaBn7xm%2BVNyeSYaHi4kYsX1NUES8ZmeRY%2Fc5gcIQn3QlKRhCYmHnJCdaJdWh4W6Bo7cfpJ8v2Uozhld8CvW9DL8SkNkgZnsdbR5XM4h%2FB7yB9dG5iQoAzl7ziZoOsBaciGpOfIUKTc5UAWduF1gPitEdGw%2FCRlpzZ60ZSzU7wqZKyHr78y6yuXBKBEe%2FPS7nbyybeBng5d4QYUZuMiArb9HTxImWxhDY0MLWWic0GOqUBNChuVOWkmsRhqf9CostwCn%2FAf6%2Bs6Y0FjioIo74Tzf2vMwLF0VfcQ%2BpnRCKH7%2B9z2z5UEQsyHkrUjkrwrOGKYzxNz5RuY8DPJugn5uYu1b7DjxT8deULdtZOHRj0RmUA%2FeiVgWXxdfTpGsz%2Fq49zalG7YorAuhEkp5EpmiSvsFHBZZL2omZKBm2mm%2BhECN0ULXlFtQbDMHbGk%2FdclPa2%2BA1PyW%2Fc&X-Amz-Signature=68237e465ee41310786ec1f1f9be409f6e0d931e38fd65ca13866722b7151a75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKLIWXRH%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKWRwOLtiSAv4k%2FXgz1DVnV4gySHJHekOHdyey0cmofgIgP%2B%2F78JsYAkkqRrEkr2%2FoKxjF659qKonMetnelyyPqa0q%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDF1wvFNeM1BIxjBVOyrcAw2kMcDl6XVGhx3ylH07XHISwUTIAzNTAhhLBawokeIkmpO6bctljApbuKeJ6LQ26dExn2DDG88Mqm%2FB1E0qsVaqeafWalm%2Buz38GLWzvdWChsdnOPOcO4Z6QGRzj1Y9n8Tr4yGoVMyH%2B4XKicUodv4mAJdeuuajvdOlJp1%2BSA0EuiLmxaZ1tnUNIV4f5ajIIwxMwR1bu4Mj7ahYigO1M%2Bx%2Bcl9elHOTpq%2BFvMFIUyA92XpYlcXoAZMRdid%2F%2Bq12o%2F0X7sAXzv1zPJ3L1T2dq%2FJcecdJR3VGUVfADcEjx%2FII6zHZOp82a71uiKJodndihyyKuHSWpAvHZvQdwJy99azr0FzmnWO%2F%2BYP9JAY5B0%2FRIRmVN9e0xUQgMnEAgYMMSeV1qbbTLpQaGMIpg69T%2BkdDOhvqaBn7xm%2BVNyeSYaHi4kYsX1NUES8ZmeRY%2Fc5gcIQn3QlKRhCYmHnJCdaJdWh4W6Bo7cfpJ8v2Uozhld8CvW9DL8SkNkgZnsdbR5XM4h%2FB7yB9dG5iQoAzl7ziZoOsBaciGpOfIUKTc5UAWduF1gPitEdGw%2FCRlpzZ60ZSzU7wqZKyHr78y6yuXBKBEe%2FPS7nbyybeBng5d4QYUZuMiArb9HTxImWxhDY0MLWWic0GOqUBNChuVOWkmsRhqf9CostwCn%2FAf6%2Bs6Y0FjioIo74Tzf2vMwLF0VfcQ%2BpnRCKH7%2B9z2z5UEQsyHkrUjkrwrOGKYzxNz5RuY8DPJugn5uYu1b7DjxT8deULdtZOHRj0RmUA%2FeiVgWXxdfTpGsz%2Fq49zalG7YorAuhEkp5EpmiSvsFHBZZL2omZKBm2mm%2BhECN0ULXlFtQbDMHbGk%2FdclPa2%2BA1PyW%2Fc&X-Amz-Signature=de38643c378356318f7dfc47c6a888c8f4189fbde7bae516642f733d336c2196&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKLIWXRH%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKWRwOLtiSAv4k%2FXgz1DVnV4gySHJHekOHdyey0cmofgIgP%2B%2F78JsYAkkqRrEkr2%2FoKxjF659qKonMetnelyyPqa0q%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDF1wvFNeM1BIxjBVOyrcAw2kMcDl6XVGhx3ylH07XHISwUTIAzNTAhhLBawokeIkmpO6bctljApbuKeJ6LQ26dExn2DDG88Mqm%2FB1E0qsVaqeafWalm%2Buz38GLWzvdWChsdnOPOcO4Z6QGRzj1Y9n8Tr4yGoVMyH%2B4XKicUodv4mAJdeuuajvdOlJp1%2BSA0EuiLmxaZ1tnUNIV4f5ajIIwxMwR1bu4Mj7ahYigO1M%2Bx%2Bcl9elHOTpq%2BFvMFIUyA92XpYlcXoAZMRdid%2F%2Bq12o%2F0X7sAXzv1zPJ3L1T2dq%2FJcecdJR3VGUVfADcEjx%2FII6zHZOp82a71uiKJodndihyyKuHSWpAvHZvQdwJy99azr0FzmnWO%2F%2BYP9JAY5B0%2FRIRmVN9e0xUQgMnEAgYMMSeV1qbbTLpQaGMIpg69T%2BkdDOhvqaBn7xm%2BVNyeSYaHi4kYsX1NUES8ZmeRY%2Fc5gcIQn3QlKRhCYmHnJCdaJdWh4W6Bo7cfpJ8v2Uozhld8CvW9DL8SkNkgZnsdbR5XM4h%2FB7yB9dG5iQoAzl7ziZoOsBaciGpOfIUKTc5UAWduF1gPitEdGw%2FCRlpzZ60ZSzU7wqZKyHr78y6yuXBKBEe%2FPS7nbyybeBng5d4QYUZuMiArb9HTxImWxhDY0MLWWic0GOqUBNChuVOWkmsRhqf9CostwCn%2FAf6%2Bs6Y0FjioIo74Tzf2vMwLF0VfcQ%2BpnRCKH7%2B9z2z5UEQsyHkrUjkrwrOGKYzxNz5RuY8DPJugn5uYu1b7DjxT8deULdtZOHRj0RmUA%2FeiVgWXxdfTpGsz%2Fq49zalG7YorAuhEkp5EpmiSvsFHBZZL2omZKBm2mm%2BhECN0ULXlFtQbDMHbGk%2FdclPa2%2BA1PyW%2Fc&X-Amz-Signature=da41f6366aafab5ed8814c0c3fd38d10ce18d6fb28c2ad4121ed3c1511d1ba46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKLIWXRH%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKWRwOLtiSAv4k%2FXgz1DVnV4gySHJHekOHdyey0cmofgIgP%2B%2F78JsYAkkqRrEkr2%2FoKxjF659qKonMetnelyyPqa0q%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDF1wvFNeM1BIxjBVOyrcAw2kMcDl6XVGhx3ylH07XHISwUTIAzNTAhhLBawokeIkmpO6bctljApbuKeJ6LQ26dExn2DDG88Mqm%2FB1E0qsVaqeafWalm%2Buz38GLWzvdWChsdnOPOcO4Z6QGRzj1Y9n8Tr4yGoVMyH%2B4XKicUodv4mAJdeuuajvdOlJp1%2BSA0EuiLmxaZ1tnUNIV4f5ajIIwxMwR1bu4Mj7ahYigO1M%2Bx%2Bcl9elHOTpq%2BFvMFIUyA92XpYlcXoAZMRdid%2F%2Bq12o%2F0X7sAXzv1zPJ3L1T2dq%2FJcecdJR3VGUVfADcEjx%2FII6zHZOp82a71uiKJodndihyyKuHSWpAvHZvQdwJy99azr0FzmnWO%2F%2BYP9JAY5B0%2FRIRmVN9e0xUQgMnEAgYMMSeV1qbbTLpQaGMIpg69T%2BkdDOhvqaBn7xm%2BVNyeSYaHi4kYsX1NUES8ZmeRY%2Fc5gcIQn3QlKRhCYmHnJCdaJdWh4W6Bo7cfpJ8v2Uozhld8CvW9DL8SkNkgZnsdbR5XM4h%2FB7yB9dG5iQoAzl7ziZoOsBaciGpOfIUKTc5UAWduF1gPitEdGw%2FCRlpzZ60ZSzU7wqZKyHr78y6yuXBKBEe%2FPS7nbyybeBng5d4QYUZuMiArb9HTxImWxhDY0MLWWic0GOqUBNChuVOWkmsRhqf9CostwCn%2FAf6%2Bs6Y0FjioIo74Tzf2vMwLF0VfcQ%2BpnRCKH7%2B9z2z5UEQsyHkrUjkrwrOGKYzxNz5RuY8DPJugn5uYu1b7DjxT8deULdtZOHRj0RmUA%2FeiVgWXxdfTpGsz%2Fq49zalG7YorAuhEkp5EpmiSvsFHBZZL2omZKBm2mm%2BhECN0ULXlFtQbDMHbGk%2FdclPa2%2BA1PyW%2Fc&X-Amz-Signature=6a7a6ee8751988c606d53beb19536cae727efd87ad6d8b2ffea3c9b4aafb8c89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

