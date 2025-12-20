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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645PCGTVX%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH9d9hw0l7sXs%2FpmUys2rv1NCuxyIDdNNH%2BSjQwkOA5zAiEA46Cl8i%2FPARY2OP5WdCJXCmpThJfRX2ycqPvvDRES19kqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIRQoQMmMq1%2FW%2FkCNCrcAwSvyu3OxCdWj4S15p4JHdWWKmlX%2FucCIOf1KJA%2B6xMXaaA2ju%2Fm5uyOh0i8DXLHw6gJf%2Fh8L%2BcIyxcwQ7G%2BvKDUN7GJX%2FiIxc3CKGY5Udd0MKYWri%2FbH4ECK3auZDLCqZRVNTL%2B49aMPh9Q2Tmz69U7pGJghfcSXwccdSX1WXjdaxZlK6Zj3zrUyeTrEVZKMsG1T%2BesvflmRNoyz5I28pMUj%2BEa2ty9qD0G%2FCjxilo%2FwFNqAgXp3MZXMAh3mmspopDEk%2BgCQYIYVmM%2BrL3evqle47kHsF5%2Bx698Ixoht0PrbP4ayeDYdlhmVtvRIfi4WdyPABJYIJKOcZGPuhbsSZzsLerMqZpTdrPnlD9fxmplHQmkRCURnEaornV%2FGeLzCb3kITXy5bWHrd2Xa%2FRdx6mfh5l7pmNOBiH%2BXUFoqRufyXma5h%2BIhc6cdFgu5gjkJDjME6CtTxuaCJQVN6irWlwW5aJvAV85Zb3aLX3Om1YW0EONh7bfwI8n7V3d7YPaSEtduXFZzda7xsMO79AdMdEDwIRjN1R7xii2R99rxfbAB31scfjqEeTFhxZZBeOww%2FzutrCfIiXW0re8PfiwUDkF1P6ebCXahjhIeYjadsaxnFYxLrKS6oCELep4MPKFmMoGOqUBo%2BAxzY0mI33C9UzugPxokcYQau1pO8CfCn0IT7kNNCKTlfjc9LyMpq6omDpNffiRaoUnn3MW8jCDppI%2FMzwuAWjUv7B%2FBzc4i%2FPOjiaABU19jmzd8N8CeqqPkKENejq6kLWgajmHfS%2BHy0hggOkaJOTl8KNb8zAscte3oGbisGK9gbwizsD7fJwFEtxf%2B%2FthnkwepmvOeVaprZVsew72%2FGNGfQyK&X-Amz-Signature=2630edbc67730d44d58003d57926a0331864891168a717f96dbeffcb98ba8b99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645PCGTVX%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH9d9hw0l7sXs%2FpmUys2rv1NCuxyIDdNNH%2BSjQwkOA5zAiEA46Cl8i%2FPARY2OP5WdCJXCmpThJfRX2ycqPvvDRES19kqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIRQoQMmMq1%2FW%2FkCNCrcAwSvyu3OxCdWj4S15p4JHdWWKmlX%2FucCIOf1KJA%2B6xMXaaA2ju%2Fm5uyOh0i8DXLHw6gJf%2Fh8L%2BcIyxcwQ7G%2BvKDUN7GJX%2FiIxc3CKGY5Udd0MKYWri%2FbH4ECK3auZDLCqZRVNTL%2B49aMPh9Q2Tmz69U7pGJghfcSXwccdSX1WXjdaxZlK6Zj3zrUyeTrEVZKMsG1T%2BesvflmRNoyz5I28pMUj%2BEa2ty9qD0G%2FCjxilo%2FwFNqAgXp3MZXMAh3mmspopDEk%2BgCQYIYVmM%2BrL3evqle47kHsF5%2Bx698Ixoht0PrbP4ayeDYdlhmVtvRIfi4WdyPABJYIJKOcZGPuhbsSZzsLerMqZpTdrPnlD9fxmplHQmkRCURnEaornV%2FGeLzCb3kITXy5bWHrd2Xa%2FRdx6mfh5l7pmNOBiH%2BXUFoqRufyXma5h%2BIhc6cdFgu5gjkJDjME6CtTxuaCJQVN6irWlwW5aJvAV85Zb3aLX3Om1YW0EONh7bfwI8n7V3d7YPaSEtduXFZzda7xsMO79AdMdEDwIRjN1R7xii2R99rxfbAB31scfjqEeTFhxZZBeOww%2FzutrCfIiXW0re8PfiwUDkF1P6ebCXahjhIeYjadsaxnFYxLrKS6oCELep4MPKFmMoGOqUBo%2BAxzY0mI33C9UzugPxokcYQau1pO8CfCn0IT7kNNCKTlfjc9LyMpq6omDpNffiRaoUnn3MW8jCDppI%2FMzwuAWjUv7B%2FBzc4i%2FPOjiaABU19jmzd8N8CeqqPkKENejq6kLWgajmHfS%2BHy0hggOkaJOTl8KNb8zAscte3oGbisGK9gbwizsD7fJwFEtxf%2B%2FthnkwepmvOeVaprZVsew72%2FGNGfQyK&X-Amz-Signature=5c576143d234086488ee80ec0118a6f6dae6a0c892dc8965d08072a58ef184a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645PCGTVX%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH9d9hw0l7sXs%2FpmUys2rv1NCuxyIDdNNH%2BSjQwkOA5zAiEA46Cl8i%2FPARY2OP5WdCJXCmpThJfRX2ycqPvvDRES19kqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIRQoQMmMq1%2FW%2FkCNCrcAwSvyu3OxCdWj4S15p4JHdWWKmlX%2FucCIOf1KJA%2B6xMXaaA2ju%2Fm5uyOh0i8DXLHw6gJf%2Fh8L%2BcIyxcwQ7G%2BvKDUN7GJX%2FiIxc3CKGY5Udd0MKYWri%2FbH4ECK3auZDLCqZRVNTL%2B49aMPh9Q2Tmz69U7pGJghfcSXwccdSX1WXjdaxZlK6Zj3zrUyeTrEVZKMsG1T%2BesvflmRNoyz5I28pMUj%2BEa2ty9qD0G%2FCjxilo%2FwFNqAgXp3MZXMAh3mmspopDEk%2BgCQYIYVmM%2BrL3evqle47kHsF5%2Bx698Ixoht0PrbP4ayeDYdlhmVtvRIfi4WdyPABJYIJKOcZGPuhbsSZzsLerMqZpTdrPnlD9fxmplHQmkRCURnEaornV%2FGeLzCb3kITXy5bWHrd2Xa%2FRdx6mfh5l7pmNOBiH%2BXUFoqRufyXma5h%2BIhc6cdFgu5gjkJDjME6CtTxuaCJQVN6irWlwW5aJvAV85Zb3aLX3Om1YW0EONh7bfwI8n7V3d7YPaSEtduXFZzda7xsMO79AdMdEDwIRjN1R7xii2R99rxfbAB31scfjqEeTFhxZZBeOww%2FzutrCfIiXW0re8PfiwUDkF1P6ebCXahjhIeYjadsaxnFYxLrKS6oCELep4MPKFmMoGOqUBo%2BAxzY0mI33C9UzugPxokcYQau1pO8CfCn0IT7kNNCKTlfjc9LyMpq6omDpNffiRaoUnn3MW8jCDppI%2FMzwuAWjUv7B%2FBzc4i%2FPOjiaABU19jmzd8N8CeqqPkKENejq6kLWgajmHfS%2BHy0hggOkaJOTl8KNb8zAscte3oGbisGK9gbwizsD7fJwFEtxf%2B%2FthnkwepmvOeVaprZVsew72%2FGNGfQyK&X-Amz-Signature=6fb2ed4c337d38ac5cc3fafec72b28c2b12f983d10d2d5af1c21e251c0177bac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645PCGTVX%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH9d9hw0l7sXs%2FpmUys2rv1NCuxyIDdNNH%2BSjQwkOA5zAiEA46Cl8i%2FPARY2OP5WdCJXCmpThJfRX2ycqPvvDRES19kqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIRQoQMmMq1%2FW%2FkCNCrcAwSvyu3OxCdWj4S15p4JHdWWKmlX%2FucCIOf1KJA%2B6xMXaaA2ju%2Fm5uyOh0i8DXLHw6gJf%2Fh8L%2BcIyxcwQ7G%2BvKDUN7GJX%2FiIxc3CKGY5Udd0MKYWri%2FbH4ECK3auZDLCqZRVNTL%2B49aMPh9Q2Tmz69U7pGJghfcSXwccdSX1WXjdaxZlK6Zj3zrUyeTrEVZKMsG1T%2BesvflmRNoyz5I28pMUj%2BEa2ty9qD0G%2FCjxilo%2FwFNqAgXp3MZXMAh3mmspopDEk%2BgCQYIYVmM%2BrL3evqle47kHsF5%2Bx698Ixoht0PrbP4ayeDYdlhmVtvRIfi4WdyPABJYIJKOcZGPuhbsSZzsLerMqZpTdrPnlD9fxmplHQmkRCURnEaornV%2FGeLzCb3kITXy5bWHrd2Xa%2FRdx6mfh5l7pmNOBiH%2BXUFoqRufyXma5h%2BIhc6cdFgu5gjkJDjME6CtTxuaCJQVN6irWlwW5aJvAV85Zb3aLX3Om1YW0EONh7bfwI8n7V3d7YPaSEtduXFZzda7xsMO79AdMdEDwIRjN1R7xii2R99rxfbAB31scfjqEeTFhxZZBeOww%2FzutrCfIiXW0re8PfiwUDkF1P6ebCXahjhIeYjadsaxnFYxLrKS6oCELep4MPKFmMoGOqUBo%2BAxzY0mI33C9UzugPxokcYQau1pO8CfCn0IT7kNNCKTlfjc9LyMpq6omDpNffiRaoUnn3MW8jCDppI%2FMzwuAWjUv7B%2FBzc4i%2FPOjiaABU19jmzd8N8CeqqPkKENejq6kLWgajmHfS%2BHy0hggOkaJOTl8KNb8zAscte3oGbisGK9gbwizsD7fJwFEtxf%2B%2FthnkwepmvOeVaprZVsew72%2FGNGfQyK&X-Amz-Signature=fef7ad46747a2a84519bf10013d3fe7e481cae1d9445b4fa4b894702c97fe530&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645PCGTVX%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH9d9hw0l7sXs%2FpmUys2rv1NCuxyIDdNNH%2BSjQwkOA5zAiEA46Cl8i%2FPARY2OP5WdCJXCmpThJfRX2ycqPvvDRES19kqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIRQoQMmMq1%2FW%2FkCNCrcAwSvyu3OxCdWj4S15p4JHdWWKmlX%2FucCIOf1KJA%2B6xMXaaA2ju%2Fm5uyOh0i8DXLHw6gJf%2Fh8L%2BcIyxcwQ7G%2BvKDUN7GJX%2FiIxc3CKGY5Udd0MKYWri%2FbH4ECK3auZDLCqZRVNTL%2B49aMPh9Q2Tmz69U7pGJghfcSXwccdSX1WXjdaxZlK6Zj3zrUyeTrEVZKMsG1T%2BesvflmRNoyz5I28pMUj%2BEa2ty9qD0G%2FCjxilo%2FwFNqAgXp3MZXMAh3mmspopDEk%2BgCQYIYVmM%2BrL3evqle47kHsF5%2Bx698Ixoht0PrbP4ayeDYdlhmVtvRIfi4WdyPABJYIJKOcZGPuhbsSZzsLerMqZpTdrPnlD9fxmplHQmkRCURnEaornV%2FGeLzCb3kITXy5bWHrd2Xa%2FRdx6mfh5l7pmNOBiH%2BXUFoqRufyXma5h%2BIhc6cdFgu5gjkJDjME6CtTxuaCJQVN6irWlwW5aJvAV85Zb3aLX3Om1YW0EONh7bfwI8n7V3d7YPaSEtduXFZzda7xsMO79AdMdEDwIRjN1R7xii2R99rxfbAB31scfjqEeTFhxZZBeOww%2FzutrCfIiXW0re8PfiwUDkF1P6ebCXahjhIeYjadsaxnFYxLrKS6oCELep4MPKFmMoGOqUBo%2BAxzY0mI33C9UzugPxokcYQau1pO8CfCn0IT7kNNCKTlfjc9LyMpq6omDpNffiRaoUnn3MW8jCDppI%2FMzwuAWjUv7B%2FBzc4i%2FPOjiaABU19jmzd8N8CeqqPkKENejq6kLWgajmHfS%2BHy0hggOkaJOTl8KNb8zAscte3oGbisGK9gbwizsD7fJwFEtxf%2B%2FthnkwepmvOeVaprZVsew72%2FGNGfQyK&X-Amz-Signature=509264a84c063f954a832cbc23b53ace1dba094933881fc9cbd5ce51806f69ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645PCGTVX%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH9d9hw0l7sXs%2FpmUys2rv1NCuxyIDdNNH%2BSjQwkOA5zAiEA46Cl8i%2FPARY2OP5WdCJXCmpThJfRX2ycqPvvDRES19kqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIRQoQMmMq1%2FW%2FkCNCrcAwSvyu3OxCdWj4S15p4JHdWWKmlX%2FucCIOf1KJA%2B6xMXaaA2ju%2Fm5uyOh0i8DXLHw6gJf%2Fh8L%2BcIyxcwQ7G%2BvKDUN7GJX%2FiIxc3CKGY5Udd0MKYWri%2FbH4ECK3auZDLCqZRVNTL%2B49aMPh9Q2Tmz69U7pGJghfcSXwccdSX1WXjdaxZlK6Zj3zrUyeTrEVZKMsG1T%2BesvflmRNoyz5I28pMUj%2BEa2ty9qD0G%2FCjxilo%2FwFNqAgXp3MZXMAh3mmspopDEk%2BgCQYIYVmM%2BrL3evqle47kHsF5%2Bx698Ixoht0PrbP4ayeDYdlhmVtvRIfi4WdyPABJYIJKOcZGPuhbsSZzsLerMqZpTdrPnlD9fxmplHQmkRCURnEaornV%2FGeLzCb3kITXy5bWHrd2Xa%2FRdx6mfh5l7pmNOBiH%2BXUFoqRufyXma5h%2BIhc6cdFgu5gjkJDjME6CtTxuaCJQVN6irWlwW5aJvAV85Zb3aLX3Om1YW0EONh7bfwI8n7V3d7YPaSEtduXFZzda7xsMO79AdMdEDwIRjN1R7xii2R99rxfbAB31scfjqEeTFhxZZBeOww%2FzutrCfIiXW0re8PfiwUDkF1P6ebCXahjhIeYjadsaxnFYxLrKS6oCELep4MPKFmMoGOqUBo%2BAxzY0mI33C9UzugPxokcYQau1pO8CfCn0IT7kNNCKTlfjc9LyMpq6omDpNffiRaoUnn3MW8jCDppI%2FMzwuAWjUv7B%2FBzc4i%2FPOjiaABU19jmzd8N8CeqqPkKENejq6kLWgajmHfS%2BHy0hggOkaJOTl8KNb8zAscte3oGbisGK9gbwizsD7fJwFEtxf%2B%2FthnkwepmvOeVaprZVsew72%2FGNGfQyK&X-Amz-Signature=6a9ee34eda4fd600be264a535fe66bb7b1bc4431bd1795569d5a8c61e45d350d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645PCGTVX%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH9d9hw0l7sXs%2FpmUys2rv1NCuxyIDdNNH%2BSjQwkOA5zAiEA46Cl8i%2FPARY2OP5WdCJXCmpThJfRX2ycqPvvDRES19kqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIRQoQMmMq1%2FW%2FkCNCrcAwSvyu3OxCdWj4S15p4JHdWWKmlX%2FucCIOf1KJA%2B6xMXaaA2ju%2Fm5uyOh0i8DXLHw6gJf%2Fh8L%2BcIyxcwQ7G%2BvKDUN7GJX%2FiIxc3CKGY5Udd0MKYWri%2FbH4ECK3auZDLCqZRVNTL%2B49aMPh9Q2Tmz69U7pGJghfcSXwccdSX1WXjdaxZlK6Zj3zrUyeTrEVZKMsG1T%2BesvflmRNoyz5I28pMUj%2BEa2ty9qD0G%2FCjxilo%2FwFNqAgXp3MZXMAh3mmspopDEk%2BgCQYIYVmM%2BrL3evqle47kHsF5%2Bx698Ixoht0PrbP4ayeDYdlhmVtvRIfi4WdyPABJYIJKOcZGPuhbsSZzsLerMqZpTdrPnlD9fxmplHQmkRCURnEaornV%2FGeLzCb3kITXy5bWHrd2Xa%2FRdx6mfh5l7pmNOBiH%2BXUFoqRufyXma5h%2BIhc6cdFgu5gjkJDjME6CtTxuaCJQVN6irWlwW5aJvAV85Zb3aLX3Om1YW0EONh7bfwI8n7V3d7YPaSEtduXFZzda7xsMO79AdMdEDwIRjN1R7xii2R99rxfbAB31scfjqEeTFhxZZBeOww%2FzutrCfIiXW0re8PfiwUDkF1P6ebCXahjhIeYjadsaxnFYxLrKS6oCELep4MPKFmMoGOqUBo%2BAxzY0mI33C9UzugPxokcYQau1pO8CfCn0IT7kNNCKTlfjc9LyMpq6omDpNffiRaoUnn3MW8jCDppI%2FMzwuAWjUv7B%2FBzc4i%2FPOjiaABU19jmzd8N8CeqqPkKENejq6kLWgajmHfS%2BHy0hggOkaJOTl8KNb8zAscte3oGbisGK9gbwizsD7fJwFEtxf%2B%2FthnkwepmvOeVaprZVsew72%2FGNGfQyK&X-Amz-Signature=2ef6d23171115d8dba944194f7db6522281c37d40436f1ee06aef831ca4db8eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

