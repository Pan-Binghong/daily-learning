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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXL5SLXD%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvLNd%2FzZ6GAUO3J1d8C3xFVpjESTp6g2tZ%2F6RV0F%2BapwIgB%2FswTbqpaU9umh%2F0dSxPdtYURc5oxLPpEZJATQ6iMVoqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO5nfgUJPKZOosTiGSrcAw31zgDu2zM3%2B03LeYsdAvuXDj9S2qTg%2B%2BAZagkxmOZXZV4q71ZL2bafZC4nITA1VMNR6LaCzY3H0R8tRE9PKFljbTDHcjmRuda2qTdRaKphf0%2F%2FbCPIVWhHgSkTDpAhfu8iF6B4ZP715hGkOZ9A4nTSfsZTXlMuV88YZ6fEpAdZ0q%2B305KMOWAVFdW1FQngPP1euLbbSGwEsm1t2XvIe26Hy2rj68MP9vcfdse%2BMDFBpXoxGu%2FHvbThN8j6FGvXJNlfjOOELFG3MdD1avb4vf6Z2PVxGuphh4A66vwfwLbh%2Bw01UWj9VoVGz2To9vjDT6AcV5dHo2inF4GW5tLjHFrLjljymPoNqHkvTda3gDSTsmDTwtdvL2PIcBnNSsyzhGEldVFpW7HZYKHnr389dQrxKaUT2ox0uclER6SoGDSIIz%2Bvmbf50rgN8BeCSoxiVqpqodHkC%2BTqoJ%2B4g7TsYtXdwWwSzaoUVjpw1Uh%2BprO68neBB4FRZEo8lHDuTefwz4R9LvesEjW1eyzZjsplsJ03%2BLnG53F3eO%2FFpy8JlXGq%2FCeB3yPAA4V%2BuZNVbYibIUKMlWg0LaMWe37OWL5ArXc0AOQimm2BmnkUuIWVci8evQ1h3WGHLak8M5WdMOPWjs4GOqUBm1iwn7ZtGg8B%2BKF6KLVaZpsWLBJWxk8BGpokweBMwTcNXdCnEc5%2BsyTs%2FZA2kk8QsBGaCP4Zkb2MeS3w0x80uaEJMUNjYTwMb8IZC3RtAZLJTBDmWP%2BPeAmQ7pTWlU39pxQZC1MCQYd43X7QvsxIdqk9quO2%2Bykl%2Fg5V37Kt3KyDYuFnAi%2BUJthiArRz83aZuN3nGZybH2RPs6N78o3Tgyoqf09i&X-Amz-Signature=9d7c76f9cebbf17e83f9974a8b21f5385627f4c372636e459964cada50541dff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXL5SLXD%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvLNd%2FzZ6GAUO3J1d8C3xFVpjESTp6g2tZ%2F6RV0F%2BapwIgB%2FswTbqpaU9umh%2F0dSxPdtYURc5oxLPpEZJATQ6iMVoqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO5nfgUJPKZOosTiGSrcAw31zgDu2zM3%2B03LeYsdAvuXDj9S2qTg%2B%2BAZagkxmOZXZV4q71ZL2bafZC4nITA1VMNR6LaCzY3H0R8tRE9PKFljbTDHcjmRuda2qTdRaKphf0%2F%2FbCPIVWhHgSkTDpAhfu8iF6B4ZP715hGkOZ9A4nTSfsZTXlMuV88YZ6fEpAdZ0q%2B305KMOWAVFdW1FQngPP1euLbbSGwEsm1t2XvIe26Hy2rj68MP9vcfdse%2BMDFBpXoxGu%2FHvbThN8j6FGvXJNlfjOOELFG3MdD1avb4vf6Z2PVxGuphh4A66vwfwLbh%2Bw01UWj9VoVGz2To9vjDT6AcV5dHo2inF4GW5tLjHFrLjljymPoNqHkvTda3gDSTsmDTwtdvL2PIcBnNSsyzhGEldVFpW7HZYKHnr389dQrxKaUT2ox0uclER6SoGDSIIz%2Bvmbf50rgN8BeCSoxiVqpqodHkC%2BTqoJ%2B4g7TsYtXdwWwSzaoUVjpw1Uh%2BprO68neBB4FRZEo8lHDuTefwz4R9LvesEjW1eyzZjsplsJ03%2BLnG53F3eO%2FFpy8JlXGq%2FCeB3yPAA4V%2BuZNVbYibIUKMlWg0LaMWe37OWL5ArXc0AOQimm2BmnkUuIWVci8evQ1h3WGHLak8M5WdMOPWjs4GOqUBm1iwn7ZtGg8B%2BKF6KLVaZpsWLBJWxk8BGpokweBMwTcNXdCnEc5%2BsyTs%2FZA2kk8QsBGaCP4Zkb2MeS3w0x80uaEJMUNjYTwMb8IZC3RtAZLJTBDmWP%2BPeAmQ7pTWlU39pxQZC1MCQYd43X7QvsxIdqk9quO2%2Bykl%2Fg5V37Kt3KyDYuFnAi%2BUJthiArRz83aZuN3nGZybH2RPs6N78o3Tgyoqf09i&X-Amz-Signature=e9a0cf78508d8d81423f42746848fd3b5c9c140878cb31893b2c321602ad26dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXL5SLXD%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvLNd%2FzZ6GAUO3J1d8C3xFVpjESTp6g2tZ%2F6RV0F%2BapwIgB%2FswTbqpaU9umh%2F0dSxPdtYURc5oxLPpEZJATQ6iMVoqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO5nfgUJPKZOosTiGSrcAw31zgDu2zM3%2B03LeYsdAvuXDj9S2qTg%2B%2BAZagkxmOZXZV4q71ZL2bafZC4nITA1VMNR6LaCzY3H0R8tRE9PKFljbTDHcjmRuda2qTdRaKphf0%2F%2FbCPIVWhHgSkTDpAhfu8iF6B4ZP715hGkOZ9A4nTSfsZTXlMuV88YZ6fEpAdZ0q%2B305KMOWAVFdW1FQngPP1euLbbSGwEsm1t2XvIe26Hy2rj68MP9vcfdse%2BMDFBpXoxGu%2FHvbThN8j6FGvXJNlfjOOELFG3MdD1avb4vf6Z2PVxGuphh4A66vwfwLbh%2Bw01UWj9VoVGz2To9vjDT6AcV5dHo2inF4GW5tLjHFrLjljymPoNqHkvTda3gDSTsmDTwtdvL2PIcBnNSsyzhGEldVFpW7HZYKHnr389dQrxKaUT2ox0uclER6SoGDSIIz%2Bvmbf50rgN8BeCSoxiVqpqodHkC%2BTqoJ%2B4g7TsYtXdwWwSzaoUVjpw1Uh%2BprO68neBB4FRZEo8lHDuTefwz4R9LvesEjW1eyzZjsplsJ03%2BLnG53F3eO%2FFpy8JlXGq%2FCeB3yPAA4V%2BuZNVbYibIUKMlWg0LaMWe37OWL5ArXc0AOQimm2BmnkUuIWVci8evQ1h3WGHLak8M5WdMOPWjs4GOqUBm1iwn7ZtGg8B%2BKF6KLVaZpsWLBJWxk8BGpokweBMwTcNXdCnEc5%2BsyTs%2FZA2kk8QsBGaCP4Zkb2MeS3w0x80uaEJMUNjYTwMb8IZC3RtAZLJTBDmWP%2BPeAmQ7pTWlU39pxQZC1MCQYd43X7QvsxIdqk9quO2%2Bykl%2Fg5V37Kt3KyDYuFnAi%2BUJthiArRz83aZuN3nGZybH2RPs6N78o3Tgyoqf09i&X-Amz-Signature=b4c6cadd803fa694d75f6ad46c3141eec0c6f8a441f06a5365cb55a3d5bd3dca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXL5SLXD%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvLNd%2FzZ6GAUO3J1d8C3xFVpjESTp6g2tZ%2F6RV0F%2BapwIgB%2FswTbqpaU9umh%2F0dSxPdtYURc5oxLPpEZJATQ6iMVoqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO5nfgUJPKZOosTiGSrcAw31zgDu2zM3%2B03LeYsdAvuXDj9S2qTg%2B%2BAZagkxmOZXZV4q71ZL2bafZC4nITA1VMNR6LaCzY3H0R8tRE9PKFljbTDHcjmRuda2qTdRaKphf0%2F%2FbCPIVWhHgSkTDpAhfu8iF6B4ZP715hGkOZ9A4nTSfsZTXlMuV88YZ6fEpAdZ0q%2B305KMOWAVFdW1FQngPP1euLbbSGwEsm1t2XvIe26Hy2rj68MP9vcfdse%2BMDFBpXoxGu%2FHvbThN8j6FGvXJNlfjOOELFG3MdD1avb4vf6Z2PVxGuphh4A66vwfwLbh%2Bw01UWj9VoVGz2To9vjDT6AcV5dHo2inF4GW5tLjHFrLjljymPoNqHkvTda3gDSTsmDTwtdvL2PIcBnNSsyzhGEldVFpW7HZYKHnr389dQrxKaUT2ox0uclER6SoGDSIIz%2Bvmbf50rgN8BeCSoxiVqpqodHkC%2BTqoJ%2B4g7TsYtXdwWwSzaoUVjpw1Uh%2BprO68neBB4FRZEo8lHDuTefwz4R9LvesEjW1eyzZjsplsJ03%2BLnG53F3eO%2FFpy8JlXGq%2FCeB3yPAA4V%2BuZNVbYibIUKMlWg0LaMWe37OWL5ArXc0AOQimm2BmnkUuIWVci8evQ1h3WGHLak8M5WdMOPWjs4GOqUBm1iwn7ZtGg8B%2BKF6KLVaZpsWLBJWxk8BGpokweBMwTcNXdCnEc5%2BsyTs%2FZA2kk8QsBGaCP4Zkb2MeS3w0x80uaEJMUNjYTwMb8IZC3RtAZLJTBDmWP%2BPeAmQ7pTWlU39pxQZC1MCQYd43X7QvsxIdqk9quO2%2Bykl%2Fg5V37Kt3KyDYuFnAi%2BUJthiArRz83aZuN3nGZybH2RPs6N78o3Tgyoqf09i&X-Amz-Signature=abf8abdacbfd15c1ded541b3f7340cd6fac7a5ef7d22d2387ebf003324890b97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXL5SLXD%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvLNd%2FzZ6GAUO3J1d8C3xFVpjESTp6g2tZ%2F6RV0F%2BapwIgB%2FswTbqpaU9umh%2F0dSxPdtYURc5oxLPpEZJATQ6iMVoqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO5nfgUJPKZOosTiGSrcAw31zgDu2zM3%2B03LeYsdAvuXDj9S2qTg%2B%2BAZagkxmOZXZV4q71ZL2bafZC4nITA1VMNR6LaCzY3H0R8tRE9PKFljbTDHcjmRuda2qTdRaKphf0%2F%2FbCPIVWhHgSkTDpAhfu8iF6B4ZP715hGkOZ9A4nTSfsZTXlMuV88YZ6fEpAdZ0q%2B305KMOWAVFdW1FQngPP1euLbbSGwEsm1t2XvIe26Hy2rj68MP9vcfdse%2BMDFBpXoxGu%2FHvbThN8j6FGvXJNlfjOOELFG3MdD1avb4vf6Z2PVxGuphh4A66vwfwLbh%2Bw01UWj9VoVGz2To9vjDT6AcV5dHo2inF4GW5tLjHFrLjljymPoNqHkvTda3gDSTsmDTwtdvL2PIcBnNSsyzhGEldVFpW7HZYKHnr389dQrxKaUT2ox0uclER6SoGDSIIz%2Bvmbf50rgN8BeCSoxiVqpqodHkC%2BTqoJ%2B4g7TsYtXdwWwSzaoUVjpw1Uh%2BprO68neBB4FRZEo8lHDuTefwz4R9LvesEjW1eyzZjsplsJ03%2BLnG53F3eO%2FFpy8JlXGq%2FCeB3yPAA4V%2BuZNVbYibIUKMlWg0LaMWe37OWL5ArXc0AOQimm2BmnkUuIWVci8evQ1h3WGHLak8M5WdMOPWjs4GOqUBm1iwn7ZtGg8B%2BKF6KLVaZpsWLBJWxk8BGpokweBMwTcNXdCnEc5%2BsyTs%2FZA2kk8QsBGaCP4Zkb2MeS3w0x80uaEJMUNjYTwMb8IZC3RtAZLJTBDmWP%2BPeAmQ7pTWlU39pxQZC1MCQYd43X7QvsxIdqk9quO2%2Bykl%2Fg5V37Kt3KyDYuFnAi%2BUJthiArRz83aZuN3nGZybH2RPs6N78o3Tgyoqf09i&X-Amz-Signature=1d563358ebab515d0e71bd0d1c62533cdbaf29279ad99e2ff413bb08381c0e4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXL5SLXD%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvLNd%2FzZ6GAUO3J1d8C3xFVpjESTp6g2tZ%2F6RV0F%2BapwIgB%2FswTbqpaU9umh%2F0dSxPdtYURc5oxLPpEZJATQ6iMVoqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO5nfgUJPKZOosTiGSrcAw31zgDu2zM3%2B03LeYsdAvuXDj9S2qTg%2B%2BAZagkxmOZXZV4q71ZL2bafZC4nITA1VMNR6LaCzY3H0R8tRE9PKFljbTDHcjmRuda2qTdRaKphf0%2F%2FbCPIVWhHgSkTDpAhfu8iF6B4ZP715hGkOZ9A4nTSfsZTXlMuV88YZ6fEpAdZ0q%2B305KMOWAVFdW1FQngPP1euLbbSGwEsm1t2XvIe26Hy2rj68MP9vcfdse%2BMDFBpXoxGu%2FHvbThN8j6FGvXJNlfjOOELFG3MdD1avb4vf6Z2PVxGuphh4A66vwfwLbh%2Bw01UWj9VoVGz2To9vjDT6AcV5dHo2inF4GW5tLjHFrLjljymPoNqHkvTda3gDSTsmDTwtdvL2PIcBnNSsyzhGEldVFpW7HZYKHnr389dQrxKaUT2ox0uclER6SoGDSIIz%2Bvmbf50rgN8BeCSoxiVqpqodHkC%2BTqoJ%2B4g7TsYtXdwWwSzaoUVjpw1Uh%2BprO68neBB4FRZEo8lHDuTefwz4R9LvesEjW1eyzZjsplsJ03%2BLnG53F3eO%2FFpy8JlXGq%2FCeB3yPAA4V%2BuZNVbYibIUKMlWg0LaMWe37OWL5ArXc0AOQimm2BmnkUuIWVci8evQ1h3WGHLak8M5WdMOPWjs4GOqUBm1iwn7ZtGg8B%2BKF6KLVaZpsWLBJWxk8BGpokweBMwTcNXdCnEc5%2BsyTs%2FZA2kk8QsBGaCP4Zkb2MeS3w0x80uaEJMUNjYTwMb8IZC3RtAZLJTBDmWP%2BPeAmQ7pTWlU39pxQZC1MCQYd43X7QvsxIdqk9quO2%2Bykl%2Fg5V37Kt3KyDYuFnAi%2BUJthiArRz83aZuN3nGZybH2RPs6N78o3Tgyoqf09i&X-Amz-Signature=640c8010b29929e8019a6d8d4a3788ca9bc54bfd37dd0ee826681b3bc8a25691&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXL5SLXD%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvLNd%2FzZ6GAUO3J1d8C3xFVpjESTp6g2tZ%2F6RV0F%2BapwIgB%2FswTbqpaU9umh%2F0dSxPdtYURc5oxLPpEZJATQ6iMVoqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO5nfgUJPKZOosTiGSrcAw31zgDu2zM3%2B03LeYsdAvuXDj9S2qTg%2B%2BAZagkxmOZXZV4q71ZL2bafZC4nITA1VMNR6LaCzY3H0R8tRE9PKFljbTDHcjmRuda2qTdRaKphf0%2F%2FbCPIVWhHgSkTDpAhfu8iF6B4ZP715hGkOZ9A4nTSfsZTXlMuV88YZ6fEpAdZ0q%2B305KMOWAVFdW1FQngPP1euLbbSGwEsm1t2XvIe26Hy2rj68MP9vcfdse%2BMDFBpXoxGu%2FHvbThN8j6FGvXJNlfjOOELFG3MdD1avb4vf6Z2PVxGuphh4A66vwfwLbh%2Bw01UWj9VoVGz2To9vjDT6AcV5dHo2inF4GW5tLjHFrLjljymPoNqHkvTda3gDSTsmDTwtdvL2PIcBnNSsyzhGEldVFpW7HZYKHnr389dQrxKaUT2ox0uclER6SoGDSIIz%2Bvmbf50rgN8BeCSoxiVqpqodHkC%2BTqoJ%2B4g7TsYtXdwWwSzaoUVjpw1Uh%2BprO68neBB4FRZEo8lHDuTefwz4R9LvesEjW1eyzZjsplsJ03%2BLnG53F3eO%2FFpy8JlXGq%2FCeB3yPAA4V%2BuZNVbYibIUKMlWg0LaMWe37OWL5ArXc0AOQimm2BmnkUuIWVci8evQ1h3WGHLak8M5WdMOPWjs4GOqUBm1iwn7ZtGg8B%2BKF6KLVaZpsWLBJWxk8BGpokweBMwTcNXdCnEc5%2BsyTs%2FZA2kk8QsBGaCP4Zkb2MeS3w0x80uaEJMUNjYTwMb8IZC3RtAZLJTBDmWP%2BPeAmQ7pTWlU39pxQZC1MCQYd43X7QvsxIdqk9quO2%2Bykl%2Fg5V37Kt3KyDYuFnAi%2BUJthiArRz83aZuN3nGZybH2RPs6N78o3Tgyoqf09i&X-Amz-Signature=a01e54f2be802eb5cc231dc8d92d048d7a48c2c7f9bfc290a69206f5fe166375&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

