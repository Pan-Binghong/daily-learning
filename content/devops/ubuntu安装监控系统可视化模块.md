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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLMRVRJ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFW3CpyiF%2FjYiZObYwcLxIQc84zTybWa29jpwworLpduAiA9Y5cg4jM70wP0srJ%2BvjAcLP7ZVmRH4rpLUxe9Ar59fCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOlQSLbZvU085r4jpKtwDUja6ued7tRdQKa0edsv2l92i%2B2it9sbm7oSUeTbUXgeNuuQ0%2Byd94xPBM8H8ZHzJ2PstSDOFXu%2FGEhxe0fU6ZEq2jOnfzc2LuddskVoqWYuzyI9bCV0a53xIYMIjiW5TKnDLj2D2SFgM2BK8K%2F2LIiUIyrQgmflAFhKZPakgjlz6Weo7%2Ff1awUHy3z2T0xyAHVVoITGGnE%2FPOF2SKWt5oZZJ7D4tp5AmPaGyE1aSLIB6F5WdloX9LbYVXpRq%2B7fwrGTqdxCWM3U2orkKoc5JYYCEmWLsF4cAqrsVNMSnBPP58Jk6tX7GfBIFdAipmp8Kd0cNMwbupQrG3cx1IcZPPpw4ThFuPzrF2Sz3%2Fs5CkysUQCYZofd2dWhgpHFCp7sYBAYwQ8mqPh4VVdwf5biO5I0r6mmG57V0fKrBQ3r9Mq6vxhnz7zLTmErTVx5SFxah7BgaCf15UzLdSj%2BITXdEAFipbhidja9z8V4sYG4ci6Vdpe5rpx0KZFF89OYEiajqGFHE5Fz1HvOo0Us%2FjO3f%2FIl7kbbVcxknQeEGTTZQFEpXdAn29nAyFWff84%2F6LBFw%2BPpWqjBNSYtCgANraEFalqGHfBHAyFRaeqOOyoeLudZZFomGa8cLdT7t4%2BgwyvGvyAY6pgESF9HnfFlQQXT7ajaTYI4Iyg6sJyX%2BxU29ru%2By8HZE2ExRBc5c1W6HfEdwCE72IHWkRX7i8ruecto8%2Fan6uvXoldTyA5fG459ck7vIBTte7Jm47mO7uWh4vV08msNSsHuiZDGENnc13%2FFhehaKa05DTiHU%2BGzmxuKzGFPTxlgoLlbAkOt5DhzqkPYvzGXIEcnwtJtjCRpDF0%2BbuWEcUuAd9%2B1Bu2Qq&X-Amz-Signature=6a2bf4ae2b336337ae32d5ed0d883f5a96d918d71d44e512ced22d6a9b6ca4c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLMRVRJ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFW3CpyiF%2FjYiZObYwcLxIQc84zTybWa29jpwworLpduAiA9Y5cg4jM70wP0srJ%2BvjAcLP7ZVmRH4rpLUxe9Ar59fCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOlQSLbZvU085r4jpKtwDUja6ued7tRdQKa0edsv2l92i%2B2it9sbm7oSUeTbUXgeNuuQ0%2Byd94xPBM8H8ZHzJ2PstSDOFXu%2FGEhxe0fU6ZEq2jOnfzc2LuddskVoqWYuzyI9bCV0a53xIYMIjiW5TKnDLj2D2SFgM2BK8K%2F2LIiUIyrQgmflAFhKZPakgjlz6Weo7%2Ff1awUHy3z2T0xyAHVVoITGGnE%2FPOF2SKWt5oZZJ7D4tp5AmPaGyE1aSLIB6F5WdloX9LbYVXpRq%2B7fwrGTqdxCWM3U2orkKoc5JYYCEmWLsF4cAqrsVNMSnBPP58Jk6tX7GfBIFdAipmp8Kd0cNMwbupQrG3cx1IcZPPpw4ThFuPzrF2Sz3%2Fs5CkysUQCYZofd2dWhgpHFCp7sYBAYwQ8mqPh4VVdwf5biO5I0r6mmG57V0fKrBQ3r9Mq6vxhnz7zLTmErTVx5SFxah7BgaCf15UzLdSj%2BITXdEAFipbhidja9z8V4sYG4ci6Vdpe5rpx0KZFF89OYEiajqGFHE5Fz1HvOo0Us%2FjO3f%2FIl7kbbVcxknQeEGTTZQFEpXdAn29nAyFWff84%2F6LBFw%2BPpWqjBNSYtCgANraEFalqGHfBHAyFRaeqOOyoeLudZZFomGa8cLdT7t4%2BgwyvGvyAY6pgESF9HnfFlQQXT7ajaTYI4Iyg6sJyX%2BxU29ru%2By8HZE2ExRBc5c1W6HfEdwCE72IHWkRX7i8ruecto8%2Fan6uvXoldTyA5fG459ck7vIBTte7Jm47mO7uWh4vV08msNSsHuiZDGENnc13%2FFhehaKa05DTiHU%2BGzmxuKzGFPTxlgoLlbAkOt5DhzqkPYvzGXIEcnwtJtjCRpDF0%2BbuWEcUuAd9%2B1Bu2Qq&X-Amz-Signature=86c19a5aa3de3a08355de80193c6f8b6b17e004fb8064cafeb81c42ef49af33a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLMRVRJ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFW3CpyiF%2FjYiZObYwcLxIQc84zTybWa29jpwworLpduAiA9Y5cg4jM70wP0srJ%2BvjAcLP7ZVmRH4rpLUxe9Ar59fCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOlQSLbZvU085r4jpKtwDUja6ued7tRdQKa0edsv2l92i%2B2it9sbm7oSUeTbUXgeNuuQ0%2Byd94xPBM8H8ZHzJ2PstSDOFXu%2FGEhxe0fU6ZEq2jOnfzc2LuddskVoqWYuzyI9bCV0a53xIYMIjiW5TKnDLj2D2SFgM2BK8K%2F2LIiUIyrQgmflAFhKZPakgjlz6Weo7%2Ff1awUHy3z2T0xyAHVVoITGGnE%2FPOF2SKWt5oZZJ7D4tp5AmPaGyE1aSLIB6F5WdloX9LbYVXpRq%2B7fwrGTqdxCWM3U2orkKoc5JYYCEmWLsF4cAqrsVNMSnBPP58Jk6tX7GfBIFdAipmp8Kd0cNMwbupQrG3cx1IcZPPpw4ThFuPzrF2Sz3%2Fs5CkysUQCYZofd2dWhgpHFCp7sYBAYwQ8mqPh4VVdwf5biO5I0r6mmG57V0fKrBQ3r9Mq6vxhnz7zLTmErTVx5SFxah7BgaCf15UzLdSj%2BITXdEAFipbhidja9z8V4sYG4ci6Vdpe5rpx0KZFF89OYEiajqGFHE5Fz1HvOo0Us%2FjO3f%2FIl7kbbVcxknQeEGTTZQFEpXdAn29nAyFWff84%2F6LBFw%2BPpWqjBNSYtCgANraEFalqGHfBHAyFRaeqOOyoeLudZZFomGa8cLdT7t4%2BgwyvGvyAY6pgESF9HnfFlQQXT7ajaTYI4Iyg6sJyX%2BxU29ru%2By8HZE2ExRBc5c1W6HfEdwCE72IHWkRX7i8ruecto8%2Fan6uvXoldTyA5fG459ck7vIBTte7Jm47mO7uWh4vV08msNSsHuiZDGENnc13%2FFhehaKa05DTiHU%2BGzmxuKzGFPTxlgoLlbAkOt5DhzqkPYvzGXIEcnwtJtjCRpDF0%2BbuWEcUuAd9%2B1Bu2Qq&X-Amz-Signature=8c775813990c2e53fde973835b0023de5115013f9d9ae6037071a3804fd0f656&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLMRVRJ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFW3CpyiF%2FjYiZObYwcLxIQc84zTybWa29jpwworLpduAiA9Y5cg4jM70wP0srJ%2BvjAcLP7ZVmRH4rpLUxe9Ar59fCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOlQSLbZvU085r4jpKtwDUja6ued7tRdQKa0edsv2l92i%2B2it9sbm7oSUeTbUXgeNuuQ0%2Byd94xPBM8H8ZHzJ2PstSDOFXu%2FGEhxe0fU6ZEq2jOnfzc2LuddskVoqWYuzyI9bCV0a53xIYMIjiW5TKnDLj2D2SFgM2BK8K%2F2LIiUIyrQgmflAFhKZPakgjlz6Weo7%2Ff1awUHy3z2T0xyAHVVoITGGnE%2FPOF2SKWt5oZZJ7D4tp5AmPaGyE1aSLIB6F5WdloX9LbYVXpRq%2B7fwrGTqdxCWM3U2orkKoc5JYYCEmWLsF4cAqrsVNMSnBPP58Jk6tX7GfBIFdAipmp8Kd0cNMwbupQrG3cx1IcZPPpw4ThFuPzrF2Sz3%2Fs5CkysUQCYZofd2dWhgpHFCp7sYBAYwQ8mqPh4VVdwf5biO5I0r6mmG57V0fKrBQ3r9Mq6vxhnz7zLTmErTVx5SFxah7BgaCf15UzLdSj%2BITXdEAFipbhidja9z8V4sYG4ci6Vdpe5rpx0KZFF89OYEiajqGFHE5Fz1HvOo0Us%2FjO3f%2FIl7kbbVcxknQeEGTTZQFEpXdAn29nAyFWff84%2F6LBFw%2BPpWqjBNSYtCgANraEFalqGHfBHAyFRaeqOOyoeLudZZFomGa8cLdT7t4%2BgwyvGvyAY6pgESF9HnfFlQQXT7ajaTYI4Iyg6sJyX%2BxU29ru%2By8HZE2ExRBc5c1W6HfEdwCE72IHWkRX7i8ruecto8%2Fan6uvXoldTyA5fG459ck7vIBTte7Jm47mO7uWh4vV08msNSsHuiZDGENnc13%2FFhehaKa05DTiHU%2BGzmxuKzGFPTxlgoLlbAkOt5DhzqkPYvzGXIEcnwtJtjCRpDF0%2BbuWEcUuAd9%2B1Bu2Qq&X-Amz-Signature=97d71a1ef81a8b9b3c31a7e4c853c9ff4c5377741d0cdff3bc920e5f6be537a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLMRVRJ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFW3CpyiF%2FjYiZObYwcLxIQc84zTybWa29jpwworLpduAiA9Y5cg4jM70wP0srJ%2BvjAcLP7ZVmRH4rpLUxe9Ar59fCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOlQSLbZvU085r4jpKtwDUja6ued7tRdQKa0edsv2l92i%2B2it9sbm7oSUeTbUXgeNuuQ0%2Byd94xPBM8H8ZHzJ2PstSDOFXu%2FGEhxe0fU6ZEq2jOnfzc2LuddskVoqWYuzyI9bCV0a53xIYMIjiW5TKnDLj2D2SFgM2BK8K%2F2LIiUIyrQgmflAFhKZPakgjlz6Weo7%2Ff1awUHy3z2T0xyAHVVoITGGnE%2FPOF2SKWt5oZZJ7D4tp5AmPaGyE1aSLIB6F5WdloX9LbYVXpRq%2B7fwrGTqdxCWM3U2orkKoc5JYYCEmWLsF4cAqrsVNMSnBPP58Jk6tX7GfBIFdAipmp8Kd0cNMwbupQrG3cx1IcZPPpw4ThFuPzrF2Sz3%2Fs5CkysUQCYZofd2dWhgpHFCp7sYBAYwQ8mqPh4VVdwf5biO5I0r6mmG57V0fKrBQ3r9Mq6vxhnz7zLTmErTVx5SFxah7BgaCf15UzLdSj%2BITXdEAFipbhidja9z8V4sYG4ci6Vdpe5rpx0KZFF89OYEiajqGFHE5Fz1HvOo0Us%2FjO3f%2FIl7kbbVcxknQeEGTTZQFEpXdAn29nAyFWff84%2F6LBFw%2BPpWqjBNSYtCgANraEFalqGHfBHAyFRaeqOOyoeLudZZFomGa8cLdT7t4%2BgwyvGvyAY6pgESF9HnfFlQQXT7ajaTYI4Iyg6sJyX%2BxU29ru%2By8HZE2ExRBc5c1W6HfEdwCE72IHWkRX7i8ruecto8%2Fan6uvXoldTyA5fG459ck7vIBTte7Jm47mO7uWh4vV08msNSsHuiZDGENnc13%2FFhehaKa05DTiHU%2BGzmxuKzGFPTxlgoLlbAkOt5DhzqkPYvzGXIEcnwtJtjCRpDF0%2BbuWEcUuAd9%2B1Bu2Qq&X-Amz-Signature=c7108bbfe1156ce5aa1f5bfc7e00eed0a9937470590a7e19df6954b43a5f17da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLMRVRJ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFW3CpyiF%2FjYiZObYwcLxIQc84zTybWa29jpwworLpduAiA9Y5cg4jM70wP0srJ%2BvjAcLP7ZVmRH4rpLUxe9Ar59fCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOlQSLbZvU085r4jpKtwDUja6ued7tRdQKa0edsv2l92i%2B2it9sbm7oSUeTbUXgeNuuQ0%2Byd94xPBM8H8ZHzJ2PstSDOFXu%2FGEhxe0fU6ZEq2jOnfzc2LuddskVoqWYuzyI9bCV0a53xIYMIjiW5TKnDLj2D2SFgM2BK8K%2F2LIiUIyrQgmflAFhKZPakgjlz6Weo7%2Ff1awUHy3z2T0xyAHVVoITGGnE%2FPOF2SKWt5oZZJ7D4tp5AmPaGyE1aSLIB6F5WdloX9LbYVXpRq%2B7fwrGTqdxCWM3U2orkKoc5JYYCEmWLsF4cAqrsVNMSnBPP58Jk6tX7GfBIFdAipmp8Kd0cNMwbupQrG3cx1IcZPPpw4ThFuPzrF2Sz3%2Fs5CkysUQCYZofd2dWhgpHFCp7sYBAYwQ8mqPh4VVdwf5biO5I0r6mmG57V0fKrBQ3r9Mq6vxhnz7zLTmErTVx5SFxah7BgaCf15UzLdSj%2BITXdEAFipbhidja9z8V4sYG4ci6Vdpe5rpx0KZFF89OYEiajqGFHE5Fz1HvOo0Us%2FjO3f%2FIl7kbbVcxknQeEGTTZQFEpXdAn29nAyFWff84%2F6LBFw%2BPpWqjBNSYtCgANraEFalqGHfBHAyFRaeqOOyoeLudZZFomGa8cLdT7t4%2BgwyvGvyAY6pgESF9HnfFlQQXT7ajaTYI4Iyg6sJyX%2BxU29ru%2By8HZE2ExRBc5c1W6HfEdwCE72IHWkRX7i8ruecto8%2Fan6uvXoldTyA5fG459ck7vIBTte7Jm47mO7uWh4vV08msNSsHuiZDGENnc13%2FFhehaKa05DTiHU%2BGzmxuKzGFPTxlgoLlbAkOt5DhzqkPYvzGXIEcnwtJtjCRpDF0%2BbuWEcUuAd9%2B1Bu2Qq&X-Amz-Signature=81fe4c5aa5c4c9a4b010f9b9b7927638e30a5e1318c0dc9ca1dca7530b6c5a8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLMRVRJ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFW3CpyiF%2FjYiZObYwcLxIQc84zTybWa29jpwworLpduAiA9Y5cg4jM70wP0srJ%2BvjAcLP7ZVmRH4rpLUxe9Ar59fCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOlQSLbZvU085r4jpKtwDUja6ued7tRdQKa0edsv2l92i%2B2it9sbm7oSUeTbUXgeNuuQ0%2Byd94xPBM8H8ZHzJ2PstSDOFXu%2FGEhxe0fU6ZEq2jOnfzc2LuddskVoqWYuzyI9bCV0a53xIYMIjiW5TKnDLj2D2SFgM2BK8K%2F2LIiUIyrQgmflAFhKZPakgjlz6Weo7%2Ff1awUHy3z2T0xyAHVVoITGGnE%2FPOF2SKWt5oZZJ7D4tp5AmPaGyE1aSLIB6F5WdloX9LbYVXpRq%2B7fwrGTqdxCWM3U2orkKoc5JYYCEmWLsF4cAqrsVNMSnBPP58Jk6tX7GfBIFdAipmp8Kd0cNMwbupQrG3cx1IcZPPpw4ThFuPzrF2Sz3%2Fs5CkysUQCYZofd2dWhgpHFCp7sYBAYwQ8mqPh4VVdwf5biO5I0r6mmG57V0fKrBQ3r9Mq6vxhnz7zLTmErTVx5SFxah7BgaCf15UzLdSj%2BITXdEAFipbhidja9z8V4sYG4ci6Vdpe5rpx0KZFF89OYEiajqGFHE5Fz1HvOo0Us%2FjO3f%2FIl7kbbVcxknQeEGTTZQFEpXdAn29nAyFWff84%2F6LBFw%2BPpWqjBNSYtCgANraEFalqGHfBHAyFRaeqOOyoeLudZZFomGa8cLdT7t4%2BgwyvGvyAY6pgESF9HnfFlQQXT7ajaTYI4Iyg6sJyX%2BxU29ru%2By8HZE2ExRBc5c1W6HfEdwCE72IHWkRX7i8ruecto8%2Fan6uvXoldTyA5fG459ck7vIBTte7Jm47mO7uWh4vV08msNSsHuiZDGENnc13%2FFhehaKa05DTiHU%2BGzmxuKzGFPTxlgoLlbAkOt5DhzqkPYvzGXIEcnwtJtjCRpDF0%2BbuWEcUuAd9%2B1Bu2Qq&X-Amz-Signature=e7164b529f9cad6093956b7794b72576cb4904e029ef8e1afe5317a0a606c50d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

