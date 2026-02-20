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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RQKBMDQ%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0siM8Qw%2B2eeQD9jOxSCARfPo9ynBShtryQx%2F%2BdSEUUgIgW0Bl%2F0SazovgzzgD9gAH%2FGiofe%2BPXTbAeITQmPo3cvgqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIMUkQLm%2B7CIRvMZhircA7%2BcD1L4xek7LcfAzw2ciVxSE%2FT3D8%2FAD%2FJLsDqiiw2Bi3sIoIJkYknqyn12ueRIKYXwYHi3UB5d%2F9d3dz5p1LNaHmQKqR6njpWDatp2y6mS9uesPFCLgMhx1vdZs6xbKJdWLxRlcwAlgAq3FJTPBpyeg%2BV0HVZMIg%2Br7vWaECIl5PBlaoCxFkZvfpBZfZafk%2B8CHGPBuNKkvFCHlD4G%2BINvzSpdAepcZChuZT79fh9gWQq29neRX74IswFkKIWoyT1Sfz4YFBhZY8HSjZnbIdhw46fzFc6eLh5PUATGs5R7Kj%2Bx9RsPvRg167njVL1e3wKbiFxokWSwdCVjI2kZt4sF4fOGluqtIs6%2F1gXbe2su5kbHjfXq4SBq4W%2FvKkT9XcZXIqSwxj8dFRLOV4ScVBT9CPnbWNgzWAwmsFe%2BwfiNLO%2BV%2FDY0LT9pGBEYxz8Rrs5fJaIr%2FAbbiOVUr0dTy%2B79qLrBAjJyccGvnW3I%2FrWWzhAH%2B2k8TQQ11ADa8WeIaW%2FCuNXrcuxlQhnlhKPnRaeJcoIoqz12FDePbanXrTWzmQgkoYTkFqxfhVk3MKT4iVYz02UHHp3Pyw8HyoO%2FgRO6XJ%2FPH8x0Rsb71FchvZjn7CUD1gdZqhqvkbseML6R38wGOqUBOyklCmm%2BmEaUXl3WB7TQMIPs5mU3RRVpyCPUflPW0n3Xd5xbuoJ4GEbNe2tnQ99W%2FXFSFQvuy7z7CMv72cvWGyYosIqsLt%2B%2B8GSOOvU3YMKJL%2BicK8IgvQf8sig5ERKJOQ%2F26bE8oZsomp3EpJQQXZNJzpo%2FQd0t4Wczo5hRHX4Rg%2FWSRO9e25YdHEt7a6gTE%2FnLGwSxcvDUEsiX9rQ0Bb3PNDoq&X-Amz-Signature=c86b9c913a74e27b63ddc56701b2d50d4edaadfbdb2e58f949d9b86df733f3f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RQKBMDQ%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0siM8Qw%2B2eeQD9jOxSCARfPo9ynBShtryQx%2F%2BdSEUUgIgW0Bl%2F0SazovgzzgD9gAH%2FGiofe%2BPXTbAeITQmPo3cvgqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIMUkQLm%2B7CIRvMZhircA7%2BcD1L4xek7LcfAzw2ciVxSE%2FT3D8%2FAD%2FJLsDqiiw2Bi3sIoIJkYknqyn12ueRIKYXwYHi3UB5d%2F9d3dz5p1LNaHmQKqR6njpWDatp2y6mS9uesPFCLgMhx1vdZs6xbKJdWLxRlcwAlgAq3FJTPBpyeg%2BV0HVZMIg%2Br7vWaECIl5PBlaoCxFkZvfpBZfZafk%2B8CHGPBuNKkvFCHlD4G%2BINvzSpdAepcZChuZT79fh9gWQq29neRX74IswFkKIWoyT1Sfz4YFBhZY8HSjZnbIdhw46fzFc6eLh5PUATGs5R7Kj%2Bx9RsPvRg167njVL1e3wKbiFxokWSwdCVjI2kZt4sF4fOGluqtIs6%2F1gXbe2su5kbHjfXq4SBq4W%2FvKkT9XcZXIqSwxj8dFRLOV4ScVBT9CPnbWNgzWAwmsFe%2BwfiNLO%2BV%2FDY0LT9pGBEYxz8Rrs5fJaIr%2FAbbiOVUr0dTy%2B79qLrBAjJyccGvnW3I%2FrWWzhAH%2B2k8TQQ11ADa8WeIaW%2FCuNXrcuxlQhnlhKPnRaeJcoIoqz12FDePbanXrTWzmQgkoYTkFqxfhVk3MKT4iVYz02UHHp3Pyw8HyoO%2FgRO6XJ%2FPH8x0Rsb71FchvZjn7CUD1gdZqhqvkbseML6R38wGOqUBOyklCmm%2BmEaUXl3WB7TQMIPs5mU3RRVpyCPUflPW0n3Xd5xbuoJ4GEbNe2tnQ99W%2FXFSFQvuy7z7CMv72cvWGyYosIqsLt%2B%2B8GSOOvU3YMKJL%2BicK8IgvQf8sig5ERKJOQ%2F26bE8oZsomp3EpJQQXZNJzpo%2FQd0t4Wczo5hRHX4Rg%2FWSRO9e25YdHEt7a6gTE%2FnLGwSxcvDUEsiX9rQ0Bb3PNDoq&X-Amz-Signature=8c37a2d34eda559f22d846d9fa6bdb9cbe67108f1ff0d11f852425905676abdf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RQKBMDQ%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0siM8Qw%2B2eeQD9jOxSCARfPo9ynBShtryQx%2F%2BdSEUUgIgW0Bl%2F0SazovgzzgD9gAH%2FGiofe%2BPXTbAeITQmPo3cvgqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIMUkQLm%2B7CIRvMZhircA7%2BcD1L4xek7LcfAzw2ciVxSE%2FT3D8%2FAD%2FJLsDqiiw2Bi3sIoIJkYknqyn12ueRIKYXwYHi3UB5d%2F9d3dz5p1LNaHmQKqR6njpWDatp2y6mS9uesPFCLgMhx1vdZs6xbKJdWLxRlcwAlgAq3FJTPBpyeg%2BV0HVZMIg%2Br7vWaECIl5PBlaoCxFkZvfpBZfZafk%2B8CHGPBuNKkvFCHlD4G%2BINvzSpdAepcZChuZT79fh9gWQq29neRX74IswFkKIWoyT1Sfz4YFBhZY8HSjZnbIdhw46fzFc6eLh5PUATGs5R7Kj%2Bx9RsPvRg167njVL1e3wKbiFxokWSwdCVjI2kZt4sF4fOGluqtIs6%2F1gXbe2su5kbHjfXq4SBq4W%2FvKkT9XcZXIqSwxj8dFRLOV4ScVBT9CPnbWNgzWAwmsFe%2BwfiNLO%2BV%2FDY0LT9pGBEYxz8Rrs5fJaIr%2FAbbiOVUr0dTy%2B79qLrBAjJyccGvnW3I%2FrWWzhAH%2B2k8TQQ11ADa8WeIaW%2FCuNXrcuxlQhnlhKPnRaeJcoIoqz12FDePbanXrTWzmQgkoYTkFqxfhVk3MKT4iVYz02UHHp3Pyw8HyoO%2FgRO6XJ%2FPH8x0Rsb71FchvZjn7CUD1gdZqhqvkbseML6R38wGOqUBOyklCmm%2BmEaUXl3WB7TQMIPs5mU3RRVpyCPUflPW0n3Xd5xbuoJ4GEbNe2tnQ99W%2FXFSFQvuy7z7CMv72cvWGyYosIqsLt%2B%2B8GSOOvU3YMKJL%2BicK8IgvQf8sig5ERKJOQ%2F26bE8oZsomp3EpJQQXZNJzpo%2FQd0t4Wczo5hRHX4Rg%2FWSRO9e25YdHEt7a6gTE%2FnLGwSxcvDUEsiX9rQ0Bb3PNDoq&X-Amz-Signature=e11b824fc3141566cc0555c29da0fe2defc9906a2de1d35e92e46488207deb04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RQKBMDQ%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0siM8Qw%2B2eeQD9jOxSCARfPo9ynBShtryQx%2F%2BdSEUUgIgW0Bl%2F0SazovgzzgD9gAH%2FGiofe%2BPXTbAeITQmPo3cvgqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIMUkQLm%2B7CIRvMZhircA7%2BcD1L4xek7LcfAzw2ciVxSE%2FT3D8%2FAD%2FJLsDqiiw2Bi3sIoIJkYknqyn12ueRIKYXwYHi3UB5d%2F9d3dz5p1LNaHmQKqR6njpWDatp2y6mS9uesPFCLgMhx1vdZs6xbKJdWLxRlcwAlgAq3FJTPBpyeg%2BV0HVZMIg%2Br7vWaECIl5PBlaoCxFkZvfpBZfZafk%2B8CHGPBuNKkvFCHlD4G%2BINvzSpdAepcZChuZT79fh9gWQq29neRX74IswFkKIWoyT1Sfz4YFBhZY8HSjZnbIdhw46fzFc6eLh5PUATGs5R7Kj%2Bx9RsPvRg167njVL1e3wKbiFxokWSwdCVjI2kZt4sF4fOGluqtIs6%2F1gXbe2su5kbHjfXq4SBq4W%2FvKkT9XcZXIqSwxj8dFRLOV4ScVBT9CPnbWNgzWAwmsFe%2BwfiNLO%2BV%2FDY0LT9pGBEYxz8Rrs5fJaIr%2FAbbiOVUr0dTy%2B79qLrBAjJyccGvnW3I%2FrWWzhAH%2B2k8TQQ11ADa8WeIaW%2FCuNXrcuxlQhnlhKPnRaeJcoIoqz12FDePbanXrTWzmQgkoYTkFqxfhVk3MKT4iVYz02UHHp3Pyw8HyoO%2FgRO6XJ%2FPH8x0Rsb71FchvZjn7CUD1gdZqhqvkbseML6R38wGOqUBOyklCmm%2BmEaUXl3WB7TQMIPs5mU3RRVpyCPUflPW0n3Xd5xbuoJ4GEbNe2tnQ99W%2FXFSFQvuy7z7CMv72cvWGyYosIqsLt%2B%2B8GSOOvU3YMKJL%2BicK8IgvQf8sig5ERKJOQ%2F26bE8oZsomp3EpJQQXZNJzpo%2FQd0t4Wczo5hRHX4Rg%2FWSRO9e25YdHEt7a6gTE%2FnLGwSxcvDUEsiX9rQ0Bb3PNDoq&X-Amz-Signature=86b20b397c2d0ae02c449c09d87201b2d7559b35b70d2045d1a71780490fc36a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RQKBMDQ%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0siM8Qw%2B2eeQD9jOxSCARfPo9ynBShtryQx%2F%2BdSEUUgIgW0Bl%2F0SazovgzzgD9gAH%2FGiofe%2BPXTbAeITQmPo3cvgqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIMUkQLm%2B7CIRvMZhircA7%2BcD1L4xek7LcfAzw2ciVxSE%2FT3D8%2FAD%2FJLsDqiiw2Bi3sIoIJkYknqyn12ueRIKYXwYHi3UB5d%2F9d3dz5p1LNaHmQKqR6njpWDatp2y6mS9uesPFCLgMhx1vdZs6xbKJdWLxRlcwAlgAq3FJTPBpyeg%2BV0HVZMIg%2Br7vWaECIl5PBlaoCxFkZvfpBZfZafk%2B8CHGPBuNKkvFCHlD4G%2BINvzSpdAepcZChuZT79fh9gWQq29neRX74IswFkKIWoyT1Sfz4YFBhZY8HSjZnbIdhw46fzFc6eLh5PUATGs5R7Kj%2Bx9RsPvRg167njVL1e3wKbiFxokWSwdCVjI2kZt4sF4fOGluqtIs6%2F1gXbe2su5kbHjfXq4SBq4W%2FvKkT9XcZXIqSwxj8dFRLOV4ScVBT9CPnbWNgzWAwmsFe%2BwfiNLO%2BV%2FDY0LT9pGBEYxz8Rrs5fJaIr%2FAbbiOVUr0dTy%2B79qLrBAjJyccGvnW3I%2FrWWzhAH%2B2k8TQQ11ADa8WeIaW%2FCuNXrcuxlQhnlhKPnRaeJcoIoqz12FDePbanXrTWzmQgkoYTkFqxfhVk3MKT4iVYz02UHHp3Pyw8HyoO%2FgRO6XJ%2FPH8x0Rsb71FchvZjn7CUD1gdZqhqvkbseML6R38wGOqUBOyklCmm%2BmEaUXl3WB7TQMIPs5mU3RRVpyCPUflPW0n3Xd5xbuoJ4GEbNe2tnQ99W%2FXFSFQvuy7z7CMv72cvWGyYosIqsLt%2B%2B8GSOOvU3YMKJL%2BicK8IgvQf8sig5ERKJOQ%2F26bE8oZsomp3EpJQQXZNJzpo%2FQd0t4Wczo5hRHX4Rg%2FWSRO9e25YdHEt7a6gTE%2FnLGwSxcvDUEsiX9rQ0Bb3PNDoq&X-Amz-Signature=6bc17c06c35dbb11fdec53adb1df4c010987c262e5f824cf40bcee891d2f66e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RQKBMDQ%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0siM8Qw%2B2eeQD9jOxSCARfPo9ynBShtryQx%2F%2BdSEUUgIgW0Bl%2F0SazovgzzgD9gAH%2FGiofe%2BPXTbAeITQmPo3cvgqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIMUkQLm%2B7CIRvMZhircA7%2BcD1L4xek7LcfAzw2ciVxSE%2FT3D8%2FAD%2FJLsDqiiw2Bi3sIoIJkYknqyn12ueRIKYXwYHi3UB5d%2F9d3dz5p1LNaHmQKqR6njpWDatp2y6mS9uesPFCLgMhx1vdZs6xbKJdWLxRlcwAlgAq3FJTPBpyeg%2BV0HVZMIg%2Br7vWaECIl5PBlaoCxFkZvfpBZfZafk%2B8CHGPBuNKkvFCHlD4G%2BINvzSpdAepcZChuZT79fh9gWQq29neRX74IswFkKIWoyT1Sfz4YFBhZY8HSjZnbIdhw46fzFc6eLh5PUATGs5R7Kj%2Bx9RsPvRg167njVL1e3wKbiFxokWSwdCVjI2kZt4sF4fOGluqtIs6%2F1gXbe2su5kbHjfXq4SBq4W%2FvKkT9XcZXIqSwxj8dFRLOV4ScVBT9CPnbWNgzWAwmsFe%2BwfiNLO%2BV%2FDY0LT9pGBEYxz8Rrs5fJaIr%2FAbbiOVUr0dTy%2B79qLrBAjJyccGvnW3I%2FrWWzhAH%2B2k8TQQ11ADa8WeIaW%2FCuNXrcuxlQhnlhKPnRaeJcoIoqz12FDePbanXrTWzmQgkoYTkFqxfhVk3MKT4iVYz02UHHp3Pyw8HyoO%2FgRO6XJ%2FPH8x0Rsb71FchvZjn7CUD1gdZqhqvkbseML6R38wGOqUBOyklCmm%2BmEaUXl3WB7TQMIPs5mU3RRVpyCPUflPW0n3Xd5xbuoJ4GEbNe2tnQ99W%2FXFSFQvuy7z7CMv72cvWGyYosIqsLt%2B%2B8GSOOvU3YMKJL%2BicK8IgvQf8sig5ERKJOQ%2F26bE8oZsomp3EpJQQXZNJzpo%2FQd0t4Wczo5hRHX4Rg%2FWSRO9e25YdHEt7a6gTE%2FnLGwSxcvDUEsiX9rQ0Bb3PNDoq&X-Amz-Signature=338cc46d5e707e65cdba6a25f3bc8684aa91b2c299b10791e03e5d6f9ae57aea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RQKBMDQ%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0siM8Qw%2B2eeQD9jOxSCARfPo9ynBShtryQx%2F%2BdSEUUgIgW0Bl%2F0SazovgzzgD9gAH%2FGiofe%2BPXTbAeITQmPo3cvgqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIMUkQLm%2B7CIRvMZhircA7%2BcD1L4xek7LcfAzw2ciVxSE%2FT3D8%2FAD%2FJLsDqiiw2Bi3sIoIJkYknqyn12ueRIKYXwYHi3UB5d%2F9d3dz5p1LNaHmQKqR6njpWDatp2y6mS9uesPFCLgMhx1vdZs6xbKJdWLxRlcwAlgAq3FJTPBpyeg%2BV0HVZMIg%2Br7vWaECIl5PBlaoCxFkZvfpBZfZafk%2B8CHGPBuNKkvFCHlD4G%2BINvzSpdAepcZChuZT79fh9gWQq29neRX74IswFkKIWoyT1Sfz4YFBhZY8HSjZnbIdhw46fzFc6eLh5PUATGs5R7Kj%2Bx9RsPvRg167njVL1e3wKbiFxokWSwdCVjI2kZt4sF4fOGluqtIs6%2F1gXbe2su5kbHjfXq4SBq4W%2FvKkT9XcZXIqSwxj8dFRLOV4ScVBT9CPnbWNgzWAwmsFe%2BwfiNLO%2BV%2FDY0LT9pGBEYxz8Rrs5fJaIr%2FAbbiOVUr0dTy%2B79qLrBAjJyccGvnW3I%2FrWWzhAH%2B2k8TQQ11ADa8WeIaW%2FCuNXrcuxlQhnlhKPnRaeJcoIoqz12FDePbanXrTWzmQgkoYTkFqxfhVk3MKT4iVYz02UHHp3Pyw8HyoO%2FgRO6XJ%2FPH8x0Rsb71FchvZjn7CUD1gdZqhqvkbseML6R38wGOqUBOyklCmm%2BmEaUXl3WB7TQMIPs5mU3RRVpyCPUflPW0n3Xd5xbuoJ4GEbNe2tnQ99W%2FXFSFQvuy7z7CMv72cvWGyYosIqsLt%2B%2B8GSOOvU3YMKJL%2BicK8IgvQf8sig5ERKJOQ%2F26bE8oZsomp3EpJQQXZNJzpo%2FQd0t4Wczo5hRHX4Rg%2FWSRO9e25YdHEt7a6gTE%2FnLGwSxcvDUEsiX9rQ0Bb3PNDoq&X-Amz-Signature=38ae72484ca1813614a863abd54c669fca8abd1965c7a88db5a9c3af8341f485&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

