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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3UMOPYJ%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0c2f5YZgzJzMECMh%2BSnkzgk1yjsqKk2QaravQeePBSQIhAIXcm191pqBXJhNIMpeDOPX1K2%2BnnmlxHFonJok6TG%2FPKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyn9l8eNVAykT1EPjMq3AMidm7lPn%2BmCMMSEAr3taQt2GfxXucLEQlTHmcU4gT%2Fl6k28tBAdNwJ11FzDIvRqHDvylamV4DRBR%2B%2B4bRXdxdDv69LncDxcJMcqIEPSOZU769jmquywPw%2FEshToV0kF3sZqrJsyKh%2BUu4F1yN7M8NeRXhodA2u%2Fb9PbSFwC8PBLwMRPhC0T8tDRPZx%2FIT3Icwzoactw4Cy%2Ff1NM6rCRNOFRG25ModANL0iyJ3Q3hg9bHgW1LBx%2Fmtl85dszzGafSnIn9%2BGIUNHh4fAabJAfZ4aW6oKRTCytSEeTxVwiYQ9MoetP5G3FzFWEUeimia4IU1R279puC8eYhVzbLlzOxSDz5y6JUfOihF5Y9Y4N%2FuNJ9d7JrMS6fknNGEPwnlnkK%2FeqClgIVleusXZrf5yqRdoRyfRWemS0uzJ2sx7D3Z6nzAxdy5i5D2muT3Tq0PxgNgraiNY1rGeDtIYfOUYUr8%2FEIJbu1Ntx2h2rqcHtcRX1qr%2Ft175UplL%2Fx5N%2B%2BE%2FS0%2BYvYQZMIZkh3YmoU2QyFbiZABs4bVne1hVfuBasadJ0wpGvqSsAlUvjzwViaanOSB37Pj8b4WRj09f8FwvFQYEOKahVoxW6onIqT2zzZXSxnln5knoDHCUePq8JTCjypLOBjqkAdLs1t14wosNDG0GqWyF30CVdeiB0Gu4GBArRDOPkzQE3at8SL3zLTDpyicFwLOIJNBtpazod7GenFnH0QRQ8AVgIIGAYO5pVIf%2B8pwM7BIQrbKozKR6WyUFigkAZ89nkVtPDX52Ff3aMWsnhszKd7NluJh7rs43HuigSmrb7bVxcNK8LissNjc9B0PH%2BW1AevHA7vnqzp7wAWN6UdRuJK%2FBvnPY&X-Amz-Signature=2faf606b938deaa4570ee81529a356b523ac82357c2be101665712d98cb0b162&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3UMOPYJ%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0c2f5YZgzJzMECMh%2BSnkzgk1yjsqKk2QaravQeePBSQIhAIXcm191pqBXJhNIMpeDOPX1K2%2BnnmlxHFonJok6TG%2FPKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyn9l8eNVAykT1EPjMq3AMidm7lPn%2BmCMMSEAr3taQt2GfxXucLEQlTHmcU4gT%2Fl6k28tBAdNwJ11FzDIvRqHDvylamV4DRBR%2B%2B4bRXdxdDv69LncDxcJMcqIEPSOZU769jmquywPw%2FEshToV0kF3sZqrJsyKh%2BUu4F1yN7M8NeRXhodA2u%2Fb9PbSFwC8PBLwMRPhC0T8tDRPZx%2FIT3Icwzoactw4Cy%2Ff1NM6rCRNOFRG25ModANL0iyJ3Q3hg9bHgW1LBx%2Fmtl85dszzGafSnIn9%2BGIUNHh4fAabJAfZ4aW6oKRTCytSEeTxVwiYQ9MoetP5G3FzFWEUeimia4IU1R279puC8eYhVzbLlzOxSDz5y6JUfOihF5Y9Y4N%2FuNJ9d7JrMS6fknNGEPwnlnkK%2FeqClgIVleusXZrf5yqRdoRyfRWemS0uzJ2sx7D3Z6nzAxdy5i5D2muT3Tq0PxgNgraiNY1rGeDtIYfOUYUr8%2FEIJbu1Ntx2h2rqcHtcRX1qr%2Ft175UplL%2Fx5N%2B%2BE%2FS0%2BYvYQZMIZkh3YmoU2QyFbiZABs4bVne1hVfuBasadJ0wpGvqSsAlUvjzwViaanOSB37Pj8b4WRj09f8FwvFQYEOKahVoxW6onIqT2zzZXSxnln5knoDHCUePq8JTCjypLOBjqkAdLs1t14wosNDG0GqWyF30CVdeiB0Gu4GBArRDOPkzQE3at8SL3zLTDpyicFwLOIJNBtpazod7GenFnH0QRQ8AVgIIGAYO5pVIf%2B8pwM7BIQrbKozKR6WyUFigkAZ89nkVtPDX52Ff3aMWsnhszKd7NluJh7rs43HuigSmrb7bVxcNK8LissNjc9B0PH%2BW1AevHA7vnqzp7wAWN6UdRuJK%2FBvnPY&X-Amz-Signature=829c37fbade98144ef742ce92eee4aa5d37b3e3913a1dd36d989eec3a377ca3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3UMOPYJ%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0c2f5YZgzJzMECMh%2BSnkzgk1yjsqKk2QaravQeePBSQIhAIXcm191pqBXJhNIMpeDOPX1K2%2BnnmlxHFonJok6TG%2FPKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyn9l8eNVAykT1EPjMq3AMidm7lPn%2BmCMMSEAr3taQt2GfxXucLEQlTHmcU4gT%2Fl6k28tBAdNwJ11FzDIvRqHDvylamV4DRBR%2B%2B4bRXdxdDv69LncDxcJMcqIEPSOZU769jmquywPw%2FEshToV0kF3sZqrJsyKh%2BUu4F1yN7M8NeRXhodA2u%2Fb9PbSFwC8PBLwMRPhC0T8tDRPZx%2FIT3Icwzoactw4Cy%2Ff1NM6rCRNOFRG25ModANL0iyJ3Q3hg9bHgW1LBx%2Fmtl85dszzGafSnIn9%2BGIUNHh4fAabJAfZ4aW6oKRTCytSEeTxVwiYQ9MoetP5G3FzFWEUeimia4IU1R279puC8eYhVzbLlzOxSDz5y6JUfOihF5Y9Y4N%2FuNJ9d7JrMS6fknNGEPwnlnkK%2FeqClgIVleusXZrf5yqRdoRyfRWemS0uzJ2sx7D3Z6nzAxdy5i5D2muT3Tq0PxgNgraiNY1rGeDtIYfOUYUr8%2FEIJbu1Ntx2h2rqcHtcRX1qr%2Ft175UplL%2Fx5N%2B%2BE%2FS0%2BYvYQZMIZkh3YmoU2QyFbiZABs4bVne1hVfuBasadJ0wpGvqSsAlUvjzwViaanOSB37Pj8b4WRj09f8FwvFQYEOKahVoxW6onIqT2zzZXSxnln5knoDHCUePq8JTCjypLOBjqkAdLs1t14wosNDG0GqWyF30CVdeiB0Gu4GBArRDOPkzQE3at8SL3zLTDpyicFwLOIJNBtpazod7GenFnH0QRQ8AVgIIGAYO5pVIf%2B8pwM7BIQrbKozKR6WyUFigkAZ89nkVtPDX52Ff3aMWsnhszKd7NluJh7rs43HuigSmrb7bVxcNK8LissNjc9B0PH%2BW1AevHA7vnqzp7wAWN6UdRuJK%2FBvnPY&X-Amz-Signature=75c775dca3ec14a16ed7c049952df1383720a9bd0be1b00e9d05864e13bf29ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3UMOPYJ%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0c2f5YZgzJzMECMh%2BSnkzgk1yjsqKk2QaravQeePBSQIhAIXcm191pqBXJhNIMpeDOPX1K2%2BnnmlxHFonJok6TG%2FPKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyn9l8eNVAykT1EPjMq3AMidm7lPn%2BmCMMSEAr3taQt2GfxXucLEQlTHmcU4gT%2Fl6k28tBAdNwJ11FzDIvRqHDvylamV4DRBR%2B%2B4bRXdxdDv69LncDxcJMcqIEPSOZU769jmquywPw%2FEshToV0kF3sZqrJsyKh%2BUu4F1yN7M8NeRXhodA2u%2Fb9PbSFwC8PBLwMRPhC0T8tDRPZx%2FIT3Icwzoactw4Cy%2Ff1NM6rCRNOFRG25ModANL0iyJ3Q3hg9bHgW1LBx%2Fmtl85dszzGafSnIn9%2BGIUNHh4fAabJAfZ4aW6oKRTCytSEeTxVwiYQ9MoetP5G3FzFWEUeimia4IU1R279puC8eYhVzbLlzOxSDz5y6JUfOihF5Y9Y4N%2FuNJ9d7JrMS6fknNGEPwnlnkK%2FeqClgIVleusXZrf5yqRdoRyfRWemS0uzJ2sx7D3Z6nzAxdy5i5D2muT3Tq0PxgNgraiNY1rGeDtIYfOUYUr8%2FEIJbu1Ntx2h2rqcHtcRX1qr%2Ft175UplL%2Fx5N%2B%2BE%2FS0%2BYvYQZMIZkh3YmoU2QyFbiZABs4bVne1hVfuBasadJ0wpGvqSsAlUvjzwViaanOSB37Pj8b4WRj09f8FwvFQYEOKahVoxW6onIqT2zzZXSxnln5knoDHCUePq8JTCjypLOBjqkAdLs1t14wosNDG0GqWyF30CVdeiB0Gu4GBArRDOPkzQE3at8SL3zLTDpyicFwLOIJNBtpazod7GenFnH0QRQ8AVgIIGAYO5pVIf%2B8pwM7BIQrbKozKR6WyUFigkAZ89nkVtPDX52Ff3aMWsnhszKd7NluJh7rs43HuigSmrb7bVxcNK8LissNjc9B0PH%2BW1AevHA7vnqzp7wAWN6UdRuJK%2FBvnPY&X-Amz-Signature=290435e098372cbdb961c648b0517b2f3fd0b4593eae8d6b4ae4499c8aad0039&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3UMOPYJ%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0c2f5YZgzJzMECMh%2BSnkzgk1yjsqKk2QaravQeePBSQIhAIXcm191pqBXJhNIMpeDOPX1K2%2BnnmlxHFonJok6TG%2FPKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyn9l8eNVAykT1EPjMq3AMidm7lPn%2BmCMMSEAr3taQt2GfxXucLEQlTHmcU4gT%2Fl6k28tBAdNwJ11FzDIvRqHDvylamV4DRBR%2B%2B4bRXdxdDv69LncDxcJMcqIEPSOZU769jmquywPw%2FEshToV0kF3sZqrJsyKh%2BUu4F1yN7M8NeRXhodA2u%2Fb9PbSFwC8PBLwMRPhC0T8tDRPZx%2FIT3Icwzoactw4Cy%2Ff1NM6rCRNOFRG25ModANL0iyJ3Q3hg9bHgW1LBx%2Fmtl85dszzGafSnIn9%2BGIUNHh4fAabJAfZ4aW6oKRTCytSEeTxVwiYQ9MoetP5G3FzFWEUeimia4IU1R279puC8eYhVzbLlzOxSDz5y6JUfOihF5Y9Y4N%2FuNJ9d7JrMS6fknNGEPwnlnkK%2FeqClgIVleusXZrf5yqRdoRyfRWemS0uzJ2sx7D3Z6nzAxdy5i5D2muT3Tq0PxgNgraiNY1rGeDtIYfOUYUr8%2FEIJbu1Ntx2h2rqcHtcRX1qr%2Ft175UplL%2Fx5N%2B%2BE%2FS0%2BYvYQZMIZkh3YmoU2QyFbiZABs4bVne1hVfuBasadJ0wpGvqSsAlUvjzwViaanOSB37Pj8b4WRj09f8FwvFQYEOKahVoxW6onIqT2zzZXSxnln5knoDHCUePq8JTCjypLOBjqkAdLs1t14wosNDG0GqWyF30CVdeiB0Gu4GBArRDOPkzQE3at8SL3zLTDpyicFwLOIJNBtpazod7GenFnH0QRQ8AVgIIGAYO5pVIf%2B8pwM7BIQrbKozKR6WyUFigkAZ89nkVtPDX52Ff3aMWsnhszKd7NluJh7rs43HuigSmrb7bVxcNK8LissNjc9B0PH%2BW1AevHA7vnqzp7wAWN6UdRuJK%2FBvnPY&X-Amz-Signature=2fdcd83cd74371fe5d3087308d4ba6a500cb9ab42e4de408bd896675cf68c470&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3UMOPYJ%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0c2f5YZgzJzMECMh%2BSnkzgk1yjsqKk2QaravQeePBSQIhAIXcm191pqBXJhNIMpeDOPX1K2%2BnnmlxHFonJok6TG%2FPKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyn9l8eNVAykT1EPjMq3AMidm7lPn%2BmCMMSEAr3taQt2GfxXucLEQlTHmcU4gT%2Fl6k28tBAdNwJ11FzDIvRqHDvylamV4DRBR%2B%2B4bRXdxdDv69LncDxcJMcqIEPSOZU769jmquywPw%2FEshToV0kF3sZqrJsyKh%2BUu4F1yN7M8NeRXhodA2u%2Fb9PbSFwC8PBLwMRPhC0T8tDRPZx%2FIT3Icwzoactw4Cy%2Ff1NM6rCRNOFRG25ModANL0iyJ3Q3hg9bHgW1LBx%2Fmtl85dszzGafSnIn9%2BGIUNHh4fAabJAfZ4aW6oKRTCytSEeTxVwiYQ9MoetP5G3FzFWEUeimia4IU1R279puC8eYhVzbLlzOxSDz5y6JUfOihF5Y9Y4N%2FuNJ9d7JrMS6fknNGEPwnlnkK%2FeqClgIVleusXZrf5yqRdoRyfRWemS0uzJ2sx7D3Z6nzAxdy5i5D2muT3Tq0PxgNgraiNY1rGeDtIYfOUYUr8%2FEIJbu1Ntx2h2rqcHtcRX1qr%2Ft175UplL%2Fx5N%2B%2BE%2FS0%2BYvYQZMIZkh3YmoU2QyFbiZABs4bVne1hVfuBasadJ0wpGvqSsAlUvjzwViaanOSB37Pj8b4WRj09f8FwvFQYEOKahVoxW6onIqT2zzZXSxnln5knoDHCUePq8JTCjypLOBjqkAdLs1t14wosNDG0GqWyF30CVdeiB0Gu4GBArRDOPkzQE3at8SL3zLTDpyicFwLOIJNBtpazod7GenFnH0QRQ8AVgIIGAYO5pVIf%2B8pwM7BIQrbKozKR6WyUFigkAZ89nkVtPDX52Ff3aMWsnhszKd7NluJh7rs43HuigSmrb7bVxcNK8LissNjc9B0PH%2BW1AevHA7vnqzp7wAWN6UdRuJK%2FBvnPY&X-Amz-Signature=c35a503f74daa8e1042899ba1ca45e4bf8a55939c2c1c9421829c6d2955da813&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3UMOPYJ%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0c2f5YZgzJzMECMh%2BSnkzgk1yjsqKk2QaravQeePBSQIhAIXcm191pqBXJhNIMpeDOPX1K2%2BnnmlxHFonJok6TG%2FPKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyn9l8eNVAykT1EPjMq3AMidm7lPn%2BmCMMSEAr3taQt2GfxXucLEQlTHmcU4gT%2Fl6k28tBAdNwJ11FzDIvRqHDvylamV4DRBR%2B%2B4bRXdxdDv69LncDxcJMcqIEPSOZU769jmquywPw%2FEshToV0kF3sZqrJsyKh%2BUu4F1yN7M8NeRXhodA2u%2Fb9PbSFwC8PBLwMRPhC0T8tDRPZx%2FIT3Icwzoactw4Cy%2Ff1NM6rCRNOFRG25ModANL0iyJ3Q3hg9bHgW1LBx%2Fmtl85dszzGafSnIn9%2BGIUNHh4fAabJAfZ4aW6oKRTCytSEeTxVwiYQ9MoetP5G3FzFWEUeimia4IU1R279puC8eYhVzbLlzOxSDz5y6JUfOihF5Y9Y4N%2FuNJ9d7JrMS6fknNGEPwnlnkK%2FeqClgIVleusXZrf5yqRdoRyfRWemS0uzJ2sx7D3Z6nzAxdy5i5D2muT3Tq0PxgNgraiNY1rGeDtIYfOUYUr8%2FEIJbu1Ntx2h2rqcHtcRX1qr%2Ft175UplL%2Fx5N%2B%2BE%2FS0%2BYvYQZMIZkh3YmoU2QyFbiZABs4bVne1hVfuBasadJ0wpGvqSsAlUvjzwViaanOSB37Pj8b4WRj09f8FwvFQYEOKahVoxW6onIqT2zzZXSxnln5knoDHCUePq8JTCjypLOBjqkAdLs1t14wosNDG0GqWyF30CVdeiB0Gu4GBArRDOPkzQE3at8SL3zLTDpyicFwLOIJNBtpazod7GenFnH0QRQ8AVgIIGAYO5pVIf%2B8pwM7BIQrbKozKR6WyUFigkAZ89nkVtPDX52Ff3aMWsnhszKd7NluJh7rs43HuigSmrb7bVxcNK8LissNjc9B0PH%2BW1AevHA7vnqzp7wAWN6UdRuJK%2FBvnPY&X-Amz-Signature=2aa23288d6234190ee6f194d442b544f12137d90c06c1fb4c6cf803148209cd3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

