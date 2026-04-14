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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XITAYNSE%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICHK%2F%2BV6Qt5843U50e5vCGTdUTmAgy4LN8MCnJoZhGvQAiB0D56bSLIOUgD%2BzAFaNlMDB%2BEv%2FrQNdee8Yn2Mc2je4iqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTXz9iqPGKNv48XU4KtwDrJ8pyjKkI%2F2qvfeSkBArNPxER2CTOatyaiqYnt%2Fjejy%2B86j3hFb39fA4JpbyEZFdsjLE%2FVUGB4JZ%2Fcd%2BVbXWQ%2B55Pge6k8XLr%2BphnRSPMCbzlQaBaylqKm7Vxts%2BmB2IHERJUNbvizfan4nHfPadZP77ByLbPJbWZ1jJbpc4GGnyqZ66V3%2Bc2aIMXHquONqfQGo7rQUmoMknC2l6fb2555wgQvjtrg4XR0PAM0Q7K4L4UOcLMTQ9ZNs%2BXh7kDgOkaX057FoCb8WSnlolGH5kV4Ca7IBqGlGfHmR1XUyVODknG1VKO%2BZ3%2BWGcXmPHbk8v%2BJ80BC5DoHmVVToFLoZpAkaFOWL%2FoKX7iZTBlHT0DOnThP%2Bcyd0nRB%2B%2Bq6JngpNpH3Bvi7woXi2RTsHqeV8Ierm18k4n%2FDuSFvR%2B9H%2BhvZItCdbcGSs1ZZu16fGbYqg5%2BBcWvrUniJF9sXtEDj53GIEYRhsmE98GPih%2FsUJGdJtvDWSsxFEX9vNlwfoEB%2Fz4ISH7dFqVpnug%2BIZhfe%2Bdgkz2%2B9BbnUEwqYmViJnUS3YuAR1%2FDjx0%2B63FfC8R%2BIeJBGhgZOajieqft3y9bdNGTbBTXPc0LrtH%2FAoNAiu3JJCJ4M4tc477GraqcLAw%2F972zgY6pgFD%2FZs5oFwBqo3psF9dBtAKC7Tae7E%2FjrJploazLjFanUMI6yLxBD6LoRs6UoK3t61oX2nsfO4zkV5nBgbnlJ5ZBS%2BkdzmxMuuYQgjBVTOVhWSk4T30JN%2F2p7dPj04tqm77RVRFDFcl7oRJvn0j93Zk%2B5p2xGGQl5ZayKY0pWR3qbGAiE9SdpwL25fQ8p3tJRNeCCqMzzYU9CIt27HtDcsIJglSwZEB&X-Amz-Signature=c02ef16418e3c4659722dba74eda162586394187694156aab134d1551dc39c26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XITAYNSE%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICHK%2F%2BV6Qt5843U50e5vCGTdUTmAgy4LN8MCnJoZhGvQAiB0D56bSLIOUgD%2BzAFaNlMDB%2BEv%2FrQNdee8Yn2Mc2je4iqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTXz9iqPGKNv48XU4KtwDrJ8pyjKkI%2F2qvfeSkBArNPxER2CTOatyaiqYnt%2Fjejy%2B86j3hFb39fA4JpbyEZFdsjLE%2FVUGB4JZ%2Fcd%2BVbXWQ%2B55Pge6k8XLr%2BphnRSPMCbzlQaBaylqKm7Vxts%2BmB2IHERJUNbvizfan4nHfPadZP77ByLbPJbWZ1jJbpc4GGnyqZ66V3%2Bc2aIMXHquONqfQGo7rQUmoMknC2l6fb2555wgQvjtrg4XR0PAM0Q7K4L4UOcLMTQ9ZNs%2BXh7kDgOkaX057FoCb8WSnlolGH5kV4Ca7IBqGlGfHmR1XUyVODknG1VKO%2BZ3%2BWGcXmPHbk8v%2BJ80BC5DoHmVVToFLoZpAkaFOWL%2FoKX7iZTBlHT0DOnThP%2Bcyd0nRB%2B%2Bq6JngpNpH3Bvi7woXi2RTsHqeV8Ierm18k4n%2FDuSFvR%2B9H%2BhvZItCdbcGSs1ZZu16fGbYqg5%2BBcWvrUniJF9sXtEDj53GIEYRhsmE98GPih%2FsUJGdJtvDWSsxFEX9vNlwfoEB%2Fz4ISH7dFqVpnug%2BIZhfe%2Bdgkz2%2B9BbnUEwqYmViJnUS3YuAR1%2FDjx0%2B63FfC8R%2BIeJBGhgZOajieqft3y9bdNGTbBTXPc0LrtH%2FAoNAiu3JJCJ4M4tc477GraqcLAw%2F972zgY6pgFD%2FZs5oFwBqo3psF9dBtAKC7Tae7E%2FjrJploazLjFanUMI6yLxBD6LoRs6UoK3t61oX2nsfO4zkV5nBgbnlJ5ZBS%2BkdzmxMuuYQgjBVTOVhWSk4T30JN%2F2p7dPj04tqm77RVRFDFcl7oRJvn0j93Zk%2B5p2xGGQl5ZayKY0pWR3qbGAiE9SdpwL25fQ8p3tJRNeCCqMzzYU9CIt27HtDcsIJglSwZEB&X-Amz-Signature=71118c9af5a7307d7af2062e3b3b2b6bb63bdcb586a4b385c9772d01c07cc634&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XITAYNSE%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICHK%2F%2BV6Qt5843U50e5vCGTdUTmAgy4LN8MCnJoZhGvQAiB0D56bSLIOUgD%2BzAFaNlMDB%2BEv%2FrQNdee8Yn2Mc2je4iqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTXz9iqPGKNv48XU4KtwDrJ8pyjKkI%2F2qvfeSkBArNPxER2CTOatyaiqYnt%2Fjejy%2B86j3hFb39fA4JpbyEZFdsjLE%2FVUGB4JZ%2Fcd%2BVbXWQ%2B55Pge6k8XLr%2BphnRSPMCbzlQaBaylqKm7Vxts%2BmB2IHERJUNbvizfan4nHfPadZP77ByLbPJbWZ1jJbpc4GGnyqZ66V3%2Bc2aIMXHquONqfQGo7rQUmoMknC2l6fb2555wgQvjtrg4XR0PAM0Q7K4L4UOcLMTQ9ZNs%2BXh7kDgOkaX057FoCb8WSnlolGH5kV4Ca7IBqGlGfHmR1XUyVODknG1VKO%2BZ3%2BWGcXmPHbk8v%2BJ80BC5DoHmVVToFLoZpAkaFOWL%2FoKX7iZTBlHT0DOnThP%2Bcyd0nRB%2B%2Bq6JngpNpH3Bvi7woXi2RTsHqeV8Ierm18k4n%2FDuSFvR%2B9H%2BhvZItCdbcGSs1ZZu16fGbYqg5%2BBcWvrUniJF9sXtEDj53GIEYRhsmE98GPih%2FsUJGdJtvDWSsxFEX9vNlwfoEB%2Fz4ISH7dFqVpnug%2BIZhfe%2Bdgkz2%2B9BbnUEwqYmViJnUS3YuAR1%2FDjx0%2B63FfC8R%2BIeJBGhgZOajieqft3y9bdNGTbBTXPc0LrtH%2FAoNAiu3JJCJ4M4tc477GraqcLAw%2F972zgY6pgFD%2FZs5oFwBqo3psF9dBtAKC7Tae7E%2FjrJploazLjFanUMI6yLxBD6LoRs6UoK3t61oX2nsfO4zkV5nBgbnlJ5ZBS%2BkdzmxMuuYQgjBVTOVhWSk4T30JN%2F2p7dPj04tqm77RVRFDFcl7oRJvn0j93Zk%2B5p2xGGQl5ZayKY0pWR3qbGAiE9SdpwL25fQ8p3tJRNeCCqMzzYU9CIt27HtDcsIJglSwZEB&X-Amz-Signature=19694aedb210a5726ec20f286b9060e9fa70a604306062bcd21ea227ef940ce6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XITAYNSE%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICHK%2F%2BV6Qt5843U50e5vCGTdUTmAgy4LN8MCnJoZhGvQAiB0D56bSLIOUgD%2BzAFaNlMDB%2BEv%2FrQNdee8Yn2Mc2je4iqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTXz9iqPGKNv48XU4KtwDrJ8pyjKkI%2F2qvfeSkBArNPxER2CTOatyaiqYnt%2Fjejy%2B86j3hFb39fA4JpbyEZFdsjLE%2FVUGB4JZ%2Fcd%2BVbXWQ%2B55Pge6k8XLr%2BphnRSPMCbzlQaBaylqKm7Vxts%2BmB2IHERJUNbvizfan4nHfPadZP77ByLbPJbWZ1jJbpc4GGnyqZ66V3%2Bc2aIMXHquONqfQGo7rQUmoMknC2l6fb2555wgQvjtrg4XR0PAM0Q7K4L4UOcLMTQ9ZNs%2BXh7kDgOkaX057FoCb8WSnlolGH5kV4Ca7IBqGlGfHmR1XUyVODknG1VKO%2BZ3%2BWGcXmPHbk8v%2BJ80BC5DoHmVVToFLoZpAkaFOWL%2FoKX7iZTBlHT0DOnThP%2Bcyd0nRB%2B%2Bq6JngpNpH3Bvi7woXi2RTsHqeV8Ierm18k4n%2FDuSFvR%2B9H%2BhvZItCdbcGSs1ZZu16fGbYqg5%2BBcWvrUniJF9sXtEDj53GIEYRhsmE98GPih%2FsUJGdJtvDWSsxFEX9vNlwfoEB%2Fz4ISH7dFqVpnug%2BIZhfe%2Bdgkz2%2B9BbnUEwqYmViJnUS3YuAR1%2FDjx0%2B63FfC8R%2BIeJBGhgZOajieqft3y9bdNGTbBTXPc0LrtH%2FAoNAiu3JJCJ4M4tc477GraqcLAw%2F972zgY6pgFD%2FZs5oFwBqo3psF9dBtAKC7Tae7E%2FjrJploazLjFanUMI6yLxBD6LoRs6UoK3t61oX2nsfO4zkV5nBgbnlJ5ZBS%2BkdzmxMuuYQgjBVTOVhWSk4T30JN%2F2p7dPj04tqm77RVRFDFcl7oRJvn0j93Zk%2B5p2xGGQl5ZayKY0pWR3qbGAiE9SdpwL25fQ8p3tJRNeCCqMzzYU9CIt27HtDcsIJglSwZEB&X-Amz-Signature=24a868ee8aad00bdfb1a0e9f0e21910709e68286d69e253a2343f569edd30287&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XITAYNSE%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICHK%2F%2BV6Qt5843U50e5vCGTdUTmAgy4LN8MCnJoZhGvQAiB0D56bSLIOUgD%2BzAFaNlMDB%2BEv%2FrQNdee8Yn2Mc2je4iqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTXz9iqPGKNv48XU4KtwDrJ8pyjKkI%2F2qvfeSkBArNPxER2CTOatyaiqYnt%2Fjejy%2B86j3hFb39fA4JpbyEZFdsjLE%2FVUGB4JZ%2Fcd%2BVbXWQ%2B55Pge6k8XLr%2BphnRSPMCbzlQaBaylqKm7Vxts%2BmB2IHERJUNbvizfan4nHfPadZP77ByLbPJbWZ1jJbpc4GGnyqZ66V3%2Bc2aIMXHquONqfQGo7rQUmoMknC2l6fb2555wgQvjtrg4XR0PAM0Q7K4L4UOcLMTQ9ZNs%2BXh7kDgOkaX057FoCb8WSnlolGH5kV4Ca7IBqGlGfHmR1XUyVODknG1VKO%2BZ3%2BWGcXmPHbk8v%2BJ80BC5DoHmVVToFLoZpAkaFOWL%2FoKX7iZTBlHT0DOnThP%2Bcyd0nRB%2B%2Bq6JngpNpH3Bvi7woXi2RTsHqeV8Ierm18k4n%2FDuSFvR%2B9H%2BhvZItCdbcGSs1ZZu16fGbYqg5%2BBcWvrUniJF9sXtEDj53GIEYRhsmE98GPih%2FsUJGdJtvDWSsxFEX9vNlwfoEB%2Fz4ISH7dFqVpnug%2BIZhfe%2Bdgkz2%2B9BbnUEwqYmViJnUS3YuAR1%2FDjx0%2B63FfC8R%2BIeJBGhgZOajieqft3y9bdNGTbBTXPc0LrtH%2FAoNAiu3JJCJ4M4tc477GraqcLAw%2F972zgY6pgFD%2FZs5oFwBqo3psF9dBtAKC7Tae7E%2FjrJploazLjFanUMI6yLxBD6LoRs6UoK3t61oX2nsfO4zkV5nBgbnlJ5ZBS%2BkdzmxMuuYQgjBVTOVhWSk4T30JN%2F2p7dPj04tqm77RVRFDFcl7oRJvn0j93Zk%2B5p2xGGQl5ZayKY0pWR3qbGAiE9SdpwL25fQ8p3tJRNeCCqMzzYU9CIt27HtDcsIJglSwZEB&X-Amz-Signature=f6391f04653470cd2d41a099f90e213e77aa860bdbef4ada6bb2c6b04fec1a67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XITAYNSE%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICHK%2F%2BV6Qt5843U50e5vCGTdUTmAgy4LN8MCnJoZhGvQAiB0D56bSLIOUgD%2BzAFaNlMDB%2BEv%2FrQNdee8Yn2Mc2je4iqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTXz9iqPGKNv48XU4KtwDrJ8pyjKkI%2F2qvfeSkBArNPxER2CTOatyaiqYnt%2Fjejy%2B86j3hFb39fA4JpbyEZFdsjLE%2FVUGB4JZ%2Fcd%2BVbXWQ%2B55Pge6k8XLr%2BphnRSPMCbzlQaBaylqKm7Vxts%2BmB2IHERJUNbvizfan4nHfPadZP77ByLbPJbWZ1jJbpc4GGnyqZ66V3%2Bc2aIMXHquONqfQGo7rQUmoMknC2l6fb2555wgQvjtrg4XR0PAM0Q7K4L4UOcLMTQ9ZNs%2BXh7kDgOkaX057FoCb8WSnlolGH5kV4Ca7IBqGlGfHmR1XUyVODknG1VKO%2BZ3%2BWGcXmPHbk8v%2BJ80BC5DoHmVVToFLoZpAkaFOWL%2FoKX7iZTBlHT0DOnThP%2Bcyd0nRB%2B%2Bq6JngpNpH3Bvi7woXi2RTsHqeV8Ierm18k4n%2FDuSFvR%2B9H%2BhvZItCdbcGSs1ZZu16fGbYqg5%2BBcWvrUniJF9sXtEDj53GIEYRhsmE98GPih%2FsUJGdJtvDWSsxFEX9vNlwfoEB%2Fz4ISH7dFqVpnug%2BIZhfe%2Bdgkz2%2B9BbnUEwqYmViJnUS3YuAR1%2FDjx0%2B63FfC8R%2BIeJBGhgZOajieqft3y9bdNGTbBTXPc0LrtH%2FAoNAiu3JJCJ4M4tc477GraqcLAw%2F972zgY6pgFD%2FZs5oFwBqo3psF9dBtAKC7Tae7E%2FjrJploazLjFanUMI6yLxBD6LoRs6UoK3t61oX2nsfO4zkV5nBgbnlJ5ZBS%2BkdzmxMuuYQgjBVTOVhWSk4T30JN%2F2p7dPj04tqm77RVRFDFcl7oRJvn0j93Zk%2B5p2xGGQl5ZayKY0pWR3qbGAiE9SdpwL25fQ8p3tJRNeCCqMzzYU9CIt27HtDcsIJglSwZEB&X-Amz-Signature=f7110f451e173ec729ad9a3f7854e54499cbf6b891e6bf556e36da6377b0647b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XITAYNSE%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICHK%2F%2BV6Qt5843U50e5vCGTdUTmAgy4LN8MCnJoZhGvQAiB0D56bSLIOUgD%2BzAFaNlMDB%2BEv%2FrQNdee8Yn2Mc2je4iqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTXz9iqPGKNv48XU4KtwDrJ8pyjKkI%2F2qvfeSkBArNPxER2CTOatyaiqYnt%2Fjejy%2B86j3hFb39fA4JpbyEZFdsjLE%2FVUGB4JZ%2Fcd%2BVbXWQ%2B55Pge6k8XLr%2BphnRSPMCbzlQaBaylqKm7Vxts%2BmB2IHERJUNbvizfan4nHfPadZP77ByLbPJbWZ1jJbpc4GGnyqZ66V3%2Bc2aIMXHquONqfQGo7rQUmoMknC2l6fb2555wgQvjtrg4XR0PAM0Q7K4L4UOcLMTQ9ZNs%2BXh7kDgOkaX057FoCb8WSnlolGH5kV4Ca7IBqGlGfHmR1XUyVODknG1VKO%2BZ3%2BWGcXmPHbk8v%2BJ80BC5DoHmVVToFLoZpAkaFOWL%2FoKX7iZTBlHT0DOnThP%2Bcyd0nRB%2B%2Bq6JngpNpH3Bvi7woXi2RTsHqeV8Ierm18k4n%2FDuSFvR%2B9H%2BhvZItCdbcGSs1ZZu16fGbYqg5%2BBcWvrUniJF9sXtEDj53GIEYRhsmE98GPih%2FsUJGdJtvDWSsxFEX9vNlwfoEB%2Fz4ISH7dFqVpnug%2BIZhfe%2Bdgkz2%2B9BbnUEwqYmViJnUS3YuAR1%2FDjx0%2B63FfC8R%2BIeJBGhgZOajieqft3y9bdNGTbBTXPc0LrtH%2FAoNAiu3JJCJ4M4tc477GraqcLAw%2F972zgY6pgFD%2FZs5oFwBqo3psF9dBtAKC7Tae7E%2FjrJploazLjFanUMI6yLxBD6LoRs6UoK3t61oX2nsfO4zkV5nBgbnlJ5ZBS%2BkdzmxMuuYQgjBVTOVhWSk4T30JN%2F2p7dPj04tqm77RVRFDFcl7oRJvn0j93Zk%2B5p2xGGQl5ZayKY0pWR3qbGAiE9SdpwL25fQ8p3tJRNeCCqMzzYU9CIt27HtDcsIJglSwZEB&X-Amz-Signature=4a330fb996cf525e14319977c6428399ee98e749f676c1037d0249d7c6475030&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

