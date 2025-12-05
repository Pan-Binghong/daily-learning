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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFHVIKP3%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQ1QegILICAbrQLN%2BWmmiLAX9i%2F%2FWekHqmvZlk6RIAugIgZWni7EpzIYYDtWhCpdDDEmvkBuB1VdnOim14N3FoKxsq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDH5wkMM3a6BO2XoaLCrcA3G4p5uNOlFpdPRI1y%2FtqWPkUA51sNz9iT94uHg%2BkKBEVv9m5a%2FasqkgDdBdUq34TJfpQTd19cnDuWFMX7SsWHhmbt1plAyZn9Ez4fGaE1jSXTqf%2F8ECRXeiH3zCw4aRO%2FqupMtUUUBQgZTKAE0%2Fzahsc0KKpJRgOz4a9oRSHS4Dr%2F6iCQWxeW3ON2%2B9vPUhTPlHnAdYkT6XofO4R5LOzuUMyoRYt8QdFScCZB7%2Bk1lY7tPnwI5hpQtO9BRYMsTCEuUbZo6IHtg4c3Nf8ZP7%2BKak%2Be%2B7tsObAtTndlWm8bXqPKGNlbeN3wm0zynwBsk%2BK34vchY4psV1OSF%2FhTO9zU4N7z00a7ybsmMeWTLg70UU1ViKCtPQdLa3CY96g4t86IZ5bsiHX3KxIVrBJ2FebEtCLVIZWFI6joevEoNeFyySHg9sVqhVPAKj2GxmnIRd%2FTOc%2B5NKGSUlG71UL3sXevBnBqJg1MbHf7fyLVFP%2F5%2B92ww83NO0VWQ31oI5aFWsfEBq5gHPgktL%2FNfftY1tVncIgt560syw0unqRNB%2Bn8M1SP2t%2FH%2BwJe7rEPM%2BU7s3pEyYc6HJlg3Eco1e3Is6bYzw980dIfmAzRGr2Up3EpxIVWiETBotffs0kghrMIaMyMkGOqUBZuOdAf%2F5g7kpuJKA1fmzowh8GSyTKcVZ2RSkR%2FBrHIHXWtKjs7wbI5xgLbdg14moBTLyMwSrIbo1SM3mCUevS7%2FlgcI34kkGAzWF%2B%2FyMRi3BkfoJMeW4tCN8eeyx5A4o3pjN4Y5PaiDn45WhkSFXlSRVB6IeKpzdZOQ5Ses7RlnI7MWlv9Xp1QKTO5pQQB4Nz7h4zvR0zB3c0YGzaAse8N1lDgWh&X-Amz-Signature=b27d066c213db7392add2378ab84c790d97e57e1723ee4e3756fc07cf84a8d98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFHVIKP3%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQ1QegILICAbrQLN%2BWmmiLAX9i%2F%2FWekHqmvZlk6RIAugIgZWni7EpzIYYDtWhCpdDDEmvkBuB1VdnOim14N3FoKxsq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDH5wkMM3a6BO2XoaLCrcA3G4p5uNOlFpdPRI1y%2FtqWPkUA51sNz9iT94uHg%2BkKBEVv9m5a%2FasqkgDdBdUq34TJfpQTd19cnDuWFMX7SsWHhmbt1plAyZn9Ez4fGaE1jSXTqf%2F8ECRXeiH3zCw4aRO%2FqupMtUUUBQgZTKAE0%2Fzahsc0KKpJRgOz4a9oRSHS4Dr%2F6iCQWxeW3ON2%2B9vPUhTPlHnAdYkT6XofO4R5LOzuUMyoRYt8QdFScCZB7%2Bk1lY7tPnwI5hpQtO9BRYMsTCEuUbZo6IHtg4c3Nf8ZP7%2BKak%2Be%2B7tsObAtTndlWm8bXqPKGNlbeN3wm0zynwBsk%2BK34vchY4psV1OSF%2FhTO9zU4N7z00a7ybsmMeWTLg70UU1ViKCtPQdLa3CY96g4t86IZ5bsiHX3KxIVrBJ2FebEtCLVIZWFI6joevEoNeFyySHg9sVqhVPAKj2GxmnIRd%2FTOc%2B5NKGSUlG71UL3sXevBnBqJg1MbHf7fyLVFP%2F5%2B92ww83NO0VWQ31oI5aFWsfEBq5gHPgktL%2FNfftY1tVncIgt560syw0unqRNB%2Bn8M1SP2t%2FH%2BwJe7rEPM%2BU7s3pEyYc6HJlg3Eco1e3Is6bYzw980dIfmAzRGr2Up3EpxIVWiETBotffs0kghrMIaMyMkGOqUBZuOdAf%2F5g7kpuJKA1fmzowh8GSyTKcVZ2RSkR%2FBrHIHXWtKjs7wbI5xgLbdg14moBTLyMwSrIbo1SM3mCUevS7%2FlgcI34kkGAzWF%2B%2FyMRi3BkfoJMeW4tCN8eeyx5A4o3pjN4Y5PaiDn45WhkSFXlSRVB6IeKpzdZOQ5Ses7RlnI7MWlv9Xp1QKTO5pQQB4Nz7h4zvR0zB3c0YGzaAse8N1lDgWh&X-Amz-Signature=cba605d959decb27c1d7f7ced0c83f04b12b0fae1a9cce85c5b47457fc5ee697&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFHVIKP3%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQ1QegILICAbrQLN%2BWmmiLAX9i%2F%2FWekHqmvZlk6RIAugIgZWni7EpzIYYDtWhCpdDDEmvkBuB1VdnOim14N3FoKxsq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDH5wkMM3a6BO2XoaLCrcA3G4p5uNOlFpdPRI1y%2FtqWPkUA51sNz9iT94uHg%2BkKBEVv9m5a%2FasqkgDdBdUq34TJfpQTd19cnDuWFMX7SsWHhmbt1plAyZn9Ez4fGaE1jSXTqf%2F8ECRXeiH3zCw4aRO%2FqupMtUUUBQgZTKAE0%2Fzahsc0KKpJRgOz4a9oRSHS4Dr%2F6iCQWxeW3ON2%2B9vPUhTPlHnAdYkT6XofO4R5LOzuUMyoRYt8QdFScCZB7%2Bk1lY7tPnwI5hpQtO9BRYMsTCEuUbZo6IHtg4c3Nf8ZP7%2BKak%2Be%2B7tsObAtTndlWm8bXqPKGNlbeN3wm0zynwBsk%2BK34vchY4psV1OSF%2FhTO9zU4N7z00a7ybsmMeWTLg70UU1ViKCtPQdLa3CY96g4t86IZ5bsiHX3KxIVrBJ2FebEtCLVIZWFI6joevEoNeFyySHg9sVqhVPAKj2GxmnIRd%2FTOc%2B5NKGSUlG71UL3sXevBnBqJg1MbHf7fyLVFP%2F5%2B92ww83NO0VWQ31oI5aFWsfEBq5gHPgktL%2FNfftY1tVncIgt560syw0unqRNB%2Bn8M1SP2t%2FH%2BwJe7rEPM%2BU7s3pEyYc6HJlg3Eco1e3Is6bYzw980dIfmAzRGr2Up3EpxIVWiETBotffs0kghrMIaMyMkGOqUBZuOdAf%2F5g7kpuJKA1fmzowh8GSyTKcVZ2RSkR%2FBrHIHXWtKjs7wbI5xgLbdg14moBTLyMwSrIbo1SM3mCUevS7%2FlgcI34kkGAzWF%2B%2FyMRi3BkfoJMeW4tCN8eeyx5A4o3pjN4Y5PaiDn45WhkSFXlSRVB6IeKpzdZOQ5Ses7RlnI7MWlv9Xp1QKTO5pQQB4Nz7h4zvR0zB3c0YGzaAse8N1lDgWh&X-Amz-Signature=160e3d6eed50731ec106de6a9d2446d0ab537c1ce8682f3be0e2bb00eaab120c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFHVIKP3%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQ1QegILICAbrQLN%2BWmmiLAX9i%2F%2FWekHqmvZlk6RIAugIgZWni7EpzIYYDtWhCpdDDEmvkBuB1VdnOim14N3FoKxsq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDH5wkMM3a6BO2XoaLCrcA3G4p5uNOlFpdPRI1y%2FtqWPkUA51sNz9iT94uHg%2BkKBEVv9m5a%2FasqkgDdBdUq34TJfpQTd19cnDuWFMX7SsWHhmbt1plAyZn9Ez4fGaE1jSXTqf%2F8ECRXeiH3zCw4aRO%2FqupMtUUUBQgZTKAE0%2Fzahsc0KKpJRgOz4a9oRSHS4Dr%2F6iCQWxeW3ON2%2B9vPUhTPlHnAdYkT6XofO4R5LOzuUMyoRYt8QdFScCZB7%2Bk1lY7tPnwI5hpQtO9BRYMsTCEuUbZo6IHtg4c3Nf8ZP7%2BKak%2Be%2B7tsObAtTndlWm8bXqPKGNlbeN3wm0zynwBsk%2BK34vchY4psV1OSF%2FhTO9zU4N7z00a7ybsmMeWTLg70UU1ViKCtPQdLa3CY96g4t86IZ5bsiHX3KxIVrBJ2FebEtCLVIZWFI6joevEoNeFyySHg9sVqhVPAKj2GxmnIRd%2FTOc%2B5NKGSUlG71UL3sXevBnBqJg1MbHf7fyLVFP%2F5%2B92ww83NO0VWQ31oI5aFWsfEBq5gHPgktL%2FNfftY1tVncIgt560syw0unqRNB%2Bn8M1SP2t%2FH%2BwJe7rEPM%2BU7s3pEyYc6HJlg3Eco1e3Is6bYzw980dIfmAzRGr2Up3EpxIVWiETBotffs0kghrMIaMyMkGOqUBZuOdAf%2F5g7kpuJKA1fmzowh8GSyTKcVZ2RSkR%2FBrHIHXWtKjs7wbI5xgLbdg14moBTLyMwSrIbo1SM3mCUevS7%2FlgcI34kkGAzWF%2B%2FyMRi3BkfoJMeW4tCN8eeyx5A4o3pjN4Y5PaiDn45WhkSFXlSRVB6IeKpzdZOQ5Ses7RlnI7MWlv9Xp1QKTO5pQQB4Nz7h4zvR0zB3c0YGzaAse8N1lDgWh&X-Amz-Signature=bd9cadae63c808d31d78a91514e5a0dd662dbbc4fce71454dcebb52b054b874b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFHVIKP3%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQ1QegILICAbrQLN%2BWmmiLAX9i%2F%2FWekHqmvZlk6RIAugIgZWni7EpzIYYDtWhCpdDDEmvkBuB1VdnOim14N3FoKxsq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDH5wkMM3a6BO2XoaLCrcA3G4p5uNOlFpdPRI1y%2FtqWPkUA51sNz9iT94uHg%2BkKBEVv9m5a%2FasqkgDdBdUq34TJfpQTd19cnDuWFMX7SsWHhmbt1plAyZn9Ez4fGaE1jSXTqf%2F8ECRXeiH3zCw4aRO%2FqupMtUUUBQgZTKAE0%2Fzahsc0KKpJRgOz4a9oRSHS4Dr%2F6iCQWxeW3ON2%2B9vPUhTPlHnAdYkT6XofO4R5LOzuUMyoRYt8QdFScCZB7%2Bk1lY7tPnwI5hpQtO9BRYMsTCEuUbZo6IHtg4c3Nf8ZP7%2BKak%2Be%2B7tsObAtTndlWm8bXqPKGNlbeN3wm0zynwBsk%2BK34vchY4psV1OSF%2FhTO9zU4N7z00a7ybsmMeWTLg70UU1ViKCtPQdLa3CY96g4t86IZ5bsiHX3KxIVrBJ2FebEtCLVIZWFI6joevEoNeFyySHg9sVqhVPAKj2GxmnIRd%2FTOc%2B5NKGSUlG71UL3sXevBnBqJg1MbHf7fyLVFP%2F5%2B92ww83NO0VWQ31oI5aFWsfEBq5gHPgktL%2FNfftY1tVncIgt560syw0unqRNB%2Bn8M1SP2t%2FH%2BwJe7rEPM%2BU7s3pEyYc6HJlg3Eco1e3Is6bYzw980dIfmAzRGr2Up3EpxIVWiETBotffs0kghrMIaMyMkGOqUBZuOdAf%2F5g7kpuJKA1fmzowh8GSyTKcVZ2RSkR%2FBrHIHXWtKjs7wbI5xgLbdg14moBTLyMwSrIbo1SM3mCUevS7%2FlgcI34kkGAzWF%2B%2FyMRi3BkfoJMeW4tCN8eeyx5A4o3pjN4Y5PaiDn45WhkSFXlSRVB6IeKpzdZOQ5Ses7RlnI7MWlv9Xp1QKTO5pQQB4Nz7h4zvR0zB3c0YGzaAse8N1lDgWh&X-Amz-Signature=4e2475212629ae621a2119d99164ff3b3c516aab4d8b789248fe7912c7712ad4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFHVIKP3%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQ1QegILICAbrQLN%2BWmmiLAX9i%2F%2FWekHqmvZlk6RIAugIgZWni7EpzIYYDtWhCpdDDEmvkBuB1VdnOim14N3FoKxsq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDH5wkMM3a6BO2XoaLCrcA3G4p5uNOlFpdPRI1y%2FtqWPkUA51sNz9iT94uHg%2BkKBEVv9m5a%2FasqkgDdBdUq34TJfpQTd19cnDuWFMX7SsWHhmbt1plAyZn9Ez4fGaE1jSXTqf%2F8ECRXeiH3zCw4aRO%2FqupMtUUUBQgZTKAE0%2Fzahsc0KKpJRgOz4a9oRSHS4Dr%2F6iCQWxeW3ON2%2B9vPUhTPlHnAdYkT6XofO4R5LOzuUMyoRYt8QdFScCZB7%2Bk1lY7tPnwI5hpQtO9BRYMsTCEuUbZo6IHtg4c3Nf8ZP7%2BKak%2Be%2B7tsObAtTndlWm8bXqPKGNlbeN3wm0zynwBsk%2BK34vchY4psV1OSF%2FhTO9zU4N7z00a7ybsmMeWTLg70UU1ViKCtPQdLa3CY96g4t86IZ5bsiHX3KxIVrBJ2FebEtCLVIZWFI6joevEoNeFyySHg9sVqhVPAKj2GxmnIRd%2FTOc%2B5NKGSUlG71UL3sXevBnBqJg1MbHf7fyLVFP%2F5%2B92ww83NO0VWQ31oI5aFWsfEBq5gHPgktL%2FNfftY1tVncIgt560syw0unqRNB%2Bn8M1SP2t%2FH%2BwJe7rEPM%2BU7s3pEyYc6HJlg3Eco1e3Is6bYzw980dIfmAzRGr2Up3EpxIVWiETBotffs0kghrMIaMyMkGOqUBZuOdAf%2F5g7kpuJKA1fmzowh8GSyTKcVZ2RSkR%2FBrHIHXWtKjs7wbI5xgLbdg14moBTLyMwSrIbo1SM3mCUevS7%2FlgcI34kkGAzWF%2B%2FyMRi3BkfoJMeW4tCN8eeyx5A4o3pjN4Y5PaiDn45WhkSFXlSRVB6IeKpzdZOQ5Ses7RlnI7MWlv9Xp1QKTO5pQQB4Nz7h4zvR0zB3c0YGzaAse8N1lDgWh&X-Amz-Signature=72f05d8e8bb37b69d1bcc5a63542856daf4b0d4767e9e9afa33c857e6fd53a81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFHVIKP3%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQ1QegILICAbrQLN%2BWmmiLAX9i%2F%2FWekHqmvZlk6RIAugIgZWni7EpzIYYDtWhCpdDDEmvkBuB1VdnOim14N3FoKxsq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDH5wkMM3a6BO2XoaLCrcA3G4p5uNOlFpdPRI1y%2FtqWPkUA51sNz9iT94uHg%2BkKBEVv9m5a%2FasqkgDdBdUq34TJfpQTd19cnDuWFMX7SsWHhmbt1plAyZn9Ez4fGaE1jSXTqf%2F8ECRXeiH3zCw4aRO%2FqupMtUUUBQgZTKAE0%2Fzahsc0KKpJRgOz4a9oRSHS4Dr%2F6iCQWxeW3ON2%2B9vPUhTPlHnAdYkT6XofO4R5LOzuUMyoRYt8QdFScCZB7%2Bk1lY7tPnwI5hpQtO9BRYMsTCEuUbZo6IHtg4c3Nf8ZP7%2BKak%2Be%2B7tsObAtTndlWm8bXqPKGNlbeN3wm0zynwBsk%2BK34vchY4psV1OSF%2FhTO9zU4N7z00a7ybsmMeWTLg70UU1ViKCtPQdLa3CY96g4t86IZ5bsiHX3KxIVrBJ2FebEtCLVIZWFI6joevEoNeFyySHg9sVqhVPAKj2GxmnIRd%2FTOc%2B5NKGSUlG71UL3sXevBnBqJg1MbHf7fyLVFP%2F5%2B92ww83NO0VWQ31oI5aFWsfEBq5gHPgktL%2FNfftY1tVncIgt560syw0unqRNB%2Bn8M1SP2t%2FH%2BwJe7rEPM%2BU7s3pEyYc6HJlg3Eco1e3Is6bYzw980dIfmAzRGr2Up3EpxIVWiETBotffs0kghrMIaMyMkGOqUBZuOdAf%2F5g7kpuJKA1fmzowh8GSyTKcVZ2RSkR%2FBrHIHXWtKjs7wbI5xgLbdg14moBTLyMwSrIbo1SM3mCUevS7%2FlgcI34kkGAzWF%2B%2FyMRi3BkfoJMeW4tCN8eeyx5A4o3pjN4Y5PaiDn45WhkSFXlSRVB6IeKpzdZOQ5Ses7RlnI7MWlv9Xp1QKTO5pQQB4Nz7h4zvR0zB3c0YGzaAse8N1lDgWh&X-Amz-Signature=acaf28d3aefcc9e1f473f8f5da51eaa6901c4eec027608597c64416a2c0da856&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

