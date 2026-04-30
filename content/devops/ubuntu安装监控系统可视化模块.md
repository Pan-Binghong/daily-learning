<<<<<<< HEAD
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg)

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

=======
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCXTX5XQ%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQC4DXLdTy3ALc3dTjRbDnn4koD%2F8F4Eas7MqKFcZpm0QwIgb3j2ATFfbqNzDlOKkga2woe%2F7tFmCfw36L8%2FnZh%2F9bcq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDFHoumyPKqkeFgsvvCrcA%2Bmt4owGgnmQ50lZVIyMWIseDP34XcFAkwEz%2FwtruiplKbxp3ollP2hS2NtN3crzYoe95DjKdHRMNzd3Ygtq28s7tMqTZ1Ng9I5Ij7rJXil1H6m05yQhEQXYeVjsGha38e%2F%2Bo8KAHP0IjmG2EUIKn%2FFBHEpRkWe7FrhXGXoasTYrHRUrdUBflyHcKlN39Lk3OqNGib1hQACGOrGJVczUjMZWeCBMFatIruetzjQ%2Fc6gmb7dn8VRhbo75%2FOgjIvRgvhrV9GPgz92wqlxfKU8r0Up9CsJmG1471651%2FfzKC4TkxxIbHsYG9qCBFs4I52Dakx%2Fan12bGiEvlvrNqxkkjUnmnILE5lkcwZ%2FPBHpLt0ticxuaZMZh6K2lzFUZTV3UgNkvxfTgMTy1yis%2FQ72m61wVocgzYSN13U9lnwyg1lM%2B%2BA29ljBqPggb0oQ%2BbjsF1P1Bsg7DL%2BiGDbOHvcFlNIC9PyWClwnYHTV8xYv374uaCCXJjK4FjMsErrQPJcHo4hK6Swuk9rTMPl75vMr4WkSC%2FblwLGF5Nckha3T6Wk0mFTgj7XZ%2FrXNhhCTpmhTTP9srJ1BLazey521E9p%2BkufPS%2Bg6GClhXu4uTMHnJcOlf8rhNGjFQmjaxoMztMN6bzM8GOqUBPYI7r8yiN7jV44AgNXBQPGZ2ttR1hs4JUyHXyyOcem1v%2Fu%2FY5SwtaA4ybpKOsddYKqqMXrjruigjwaqGxip4OaWJu36m8VwmkSQfoZetbkffH7W%2BWvoacAn5hdL8LHEAuuD5Xqmgi8paVlar%2BQtK%2FjPdjLMby00UZ6mMQ7RcRocokQ19Ms7xhZpFVqtI6Mtfd2T9xhseaKsjpTvE%2BfKSS3YQnlTI&X-Amz-Signature=b036605eb3a1273a46626d1db50c550402365c4effdc56ad76444d9e65a48a40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCXTX5XQ%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQC4DXLdTy3ALc3dTjRbDnn4koD%2F8F4Eas7MqKFcZpm0QwIgb3j2ATFfbqNzDlOKkga2woe%2F7tFmCfw36L8%2FnZh%2F9bcq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDFHoumyPKqkeFgsvvCrcA%2Bmt4owGgnmQ50lZVIyMWIseDP34XcFAkwEz%2FwtruiplKbxp3ollP2hS2NtN3crzYoe95DjKdHRMNzd3Ygtq28s7tMqTZ1Ng9I5Ij7rJXil1H6m05yQhEQXYeVjsGha38e%2F%2Bo8KAHP0IjmG2EUIKn%2FFBHEpRkWe7FrhXGXoasTYrHRUrdUBflyHcKlN39Lk3OqNGib1hQACGOrGJVczUjMZWeCBMFatIruetzjQ%2Fc6gmb7dn8VRhbo75%2FOgjIvRgvhrV9GPgz92wqlxfKU8r0Up9CsJmG1471651%2FfzKC4TkxxIbHsYG9qCBFs4I52Dakx%2Fan12bGiEvlvrNqxkkjUnmnILE5lkcwZ%2FPBHpLt0ticxuaZMZh6K2lzFUZTV3UgNkvxfTgMTy1yis%2FQ72m61wVocgzYSN13U9lnwyg1lM%2B%2BA29ljBqPggb0oQ%2BbjsF1P1Bsg7DL%2BiGDbOHvcFlNIC9PyWClwnYHTV8xYv374uaCCXJjK4FjMsErrQPJcHo4hK6Swuk9rTMPl75vMr4WkSC%2FblwLGF5Nckha3T6Wk0mFTgj7XZ%2FrXNhhCTpmhTTP9srJ1BLazey521E9p%2BkufPS%2Bg6GClhXu4uTMHnJcOlf8rhNGjFQmjaxoMztMN6bzM8GOqUBPYI7r8yiN7jV44AgNXBQPGZ2ttR1hs4JUyHXyyOcem1v%2Fu%2FY5SwtaA4ybpKOsddYKqqMXrjruigjwaqGxip4OaWJu36m8VwmkSQfoZetbkffH7W%2BWvoacAn5hdL8LHEAuuD5Xqmgi8paVlar%2BQtK%2FjPdjLMby00UZ6mMQ7RcRocokQ19Ms7xhZpFVqtI6Mtfd2T9xhseaKsjpTvE%2BfKSS3YQnlTI&X-Amz-Signature=b4f8c2543b022425cb157cad7f8b26d336347dd4a10b0a4e5153914a8d646238&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCXTX5XQ%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQC4DXLdTy3ALc3dTjRbDnn4koD%2F8F4Eas7MqKFcZpm0QwIgb3j2ATFfbqNzDlOKkga2woe%2F7tFmCfw36L8%2FnZh%2F9bcq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDFHoumyPKqkeFgsvvCrcA%2Bmt4owGgnmQ50lZVIyMWIseDP34XcFAkwEz%2FwtruiplKbxp3ollP2hS2NtN3crzYoe95DjKdHRMNzd3Ygtq28s7tMqTZ1Ng9I5Ij7rJXil1H6m05yQhEQXYeVjsGha38e%2F%2Bo8KAHP0IjmG2EUIKn%2FFBHEpRkWe7FrhXGXoasTYrHRUrdUBflyHcKlN39Lk3OqNGib1hQACGOrGJVczUjMZWeCBMFatIruetzjQ%2Fc6gmb7dn8VRhbo75%2FOgjIvRgvhrV9GPgz92wqlxfKU8r0Up9CsJmG1471651%2FfzKC4TkxxIbHsYG9qCBFs4I52Dakx%2Fan12bGiEvlvrNqxkkjUnmnILE5lkcwZ%2FPBHpLt0ticxuaZMZh6K2lzFUZTV3UgNkvxfTgMTy1yis%2FQ72m61wVocgzYSN13U9lnwyg1lM%2B%2BA29ljBqPggb0oQ%2BbjsF1P1Bsg7DL%2BiGDbOHvcFlNIC9PyWClwnYHTV8xYv374uaCCXJjK4FjMsErrQPJcHo4hK6Swuk9rTMPl75vMr4WkSC%2FblwLGF5Nckha3T6Wk0mFTgj7XZ%2FrXNhhCTpmhTTP9srJ1BLazey521E9p%2BkufPS%2Bg6GClhXu4uTMHnJcOlf8rhNGjFQmjaxoMztMN6bzM8GOqUBPYI7r8yiN7jV44AgNXBQPGZ2ttR1hs4JUyHXyyOcem1v%2Fu%2FY5SwtaA4ybpKOsddYKqqMXrjruigjwaqGxip4OaWJu36m8VwmkSQfoZetbkffH7W%2BWvoacAn5hdL8LHEAuuD5Xqmgi8paVlar%2BQtK%2FjPdjLMby00UZ6mMQ7RcRocokQ19Ms7xhZpFVqtI6Mtfd2T9xhseaKsjpTvE%2BfKSS3YQnlTI&X-Amz-Signature=d8afd330e2dae24d242b6ca370b10efcf071f12fb1750859701a3de18cd11304&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCXTX5XQ%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQC4DXLdTy3ALc3dTjRbDnn4koD%2F8F4Eas7MqKFcZpm0QwIgb3j2ATFfbqNzDlOKkga2woe%2F7tFmCfw36L8%2FnZh%2F9bcq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDFHoumyPKqkeFgsvvCrcA%2Bmt4owGgnmQ50lZVIyMWIseDP34XcFAkwEz%2FwtruiplKbxp3ollP2hS2NtN3crzYoe95DjKdHRMNzd3Ygtq28s7tMqTZ1Ng9I5Ij7rJXil1H6m05yQhEQXYeVjsGha38e%2F%2Bo8KAHP0IjmG2EUIKn%2FFBHEpRkWe7FrhXGXoasTYrHRUrdUBflyHcKlN39Lk3OqNGib1hQACGOrGJVczUjMZWeCBMFatIruetzjQ%2Fc6gmb7dn8VRhbo75%2FOgjIvRgvhrV9GPgz92wqlxfKU8r0Up9CsJmG1471651%2FfzKC4TkxxIbHsYG9qCBFs4I52Dakx%2Fan12bGiEvlvrNqxkkjUnmnILE5lkcwZ%2FPBHpLt0ticxuaZMZh6K2lzFUZTV3UgNkvxfTgMTy1yis%2FQ72m61wVocgzYSN13U9lnwyg1lM%2B%2BA29ljBqPggb0oQ%2BbjsF1P1Bsg7DL%2BiGDbOHvcFlNIC9PyWClwnYHTV8xYv374uaCCXJjK4FjMsErrQPJcHo4hK6Swuk9rTMPl75vMr4WkSC%2FblwLGF5Nckha3T6Wk0mFTgj7XZ%2FrXNhhCTpmhTTP9srJ1BLazey521E9p%2BkufPS%2Bg6GClhXu4uTMHnJcOlf8rhNGjFQmjaxoMztMN6bzM8GOqUBPYI7r8yiN7jV44AgNXBQPGZ2ttR1hs4JUyHXyyOcem1v%2Fu%2FY5SwtaA4ybpKOsddYKqqMXrjruigjwaqGxip4OaWJu36m8VwmkSQfoZetbkffH7W%2BWvoacAn5hdL8LHEAuuD5Xqmgi8paVlar%2BQtK%2FjPdjLMby00UZ6mMQ7RcRocokQ19Ms7xhZpFVqtI6Mtfd2T9xhseaKsjpTvE%2BfKSS3YQnlTI&X-Amz-Signature=5c0d34a8a017048c7fa16c33996080e3a3eab81fa9848b3d6f868b4bf4f24aaa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCXTX5XQ%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQC4DXLdTy3ALc3dTjRbDnn4koD%2F8F4Eas7MqKFcZpm0QwIgb3j2ATFfbqNzDlOKkga2woe%2F7tFmCfw36L8%2FnZh%2F9bcq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDFHoumyPKqkeFgsvvCrcA%2Bmt4owGgnmQ50lZVIyMWIseDP34XcFAkwEz%2FwtruiplKbxp3ollP2hS2NtN3crzYoe95DjKdHRMNzd3Ygtq28s7tMqTZ1Ng9I5Ij7rJXil1H6m05yQhEQXYeVjsGha38e%2F%2Bo8KAHP0IjmG2EUIKn%2FFBHEpRkWe7FrhXGXoasTYrHRUrdUBflyHcKlN39Lk3OqNGib1hQACGOrGJVczUjMZWeCBMFatIruetzjQ%2Fc6gmb7dn8VRhbo75%2FOgjIvRgvhrV9GPgz92wqlxfKU8r0Up9CsJmG1471651%2FfzKC4TkxxIbHsYG9qCBFs4I52Dakx%2Fan12bGiEvlvrNqxkkjUnmnILE5lkcwZ%2FPBHpLt0ticxuaZMZh6K2lzFUZTV3UgNkvxfTgMTy1yis%2FQ72m61wVocgzYSN13U9lnwyg1lM%2B%2BA29ljBqPggb0oQ%2BbjsF1P1Bsg7DL%2BiGDbOHvcFlNIC9PyWClwnYHTV8xYv374uaCCXJjK4FjMsErrQPJcHo4hK6Swuk9rTMPl75vMr4WkSC%2FblwLGF5Nckha3T6Wk0mFTgj7XZ%2FrXNhhCTpmhTTP9srJ1BLazey521E9p%2BkufPS%2Bg6GClhXu4uTMHnJcOlf8rhNGjFQmjaxoMztMN6bzM8GOqUBPYI7r8yiN7jV44AgNXBQPGZ2ttR1hs4JUyHXyyOcem1v%2Fu%2FY5SwtaA4ybpKOsddYKqqMXrjruigjwaqGxip4OaWJu36m8VwmkSQfoZetbkffH7W%2BWvoacAn5hdL8LHEAuuD5Xqmgi8paVlar%2BQtK%2FjPdjLMby00UZ6mMQ7RcRocokQ19Ms7xhZpFVqtI6Mtfd2T9xhseaKsjpTvE%2BfKSS3YQnlTI&X-Amz-Signature=118fb9074b9e019bcb5ebb8287bf1399bfab5ab22f7699752c8880764db153ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCXTX5XQ%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQC4DXLdTy3ALc3dTjRbDnn4koD%2F8F4Eas7MqKFcZpm0QwIgb3j2ATFfbqNzDlOKkga2woe%2F7tFmCfw36L8%2FnZh%2F9bcq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDFHoumyPKqkeFgsvvCrcA%2Bmt4owGgnmQ50lZVIyMWIseDP34XcFAkwEz%2FwtruiplKbxp3ollP2hS2NtN3crzYoe95DjKdHRMNzd3Ygtq28s7tMqTZ1Ng9I5Ij7rJXil1H6m05yQhEQXYeVjsGha38e%2F%2Bo8KAHP0IjmG2EUIKn%2FFBHEpRkWe7FrhXGXoasTYrHRUrdUBflyHcKlN39Lk3OqNGib1hQACGOrGJVczUjMZWeCBMFatIruetzjQ%2Fc6gmb7dn8VRhbo75%2FOgjIvRgvhrV9GPgz92wqlxfKU8r0Up9CsJmG1471651%2FfzKC4TkxxIbHsYG9qCBFs4I52Dakx%2Fan12bGiEvlvrNqxkkjUnmnILE5lkcwZ%2FPBHpLt0ticxuaZMZh6K2lzFUZTV3UgNkvxfTgMTy1yis%2FQ72m61wVocgzYSN13U9lnwyg1lM%2B%2BA29ljBqPggb0oQ%2BbjsF1P1Bsg7DL%2BiGDbOHvcFlNIC9PyWClwnYHTV8xYv374uaCCXJjK4FjMsErrQPJcHo4hK6Swuk9rTMPl75vMr4WkSC%2FblwLGF5Nckha3T6Wk0mFTgj7XZ%2FrXNhhCTpmhTTP9srJ1BLazey521E9p%2BkufPS%2Bg6GClhXu4uTMHnJcOlf8rhNGjFQmjaxoMztMN6bzM8GOqUBPYI7r8yiN7jV44AgNXBQPGZ2ttR1hs4JUyHXyyOcem1v%2Fu%2FY5SwtaA4ybpKOsddYKqqMXrjruigjwaqGxip4OaWJu36m8VwmkSQfoZetbkffH7W%2BWvoacAn5hdL8LHEAuuD5Xqmgi8paVlar%2BQtK%2FjPdjLMby00UZ6mMQ7RcRocokQ19Ms7xhZpFVqtI6Mtfd2T9xhseaKsjpTvE%2BfKSS3YQnlTI&X-Amz-Signature=fe84fb3518ad42745e1829a7847965f05e953691251c4ce2b8cc29cad9cd25db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCXTX5XQ%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQC4DXLdTy3ALc3dTjRbDnn4koD%2F8F4Eas7MqKFcZpm0QwIgb3j2ATFfbqNzDlOKkga2woe%2F7tFmCfw36L8%2FnZh%2F9bcq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDFHoumyPKqkeFgsvvCrcA%2Bmt4owGgnmQ50lZVIyMWIseDP34XcFAkwEz%2FwtruiplKbxp3ollP2hS2NtN3crzYoe95DjKdHRMNzd3Ygtq28s7tMqTZ1Ng9I5Ij7rJXil1H6m05yQhEQXYeVjsGha38e%2F%2Bo8KAHP0IjmG2EUIKn%2FFBHEpRkWe7FrhXGXoasTYrHRUrdUBflyHcKlN39Lk3OqNGib1hQACGOrGJVczUjMZWeCBMFatIruetzjQ%2Fc6gmb7dn8VRhbo75%2FOgjIvRgvhrV9GPgz92wqlxfKU8r0Up9CsJmG1471651%2FfzKC4TkxxIbHsYG9qCBFs4I52Dakx%2Fan12bGiEvlvrNqxkkjUnmnILE5lkcwZ%2FPBHpLt0ticxuaZMZh6K2lzFUZTV3UgNkvxfTgMTy1yis%2FQ72m61wVocgzYSN13U9lnwyg1lM%2B%2BA29ljBqPggb0oQ%2BbjsF1P1Bsg7DL%2BiGDbOHvcFlNIC9PyWClwnYHTV8xYv374uaCCXJjK4FjMsErrQPJcHo4hK6Swuk9rTMPl75vMr4WkSC%2FblwLGF5Nckha3T6Wk0mFTgj7XZ%2FrXNhhCTpmhTTP9srJ1BLazey521E9p%2BkufPS%2Bg6GClhXu4uTMHnJcOlf8rhNGjFQmjaxoMztMN6bzM8GOqUBPYI7r8yiN7jV44AgNXBQPGZ2ttR1hs4JUyHXyyOcem1v%2Fu%2FY5SwtaA4ybpKOsddYKqqMXrjruigjwaqGxip4OaWJu36m8VwmkSQfoZetbkffH7W%2BWvoacAn5hdL8LHEAuuD5Xqmgi8paVlar%2BQtK%2FjPdjLMby00UZ6mMQ7RcRocokQ19Ms7xhZpFVqtI6Mtfd2T9xhseaKsjpTvE%2BfKSS3YQnlTI&X-Amz-Signature=fee7273e7a57032f1e6be4d92632c6cdff594002a50c38ef86cccb2334f319a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

>>>>>>> 67e2e8ba81abbca0065a5254fe8b7b646ead6176
