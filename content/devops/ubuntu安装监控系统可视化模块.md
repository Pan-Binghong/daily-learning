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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNRGGTPM%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBqiMafNPOLOrLoNiCVZ1Jl0Gur9XClnoGVS0qAc7RqyAiAu4Wi4iUyP0lkmN7QGiRl6tFNSN51O2jHgr2Ejwfpljir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM83FGTegBVPnWbmFUKtwD1y4DnH2PjjeTKWpf9OJZlAUgMhKpOVO8SnLg4uOuKjTzs1BGaBx2ndUOK4LIt9Mqn3FITUKddgEvbDIdsUOYzQLMz2a2VHwB7MMLWFbpawaCDkSSPyQDLgzDY%2F%2BL8NVT6FiSEkozpp8ERJvEvDin8ZRQ3vdLRcFgCCQxIjFnKBFb5u5DMoenOMmcLUwlhfrieZWNpZGdsQFQOlr8j%2BLWd1DpUUZZM5JhMGR5Z7mykLum6jllZE25Rx6ebFApoK%2B%2BtBEMoSmP%2FPyAqTiQo1pbWoRH4IDjJeHlghdCtzMrTJ4zljVjDmG%2Bk3rOKoIVWZHkZifCkGHbSHOdiNjpVHMwGijR2GK9bFsFXgJAGqgjBilYu3inAymmUNE6nsYgHmmb0%2BowZHUG2epKBtFU3RIFLGEelxl%2FZ8sghZMlz%2F7G%2FT0JWJYbKoJ4NeZA7WUvWPch6BFPs%2F8J%2BjcfPhmYbIjW35e75SijyUCd8H21t%2FbTW3nskmrU71aHHtagZWGujvttvuHeTJoCq7xgwKdGrq33XgxpDa6%2FjWF6haE2iZmaMDZjnfY6TL%2BJTUHP1xb66OPKtODizn%2FlmQ0uYGrkUgVzOJVUF42vUSzL%2FxbmPrP1gvoOtw4xohMYlqAh22ow6d%2B8ygY6pgHlU6H510lDcgt%2Fye6na2qXMaYIShFJQT0ovhySZBX%2BU5%2B2M3nmTQxQfF08g0pZ%2B0VeXmZ9bj0eAMVWv67PrcjpsqYuFtCiIsevh6y488s07NNj%2BAP4FGR2Q%2BhTtvXHoLbFYvWBi0db6OnR9a3hAYU3O%2FTvRHk67CE6MkAzKX4ZmBmjss9r50vPMlKTEAJBNGlzzRC3ChLFBN4QJdRagzn1bhfx73VK&X-Amz-Signature=e462a0fd2c6458d9207955705fd95533a66830811b5da2661b53484af42f0a4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNRGGTPM%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBqiMafNPOLOrLoNiCVZ1Jl0Gur9XClnoGVS0qAc7RqyAiAu4Wi4iUyP0lkmN7QGiRl6tFNSN51O2jHgr2Ejwfpljir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM83FGTegBVPnWbmFUKtwD1y4DnH2PjjeTKWpf9OJZlAUgMhKpOVO8SnLg4uOuKjTzs1BGaBx2ndUOK4LIt9Mqn3FITUKddgEvbDIdsUOYzQLMz2a2VHwB7MMLWFbpawaCDkSSPyQDLgzDY%2F%2BL8NVT6FiSEkozpp8ERJvEvDin8ZRQ3vdLRcFgCCQxIjFnKBFb5u5DMoenOMmcLUwlhfrieZWNpZGdsQFQOlr8j%2BLWd1DpUUZZM5JhMGR5Z7mykLum6jllZE25Rx6ebFApoK%2B%2BtBEMoSmP%2FPyAqTiQo1pbWoRH4IDjJeHlghdCtzMrTJ4zljVjDmG%2Bk3rOKoIVWZHkZifCkGHbSHOdiNjpVHMwGijR2GK9bFsFXgJAGqgjBilYu3inAymmUNE6nsYgHmmb0%2BowZHUG2epKBtFU3RIFLGEelxl%2FZ8sghZMlz%2F7G%2FT0JWJYbKoJ4NeZA7WUvWPch6BFPs%2F8J%2BjcfPhmYbIjW35e75SijyUCd8H21t%2FbTW3nskmrU71aHHtagZWGujvttvuHeTJoCq7xgwKdGrq33XgxpDa6%2FjWF6haE2iZmaMDZjnfY6TL%2BJTUHP1xb66OPKtODizn%2FlmQ0uYGrkUgVzOJVUF42vUSzL%2FxbmPrP1gvoOtw4xohMYlqAh22ow6d%2B8ygY6pgHlU6H510lDcgt%2Fye6na2qXMaYIShFJQT0ovhySZBX%2BU5%2B2M3nmTQxQfF08g0pZ%2B0VeXmZ9bj0eAMVWv67PrcjpsqYuFtCiIsevh6y488s07NNj%2BAP4FGR2Q%2BhTtvXHoLbFYvWBi0db6OnR9a3hAYU3O%2FTvRHk67CE6MkAzKX4ZmBmjss9r50vPMlKTEAJBNGlzzRC3ChLFBN4QJdRagzn1bhfx73VK&X-Amz-Signature=120acb1ce38ac8b15da56f2207e44543028e9abcfd47cd08905649e9b09afa28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNRGGTPM%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBqiMafNPOLOrLoNiCVZ1Jl0Gur9XClnoGVS0qAc7RqyAiAu4Wi4iUyP0lkmN7QGiRl6tFNSN51O2jHgr2Ejwfpljir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM83FGTegBVPnWbmFUKtwD1y4DnH2PjjeTKWpf9OJZlAUgMhKpOVO8SnLg4uOuKjTzs1BGaBx2ndUOK4LIt9Mqn3FITUKddgEvbDIdsUOYzQLMz2a2VHwB7MMLWFbpawaCDkSSPyQDLgzDY%2F%2BL8NVT6FiSEkozpp8ERJvEvDin8ZRQ3vdLRcFgCCQxIjFnKBFb5u5DMoenOMmcLUwlhfrieZWNpZGdsQFQOlr8j%2BLWd1DpUUZZM5JhMGR5Z7mykLum6jllZE25Rx6ebFApoK%2B%2BtBEMoSmP%2FPyAqTiQo1pbWoRH4IDjJeHlghdCtzMrTJ4zljVjDmG%2Bk3rOKoIVWZHkZifCkGHbSHOdiNjpVHMwGijR2GK9bFsFXgJAGqgjBilYu3inAymmUNE6nsYgHmmb0%2BowZHUG2epKBtFU3RIFLGEelxl%2FZ8sghZMlz%2F7G%2FT0JWJYbKoJ4NeZA7WUvWPch6BFPs%2F8J%2BjcfPhmYbIjW35e75SijyUCd8H21t%2FbTW3nskmrU71aHHtagZWGujvttvuHeTJoCq7xgwKdGrq33XgxpDa6%2FjWF6haE2iZmaMDZjnfY6TL%2BJTUHP1xb66OPKtODizn%2FlmQ0uYGrkUgVzOJVUF42vUSzL%2FxbmPrP1gvoOtw4xohMYlqAh22ow6d%2B8ygY6pgHlU6H510lDcgt%2Fye6na2qXMaYIShFJQT0ovhySZBX%2BU5%2B2M3nmTQxQfF08g0pZ%2B0VeXmZ9bj0eAMVWv67PrcjpsqYuFtCiIsevh6y488s07NNj%2BAP4FGR2Q%2BhTtvXHoLbFYvWBi0db6OnR9a3hAYU3O%2FTvRHk67CE6MkAzKX4ZmBmjss9r50vPMlKTEAJBNGlzzRC3ChLFBN4QJdRagzn1bhfx73VK&X-Amz-Signature=e67c7da47a12ce3dae3e1ea1d9188f59833923429f38e7d0c0b15ced4a6feaa9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNRGGTPM%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBqiMafNPOLOrLoNiCVZ1Jl0Gur9XClnoGVS0qAc7RqyAiAu4Wi4iUyP0lkmN7QGiRl6tFNSN51O2jHgr2Ejwfpljir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM83FGTegBVPnWbmFUKtwD1y4DnH2PjjeTKWpf9OJZlAUgMhKpOVO8SnLg4uOuKjTzs1BGaBx2ndUOK4LIt9Mqn3FITUKddgEvbDIdsUOYzQLMz2a2VHwB7MMLWFbpawaCDkSSPyQDLgzDY%2F%2BL8NVT6FiSEkozpp8ERJvEvDin8ZRQ3vdLRcFgCCQxIjFnKBFb5u5DMoenOMmcLUwlhfrieZWNpZGdsQFQOlr8j%2BLWd1DpUUZZM5JhMGR5Z7mykLum6jllZE25Rx6ebFApoK%2B%2BtBEMoSmP%2FPyAqTiQo1pbWoRH4IDjJeHlghdCtzMrTJ4zljVjDmG%2Bk3rOKoIVWZHkZifCkGHbSHOdiNjpVHMwGijR2GK9bFsFXgJAGqgjBilYu3inAymmUNE6nsYgHmmb0%2BowZHUG2epKBtFU3RIFLGEelxl%2FZ8sghZMlz%2F7G%2FT0JWJYbKoJ4NeZA7WUvWPch6BFPs%2F8J%2BjcfPhmYbIjW35e75SijyUCd8H21t%2FbTW3nskmrU71aHHtagZWGujvttvuHeTJoCq7xgwKdGrq33XgxpDa6%2FjWF6haE2iZmaMDZjnfY6TL%2BJTUHP1xb66OPKtODizn%2FlmQ0uYGrkUgVzOJVUF42vUSzL%2FxbmPrP1gvoOtw4xohMYlqAh22ow6d%2B8ygY6pgHlU6H510lDcgt%2Fye6na2qXMaYIShFJQT0ovhySZBX%2BU5%2B2M3nmTQxQfF08g0pZ%2B0VeXmZ9bj0eAMVWv67PrcjpsqYuFtCiIsevh6y488s07NNj%2BAP4FGR2Q%2BhTtvXHoLbFYvWBi0db6OnR9a3hAYU3O%2FTvRHk67CE6MkAzKX4ZmBmjss9r50vPMlKTEAJBNGlzzRC3ChLFBN4QJdRagzn1bhfx73VK&X-Amz-Signature=fe2b2983953520420f35a352b04a68ada6fcfb3462089dd69069c7780b3a7702&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNRGGTPM%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBqiMafNPOLOrLoNiCVZ1Jl0Gur9XClnoGVS0qAc7RqyAiAu4Wi4iUyP0lkmN7QGiRl6tFNSN51O2jHgr2Ejwfpljir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM83FGTegBVPnWbmFUKtwD1y4DnH2PjjeTKWpf9OJZlAUgMhKpOVO8SnLg4uOuKjTzs1BGaBx2ndUOK4LIt9Mqn3FITUKddgEvbDIdsUOYzQLMz2a2VHwB7MMLWFbpawaCDkSSPyQDLgzDY%2F%2BL8NVT6FiSEkozpp8ERJvEvDin8ZRQ3vdLRcFgCCQxIjFnKBFb5u5DMoenOMmcLUwlhfrieZWNpZGdsQFQOlr8j%2BLWd1DpUUZZM5JhMGR5Z7mykLum6jllZE25Rx6ebFApoK%2B%2BtBEMoSmP%2FPyAqTiQo1pbWoRH4IDjJeHlghdCtzMrTJ4zljVjDmG%2Bk3rOKoIVWZHkZifCkGHbSHOdiNjpVHMwGijR2GK9bFsFXgJAGqgjBilYu3inAymmUNE6nsYgHmmb0%2BowZHUG2epKBtFU3RIFLGEelxl%2FZ8sghZMlz%2F7G%2FT0JWJYbKoJ4NeZA7WUvWPch6BFPs%2F8J%2BjcfPhmYbIjW35e75SijyUCd8H21t%2FbTW3nskmrU71aHHtagZWGujvttvuHeTJoCq7xgwKdGrq33XgxpDa6%2FjWF6haE2iZmaMDZjnfY6TL%2BJTUHP1xb66OPKtODizn%2FlmQ0uYGrkUgVzOJVUF42vUSzL%2FxbmPrP1gvoOtw4xohMYlqAh22ow6d%2B8ygY6pgHlU6H510lDcgt%2Fye6na2qXMaYIShFJQT0ovhySZBX%2BU5%2B2M3nmTQxQfF08g0pZ%2B0VeXmZ9bj0eAMVWv67PrcjpsqYuFtCiIsevh6y488s07NNj%2BAP4FGR2Q%2BhTtvXHoLbFYvWBi0db6OnR9a3hAYU3O%2FTvRHk67CE6MkAzKX4ZmBmjss9r50vPMlKTEAJBNGlzzRC3ChLFBN4QJdRagzn1bhfx73VK&X-Amz-Signature=6377d289c4b0edb4f42e9f95eec6b6ce0870b2bc7b414458b491a3347b75159a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNRGGTPM%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBqiMafNPOLOrLoNiCVZ1Jl0Gur9XClnoGVS0qAc7RqyAiAu4Wi4iUyP0lkmN7QGiRl6tFNSN51O2jHgr2Ejwfpljir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM83FGTegBVPnWbmFUKtwD1y4DnH2PjjeTKWpf9OJZlAUgMhKpOVO8SnLg4uOuKjTzs1BGaBx2ndUOK4LIt9Mqn3FITUKddgEvbDIdsUOYzQLMz2a2VHwB7MMLWFbpawaCDkSSPyQDLgzDY%2F%2BL8NVT6FiSEkozpp8ERJvEvDin8ZRQ3vdLRcFgCCQxIjFnKBFb5u5DMoenOMmcLUwlhfrieZWNpZGdsQFQOlr8j%2BLWd1DpUUZZM5JhMGR5Z7mykLum6jllZE25Rx6ebFApoK%2B%2BtBEMoSmP%2FPyAqTiQo1pbWoRH4IDjJeHlghdCtzMrTJ4zljVjDmG%2Bk3rOKoIVWZHkZifCkGHbSHOdiNjpVHMwGijR2GK9bFsFXgJAGqgjBilYu3inAymmUNE6nsYgHmmb0%2BowZHUG2epKBtFU3RIFLGEelxl%2FZ8sghZMlz%2F7G%2FT0JWJYbKoJ4NeZA7WUvWPch6BFPs%2F8J%2BjcfPhmYbIjW35e75SijyUCd8H21t%2FbTW3nskmrU71aHHtagZWGujvttvuHeTJoCq7xgwKdGrq33XgxpDa6%2FjWF6haE2iZmaMDZjnfY6TL%2BJTUHP1xb66OPKtODizn%2FlmQ0uYGrkUgVzOJVUF42vUSzL%2FxbmPrP1gvoOtw4xohMYlqAh22ow6d%2B8ygY6pgHlU6H510lDcgt%2Fye6na2qXMaYIShFJQT0ovhySZBX%2BU5%2B2M3nmTQxQfF08g0pZ%2B0VeXmZ9bj0eAMVWv67PrcjpsqYuFtCiIsevh6y488s07NNj%2BAP4FGR2Q%2BhTtvXHoLbFYvWBi0db6OnR9a3hAYU3O%2FTvRHk67CE6MkAzKX4ZmBmjss9r50vPMlKTEAJBNGlzzRC3ChLFBN4QJdRagzn1bhfx73VK&X-Amz-Signature=2bfe3e67454bb31fb25024da0f71fe70d57617fc81ffb1095ba41089a23c2a77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNRGGTPM%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBqiMafNPOLOrLoNiCVZ1Jl0Gur9XClnoGVS0qAc7RqyAiAu4Wi4iUyP0lkmN7QGiRl6tFNSN51O2jHgr2Ejwfpljir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM83FGTegBVPnWbmFUKtwD1y4DnH2PjjeTKWpf9OJZlAUgMhKpOVO8SnLg4uOuKjTzs1BGaBx2ndUOK4LIt9Mqn3FITUKddgEvbDIdsUOYzQLMz2a2VHwB7MMLWFbpawaCDkSSPyQDLgzDY%2F%2BL8NVT6FiSEkozpp8ERJvEvDin8ZRQ3vdLRcFgCCQxIjFnKBFb5u5DMoenOMmcLUwlhfrieZWNpZGdsQFQOlr8j%2BLWd1DpUUZZM5JhMGR5Z7mykLum6jllZE25Rx6ebFApoK%2B%2BtBEMoSmP%2FPyAqTiQo1pbWoRH4IDjJeHlghdCtzMrTJ4zljVjDmG%2Bk3rOKoIVWZHkZifCkGHbSHOdiNjpVHMwGijR2GK9bFsFXgJAGqgjBilYu3inAymmUNE6nsYgHmmb0%2BowZHUG2epKBtFU3RIFLGEelxl%2FZ8sghZMlz%2F7G%2FT0JWJYbKoJ4NeZA7WUvWPch6BFPs%2F8J%2BjcfPhmYbIjW35e75SijyUCd8H21t%2FbTW3nskmrU71aHHtagZWGujvttvuHeTJoCq7xgwKdGrq33XgxpDa6%2FjWF6haE2iZmaMDZjnfY6TL%2BJTUHP1xb66OPKtODizn%2FlmQ0uYGrkUgVzOJVUF42vUSzL%2FxbmPrP1gvoOtw4xohMYlqAh22ow6d%2B8ygY6pgHlU6H510lDcgt%2Fye6na2qXMaYIShFJQT0ovhySZBX%2BU5%2B2M3nmTQxQfF08g0pZ%2B0VeXmZ9bj0eAMVWv67PrcjpsqYuFtCiIsevh6y488s07NNj%2BAP4FGR2Q%2BhTtvXHoLbFYvWBi0db6OnR9a3hAYU3O%2FTvRHk67CE6MkAzKX4ZmBmjss9r50vPMlKTEAJBNGlzzRC3ChLFBN4QJdRagzn1bhfx73VK&X-Amz-Signature=b4c240920023b3ff904c82c7e13a752557905be550fe9af5783ef0b298ea35a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

