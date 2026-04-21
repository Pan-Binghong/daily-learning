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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X4Q2YTQ%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQC%2B%2FOQ5rTLrYnzepyVhkyvzFjP4G4K9YKusfFyO2LF9oQIgfk%2FdoM6oUF7UxesOfL0GqkQJk4vf7Z29sM8XEqMkidYq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDNT2OLeZM1zfrIkh6yrcA0%2FjZpfavGaCZBDHXEya6a23WCESbURdHOtxVstVjbQSeAoDdxuuwEWirlzOoDfkqbct7f7SG1sV8u%2BlWhHr%2FoQfdFAN5chGj6nETW6L3%2Firdc%2B1GL61wZkMXv9bzZ0gpeZ8jCKDqN5I%2B91SbVo6WbZe0cWKO8SORhESGKPrLsr%2FkMz%2B%2FER5nsojq6bT2S%2FQs%2FdXbZNzwDL%2B5%2BfMKwaVWUjJ%2BaVcKxuqgxaieHC0atdZYKKt7kO4RfDvqyxFZ0B%2FuxlCMGd6Xwktu9dNTUVVwO%2B%2B7f%2B%2BN0CS581tm5gpeyZi4pzeIxCuAxAEENRuMHkzBUFEJRBzXZqD3HVdiBMbSaidqgSP%2FJOnoFXbALbhOOYFRWM7lSfdTWml37yLJhKIA1zhv61N5dfk2Okflz%2F8HeUMcqKKHulgv47dOCBlKr9PkyzkLalRueIbxWcc%2F8UyJn6%2Fkr%2BS%2Baf1CTCaVK2ZiKWbYOUUGiLmGKrcnyeNN4cxJveSuFPy4GbRjlP3HBgVqoEKSmqluwaiq8i2WACwW8eJaoGEL84Y0Il4Uh%2Fzye3zA0cf9EUUte4rkder6%2By6KxjUb9lHzZCqIHcjrntqOkYIvFkA%2FSfuz8n1lfD84cfyj2bAERxXYupMWrCQMOfUm88GOqUB%2F9LPyKuACKB0ivu5bF4N3ewkKj2dogGBqxu%2FOCfTBQLMS8cW2gwHWolEsoXNc34vpFccTEGlue4PTOul1%2B%2FDL5klkPKquLcEVMlJgsxwGKyFjw5ewKwEh8uJQS0uR%2BgfhXlFmx3tFzoC4FAfVH5T12HybMfAfes%2Bl4gEYDChnPm6kaSL%2BH696qnM013AHuRcjDcfkuz38yzIHn1yaQw5LPh%2FBnBS&X-Amz-Signature=7d3accc773ff05933f408afea25abd6327cacdd32e2285408b5ef2a70e8d08fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X4Q2YTQ%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQC%2B%2FOQ5rTLrYnzepyVhkyvzFjP4G4K9YKusfFyO2LF9oQIgfk%2FdoM6oUF7UxesOfL0GqkQJk4vf7Z29sM8XEqMkidYq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDNT2OLeZM1zfrIkh6yrcA0%2FjZpfavGaCZBDHXEya6a23WCESbURdHOtxVstVjbQSeAoDdxuuwEWirlzOoDfkqbct7f7SG1sV8u%2BlWhHr%2FoQfdFAN5chGj6nETW6L3%2Firdc%2B1GL61wZkMXv9bzZ0gpeZ8jCKDqN5I%2B91SbVo6WbZe0cWKO8SORhESGKPrLsr%2FkMz%2B%2FER5nsojq6bT2S%2FQs%2FdXbZNzwDL%2B5%2BfMKwaVWUjJ%2BaVcKxuqgxaieHC0atdZYKKt7kO4RfDvqyxFZ0B%2FuxlCMGd6Xwktu9dNTUVVwO%2B%2B7f%2B%2BN0CS581tm5gpeyZi4pzeIxCuAxAEENRuMHkzBUFEJRBzXZqD3HVdiBMbSaidqgSP%2FJOnoFXbALbhOOYFRWM7lSfdTWml37yLJhKIA1zhv61N5dfk2Okflz%2F8HeUMcqKKHulgv47dOCBlKr9PkyzkLalRueIbxWcc%2F8UyJn6%2Fkr%2BS%2Baf1CTCaVK2ZiKWbYOUUGiLmGKrcnyeNN4cxJveSuFPy4GbRjlP3HBgVqoEKSmqluwaiq8i2WACwW8eJaoGEL84Y0Il4Uh%2Fzye3zA0cf9EUUte4rkder6%2By6KxjUb9lHzZCqIHcjrntqOkYIvFkA%2FSfuz8n1lfD84cfyj2bAERxXYupMWrCQMOfUm88GOqUB%2F9LPyKuACKB0ivu5bF4N3ewkKj2dogGBqxu%2FOCfTBQLMS8cW2gwHWolEsoXNc34vpFccTEGlue4PTOul1%2B%2FDL5klkPKquLcEVMlJgsxwGKyFjw5ewKwEh8uJQS0uR%2BgfhXlFmx3tFzoC4FAfVH5T12HybMfAfes%2Bl4gEYDChnPm6kaSL%2BH696qnM013AHuRcjDcfkuz38yzIHn1yaQw5LPh%2FBnBS&X-Amz-Signature=04a44efebc66c55869b9eb0a99aa615e69392dc72f3786c032d5c8861963313f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X4Q2YTQ%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQC%2B%2FOQ5rTLrYnzepyVhkyvzFjP4G4K9YKusfFyO2LF9oQIgfk%2FdoM6oUF7UxesOfL0GqkQJk4vf7Z29sM8XEqMkidYq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDNT2OLeZM1zfrIkh6yrcA0%2FjZpfavGaCZBDHXEya6a23WCESbURdHOtxVstVjbQSeAoDdxuuwEWirlzOoDfkqbct7f7SG1sV8u%2BlWhHr%2FoQfdFAN5chGj6nETW6L3%2Firdc%2B1GL61wZkMXv9bzZ0gpeZ8jCKDqN5I%2B91SbVo6WbZe0cWKO8SORhESGKPrLsr%2FkMz%2B%2FER5nsojq6bT2S%2FQs%2FdXbZNzwDL%2B5%2BfMKwaVWUjJ%2BaVcKxuqgxaieHC0atdZYKKt7kO4RfDvqyxFZ0B%2FuxlCMGd6Xwktu9dNTUVVwO%2B%2B7f%2B%2BN0CS581tm5gpeyZi4pzeIxCuAxAEENRuMHkzBUFEJRBzXZqD3HVdiBMbSaidqgSP%2FJOnoFXbALbhOOYFRWM7lSfdTWml37yLJhKIA1zhv61N5dfk2Okflz%2F8HeUMcqKKHulgv47dOCBlKr9PkyzkLalRueIbxWcc%2F8UyJn6%2Fkr%2BS%2Baf1CTCaVK2ZiKWbYOUUGiLmGKrcnyeNN4cxJveSuFPy4GbRjlP3HBgVqoEKSmqluwaiq8i2WACwW8eJaoGEL84Y0Il4Uh%2Fzye3zA0cf9EUUte4rkder6%2By6KxjUb9lHzZCqIHcjrntqOkYIvFkA%2FSfuz8n1lfD84cfyj2bAERxXYupMWrCQMOfUm88GOqUB%2F9LPyKuACKB0ivu5bF4N3ewkKj2dogGBqxu%2FOCfTBQLMS8cW2gwHWolEsoXNc34vpFccTEGlue4PTOul1%2B%2FDL5klkPKquLcEVMlJgsxwGKyFjw5ewKwEh8uJQS0uR%2BgfhXlFmx3tFzoC4FAfVH5T12HybMfAfes%2Bl4gEYDChnPm6kaSL%2BH696qnM013AHuRcjDcfkuz38yzIHn1yaQw5LPh%2FBnBS&X-Amz-Signature=b66725b08e87750eb92c9ba64efd28ab805d45149097c2fa38319ef332871f4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X4Q2YTQ%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQC%2B%2FOQ5rTLrYnzepyVhkyvzFjP4G4K9YKusfFyO2LF9oQIgfk%2FdoM6oUF7UxesOfL0GqkQJk4vf7Z29sM8XEqMkidYq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDNT2OLeZM1zfrIkh6yrcA0%2FjZpfavGaCZBDHXEya6a23WCESbURdHOtxVstVjbQSeAoDdxuuwEWirlzOoDfkqbct7f7SG1sV8u%2BlWhHr%2FoQfdFAN5chGj6nETW6L3%2Firdc%2B1GL61wZkMXv9bzZ0gpeZ8jCKDqN5I%2B91SbVo6WbZe0cWKO8SORhESGKPrLsr%2FkMz%2B%2FER5nsojq6bT2S%2FQs%2FdXbZNzwDL%2B5%2BfMKwaVWUjJ%2BaVcKxuqgxaieHC0atdZYKKt7kO4RfDvqyxFZ0B%2FuxlCMGd6Xwktu9dNTUVVwO%2B%2B7f%2B%2BN0CS581tm5gpeyZi4pzeIxCuAxAEENRuMHkzBUFEJRBzXZqD3HVdiBMbSaidqgSP%2FJOnoFXbALbhOOYFRWM7lSfdTWml37yLJhKIA1zhv61N5dfk2Okflz%2F8HeUMcqKKHulgv47dOCBlKr9PkyzkLalRueIbxWcc%2F8UyJn6%2Fkr%2BS%2Baf1CTCaVK2ZiKWbYOUUGiLmGKrcnyeNN4cxJveSuFPy4GbRjlP3HBgVqoEKSmqluwaiq8i2WACwW8eJaoGEL84Y0Il4Uh%2Fzye3zA0cf9EUUte4rkder6%2By6KxjUb9lHzZCqIHcjrntqOkYIvFkA%2FSfuz8n1lfD84cfyj2bAERxXYupMWrCQMOfUm88GOqUB%2F9LPyKuACKB0ivu5bF4N3ewkKj2dogGBqxu%2FOCfTBQLMS8cW2gwHWolEsoXNc34vpFccTEGlue4PTOul1%2B%2FDL5klkPKquLcEVMlJgsxwGKyFjw5ewKwEh8uJQS0uR%2BgfhXlFmx3tFzoC4FAfVH5T12HybMfAfes%2Bl4gEYDChnPm6kaSL%2BH696qnM013AHuRcjDcfkuz38yzIHn1yaQw5LPh%2FBnBS&X-Amz-Signature=859ce6e4ab64f9fb1b251a7ffaf1f64490065b731ce110c212eb5529cec79b8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X4Q2YTQ%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQC%2B%2FOQ5rTLrYnzepyVhkyvzFjP4G4K9YKusfFyO2LF9oQIgfk%2FdoM6oUF7UxesOfL0GqkQJk4vf7Z29sM8XEqMkidYq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDNT2OLeZM1zfrIkh6yrcA0%2FjZpfavGaCZBDHXEya6a23WCESbURdHOtxVstVjbQSeAoDdxuuwEWirlzOoDfkqbct7f7SG1sV8u%2BlWhHr%2FoQfdFAN5chGj6nETW6L3%2Firdc%2B1GL61wZkMXv9bzZ0gpeZ8jCKDqN5I%2B91SbVo6WbZe0cWKO8SORhESGKPrLsr%2FkMz%2B%2FER5nsojq6bT2S%2FQs%2FdXbZNzwDL%2B5%2BfMKwaVWUjJ%2BaVcKxuqgxaieHC0atdZYKKt7kO4RfDvqyxFZ0B%2FuxlCMGd6Xwktu9dNTUVVwO%2B%2B7f%2B%2BN0CS581tm5gpeyZi4pzeIxCuAxAEENRuMHkzBUFEJRBzXZqD3HVdiBMbSaidqgSP%2FJOnoFXbALbhOOYFRWM7lSfdTWml37yLJhKIA1zhv61N5dfk2Okflz%2F8HeUMcqKKHulgv47dOCBlKr9PkyzkLalRueIbxWcc%2F8UyJn6%2Fkr%2BS%2Baf1CTCaVK2ZiKWbYOUUGiLmGKrcnyeNN4cxJveSuFPy4GbRjlP3HBgVqoEKSmqluwaiq8i2WACwW8eJaoGEL84Y0Il4Uh%2Fzye3zA0cf9EUUte4rkder6%2By6KxjUb9lHzZCqIHcjrntqOkYIvFkA%2FSfuz8n1lfD84cfyj2bAERxXYupMWrCQMOfUm88GOqUB%2F9LPyKuACKB0ivu5bF4N3ewkKj2dogGBqxu%2FOCfTBQLMS8cW2gwHWolEsoXNc34vpFccTEGlue4PTOul1%2B%2FDL5klkPKquLcEVMlJgsxwGKyFjw5ewKwEh8uJQS0uR%2BgfhXlFmx3tFzoC4FAfVH5T12HybMfAfes%2Bl4gEYDChnPm6kaSL%2BH696qnM013AHuRcjDcfkuz38yzIHn1yaQw5LPh%2FBnBS&X-Amz-Signature=85b0a5a1bd5f419cfd984d7031cb0fc1e3fb8463b0ab6f00c68111b6b80673b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X4Q2YTQ%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQC%2B%2FOQ5rTLrYnzepyVhkyvzFjP4G4K9YKusfFyO2LF9oQIgfk%2FdoM6oUF7UxesOfL0GqkQJk4vf7Z29sM8XEqMkidYq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDNT2OLeZM1zfrIkh6yrcA0%2FjZpfavGaCZBDHXEya6a23WCESbURdHOtxVstVjbQSeAoDdxuuwEWirlzOoDfkqbct7f7SG1sV8u%2BlWhHr%2FoQfdFAN5chGj6nETW6L3%2Firdc%2B1GL61wZkMXv9bzZ0gpeZ8jCKDqN5I%2B91SbVo6WbZe0cWKO8SORhESGKPrLsr%2FkMz%2B%2FER5nsojq6bT2S%2FQs%2FdXbZNzwDL%2B5%2BfMKwaVWUjJ%2BaVcKxuqgxaieHC0atdZYKKt7kO4RfDvqyxFZ0B%2FuxlCMGd6Xwktu9dNTUVVwO%2B%2B7f%2B%2BN0CS581tm5gpeyZi4pzeIxCuAxAEENRuMHkzBUFEJRBzXZqD3HVdiBMbSaidqgSP%2FJOnoFXbALbhOOYFRWM7lSfdTWml37yLJhKIA1zhv61N5dfk2Okflz%2F8HeUMcqKKHulgv47dOCBlKr9PkyzkLalRueIbxWcc%2F8UyJn6%2Fkr%2BS%2Baf1CTCaVK2ZiKWbYOUUGiLmGKrcnyeNN4cxJveSuFPy4GbRjlP3HBgVqoEKSmqluwaiq8i2WACwW8eJaoGEL84Y0Il4Uh%2Fzye3zA0cf9EUUte4rkder6%2By6KxjUb9lHzZCqIHcjrntqOkYIvFkA%2FSfuz8n1lfD84cfyj2bAERxXYupMWrCQMOfUm88GOqUB%2F9LPyKuACKB0ivu5bF4N3ewkKj2dogGBqxu%2FOCfTBQLMS8cW2gwHWolEsoXNc34vpFccTEGlue4PTOul1%2B%2FDL5klkPKquLcEVMlJgsxwGKyFjw5ewKwEh8uJQS0uR%2BgfhXlFmx3tFzoC4FAfVH5T12HybMfAfes%2Bl4gEYDChnPm6kaSL%2BH696qnM013AHuRcjDcfkuz38yzIHn1yaQw5LPh%2FBnBS&X-Amz-Signature=04321f2fb52c15dedb38ad91f076556b5d0ba04b0fdc5d61787d54766559a155&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X4Q2YTQ%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQC%2B%2FOQ5rTLrYnzepyVhkyvzFjP4G4K9YKusfFyO2LF9oQIgfk%2FdoM6oUF7UxesOfL0GqkQJk4vf7Z29sM8XEqMkidYq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDNT2OLeZM1zfrIkh6yrcA0%2FjZpfavGaCZBDHXEya6a23WCESbURdHOtxVstVjbQSeAoDdxuuwEWirlzOoDfkqbct7f7SG1sV8u%2BlWhHr%2FoQfdFAN5chGj6nETW6L3%2Firdc%2B1GL61wZkMXv9bzZ0gpeZ8jCKDqN5I%2B91SbVo6WbZe0cWKO8SORhESGKPrLsr%2FkMz%2B%2FER5nsojq6bT2S%2FQs%2FdXbZNzwDL%2B5%2BfMKwaVWUjJ%2BaVcKxuqgxaieHC0atdZYKKt7kO4RfDvqyxFZ0B%2FuxlCMGd6Xwktu9dNTUVVwO%2B%2B7f%2B%2BN0CS581tm5gpeyZi4pzeIxCuAxAEENRuMHkzBUFEJRBzXZqD3HVdiBMbSaidqgSP%2FJOnoFXbALbhOOYFRWM7lSfdTWml37yLJhKIA1zhv61N5dfk2Okflz%2F8HeUMcqKKHulgv47dOCBlKr9PkyzkLalRueIbxWcc%2F8UyJn6%2Fkr%2BS%2Baf1CTCaVK2ZiKWbYOUUGiLmGKrcnyeNN4cxJveSuFPy4GbRjlP3HBgVqoEKSmqluwaiq8i2WACwW8eJaoGEL84Y0Il4Uh%2Fzye3zA0cf9EUUte4rkder6%2By6KxjUb9lHzZCqIHcjrntqOkYIvFkA%2FSfuz8n1lfD84cfyj2bAERxXYupMWrCQMOfUm88GOqUB%2F9LPyKuACKB0ivu5bF4N3ewkKj2dogGBqxu%2FOCfTBQLMS8cW2gwHWolEsoXNc34vpFccTEGlue4PTOul1%2B%2FDL5klkPKquLcEVMlJgsxwGKyFjw5ewKwEh8uJQS0uR%2BgfhXlFmx3tFzoC4FAfVH5T12HybMfAfes%2Bl4gEYDChnPm6kaSL%2BH696qnM013AHuRcjDcfkuz38yzIHn1yaQw5LPh%2FBnBS&X-Amz-Signature=5e8960a0c687eb101b993c8bf77790ed96bde3c8ffba1bd0e111d7e28eb01e7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

