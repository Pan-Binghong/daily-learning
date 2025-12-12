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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7NUAR7B%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIHg45F%2FueFFes0lxrh2eGhkpd31UuTMMh4TBa7Fq7dJzAiEAu%2Bqpivg%2FDszWh1OkYA%2BPgiflrWui602gJewZmMnyDWcqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKODGQR1%2B78zpm8y5yrcA%2F55WOwISEDZj1C3M18aBHvuPiyvFKlwFlDRf6XuKnYFxWzc0jza19wLPrR0l9toZmBxdWTI9gNgviQBgOiK6GA2sR0yTDg4lOZboUWHvRn1as0uZmODq3B9zbMbanlHereFUrvHklu7%2BsdtHWOtHRn4RMGiLaYe1K9tSbdmOscTnYLto80ZTLIZsMWw2y1ZZWC2I7%2FlPqLnO5hso%2BYeQ4dPD2Kb0oxw4QLjpA3NOSY8itR3FRL3Y%2FqItYYuFvO8mVMGiluZWzig%2FruzpsiNCKEmElRe3xIp%2FXg4%2BWJcleeHBeQp%2B10ZZnLAa08I7UhBj4GbmRTLXVT%2F8MvrMjCodvH9MEvlKnkHp3fbXN99zpBeAneKG9BrdlbEsi5jsVQHootvirzvagsIO%2FPjWSWKcJuj314aqsBEVI9%2B12Eijz1LJMHme%2Bm6XYIj7QfPNPDhB9hHlz8AeEeLyY32nCEwcm67Bcx123FPtPa7IadPrFX92kZqbqClJNq85gVRvqcAZH3%2BY8mVz5rgdQzQra1nVIjC1UDjC0ugcUHkBQ2n%2FNAkwO5Rg0hFs0wojNPngvtxeJdCZv0lhuVXG0BVDpXnsE1oZpVCJuewnYJZXDpHfx3N26yDE2y0LTL4QaCsMIHW7ckGOqUBDh8lBdKuPsTaxjirvKE%2FDMbmSD6twvQ8G%2F70jZqe%2B1UUADKykc1zecREc2rsen%2BQKKOTgIS8yTyDmRAEa7iLv9G6UOacj5Wzm2ezrV1xEcKDCGeJBC3RoiZ4GBJzHArgBwMHSkvZYstxgPRo3pAr%2BfkKTLh9LndyWcVZqFuvquBMx1QG2Zk0OmeC5vyzMsni6qFk00lOBX2vwCDNyY1xotNxJTjI&X-Amz-Signature=5b70d47cee9debee128ed5edcc3f704967de0255684125e5bbe889faa6fc96ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7NUAR7B%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIHg45F%2FueFFes0lxrh2eGhkpd31UuTMMh4TBa7Fq7dJzAiEAu%2Bqpivg%2FDszWh1OkYA%2BPgiflrWui602gJewZmMnyDWcqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKODGQR1%2B78zpm8y5yrcA%2F55WOwISEDZj1C3M18aBHvuPiyvFKlwFlDRf6XuKnYFxWzc0jza19wLPrR0l9toZmBxdWTI9gNgviQBgOiK6GA2sR0yTDg4lOZboUWHvRn1as0uZmODq3B9zbMbanlHereFUrvHklu7%2BsdtHWOtHRn4RMGiLaYe1K9tSbdmOscTnYLto80ZTLIZsMWw2y1ZZWC2I7%2FlPqLnO5hso%2BYeQ4dPD2Kb0oxw4QLjpA3NOSY8itR3FRL3Y%2FqItYYuFvO8mVMGiluZWzig%2FruzpsiNCKEmElRe3xIp%2FXg4%2BWJcleeHBeQp%2B10ZZnLAa08I7UhBj4GbmRTLXVT%2F8MvrMjCodvH9MEvlKnkHp3fbXN99zpBeAneKG9BrdlbEsi5jsVQHootvirzvagsIO%2FPjWSWKcJuj314aqsBEVI9%2B12Eijz1LJMHme%2Bm6XYIj7QfPNPDhB9hHlz8AeEeLyY32nCEwcm67Bcx123FPtPa7IadPrFX92kZqbqClJNq85gVRvqcAZH3%2BY8mVz5rgdQzQra1nVIjC1UDjC0ugcUHkBQ2n%2FNAkwO5Rg0hFs0wojNPngvtxeJdCZv0lhuVXG0BVDpXnsE1oZpVCJuewnYJZXDpHfx3N26yDE2y0LTL4QaCsMIHW7ckGOqUBDh8lBdKuPsTaxjirvKE%2FDMbmSD6twvQ8G%2F70jZqe%2B1UUADKykc1zecREc2rsen%2BQKKOTgIS8yTyDmRAEa7iLv9G6UOacj5Wzm2ezrV1xEcKDCGeJBC3RoiZ4GBJzHArgBwMHSkvZYstxgPRo3pAr%2BfkKTLh9LndyWcVZqFuvquBMx1QG2Zk0OmeC5vyzMsni6qFk00lOBX2vwCDNyY1xotNxJTjI&X-Amz-Signature=8dbf3614905fa9a0b6dcb957ba8b348e6d7f2b05d3fc5f9409ea71b2859d01b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7NUAR7B%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIHg45F%2FueFFes0lxrh2eGhkpd31UuTMMh4TBa7Fq7dJzAiEAu%2Bqpivg%2FDszWh1OkYA%2BPgiflrWui602gJewZmMnyDWcqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKODGQR1%2B78zpm8y5yrcA%2F55WOwISEDZj1C3M18aBHvuPiyvFKlwFlDRf6XuKnYFxWzc0jza19wLPrR0l9toZmBxdWTI9gNgviQBgOiK6GA2sR0yTDg4lOZboUWHvRn1as0uZmODq3B9zbMbanlHereFUrvHklu7%2BsdtHWOtHRn4RMGiLaYe1K9tSbdmOscTnYLto80ZTLIZsMWw2y1ZZWC2I7%2FlPqLnO5hso%2BYeQ4dPD2Kb0oxw4QLjpA3NOSY8itR3FRL3Y%2FqItYYuFvO8mVMGiluZWzig%2FruzpsiNCKEmElRe3xIp%2FXg4%2BWJcleeHBeQp%2B10ZZnLAa08I7UhBj4GbmRTLXVT%2F8MvrMjCodvH9MEvlKnkHp3fbXN99zpBeAneKG9BrdlbEsi5jsVQHootvirzvagsIO%2FPjWSWKcJuj314aqsBEVI9%2B12Eijz1LJMHme%2Bm6XYIj7QfPNPDhB9hHlz8AeEeLyY32nCEwcm67Bcx123FPtPa7IadPrFX92kZqbqClJNq85gVRvqcAZH3%2BY8mVz5rgdQzQra1nVIjC1UDjC0ugcUHkBQ2n%2FNAkwO5Rg0hFs0wojNPngvtxeJdCZv0lhuVXG0BVDpXnsE1oZpVCJuewnYJZXDpHfx3N26yDE2y0LTL4QaCsMIHW7ckGOqUBDh8lBdKuPsTaxjirvKE%2FDMbmSD6twvQ8G%2F70jZqe%2B1UUADKykc1zecREc2rsen%2BQKKOTgIS8yTyDmRAEa7iLv9G6UOacj5Wzm2ezrV1xEcKDCGeJBC3RoiZ4GBJzHArgBwMHSkvZYstxgPRo3pAr%2BfkKTLh9LndyWcVZqFuvquBMx1QG2Zk0OmeC5vyzMsni6qFk00lOBX2vwCDNyY1xotNxJTjI&X-Amz-Signature=3fce61156c6a173d85d4a21a36f07287a91f70b9097ebc0105041e1c5c083ffc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7NUAR7B%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIHg45F%2FueFFes0lxrh2eGhkpd31UuTMMh4TBa7Fq7dJzAiEAu%2Bqpivg%2FDszWh1OkYA%2BPgiflrWui602gJewZmMnyDWcqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKODGQR1%2B78zpm8y5yrcA%2F55WOwISEDZj1C3M18aBHvuPiyvFKlwFlDRf6XuKnYFxWzc0jza19wLPrR0l9toZmBxdWTI9gNgviQBgOiK6GA2sR0yTDg4lOZboUWHvRn1as0uZmODq3B9zbMbanlHereFUrvHklu7%2BsdtHWOtHRn4RMGiLaYe1K9tSbdmOscTnYLto80ZTLIZsMWw2y1ZZWC2I7%2FlPqLnO5hso%2BYeQ4dPD2Kb0oxw4QLjpA3NOSY8itR3FRL3Y%2FqItYYuFvO8mVMGiluZWzig%2FruzpsiNCKEmElRe3xIp%2FXg4%2BWJcleeHBeQp%2B10ZZnLAa08I7UhBj4GbmRTLXVT%2F8MvrMjCodvH9MEvlKnkHp3fbXN99zpBeAneKG9BrdlbEsi5jsVQHootvirzvagsIO%2FPjWSWKcJuj314aqsBEVI9%2B12Eijz1LJMHme%2Bm6XYIj7QfPNPDhB9hHlz8AeEeLyY32nCEwcm67Bcx123FPtPa7IadPrFX92kZqbqClJNq85gVRvqcAZH3%2BY8mVz5rgdQzQra1nVIjC1UDjC0ugcUHkBQ2n%2FNAkwO5Rg0hFs0wojNPngvtxeJdCZv0lhuVXG0BVDpXnsE1oZpVCJuewnYJZXDpHfx3N26yDE2y0LTL4QaCsMIHW7ckGOqUBDh8lBdKuPsTaxjirvKE%2FDMbmSD6twvQ8G%2F70jZqe%2B1UUADKykc1zecREc2rsen%2BQKKOTgIS8yTyDmRAEa7iLv9G6UOacj5Wzm2ezrV1xEcKDCGeJBC3RoiZ4GBJzHArgBwMHSkvZYstxgPRo3pAr%2BfkKTLh9LndyWcVZqFuvquBMx1QG2Zk0OmeC5vyzMsni6qFk00lOBX2vwCDNyY1xotNxJTjI&X-Amz-Signature=d021da8c8f20a8b5b75c14d2a7b35e86bff44615bef41159d6c17625e150c9c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7NUAR7B%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIHg45F%2FueFFes0lxrh2eGhkpd31UuTMMh4TBa7Fq7dJzAiEAu%2Bqpivg%2FDszWh1OkYA%2BPgiflrWui602gJewZmMnyDWcqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKODGQR1%2B78zpm8y5yrcA%2F55WOwISEDZj1C3M18aBHvuPiyvFKlwFlDRf6XuKnYFxWzc0jza19wLPrR0l9toZmBxdWTI9gNgviQBgOiK6GA2sR0yTDg4lOZboUWHvRn1as0uZmODq3B9zbMbanlHereFUrvHklu7%2BsdtHWOtHRn4RMGiLaYe1K9tSbdmOscTnYLto80ZTLIZsMWw2y1ZZWC2I7%2FlPqLnO5hso%2BYeQ4dPD2Kb0oxw4QLjpA3NOSY8itR3FRL3Y%2FqItYYuFvO8mVMGiluZWzig%2FruzpsiNCKEmElRe3xIp%2FXg4%2BWJcleeHBeQp%2B10ZZnLAa08I7UhBj4GbmRTLXVT%2F8MvrMjCodvH9MEvlKnkHp3fbXN99zpBeAneKG9BrdlbEsi5jsVQHootvirzvagsIO%2FPjWSWKcJuj314aqsBEVI9%2B12Eijz1LJMHme%2Bm6XYIj7QfPNPDhB9hHlz8AeEeLyY32nCEwcm67Bcx123FPtPa7IadPrFX92kZqbqClJNq85gVRvqcAZH3%2BY8mVz5rgdQzQra1nVIjC1UDjC0ugcUHkBQ2n%2FNAkwO5Rg0hFs0wojNPngvtxeJdCZv0lhuVXG0BVDpXnsE1oZpVCJuewnYJZXDpHfx3N26yDE2y0LTL4QaCsMIHW7ckGOqUBDh8lBdKuPsTaxjirvKE%2FDMbmSD6twvQ8G%2F70jZqe%2B1UUADKykc1zecREc2rsen%2BQKKOTgIS8yTyDmRAEa7iLv9G6UOacj5Wzm2ezrV1xEcKDCGeJBC3RoiZ4GBJzHArgBwMHSkvZYstxgPRo3pAr%2BfkKTLh9LndyWcVZqFuvquBMx1QG2Zk0OmeC5vyzMsni6qFk00lOBX2vwCDNyY1xotNxJTjI&X-Amz-Signature=58a40d9c56397735124d3a7fc9c52ca86884855c0f7db524a681161e80075bc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7NUAR7B%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIHg45F%2FueFFes0lxrh2eGhkpd31UuTMMh4TBa7Fq7dJzAiEAu%2Bqpivg%2FDszWh1OkYA%2BPgiflrWui602gJewZmMnyDWcqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKODGQR1%2B78zpm8y5yrcA%2F55WOwISEDZj1C3M18aBHvuPiyvFKlwFlDRf6XuKnYFxWzc0jza19wLPrR0l9toZmBxdWTI9gNgviQBgOiK6GA2sR0yTDg4lOZboUWHvRn1as0uZmODq3B9zbMbanlHereFUrvHklu7%2BsdtHWOtHRn4RMGiLaYe1K9tSbdmOscTnYLto80ZTLIZsMWw2y1ZZWC2I7%2FlPqLnO5hso%2BYeQ4dPD2Kb0oxw4QLjpA3NOSY8itR3FRL3Y%2FqItYYuFvO8mVMGiluZWzig%2FruzpsiNCKEmElRe3xIp%2FXg4%2BWJcleeHBeQp%2B10ZZnLAa08I7UhBj4GbmRTLXVT%2F8MvrMjCodvH9MEvlKnkHp3fbXN99zpBeAneKG9BrdlbEsi5jsVQHootvirzvagsIO%2FPjWSWKcJuj314aqsBEVI9%2B12Eijz1LJMHme%2Bm6XYIj7QfPNPDhB9hHlz8AeEeLyY32nCEwcm67Bcx123FPtPa7IadPrFX92kZqbqClJNq85gVRvqcAZH3%2BY8mVz5rgdQzQra1nVIjC1UDjC0ugcUHkBQ2n%2FNAkwO5Rg0hFs0wojNPngvtxeJdCZv0lhuVXG0BVDpXnsE1oZpVCJuewnYJZXDpHfx3N26yDE2y0LTL4QaCsMIHW7ckGOqUBDh8lBdKuPsTaxjirvKE%2FDMbmSD6twvQ8G%2F70jZqe%2B1UUADKykc1zecREc2rsen%2BQKKOTgIS8yTyDmRAEa7iLv9G6UOacj5Wzm2ezrV1xEcKDCGeJBC3RoiZ4GBJzHArgBwMHSkvZYstxgPRo3pAr%2BfkKTLh9LndyWcVZqFuvquBMx1QG2Zk0OmeC5vyzMsni6qFk00lOBX2vwCDNyY1xotNxJTjI&X-Amz-Signature=c84d9584913fe0947aa73f62aa62791be73810f72969781fb1d98fc8a2db2d32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7NUAR7B%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIHg45F%2FueFFes0lxrh2eGhkpd31UuTMMh4TBa7Fq7dJzAiEAu%2Bqpivg%2FDszWh1OkYA%2BPgiflrWui602gJewZmMnyDWcqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKODGQR1%2B78zpm8y5yrcA%2F55WOwISEDZj1C3M18aBHvuPiyvFKlwFlDRf6XuKnYFxWzc0jza19wLPrR0l9toZmBxdWTI9gNgviQBgOiK6GA2sR0yTDg4lOZboUWHvRn1as0uZmODq3B9zbMbanlHereFUrvHklu7%2BsdtHWOtHRn4RMGiLaYe1K9tSbdmOscTnYLto80ZTLIZsMWw2y1ZZWC2I7%2FlPqLnO5hso%2BYeQ4dPD2Kb0oxw4QLjpA3NOSY8itR3FRL3Y%2FqItYYuFvO8mVMGiluZWzig%2FruzpsiNCKEmElRe3xIp%2FXg4%2BWJcleeHBeQp%2B10ZZnLAa08I7UhBj4GbmRTLXVT%2F8MvrMjCodvH9MEvlKnkHp3fbXN99zpBeAneKG9BrdlbEsi5jsVQHootvirzvagsIO%2FPjWSWKcJuj314aqsBEVI9%2B12Eijz1LJMHme%2Bm6XYIj7QfPNPDhB9hHlz8AeEeLyY32nCEwcm67Bcx123FPtPa7IadPrFX92kZqbqClJNq85gVRvqcAZH3%2BY8mVz5rgdQzQra1nVIjC1UDjC0ugcUHkBQ2n%2FNAkwO5Rg0hFs0wojNPngvtxeJdCZv0lhuVXG0BVDpXnsE1oZpVCJuewnYJZXDpHfx3N26yDE2y0LTL4QaCsMIHW7ckGOqUBDh8lBdKuPsTaxjirvKE%2FDMbmSD6twvQ8G%2F70jZqe%2B1UUADKykc1zecREc2rsen%2BQKKOTgIS8yTyDmRAEa7iLv9G6UOacj5Wzm2ezrV1xEcKDCGeJBC3RoiZ4GBJzHArgBwMHSkvZYstxgPRo3pAr%2BfkKTLh9LndyWcVZqFuvquBMx1QG2Zk0OmeC5vyzMsni6qFk00lOBX2vwCDNyY1xotNxJTjI&X-Amz-Signature=9a147ca3559948c14962659d332d5b42b072af5e136ce5e9cd897ddd52143678&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

