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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHERIEKQ%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExkRAmgasK7LARVu8f9lZXC0CJtoBbNLaT9f%2B5o5JK8AiBozif1yNnLiY2EnBUzCvzJxBqUAapH6XyY%2FjI3BJqUUCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMixXHh7Ja8PmOnVmMKtwDPI50JukLXJyhBMDL8umV0f692RkkbGTjrUaseZc66pACfg%2FCJ6lI5ZuYg149%2Ff5NCYwoNB4AksriPHLfKoUyN6jBTCDc%2BTjzGtp1WgDL51%2Fb7fTQtb7PrTVbKxZ7%2FFtnf%2BYLtgle9yIQwdScEeHatey%2Bu6JRPOE55SWm0q%2FuXHpSFDt5FvCRNn6yb9UWtx%2BK2ixODZ7Tr7bPsc7NH1ku3Jtv17KK6AG2O%2Fl3QuiXenbLIvvi6LgApthdcaSEX2w4Fgz%2BL3XbtoMzx3q6p397OKenfZUFFJwE2Mq4Tlw2yjoN2cC%2BfTNIpxKmIG12J1XbfZorwyruWfLEJJhn%2BTVpQj1LOixDJoFGuRRm%2FMGs9DLJejFs15x41sh3aNPpK4nAKF9MccEBKuN8lvcDIMyrqAwNRI9r%2Fbcf0ve94M8RWfGUojDQ4RN9%2Fcntq3cFY8kpm5cLS5x7stwXi6ug5dwpsRBZtr85%2FD7%2BcBkhyobF8PeLwuNXY6vHnHDVBcL4RQW%2Bves4NVvuBQ%2BdOGGeonj936OZStsY9FzR75iass3QepEaJGkN9qSpMC%2BuBjwMxcNBuJxGPtjgOyWHpAveWcduPnFKYCKKEYwqYwi12V%2FxFSKdTOosYhHwmUM0tbowlsqNygY6pgEDTYqTUeIZXkGaWPk1i48VH%2FtYDHiE6Tl7EZkARySekHnQlMlW6QHoun94LxO5lkP1Mwn16j3%2FzVKBzHTX2VK0PLgkgl6gJkF%2FT0Go5ellSHAxaWH%2F6q%2B1KNxaTJiBQ6YR7UT52uNBSA5FsLRyHcfb3oJbm8jqPh96uXTC83fUYvDxj9lZLixApAAlkvKvHUooEugw6Qn6orbr6vNhib2wtRukUkYS&X-Amz-Signature=b3ee04d3c2889bf8c657cc956e7175936faa19de071f6fcb273eca46c7fc9954&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHERIEKQ%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExkRAmgasK7LARVu8f9lZXC0CJtoBbNLaT9f%2B5o5JK8AiBozif1yNnLiY2EnBUzCvzJxBqUAapH6XyY%2FjI3BJqUUCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMixXHh7Ja8PmOnVmMKtwDPI50JukLXJyhBMDL8umV0f692RkkbGTjrUaseZc66pACfg%2FCJ6lI5ZuYg149%2Ff5NCYwoNB4AksriPHLfKoUyN6jBTCDc%2BTjzGtp1WgDL51%2Fb7fTQtb7PrTVbKxZ7%2FFtnf%2BYLtgle9yIQwdScEeHatey%2Bu6JRPOE55SWm0q%2FuXHpSFDt5FvCRNn6yb9UWtx%2BK2ixODZ7Tr7bPsc7NH1ku3Jtv17KK6AG2O%2Fl3QuiXenbLIvvi6LgApthdcaSEX2w4Fgz%2BL3XbtoMzx3q6p397OKenfZUFFJwE2Mq4Tlw2yjoN2cC%2BfTNIpxKmIG12J1XbfZorwyruWfLEJJhn%2BTVpQj1LOixDJoFGuRRm%2FMGs9DLJejFs15x41sh3aNPpK4nAKF9MccEBKuN8lvcDIMyrqAwNRI9r%2Fbcf0ve94M8RWfGUojDQ4RN9%2Fcntq3cFY8kpm5cLS5x7stwXi6ug5dwpsRBZtr85%2FD7%2BcBkhyobF8PeLwuNXY6vHnHDVBcL4RQW%2Bves4NVvuBQ%2BdOGGeonj936OZStsY9FzR75iass3QepEaJGkN9qSpMC%2BuBjwMxcNBuJxGPtjgOyWHpAveWcduPnFKYCKKEYwqYwi12V%2FxFSKdTOosYhHwmUM0tbowlsqNygY6pgEDTYqTUeIZXkGaWPk1i48VH%2FtYDHiE6Tl7EZkARySekHnQlMlW6QHoun94LxO5lkP1Mwn16j3%2FzVKBzHTX2VK0PLgkgl6gJkF%2FT0Go5ellSHAxaWH%2F6q%2B1KNxaTJiBQ6YR7UT52uNBSA5FsLRyHcfb3oJbm8jqPh96uXTC83fUYvDxj9lZLixApAAlkvKvHUooEugw6Qn6orbr6vNhib2wtRukUkYS&X-Amz-Signature=54e0c38260dc2762cb22461f487e26e97885109c7561e97a01700b12b8487092&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHERIEKQ%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExkRAmgasK7LARVu8f9lZXC0CJtoBbNLaT9f%2B5o5JK8AiBozif1yNnLiY2EnBUzCvzJxBqUAapH6XyY%2FjI3BJqUUCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMixXHh7Ja8PmOnVmMKtwDPI50JukLXJyhBMDL8umV0f692RkkbGTjrUaseZc66pACfg%2FCJ6lI5ZuYg149%2Ff5NCYwoNB4AksriPHLfKoUyN6jBTCDc%2BTjzGtp1WgDL51%2Fb7fTQtb7PrTVbKxZ7%2FFtnf%2BYLtgle9yIQwdScEeHatey%2Bu6JRPOE55SWm0q%2FuXHpSFDt5FvCRNn6yb9UWtx%2BK2ixODZ7Tr7bPsc7NH1ku3Jtv17KK6AG2O%2Fl3QuiXenbLIvvi6LgApthdcaSEX2w4Fgz%2BL3XbtoMzx3q6p397OKenfZUFFJwE2Mq4Tlw2yjoN2cC%2BfTNIpxKmIG12J1XbfZorwyruWfLEJJhn%2BTVpQj1LOixDJoFGuRRm%2FMGs9DLJejFs15x41sh3aNPpK4nAKF9MccEBKuN8lvcDIMyrqAwNRI9r%2Fbcf0ve94M8RWfGUojDQ4RN9%2Fcntq3cFY8kpm5cLS5x7stwXi6ug5dwpsRBZtr85%2FD7%2BcBkhyobF8PeLwuNXY6vHnHDVBcL4RQW%2Bves4NVvuBQ%2BdOGGeonj936OZStsY9FzR75iass3QepEaJGkN9qSpMC%2BuBjwMxcNBuJxGPtjgOyWHpAveWcduPnFKYCKKEYwqYwi12V%2FxFSKdTOosYhHwmUM0tbowlsqNygY6pgEDTYqTUeIZXkGaWPk1i48VH%2FtYDHiE6Tl7EZkARySekHnQlMlW6QHoun94LxO5lkP1Mwn16j3%2FzVKBzHTX2VK0PLgkgl6gJkF%2FT0Go5ellSHAxaWH%2F6q%2B1KNxaTJiBQ6YR7UT52uNBSA5FsLRyHcfb3oJbm8jqPh96uXTC83fUYvDxj9lZLixApAAlkvKvHUooEugw6Qn6orbr6vNhib2wtRukUkYS&X-Amz-Signature=42c1d6bde4b2adb369bbfe7ffefcaad2e42a2276db48294458132c42fec124a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHERIEKQ%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExkRAmgasK7LARVu8f9lZXC0CJtoBbNLaT9f%2B5o5JK8AiBozif1yNnLiY2EnBUzCvzJxBqUAapH6XyY%2FjI3BJqUUCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMixXHh7Ja8PmOnVmMKtwDPI50JukLXJyhBMDL8umV0f692RkkbGTjrUaseZc66pACfg%2FCJ6lI5ZuYg149%2Ff5NCYwoNB4AksriPHLfKoUyN6jBTCDc%2BTjzGtp1WgDL51%2Fb7fTQtb7PrTVbKxZ7%2FFtnf%2BYLtgle9yIQwdScEeHatey%2Bu6JRPOE55SWm0q%2FuXHpSFDt5FvCRNn6yb9UWtx%2BK2ixODZ7Tr7bPsc7NH1ku3Jtv17KK6AG2O%2Fl3QuiXenbLIvvi6LgApthdcaSEX2w4Fgz%2BL3XbtoMzx3q6p397OKenfZUFFJwE2Mq4Tlw2yjoN2cC%2BfTNIpxKmIG12J1XbfZorwyruWfLEJJhn%2BTVpQj1LOixDJoFGuRRm%2FMGs9DLJejFs15x41sh3aNPpK4nAKF9MccEBKuN8lvcDIMyrqAwNRI9r%2Fbcf0ve94M8RWfGUojDQ4RN9%2Fcntq3cFY8kpm5cLS5x7stwXi6ug5dwpsRBZtr85%2FD7%2BcBkhyobF8PeLwuNXY6vHnHDVBcL4RQW%2Bves4NVvuBQ%2BdOGGeonj936OZStsY9FzR75iass3QepEaJGkN9qSpMC%2BuBjwMxcNBuJxGPtjgOyWHpAveWcduPnFKYCKKEYwqYwi12V%2FxFSKdTOosYhHwmUM0tbowlsqNygY6pgEDTYqTUeIZXkGaWPk1i48VH%2FtYDHiE6Tl7EZkARySekHnQlMlW6QHoun94LxO5lkP1Mwn16j3%2FzVKBzHTX2VK0PLgkgl6gJkF%2FT0Go5ellSHAxaWH%2F6q%2B1KNxaTJiBQ6YR7UT52uNBSA5FsLRyHcfb3oJbm8jqPh96uXTC83fUYvDxj9lZLixApAAlkvKvHUooEugw6Qn6orbr6vNhib2wtRukUkYS&X-Amz-Signature=b5b77184e896fb655ea2e1a5452c56d9ca5db620d1902e9396db0bebc4b8f81f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHERIEKQ%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExkRAmgasK7LARVu8f9lZXC0CJtoBbNLaT9f%2B5o5JK8AiBozif1yNnLiY2EnBUzCvzJxBqUAapH6XyY%2FjI3BJqUUCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMixXHh7Ja8PmOnVmMKtwDPI50JukLXJyhBMDL8umV0f692RkkbGTjrUaseZc66pACfg%2FCJ6lI5ZuYg149%2Ff5NCYwoNB4AksriPHLfKoUyN6jBTCDc%2BTjzGtp1WgDL51%2Fb7fTQtb7PrTVbKxZ7%2FFtnf%2BYLtgle9yIQwdScEeHatey%2Bu6JRPOE55SWm0q%2FuXHpSFDt5FvCRNn6yb9UWtx%2BK2ixODZ7Tr7bPsc7NH1ku3Jtv17KK6AG2O%2Fl3QuiXenbLIvvi6LgApthdcaSEX2w4Fgz%2BL3XbtoMzx3q6p397OKenfZUFFJwE2Mq4Tlw2yjoN2cC%2BfTNIpxKmIG12J1XbfZorwyruWfLEJJhn%2BTVpQj1LOixDJoFGuRRm%2FMGs9DLJejFs15x41sh3aNPpK4nAKF9MccEBKuN8lvcDIMyrqAwNRI9r%2Fbcf0ve94M8RWfGUojDQ4RN9%2Fcntq3cFY8kpm5cLS5x7stwXi6ug5dwpsRBZtr85%2FD7%2BcBkhyobF8PeLwuNXY6vHnHDVBcL4RQW%2Bves4NVvuBQ%2BdOGGeonj936OZStsY9FzR75iass3QepEaJGkN9qSpMC%2BuBjwMxcNBuJxGPtjgOyWHpAveWcduPnFKYCKKEYwqYwi12V%2FxFSKdTOosYhHwmUM0tbowlsqNygY6pgEDTYqTUeIZXkGaWPk1i48VH%2FtYDHiE6Tl7EZkARySekHnQlMlW6QHoun94LxO5lkP1Mwn16j3%2FzVKBzHTX2VK0PLgkgl6gJkF%2FT0Go5ellSHAxaWH%2F6q%2B1KNxaTJiBQ6YR7UT52uNBSA5FsLRyHcfb3oJbm8jqPh96uXTC83fUYvDxj9lZLixApAAlkvKvHUooEugw6Qn6orbr6vNhib2wtRukUkYS&X-Amz-Signature=430c1ae24c6f5c4721770aa925904b0d2a6a58dc01fea6c2d0dfaeda90bde866&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHERIEKQ%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExkRAmgasK7LARVu8f9lZXC0CJtoBbNLaT9f%2B5o5JK8AiBozif1yNnLiY2EnBUzCvzJxBqUAapH6XyY%2FjI3BJqUUCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMixXHh7Ja8PmOnVmMKtwDPI50JukLXJyhBMDL8umV0f692RkkbGTjrUaseZc66pACfg%2FCJ6lI5ZuYg149%2Ff5NCYwoNB4AksriPHLfKoUyN6jBTCDc%2BTjzGtp1WgDL51%2Fb7fTQtb7PrTVbKxZ7%2FFtnf%2BYLtgle9yIQwdScEeHatey%2Bu6JRPOE55SWm0q%2FuXHpSFDt5FvCRNn6yb9UWtx%2BK2ixODZ7Tr7bPsc7NH1ku3Jtv17KK6AG2O%2Fl3QuiXenbLIvvi6LgApthdcaSEX2w4Fgz%2BL3XbtoMzx3q6p397OKenfZUFFJwE2Mq4Tlw2yjoN2cC%2BfTNIpxKmIG12J1XbfZorwyruWfLEJJhn%2BTVpQj1LOixDJoFGuRRm%2FMGs9DLJejFs15x41sh3aNPpK4nAKF9MccEBKuN8lvcDIMyrqAwNRI9r%2Fbcf0ve94M8RWfGUojDQ4RN9%2Fcntq3cFY8kpm5cLS5x7stwXi6ug5dwpsRBZtr85%2FD7%2BcBkhyobF8PeLwuNXY6vHnHDVBcL4RQW%2Bves4NVvuBQ%2BdOGGeonj936OZStsY9FzR75iass3QepEaJGkN9qSpMC%2BuBjwMxcNBuJxGPtjgOyWHpAveWcduPnFKYCKKEYwqYwi12V%2FxFSKdTOosYhHwmUM0tbowlsqNygY6pgEDTYqTUeIZXkGaWPk1i48VH%2FtYDHiE6Tl7EZkARySekHnQlMlW6QHoun94LxO5lkP1Mwn16j3%2FzVKBzHTX2VK0PLgkgl6gJkF%2FT0Go5ellSHAxaWH%2F6q%2B1KNxaTJiBQ6YR7UT52uNBSA5FsLRyHcfb3oJbm8jqPh96uXTC83fUYvDxj9lZLixApAAlkvKvHUooEugw6Qn6orbr6vNhib2wtRukUkYS&X-Amz-Signature=76bc385467ac7f8f5ba08fbc93d3049c4ae07dbe1375f9375358a1b9b9210524&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHERIEKQ%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExkRAmgasK7LARVu8f9lZXC0CJtoBbNLaT9f%2B5o5JK8AiBozif1yNnLiY2EnBUzCvzJxBqUAapH6XyY%2FjI3BJqUUCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMixXHh7Ja8PmOnVmMKtwDPI50JukLXJyhBMDL8umV0f692RkkbGTjrUaseZc66pACfg%2FCJ6lI5ZuYg149%2Ff5NCYwoNB4AksriPHLfKoUyN6jBTCDc%2BTjzGtp1WgDL51%2Fb7fTQtb7PrTVbKxZ7%2FFtnf%2BYLtgle9yIQwdScEeHatey%2Bu6JRPOE55SWm0q%2FuXHpSFDt5FvCRNn6yb9UWtx%2BK2ixODZ7Tr7bPsc7NH1ku3Jtv17KK6AG2O%2Fl3QuiXenbLIvvi6LgApthdcaSEX2w4Fgz%2BL3XbtoMzx3q6p397OKenfZUFFJwE2Mq4Tlw2yjoN2cC%2BfTNIpxKmIG12J1XbfZorwyruWfLEJJhn%2BTVpQj1LOixDJoFGuRRm%2FMGs9DLJejFs15x41sh3aNPpK4nAKF9MccEBKuN8lvcDIMyrqAwNRI9r%2Fbcf0ve94M8RWfGUojDQ4RN9%2Fcntq3cFY8kpm5cLS5x7stwXi6ug5dwpsRBZtr85%2FD7%2BcBkhyobF8PeLwuNXY6vHnHDVBcL4RQW%2Bves4NVvuBQ%2BdOGGeonj936OZStsY9FzR75iass3QepEaJGkN9qSpMC%2BuBjwMxcNBuJxGPtjgOyWHpAveWcduPnFKYCKKEYwqYwi12V%2FxFSKdTOosYhHwmUM0tbowlsqNygY6pgEDTYqTUeIZXkGaWPk1i48VH%2FtYDHiE6Tl7EZkARySekHnQlMlW6QHoun94LxO5lkP1Mwn16j3%2FzVKBzHTX2VK0PLgkgl6gJkF%2FT0Go5ellSHAxaWH%2F6q%2B1KNxaTJiBQ6YR7UT52uNBSA5FsLRyHcfb3oJbm8jqPh96uXTC83fUYvDxj9lZLixApAAlkvKvHUooEugw6Qn6orbr6vNhib2wtRukUkYS&X-Amz-Signature=a06b9f51c26b1f2a16b0cacd69ba88221ab83e0ee626476f23693256ccf3da96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

