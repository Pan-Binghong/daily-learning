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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FZW4K52%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDpHlPkp8udOp1ZADuPsPblHthZa6Opw9KBvHCq9zA4jwIhAPA1Zk9UgWwcG0uuM%2F4aQLo7Bk%2BUvrdgrIorbduGzkrWKv8DCBQQABoMNjM3NDIzMTgzODA1IgyFwEGAq5Vzk9MzuW4q3ANOKI3hNIJnhf8tznb1fLRF%2Fylod88UOp50087ccvs5a7py5gcRgRFw5fIGC%2BFnEeyr42ofOBpT4I0ycEkimTRkaQItVczbMqTSzuhP9kkSejrh63W5B5q8Jyt1UZjakQv22YVud9aceE0%2BEWzfsxmrWGjftI7Wbq%2ByZRosv8kddjWdOtP3%2FEKHh1t%2Ba25havxwlpIIX3OKetbmsk%2FzQLDS3Vp2cB18TRgVY0EOiatgfs6oMpw%2BU2s00yzYqS9r%2FHW8zEO45Q3jyn5FlUZBZfRMlX5jqfs%2FG6maSlpC7k51ZA59MR6s39kKCQIR%2FiTVrX2fmOE7VBhEhYURbE3%2BpADrhPW%2BH9nW4DsxcYNA27V5Sd%2BBro78i4ALl7tF3bZs4KBRqwf8SKYG7IFghTvCNsEiJWU6mW%2Fwnxx3Hd7UJSXyIzMswkxreLhc1ZGNgyhpWt%2Fg1e%2BYrDx6365Cc18rPo6ji%2BiPdgwT8yAKjeLcLWONHINPyeTkQolHDPIP%2FM4N6sNrXWTCMvfCc5AIguDGF2%2BRJZ9ohnyKHrFjmzpZyZGsEgkUw%2BcJCn3pPt62u%2BWk6BxQVcDYZRudWZoLfsLLadDS1WK%2BV6iFqG5tjyGym%2FicbwAZhd8X9WV%2BvIsrCDD2xu3NBjqkARmvHFScdNhLC9VdZFh78LXxzHOA4HWHeZ%2B77I4A3QJoW44%2F2QouFH%2FjFfO6iunWMNl12EDP5n8L1CvgPDHSF25LFgKOTixiXWvcCuIz%2F0LAE90AuVBv9H5fuc9DBd9GCR4lkJAsQQJZZxqImPn8xAiEUwNL5BDX51pB0NWt6jX1mw0Gy08L%2BOs%2BJ8q%2FuNhrPyXJGnuZSBC2b%2BWDALiKzVofztXA&X-Amz-Signature=b711cd7bc5b5a0c363ebe9b589f8ebb57c788f44a5f7b2d3a7570a5270c0379f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FZW4K52%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDpHlPkp8udOp1ZADuPsPblHthZa6Opw9KBvHCq9zA4jwIhAPA1Zk9UgWwcG0uuM%2F4aQLo7Bk%2BUvrdgrIorbduGzkrWKv8DCBQQABoMNjM3NDIzMTgzODA1IgyFwEGAq5Vzk9MzuW4q3ANOKI3hNIJnhf8tznb1fLRF%2Fylod88UOp50087ccvs5a7py5gcRgRFw5fIGC%2BFnEeyr42ofOBpT4I0ycEkimTRkaQItVczbMqTSzuhP9kkSejrh63W5B5q8Jyt1UZjakQv22YVud9aceE0%2BEWzfsxmrWGjftI7Wbq%2ByZRosv8kddjWdOtP3%2FEKHh1t%2Ba25havxwlpIIX3OKetbmsk%2FzQLDS3Vp2cB18TRgVY0EOiatgfs6oMpw%2BU2s00yzYqS9r%2FHW8zEO45Q3jyn5FlUZBZfRMlX5jqfs%2FG6maSlpC7k51ZA59MR6s39kKCQIR%2FiTVrX2fmOE7VBhEhYURbE3%2BpADrhPW%2BH9nW4DsxcYNA27V5Sd%2BBro78i4ALl7tF3bZs4KBRqwf8SKYG7IFghTvCNsEiJWU6mW%2Fwnxx3Hd7UJSXyIzMswkxreLhc1ZGNgyhpWt%2Fg1e%2BYrDx6365Cc18rPo6ji%2BiPdgwT8yAKjeLcLWONHINPyeTkQolHDPIP%2FM4N6sNrXWTCMvfCc5AIguDGF2%2BRJZ9ohnyKHrFjmzpZyZGsEgkUw%2BcJCn3pPt62u%2BWk6BxQVcDYZRudWZoLfsLLadDS1WK%2BV6iFqG5tjyGym%2FicbwAZhd8X9WV%2BvIsrCDD2xu3NBjqkARmvHFScdNhLC9VdZFh78LXxzHOA4HWHeZ%2B77I4A3QJoW44%2F2QouFH%2FjFfO6iunWMNl12EDP5n8L1CvgPDHSF25LFgKOTixiXWvcCuIz%2F0LAE90AuVBv9H5fuc9DBd9GCR4lkJAsQQJZZxqImPn8xAiEUwNL5BDX51pB0NWt6jX1mw0Gy08L%2BOs%2BJ8q%2FuNhrPyXJGnuZSBC2b%2BWDALiKzVofztXA&X-Amz-Signature=ca47a4ad01432c0990692e1aae255ec4776c818033732e38e52b9f6af2659440&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FZW4K52%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDpHlPkp8udOp1ZADuPsPblHthZa6Opw9KBvHCq9zA4jwIhAPA1Zk9UgWwcG0uuM%2F4aQLo7Bk%2BUvrdgrIorbduGzkrWKv8DCBQQABoMNjM3NDIzMTgzODA1IgyFwEGAq5Vzk9MzuW4q3ANOKI3hNIJnhf8tznb1fLRF%2Fylod88UOp50087ccvs5a7py5gcRgRFw5fIGC%2BFnEeyr42ofOBpT4I0ycEkimTRkaQItVczbMqTSzuhP9kkSejrh63W5B5q8Jyt1UZjakQv22YVud9aceE0%2BEWzfsxmrWGjftI7Wbq%2ByZRosv8kddjWdOtP3%2FEKHh1t%2Ba25havxwlpIIX3OKetbmsk%2FzQLDS3Vp2cB18TRgVY0EOiatgfs6oMpw%2BU2s00yzYqS9r%2FHW8zEO45Q3jyn5FlUZBZfRMlX5jqfs%2FG6maSlpC7k51ZA59MR6s39kKCQIR%2FiTVrX2fmOE7VBhEhYURbE3%2BpADrhPW%2BH9nW4DsxcYNA27V5Sd%2BBro78i4ALl7tF3bZs4KBRqwf8SKYG7IFghTvCNsEiJWU6mW%2Fwnxx3Hd7UJSXyIzMswkxreLhc1ZGNgyhpWt%2Fg1e%2BYrDx6365Cc18rPo6ji%2BiPdgwT8yAKjeLcLWONHINPyeTkQolHDPIP%2FM4N6sNrXWTCMvfCc5AIguDGF2%2BRJZ9ohnyKHrFjmzpZyZGsEgkUw%2BcJCn3pPt62u%2BWk6BxQVcDYZRudWZoLfsLLadDS1WK%2BV6iFqG5tjyGym%2FicbwAZhd8X9WV%2BvIsrCDD2xu3NBjqkARmvHFScdNhLC9VdZFh78LXxzHOA4HWHeZ%2B77I4A3QJoW44%2F2QouFH%2FjFfO6iunWMNl12EDP5n8L1CvgPDHSF25LFgKOTixiXWvcCuIz%2F0LAE90AuVBv9H5fuc9DBd9GCR4lkJAsQQJZZxqImPn8xAiEUwNL5BDX51pB0NWt6jX1mw0Gy08L%2BOs%2BJ8q%2FuNhrPyXJGnuZSBC2b%2BWDALiKzVofztXA&X-Amz-Signature=5910cb9f2a57d8756b02fd07f367c1f020ae0b19113d2d699170443b274dce5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FZW4K52%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDpHlPkp8udOp1ZADuPsPblHthZa6Opw9KBvHCq9zA4jwIhAPA1Zk9UgWwcG0uuM%2F4aQLo7Bk%2BUvrdgrIorbduGzkrWKv8DCBQQABoMNjM3NDIzMTgzODA1IgyFwEGAq5Vzk9MzuW4q3ANOKI3hNIJnhf8tznb1fLRF%2Fylod88UOp50087ccvs5a7py5gcRgRFw5fIGC%2BFnEeyr42ofOBpT4I0ycEkimTRkaQItVczbMqTSzuhP9kkSejrh63W5B5q8Jyt1UZjakQv22YVud9aceE0%2BEWzfsxmrWGjftI7Wbq%2ByZRosv8kddjWdOtP3%2FEKHh1t%2Ba25havxwlpIIX3OKetbmsk%2FzQLDS3Vp2cB18TRgVY0EOiatgfs6oMpw%2BU2s00yzYqS9r%2FHW8zEO45Q3jyn5FlUZBZfRMlX5jqfs%2FG6maSlpC7k51ZA59MR6s39kKCQIR%2FiTVrX2fmOE7VBhEhYURbE3%2BpADrhPW%2BH9nW4DsxcYNA27V5Sd%2BBro78i4ALl7tF3bZs4KBRqwf8SKYG7IFghTvCNsEiJWU6mW%2Fwnxx3Hd7UJSXyIzMswkxreLhc1ZGNgyhpWt%2Fg1e%2BYrDx6365Cc18rPo6ji%2BiPdgwT8yAKjeLcLWONHINPyeTkQolHDPIP%2FM4N6sNrXWTCMvfCc5AIguDGF2%2BRJZ9ohnyKHrFjmzpZyZGsEgkUw%2BcJCn3pPt62u%2BWk6BxQVcDYZRudWZoLfsLLadDS1WK%2BV6iFqG5tjyGym%2FicbwAZhd8X9WV%2BvIsrCDD2xu3NBjqkARmvHFScdNhLC9VdZFh78LXxzHOA4HWHeZ%2B77I4A3QJoW44%2F2QouFH%2FjFfO6iunWMNl12EDP5n8L1CvgPDHSF25LFgKOTixiXWvcCuIz%2F0LAE90AuVBv9H5fuc9DBd9GCR4lkJAsQQJZZxqImPn8xAiEUwNL5BDX51pB0NWt6jX1mw0Gy08L%2BOs%2BJ8q%2FuNhrPyXJGnuZSBC2b%2BWDALiKzVofztXA&X-Amz-Signature=386b79236305ae509f2e6fbe456916c200397986556c5fb8f3f077107780f516&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FZW4K52%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDpHlPkp8udOp1ZADuPsPblHthZa6Opw9KBvHCq9zA4jwIhAPA1Zk9UgWwcG0uuM%2F4aQLo7Bk%2BUvrdgrIorbduGzkrWKv8DCBQQABoMNjM3NDIzMTgzODA1IgyFwEGAq5Vzk9MzuW4q3ANOKI3hNIJnhf8tznb1fLRF%2Fylod88UOp50087ccvs5a7py5gcRgRFw5fIGC%2BFnEeyr42ofOBpT4I0ycEkimTRkaQItVczbMqTSzuhP9kkSejrh63W5B5q8Jyt1UZjakQv22YVud9aceE0%2BEWzfsxmrWGjftI7Wbq%2ByZRosv8kddjWdOtP3%2FEKHh1t%2Ba25havxwlpIIX3OKetbmsk%2FzQLDS3Vp2cB18TRgVY0EOiatgfs6oMpw%2BU2s00yzYqS9r%2FHW8zEO45Q3jyn5FlUZBZfRMlX5jqfs%2FG6maSlpC7k51ZA59MR6s39kKCQIR%2FiTVrX2fmOE7VBhEhYURbE3%2BpADrhPW%2BH9nW4DsxcYNA27V5Sd%2BBro78i4ALl7tF3bZs4KBRqwf8SKYG7IFghTvCNsEiJWU6mW%2Fwnxx3Hd7UJSXyIzMswkxreLhc1ZGNgyhpWt%2Fg1e%2BYrDx6365Cc18rPo6ji%2BiPdgwT8yAKjeLcLWONHINPyeTkQolHDPIP%2FM4N6sNrXWTCMvfCc5AIguDGF2%2BRJZ9ohnyKHrFjmzpZyZGsEgkUw%2BcJCn3pPt62u%2BWk6BxQVcDYZRudWZoLfsLLadDS1WK%2BV6iFqG5tjyGym%2FicbwAZhd8X9WV%2BvIsrCDD2xu3NBjqkARmvHFScdNhLC9VdZFh78LXxzHOA4HWHeZ%2B77I4A3QJoW44%2F2QouFH%2FjFfO6iunWMNl12EDP5n8L1CvgPDHSF25LFgKOTixiXWvcCuIz%2F0LAE90AuVBv9H5fuc9DBd9GCR4lkJAsQQJZZxqImPn8xAiEUwNL5BDX51pB0NWt6jX1mw0Gy08L%2BOs%2BJ8q%2FuNhrPyXJGnuZSBC2b%2BWDALiKzVofztXA&X-Amz-Signature=19fbbf38aa0ce373d67d6e0a65f158b32352370945e68992a37c88c91ca66ac9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FZW4K52%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDpHlPkp8udOp1ZADuPsPblHthZa6Opw9KBvHCq9zA4jwIhAPA1Zk9UgWwcG0uuM%2F4aQLo7Bk%2BUvrdgrIorbduGzkrWKv8DCBQQABoMNjM3NDIzMTgzODA1IgyFwEGAq5Vzk9MzuW4q3ANOKI3hNIJnhf8tznb1fLRF%2Fylod88UOp50087ccvs5a7py5gcRgRFw5fIGC%2BFnEeyr42ofOBpT4I0ycEkimTRkaQItVczbMqTSzuhP9kkSejrh63W5B5q8Jyt1UZjakQv22YVud9aceE0%2BEWzfsxmrWGjftI7Wbq%2ByZRosv8kddjWdOtP3%2FEKHh1t%2Ba25havxwlpIIX3OKetbmsk%2FzQLDS3Vp2cB18TRgVY0EOiatgfs6oMpw%2BU2s00yzYqS9r%2FHW8zEO45Q3jyn5FlUZBZfRMlX5jqfs%2FG6maSlpC7k51ZA59MR6s39kKCQIR%2FiTVrX2fmOE7VBhEhYURbE3%2BpADrhPW%2BH9nW4DsxcYNA27V5Sd%2BBro78i4ALl7tF3bZs4KBRqwf8SKYG7IFghTvCNsEiJWU6mW%2Fwnxx3Hd7UJSXyIzMswkxreLhc1ZGNgyhpWt%2Fg1e%2BYrDx6365Cc18rPo6ji%2BiPdgwT8yAKjeLcLWONHINPyeTkQolHDPIP%2FM4N6sNrXWTCMvfCc5AIguDGF2%2BRJZ9ohnyKHrFjmzpZyZGsEgkUw%2BcJCn3pPt62u%2BWk6BxQVcDYZRudWZoLfsLLadDS1WK%2BV6iFqG5tjyGym%2FicbwAZhd8X9WV%2BvIsrCDD2xu3NBjqkARmvHFScdNhLC9VdZFh78LXxzHOA4HWHeZ%2B77I4A3QJoW44%2F2QouFH%2FjFfO6iunWMNl12EDP5n8L1CvgPDHSF25LFgKOTixiXWvcCuIz%2F0LAE90AuVBv9H5fuc9DBd9GCR4lkJAsQQJZZxqImPn8xAiEUwNL5BDX51pB0NWt6jX1mw0Gy08L%2BOs%2BJ8q%2FuNhrPyXJGnuZSBC2b%2BWDALiKzVofztXA&X-Amz-Signature=d1ef4fa02fc230d87a0394bcff542098b5e93ddabadbfacab763707524fc5ce2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FZW4K52%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDpHlPkp8udOp1ZADuPsPblHthZa6Opw9KBvHCq9zA4jwIhAPA1Zk9UgWwcG0uuM%2F4aQLo7Bk%2BUvrdgrIorbduGzkrWKv8DCBQQABoMNjM3NDIzMTgzODA1IgyFwEGAq5Vzk9MzuW4q3ANOKI3hNIJnhf8tznb1fLRF%2Fylod88UOp50087ccvs5a7py5gcRgRFw5fIGC%2BFnEeyr42ofOBpT4I0ycEkimTRkaQItVczbMqTSzuhP9kkSejrh63W5B5q8Jyt1UZjakQv22YVud9aceE0%2BEWzfsxmrWGjftI7Wbq%2ByZRosv8kddjWdOtP3%2FEKHh1t%2Ba25havxwlpIIX3OKetbmsk%2FzQLDS3Vp2cB18TRgVY0EOiatgfs6oMpw%2BU2s00yzYqS9r%2FHW8zEO45Q3jyn5FlUZBZfRMlX5jqfs%2FG6maSlpC7k51ZA59MR6s39kKCQIR%2FiTVrX2fmOE7VBhEhYURbE3%2BpADrhPW%2BH9nW4DsxcYNA27V5Sd%2BBro78i4ALl7tF3bZs4KBRqwf8SKYG7IFghTvCNsEiJWU6mW%2Fwnxx3Hd7UJSXyIzMswkxreLhc1ZGNgyhpWt%2Fg1e%2BYrDx6365Cc18rPo6ji%2BiPdgwT8yAKjeLcLWONHINPyeTkQolHDPIP%2FM4N6sNrXWTCMvfCc5AIguDGF2%2BRJZ9ohnyKHrFjmzpZyZGsEgkUw%2BcJCn3pPt62u%2BWk6BxQVcDYZRudWZoLfsLLadDS1WK%2BV6iFqG5tjyGym%2FicbwAZhd8X9WV%2BvIsrCDD2xu3NBjqkARmvHFScdNhLC9VdZFh78LXxzHOA4HWHeZ%2B77I4A3QJoW44%2F2QouFH%2FjFfO6iunWMNl12EDP5n8L1CvgPDHSF25LFgKOTixiXWvcCuIz%2F0LAE90AuVBv9H5fuc9DBd9GCR4lkJAsQQJZZxqImPn8xAiEUwNL5BDX51pB0NWt6jX1mw0Gy08L%2BOs%2BJ8q%2FuNhrPyXJGnuZSBC2b%2BWDALiKzVofztXA&X-Amz-Signature=a7a4178f1203abf7841649a84a888fc10741108e1b7e7893376df36fc15ad706&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

