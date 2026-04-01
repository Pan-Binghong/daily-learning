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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLBDT2DZ%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpdfoVJ4QsjRoUbA%2FTsVJUX%2BpEb%2BBM3S7Y30PzGYmTAAiEAqojbXN8gEfYhZO9IfLvf1%2FPXKEXgSmc23jeH1PhXcbUq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDK9a72j4%2BRK5fX3D4yrcA6IJKr0McyShA8u9QK6RcoW8y7rDGLjS0PBNtIZapIOZXGzv4QYbbyiOsgIIJxtTTNxduZVHG6PMDl6czNFPj2kQf2ZJPw5m2hoyl4HrHrynuSWm6tJ47K%2BFS3DIilzEZ0UTMs8xzufj7OWzXG1gevDQVPG1NB5q8SfUwziodh77NFrypHuLSY1m5AFQLkvzPAJs7yMuuEo2bofvxO%2FfNvT3fPwJebMeF6TmzCw9D3S7FFMuzW3nCZVs4i5bT4GaJ2Q0E1e9T5XtkzqOKe7R6YtEYOKiNCViEeyaT%2BW9rkj0mazzCq%2F085iJwTW%2BTioyAYE%2BD%2BgnZipvlGLS44Jlh824XuR8FbUWObh4GNQUYm5k9iWgFAaSfqHFIQNZn12NbemKNs%2B7cCXNL2khTJUjvA4PI5ErRkXuZ5RHZgv%2BcDTn2y36okUgicuOt0ss98kcfwCO7ilE2wnrLACZgb%2Bi4sdm3zWeGN5MmeYpvUCkfflQD4V8jP7xic6l8VIJUNBHCfvwLThaWHlls%2BFZZnErUpjU8YVFmt%2BkNTCCeM6mo8ir2BLzH90ITkUFX57iRGX6mafups29cFJgrv%2BlrQKolNQDL3SRmx82jcJK%2Fb3FA46fe2Sdvhiwlvcp1UlgMK%2Bgss4GOqUBFpODCy063JrG7xJ%2BTvci8iu4XzKrJBiWP77ILG91bD8bbglKMWhPKiXR8ljSjw%2FX7YRk%2FUv42oOkz2jrWvWRhAZeXQGjXoL8eHMMUEYRutP9JTGwX54rDJNxdMHpTdDieIaXmNSw7G3cu7e67wy9uKbWHnKH%2FwyBUu6YNPpNXyYX9HE5kS5z10K5c1ECAO2Nc%2BVxBmjWlG8c1ZkpB86IzPVbrXGe&X-Amz-Signature=533f4de90eca73dc016da4405ebc3d6be3ac8e515d92cdf8ac46dcd65ca469f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLBDT2DZ%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpdfoVJ4QsjRoUbA%2FTsVJUX%2BpEb%2BBM3S7Y30PzGYmTAAiEAqojbXN8gEfYhZO9IfLvf1%2FPXKEXgSmc23jeH1PhXcbUq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDK9a72j4%2BRK5fX3D4yrcA6IJKr0McyShA8u9QK6RcoW8y7rDGLjS0PBNtIZapIOZXGzv4QYbbyiOsgIIJxtTTNxduZVHG6PMDl6czNFPj2kQf2ZJPw5m2hoyl4HrHrynuSWm6tJ47K%2BFS3DIilzEZ0UTMs8xzufj7OWzXG1gevDQVPG1NB5q8SfUwziodh77NFrypHuLSY1m5AFQLkvzPAJs7yMuuEo2bofvxO%2FfNvT3fPwJebMeF6TmzCw9D3S7FFMuzW3nCZVs4i5bT4GaJ2Q0E1e9T5XtkzqOKe7R6YtEYOKiNCViEeyaT%2BW9rkj0mazzCq%2F085iJwTW%2BTioyAYE%2BD%2BgnZipvlGLS44Jlh824XuR8FbUWObh4GNQUYm5k9iWgFAaSfqHFIQNZn12NbemKNs%2B7cCXNL2khTJUjvA4PI5ErRkXuZ5RHZgv%2BcDTn2y36okUgicuOt0ss98kcfwCO7ilE2wnrLACZgb%2Bi4sdm3zWeGN5MmeYpvUCkfflQD4V8jP7xic6l8VIJUNBHCfvwLThaWHlls%2BFZZnErUpjU8YVFmt%2BkNTCCeM6mo8ir2BLzH90ITkUFX57iRGX6mafups29cFJgrv%2BlrQKolNQDL3SRmx82jcJK%2Fb3FA46fe2Sdvhiwlvcp1UlgMK%2Bgss4GOqUBFpODCy063JrG7xJ%2BTvci8iu4XzKrJBiWP77ILG91bD8bbglKMWhPKiXR8ljSjw%2FX7YRk%2FUv42oOkz2jrWvWRhAZeXQGjXoL8eHMMUEYRutP9JTGwX54rDJNxdMHpTdDieIaXmNSw7G3cu7e67wy9uKbWHnKH%2FwyBUu6YNPpNXyYX9HE5kS5z10K5c1ECAO2Nc%2BVxBmjWlG8c1ZkpB86IzPVbrXGe&X-Amz-Signature=94a4af52cfc50b314d789758ae415d7c7371611ac69be43ad7e7c44bc84f0d20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLBDT2DZ%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpdfoVJ4QsjRoUbA%2FTsVJUX%2BpEb%2BBM3S7Y30PzGYmTAAiEAqojbXN8gEfYhZO9IfLvf1%2FPXKEXgSmc23jeH1PhXcbUq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDK9a72j4%2BRK5fX3D4yrcA6IJKr0McyShA8u9QK6RcoW8y7rDGLjS0PBNtIZapIOZXGzv4QYbbyiOsgIIJxtTTNxduZVHG6PMDl6czNFPj2kQf2ZJPw5m2hoyl4HrHrynuSWm6tJ47K%2BFS3DIilzEZ0UTMs8xzufj7OWzXG1gevDQVPG1NB5q8SfUwziodh77NFrypHuLSY1m5AFQLkvzPAJs7yMuuEo2bofvxO%2FfNvT3fPwJebMeF6TmzCw9D3S7FFMuzW3nCZVs4i5bT4GaJ2Q0E1e9T5XtkzqOKe7R6YtEYOKiNCViEeyaT%2BW9rkj0mazzCq%2F085iJwTW%2BTioyAYE%2BD%2BgnZipvlGLS44Jlh824XuR8FbUWObh4GNQUYm5k9iWgFAaSfqHFIQNZn12NbemKNs%2B7cCXNL2khTJUjvA4PI5ErRkXuZ5RHZgv%2BcDTn2y36okUgicuOt0ss98kcfwCO7ilE2wnrLACZgb%2Bi4sdm3zWeGN5MmeYpvUCkfflQD4V8jP7xic6l8VIJUNBHCfvwLThaWHlls%2BFZZnErUpjU8YVFmt%2BkNTCCeM6mo8ir2BLzH90ITkUFX57iRGX6mafups29cFJgrv%2BlrQKolNQDL3SRmx82jcJK%2Fb3FA46fe2Sdvhiwlvcp1UlgMK%2Bgss4GOqUBFpODCy063JrG7xJ%2BTvci8iu4XzKrJBiWP77ILG91bD8bbglKMWhPKiXR8ljSjw%2FX7YRk%2FUv42oOkz2jrWvWRhAZeXQGjXoL8eHMMUEYRutP9JTGwX54rDJNxdMHpTdDieIaXmNSw7G3cu7e67wy9uKbWHnKH%2FwyBUu6YNPpNXyYX9HE5kS5z10K5c1ECAO2Nc%2BVxBmjWlG8c1ZkpB86IzPVbrXGe&X-Amz-Signature=052f36df4f5a5794c5f9c5619248179a7c0b5bbba7d089065ae1a09d444ce651&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLBDT2DZ%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpdfoVJ4QsjRoUbA%2FTsVJUX%2BpEb%2BBM3S7Y30PzGYmTAAiEAqojbXN8gEfYhZO9IfLvf1%2FPXKEXgSmc23jeH1PhXcbUq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDK9a72j4%2BRK5fX3D4yrcA6IJKr0McyShA8u9QK6RcoW8y7rDGLjS0PBNtIZapIOZXGzv4QYbbyiOsgIIJxtTTNxduZVHG6PMDl6czNFPj2kQf2ZJPw5m2hoyl4HrHrynuSWm6tJ47K%2BFS3DIilzEZ0UTMs8xzufj7OWzXG1gevDQVPG1NB5q8SfUwziodh77NFrypHuLSY1m5AFQLkvzPAJs7yMuuEo2bofvxO%2FfNvT3fPwJebMeF6TmzCw9D3S7FFMuzW3nCZVs4i5bT4GaJ2Q0E1e9T5XtkzqOKe7R6YtEYOKiNCViEeyaT%2BW9rkj0mazzCq%2F085iJwTW%2BTioyAYE%2BD%2BgnZipvlGLS44Jlh824XuR8FbUWObh4GNQUYm5k9iWgFAaSfqHFIQNZn12NbemKNs%2B7cCXNL2khTJUjvA4PI5ErRkXuZ5RHZgv%2BcDTn2y36okUgicuOt0ss98kcfwCO7ilE2wnrLACZgb%2Bi4sdm3zWeGN5MmeYpvUCkfflQD4V8jP7xic6l8VIJUNBHCfvwLThaWHlls%2BFZZnErUpjU8YVFmt%2BkNTCCeM6mo8ir2BLzH90ITkUFX57iRGX6mafups29cFJgrv%2BlrQKolNQDL3SRmx82jcJK%2Fb3FA46fe2Sdvhiwlvcp1UlgMK%2Bgss4GOqUBFpODCy063JrG7xJ%2BTvci8iu4XzKrJBiWP77ILG91bD8bbglKMWhPKiXR8ljSjw%2FX7YRk%2FUv42oOkz2jrWvWRhAZeXQGjXoL8eHMMUEYRutP9JTGwX54rDJNxdMHpTdDieIaXmNSw7G3cu7e67wy9uKbWHnKH%2FwyBUu6YNPpNXyYX9HE5kS5z10K5c1ECAO2Nc%2BVxBmjWlG8c1ZkpB86IzPVbrXGe&X-Amz-Signature=887388e0df692851fd8e255975c1e48052b7b103b0124ffb404b88cd9d67817d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLBDT2DZ%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpdfoVJ4QsjRoUbA%2FTsVJUX%2BpEb%2BBM3S7Y30PzGYmTAAiEAqojbXN8gEfYhZO9IfLvf1%2FPXKEXgSmc23jeH1PhXcbUq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDK9a72j4%2BRK5fX3D4yrcA6IJKr0McyShA8u9QK6RcoW8y7rDGLjS0PBNtIZapIOZXGzv4QYbbyiOsgIIJxtTTNxduZVHG6PMDl6czNFPj2kQf2ZJPw5m2hoyl4HrHrynuSWm6tJ47K%2BFS3DIilzEZ0UTMs8xzufj7OWzXG1gevDQVPG1NB5q8SfUwziodh77NFrypHuLSY1m5AFQLkvzPAJs7yMuuEo2bofvxO%2FfNvT3fPwJebMeF6TmzCw9D3S7FFMuzW3nCZVs4i5bT4GaJ2Q0E1e9T5XtkzqOKe7R6YtEYOKiNCViEeyaT%2BW9rkj0mazzCq%2F085iJwTW%2BTioyAYE%2BD%2BgnZipvlGLS44Jlh824XuR8FbUWObh4GNQUYm5k9iWgFAaSfqHFIQNZn12NbemKNs%2B7cCXNL2khTJUjvA4PI5ErRkXuZ5RHZgv%2BcDTn2y36okUgicuOt0ss98kcfwCO7ilE2wnrLACZgb%2Bi4sdm3zWeGN5MmeYpvUCkfflQD4V8jP7xic6l8VIJUNBHCfvwLThaWHlls%2BFZZnErUpjU8YVFmt%2BkNTCCeM6mo8ir2BLzH90ITkUFX57iRGX6mafups29cFJgrv%2BlrQKolNQDL3SRmx82jcJK%2Fb3FA46fe2Sdvhiwlvcp1UlgMK%2Bgss4GOqUBFpODCy063JrG7xJ%2BTvci8iu4XzKrJBiWP77ILG91bD8bbglKMWhPKiXR8ljSjw%2FX7YRk%2FUv42oOkz2jrWvWRhAZeXQGjXoL8eHMMUEYRutP9JTGwX54rDJNxdMHpTdDieIaXmNSw7G3cu7e67wy9uKbWHnKH%2FwyBUu6YNPpNXyYX9HE5kS5z10K5c1ECAO2Nc%2BVxBmjWlG8c1ZkpB86IzPVbrXGe&X-Amz-Signature=54730dfe43c67dff157c13c04a507d59dde017e27f16627e9f666a5c78da57d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLBDT2DZ%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpdfoVJ4QsjRoUbA%2FTsVJUX%2BpEb%2BBM3S7Y30PzGYmTAAiEAqojbXN8gEfYhZO9IfLvf1%2FPXKEXgSmc23jeH1PhXcbUq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDK9a72j4%2BRK5fX3D4yrcA6IJKr0McyShA8u9QK6RcoW8y7rDGLjS0PBNtIZapIOZXGzv4QYbbyiOsgIIJxtTTNxduZVHG6PMDl6czNFPj2kQf2ZJPw5m2hoyl4HrHrynuSWm6tJ47K%2BFS3DIilzEZ0UTMs8xzufj7OWzXG1gevDQVPG1NB5q8SfUwziodh77NFrypHuLSY1m5AFQLkvzPAJs7yMuuEo2bofvxO%2FfNvT3fPwJebMeF6TmzCw9D3S7FFMuzW3nCZVs4i5bT4GaJ2Q0E1e9T5XtkzqOKe7R6YtEYOKiNCViEeyaT%2BW9rkj0mazzCq%2F085iJwTW%2BTioyAYE%2BD%2BgnZipvlGLS44Jlh824XuR8FbUWObh4GNQUYm5k9iWgFAaSfqHFIQNZn12NbemKNs%2B7cCXNL2khTJUjvA4PI5ErRkXuZ5RHZgv%2BcDTn2y36okUgicuOt0ss98kcfwCO7ilE2wnrLACZgb%2Bi4sdm3zWeGN5MmeYpvUCkfflQD4V8jP7xic6l8VIJUNBHCfvwLThaWHlls%2BFZZnErUpjU8YVFmt%2BkNTCCeM6mo8ir2BLzH90ITkUFX57iRGX6mafups29cFJgrv%2BlrQKolNQDL3SRmx82jcJK%2Fb3FA46fe2Sdvhiwlvcp1UlgMK%2Bgss4GOqUBFpODCy063JrG7xJ%2BTvci8iu4XzKrJBiWP77ILG91bD8bbglKMWhPKiXR8ljSjw%2FX7YRk%2FUv42oOkz2jrWvWRhAZeXQGjXoL8eHMMUEYRutP9JTGwX54rDJNxdMHpTdDieIaXmNSw7G3cu7e67wy9uKbWHnKH%2FwyBUu6YNPpNXyYX9HE5kS5z10K5c1ECAO2Nc%2BVxBmjWlG8c1ZkpB86IzPVbrXGe&X-Amz-Signature=26f48461f49d83ecf8d037b2f0e421798b9071f3634356e85f444e93eb0b1e83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLBDT2DZ%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpdfoVJ4QsjRoUbA%2FTsVJUX%2BpEb%2BBM3S7Y30PzGYmTAAiEAqojbXN8gEfYhZO9IfLvf1%2FPXKEXgSmc23jeH1PhXcbUq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDK9a72j4%2BRK5fX3D4yrcA6IJKr0McyShA8u9QK6RcoW8y7rDGLjS0PBNtIZapIOZXGzv4QYbbyiOsgIIJxtTTNxduZVHG6PMDl6czNFPj2kQf2ZJPw5m2hoyl4HrHrynuSWm6tJ47K%2BFS3DIilzEZ0UTMs8xzufj7OWzXG1gevDQVPG1NB5q8SfUwziodh77NFrypHuLSY1m5AFQLkvzPAJs7yMuuEo2bofvxO%2FfNvT3fPwJebMeF6TmzCw9D3S7FFMuzW3nCZVs4i5bT4GaJ2Q0E1e9T5XtkzqOKe7R6YtEYOKiNCViEeyaT%2BW9rkj0mazzCq%2F085iJwTW%2BTioyAYE%2BD%2BgnZipvlGLS44Jlh824XuR8FbUWObh4GNQUYm5k9iWgFAaSfqHFIQNZn12NbemKNs%2B7cCXNL2khTJUjvA4PI5ErRkXuZ5RHZgv%2BcDTn2y36okUgicuOt0ss98kcfwCO7ilE2wnrLACZgb%2Bi4sdm3zWeGN5MmeYpvUCkfflQD4V8jP7xic6l8VIJUNBHCfvwLThaWHlls%2BFZZnErUpjU8YVFmt%2BkNTCCeM6mo8ir2BLzH90ITkUFX57iRGX6mafups29cFJgrv%2BlrQKolNQDL3SRmx82jcJK%2Fb3FA46fe2Sdvhiwlvcp1UlgMK%2Bgss4GOqUBFpODCy063JrG7xJ%2BTvci8iu4XzKrJBiWP77ILG91bD8bbglKMWhPKiXR8ljSjw%2FX7YRk%2FUv42oOkz2jrWvWRhAZeXQGjXoL8eHMMUEYRutP9JTGwX54rDJNxdMHpTdDieIaXmNSw7G3cu7e67wy9uKbWHnKH%2FwyBUu6YNPpNXyYX9HE5kS5z10K5c1ECAO2Nc%2BVxBmjWlG8c1ZkpB86IzPVbrXGe&X-Amz-Signature=5cc07f489014489e380dd25b49911fb39d6a5f07b0f7aa82228191ece723b5b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

