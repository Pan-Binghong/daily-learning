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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXSN3STQ%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQCqYtzIT21QXIH0feLwPMnZnKHer%2FqykoQYl6bAOjGu4AIgTUqCBOA%2Bp3GqI%2B1TA7qZVHqS317igrBTc8%2FOAe31OvMq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDEb5raJ6y07HEY0%2BqSrcA%2BD8MWgoRd6qvsD3xMnzTE3oPyzBxOQIIxVpJdyqEY%2FJobZSL9Ho%2F31pwqsPK5MZP7LcNp%2BXFLKTsyXnZjilurGyyZq643ICN9gzce1hGyn71NLdZMdC72D%2FaglDoQ0mC%2BbwW7kGdA8wrEyPak0wOzZ4XL47V1Cv1WSiIZkOshqdx6G9HSxFoIDtKRdmVcY0KPycsSKIl9j6FanHSz%2BlHktUT5tlMJmQF4dNic2ZmVhpw2t4MIqy6Fl58ZSACNt7Iiq2fUtsscJ61iS1H%2BTJAi3ziqaDhWl6gFmhsXfpikjWE6B45PAXSHpQ86LtvRu3G24yc4EqTngrX8YRyvZ%2BkEjR%2FRGPdJbfxSHaab2kbU0Xij30T64H6uHbC9iqsOx3Wr7bSlJrIcSWR05%2FFP2QS5Pt%2BEncQWZC4%2B%2FOnbcrVS2tsFWSxzjEGwvIryC1W4qpLcMD98yTzL3OU30FOk0w98RyBk%2FBTIGIkPO56sj%2BtUE9RijUnjAhk4vUQ8FLHeprlIxXO2PKxT9PeKNQJ5%2BMLDrTAwMPv1tHplkLx38gxKmEqeKzTr%2BDlH3q%2FZYF7V%2BBVd8PSWybscBPnvVWZsjsgoL4aq%2B6xmNVHjodeK0Su2%2FbkQ19EjSsGZfVfSoVMNqTkMwGOqUBpWNFJVe%2FHBVlUYbkHAbDkC%2FXk6QydV11dimBSA9PGb1P2y%2Fm3HbNND2Sj6jDTNt622VShZi3Sv9Z2gHAtxfZEfS2%2Fb8YzOcsycqZZmBt%2FgjfpmAHSRUNmPyn8BI%2FBfVMgdusuuGhF1dU3p%2FNYvIkxIX7LpqxkK2pByuB7Fw5cKZ9wMVCv6LMwHsYwHrqeK9miwu89gCBcGJARAoPxIVDKdmUL75k&X-Amz-Signature=adfd65569906e2d6716d1466e0ac3887dd8e998dce43fbbec3ba58a03379cd33&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXSN3STQ%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQCqYtzIT21QXIH0feLwPMnZnKHer%2FqykoQYl6bAOjGu4AIgTUqCBOA%2Bp3GqI%2B1TA7qZVHqS317igrBTc8%2FOAe31OvMq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDEb5raJ6y07HEY0%2BqSrcA%2BD8MWgoRd6qvsD3xMnzTE3oPyzBxOQIIxVpJdyqEY%2FJobZSL9Ho%2F31pwqsPK5MZP7LcNp%2BXFLKTsyXnZjilurGyyZq643ICN9gzce1hGyn71NLdZMdC72D%2FaglDoQ0mC%2BbwW7kGdA8wrEyPak0wOzZ4XL47V1Cv1WSiIZkOshqdx6G9HSxFoIDtKRdmVcY0KPycsSKIl9j6FanHSz%2BlHktUT5tlMJmQF4dNic2ZmVhpw2t4MIqy6Fl58ZSACNt7Iiq2fUtsscJ61iS1H%2BTJAi3ziqaDhWl6gFmhsXfpikjWE6B45PAXSHpQ86LtvRu3G24yc4EqTngrX8YRyvZ%2BkEjR%2FRGPdJbfxSHaab2kbU0Xij30T64H6uHbC9iqsOx3Wr7bSlJrIcSWR05%2FFP2QS5Pt%2BEncQWZC4%2B%2FOnbcrVS2tsFWSxzjEGwvIryC1W4qpLcMD98yTzL3OU30FOk0w98RyBk%2FBTIGIkPO56sj%2BtUE9RijUnjAhk4vUQ8FLHeprlIxXO2PKxT9PeKNQJ5%2BMLDrTAwMPv1tHplkLx38gxKmEqeKzTr%2BDlH3q%2FZYF7V%2BBVd8PSWybscBPnvVWZsjsgoL4aq%2B6xmNVHjodeK0Su2%2FbkQ19EjSsGZfVfSoVMNqTkMwGOqUBpWNFJVe%2FHBVlUYbkHAbDkC%2FXk6QydV11dimBSA9PGb1P2y%2Fm3HbNND2Sj6jDTNt622VShZi3Sv9Z2gHAtxfZEfS2%2Fb8YzOcsycqZZmBt%2FgjfpmAHSRUNmPyn8BI%2FBfVMgdusuuGhF1dU3p%2FNYvIkxIX7LpqxkK2pByuB7Fw5cKZ9wMVCv6LMwHsYwHrqeK9miwu89gCBcGJARAoPxIVDKdmUL75k&X-Amz-Signature=066cc52280548dc055dfaef5ee4fc22f2a3ee64613da5f35c2aa63c2755e9097&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXSN3STQ%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQCqYtzIT21QXIH0feLwPMnZnKHer%2FqykoQYl6bAOjGu4AIgTUqCBOA%2Bp3GqI%2B1TA7qZVHqS317igrBTc8%2FOAe31OvMq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDEb5raJ6y07HEY0%2BqSrcA%2BD8MWgoRd6qvsD3xMnzTE3oPyzBxOQIIxVpJdyqEY%2FJobZSL9Ho%2F31pwqsPK5MZP7LcNp%2BXFLKTsyXnZjilurGyyZq643ICN9gzce1hGyn71NLdZMdC72D%2FaglDoQ0mC%2BbwW7kGdA8wrEyPak0wOzZ4XL47V1Cv1WSiIZkOshqdx6G9HSxFoIDtKRdmVcY0KPycsSKIl9j6FanHSz%2BlHktUT5tlMJmQF4dNic2ZmVhpw2t4MIqy6Fl58ZSACNt7Iiq2fUtsscJ61iS1H%2BTJAi3ziqaDhWl6gFmhsXfpikjWE6B45PAXSHpQ86LtvRu3G24yc4EqTngrX8YRyvZ%2BkEjR%2FRGPdJbfxSHaab2kbU0Xij30T64H6uHbC9iqsOx3Wr7bSlJrIcSWR05%2FFP2QS5Pt%2BEncQWZC4%2B%2FOnbcrVS2tsFWSxzjEGwvIryC1W4qpLcMD98yTzL3OU30FOk0w98RyBk%2FBTIGIkPO56sj%2BtUE9RijUnjAhk4vUQ8FLHeprlIxXO2PKxT9PeKNQJ5%2BMLDrTAwMPv1tHplkLx38gxKmEqeKzTr%2BDlH3q%2FZYF7V%2BBVd8PSWybscBPnvVWZsjsgoL4aq%2B6xmNVHjodeK0Su2%2FbkQ19EjSsGZfVfSoVMNqTkMwGOqUBpWNFJVe%2FHBVlUYbkHAbDkC%2FXk6QydV11dimBSA9PGb1P2y%2Fm3HbNND2Sj6jDTNt622VShZi3Sv9Z2gHAtxfZEfS2%2Fb8YzOcsycqZZmBt%2FgjfpmAHSRUNmPyn8BI%2FBfVMgdusuuGhF1dU3p%2FNYvIkxIX7LpqxkK2pByuB7Fw5cKZ9wMVCv6LMwHsYwHrqeK9miwu89gCBcGJARAoPxIVDKdmUL75k&X-Amz-Signature=ae1bc6b950234cb709fdf2dbe3a39114a08ec5e88e61339c6d2fddf4b839043f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXSN3STQ%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQCqYtzIT21QXIH0feLwPMnZnKHer%2FqykoQYl6bAOjGu4AIgTUqCBOA%2Bp3GqI%2B1TA7qZVHqS317igrBTc8%2FOAe31OvMq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDEb5raJ6y07HEY0%2BqSrcA%2BD8MWgoRd6qvsD3xMnzTE3oPyzBxOQIIxVpJdyqEY%2FJobZSL9Ho%2F31pwqsPK5MZP7LcNp%2BXFLKTsyXnZjilurGyyZq643ICN9gzce1hGyn71NLdZMdC72D%2FaglDoQ0mC%2BbwW7kGdA8wrEyPak0wOzZ4XL47V1Cv1WSiIZkOshqdx6G9HSxFoIDtKRdmVcY0KPycsSKIl9j6FanHSz%2BlHktUT5tlMJmQF4dNic2ZmVhpw2t4MIqy6Fl58ZSACNt7Iiq2fUtsscJ61iS1H%2BTJAi3ziqaDhWl6gFmhsXfpikjWE6B45PAXSHpQ86LtvRu3G24yc4EqTngrX8YRyvZ%2BkEjR%2FRGPdJbfxSHaab2kbU0Xij30T64H6uHbC9iqsOx3Wr7bSlJrIcSWR05%2FFP2QS5Pt%2BEncQWZC4%2B%2FOnbcrVS2tsFWSxzjEGwvIryC1W4qpLcMD98yTzL3OU30FOk0w98RyBk%2FBTIGIkPO56sj%2BtUE9RijUnjAhk4vUQ8FLHeprlIxXO2PKxT9PeKNQJ5%2BMLDrTAwMPv1tHplkLx38gxKmEqeKzTr%2BDlH3q%2FZYF7V%2BBVd8PSWybscBPnvVWZsjsgoL4aq%2B6xmNVHjodeK0Su2%2FbkQ19EjSsGZfVfSoVMNqTkMwGOqUBpWNFJVe%2FHBVlUYbkHAbDkC%2FXk6QydV11dimBSA9PGb1P2y%2Fm3HbNND2Sj6jDTNt622VShZi3Sv9Z2gHAtxfZEfS2%2Fb8YzOcsycqZZmBt%2FgjfpmAHSRUNmPyn8BI%2FBfVMgdusuuGhF1dU3p%2FNYvIkxIX7LpqxkK2pByuB7Fw5cKZ9wMVCv6LMwHsYwHrqeK9miwu89gCBcGJARAoPxIVDKdmUL75k&X-Amz-Signature=ca2c22f776257740c4bf362e84b001c3f9202922535d072fa8f96257e01ac33c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXSN3STQ%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQCqYtzIT21QXIH0feLwPMnZnKHer%2FqykoQYl6bAOjGu4AIgTUqCBOA%2Bp3GqI%2B1TA7qZVHqS317igrBTc8%2FOAe31OvMq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDEb5raJ6y07HEY0%2BqSrcA%2BD8MWgoRd6qvsD3xMnzTE3oPyzBxOQIIxVpJdyqEY%2FJobZSL9Ho%2F31pwqsPK5MZP7LcNp%2BXFLKTsyXnZjilurGyyZq643ICN9gzce1hGyn71NLdZMdC72D%2FaglDoQ0mC%2BbwW7kGdA8wrEyPak0wOzZ4XL47V1Cv1WSiIZkOshqdx6G9HSxFoIDtKRdmVcY0KPycsSKIl9j6FanHSz%2BlHktUT5tlMJmQF4dNic2ZmVhpw2t4MIqy6Fl58ZSACNt7Iiq2fUtsscJ61iS1H%2BTJAi3ziqaDhWl6gFmhsXfpikjWE6B45PAXSHpQ86LtvRu3G24yc4EqTngrX8YRyvZ%2BkEjR%2FRGPdJbfxSHaab2kbU0Xij30T64H6uHbC9iqsOx3Wr7bSlJrIcSWR05%2FFP2QS5Pt%2BEncQWZC4%2B%2FOnbcrVS2tsFWSxzjEGwvIryC1W4qpLcMD98yTzL3OU30FOk0w98RyBk%2FBTIGIkPO56sj%2BtUE9RijUnjAhk4vUQ8FLHeprlIxXO2PKxT9PeKNQJ5%2BMLDrTAwMPv1tHplkLx38gxKmEqeKzTr%2BDlH3q%2FZYF7V%2BBVd8PSWybscBPnvVWZsjsgoL4aq%2B6xmNVHjodeK0Su2%2FbkQ19EjSsGZfVfSoVMNqTkMwGOqUBpWNFJVe%2FHBVlUYbkHAbDkC%2FXk6QydV11dimBSA9PGb1P2y%2Fm3HbNND2Sj6jDTNt622VShZi3Sv9Z2gHAtxfZEfS2%2Fb8YzOcsycqZZmBt%2FgjfpmAHSRUNmPyn8BI%2FBfVMgdusuuGhF1dU3p%2FNYvIkxIX7LpqxkK2pByuB7Fw5cKZ9wMVCv6LMwHsYwHrqeK9miwu89gCBcGJARAoPxIVDKdmUL75k&X-Amz-Signature=79e9a9d28b946a4c9dab6414da51ca4e422c7845aa060678e85519a70722407d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXSN3STQ%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQCqYtzIT21QXIH0feLwPMnZnKHer%2FqykoQYl6bAOjGu4AIgTUqCBOA%2Bp3GqI%2B1TA7qZVHqS317igrBTc8%2FOAe31OvMq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDEb5raJ6y07HEY0%2BqSrcA%2BD8MWgoRd6qvsD3xMnzTE3oPyzBxOQIIxVpJdyqEY%2FJobZSL9Ho%2F31pwqsPK5MZP7LcNp%2BXFLKTsyXnZjilurGyyZq643ICN9gzce1hGyn71NLdZMdC72D%2FaglDoQ0mC%2BbwW7kGdA8wrEyPak0wOzZ4XL47V1Cv1WSiIZkOshqdx6G9HSxFoIDtKRdmVcY0KPycsSKIl9j6FanHSz%2BlHktUT5tlMJmQF4dNic2ZmVhpw2t4MIqy6Fl58ZSACNt7Iiq2fUtsscJ61iS1H%2BTJAi3ziqaDhWl6gFmhsXfpikjWE6B45PAXSHpQ86LtvRu3G24yc4EqTngrX8YRyvZ%2BkEjR%2FRGPdJbfxSHaab2kbU0Xij30T64H6uHbC9iqsOx3Wr7bSlJrIcSWR05%2FFP2QS5Pt%2BEncQWZC4%2B%2FOnbcrVS2tsFWSxzjEGwvIryC1W4qpLcMD98yTzL3OU30FOk0w98RyBk%2FBTIGIkPO56sj%2BtUE9RijUnjAhk4vUQ8FLHeprlIxXO2PKxT9PeKNQJ5%2BMLDrTAwMPv1tHplkLx38gxKmEqeKzTr%2BDlH3q%2FZYF7V%2BBVd8PSWybscBPnvVWZsjsgoL4aq%2B6xmNVHjodeK0Su2%2FbkQ19EjSsGZfVfSoVMNqTkMwGOqUBpWNFJVe%2FHBVlUYbkHAbDkC%2FXk6QydV11dimBSA9PGb1P2y%2Fm3HbNND2Sj6jDTNt622VShZi3Sv9Z2gHAtxfZEfS2%2Fb8YzOcsycqZZmBt%2FgjfpmAHSRUNmPyn8BI%2FBfVMgdusuuGhF1dU3p%2FNYvIkxIX7LpqxkK2pByuB7Fw5cKZ9wMVCv6LMwHsYwHrqeK9miwu89gCBcGJARAoPxIVDKdmUL75k&X-Amz-Signature=fc8b1b9fbc5e84e4cd451247cd6f13df709ece9881eef7c7a588f7b6d58d7c92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXSN3STQ%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQCqYtzIT21QXIH0feLwPMnZnKHer%2FqykoQYl6bAOjGu4AIgTUqCBOA%2Bp3GqI%2B1TA7qZVHqS317igrBTc8%2FOAe31OvMq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDEb5raJ6y07HEY0%2BqSrcA%2BD8MWgoRd6qvsD3xMnzTE3oPyzBxOQIIxVpJdyqEY%2FJobZSL9Ho%2F31pwqsPK5MZP7LcNp%2BXFLKTsyXnZjilurGyyZq643ICN9gzce1hGyn71NLdZMdC72D%2FaglDoQ0mC%2BbwW7kGdA8wrEyPak0wOzZ4XL47V1Cv1WSiIZkOshqdx6G9HSxFoIDtKRdmVcY0KPycsSKIl9j6FanHSz%2BlHktUT5tlMJmQF4dNic2ZmVhpw2t4MIqy6Fl58ZSACNt7Iiq2fUtsscJ61iS1H%2BTJAi3ziqaDhWl6gFmhsXfpikjWE6B45PAXSHpQ86LtvRu3G24yc4EqTngrX8YRyvZ%2BkEjR%2FRGPdJbfxSHaab2kbU0Xij30T64H6uHbC9iqsOx3Wr7bSlJrIcSWR05%2FFP2QS5Pt%2BEncQWZC4%2B%2FOnbcrVS2tsFWSxzjEGwvIryC1W4qpLcMD98yTzL3OU30FOk0w98RyBk%2FBTIGIkPO56sj%2BtUE9RijUnjAhk4vUQ8FLHeprlIxXO2PKxT9PeKNQJ5%2BMLDrTAwMPv1tHplkLx38gxKmEqeKzTr%2BDlH3q%2FZYF7V%2BBVd8PSWybscBPnvVWZsjsgoL4aq%2B6xmNVHjodeK0Su2%2FbkQ19EjSsGZfVfSoVMNqTkMwGOqUBpWNFJVe%2FHBVlUYbkHAbDkC%2FXk6QydV11dimBSA9PGb1P2y%2Fm3HbNND2Sj6jDTNt622VShZi3Sv9Z2gHAtxfZEfS2%2Fb8YzOcsycqZZmBt%2FgjfpmAHSRUNmPyn8BI%2FBfVMgdusuuGhF1dU3p%2FNYvIkxIX7LpqxkK2pByuB7Fw5cKZ9wMVCv6LMwHsYwHrqeK9miwu89gCBcGJARAoPxIVDKdmUL75k&X-Amz-Signature=b0756018302b505f2773bc845dd8b4d1ac14df46d84c755fdb73863c9e0a2968&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

