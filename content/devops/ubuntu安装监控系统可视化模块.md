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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOSDLDQ4%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID7mfy8K5JLuknLJ4fzag1W72w2v0FbwIKg01JV5Ej0iAiACSsDL%2BFsZ2eqgzgDKSBRdPQ%2BZpXy60blPvYlVc14UJyqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQhCd%2BLZVHhaehFrOKtwDHeUDrbuZBEW1k%2B%2FImK2sadpFSUNKJCeyxdGtjRaDQmQeVlN%2BEjLPMi%2FB36G4M3gaoRVVizCsOOxnaY%2BCEloNLmTatMHX4wgaZTNvAW%2ByBBToX%2BbWqSrnt%2BJjhTlzk8rhqg3eOydyAEtFrSNfhjTri9V51tNEAb2%2BcxJg0BD%2BwUldzD4ecER7PqQWtGna417RPUrjGK2JDvbFmCHzcLC%2B6ySUQ%2FtXQkdi53Px39frBPg5GzgYPQUdybcSkOahu1wowM%2FXraCGvuvEb9SS1D%2FjOfExcLiVQ1A42%2FoAmNLWZpJ5vVLGU9MyoK%2FTx0puule3QG3mLHekgirvAJkI7anQGYq5CBzLPLtQy3vHNmUH42fttaUfpGTc%2FEvJ5m%2BRU1iw%2BTw37AYp%2BC1s1aDYSkLwM2WzxQKi1aPbT7qZI1umjC%2FFB91UxBjdJjnVyORvoGJLjS7wWHL3nvB2agi42enDz4rzd3qKMK85vlbCdF7rMVv6MPn5RpX8CH4xdG3ydFchkev36kmqswA0eNtN5hiGn3T%2FZDmUeme5X%2BATOX8v9DQQOjAMY%2B7BVdU5gpr8zmytZ6VRxw%2FKBfFzoxAgKNDSg5D8kytQdf6xQETVrUC1vqxL%2FO9P78%2BUkvgNQ2Iw%2FOOeyQY6pgGGvOLyXy%2FRUn2eVZBW1dRKUtIR1qMhWy%2BglUWHD0RxqUVhr6sI%2FsPJXJr8fGAHpVx67dIe1Kr85kBUcTGpd9bSY6VpwBjoJaon4Mh4boAF%2FNg8fcEtvh8cb2bokuujtTNunXr8lnmiafV8N07JN7FjET1EmhF0Dtb4%2F9pYc9H9rZqIqOvvqQ5sE9RCcIo%2Bwru7HVifIH%2BdKkBNquobr9IVzWDPulBp&X-Amz-Signature=f71190623319c1e16289a7c6802c90260442ff8ee8e5ba8d37ac58c1b7b51486&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOSDLDQ4%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID7mfy8K5JLuknLJ4fzag1W72w2v0FbwIKg01JV5Ej0iAiACSsDL%2BFsZ2eqgzgDKSBRdPQ%2BZpXy60blPvYlVc14UJyqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQhCd%2BLZVHhaehFrOKtwDHeUDrbuZBEW1k%2B%2FImK2sadpFSUNKJCeyxdGtjRaDQmQeVlN%2BEjLPMi%2FB36G4M3gaoRVVizCsOOxnaY%2BCEloNLmTatMHX4wgaZTNvAW%2ByBBToX%2BbWqSrnt%2BJjhTlzk8rhqg3eOydyAEtFrSNfhjTri9V51tNEAb2%2BcxJg0BD%2BwUldzD4ecER7PqQWtGna417RPUrjGK2JDvbFmCHzcLC%2B6ySUQ%2FtXQkdi53Px39frBPg5GzgYPQUdybcSkOahu1wowM%2FXraCGvuvEb9SS1D%2FjOfExcLiVQ1A42%2FoAmNLWZpJ5vVLGU9MyoK%2FTx0puule3QG3mLHekgirvAJkI7anQGYq5CBzLPLtQy3vHNmUH42fttaUfpGTc%2FEvJ5m%2BRU1iw%2BTw37AYp%2BC1s1aDYSkLwM2WzxQKi1aPbT7qZI1umjC%2FFB91UxBjdJjnVyORvoGJLjS7wWHL3nvB2agi42enDz4rzd3qKMK85vlbCdF7rMVv6MPn5RpX8CH4xdG3ydFchkev36kmqswA0eNtN5hiGn3T%2FZDmUeme5X%2BATOX8v9DQQOjAMY%2B7BVdU5gpr8zmytZ6VRxw%2FKBfFzoxAgKNDSg5D8kytQdf6xQETVrUC1vqxL%2FO9P78%2BUkvgNQ2Iw%2FOOeyQY6pgGGvOLyXy%2FRUn2eVZBW1dRKUtIR1qMhWy%2BglUWHD0RxqUVhr6sI%2FsPJXJr8fGAHpVx67dIe1Kr85kBUcTGpd9bSY6VpwBjoJaon4Mh4boAF%2FNg8fcEtvh8cb2bokuujtTNunXr8lnmiafV8N07JN7FjET1EmhF0Dtb4%2F9pYc9H9rZqIqOvvqQ5sE9RCcIo%2Bwru7HVifIH%2BdKkBNquobr9IVzWDPulBp&X-Amz-Signature=938628ab8bf0cdaf769ff17c0c476c590f0d64538724234e33c4b183e7514d1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOSDLDQ4%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID7mfy8K5JLuknLJ4fzag1W72w2v0FbwIKg01JV5Ej0iAiACSsDL%2BFsZ2eqgzgDKSBRdPQ%2BZpXy60blPvYlVc14UJyqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQhCd%2BLZVHhaehFrOKtwDHeUDrbuZBEW1k%2B%2FImK2sadpFSUNKJCeyxdGtjRaDQmQeVlN%2BEjLPMi%2FB36G4M3gaoRVVizCsOOxnaY%2BCEloNLmTatMHX4wgaZTNvAW%2ByBBToX%2BbWqSrnt%2BJjhTlzk8rhqg3eOydyAEtFrSNfhjTri9V51tNEAb2%2BcxJg0BD%2BwUldzD4ecER7PqQWtGna417RPUrjGK2JDvbFmCHzcLC%2B6ySUQ%2FtXQkdi53Px39frBPg5GzgYPQUdybcSkOahu1wowM%2FXraCGvuvEb9SS1D%2FjOfExcLiVQ1A42%2FoAmNLWZpJ5vVLGU9MyoK%2FTx0puule3QG3mLHekgirvAJkI7anQGYq5CBzLPLtQy3vHNmUH42fttaUfpGTc%2FEvJ5m%2BRU1iw%2BTw37AYp%2BC1s1aDYSkLwM2WzxQKi1aPbT7qZI1umjC%2FFB91UxBjdJjnVyORvoGJLjS7wWHL3nvB2agi42enDz4rzd3qKMK85vlbCdF7rMVv6MPn5RpX8CH4xdG3ydFchkev36kmqswA0eNtN5hiGn3T%2FZDmUeme5X%2BATOX8v9DQQOjAMY%2B7BVdU5gpr8zmytZ6VRxw%2FKBfFzoxAgKNDSg5D8kytQdf6xQETVrUC1vqxL%2FO9P78%2BUkvgNQ2Iw%2FOOeyQY6pgGGvOLyXy%2FRUn2eVZBW1dRKUtIR1qMhWy%2BglUWHD0RxqUVhr6sI%2FsPJXJr8fGAHpVx67dIe1Kr85kBUcTGpd9bSY6VpwBjoJaon4Mh4boAF%2FNg8fcEtvh8cb2bokuujtTNunXr8lnmiafV8N07JN7FjET1EmhF0Dtb4%2F9pYc9H9rZqIqOvvqQ5sE9RCcIo%2Bwru7HVifIH%2BdKkBNquobr9IVzWDPulBp&X-Amz-Signature=3e838efb4711d1132423df83045412ab5b06fbd8f6b7d8c14a8234ce433f3c29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOSDLDQ4%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID7mfy8K5JLuknLJ4fzag1W72w2v0FbwIKg01JV5Ej0iAiACSsDL%2BFsZ2eqgzgDKSBRdPQ%2BZpXy60blPvYlVc14UJyqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQhCd%2BLZVHhaehFrOKtwDHeUDrbuZBEW1k%2B%2FImK2sadpFSUNKJCeyxdGtjRaDQmQeVlN%2BEjLPMi%2FB36G4M3gaoRVVizCsOOxnaY%2BCEloNLmTatMHX4wgaZTNvAW%2ByBBToX%2BbWqSrnt%2BJjhTlzk8rhqg3eOydyAEtFrSNfhjTri9V51tNEAb2%2BcxJg0BD%2BwUldzD4ecER7PqQWtGna417RPUrjGK2JDvbFmCHzcLC%2B6ySUQ%2FtXQkdi53Px39frBPg5GzgYPQUdybcSkOahu1wowM%2FXraCGvuvEb9SS1D%2FjOfExcLiVQ1A42%2FoAmNLWZpJ5vVLGU9MyoK%2FTx0puule3QG3mLHekgirvAJkI7anQGYq5CBzLPLtQy3vHNmUH42fttaUfpGTc%2FEvJ5m%2BRU1iw%2BTw37AYp%2BC1s1aDYSkLwM2WzxQKi1aPbT7qZI1umjC%2FFB91UxBjdJjnVyORvoGJLjS7wWHL3nvB2agi42enDz4rzd3qKMK85vlbCdF7rMVv6MPn5RpX8CH4xdG3ydFchkev36kmqswA0eNtN5hiGn3T%2FZDmUeme5X%2BATOX8v9DQQOjAMY%2B7BVdU5gpr8zmytZ6VRxw%2FKBfFzoxAgKNDSg5D8kytQdf6xQETVrUC1vqxL%2FO9P78%2BUkvgNQ2Iw%2FOOeyQY6pgGGvOLyXy%2FRUn2eVZBW1dRKUtIR1qMhWy%2BglUWHD0RxqUVhr6sI%2FsPJXJr8fGAHpVx67dIe1Kr85kBUcTGpd9bSY6VpwBjoJaon4Mh4boAF%2FNg8fcEtvh8cb2bokuujtTNunXr8lnmiafV8N07JN7FjET1EmhF0Dtb4%2F9pYc9H9rZqIqOvvqQ5sE9RCcIo%2Bwru7HVifIH%2BdKkBNquobr9IVzWDPulBp&X-Amz-Signature=46ee1771a6d2c2c5d791d8cbd16c5197b30af377b823909ba7c620a4c5ecbf02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOSDLDQ4%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID7mfy8K5JLuknLJ4fzag1W72w2v0FbwIKg01JV5Ej0iAiACSsDL%2BFsZ2eqgzgDKSBRdPQ%2BZpXy60blPvYlVc14UJyqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQhCd%2BLZVHhaehFrOKtwDHeUDrbuZBEW1k%2B%2FImK2sadpFSUNKJCeyxdGtjRaDQmQeVlN%2BEjLPMi%2FB36G4M3gaoRVVizCsOOxnaY%2BCEloNLmTatMHX4wgaZTNvAW%2ByBBToX%2BbWqSrnt%2BJjhTlzk8rhqg3eOydyAEtFrSNfhjTri9V51tNEAb2%2BcxJg0BD%2BwUldzD4ecER7PqQWtGna417RPUrjGK2JDvbFmCHzcLC%2B6ySUQ%2FtXQkdi53Px39frBPg5GzgYPQUdybcSkOahu1wowM%2FXraCGvuvEb9SS1D%2FjOfExcLiVQ1A42%2FoAmNLWZpJ5vVLGU9MyoK%2FTx0puule3QG3mLHekgirvAJkI7anQGYq5CBzLPLtQy3vHNmUH42fttaUfpGTc%2FEvJ5m%2BRU1iw%2BTw37AYp%2BC1s1aDYSkLwM2WzxQKi1aPbT7qZI1umjC%2FFB91UxBjdJjnVyORvoGJLjS7wWHL3nvB2agi42enDz4rzd3qKMK85vlbCdF7rMVv6MPn5RpX8CH4xdG3ydFchkev36kmqswA0eNtN5hiGn3T%2FZDmUeme5X%2BATOX8v9DQQOjAMY%2B7BVdU5gpr8zmytZ6VRxw%2FKBfFzoxAgKNDSg5D8kytQdf6xQETVrUC1vqxL%2FO9P78%2BUkvgNQ2Iw%2FOOeyQY6pgGGvOLyXy%2FRUn2eVZBW1dRKUtIR1qMhWy%2BglUWHD0RxqUVhr6sI%2FsPJXJr8fGAHpVx67dIe1Kr85kBUcTGpd9bSY6VpwBjoJaon4Mh4boAF%2FNg8fcEtvh8cb2bokuujtTNunXr8lnmiafV8N07JN7FjET1EmhF0Dtb4%2F9pYc9H9rZqIqOvvqQ5sE9RCcIo%2Bwru7HVifIH%2BdKkBNquobr9IVzWDPulBp&X-Amz-Signature=627c08fa481f505c3bf093a4f996afaa4ba5adb24cbcb5c861c4158f01e86d0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOSDLDQ4%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID7mfy8K5JLuknLJ4fzag1W72w2v0FbwIKg01JV5Ej0iAiACSsDL%2BFsZ2eqgzgDKSBRdPQ%2BZpXy60blPvYlVc14UJyqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQhCd%2BLZVHhaehFrOKtwDHeUDrbuZBEW1k%2B%2FImK2sadpFSUNKJCeyxdGtjRaDQmQeVlN%2BEjLPMi%2FB36G4M3gaoRVVizCsOOxnaY%2BCEloNLmTatMHX4wgaZTNvAW%2ByBBToX%2BbWqSrnt%2BJjhTlzk8rhqg3eOydyAEtFrSNfhjTri9V51tNEAb2%2BcxJg0BD%2BwUldzD4ecER7PqQWtGna417RPUrjGK2JDvbFmCHzcLC%2B6ySUQ%2FtXQkdi53Px39frBPg5GzgYPQUdybcSkOahu1wowM%2FXraCGvuvEb9SS1D%2FjOfExcLiVQ1A42%2FoAmNLWZpJ5vVLGU9MyoK%2FTx0puule3QG3mLHekgirvAJkI7anQGYq5CBzLPLtQy3vHNmUH42fttaUfpGTc%2FEvJ5m%2BRU1iw%2BTw37AYp%2BC1s1aDYSkLwM2WzxQKi1aPbT7qZI1umjC%2FFB91UxBjdJjnVyORvoGJLjS7wWHL3nvB2agi42enDz4rzd3qKMK85vlbCdF7rMVv6MPn5RpX8CH4xdG3ydFchkev36kmqswA0eNtN5hiGn3T%2FZDmUeme5X%2BATOX8v9DQQOjAMY%2B7BVdU5gpr8zmytZ6VRxw%2FKBfFzoxAgKNDSg5D8kytQdf6xQETVrUC1vqxL%2FO9P78%2BUkvgNQ2Iw%2FOOeyQY6pgGGvOLyXy%2FRUn2eVZBW1dRKUtIR1qMhWy%2BglUWHD0RxqUVhr6sI%2FsPJXJr8fGAHpVx67dIe1Kr85kBUcTGpd9bSY6VpwBjoJaon4Mh4boAF%2FNg8fcEtvh8cb2bokuujtTNunXr8lnmiafV8N07JN7FjET1EmhF0Dtb4%2F9pYc9H9rZqIqOvvqQ5sE9RCcIo%2Bwru7HVifIH%2BdKkBNquobr9IVzWDPulBp&X-Amz-Signature=c43d4469cd1b9f0f7f6720e1224cdceb215b5ea7859dc571c96f386c997b23a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOSDLDQ4%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID7mfy8K5JLuknLJ4fzag1W72w2v0FbwIKg01JV5Ej0iAiACSsDL%2BFsZ2eqgzgDKSBRdPQ%2BZpXy60blPvYlVc14UJyqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQhCd%2BLZVHhaehFrOKtwDHeUDrbuZBEW1k%2B%2FImK2sadpFSUNKJCeyxdGtjRaDQmQeVlN%2BEjLPMi%2FB36G4M3gaoRVVizCsOOxnaY%2BCEloNLmTatMHX4wgaZTNvAW%2ByBBToX%2BbWqSrnt%2BJjhTlzk8rhqg3eOydyAEtFrSNfhjTri9V51tNEAb2%2BcxJg0BD%2BwUldzD4ecER7PqQWtGna417RPUrjGK2JDvbFmCHzcLC%2B6ySUQ%2FtXQkdi53Px39frBPg5GzgYPQUdybcSkOahu1wowM%2FXraCGvuvEb9SS1D%2FjOfExcLiVQ1A42%2FoAmNLWZpJ5vVLGU9MyoK%2FTx0puule3QG3mLHekgirvAJkI7anQGYq5CBzLPLtQy3vHNmUH42fttaUfpGTc%2FEvJ5m%2BRU1iw%2BTw37AYp%2BC1s1aDYSkLwM2WzxQKi1aPbT7qZI1umjC%2FFB91UxBjdJjnVyORvoGJLjS7wWHL3nvB2agi42enDz4rzd3qKMK85vlbCdF7rMVv6MPn5RpX8CH4xdG3ydFchkev36kmqswA0eNtN5hiGn3T%2FZDmUeme5X%2BATOX8v9DQQOjAMY%2B7BVdU5gpr8zmytZ6VRxw%2FKBfFzoxAgKNDSg5D8kytQdf6xQETVrUC1vqxL%2FO9P78%2BUkvgNQ2Iw%2FOOeyQY6pgGGvOLyXy%2FRUn2eVZBW1dRKUtIR1qMhWy%2BglUWHD0RxqUVhr6sI%2FsPJXJr8fGAHpVx67dIe1Kr85kBUcTGpd9bSY6VpwBjoJaon4Mh4boAF%2FNg8fcEtvh8cb2bokuujtTNunXr8lnmiafV8N07JN7FjET1EmhF0Dtb4%2F9pYc9H9rZqIqOvvqQ5sE9RCcIo%2Bwru7HVifIH%2BdKkBNquobr9IVzWDPulBp&X-Amz-Signature=a629b063f8f9f19324a42059f30eeb809cf9593cf37e1c10f51aedc137b76bd6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

