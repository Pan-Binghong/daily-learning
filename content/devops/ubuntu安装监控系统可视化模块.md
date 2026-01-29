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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUJU2U7G%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFCp%2BgU67AWSas6U01TiM%2B%2B7XVrywYN46zqPUwRqbvGLAiBiSUTGeK8maZWj89DM5zqLCvyKidVxweBkc1aiBNscnSr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIM05JYzix9fpKOPw%2FNKtwD6J2o69GwUow3u0nwcaKqPigJbKMXxtuYrPzdBqNkgL5v7BrklF6L8yyOTX45k15yQ5iwJSxSR5dsrj0FUDII%2FCCtby%2FgcP%2BfuSgEewDKbsl%2BY0T3HouT9Qx2yVy8x%2B9XwWP1XlRUFpEsk5uUnbTwJ0K%2FKGMnqdRDBwaR%2F%2FsqcyOes4Om4w5E2rEzBlqwaXAPaNDW7XQnhfDIqCeEm937IrcBjna%2FsJIrHFbiW2lHpasdC1nVL1UKkesK3D3sHuz0o1Ed1JWEogENOs4iQkeZEqcUe9GW%2BtLSJQBqQeJnx2bZY1Www3CS1q7JT8OLYg8HiKfMxEZIwFT3yPOHYbWT3rlEXHBtlyxV4d9aPg8P9OMmojNaES4Gmp4KsCztIgX7XABQPK9SIIBKqIoGCnCgseuCvgSuB8FUPBQAtFJ%2BI8gZ%2BGE%2FWWCu6ZXFSWMY1BVln1EVCdfxXa7EhybB5cDJottYRZFCIEFKenZk2WqerxAlfEfXizrvtlo%2BkXzw%2ByP969%2FzR3xajNd3RQpJoRdeahtVDY7OX1c4QCi3Y36dUv6EfngjTmpig8mM9yuLtIIIgRKEnSmYGJaKPCXz8yE9niiUtMJS2aBIjxpc%2B2eA1nG3vWbzelGnyoUeYFgw2aLrywY6pgHKdDjtVkKpyin1xyra7zQaNb%2BO%2FJauBzZWjuGe2eeoDsF8Vz9TnbYcFT5zzaius%2FK5UHJUzKqXmhvCmab%2B63PWM4tL%2BYdXeddLA%2BI91CcicsNoOENUmPtFKMQPxZZe1IrWdqKVNCZoJiRAqGckPWJ3epRWuiJ%2F3n58Kp9M1PiAQY6a8CtpiCnoLHKddRQCLyUV8NvAOceDQGQKy9niFDszpTFA%2Begi&X-Amz-Signature=bc6ad272fec2e338d80a39321171f343b487bd0569d1b8790eff97da071aa7bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUJU2U7G%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFCp%2BgU67AWSas6U01TiM%2B%2B7XVrywYN46zqPUwRqbvGLAiBiSUTGeK8maZWj89DM5zqLCvyKidVxweBkc1aiBNscnSr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIM05JYzix9fpKOPw%2FNKtwD6J2o69GwUow3u0nwcaKqPigJbKMXxtuYrPzdBqNkgL5v7BrklF6L8yyOTX45k15yQ5iwJSxSR5dsrj0FUDII%2FCCtby%2FgcP%2BfuSgEewDKbsl%2BY0T3HouT9Qx2yVy8x%2B9XwWP1XlRUFpEsk5uUnbTwJ0K%2FKGMnqdRDBwaR%2F%2FsqcyOes4Om4w5E2rEzBlqwaXAPaNDW7XQnhfDIqCeEm937IrcBjna%2FsJIrHFbiW2lHpasdC1nVL1UKkesK3D3sHuz0o1Ed1JWEogENOs4iQkeZEqcUe9GW%2BtLSJQBqQeJnx2bZY1Www3CS1q7JT8OLYg8HiKfMxEZIwFT3yPOHYbWT3rlEXHBtlyxV4d9aPg8P9OMmojNaES4Gmp4KsCztIgX7XABQPK9SIIBKqIoGCnCgseuCvgSuB8FUPBQAtFJ%2BI8gZ%2BGE%2FWWCu6ZXFSWMY1BVln1EVCdfxXa7EhybB5cDJottYRZFCIEFKenZk2WqerxAlfEfXizrvtlo%2BkXzw%2ByP969%2FzR3xajNd3RQpJoRdeahtVDY7OX1c4QCi3Y36dUv6EfngjTmpig8mM9yuLtIIIgRKEnSmYGJaKPCXz8yE9niiUtMJS2aBIjxpc%2B2eA1nG3vWbzelGnyoUeYFgw2aLrywY6pgHKdDjtVkKpyin1xyra7zQaNb%2BO%2FJauBzZWjuGe2eeoDsF8Vz9TnbYcFT5zzaius%2FK5UHJUzKqXmhvCmab%2B63PWM4tL%2BYdXeddLA%2BI91CcicsNoOENUmPtFKMQPxZZe1IrWdqKVNCZoJiRAqGckPWJ3epRWuiJ%2F3n58Kp9M1PiAQY6a8CtpiCnoLHKddRQCLyUV8NvAOceDQGQKy9niFDszpTFA%2Begi&X-Amz-Signature=75ae2ec1b6d947e7afd5cbc922852ee2d2e69d0b65221634e959a0e71f3eba8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUJU2U7G%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFCp%2BgU67AWSas6U01TiM%2B%2B7XVrywYN46zqPUwRqbvGLAiBiSUTGeK8maZWj89DM5zqLCvyKidVxweBkc1aiBNscnSr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIM05JYzix9fpKOPw%2FNKtwD6J2o69GwUow3u0nwcaKqPigJbKMXxtuYrPzdBqNkgL5v7BrklF6L8yyOTX45k15yQ5iwJSxSR5dsrj0FUDII%2FCCtby%2FgcP%2BfuSgEewDKbsl%2BY0T3HouT9Qx2yVy8x%2B9XwWP1XlRUFpEsk5uUnbTwJ0K%2FKGMnqdRDBwaR%2F%2FsqcyOes4Om4w5E2rEzBlqwaXAPaNDW7XQnhfDIqCeEm937IrcBjna%2FsJIrHFbiW2lHpasdC1nVL1UKkesK3D3sHuz0o1Ed1JWEogENOs4iQkeZEqcUe9GW%2BtLSJQBqQeJnx2bZY1Www3CS1q7JT8OLYg8HiKfMxEZIwFT3yPOHYbWT3rlEXHBtlyxV4d9aPg8P9OMmojNaES4Gmp4KsCztIgX7XABQPK9SIIBKqIoGCnCgseuCvgSuB8FUPBQAtFJ%2BI8gZ%2BGE%2FWWCu6ZXFSWMY1BVln1EVCdfxXa7EhybB5cDJottYRZFCIEFKenZk2WqerxAlfEfXizrvtlo%2BkXzw%2ByP969%2FzR3xajNd3RQpJoRdeahtVDY7OX1c4QCi3Y36dUv6EfngjTmpig8mM9yuLtIIIgRKEnSmYGJaKPCXz8yE9niiUtMJS2aBIjxpc%2B2eA1nG3vWbzelGnyoUeYFgw2aLrywY6pgHKdDjtVkKpyin1xyra7zQaNb%2BO%2FJauBzZWjuGe2eeoDsF8Vz9TnbYcFT5zzaius%2FK5UHJUzKqXmhvCmab%2B63PWM4tL%2BYdXeddLA%2BI91CcicsNoOENUmPtFKMQPxZZe1IrWdqKVNCZoJiRAqGckPWJ3epRWuiJ%2F3n58Kp9M1PiAQY6a8CtpiCnoLHKddRQCLyUV8NvAOceDQGQKy9niFDszpTFA%2Begi&X-Amz-Signature=44e74c229888b045862a69cc9448381ca4b7b1cc1d2134e537577cd750484af6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUJU2U7G%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFCp%2BgU67AWSas6U01TiM%2B%2B7XVrywYN46zqPUwRqbvGLAiBiSUTGeK8maZWj89DM5zqLCvyKidVxweBkc1aiBNscnSr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIM05JYzix9fpKOPw%2FNKtwD6J2o69GwUow3u0nwcaKqPigJbKMXxtuYrPzdBqNkgL5v7BrklF6L8yyOTX45k15yQ5iwJSxSR5dsrj0FUDII%2FCCtby%2FgcP%2BfuSgEewDKbsl%2BY0T3HouT9Qx2yVy8x%2B9XwWP1XlRUFpEsk5uUnbTwJ0K%2FKGMnqdRDBwaR%2F%2FsqcyOes4Om4w5E2rEzBlqwaXAPaNDW7XQnhfDIqCeEm937IrcBjna%2FsJIrHFbiW2lHpasdC1nVL1UKkesK3D3sHuz0o1Ed1JWEogENOs4iQkeZEqcUe9GW%2BtLSJQBqQeJnx2bZY1Www3CS1q7JT8OLYg8HiKfMxEZIwFT3yPOHYbWT3rlEXHBtlyxV4d9aPg8P9OMmojNaES4Gmp4KsCztIgX7XABQPK9SIIBKqIoGCnCgseuCvgSuB8FUPBQAtFJ%2BI8gZ%2BGE%2FWWCu6ZXFSWMY1BVln1EVCdfxXa7EhybB5cDJottYRZFCIEFKenZk2WqerxAlfEfXizrvtlo%2BkXzw%2ByP969%2FzR3xajNd3RQpJoRdeahtVDY7OX1c4QCi3Y36dUv6EfngjTmpig8mM9yuLtIIIgRKEnSmYGJaKPCXz8yE9niiUtMJS2aBIjxpc%2B2eA1nG3vWbzelGnyoUeYFgw2aLrywY6pgHKdDjtVkKpyin1xyra7zQaNb%2BO%2FJauBzZWjuGe2eeoDsF8Vz9TnbYcFT5zzaius%2FK5UHJUzKqXmhvCmab%2B63PWM4tL%2BYdXeddLA%2BI91CcicsNoOENUmPtFKMQPxZZe1IrWdqKVNCZoJiRAqGckPWJ3epRWuiJ%2F3n58Kp9M1PiAQY6a8CtpiCnoLHKddRQCLyUV8NvAOceDQGQKy9niFDszpTFA%2Begi&X-Amz-Signature=b2381b17b09f3c4cc586980a10cf6fa3eb86125e89014d873268176bf10e6ca5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUJU2U7G%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFCp%2BgU67AWSas6U01TiM%2B%2B7XVrywYN46zqPUwRqbvGLAiBiSUTGeK8maZWj89DM5zqLCvyKidVxweBkc1aiBNscnSr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIM05JYzix9fpKOPw%2FNKtwD6J2o69GwUow3u0nwcaKqPigJbKMXxtuYrPzdBqNkgL5v7BrklF6L8yyOTX45k15yQ5iwJSxSR5dsrj0FUDII%2FCCtby%2FgcP%2BfuSgEewDKbsl%2BY0T3HouT9Qx2yVy8x%2B9XwWP1XlRUFpEsk5uUnbTwJ0K%2FKGMnqdRDBwaR%2F%2FsqcyOes4Om4w5E2rEzBlqwaXAPaNDW7XQnhfDIqCeEm937IrcBjna%2FsJIrHFbiW2lHpasdC1nVL1UKkesK3D3sHuz0o1Ed1JWEogENOs4iQkeZEqcUe9GW%2BtLSJQBqQeJnx2bZY1Www3CS1q7JT8OLYg8HiKfMxEZIwFT3yPOHYbWT3rlEXHBtlyxV4d9aPg8P9OMmojNaES4Gmp4KsCztIgX7XABQPK9SIIBKqIoGCnCgseuCvgSuB8FUPBQAtFJ%2BI8gZ%2BGE%2FWWCu6ZXFSWMY1BVln1EVCdfxXa7EhybB5cDJottYRZFCIEFKenZk2WqerxAlfEfXizrvtlo%2BkXzw%2ByP969%2FzR3xajNd3RQpJoRdeahtVDY7OX1c4QCi3Y36dUv6EfngjTmpig8mM9yuLtIIIgRKEnSmYGJaKPCXz8yE9niiUtMJS2aBIjxpc%2B2eA1nG3vWbzelGnyoUeYFgw2aLrywY6pgHKdDjtVkKpyin1xyra7zQaNb%2BO%2FJauBzZWjuGe2eeoDsF8Vz9TnbYcFT5zzaius%2FK5UHJUzKqXmhvCmab%2B63PWM4tL%2BYdXeddLA%2BI91CcicsNoOENUmPtFKMQPxZZe1IrWdqKVNCZoJiRAqGckPWJ3epRWuiJ%2F3n58Kp9M1PiAQY6a8CtpiCnoLHKddRQCLyUV8NvAOceDQGQKy9niFDszpTFA%2Begi&X-Amz-Signature=54bba0151d37ce970f0c18b8be4d3ea629905b2387b0008e07e3e7709c7c293e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUJU2U7G%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFCp%2BgU67AWSas6U01TiM%2B%2B7XVrywYN46zqPUwRqbvGLAiBiSUTGeK8maZWj89DM5zqLCvyKidVxweBkc1aiBNscnSr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIM05JYzix9fpKOPw%2FNKtwD6J2o69GwUow3u0nwcaKqPigJbKMXxtuYrPzdBqNkgL5v7BrklF6L8yyOTX45k15yQ5iwJSxSR5dsrj0FUDII%2FCCtby%2FgcP%2BfuSgEewDKbsl%2BY0T3HouT9Qx2yVy8x%2B9XwWP1XlRUFpEsk5uUnbTwJ0K%2FKGMnqdRDBwaR%2F%2FsqcyOes4Om4w5E2rEzBlqwaXAPaNDW7XQnhfDIqCeEm937IrcBjna%2FsJIrHFbiW2lHpasdC1nVL1UKkesK3D3sHuz0o1Ed1JWEogENOs4iQkeZEqcUe9GW%2BtLSJQBqQeJnx2bZY1Www3CS1q7JT8OLYg8HiKfMxEZIwFT3yPOHYbWT3rlEXHBtlyxV4d9aPg8P9OMmojNaES4Gmp4KsCztIgX7XABQPK9SIIBKqIoGCnCgseuCvgSuB8FUPBQAtFJ%2BI8gZ%2BGE%2FWWCu6ZXFSWMY1BVln1EVCdfxXa7EhybB5cDJottYRZFCIEFKenZk2WqerxAlfEfXizrvtlo%2BkXzw%2ByP969%2FzR3xajNd3RQpJoRdeahtVDY7OX1c4QCi3Y36dUv6EfngjTmpig8mM9yuLtIIIgRKEnSmYGJaKPCXz8yE9niiUtMJS2aBIjxpc%2B2eA1nG3vWbzelGnyoUeYFgw2aLrywY6pgHKdDjtVkKpyin1xyra7zQaNb%2BO%2FJauBzZWjuGe2eeoDsF8Vz9TnbYcFT5zzaius%2FK5UHJUzKqXmhvCmab%2B63PWM4tL%2BYdXeddLA%2BI91CcicsNoOENUmPtFKMQPxZZe1IrWdqKVNCZoJiRAqGckPWJ3epRWuiJ%2F3n58Kp9M1PiAQY6a8CtpiCnoLHKddRQCLyUV8NvAOceDQGQKy9niFDszpTFA%2Begi&X-Amz-Signature=133f577389c2916d629b5e8e17289f78c3f2514ee6c248d4f72904c991b9f51f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUJU2U7G%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFCp%2BgU67AWSas6U01TiM%2B%2B7XVrywYN46zqPUwRqbvGLAiBiSUTGeK8maZWj89DM5zqLCvyKidVxweBkc1aiBNscnSr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIM05JYzix9fpKOPw%2FNKtwD6J2o69GwUow3u0nwcaKqPigJbKMXxtuYrPzdBqNkgL5v7BrklF6L8yyOTX45k15yQ5iwJSxSR5dsrj0FUDII%2FCCtby%2FgcP%2BfuSgEewDKbsl%2BY0T3HouT9Qx2yVy8x%2B9XwWP1XlRUFpEsk5uUnbTwJ0K%2FKGMnqdRDBwaR%2F%2FsqcyOes4Om4w5E2rEzBlqwaXAPaNDW7XQnhfDIqCeEm937IrcBjna%2FsJIrHFbiW2lHpasdC1nVL1UKkesK3D3sHuz0o1Ed1JWEogENOs4iQkeZEqcUe9GW%2BtLSJQBqQeJnx2bZY1Www3CS1q7JT8OLYg8HiKfMxEZIwFT3yPOHYbWT3rlEXHBtlyxV4d9aPg8P9OMmojNaES4Gmp4KsCztIgX7XABQPK9SIIBKqIoGCnCgseuCvgSuB8FUPBQAtFJ%2BI8gZ%2BGE%2FWWCu6ZXFSWMY1BVln1EVCdfxXa7EhybB5cDJottYRZFCIEFKenZk2WqerxAlfEfXizrvtlo%2BkXzw%2ByP969%2FzR3xajNd3RQpJoRdeahtVDY7OX1c4QCi3Y36dUv6EfngjTmpig8mM9yuLtIIIgRKEnSmYGJaKPCXz8yE9niiUtMJS2aBIjxpc%2B2eA1nG3vWbzelGnyoUeYFgw2aLrywY6pgHKdDjtVkKpyin1xyra7zQaNb%2BO%2FJauBzZWjuGe2eeoDsF8Vz9TnbYcFT5zzaius%2FK5UHJUzKqXmhvCmab%2B63PWM4tL%2BYdXeddLA%2BI91CcicsNoOENUmPtFKMQPxZZe1IrWdqKVNCZoJiRAqGckPWJ3epRWuiJ%2F3n58Kp9M1PiAQY6a8CtpiCnoLHKddRQCLyUV8NvAOceDQGQKy9niFDszpTFA%2Begi&X-Amz-Signature=9ec750d5816378def5266ed8822e9602354d141c22b7f668fa59e3c4ebe59de7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

