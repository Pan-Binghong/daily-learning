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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NQYD3LP%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIFqLxCMKdT501NSp3nbzpdI1cl6Wlij58mghI1r8ZH3rAiEAkNR%2FxpeZLFdzG502KiDjWJNKJpB1omtJFWOzE2OdRSsq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDPA%2B6W0Uv6RNI%2FbQuircA23lYmurRjPODrd%2FCODPazDzZOSuIUoB5ngdSVsd7mRpcl%2FNekhWklcOHga1xy2Uk3T10SfNC7COWYwxlSLFy2TG1AHAs%2B7N%2BiXrTo58xZd%2FECZCW6JJZv2ecfJwPgNuQmwZ5gntaCH3M%2BXjf1KwmydXqHSE8utI3ka3Lp8o7m7jlMr54nnYWaltUEqrBC1No%2FWz%2BOifQRpw3LzM%2FhqFQOv38QbWtVuf6Yla%2Bu4pqPeyqLUCps9frqxnn4A6uLCqJBB9ittKM6I6k4XsJSXAL4K77qNzhoo2OdQqU%2B%2FUjag7xdkwxuuExjWBLf%2BsWs%2BIEoCD9uKmejCb9feF4nU1KqXY5R7h4R%2F8y2w8nr2IPph1SJC%2FCBgMS%2BNZntmG2JxHmK1AA8Qgcn%2BjSQVTLnOBL0qrqWMpJUEPMRWIkfUA8GJRtfUQ98sjA4EtB0fFnVEq5SxtIlT0n2Dpg8LoHcyyCqZdFhXupGSSFsxdq%2FV7bMN%2BHU5TgdLjkNBVpL4LYV1V44KdJrrtQZ5NsULOALaG3AHmR4RbAc4jGaLTxKg5BZRnChHk5QtXSjzaOvoy%2Bc54Yv2gPL6bI4YYGSWepBJ%2B4s0e%2F52cPO8EvKZ9bhSmAzLDMhmqFPwLh0yG%2Fi%2BoMIX%2BuM0GOqUBkigscPpsBl4QHHQeof5M8SLKGherTBL2c9%2BtZfWnryfDfGQEaLiWoDkXVUzJbRwoOpppmQkrxV5JyZUzD43kXSK4HoyzrtVZKHVYaX61gonzP2JjrGKdh8rIbYH5HwjH0gCbN5wAI0k9HQZpTKqU9pSFwF%2BHWdhEAtE9spb1Kfyzvd5IfGgidAwu6jayDaLd7WT9pFCANgqrIslLt8akb%2FecqvHY&X-Amz-Signature=fa6619a99eb5b6b9a002bfdd9faef688a76290242646ee38d86036c7752bb8ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NQYD3LP%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIFqLxCMKdT501NSp3nbzpdI1cl6Wlij58mghI1r8ZH3rAiEAkNR%2FxpeZLFdzG502KiDjWJNKJpB1omtJFWOzE2OdRSsq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDPA%2B6W0Uv6RNI%2FbQuircA23lYmurRjPODrd%2FCODPazDzZOSuIUoB5ngdSVsd7mRpcl%2FNekhWklcOHga1xy2Uk3T10SfNC7COWYwxlSLFy2TG1AHAs%2B7N%2BiXrTo58xZd%2FECZCW6JJZv2ecfJwPgNuQmwZ5gntaCH3M%2BXjf1KwmydXqHSE8utI3ka3Lp8o7m7jlMr54nnYWaltUEqrBC1No%2FWz%2BOifQRpw3LzM%2FhqFQOv38QbWtVuf6Yla%2Bu4pqPeyqLUCps9frqxnn4A6uLCqJBB9ittKM6I6k4XsJSXAL4K77qNzhoo2OdQqU%2B%2FUjag7xdkwxuuExjWBLf%2BsWs%2BIEoCD9uKmejCb9feF4nU1KqXY5R7h4R%2F8y2w8nr2IPph1SJC%2FCBgMS%2BNZntmG2JxHmK1AA8Qgcn%2BjSQVTLnOBL0qrqWMpJUEPMRWIkfUA8GJRtfUQ98sjA4EtB0fFnVEq5SxtIlT0n2Dpg8LoHcyyCqZdFhXupGSSFsxdq%2FV7bMN%2BHU5TgdLjkNBVpL4LYV1V44KdJrrtQZ5NsULOALaG3AHmR4RbAc4jGaLTxKg5BZRnChHk5QtXSjzaOvoy%2Bc54Yv2gPL6bI4YYGSWepBJ%2B4s0e%2F52cPO8EvKZ9bhSmAzLDMhmqFPwLh0yG%2Fi%2BoMIX%2BuM0GOqUBkigscPpsBl4QHHQeof5M8SLKGherTBL2c9%2BtZfWnryfDfGQEaLiWoDkXVUzJbRwoOpppmQkrxV5JyZUzD43kXSK4HoyzrtVZKHVYaX61gonzP2JjrGKdh8rIbYH5HwjH0gCbN5wAI0k9HQZpTKqU9pSFwF%2BHWdhEAtE9spb1Kfyzvd5IfGgidAwu6jayDaLd7WT9pFCANgqrIslLt8akb%2FecqvHY&X-Amz-Signature=aa5c45df9ee5a17f5fa01541ab080722b1de9d538e9cfcc2320e3779dd582718&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NQYD3LP%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIFqLxCMKdT501NSp3nbzpdI1cl6Wlij58mghI1r8ZH3rAiEAkNR%2FxpeZLFdzG502KiDjWJNKJpB1omtJFWOzE2OdRSsq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDPA%2B6W0Uv6RNI%2FbQuircA23lYmurRjPODrd%2FCODPazDzZOSuIUoB5ngdSVsd7mRpcl%2FNekhWklcOHga1xy2Uk3T10SfNC7COWYwxlSLFy2TG1AHAs%2B7N%2BiXrTo58xZd%2FECZCW6JJZv2ecfJwPgNuQmwZ5gntaCH3M%2BXjf1KwmydXqHSE8utI3ka3Lp8o7m7jlMr54nnYWaltUEqrBC1No%2FWz%2BOifQRpw3LzM%2FhqFQOv38QbWtVuf6Yla%2Bu4pqPeyqLUCps9frqxnn4A6uLCqJBB9ittKM6I6k4XsJSXAL4K77qNzhoo2OdQqU%2B%2FUjag7xdkwxuuExjWBLf%2BsWs%2BIEoCD9uKmejCb9feF4nU1KqXY5R7h4R%2F8y2w8nr2IPph1SJC%2FCBgMS%2BNZntmG2JxHmK1AA8Qgcn%2BjSQVTLnOBL0qrqWMpJUEPMRWIkfUA8GJRtfUQ98sjA4EtB0fFnVEq5SxtIlT0n2Dpg8LoHcyyCqZdFhXupGSSFsxdq%2FV7bMN%2BHU5TgdLjkNBVpL4LYV1V44KdJrrtQZ5NsULOALaG3AHmR4RbAc4jGaLTxKg5BZRnChHk5QtXSjzaOvoy%2Bc54Yv2gPL6bI4YYGSWepBJ%2B4s0e%2F52cPO8EvKZ9bhSmAzLDMhmqFPwLh0yG%2Fi%2BoMIX%2BuM0GOqUBkigscPpsBl4QHHQeof5M8SLKGherTBL2c9%2BtZfWnryfDfGQEaLiWoDkXVUzJbRwoOpppmQkrxV5JyZUzD43kXSK4HoyzrtVZKHVYaX61gonzP2JjrGKdh8rIbYH5HwjH0gCbN5wAI0k9HQZpTKqU9pSFwF%2BHWdhEAtE9spb1Kfyzvd5IfGgidAwu6jayDaLd7WT9pFCANgqrIslLt8akb%2FecqvHY&X-Amz-Signature=2c85cfad65269201b4296d953df36702b7914bad7f01834d593521e6cc7547b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NQYD3LP%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIFqLxCMKdT501NSp3nbzpdI1cl6Wlij58mghI1r8ZH3rAiEAkNR%2FxpeZLFdzG502KiDjWJNKJpB1omtJFWOzE2OdRSsq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDPA%2B6W0Uv6RNI%2FbQuircA23lYmurRjPODrd%2FCODPazDzZOSuIUoB5ngdSVsd7mRpcl%2FNekhWklcOHga1xy2Uk3T10SfNC7COWYwxlSLFy2TG1AHAs%2B7N%2BiXrTo58xZd%2FECZCW6JJZv2ecfJwPgNuQmwZ5gntaCH3M%2BXjf1KwmydXqHSE8utI3ka3Lp8o7m7jlMr54nnYWaltUEqrBC1No%2FWz%2BOifQRpw3LzM%2FhqFQOv38QbWtVuf6Yla%2Bu4pqPeyqLUCps9frqxnn4A6uLCqJBB9ittKM6I6k4XsJSXAL4K77qNzhoo2OdQqU%2B%2FUjag7xdkwxuuExjWBLf%2BsWs%2BIEoCD9uKmejCb9feF4nU1KqXY5R7h4R%2F8y2w8nr2IPph1SJC%2FCBgMS%2BNZntmG2JxHmK1AA8Qgcn%2BjSQVTLnOBL0qrqWMpJUEPMRWIkfUA8GJRtfUQ98sjA4EtB0fFnVEq5SxtIlT0n2Dpg8LoHcyyCqZdFhXupGSSFsxdq%2FV7bMN%2BHU5TgdLjkNBVpL4LYV1V44KdJrrtQZ5NsULOALaG3AHmR4RbAc4jGaLTxKg5BZRnChHk5QtXSjzaOvoy%2Bc54Yv2gPL6bI4YYGSWepBJ%2B4s0e%2F52cPO8EvKZ9bhSmAzLDMhmqFPwLh0yG%2Fi%2BoMIX%2BuM0GOqUBkigscPpsBl4QHHQeof5M8SLKGherTBL2c9%2BtZfWnryfDfGQEaLiWoDkXVUzJbRwoOpppmQkrxV5JyZUzD43kXSK4HoyzrtVZKHVYaX61gonzP2JjrGKdh8rIbYH5HwjH0gCbN5wAI0k9HQZpTKqU9pSFwF%2BHWdhEAtE9spb1Kfyzvd5IfGgidAwu6jayDaLd7WT9pFCANgqrIslLt8akb%2FecqvHY&X-Amz-Signature=534e7c86eab65ff2ddcdeeaac57446447bfc57c92a7fd68b36ee427dc0deb3df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NQYD3LP%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIFqLxCMKdT501NSp3nbzpdI1cl6Wlij58mghI1r8ZH3rAiEAkNR%2FxpeZLFdzG502KiDjWJNKJpB1omtJFWOzE2OdRSsq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDPA%2B6W0Uv6RNI%2FbQuircA23lYmurRjPODrd%2FCODPazDzZOSuIUoB5ngdSVsd7mRpcl%2FNekhWklcOHga1xy2Uk3T10SfNC7COWYwxlSLFy2TG1AHAs%2B7N%2BiXrTo58xZd%2FECZCW6JJZv2ecfJwPgNuQmwZ5gntaCH3M%2BXjf1KwmydXqHSE8utI3ka3Lp8o7m7jlMr54nnYWaltUEqrBC1No%2FWz%2BOifQRpw3LzM%2FhqFQOv38QbWtVuf6Yla%2Bu4pqPeyqLUCps9frqxnn4A6uLCqJBB9ittKM6I6k4XsJSXAL4K77qNzhoo2OdQqU%2B%2FUjag7xdkwxuuExjWBLf%2BsWs%2BIEoCD9uKmejCb9feF4nU1KqXY5R7h4R%2F8y2w8nr2IPph1SJC%2FCBgMS%2BNZntmG2JxHmK1AA8Qgcn%2BjSQVTLnOBL0qrqWMpJUEPMRWIkfUA8GJRtfUQ98sjA4EtB0fFnVEq5SxtIlT0n2Dpg8LoHcyyCqZdFhXupGSSFsxdq%2FV7bMN%2BHU5TgdLjkNBVpL4LYV1V44KdJrrtQZ5NsULOALaG3AHmR4RbAc4jGaLTxKg5BZRnChHk5QtXSjzaOvoy%2Bc54Yv2gPL6bI4YYGSWepBJ%2B4s0e%2F52cPO8EvKZ9bhSmAzLDMhmqFPwLh0yG%2Fi%2BoMIX%2BuM0GOqUBkigscPpsBl4QHHQeof5M8SLKGherTBL2c9%2BtZfWnryfDfGQEaLiWoDkXVUzJbRwoOpppmQkrxV5JyZUzD43kXSK4HoyzrtVZKHVYaX61gonzP2JjrGKdh8rIbYH5HwjH0gCbN5wAI0k9HQZpTKqU9pSFwF%2BHWdhEAtE9spb1Kfyzvd5IfGgidAwu6jayDaLd7WT9pFCANgqrIslLt8akb%2FecqvHY&X-Amz-Signature=d22965d45eacc48ea2a49449c65951c35baa6ca11bfa217e95ec1dfbfde38be8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NQYD3LP%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIFqLxCMKdT501NSp3nbzpdI1cl6Wlij58mghI1r8ZH3rAiEAkNR%2FxpeZLFdzG502KiDjWJNKJpB1omtJFWOzE2OdRSsq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDPA%2B6W0Uv6RNI%2FbQuircA23lYmurRjPODrd%2FCODPazDzZOSuIUoB5ngdSVsd7mRpcl%2FNekhWklcOHga1xy2Uk3T10SfNC7COWYwxlSLFy2TG1AHAs%2B7N%2BiXrTo58xZd%2FECZCW6JJZv2ecfJwPgNuQmwZ5gntaCH3M%2BXjf1KwmydXqHSE8utI3ka3Lp8o7m7jlMr54nnYWaltUEqrBC1No%2FWz%2BOifQRpw3LzM%2FhqFQOv38QbWtVuf6Yla%2Bu4pqPeyqLUCps9frqxnn4A6uLCqJBB9ittKM6I6k4XsJSXAL4K77qNzhoo2OdQqU%2B%2FUjag7xdkwxuuExjWBLf%2BsWs%2BIEoCD9uKmejCb9feF4nU1KqXY5R7h4R%2F8y2w8nr2IPph1SJC%2FCBgMS%2BNZntmG2JxHmK1AA8Qgcn%2BjSQVTLnOBL0qrqWMpJUEPMRWIkfUA8GJRtfUQ98sjA4EtB0fFnVEq5SxtIlT0n2Dpg8LoHcyyCqZdFhXupGSSFsxdq%2FV7bMN%2BHU5TgdLjkNBVpL4LYV1V44KdJrrtQZ5NsULOALaG3AHmR4RbAc4jGaLTxKg5BZRnChHk5QtXSjzaOvoy%2Bc54Yv2gPL6bI4YYGSWepBJ%2B4s0e%2F52cPO8EvKZ9bhSmAzLDMhmqFPwLh0yG%2Fi%2BoMIX%2BuM0GOqUBkigscPpsBl4QHHQeof5M8SLKGherTBL2c9%2BtZfWnryfDfGQEaLiWoDkXVUzJbRwoOpppmQkrxV5JyZUzD43kXSK4HoyzrtVZKHVYaX61gonzP2JjrGKdh8rIbYH5HwjH0gCbN5wAI0k9HQZpTKqU9pSFwF%2BHWdhEAtE9spb1Kfyzvd5IfGgidAwu6jayDaLd7WT9pFCANgqrIslLt8akb%2FecqvHY&X-Amz-Signature=e3d5d902351dbd1b363644d34c7d085a8c171cd39561ab4c4ee45837268b492d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NQYD3LP%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIFqLxCMKdT501NSp3nbzpdI1cl6Wlij58mghI1r8ZH3rAiEAkNR%2FxpeZLFdzG502KiDjWJNKJpB1omtJFWOzE2OdRSsq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDPA%2B6W0Uv6RNI%2FbQuircA23lYmurRjPODrd%2FCODPazDzZOSuIUoB5ngdSVsd7mRpcl%2FNekhWklcOHga1xy2Uk3T10SfNC7COWYwxlSLFy2TG1AHAs%2B7N%2BiXrTo58xZd%2FECZCW6JJZv2ecfJwPgNuQmwZ5gntaCH3M%2BXjf1KwmydXqHSE8utI3ka3Lp8o7m7jlMr54nnYWaltUEqrBC1No%2FWz%2BOifQRpw3LzM%2FhqFQOv38QbWtVuf6Yla%2Bu4pqPeyqLUCps9frqxnn4A6uLCqJBB9ittKM6I6k4XsJSXAL4K77qNzhoo2OdQqU%2B%2FUjag7xdkwxuuExjWBLf%2BsWs%2BIEoCD9uKmejCb9feF4nU1KqXY5R7h4R%2F8y2w8nr2IPph1SJC%2FCBgMS%2BNZntmG2JxHmK1AA8Qgcn%2BjSQVTLnOBL0qrqWMpJUEPMRWIkfUA8GJRtfUQ98sjA4EtB0fFnVEq5SxtIlT0n2Dpg8LoHcyyCqZdFhXupGSSFsxdq%2FV7bMN%2BHU5TgdLjkNBVpL4LYV1V44KdJrrtQZ5NsULOALaG3AHmR4RbAc4jGaLTxKg5BZRnChHk5QtXSjzaOvoy%2Bc54Yv2gPL6bI4YYGSWepBJ%2B4s0e%2F52cPO8EvKZ9bhSmAzLDMhmqFPwLh0yG%2Fi%2BoMIX%2BuM0GOqUBkigscPpsBl4QHHQeof5M8SLKGherTBL2c9%2BtZfWnryfDfGQEaLiWoDkXVUzJbRwoOpppmQkrxV5JyZUzD43kXSK4HoyzrtVZKHVYaX61gonzP2JjrGKdh8rIbYH5HwjH0gCbN5wAI0k9HQZpTKqU9pSFwF%2BHWdhEAtE9spb1Kfyzvd5IfGgidAwu6jayDaLd7WT9pFCANgqrIslLt8akb%2FecqvHY&X-Amz-Signature=591bb1872e7a4da8f3a5395bbed31fd94606a937e7cf34ea0254bee196dd11e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

