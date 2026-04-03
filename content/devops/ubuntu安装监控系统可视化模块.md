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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC42AEG3%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBmeLA7hSx7TR30a59epz3CdXxMhrs6h9qNIaXOWiHPYAiEAjbQrtltab1lGF%2FY8K1%2FAx3TCGKO5R7Z%2B6gqO0Sn%2Bcqkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDEjr6Pr9FaQV2ydLISrcA0yZv1eETN7Xz1UJ6K0CoIF8o%2FqYJIe4XKM8Mel7FDl6GzyXz1brhGTSuJaD1ir%2F0oZMJ8UKwZotzTDgV7%2F7MkCaF1jE0BpL4iXJTm7Cbxz2iAKfbfQSB14%2F0IqhuSfGx5a%2BCYtLcgwjqL%2BuN3sz%2FU3UcNQhKsO8oCSNqVJo2CZJHW%2FW1JDftmYF5kaalVLWZQYQ3uhglqDHTxbHf0o68vARFsZPscq84VLaeFAaVB1bm2jYlBCqe%2F9PBaULwVjVXrN1SE6gp%2BWZH6SK91EW5FUUVcrj1JamYT8UG7dKWU%2FXDJS97p1IS7mQBZKJRaPowElbutWpFNrNBo8Mp9BtystrSkEjPdU5JfC5eAdkc1rUqTy0ttw480Z8Kpg2urn5YKavHfoVh2uPeqmqpsDV37aKanymCqAjYhylsCP2w4d5Lbyh%2BrWUk9EHhQYoIb1fmZf2NHSpvMBw8vAvyLZE0iz%2BxWvdhhdzZf1CBJpDAtAmX65KT7ElQ14JyQDzImwU8hhofB3I07dwU4z5i7Tk%2FU%2BZ9BDyzIP%2B6o2WkhPAP%2B4wBCKuHW32bWMfe%2B4f8QKCSNAxSaRhaR0aGwtf%2F4xCDp14nNe8nW1xAS0sYgt1ddiOAWAK3a3mWpSqaL1wMI2svc4GOqUB53Dhtru16cjIlfAaWcgwSTqtKgTxsn7vLjL4liFpmLEcPaTDS3OtwS9XnQoMImPZkNmpJNd2b4KwnCTPO5SX5igI7JpRX5md2ZFGZcyg%2BNWdPs0XYor0SaUI8NcriaCCok0aER1VR85nHQ9ERLEAI6P70IQKevhwaCpfkMHtRJgcZfKSAL27TQtVCLw7xvkYPLKgbaOIxybjA3jB8yh2rMrPI7RA&X-Amz-Signature=2845bd4d036df1d566f59c68c845dcef2c0c9ca0e7363ee94fd6cd165eb2a158&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC42AEG3%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBmeLA7hSx7TR30a59epz3CdXxMhrs6h9qNIaXOWiHPYAiEAjbQrtltab1lGF%2FY8K1%2FAx3TCGKO5R7Z%2B6gqO0Sn%2Bcqkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDEjr6Pr9FaQV2ydLISrcA0yZv1eETN7Xz1UJ6K0CoIF8o%2FqYJIe4XKM8Mel7FDl6GzyXz1brhGTSuJaD1ir%2F0oZMJ8UKwZotzTDgV7%2F7MkCaF1jE0BpL4iXJTm7Cbxz2iAKfbfQSB14%2F0IqhuSfGx5a%2BCYtLcgwjqL%2BuN3sz%2FU3UcNQhKsO8oCSNqVJo2CZJHW%2FW1JDftmYF5kaalVLWZQYQ3uhglqDHTxbHf0o68vARFsZPscq84VLaeFAaVB1bm2jYlBCqe%2F9PBaULwVjVXrN1SE6gp%2BWZH6SK91EW5FUUVcrj1JamYT8UG7dKWU%2FXDJS97p1IS7mQBZKJRaPowElbutWpFNrNBo8Mp9BtystrSkEjPdU5JfC5eAdkc1rUqTy0ttw480Z8Kpg2urn5YKavHfoVh2uPeqmqpsDV37aKanymCqAjYhylsCP2w4d5Lbyh%2BrWUk9EHhQYoIb1fmZf2NHSpvMBw8vAvyLZE0iz%2BxWvdhhdzZf1CBJpDAtAmX65KT7ElQ14JyQDzImwU8hhofB3I07dwU4z5i7Tk%2FU%2BZ9BDyzIP%2B6o2WkhPAP%2B4wBCKuHW32bWMfe%2B4f8QKCSNAxSaRhaR0aGwtf%2F4xCDp14nNe8nW1xAS0sYgt1ddiOAWAK3a3mWpSqaL1wMI2svc4GOqUB53Dhtru16cjIlfAaWcgwSTqtKgTxsn7vLjL4liFpmLEcPaTDS3OtwS9XnQoMImPZkNmpJNd2b4KwnCTPO5SX5igI7JpRX5md2ZFGZcyg%2BNWdPs0XYor0SaUI8NcriaCCok0aER1VR85nHQ9ERLEAI6P70IQKevhwaCpfkMHtRJgcZfKSAL27TQtVCLw7xvkYPLKgbaOIxybjA3jB8yh2rMrPI7RA&X-Amz-Signature=d447d9b9eb791d433f4cf30b780c9d33b79c198d5958e3cb12fd37fb3b041e81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC42AEG3%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBmeLA7hSx7TR30a59epz3CdXxMhrs6h9qNIaXOWiHPYAiEAjbQrtltab1lGF%2FY8K1%2FAx3TCGKO5R7Z%2B6gqO0Sn%2Bcqkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDEjr6Pr9FaQV2ydLISrcA0yZv1eETN7Xz1UJ6K0CoIF8o%2FqYJIe4XKM8Mel7FDl6GzyXz1brhGTSuJaD1ir%2F0oZMJ8UKwZotzTDgV7%2F7MkCaF1jE0BpL4iXJTm7Cbxz2iAKfbfQSB14%2F0IqhuSfGx5a%2BCYtLcgwjqL%2BuN3sz%2FU3UcNQhKsO8oCSNqVJo2CZJHW%2FW1JDftmYF5kaalVLWZQYQ3uhglqDHTxbHf0o68vARFsZPscq84VLaeFAaVB1bm2jYlBCqe%2F9PBaULwVjVXrN1SE6gp%2BWZH6SK91EW5FUUVcrj1JamYT8UG7dKWU%2FXDJS97p1IS7mQBZKJRaPowElbutWpFNrNBo8Mp9BtystrSkEjPdU5JfC5eAdkc1rUqTy0ttw480Z8Kpg2urn5YKavHfoVh2uPeqmqpsDV37aKanymCqAjYhylsCP2w4d5Lbyh%2BrWUk9EHhQYoIb1fmZf2NHSpvMBw8vAvyLZE0iz%2BxWvdhhdzZf1CBJpDAtAmX65KT7ElQ14JyQDzImwU8hhofB3I07dwU4z5i7Tk%2FU%2BZ9BDyzIP%2B6o2WkhPAP%2B4wBCKuHW32bWMfe%2B4f8QKCSNAxSaRhaR0aGwtf%2F4xCDp14nNe8nW1xAS0sYgt1ddiOAWAK3a3mWpSqaL1wMI2svc4GOqUB53Dhtru16cjIlfAaWcgwSTqtKgTxsn7vLjL4liFpmLEcPaTDS3OtwS9XnQoMImPZkNmpJNd2b4KwnCTPO5SX5igI7JpRX5md2ZFGZcyg%2BNWdPs0XYor0SaUI8NcriaCCok0aER1VR85nHQ9ERLEAI6P70IQKevhwaCpfkMHtRJgcZfKSAL27TQtVCLw7xvkYPLKgbaOIxybjA3jB8yh2rMrPI7RA&X-Amz-Signature=cadb2448dc1d39dbbc5ecde9e4944c08c14b77500e0c6b5f3aa4fbc791aaa056&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC42AEG3%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBmeLA7hSx7TR30a59epz3CdXxMhrs6h9qNIaXOWiHPYAiEAjbQrtltab1lGF%2FY8K1%2FAx3TCGKO5R7Z%2B6gqO0Sn%2Bcqkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDEjr6Pr9FaQV2ydLISrcA0yZv1eETN7Xz1UJ6K0CoIF8o%2FqYJIe4XKM8Mel7FDl6GzyXz1brhGTSuJaD1ir%2F0oZMJ8UKwZotzTDgV7%2F7MkCaF1jE0BpL4iXJTm7Cbxz2iAKfbfQSB14%2F0IqhuSfGx5a%2BCYtLcgwjqL%2BuN3sz%2FU3UcNQhKsO8oCSNqVJo2CZJHW%2FW1JDftmYF5kaalVLWZQYQ3uhglqDHTxbHf0o68vARFsZPscq84VLaeFAaVB1bm2jYlBCqe%2F9PBaULwVjVXrN1SE6gp%2BWZH6SK91EW5FUUVcrj1JamYT8UG7dKWU%2FXDJS97p1IS7mQBZKJRaPowElbutWpFNrNBo8Mp9BtystrSkEjPdU5JfC5eAdkc1rUqTy0ttw480Z8Kpg2urn5YKavHfoVh2uPeqmqpsDV37aKanymCqAjYhylsCP2w4d5Lbyh%2BrWUk9EHhQYoIb1fmZf2NHSpvMBw8vAvyLZE0iz%2BxWvdhhdzZf1CBJpDAtAmX65KT7ElQ14JyQDzImwU8hhofB3I07dwU4z5i7Tk%2FU%2BZ9BDyzIP%2B6o2WkhPAP%2B4wBCKuHW32bWMfe%2B4f8QKCSNAxSaRhaR0aGwtf%2F4xCDp14nNe8nW1xAS0sYgt1ddiOAWAK3a3mWpSqaL1wMI2svc4GOqUB53Dhtru16cjIlfAaWcgwSTqtKgTxsn7vLjL4liFpmLEcPaTDS3OtwS9XnQoMImPZkNmpJNd2b4KwnCTPO5SX5igI7JpRX5md2ZFGZcyg%2BNWdPs0XYor0SaUI8NcriaCCok0aER1VR85nHQ9ERLEAI6P70IQKevhwaCpfkMHtRJgcZfKSAL27TQtVCLw7xvkYPLKgbaOIxybjA3jB8yh2rMrPI7RA&X-Amz-Signature=9d5816c76fec9ee259f791081c61c4c433d23f6849e01946e2080bb1c23808da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC42AEG3%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBmeLA7hSx7TR30a59epz3CdXxMhrs6h9qNIaXOWiHPYAiEAjbQrtltab1lGF%2FY8K1%2FAx3TCGKO5R7Z%2B6gqO0Sn%2Bcqkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDEjr6Pr9FaQV2ydLISrcA0yZv1eETN7Xz1UJ6K0CoIF8o%2FqYJIe4XKM8Mel7FDl6GzyXz1brhGTSuJaD1ir%2F0oZMJ8UKwZotzTDgV7%2F7MkCaF1jE0BpL4iXJTm7Cbxz2iAKfbfQSB14%2F0IqhuSfGx5a%2BCYtLcgwjqL%2BuN3sz%2FU3UcNQhKsO8oCSNqVJo2CZJHW%2FW1JDftmYF5kaalVLWZQYQ3uhglqDHTxbHf0o68vARFsZPscq84VLaeFAaVB1bm2jYlBCqe%2F9PBaULwVjVXrN1SE6gp%2BWZH6SK91EW5FUUVcrj1JamYT8UG7dKWU%2FXDJS97p1IS7mQBZKJRaPowElbutWpFNrNBo8Mp9BtystrSkEjPdU5JfC5eAdkc1rUqTy0ttw480Z8Kpg2urn5YKavHfoVh2uPeqmqpsDV37aKanymCqAjYhylsCP2w4d5Lbyh%2BrWUk9EHhQYoIb1fmZf2NHSpvMBw8vAvyLZE0iz%2BxWvdhhdzZf1CBJpDAtAmX65KT7ElQ14JyQDzImwU8hhofB3I07dwU4z5i7Tk%2FU%2BZ9BDyzIP%2B6o2WkhPAP%2B4wBCKuHW32bWMfe%2B4f8QKCSNAxSaRhaR0aGwtf%2F4xCDp14nNe8nW1xAS0sYgt1ddiOAWAK3a3mWpSqaL1wMI2svc4GOqUB53Dhtru16cjIlfAaWcgwSTqtKgTxsn7vLjL4liFpmLEcPaTDS3OtwS9XnQoMImPZkNmpJNd2b4KwnCTPO5SX5igI7JpRX5md2ZFGZcyg%2BNWdPs0XYor0SaUI8NcriaCCok0aER1VR85nHQ9ERLEAI6P70IQKevhwaCpfkMHtRJgcZfKSAL27TQtVCLw7xvkYPLKgbaOIxybjA3jB8yh2rMrPI7RA&X-Amz-Signature=b7dad4e5460f5ecd60286f1405efdbf366ab304abf02a7fe77f1481df79915c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC42AEG3%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBmeLA7hSx7TR30a59epz3CdXxMhrs6h9qNIaXOWiHPYAiEAjbQrtltab1lGF%2FY8K1%2FAx3TCGKO5R7Z%2B6gqO0Sn%2Bcqkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDEjr6Pr9FaQV2ydLISrcA0yZv1eETN7Xz1UJ6K0CoIF8o%2FqYJIe4XKM8Mel7FDl6GzyXz1brhGTSuJaD1ir%2F0oZMJ8UKwZotzTDgV7%2F7MkCaF1jE0BpL4iXJTm7Cbxz2iAKfbfQSB14%2F0IqhuSfGx5a%2BCYtLcgwjqL%2BuN3sz%2FU3UcNQhKsO8oCSNqVJo2CZJHW%2FW1JDftmYF5kaalVLWZQYQ3uhglqDHTxbHf0o68vARFsZPscq84VLaeFAaVB1bm2jYlBCqe%2F9PBaULwVjVXrN1SE6gp%2BWZH6SK91EW5FUUVcrj1JamYT8UG7dKWU%2FXDJS97p1IS7mQBZKJRaPowElbutWpFNrNBo8Mp9BtystrSkEjPdU5JfC5eAdkc1rUqTy0ttw480Z8Kpg2urn5YKavHfoVh2uPeqmqpsDV37aKanymCqAjYhylsCP2w4d5Lbyh%2BrWUk9EHhQYoIb1fmZf2NHSpvMBw8vAvyLZE0iz%2BxWvdhhdzZf1CBJpDAtAmX65KT7ElQ14JyQDzImwU8hhofB3I07dwU4z5i7Tk%2FU%2BZ9BDyzIP%2B6o2WkhPAP%2B4wBCKuHW32bWMfe%2B4f8QKCSNAxSaRhaR0aGwtf%2F4xCDp14nNe8nW1xAS0sYgt1ddiOAWAK3a3mWpSqaL1wMI2svc4GOqUB53Dhtru16cjIlfAaWcgwSTqtKgTxsn7vLjL4liFpmLEcPaTDS3OtwS9XnQoMImPZkNmpJNd2b4KwnCTPO5SX5igI7JpRX5md2ZFGZcyg%2BNWdPs0XYor0SaUI8NcriaCCok0aER1VR85nHQ9ERLEAI6P70IQKevhwaCpfkMHtRJgcZfKSAL27TQtVCLw7xvkYPLKgbaOIxybjA3jB8yh2rMrPI7RA&X-Amz-Signature=8b0cbf2b9af5f85c6fa1ef3c14b4694e0b29cb25c066fc7eff7fb396ca9a8f53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC42AEG3%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBmeLA7hSx7TR30a59epz3CdXxMhrs6h9qNIaXOWiHPYAiEAjbQrtltab1lGF%2FY8K1%2FAx3TCGKO5R7Z%2B6gqO0Sn%2Bcqkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDEjr6Pr9FaQV2ydLISrcA0yZv1eETN7Xz1UJ6K0CoIF8o%2FqYJIe4XKM8Mel7FDl6GzyXz1brhGTSuJaD1ir%2F0oZMJ8UKwZotzTDgV7%2F7MkCaF1jE0BpL4iXJTm7Cbxz2iAKfbfQSB14%2F0IqhuSfGx5a%2BCYtLcgwjqL%2BuN3sz%2FU3UcNQhKsO8oCSNqVJo2CZJHW%2FW1JDftmYF5kaalVLWZQYQ3uhglqDHTxbHf0o68vARFsZPscq84VLaeFAaVB1bm2jYlBCqe%2F9PBaULwVjVXrN1SE6gp%2BWZH6SK91EW5FUUVcrj1JamYT8UG7dKWU%2FXDJS97p1IS7mQBZKJRaPowElbutWpFNrNBo8Mp9BtystrSkEjPdU5JfC5eAdkc1rUqTy0ttw480Z8Kpg2urn5YKavHfoVh2uPeqmqpsDV37aKanymCqAjYhylsCP2w4d5Lbyh%2BrWUk9EHhQYoIb1fmZf2NHSpvMBw8vAvyLZE0iz%2BxWvdhhdzZf1CBJpDAtAmX65KT7ElQ14JyQDzImwU8hhofB3I07dwU4z5i7Tk%2FU%2BZ9BDyzIP%2B6o2WkhPAP%2B4wBCKuHW32bWMfe%2B4f8QKCSNAxSaRhaR0aGwtf%2F4xCDp14nNe8nW1xAS0sYgt1ddiOAWAK3a3mWpSqaL1wMI2svc4GOqUB53Dhtru16cjIlfAaWcgwSTqtKgTxsn7vLjL4liFpmLEcPaTDS3OtwS9XnQoMImPZkNmpJNd2b4KwnCTPO5SX5igI7JpRX5md2ZFGZcyg%2BNWdPs0XYor0SaUI8NcriaCCok0aER1VR85nHQ9ERLEAI6P70IQKevhwaCpfkMHtRJgcZfKSAL27TQtVCLw7xvkYPLKgbaOIxybjA3jB8yh2rMrPI7RA&X-Amz-Signature=5b1aa1fe6031ef3516c2e8a5fb13578e0c351f40e541e50c54e251b11d5ae1e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

