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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IJB4XGH%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGSjsTwPMY6dj7DgfTRz8FrDT3%2B0KMfIeRBW%2BbOSJuIxAiAnZtSIjdT9Gwtir05kYGo%2BDAqqHtkVoxOolTIIrGtVMSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMYQ7KWfHtDvM4pJdOKtwDu1%2Fa%2B2otdCUKKmLzV3hSWxhmjQyXk8TJIguxk%2FHv9EQAqS5Ru%2BmLJpdaDQCv9aFtmUhJoKwOpAKnheSl2qdTd1ceBOqNZ3gWsF%2BH2DS%2BUHz49gwftB0UUrPl6e4TqtYiPFInok%2Fy0JUICarZi7Tf6J8OGYS%2Fu9iEqNwJfYUg3vlWPwy%2BI4dg%2F%2BQBVSw4gYubUQD%2F0sRXh5XEaz30cvOsIUwkgGjrGuFndXop7377IHoGYbKucFlti8qw58zH6SE%2BO2IKSypJ1rrGOaT5JbtMmELkLMYdB8bzKojBPpfe1%2BtpaIzsXmNgJdPS2cMalGpNp3d3jCY%2B8ZGEu2d0VScaBynCZ0gArko5z9T97CBCcqAH5afY7zrNgTG4NgYrT549Weiz%2F1nlqlviKUDujxNE9gmF%2BopgDoJPDVt82p7NLThoZ%2BCibfezkKJQQZe30GxmpT69HcnyhKFCcZlbPQWXcI9Sz6KrCbOwqBx7S880zpkUV8iy77kteHCZsqduZOPanq9r2GzYbpxriNqPUWaLXdNMj7G5%2BrdZgbnKJfSFN54YZ9SJpYjxA%2BHCVhgsxqgi5py1vkT1%2F3cP0hbj711QHdMCzOPH1D0VM1eIJnDtIE%2B1OBAee0ozx1rK6bgw%2FbKZyQY6pgF6MEWNjbf%2BG7uSRij2Sb0lGU52AYP%2FDZddeR1xJwKZ3oTEmJeb4UYBN0%2FcT2kCrimTXAgZQAxPZUTMNJhwnhnTpwRsQB3LbLyAayRHv1tROCszl0Kr24gpm4H9hyVM3O2WepMzpjR0aU65Hf50HshgYoNvBg1gT%2FffKzIJCxhAqlzvkRv39KEE6S7ezDed4w%2BRKomrDdmQArKgWy4CdfB1QzJpZtwp&X-Amz-Signature=fb7c7bf0a855e6f40e11802b32a70742ccd9c5be5ba835b3b76ad93d8ed986c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IJB4XGH%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGSjsTwPMY6dj7DgfTRz8FrDT3%2B0KMfIeRBW%2BbOSJuIxAiAnZtSIjdT9Gwtir05kYGo%2BDAqqHtkVoxOolTIIrGtVMSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMYQ7KWfHtDvM4pJdOKtwDu1%2Fa%2B2otdCUKKmLzV3hSWxhmjQyXk8TJIguxk%2FHv9EQAqS5Ru%2BmLJpdaDQCv9aFtmUhJoKwOpAKnheSl2qdTd1ceBOqNZ3gWsF%2BH2DS%2BUHz49gwftB0UUrPl6e4TqtYiPFInok%2Fy0JUICarZi7Tf6J8OGYS%2Fu9iEqNwJfYUg3vlWPwy%2BI4dg%2F%2BQBVSw4gYubUQD%2F0sRXh5XEaz30cvOsIUwkgGjrGuFndXop7377IHoGYbKucFlti8qw58zH6SE%2BO2IKSypJ1rrGOaT5JbtMmELkLMYdB8bzKojBPpfe1%2BtpaIzsXmNgJdPS2cMalGpNp3d3jCY%2B8ZGEu2d0VScaBynCZ0gArko5z9T97CBCcqAH5afY7zrNgTG4NgYrT549Weiz%2F1nlqlviKUDujxNE9gmF%2BopgDoJPDVt82p7NLThoZ%2BCibfezkKJQQZe30GxmpT69HcnyhKFCcZlbPQWXcI9Sz6KrCbOwqBx7S880zpkUV8iy77kteHCZsqduZOPanq9r2GzYbpxriNqPUWaLXdNMj7G5%2BrdZgbnKJfSFN54YZ9SJpYjxA%2BHCVhgsxqgi5py1vkT1%2F3cP0hbj711QHdMCzOPH1D0VM1eIJnDtIE%2B1OBAee0ozx1rK6bgw%2FbKZyQY6pgF6MEWNjbf%2BG7uSRij2Sb0lGU52AYP%2FDZddeR1xJwKZ3oTEmJeb4UYBN0%2FcT2kCrimTXAgZQAxPZUTMNJhwnhnTpwRsQB3LbLyAayRHv1tROCszl0Kr24gpm4H9hyVM3O2WepMzpjR0aU65Hf50HshgYoNvBg1gT%2FffKzIJCxhAqlzvkRv39KEE6S7ezDed4w%2BRKomrDdmQArKgWy4CdfB1QzJpZtwp&X-Amz-Signature=1bafebb8cb044b97db0d8716941909fa2330b7e7dc9ba15cfba0a37cc768faa1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IJB4XGH%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGSjsTwPMY6dj7DgfTRz8FrDT3%2B0KMfIeRBW%2BbOSJuIxAiAnZtSIjdT9Gwtir05kYGo%2BDAqqHtkVoxOolTIIrGtVMSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMYQ7KWfHtDvM4pJdOKtwDu1%2Fa%2B2otdCUKKmLzV3hSWxhmjQyXk8TJIguxk%2FHv9EQAqS5Ru%2BmLJpdaDQCv9aFtmUhJoKwOpAKnheSl2qdTd1ceBOqNZ3gWsF%2BH2DS%2BUHz49gwftB0UUrPl6e4TqtYiPFInok%2Fy0JUICarZi7Tf6J8OGYS%2Fu9iEqNwJfYUg3vlWPwy%2BI4dg%2F%2BQBVSw4gYubUQD%2F0sRXh5XEaz30cvOsIUwkgGjrGuFndXop7377IHoGYbKucFlti8qw58zH6SE%2BO2IKSypJ1rrGOaT5JbtMmELkLMYdB8bzKojBPpfe1%2BtpaIzsXmNgJdPS2cMalGpNp3d3jCY%2B8ZGEu2d0VScaBynCZ0gArko5z9T97CBCcqAH5afY7zrNgTG4NgYrT549Weiz%2F1nlqlviKUDujxNE9gmF%2BopgDoJPDVt82p7NLThoZ%2BCibfezkKJQQZe30GxmpT69HcnyhKFCcZlbPQWXcI9Sz6KrCbOwqBx7S880zpkUV8iy77kteHCZsqduZOPanq9r2GzYbpxriNqPUWaLXdNMj7G5%2BrdZgbnKJfSFN54YZ9SJpYjxA%2BHCVhgsxqgi5py1vkT1%2F3cP0hbj711QHdMCzOPH1D0VM1eIJnDtIE%2B1OBAee0ozx1rK6bgw%2FbKZyQY6pgF6MEWNjbf%2BG7uSRij2Sb0lGU52AYP%2FDZddeR1xJwKZ3oTEmJeb4UYBN0%2FcT2kCrimTXAgZQAxPZUTMNJhwnhnTpwRsQB3LbLyAayRHv1tROCszl0Kr24gpm4H9hyVM3O2WepMzpjR0aU65Hf50HshgYoNvBg1gT%2FffKzIJCxhAqlzvkRv39KEE6S7ezDed4w%2BRKomrDdmQArKgWy4CdfB1QzJpZtwp&X-Amz-Signature=000e3823b707c79df9c718bb61ad6e13f19786320c30d1d8fe9079ef4a297cf7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IJB4XGH%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGSjsTwPMY6dj7DgfTRz8FrDT3%2B0KMfIeRBW%2BbOSJuIxAiAnZtSIjdT9Gwtir05kYGo%2BDAqqHtkVoxOolTIIrGtVMSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMYQ7KWfHtDvM4pJdOKtwDu1%2Fa%2B2otdCUKKmLzV3hSWxhmjQyXk8TJIguxk%2FHv9EQAqS5Ru%2BmLJpdaDQCv9aFtmUhJoKwOpAKnheSl2qdTd1ceBOqNZ3gWsF%2BH2DS%2BUHz49gwftB0UUrPl6e4TqtYiPFInok%2Fy0JUICarZi7Tf6J8OGYS%2Fu9iEqNwJfYUg3vlWPwy%2BI4dg%2F%2BQBVSw4gYubUQD%2F0sRXh5XEaz30cvOsIUwkgGjrGuFndXop7377IHoGYbKucFlti8qw58zH6SE%2BO2IKSypJ1rrGOaT5JbtMmELkLMYdB8bzKojBPpfe1%2BtpaIzsXmNgJdPS2cMalGpNp3d3jCY%2B8ZGEu2d0VScaBynCZ0gArko5z9T97CBCcqAH5afY7zrNgTG4NgYrT549Weiz%2F1nlqlviKUDujxNE9gmF%2BopgDoJPDVt82p7NLThoZ%2BCibfezkKJQQZe30GxmpT69HcnyhKFCcZlbPQWXcI9Sz6KrCbOwqBx7S880zpkUV8iy77kteHCZsqduZOPanq9r2GzYbpxriNqPUWaLXdNMj7G5%2BrdZgbnKJfSFN54YZ9SJpYjxA%2BHCVhgsxqgi5py1vkT1%2F3cP0hbj711QHdMCzOPH1D0VM1eIJnDtIE%2B1OBAee0ozx1rK6bgw%2FbKZyQY6pgF6MEWNjbf%2BG7uSRij2Sb0lGU52AYP%2FDZddeR1xJwKZ3oTEmJeb4UYBN0%2FcT2kCrimTXAgZQAxPZUTMNJhwnhnTpwRsQB3LbLyAayRHv1tROCszl0Kr24gpm4H9hyVM3O2WepMzpjR0aU65Hf50HshgYoNvBg1gT%2FffKzIJCxhAqlzvkRv39KEE6S7ezDed4w%2BRKomrDdmQArKgWy4CdfB1QzJpZtwp&X-Amz-Signature=a282a2a561af1f18c787d1737cef41048b23b6a95ba50f8cbe39f37a61a11d40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IJB4XGH%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGSjsTwPMY6dj7DgfTRz8FrDT3%2B0KMfIeRBW%2BbOSJuIxAiAnZtSIjdT9Gwtir05kYGo%2BDAqqHtkVoxOolTIIrGtVMSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMYQ7KWfHtDvM4pJdOKtwDu1%2Fa%2B2otdCUKKmLzV3hSWxhmjQyXk8TJIguxk%2FHv9EQAqS5Ru%2BmLJpdaDQCv9aFtmUhJoKwOpAKnheSl2qdTd1ceBOqNZ3gWsF%2BH2DS%2BUHz49gwftB0UUrPl6e4TqtYiPFInok%2Fy0JUICarZi7Tf6J8OGYS%2Fu9iEqNwJfYUg3vlWPwy%2BI4dg%2F%2BQBVSw4gYubUQD%2F0sRXh5XEaz30cvOsIUwkgGjrGuFndXop7377IHoGYbKucFlti8qw58zH6SE%2BO2IKSypJ1rrGOaT5JbtMmELkLMYdB8bzKojBPpfe1%2BtpaIzsXmNgJdPS2cMalGpNp3d3jCY%2B8ZGEu2d0VScaBynCZ0gArko5z9T97CBCcqAH5afY7zrNgTG4NgYrT549Weiz%2F1nlqlviKUDujxNE9gmF%2BopgDoJPDVt82p7NLThoZ%2BCibfezkKJQQZe30GxmpT69HcnyhKFCcZlbPQWXcI9Sz6KrCbOwqBx7S880zpkUV8iy77kteHCZsqduZOPanq9r2GzYbpxriNqPUWaLXdNMj7G5%2BrdZgbnKJfSFN54YZ9SJpYjxA%2BHCVhgsxqgi5py1vkT1%2F3cP0hbj711QHdMCzOPH1D0VM1eIJnDtIE%2B1OBAee0ozx1rK6bgw%2FbKZyQY6pgF6MEWNjbf%2BG7uSRij2Sb0lGU52AYP%2FDZddeR1xJwKZ3oTEmJeb4UYBN0%2FcT2kCrimTXAgZQAxPZUTMNJhwnhnTpwRsQB3LbLyAayRHv1tROCszl0Kr24gpm4H9hyVM3O2WepMzpjR0aU65Hf50HshgYoNvBg1gT%2FffKzIJCxhAqlzvkRv39KEE6S7ezDed4w%2BRKomrDdmQArKgWy4CdfB1QzJpZtwp&X-Amz-Signature=c708ede7ebeb302b559bdeb1ea15885789fdac0a765218344b70d184d1ef9c0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IJB4XGH%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGSjsTwPMY6dj7DgfTRz8FrDT3%2B0KMfIeRBW%2BbOSJuIxAiAnZtSIjdT9Gwtir05kYGo%2BDAqqHtkVoxOolTIIrGtVMSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMYQ7KWfHtDvM4pJdOKtwDu1%2Fa%2B2otdCUKKmLzV3hSWxhmjQyXk8TJIguxk%2FHv9EQAqS5Ru%2BmLJpdaDQCv9aFtmUhJoKwOpAKnheSl2qdTd1ceBOqNZ3gWsF%2BH2DS%2BUHz49gwftB0UUrPl6e4TqtYiPFInok%2Fy0JUICarZi7Tf6J8OGYS%2Fu9iEqNwJfYUg3vlWPwy%2BI4dg%2F%2BQBVSw4gYubUQD%2F0sRXh5XEaz30cvOsIUwkgGjrGuFndXop7377IHoGYbKucFlti8qw58zH6SE%2BO2IKSypJ1rrGOaT5JbtMmELkLMYdB8bzKojBPpfe1%2BtpaIzsXmNgJdPS2cMalGpNp3d3jCY%2B8ZGEu2d0VScaBynCZ0gArko5z9T97CBCcqAH5afY7zrNgTG4NgYrT549Weiz%2F1nlqlviKUDujxNE9gmF%2BopgDoJPDVt82p7NLThoZ%2BCibfezkKJQQZe30GxmpT69HcnyhKFCcZlbPQWXcI9Sz6KrCbOwqBx7S880zpkUV8iy77kteHCZsqduZOPanq9r2GzYbpxriNqPUWaLXdNMj7G5%2BrdZgbnKJfSFN54YZ9SJpYjxA%2BHCVhgsxqgi5py1vkT1%2F3cP0hbj711QHdMCzOPH1D0VM1eIJnDtIE%2B1OBAee0ozx1rK6bgw%2FbKZyQY6pgF6MEWNjbf%2BG7uSRij2Sb0lGU52AYP%2FDZddeR1xJwKZ3oTEmJeb4UYBN0%2FcT2kCrimTXAgZQAxPZUTMNJhwnhnTpwRsQB3LbLyAayRHv1tROCszl0Kr24gpm4H9hyVM3O2WepMzpjR0aU65Hf50HshgYoNvBg1gT%2FffKzIJCxhAqlzvkRv39KEE6S7ezDed4w%2BRKomrDdmQArKgWy4CdfB1QzJpZtwp&X-Amz-Signature=131daa60784a23a1a54fc4a4795aae31af96eb989706aa054ee26e4d56694396&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IJB4XGH%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGSjsTwPMY6dj7DgfTRz8FrDT3%2B0KMfIeRBW%2BbOSJuIxAiAnZtSIjdT9Gwtir05kYGo%2BDAqqHtkVoxOolTIIrGtVMSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMYQ7KWfHtDvM4pJdOKtwDu1%2Fa%2B2otdCUKKmLzV3hSWxhmjQyXk8TJIguxk%2FHv9EQAqS5Ru%2BmLJpdaDQCv9aFtmUhJoKwOpAKnheSl2qdTd1ceBOqNZ3gWsF%2BH2DS%2BUHz49gwftB0UUrPl6e4TqtYiPFInok%2Fy0JUICarZi7Tf6J8OGYS%2Fu9iEqNwJfYUg3vlWPwy%2BI4dg%2F%2BQBVSw4gYubUQD%2F0sRXh5XEaz30cvOsIUwkgGjrGuFndXop7377IHoGYbKucFlti8qw58zH6SE%2BO2IKSypJ1rrGOaT5JbtMmELkLMYdB8bzKojBPpfe1%2BtpaIzsXmNgJdPS2cMalGpNp3d3jCY%2B8ZGEu2d0VScaBynCZ0gArko5z9T97CBCcqAH5afY7zrNgTG4NgYrT549Weiz%2F1nlqlviKUDujxNE9gmF%2BopgDoJPDVt82p7NLThoZ%2BCibfezkKJQQZe30GxmpT69HcnyhKFCcZlbPQWXcI9Sz6KrCbOwqBx7S880zpkUV8iy77kteHCZsqduZOPanq9r2GzYbpxriNqPUWaLXdNMj7G5%2BrdZgbnKJfSFN54YZ9SJpYjxA%2BHCVhgsxqgi5py1vkT1%2F3cP0hbj711QHdMCzOPH1D0VM1eIJnDtIE%2B1OBAee0ozx1rK6bgw%2FbKZyQY6pgF6MEWNjbf%2BG7uSRij2Sb0lGU52AYP%2FDZddeR1xJwKZ3oTEmJeb4UYBN0%2FcT2kCrimTXAgZQAxPZUTMNJhwnhnTpwRsQB3LbLyAayRHv1tROCszl0Kr24gpm4H9hyVM3O2WepMzpjR0aU65Hf50HshgYoNvBg1gT%2FffKzIJCxhAqlzvkRv39KEE6S7ezDed4w%2BRKomrDdmQArKgWy4CdfB1QzJpZtwp&X-Amz-Signature=b318cfbe33f242688285236c65896fe36678fa108b6303818856a14ba33a4805&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

