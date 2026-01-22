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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SJUEQY4%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIEGAsAPTSVry9y3oKss4WqK6SoHErumh%2B7wcxulyTcneAiEAnX%2B%2F7%2B0yKy4zk8hu03nClJqU4v6CzYCgcl0PG%2BxHGhAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFisI%2FB6dKoiDL%2B53CrcAwKxwK%2FwLOLS2HbiamjYojNEsRXUmP6p5t%2F3LyTqPyItD2qiskqR9uy4QfLOahjB8OGJCQksI3ArfY1wJMnncefsIBrNe7EIVa%2Fw%2BnLYK%2FqcBD7DNO0%2BxlpR5kw9o0fQ41PiNHqdPbt5ONfFnjlOmxy%2FWWiItI2%2BbIO%2Fqy%2FOGF8UF1eWnAmy2y7sTzSKKubUnNzvFbhmSkPMsDiqWVDKnVIrsXL%2BmO2izAs7BSWykNeT5C1Wi8oGCiJJ5OoGWxrGQqNBBhbYO%2BDHyv2I6mADCSIl%2Brt%2B2Jq3Tj%2Fmm1F0xKvsVDvZeNBg7lSnnb1tGSsAbu%2BpytMViVS9wXxT8X21I%2FJZz9kw9sqZQRGuMT5NT57Ufzpc6g5dn1GzCT3O3ajNQWH0s9Zlbn2EKl8h6GEjsNUcdUF9XVwF4M7YGy6SxB733HMO8t%2B73NQuRj8livPk3ENidXAOf%2FvuknrZqPqD9CDGmT%2F8yEB2bjnCgzgsZyOyYzxSop5iuhED%2FR6NDR1d4DFm7ZLS9D2CoNKTcP0GxnDmyC8suhcj0XOl3918LWipH4GnaBGyYusQX4qNhGVnLdHyiIwTdRAb1YrBJbha0Y4Ttixm63s9c7yE8z2byRr8AJDMIwTSKz7f4gWKMJDXxcsGOqUBUDNpSWNvAZ%2B0n5QfucSIxTsgoNOINYbWDnXNGg%2FhyVdRu%2Fg%2BD3Km6tis%2ByzIYEH87sxgDvEVe31A8qkMEpFcg4lP4WoGnzL1qBe5wDUHTTYbJB1PgdtXgMUdKyPgxxhAbKZIfkE6vHBqZ6reHCoMBYEG1eypwBq5%2BRbZw5%2BnAgySZC1y40dWcvNy5ClSAkaNweihpjm%2BWZ%2B5nnq%2BOGwiUoqnZFsz&X-Amz-Signature=a8d36c49e2285aef55c1148cf13ac108bd31ad012ab4e7a71ceb7abee3098a60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SJUEQY4%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIEGAsAPTSVry9y3oKss4WqK6SoHErumh%2B7wcxulyTcneAiEAnX%2B%2F7%2B0yKy4zk8hu03nClJqU4v6CzYCgcl0PG%2BxHGhAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFisI%2FB6dKoiDL%2B53CrcAwKxwK%2FwLOLS2HbiamjYojNEsRXUmP6p5t%2F3LyTqPyItD2qiskqR9uy4QfLOahjB8OGJCQksI3ArfY1wJMnncefsIBrNe7EIVa%2Fw%2BnLYK%2FqcBD7DNO0%2BxlpR5kw9o0fQ41PiNHqdPbt5ONfFnjlOmxy%2FWWiItI2%2BbIO%2Fqy%2FOGF8UF1eWnAmy2y7sTzSKKubUnNzvFbhmSkPMsDiqWVDKnVIrsXL%2BmO2izAs7BSWykNeT5C1Wi8oGCiJJ5OoGWxrGQqNBBhbYO%2BDHyv2I6mADCSIl%2Brt%2B2Jq3Tj%2Fmm1F0xKvsVDvZeNBg7lSnnb1tGSsAbu%2BpytMViVS9wXxT8X21I%2FJZz9kw9sqZQRGuMT5NT57Ufzpc6g5dn1GzCT3O3ajNQWH0s9Zlbn2EKl8h6GEjsNUcdUF9XVwF4M7YGy6SxB733HMO8t%2B73NQuRj8livPk3ENidXAOf%2FvuknrZqPqD9CDGmT%2F8yEB2bjnCgzgsZyOyYzxSop5iuhED%2FR6NDR1d4DFm7ZLS9D2CoNKTcP0GxnDmyC8suhcj0XOl3918LWipH4GnaBGyYusQX4qNhGVnLdHyiIwTdRAb1YrBJbha0Y4Ttixm63s9c7yE8z2byRr8AJDMIwTSKz7f4gWKMJDXxcsGOqUBUDNpSWNvAZ%2B0n5QfucSIxTsgoNOINYbWDnXNGg%2FhyVdRu%2Fg%2BD3Km6tis%2ByzIYEH87sxgDvEVe31A8qkMEpFcg4lP4WoGnzL1qBe5wDUHTTYbJB1PgdtXgMUdKyPgxxhAbKZIfkE6vHBqZ6reHCoMBYEG1eypwBq5%2BRbZw5%2BnAgySZC1y40dWcvNy5ClSAkaNweihpjm%2BWZ%2B5nnq%2BOGwiUoqnZFsz&X-Amz-Signature=5fec0c5f15ed3d263c4f10ba0bac91ab4cf6792e8372023700b3fe901a6a162a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SJUEQY4%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIEGAsAPTSVry9y3oKss4WqK6SoHErumh%2B7wcxulyTcneAiEAnX%2B%2F7%2B0yKy4zk8hu03nClJqU4v6CzYCgcl0PG%2BxHGhAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFisI%2FB6dKoiDL%2B53CrcAwKxwK%2FwLOLS2HbiamjYojNEsRXUmP6p5t%2F3LyTqPyItD2qiskqR9uy4QfLOahjB8OGJCQksI3ArfY1wJMnncefsIBrNe7EIVa%2Fw%2BnLYK%2FqcBD7DNO0%2BxlpR5kw9o0fQ41PiNHqdPbt5ONfFnjlOmxy%2FWWiItI2%2BbIO%2Fqy%2FOGF8UF1eWnAmy2y7sTzSKKubUnNzvFbhmSkPMsDiqWVDKnVIrsXL%2BmO2izAs7BSWykNeT5C1Wi8oGCiJJ5OoGWxrGQqNBBhbYO%2BDHyv2I6mADCSIl%2Brt%2B2Jq3Tj%2Fmm1F0xKvsVDvZeNBg7lSnnb1tGSsAbu%2BpytMViVS9wXxT8X21I%2FJZz9kw9sqZQRGuMT5NT57Ufzpc6g5dn1GzCT3O3ajNQWH0s9Zlbn2EKl8h6GEjsNUcdUF9XVwF4M7YGy6SxB733HMO8t%2B73NQuRj8livPk3ENidXAOf%2FvuknrZqPqD9CDGmT%2F8yEB2bjnCgzgsZyOyYzxSop5iuhED%2FR6NDR1d4DFm7ZLS9D2CoNKTcP0GxnDmyC8suhcj0XOl3918LWipH4GnaBGyYusQX4qNhGVnLdHyiIwTdRAb1YrBJbha0Y4Ttixm63s9c7yE8z2byRr8AJDMIwTSKz7f4gWKMJDXxcsGOqUBUDNpSWNvAZ%2B0n5QfucSIxTsgoNOINYbWDnXNGg%2FhyVdRu%2Fg%2BD3Km6tis%2ByzIYEH87sxgDvEVe31A8qkMEpFcg4lP4WoGnzL1qBe5wDUHTTYbJB1PgdtXgMUdKyPgxxhAbKZIfkE6vHBqZ6reHCoMBYEG1eypwBq5%2BRbZw5%2BnAgySZC1y40dWcvNy5ClSAkaNweihpjm%2BWZ%2B5nnq%2BOGwiUoqnZFsz&X-Amz-Signature=3eadb17fd8b7bd2dd025809a27281c45eb947aaf34d111fd827649be4d5b0e30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SJUEQY4%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIEGAsAPTSVry9y3oKss4WqK6SoHErumh%2B7wcxulyTcneAiEAnX%2B%2F7%2B0yKy4zk8hu03nClJqU4v6CzYCgcl0PG%2BxHGhAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFisI%2FB6dKoiDL%2B53CrcAwKxwK%2FwLOLS2HbiamjYojNEsRXUmP6p5t%2F3LyTqPyItD2qiskqR9uy4QfLOahjB8OGJCQksI3ArfY1wJMnncefsIBrNe7EIVa%2Fw%2BnLYK%2FqcBD7DNO0%2BxlpR5kw9o0fQ41PiNHqdPbt5ONfFnjlOmxy%2FWWiItI2%2BbIO%2Fqy%2FOGF8UF1eWnAmy2y7sTzSKKubUnNzvFbhmSkPMsDiqWVDKnVIrsXL%2BmO2izAs7BSWykNeT5C1Wi8oGCiJJ5OoGWxrGQqNBBhbYO%2BDHyv2I6mADCSIl%2Brt%2B2Jq3Tj%2Fmm1F0xKvsVDvZeNBg7lSnnb1tGSsAbu%2BpytMViVS9wXxT8X21I%2FJZz9kw9sqZQRGuMT5NT57Ufzpc6g5dn1GzCT3O3ajNQWH0s9Zlbn2EKl8h6GEjsNUcdUF9XVwF4M7YGy6SxB733HMO8t%2B73NQuRj8livPk3ENidXAOf%2FvuknrZqPqD9CDGmT%2F8yEB2bjnCgzgsZyOyYzxSop5iuhED%2FR6NDR1d4DFm7ZLS9D2CoNKTcP0GxnDmyC8suhcj0XOl3918LWipH4GnaBGyYusQX4qNhGVnLdHyiIwTdRAb1YrBJbha0Y4Ttixm63s9c7yE8z2byRr8AJDMIwTSKz7f4gWKMJDXxcsGOqUBUDNpSWNvAZ%2B0n5QfucSIxTsgoNOINYbWDnXNGg%2FhyVdRu%2Fg%2BD3Km6tis%2ByzIYEH87sxgDvEVe31A8qkMEpFcg4lP4WoGnzL1qBe5wDUHTTYbJB1PgdtXgMUdKyPgxxhAbKZIfkE6vHBqZ6reHCoMBYEG1eypwBq5%2BRbZw5%2BnAgySZC1y40dWcvNy5ClSAkaNweihpjm%2BWZ%2B5nnq%2BOGwiUoqnZFsz&X-Amz-Signature=1f124378a19587b98a7c7b265ded5fd0a41e5a899d9b4ec0afef1d74466205cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SJUEQY4%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIEGAsAPTSVry9y3oKss4WqK6SoHErumh%2B7wcxulyTcneAiEAnX%2B%2F7%2B0yKy4zk8hu03nClJqU4v6CzYCgcl0PG%2BxHGhAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFisI%2FB6dKoiDL%2B53CrcAwKxwK%2FwLOLS2HbiamjYojNEsRXUmP6p5t%2F3LyTqPyItD2qiskqR9uy4QfLOahjB8OGJCQksI3ArfY1wJMnncefsIBrNe7EIVa%2Fw%2BnLYK%2FqcBD7DNO0%2BxlpR5kw9o0fQ41PiNHqdPbt5ONfFnjlOmxy%2FWWiItI2%2BbIO%2Fqy%2FOGF8UF1eWnAmy2y7sTzSKKubUnNzvFbhmSkPMsDiqWVDKnVIrsXL%2BmO2izAs7BSWykNeT5C1Wi8oGCiJJ5OoGWxrGQqNBBhbYO%2BDHyv2I6mADCSIl%2Brt%2B2Jq3Tj%2Fmm1F0xKvsVDvZeNBg7lSnnb1tGSsAbu%2BpytMViVS9wXxT8X21I%2FJZz9kw9sqZQRGuMT5NT57Ufzpc6g5dn1GzCT3O3ajNQWH0s9Zlbn2EKl8h6GEjsNUcdUF9XVwF4M7YGy6SxB733HMO8t%2B73NQuRj8livPk3ENidXAOf%2FvuknrZqPqD9CDGmT%2F8yEB2bjnCgzgsZyOyYzxSop5iuhED%2FR6NDR1d4DFm7ZLS9D2CoNKTcP0GxnDmyC8suhcj0XOl3918LWipH4GnaBGyYusQX4qNhGVnLdHyiIwTdRAb1YrBJbha0Y4Ttixm63s9c7yE8z2byRr8AJDMIwTSKz7f4gWKMJDXxcsGOqUBUDNpSWNvAZ%2B0n5QfucSIxTsgoNOINYbWDnXNGg%2FhyVdRu%2Fg%2BD3Km6tis%2ByzIYEH87sxgDvEVe31A8qkMEpFcg4lP4WoGnzL1qBe5wDUHTTYbJB1PgdtXgMUdKyPgxxhAbKZIfkE6vHBqZ6reHCoMBYEG1eypwBq5%2BRbZw5%2BnAgySZC1y40dWcvNy5ClSAkaNweihpjm%2BWZ%2B5nnq%2BOGwiUoqnZFsz&X-Amz-Signature=c4bb0116575a01bb427107bd7f23d48f095e0608c9b372e9e0b1aa14fae57433&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SJUEQY4%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIEGAsAPTSVry9y3oKss4WqK6SoHErumh%2B7wcxulyTcneAiEAnX%2B%2F7%2B0yKy4zk8hu03nClJqU4v6CzYCgcl0PG%2BxHGhAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFisI%2FB6dKoiDL%2B53CrcAwKxwK%2FwLOLS2HbiamjYojNEsRXUmP6p5t%2F3LyTqPyItD2qiskqR9uy4QfLOahjB8OGJCQksI3ArfY1wJMnncefsIBrNe7EIVa%2Fw%2BnLYK%2FqcBD7DNO0%2BxlpR5kw9o0fQ41PiNHqdPbt5ONfFnjlOmxy%2FWWiItI2%2BbIO%2Fqy%2FOGF8UF1eWnAmy2y7sTzSKKubUnNzvFbhmSkPMsDiqWVDKnVIrsXL%2BmO2izAs7BSWykNeT5C1Wi8oGCiJJ5OoGWxrGQqNBBhbYO%2BDHyv2I6mADCSIl%2Brt%2B2Jq3Tj%2Fmm1F0xKvsVDvZeNBg7lSnnb1tGSsAbu%2BpytMViVS9wXxT8X21I%2FJZz9kw9sqZQRGuMT5NT57Ufzpc6g5dn1GzCT3O3ajNQWH0s9Zlbn2EKl8h6GEjsNUcdUF9XVwF4M7YGy6SxB733HMO8t%2B73NQuRj8livPk3ENidXAOf%2FvuknrZqPqD9CDGmT%2F8yEB2bjnCgzgsZyOyYzxSop5iuhED%2FR6NDR1d4DFm7ZLS9D2CoNKTcP0GxnDmyC8suhcj0XOl3918LWipH4GnaBGyYusQX4qNhGVnLdHyiIwTdRAb1YrBJbha0Y4Ttixm63s9c7yE8z2byRr8AJDMIwTSKz7f4gWKMJDXxcsGOqUBUDNpSWNvAZ%2B0n5QfucSIxTsgoNOINYbWDnXNGg%2FhyVdRu%2Fg%2BD3Km6tis%2ByzIYEH87sxgDvEVe31A8qkMEpFcg4lP4WoGnzL1qBe5wDUHTTYbJB1PgdtXgMUdKyPgxxhAbKZIfkE6vHBqZ6reHCoMBYEG1eypwBq5%2BRbZw5%2BnAgySZC1y40dWcvNy5ClSAkaNweihpjm%2BWZ%2B5nnq%2BOGwiUoqnZFsz&X-Amz-Signature=967b8d4f64cfb8522ee23e7ba11e2c7f7d8d98724cf72ac29a4af624b2852765&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SJUEQY4%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIEGAsAPTSVry9y3oKss4WqK6SoHErumh%2B7wcxulyTcneAiEAnX%2B%2F7%2B0yKy4zk8hu03nClJqU4v6CzYCgcl0PG%2BxHGhAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFisI%2FB6dKoiDL%2B53CrcAwKxwK%2FwLOLS2HbiamjYojNEsRXUmP6p5t%2F3LyTqPyItD2qiskqR9uy4QfLOahjB8OGJCQksI3ArfY1wJMnncefsIBrNe7EIVa%2Fw%2BnLYK%2FqcBD7DNO0%2BxlpR5kw9o0fQ41PiNHqdPbt5ONfFnjlOmxy%2FWWiItI2%2BbIO%2Fqy%2FOGF8UF1eWnAmy2y7sTzSKKubUnNzvFbhmSkPMsDiqWVDKnVIrsXL%2BmO2izAs7BSWykNeT5C1Wi8oGCiJJ5OoGWxrGQqNBBhbYO%2BDHyv2I6mADCSIl%2Brt%2B2Jq3Tj%2Fmm1F0xKvsVDvZeNBg7lSnnb1tGSsAbu%2BpytMViVS9wXxT8X21I%2FJZz9kw9sqZQRGuMT5NT57Ufzpc6g5dn1GzCT3O3ajNQWH0s9Zlbn2EKl8h6GEjsNUcdUF9XVwF4M7YGy6SxB733HMO8t%2B73NQuRj8livPk3ENidXAOf%2FvuknrZqPqD9CDGmT%2F8yEB2bjnCgzgsZyOyYzxSop5iuhED%2FR6NDR1d4DFm7ZLS9D2CoNKTcP0GxnDmyC8suhcj0XOl3918LWipH4GnaBGyYusQX4qNhGVnLdHyiIwTdRAb1YrBJbha0Y4Ttixm63s9c7yE8z2byRr8AJDMIwTSKz7f4gWKMJDXxcsGOqUBUDNpSWNvAZ%2B0n5QfucSIxTsgoNOINYbWDnXNGg%2FhyVdRu%2Fg%2BD3Km6tis%2ByzIYEH87sxgDvEVe31A8qkMEpFcg4lP4WoGnzL1qBe5wDUHTTYbJB1PgdtXgMUdKyPgxxhAbKZIfkE6vHBqZ6reHCoMBYEG1eypwBq5%2BRbZw5%2BnAgySZC1y40dWcvNy5ClSAkaNweihpjm%2BWZ%2B5nnq%2BOGwiUoqnZFsz&X-Amz-Signature=a3e6eaf392795f2343729d879fd2ae97a115d4473871b35b7779dbbfacb82ce9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

