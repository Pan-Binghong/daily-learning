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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S2C2FO4%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk2ywTjZsnFwoUvQIJaVhCIJ6XC1NoB%2BS79CKuPZa6nwIga7YSi2a0q2ThGKwRMFWFkGPxim7d9uopEjhsApgHiK8qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHu7Z6wYoufX%2FzJFwircA4GcuI0l7QoqLGvOIF6qE4UdZ%2BRxEfbqS%2FxN%2Fr7oxYQj15vjfmMm%2Bt5W5Z9ExiBVfz1xUVQhWPiqKfnrGHyUOv4q2mW7aBc2mpgOCzs4xzf7YA%2BvqJ79aHl6DMl5OuplDueIcU3GILMQf5KP6wCWK8IVsYScqIqeE7bkOuvo8C3HucOXTpzdOD62koP%2BYzNMs0s3DAJHMyoVgVNVl4xjKeY9eOs%2Fq2GLD%2FfZg4ejWMuFy8OwtDhJcBa%2BdOGUPDE%2BmtspTFfkZSeaybfn%2FaI1iRIltNZLb31qN15DGzHiLU%2F0LwGDWuJv%2F766I4NduV59WTuMbmkcfHrN9VuqmVTWXKI0tQHSEh%2FOgf7iO6tb1wlZRgYDnJLkWlmGcGnxQJVetxnqtakR9MnGc8GvyCbcShPT4EePjJWiwhWgJ24casw%2BPadXU3oMfLjwFaYys9QRHX6ZhKvz%2Fvplb5BAqqD%2FmkKNqKyG0qs75dR09C%2BFB5Xf2V9beiZtcHLcBfCZDNi1y7LSZxT%2FZETyfQIbf9%2FtBlIgYi41tjqf03gYnOxVa%2BZYargucAcVd6D7BJ%2BAaI9YRcasaX1Zjrkel0Pngld9IbUdT0%2FdYNl8VK78Apx9BNo66N761ulfAHb8HP1MMODz6cwGOqUBNIMs9mfMV6jkYnVl3zG60X5Dn2WR1fvZCO5vn6h44t387bnLhrGGDnbaFxyUvmR%2BxNOMzFbSqP%2FbumVyXNv90OVjgkjVelIv516tAaDvQfT%2FRcrxOAdsFu8WaTmD4YPEBvBYDRKt2Adl3nCmo6aL5ejwPipsQF3OrYu8k62BLmS42ND0HIM93guDCmxoo3WZAmcPBbMXKXYRdjNPFq60MKjzqrNS&X-Amz-Signature=0467ef51effde9a2b39ec01553ac89270ff01ae61a527ac064388f8de6bab30e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S2C2FO4%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk2ywTjZsnFwoUvQIJaVhCIJ6XC1NoB%2BS79CKuPZa6nwIga7YSi2a0q2ThGKwRMFWFkGPxim7d9uopEjhsApgHiK8qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHu7Z6wYoufX%2FzJFwircA4GcuI0l7QoqLGvOIF6qE4UdZ%2BRxEfbqS%2FxN%2Fr7oxYQj15vjfmMm%2Bt5W5Z9ExiBVfz1xUVQhWPiqKfnrGHyUOv4q2mW7aBc2mpgOCzs4xzf7YA%2BvqJ79aHl6DMl5OuplDueIcU3GILMQf5KP6wCWK8IVsYScqIqeE7bkOuvo8C3HucOXTpzdOD62koP%2BYzNMs0s3DAJHMyoVgVNVl4xjKeY9eOs%2Fq2GLD%2FfZg4ejWMuFy8OwtDhJcBa%2BdOGUPDE%2BmtspTFfkZSeaybfn%2FaI1iRIltNZLb31qN15DGzHiLU%2F0LwGDWuJv%2F766I4NduV59WTuMbmkcfHrN9VuqmVTWXKI0tQHSEh%2FOgf7iO6tb1wlZRgYDnJLkWlmGcGnxQJVetxnqtakR9MnGc8GvyCbcShPT4EePjJWiwhWgJ24casw%2BPadXU3oMfLjwFaYys9QRHX6ZhKvz%2Fvplb5BAqqD%2FmkKNqKyG0qs75dR09C%2BFB5Xf2V9beiZtcHLcBfCZDNi1y7LSZxT%2FZETyfQIbf9%2FtBlIgYi41tjqf03gYnOxVa%2BZYargucAcVd6D7BJ%2BAaI9YRcasaX1Zjrkel0Pngld9IbUdT0%2FdYNl8VK78Apx9BNo66N761ulfAHb8HP1MMODz6cwGOqUBNIMs9mfMV6jkYnVl3zG60X5Dn2WR1fvZCO5vn6h44t387bnLhrGGDnbaFxyUvmR%2BxNOMzFbSqP%2FbumVyXNv90OVjgkjVelIv516tAaDvQfT%2FRcrxOAdsFu8WaTmD4YPEBvBYDRKt2Adl3nCmo6aL5ejwPipsQF3OrYu8k62BLmS42ND0HIM93guDCmxoo3WZAmcPBbMXKXYRdjNPFq60MKjzqrNS&X-Amz-Signature=5dbbfed47f61ef2e5cee6f4966a3c37afb30a3be40ac910c83dfe6c7bbb770cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S2C2FO4%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk2ywTjZsnFwoUvQIJaVhCIJ6XC1NoB%2BS79CKuPZa6nwIga7YSi2a0q2ThGKwRMFWFkGPxim7d9uopEjhsApgHiK8qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHu7Z6wYoufX%2FzJFwircA4GcuI0l7QoqLGvOIF6qE4UdZ%2BRxEfbqS%2FxN%2Fr7oxYQj15vjfmMm%2Bt5W5Z9ExiBVfz1xUVQhWPiqKfnrGHyUOv4q2mW7aBc2mpgOCzs4xzf7YA%2BvqJ79aHl6DMl5OuplDueIcU3GILMQf5KP6wCWK8IVsYScqIqeE7bkOuvo8C3HucOXTpzdOD62koP%2BYzNMs0s3DAJHMyoVgVNVl4xjKeY9eOs%2Fq2GLD%2FfZg4ejWMuFy8OwtDhJcBa%2BdOGUPDE%2BmtspTFfkZSeaybfn%2FaI1iRIltNZLb31qN15DGzHiLU%2F0LwGDWuJv%2F766I4NduV59WTuMbmkcfHrN9VuqmVTWXKI0tQHSEh%2FOgf7iO6tb1wlZRgYDnJLkWlmGcGnxQJVetxnqtakR9MnGc8GvyCbcShPT4EePjJWiwhWgJ24casw%2BPadXU3oMfLjwFaYys9QRHX6ZhKvz%2Fvplb5BAqqD%2FmkKNqKyG0qs75dR09C%2BFB5Xf2V9beiZtcHLcBfCZDNi1y7LSZxT%2FZETyfQIbf9%2FtBlIgYi41tjqf03gYnOxVa%2BZYargucAcVd6D7BJ%2BAaI9YRcasaX1Zjrkel0Pngld9IbUdT0%2FdYNl8VK78Apx9BNo66N761ulfAHb8HP1MMODz6cwGOqUBNIMs9mfMV6jkYnVl3zG60X5Dn2WR1fvZCO5vn6h44t387bnLhrGGDnbaFxyUvmR%2BxNOMzFbSqP%2FbumVyXNv90OVjgkjVelIv516tAaDvQfT%2FRcrxOAdsFu8WaTmD4YPEBvBYDRKt2Adl3nCmo6aL5ejwPipsQF3OrYu8k62BLmS42ND0HIM93guDCmxoo3WZAmcPBbMXKXYRdjNPFq60MKjzqrNS&X-Amz-Signature=a4acd52dbf3dfcde096503e440903cf0c2040be0869bf4dd181bb0e5bdb1fb07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S2C2FO4%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk2ywTjZsnFwoUvQIJaVhCIJ6XC1NoB%2BS79CKuPZa6nwIga7YSi2a0q2ThGKwRMFWFkGPxim7d9uopEjhsApgHiK8qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHu7Z6wYoufX%2FzJFwircA4GcuI0l7QoqLGvOIF6qE4UdZ%2BRxEfbqS%2FxN%2Fr7oxYQj15vjfmMm%2Bt5W5Z9ExiBVfz1xUVQhWPiqKfnrGHyUOv4q2mW7aBc2mpgOCzs4xzf7YA%2BvqJ79aHl6DMl5OuplDueIcU3GILMQf5KP6wCWK8IVsYScqIqeE7bkOuvo8C3HucOXTpzdOD62koP%2BYzNMs0s3DAJHMyoVgVNVl4xjKeY9eOs%2Fq2GLD%2FfZg4ejWMuFy8OwtDhJcBa%2BdOGUPDE%2BmtspTFfkZSeaybfn%2FaI1iRIltNZLb31qN15DGzHiLU%2F0LwGDWuJv%2F766I4NduV59WTuMbmkcfHrN9VuqmVTWXKI0tQHSEh%2FOgf7iO6tb1wlZRgYDnJLkWlmGcGnxQJVetxnqtakR9MnGc8GvyCbcShPT4EePjJWiwhWgJ24casw%2BPadXU3oMfLjwFaYys9QRHX6ZhKvz%2Fvplb5BAqqD%2FmkKNqKyG0qs75dR09C%2BFB5Xf2V9beiZtcHLcBfCZDNi1y7LSZxT%2FZETyfQIbf9%2FtBlIgYi41tjqf03gYnOxVa%2BZYargucAcVd6D7BJ%2BAaI9YRcasaX1Zjrkel0Pngld9IbUdT0%2FdYNl8VK78Apx9BNo66N761ulfAHb8HP1MMODz6cwGOqUBNIMs9mfMV6jkYnVl3zG60X5Dn2WR1fvZCO5vn6h44t387bnLhrGGDnbaFxyUvmR%2BxNOMzFbSqP%2FbumVyXNv90OVjgkjVelIv516tAaDvQfT%2FRcrxOAdsFu8WaTmD4YPEBvBYDRKt2Adl3nCmo6aL5ejwPipsQF3OrYu8k62BLmS42ND0HIM93guDCmxoo3WZAmcPBbMXKXYRdjNPFq60MKjzqrNS&X-Amz-Signature=33bdfb1b3d702f6f187c27f85e5bae1433a7c454ac50c560d80e1d358cc13123&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S2C2FO4%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk2ywTjZsnFwoUvQIJaVhCIJ6XC1NoB%2BS79CKuPZa6nwIga7YSi2a0q2ThGKwRMFWFkGPxim7d9uopEjhsApgHiK8qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHu7Z6wYoufX%2FzJFwircA4GcuI0l7QoqLGvOIF6qE4UdZ%2BRxEfbqS%2FxN%2Fr7oxYQj15vjfmMm%2Bt5W5Z9ExiBVfz1xUVQhWPiqKfnrGHyUOv4q2mW7aBc2mpgOCzs4xzf7YA%2BvqJ79aHl6DMl5OuplDueIcU3GILMQf5KP6wCWK8IVsYScqIqeE7bkOuvo8C3HucOXTpzdOD62koP%2BYzNMs0s3DAJHMyoVgVNVl4xjKeY9eOs%2Fq2GLD%2FfZg4ejWMuFy8OwtDhJcBa%2BdOGUPDE%2BmtspTFfkZSeaybfn%2FaI1iRIltNZLb31qN15DGzHiLU%2F0LwGDWuJv%2F766I4NduV59WTuMbmkcfHrN9VuqmVTWXKI0tQHSEh%2FOgf7iO6tb1wlZRgYDnJLkWlmGcGnxQJVetxnqtakR9MnGc8GvyCbcShPT4EePjJWiwhWgJ24casw%2BPadXU3oMfLjwFaYys9QRHX6ZhKvz%2Fvplb5BAqqD%2FmkKNqKyG0qs75dR09C%2BFB5Xf2V9beiZtcHLcBfCZDNi1y7LSZxT%2FZETyfQIbf9%2FtBlIgYi41tjqf03gYnOxVa%2BZYargucAcVd6D7BJ%2BAaI9YRcasaX1Zjrkel0Pngld9IbUdT0%2FdYNl8VK78Apx9BNo66N761ulfAHb8HP1MMODz6cwGOqUBNIMs9mfMV6jkYnVl3zG60X5Dn2WR1fvZCO5vn6h44t387bnLhrGGDnbaFxyUvmR%2BxNOMzFbSqP%2FbumVyXNv90OVjgkjVelIv516tAaDvQfT%2FRcrxOAdsFu8WaTmD4YPEBvBYDRKt2Adl3nCmo6aL5ejwPipsQF3OrYu8k62BLmS42ND0HIM93guDCmxoo3WZAmcPBbMXKXYRdjNPFq60MKjzqrNS&X-Amz-Signature=814a42a85517212faff0daf1ace6aad31958c5de0ef6a9ffa71552b7f4765f76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S2C2FO4%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk2ywTjZsnFwoUvQIJaVhCIJ6XC1NoB%2BS79CKuPZa6nwIga7YSi2a0q2ThGKwRMFWFkGPxim7d9uopEjhsApgHiK8qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHu7Z6wYoufX%2FzJFwircA4GcuI0l7QoqLGvOIF6qE4UdZ%2BRxEfbqS%2FxN%2Fr7oxYQj15vjfmMm%2Bt5W5Z9ExiBVfz1xUVQhWPiqKfnrGHyUOv4q2mW7aBc2mpgOCzs4xzf7YA%2BvqJ79aHl6DMl5OuplDueIcU3GILMQf5KP6wCWK8IVsYScqIqeE7bkOuvo8C3HucOXTpzdOD62koP%2BYzNMs0s3DAJHMyoVgVNVl4xjKeY9eOs%2Fq2GLD%2FfZg4ejWMuFy8OwtDhJcBa%2BdOGUPDE%2BmtspTFfkZSeaybfn%2FaI1iRIltNZLb31qN15DGzHiLU%2F0LwGDWuJv%2F766I4NduV59WTuMbmkcfHrN9VuqmVTWXKI0tQHSEh%2FOgf7iO6tb1wlZRgYDnJLkWlmGcGnxQJVetxnqtakR9MnGc8GvyCbcShPT4EePjJWiwhWgJ24casw%2BPadXU3oMfLjwFaYys9QRHX6ZhKvz%2Fvplb5BAqqD%2FmkKNqKyG0qs75dR09C%2BFB5Xf2V9beiZtcHLcBfCZDNi1y7LSZxT%2FZETyfQIbf9%2FtBlIgYi41tjqf03gYnOxVa%2BZYargucAcVd6D7BJ%2BAaI9YRcasaX1Zjrkel0Pngld9IbUdT0%2FdYNl8VK78Apx9BNo66N761ulfAHb8HP1MMODz6cwGOqUBNIMs9mfMV6jkYnVl3zG60X5Dn2WR1fvZCO5vn6h44t387bnLhrGGDnbaFxyUvmR%2BxNOMzFbSqP%2FbumVyXNv90OVjgkjVelIv516tAaDvQfT%2FRcrxOAdsFu8WaTmD4YPEBvBYDRKt2Adl3nCmo6aL5ejwPipsQF3OrYu8k62BLmS42ND0HIM93guDCmxoo3WZAmcPBbMXKXYRdjNPFq60MKjzqrNS&X-Amz-Signature=4919139ddd4136bb26ee3d153c5c5e310a0dc011b6b1df65b347bf5697cbff8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S2C2FO4%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk2ywTjZsnFwoUvQIJaVhCIJ6XC1NoB%2BS79CKuPZa6nwIga7YSi2a0q2ThGKwRMFWFkGPxim7d9uopEjhsApgHiK8qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHu7Z6wYoufX%2FzJFwircA4GcuI0l7QoqLGvOIF6qE4UdZ%2BRxEfbqS%2FxN%2Fr7oxYQj15vjfmMm%2Bt5W5Z9ExiBVfz1xUVQhWPiqKfnrGHyUOv4q2mW7aBc2mpgOCzs4xzf7YA%2BvqJ79aHl6DMl5OuplDueIcU3GILMQf5KP6wCWK8IVsYScqIqeE7bkOuvo8C3HucOXTpzdOD62koP%2BYzNMs0s3DAJHMyoVgVNVl4xjKeY9eOs%2Fq2GLD%2FfZg4ejWMuFy8OwtDhJcBa%2BdOGUPDE%2BmtspTFfkZSeaybfn%2FaI1iRIltNZLb31qN15DGzHiLU%2F0LwGDWuJv%2F766I4NduV59WTuMbmkcfHrN9VuqmVTWXKI0tQHSEh%2FOgf7iO6tb1wlZRgYDnJLkWlmGcGnxQJVetxnqtakR9MnGc8GvyCbcShPT4EePjJWiwhWgJ24casw%2BPadXU3oMfLjwFaYys9QRHX6ZhKvz%2Fvplb5BAqqD%2FmkKNqKyG0qs75dR09C%2BFB5Xf2V9beiZtcHLcBfCZDNi1y7LSZxT%2FZETyfQIbf9%2FtBlIgYi41tjqf03gYnOxVa%2BZYargucAcVd6D7BJ%2BAaI9YRcasaX1Zjrkel0Pngld9IbUdT0%2FdYNl8VK78Apx9BNo66N761ulfAHb8HP1MMODz6cwGOqUBNIMs9mfMV6jkYnVl3zG60X5Dn2WR1fvZCO5vn6h44t387bnLhrGGDnbaFxyUvmR%2BxNOMzFbSqP%2FbumVyXNv90OVjgkjVelIv516tAaDvQfT%2FRcrxOAdsFu8WaTmD4YPEBvBYDRKt2Adl3nCmo6aL5ejwPipsQF3OrYu8k62BLmS42ND0HIM93guDCmxoo3WZAmcPBbMXKXYRdjNPFq60MKjzqrNS&X-Amz-Signature=6b265c664a67eff81537808305453d526de669546bcc499385a9070f8619e3ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

