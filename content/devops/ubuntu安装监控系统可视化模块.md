---
title: Ubuntu安装监控系统可视化模块
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-20T03:10:00.000Z'
draft: false
标签:
- Linux
- Ubuntu
categories:
- DevOps
---

Prometheus是一个开放性的监控解决方案，用户可以非常方便的安装和使用Prometheus并且能够非常方便的对其进行扩展。为了能够更加直观的了解Prometheus Server，接下来我们将在本地部署并运行一个Prometheus Server实例，通过Node Exporter采集当前主机的系统资源使用情况。 并通过Grafana创建一个简单的可视化仪表盘。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXWHW6ZF%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDecATWQmI7Wq5aEDE%2FSbN9I9CbFJsf1pucsT8deq6NCgIhANBoXbzfXE32JglQTwmstfIM3Ijds4%2FVhJ36J4PKcuYjKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySRQus8SPlAomTJIcq3APaPtmVU%2FH6bMtPV4DZsLi2vUHXaMR9kJ3%2Bf5BKfKIkm2nnPirESp7PMfFWeIiJhpxRUjqMvSnvVFWyY9xMLwuUTSECHK857M%2FlnZk0TZjpIqmA5u1kXvaDoAgmK%2FTNt33rzZQ%2FlRoHvdL950sLNChsaYdhpfEPPbYGo2WIypVVPUFHQBdKZ4LRvEjUApHN8n7ztayZG%2BDK14MvzALKVglaKZV9a09p1N461XstI%2Bgr4FxYihJ8t4bZbSvb4gP2L7clmI9tXxfBDXr96PkWXnc3I9BCwOVGX4bSkS8ncxyBB3TVTIAN1YUozD%2FivLJRJqBhq7gBrsF5wrJAur%2FkwzKBeyv4WxO2rHY7CkxB74r7gp2FmM%2BKHLBU0jEPL2hQkeMdxIBD7oNrPBHS0qK1AG0GEETK9ZWX09Lcrnua7UhK%2Frk3f2wlFM%2FNoDXKW6MVhAVT03ReNZ4cy%2BiLyacI2vQaSqdB4T2omWwjREO7d0%2FK1epnX9wvgZqFvKhv8fEBsyAHMNa0J5sGi8ISi4r1ChsnbKjZjfZFazQGBWLYUKwnT5mUhg7xtYZoPbDmoaVOdNzi8dUmOZSISEq6Y8mlSDrqNNVDkMXFsW3SQYBj5TcyumP0f79ZTfq3%2BUhDhzD2oqzIBjqkAYMxSlwJAdYygGLoWKJ8m5O%2F2F0t2PAPdZUnzq6dCRFsU9FpKuyTjUgcnZC3TOjgL6ZnfeVfb8DnidNIytFJvDAHPRbD3plDf9%2Bynd2NKIKDJtO91r7jQTUEzxIXCNWYvFnU3YjpJNMDeSzjttSPebt9WR4dJ9r16tKvBDZ0fXIZs4kW4VwnvbSVz%2BeJ04Q9eIAHktSsWo0nadfk9XG2UryYSbWg&X-Amz-Signature=649d905c479a0ecd9389941c69fb16f029bea7bd13e443fb32663892a9c210bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXWHW6ZF%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDecATWQmI7Wq5aEDE%2FSbN9I9CbFJsf1pucsT8deq6NCgIhANBoXbzfXE32JglQTwmstfIM3Ijds4%2FVhJ36J4PKcuYjKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySRQus8SPlAomTJIcq3APaPtmVU%2FH6bMtPV4DZsLi2vUHXaMR9kJ3%2Bf5BKfKIkm2nnPirESp7PMfFWeIiJhpxRUjqMvSnvVFWyY9xMLwuUTSECHK857M%2FlnZk0TZjpIqmA5u1kXvaDoAgmK%2FTNt33rzZQ%2FlRoHvdL950sLNChsaYdhpfEPPbYGo2WIypVVPUFHQBdKZ4LRvEjUApHN8n7ztayZG%2BDK14MvzALKVglaKZV9a09p1N461XstI%2Bgr4FxYihJ8t4bZbSvb4gP2L7clmI9tXxfBDXr96PkWXnc3I9BCwOVGX4bSkS8ncxyBB3TVTIAN1YUozD%2FivLJRJqBhq7gBrsF5wrJAur%2FkwzKBeyv4WxO2rHY7CkxB74r7gp2FmM%2BKHLBU0jEPL2hQkeMdxIBD7oNrPBHS0qK1AG0GEETK9ZWX09Lcrnua7UhK%2Frk3f2wlFM%2FNoDXKW6MVhAVT03ReNZ4cy%2BiLyacI2vQaSqdB4T2omWwjREO7d0%2FK1epnX9wvgZqFvKhv8fEBsyAHMNa0J5sGi8ISi4r1ChsnbKjZjfZFazQGBWLYUKwnT5mUhg7xtYZoPbDmoaVOdNzi8dUmOZSISEq6Y8mlSDrqNNVDkMXFsW3SQYBj5TcyumP0f79ZTfq3%2BUhDhzD2oqzIBjqkAYMxSlwJAdYygGLoWKJ8m5O%2F2F0t2PAPdZUnzq6dCRFsU9FpKuyTjUgcnZC3TOjgL6ZnfeVfb8DnidNIytFJvDAHPRbD3plDf9%2Bynd2NKIKDJtO91r7jQTUEzxIXCNWYvFnU3YjpJNMDeSzjttSPebt9WR4dJ9r16tKvBDZ0fXIZs4kW4VwnvbSVz%2BeJ04Q9eIAHktSsWo0nadfk9XG2UryYSbWg&X-Amz-Signature=9d75ca682cbfe4b1ee6040c84da73e03f12a13c5f20ffe8563b40ae872fe8e3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXWHW6ZF%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDecATWQmI7Wq5aEDE%2FSbN9I9CbFJsf1pucsT8deq6NCgIhANBoXbzfXE32JglQTwmstfIM3Ijds4%2FVhJ36J4PKcuYjKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySRQus8SPlAomTJIcq3APaPtmVU%2FH6bMtPV4DZsLi2vUHXaMR9kJ3%2Bf5BKfKIkm2nnPirESp7PMfFWeIiJhpxRUjqMvSnvVFWyY9xMLwuUTSECHK857M%2FlnZk0TZjpIqmA5u1kXvaDoAgmK%2FTNt33rzZQ%2FlRoHvdL950sLNChsaYdhpfEPPbYGo2WIypVVPUFHQBdKZ4LRvEjUApHN8n7ztayZG%2BDK14MvzALKVglaKZV9a09p1N461XstI%2Bgr4FxYihJ8t4bZbSvb4gP2L7clmI9tXxfBDXr96PkWXnc3I9BCwOVGX4bSkS8ncxyBB3TVTIAN1YUozD%2FivLJRJqBhq7gBrsF5wrJAur%2FkwzKBeyv4WxO2rHY7CkxB74r7gp2FmM%2BKHLBU0jEPL2hQkeMdxIBD7oNrPBHS0qK1AG0GEETK9ZWX09Lcrnua7UhK%2Frk3f2wlFM%2FNoDXKW6MVhAVT03ReNZ4cy%2BiLyacI2vQaSqdB4T2omWwjREO7d0%2FK1epnX9wvgZqFvKhv8fEBsyAHMNa0J5sGi8ISi4r1ChsnbKjZjfZFazQGBWLYUKwnT5mUhg7xtYZoPbDmoaVOdNzi8dUmOZSISEq6Y8mlSDrqNNVDkMXFsW3SQYBj5TcyumP0f79ZTfq3%2BUhDhzD2oqzIBjqkAYMxSlwJAdYygGLoWKJ8m5O%2F2F0t2PAPdZUnzq6dCRFsU9FpKuyTjUgcnZC3TOjgL6ZnfeVfb8DnidNIytFJvDAHPRbD3plDf9%2Bynd2NKIKDJtO91r7jQTUEzxIXCNWYvFnU3YjpJNMDeSzjttSPebt9WR4dJ9r16tKvBDZ0fXIZs4kW4VwnvbSVz%2BeJ04Q9eIAHktSsWo0nadfk9XG2UryYSbWg&X-Amz-Signature=2b637b029f5462e12e12cea880e619bbef3d089b031c5c12f0c734da5446e69e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXWHW6ZF%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDecATWQmI7Wq5aEDE%2FSbN9I9CbFJsf1pucsT8deq6NCgIhANBoXbzfXE32JglQTwmstfIM3Ijds4%2FVhJ36J4PKcuYjKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySRQus8SPlAomTJIcq3APaPtmVU%2FH6bMtPV4DZsLi2vUHXaMR9kJ3%2Bf5BKfKIkm2nnPirESp7PMfFWeIiJhpxRUjqMvSnvVFWyY9xMLwuUTSECHK857M%2FlnZk0TZjpIqmA5u1kXvaDoAgmK%2FTNt33rzZQ%2FlRoHvdL950sLNChsaYdhpfEPPbYGo2WIypVVPUFHQBdKZ4LRvEjUApHN8n7ztayZG%2BDK14MvzALKVglaKZV9a09p1N461XstI%2Bgr4FxYihJ8t4bZbSvb4gP2L7clmI9tXxfBDXr96PkWXnc3I9BCwOVGX4bSkS8ncxyBB3TVTIAN1YUozD%2FivLJRJqBhq7gBrsF5wrJAur%2FkwzKBeyv4WxO2rHY7CkxB74r7gp2FmM%2BKHLBU0jEPL2hQkeMdxIBD7oNrPBHS0qK1AG0GEETK9ZWX09Lcrnua7UhK%2Frk3f2wlFM%2FNoDXKW6MVhAVT03ReNZ4cy%2BiLyacI2vQaSqdB4T2omWwjREO7d0%2FK1epnX9wvgZqFvKhv8fEBsyAHMNa0J5sGi8ISi4r1ChsnbKjZjfZFazQGBWLYUKwnT5mUhg7xtYZoPbDmoaVOdNzi8dUmOZSISEq6Y8mlSDrqNNVDkMXFsW3SQYBj5TcyumP0f79ZTfq3%2BUhDhzD2oqzIBjqkAYMxSlwJAdYygGLoWKJ8m5O%2F2F0t2PAPdZUnzq6dCRFsU9FpKuyTjUgcnZC3TOjgL6ZnfeVfb8DnidNIytFJvDAHPRbD3plDf9%2Bynd2NKIKDJtO91r7jQTUEzxIXCNWYvFnU3YjpJNMDeSzjttSPebt9WR4dJ9r16tKvBDZ0fXIZs4kW4VwnvbSVz%2BeJ04Q9eIAHktSsWo0nadfk9XG2UryYSbWg&X-Amz-Signature=bb336e0d175fc6233ea107126485d20c1dcffb30224976c5dc296a536efa9b34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXWHW6ZF%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDecATWQmI7Wq5aEDE%2FSbN9I9CbFJsf1pucsT8deq6NCgIhANBoXbzfXE32JglQTwmstfIM3Ijds4%2FVhJ36J4PKcuYjKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySRQus8SPlAomTJIcq3APaPtmVU%2FH6bMtPV4DZsLi2vUHXaMR9kJ3%2Bf5BKfKIkm2nnPirESp7PMfFWeIiJhpxRUjqMvSnvVFWyY9xMLwuUTSECHK857M%2FlnZk0TZjpIqmA5u1kXvaDoAgmK%2FTNt33rzZQ%2FlRoHvdL950sLNChsaYdhpfEPPbYGo2WIypVVPUFHQBdKZ4LRvEjUApHN8n7ztayZG%2BDK14MvzALKVglaKZV9a09p1N461XstI%2Bgr4FxYihJ8t4bZbSvb4gP2L7clmI9tXxfBDXr96PkWXnc3I9BCwOVGX4bSkS8ncxyBB3TVTIAN1YUozD%2FivLJRJqBhq7gBrsF5wrJAur%2FkwzKBeyv4WxO2rHY7CkxB74r7gp2FmM%2BKHLBU0jEPL2hQkeMdxIBD7oNrPBHS0qK1AG0GEETK9ZWX09Lcrnua7UhK%2Frk3f2wlFM%2FNoDXKW6MVhAVT03ReNZ4cy%2BiLyacI2vQaSqdB4T2omWwjREO7d0%2FK1epnX9wvgZqFvKhv8fEBsyAHMNa0J5sGi8ISi4r1ChsnbKjZjfZFazQGBWLYUKwnT5mUhg7xtYZoPbDmoaVOdNzi8dUmOZSISEq6Y8mlSDrqNNVDkMXFsW3SQYBj5TcyumP0f79ZTfq3%2BUhDhzD2oqzIBjqkAYMxSlwJAdYygGLoWKJ8m5O%2F2F0t2PAPdZUnzq6dCRFsU9FpKuyTjUgcnZC3TOjgL6ZnfeVfb8DnidNIytFJvDAHPRbD3plDf9%2Bynd2NKIKDJtO91r7jQTUEzxIXCNWYvFnU3YjpJNMDeSzjttSPebt9WR4dJ9r16tKvBDZ0fXIZs4kW4VwnvbSVz%2BeJ04Q9eIAHktSsWo0nadfk9XG2UryYSbWg&X-Amz-Signature=61feba67fc744cb7858df28c4f4db81bc1093881ce43a78750114dfb112f244c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXWHW6ZF%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDecATWQmI7Wq5aEDE%2FSbN9I9CbFJsf1pucsT8deq6NCgIhANBoXbzfXE32JglQTwmstfIM3Ijds4%2FVhJ36J4PKcuYjKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySRQus8SPlAomTJIcq3APaPtmVU%2FH6bMtPV4DZsLi2vUHXaMR9kJ3%2Bf5BKfKIkm2nnPirESp7PMfFWeIiJhpxRUjqMvSnvVFWyY9xMLwuUTSECHK857M%2FlnZk0TZjpIqmA5u1kXvaDoAgmK%2FTNt33rzZQ%2FlRoHvdL950sLNChsaYdhpfEPPbYGo2WIypVVPUFHQBdKZ4LRvEjUApHN8n7ztayZG%2BDK14MvzALKVglaKZV9a09p1N461XstI%2Bgr4FxYihJ8t4bZbSvb4gP2L7clmI9tXxfBDXr96PkWXnc3I9BCwOVGX4bSkS8ncxyBB3TVTIAN1YUozD%2FivLJRJqBhq7gBrsF5wrJAur%2FkwzKBeyv4WxO2rHY7CkxB74r7gp2FmM%2BKHLBU0jEPL2hQkeMdxIBD7oNrPBHS0qK1AG0GEETK9ZWX09Lcrnua7UhK%2Frk3f2wlFM%2FNoDXKW6MVhAVT03ReNZ4cy%2BiLyacI2vQaSqdB4T2omWwjREO7d0%2FK1epnX9wvgZqFvKhv8fEBsyAHMNa0J5sGi8ISi4r1ChsnbKjZjfZFazQGBWLYUKwnT5mUhg7xtYZoPbDmoaVOdNzi8dUmOZSISEq6Y8mlSDrqNNVDkMXFsW3SQYBj5TcyumP0f79ZTfq3%2BUhDhzD2oqzIBjqkAYMxSlwJAdYygGLoWKJ8m5O%2F2F0t2PAPdZUnzq6dCRFsU9FpKuyTjUgcnZC3TOjgL6ZnfeVfb8DnidNIytFJvDAHPRbD3plDf9%2Bynd2NKIKDJtO91r7jQTUEzxIXCNWYvFnU3YjpJNMDeSzjttSPebt9WR4dJ9r16tKvBDZ0fXIZs4kW4VwnvbSVz%2BeJ04Q9eIAHktSsWo0nadfk9XG2UryYSbWg&X-Amz-Signature=b3365ac26b96e92eeb1ba7ac69aeadc9f7fdd0806d627cb1b4aa880d4cd7e5e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXWHW6ZF%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDecATWQmI7Wq5aEDE%2FSbN9I9CbFJsf1pucsT8deq6NCgIhANBoXbzfXE32JglQTwmstfIM3Ijds4%2FVhJ36J4PKcuYjKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySRQus8SPlAomTJIcq3APaPtmVU%2FH6bMtPV4DZsLi2vUHXaMR9kJ3%2Bf5BKfKIkm2nnPirESp7PMfFWeIiJhpxRUjqMvSnvVFWyY9xMLwuUTSECHK857M%2FlnZk0TZjpIqmA5u1kXvaDoAgmK%2FTNt33rzZQ%2FlRoHvdL950sLNChsaYdhpfEPPbYGo2WIypVVPUFHQBdKZ4LRvEjUApHN8n7ztayZG%2BDK14MvzALKVglaKZV9a09p1N461XstI%2Bgr4FxYihJ8t4bZbSvb4gP2L7clmI9tXxfBDXr96PkWXnc3I9BCwOVGX4bSkS8ncxyBB3TVTIAN1YUozD%2FivLJRJqBhq7gBrsF5wrJAur%2FkwzKBeyv4WxO2rHY7CkxB74r7gp2FmM%2BKHLBU0jEPL2hQkeMdxIBD7oNrPBHS0qK1AG0GEETK9ZWX09Lcrnua7UhK%2Frk3f2wlFM%2FNoDXKW6MVhAVT03ReNZ4cy%2BiLyacI2vQaSqdB4T2omWwjREO7d0%2FK1epnX9wvgZqFvKhv8fEBsyAHMNa0J5sGi8ISi4r1ChsnbKjZjfZFazQGBWLYUKwnT5mUhg7xtYZoPbDmoaVOdNzi8dUmOZSISEq6Y8mlSDrqNNVDkMXFsW3SQYBj5TcyumP0f79ZTfq3%2BUhDhzD2oqzIBjqkAYMxSlwJAdYygGLoWKJ8m5O%2F2F0t2PAPdZUnzq6dCRFsU9FpKuyTjUgcnZC3TOjgL6ZnfeVfb8DnidNIytFJvDAHPRbD3plDf9%2Bynd2NKIKDJtO91r7jQTUEzxIXCNWYvFnU3YjpJNMDeSzjttSPebt9WR4dJ9r16tKvBDZ0fXIZs4kW4VwnvbSVz%2BeJ04Q9eIAHktSsWo0nadfk9XG2UryYSbWg&X-Amz-Signature=0efef12ff28991031d540dfbd60c96abb266511723b35e64b0077a3140f49efe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

