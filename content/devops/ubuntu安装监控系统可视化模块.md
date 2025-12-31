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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTF7R5KF%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq8q%2FYA6pDhCe%2Fn6R7ZVUI1fS8BXfWPYBNTM9YkTRR7AiBxJzkbSgTpjndIUmDh3eeUXPb6TZksxa%2Brl8t89LXJiiqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJT1SUfQqZDSD%2Bz7pKtwD%2FRh36ZL9VW7PSdevklt%2BgGdiGjH14ogC8hDIgbkoDXZp%2B2Z9kwfMQFQpPAErvHZfWviJKL%2Fjs2HhTmznYBqZPT23NJhtKq23C9N0JzP3CZ1lFGgm31R4lo8wD5w0wRHijLtTJ3iw2z%2BbEreIQGNzenfJY2%2Fcs6EE00%2BwFKO0T5QaGUhwCYoaDZlJBowjqsQdHdWJ83Xlc4xhJ9pQB2HaGq2SYdshgMnyotrv0t7YHS56LDYIdJ6A7zUoR%2Fyq2wfh2bCUGD6Iw%2BPRnPQpZu4Bo2C3WMjsWSSzZjRZeDRz%2BPkgTVS20g2UaW%2B6C3U7cjpZSlGS0B21LPzsQHAHoE4mikJV4OWTd2Acl86I1W4FYXhHUuUD7%2Fdju9R%2FMaWm7sfBAcDnmd7MFART5VrrPRj76ndo6KYNYYKN%2BjNh8auz2HAOR%2BTNXepKG4jPA0MmSIv0RRRWR1xgWIyF3dFFVAL%2Fs3PJyf0qTLI6tlo7kB6ewchfps6mBj%2FikKdXRiW4vBIlrMB%2Foe9nz0vfPsyOWH0TGlROaE2L6864AL9Gh8cyWtCCsMKLAn5QCq1hiDPg6585GoluhagUD9mIF7SCN9UWBXSBLkDDimuVtzqhhjtr4Zb74S0wW8BvJuz9tNAwqfXRygY6pgFBfLHy37l2mF48UYs1CHIMlzk%2F0cJHegPJH5TCAedMtKhJDo6zgKxD8L770yPm9C8Jm0eFBwWWqq0%2FzGR3vKaDLNimTHj0CZeKUP7vqNtlVV81ZQG5J2jhrQLxC3wfis18z2JDXySnWDL2h3x6Lnhaex1L6LMd6ipuHP6zE5KZrYxP6NOqyQGC5LmIh9UWwJ0U1zMExoL32YdYskkfV4KKAiN5Xen9&X-Amz-Signature=378936914f410d2ee9ce0a0c2177542f35be2f6b1df39cf985dd2ac4428170ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTF7R5KF%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq8q%2FYA6pDhCe%2Fn6R7ZVUI1fS8BXfWPYBNTM9YkTRR7AiBxJzkbSgTpjndIUmDh3eeUXPb6TZksxa%2Brl8t89LXJiiqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJT1SUfQqZDSD%2Bz7pKtwD%2FRh36ZL9VW7PSdevklt%2BgGdiGjH14ogC8hDIgbkoDXZp%2B2Z9kwfMQFQpPAErvHZfWviJKL%2Fjs2HhTmznYBqZPT23NJhtKq23C9N0JzP3CZ1lFGgm31R4lo8wD5w0wRHijLtTJ3iw2z%2BbEreIQGNzenfJY2%2Fcs6EE00%2BwFKO0T5QaGUhwCYoaDZlJBowjqsQdHdWJ83Xlc4xhJ9pQB2HaGq2SYdshgMnyotrv0t7YHS56LDYIdJ6A7zUoR%2Fyq2wfh2bCUGD6Iw%2BPRnPQpZu4Bo2C3WMjsWSSzZjRZeDRz%2BPkgTVS20g2UaW%2B6C3U7cjpZSlGS0B21LPzsQHAHoE4mikJV4OWTd2Acl86I1W4FYXhHUuUD7%2Fdju9R%2FMaWm7sfBAcDnmd7MFART5VrrPRj76ndo6KYNYYKN%2BjNh8auz2HAOR%2BTNXepKG4jPA0MmSIv0RRRWR1xgWIyF3dFFVAL%2Fs3PJyf0qTLI6tlo7kB6ewchfps6mBj%2FikKdXRiW4vBIlrMB%2Foe9nz0vfPsyOWH0TGlROaE2L6864AL9Gh8cyWtCCsMKLAn5QCq1hiDPg6585GoluhagUD9mIF7SCN9UWBXSBLkDDimuVtzqhhjtr4Zb74S0wW8BvJuz9tNAwqfXRygY6pgFBfLHy37l2mF48UYs1CHIMlzk%2F0cJHegPJH5TCAedMtKhJDo6zgKxD8L770yPm9C8Jm0eFBwWWqq0%2FzGR3vKaDLNimTHj0CZeKUP7vqNtlVV81ZQG5J2jhrQLxC3wfis18z2JDXySnWDL2h3x6Lnhaex1L6LMd6ipuHP6zE5KZrYxP6NOqyQGC5LmIh9UWwJ0U1zMExoL32YdYskkfV4KKAiN5Xen9&X-Amz-Signature=88c33731b13937d165821100eecd0e31030dfd924b7c09c30458b299120861e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTF7R5KF%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq8q%2FYA6pDhCe%2Fn6R7ZVUI1fS8BXfWPYBNTM9YkTRR7AiBxJzkbSgTpjndIUmDh3eeUXPb6TZksxa%2Brl8t89LXJiiqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJT1SUfQqZDSD%2Bz7pKtwD%2FRh36ZL9VW7PSdevklt%2BgGdiGjH14ogC8hDIgbkoDXZp%2B2Z9kwfMQFQpPAErvHZfWviJKL%2Fjs2HhTmznYBqZPT23NJhtKq23C9N0JzP3CZ1lFGgm31R4lo8wD5w0wRHijLtTJ3iw2z%2BbEreIQGNzenfJY2%2Fcs6EE00%2BwFKO0T5QaGUhwCYoaDZlJBowjqsQdHdWJ83Xlc4xhJ9pQB2HaGq2SYdshgMnyotrv0t7YHS56LDYIdJ6A7zUoR%2Fyq2wfh2bCUGD6Iw%2BPRnPQpZu4Bo2C3WMjsWSSzZjRZeDRz%2BPkgTVS20g2UaW%2B6C3U7cjpZSlGS0B21LPzsQHAHoE4mikJV4OWTd2Acl86I1W4FYXhHUuUD7%2Fdju9R%2FMaWm7sfBAcDnmd7MFART5VrrPRj76ndo6KYNYYKN%2BjNh8auz2HAOR%2BTNXepKG4jPA0MmSIv0RRRWR1xgWIyF3dFFVAL%2Fs3PJyf0qTLI6tlo7kB6ewchfps6mBj%2FikKdXRiW4vBIlrMB%2Foe9nz0vfPsyOWH0TGlROaE2L6864AL9Gh8cyWtCCsMKLAn5QCq1hiDPg6585GoluhagUD9mIF7SCN9UWBXSBLkDDimuVtzqhhjtr4Zb74S0wW8BvJuz9tNAwqfXRygY6pgFBfLHy37l2mF48UYs1CHIMlzk%2F0cJHegPJH5TCAedMtKhJDo6zgKxD8L770yPm9C8Jm0eFBwWWqq0%2FzGR3vKaDLNimTHj0CZeKUP7vqNtlVV81ZQG5J2jhrQLxC3wfis18z2JDXySnWDL2h3x6Lnhaex1L6LMd6ipuHP6zE5KZrYxP6NOqyQGC5LmIh9UWwJ0U1zMExoL32YdYskkfV4KKAiN5Xen9&X-Amz-Signature=6b8fe08a9fe9cc1ed70bfbd1bcd65cee99ab66589e47488f3961a15119743281&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTF7R5KF%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq8q%2FYA6pDhCe%2Fn6R7ZVUI1fS8BXfWPYBNTM9YkTRR7AiBxJzkbSgTpjndIUmDh3eeUXPb6TZksxa%2Brl8t89LXJiiqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJT1SUfQqZDSD%2Bz7pKtwD%2FRh36ZL9VW7PSdevklt%2BgGdiGjH14ogC8hDIgbkoDXZp%2B2Z9kwfMQFQpPAErvHZfWviJKL%2Fjs2HhTmznYBqZPT23NJhtKq23C9N0JzP3CZ1lFGgm31R4lo8wD5w0wRHijLtTJ3iw2z%2BbEreIQGNzenfJY2%2Fcs6EE00%2BwFKO0T5QaGUhwCYoaDZlJBowjqsQdHdWJ83Xlc4xhJ9pQB2HaGq2SYdshgMnyotrv0t7YHS56LDYIdJ6A7zUoR%2Fyq2wfh2bCUGD6Iw%2BPRnPQpZu4Bo2C3WMjsWSSzZjRZeDRz%2BPkgTVS20g2UaW%2B6C3U7cjpZSlGS0B21LPzsQHAHoE4mikJV4OWTd2Acl86I1W4FYXhHUuUD7%2Fdju9R%2FMaWm7sfBAcDnmd7MFART5VrrPRj76ndo6KYNYYKN%2BjNh8auz2HAOR%2BTNXepKG4jPA0MmSIv0RRRWR1xgWIyF3dFFVAL%2Fs3PJyf0qTLI6tlo7kB6ewchfps6mBj%2FikKdXRiW4vBIlrMB%2Foe9nz0vfPsyOWH0TGlROaE2L6864AL9Gh8cyWtCCsMKLAn5QCq1hiDPg6585GoluhagUD9mIF7SCN9UWBXSBLkDDimuVtzqhhjtr4Zb74S0wW8BvJuz9tNAwqfXRygY6pgFBfLHy37l2mF48UYs1CHIMlzk%2F0cJHegPJH5TCAedMtKhJDo6zgKxD8L770yPm9C8Jm0eFBwWWqq0%2FzGR3vKaDLNimTHj0CZeKUP7vqNtlVV81ZQG5J2jhrQLxC3wfis18z2JDXySnWDL2h3x6Lnhaex1L6LMd6ipuHP6zE5KZrYxP6NOqyQGC5LmIh9UWwJ0U1zMExoL32YdYskkfV4KKAiN5Xen9&X-Amz-Signature=1cdd2e457b9938546e8219dacac11d35a1807dbb4bda0cb9abe4223970756b5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTF7R5KF%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq8q%2FYA6pDhCe%2Fn6R7ZVUI1fS8BXfWPYBNTM9YkTRR7AiBxJzkbSgTpjndIUmDh3eeUXPb6TZksxa%2Brl8t89LXJiiqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJT1SUfQqZDSD%2Bz7pKtwD%2FRh36ZL9VW7PSdevklt%2BgGdiGjH14ogC8hDIgbkoDXZp%2B2Z9kwfMQFQpPAErvHZfWviJKL%2Fjs2HhTmznYBqZPT23NJhtKq23C9N0JzP3CZ1lFGgm31R4lo8wD5w0wRHijLtTJ3iw2z%2BbEreIQGNzenfJY2%2Fcs6EE00%2BwFKO0T5QaGUhwCYoaDZlJBowjqsQdHdWJ83Xlc4xhJ9pQB2HaGq2SYdshgMnyotrv0t7YHS56LDYIdJ6A7zUoR%2Fyq2wfh2bCUGD6Iw%2BPRnPQpZu4Bo2C3WMjsWSSzZjRZeDRz%2BPkgTVS20g2UaW%2B6C3U7cjpZSlGS0B21LPzsQHAHoE4mikJV4OWTd2Acl86I1W4FYXhHUuUD7%2Fdju9R%2FMaWm7sfBAcDnmd7MFART5VrrPRj76ndo6KYNYYKN%2BjNh8auz2HAOR%2BTNXepKG4jPA0MmSIv0RRRWR1xgWIyF3dFFVAL%2Fs3PJyf0qTLI6tlo7kB6ewchfps6mBj%2FikKdXRiW4vBIlrMB%2Foe9nz0vfPsyOWH0TGlROaE2L6864AL9Gh8cyWtCCsMKLAn5QCq1hiDPg6585GoluhagUD9mIF7SCN9UWBXSBLkDDimuVtzqhhjtr4Zb74S0wW8BvJuz9tNAwqfXRygY6pgFBfLHy37l2mF48UYs1CHIMlzk%2F0cJHegPJH5TCAedMtKhJDo6zgKxD8L770yPm9C8Jm0eFBwWWqq0%2FzGR3vKaDLNimTHj0CZeKUP7vqNtlVV81ZQG5J2jhrQLxC3wfis18z2JDXySnWDL2h3x6Lnhaex1L6LMd6ipuHP6zE5KZrYxP6NOqyQGC5LmIh9UWwJ0U1zMExoL32YdYskkfV4KKAiN5Xen9&X-Amz-Signature=1a8a967b4f2631cd4cbe07ca2863da6d7c733e029fa696ead01ac8257b569566&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTF7R5KF%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq8q%2FYA6pDhCe%2Fn6R7ZVUI1fS8BXfWPYBNTM9YkTRR7AiBxJzkbSgTpjndIUmDh3eeUXPb6TZksxa%2Brl8t89LXJiiqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJT1SUfQqZDSD%2Bz7pKtwD%2FRh36ZL9VW7PSdevklt%2BgGdiGjH14ogC8hDIgbkoDXZp%2B2Z9kwfMQFQpPAErvHZfWviJKL%2Fjs2HhTmznYBqZPT23NJhtKq23C9N0JzP3CZ1lFGgm31R4lo8wD5w0wRHijLtTJ3iw2z%2BbEreIQGNzenfJY2%2Fcs6EE00%2BwFKO0T5QaGUhwCYoaDZlJBowjqsQdHdWJ83Xlc4xhJ9pQB2HaGq2SYdshgMnyotrv0t7YHS56LDYIdJ6A7zUoR%2Fyq2wfh2bCUGD6Iw%2BPRnPQpZu4Bo2C3WMjsWSSzZjRZeDRz%2BPkgTVS20g2UaW%2B6C3U7cjpZSlGS0B21LPzsQHAHoE4mikJV4OWTd2Acl86I1W4FYXhHUuUD7%2Fdju9R%2FMaWm7sfBAcDnmd7MFART5VrrPRj76ndo6KYNYYKN%2BjNh8auz2HAOR%2BTNXepKG4jPA0MmSIv0RRRWR1xgWIyF3dFFVAL%2Fs3PJyf0qTLI6tlo7kB6ewchfps6mBj%2FikKdXRiW4vBIlrMB%2Foe9nz0vfPsyOWH0TGlROaE2L6864AL9Gh8cyWtCCsMKLAn5QCq1hiDPg6585GoluhagUD9mIF7SCN9UWBXSBLkDDimuVtzqhhjtr4Zb74S0wW8BvJuz9tNAwqfXRygY6pgFBfLHy37l2mF48UYs1CHIMlzk%2F0cJHegPJH5TCAedMtKhJDo6zgKxD8L770yPm9C8Jm0eFBwWWqq0%2FzGR3vKaDLNimTHj0CZeKUP7vqNtlVV81ZQG5J2jhrQLxC3wfis18z2JDXySnWDL2h3x6Lnhaex1L6LMd6ipuHP6zE5KZrYxP6NOqyQGC5LmIh9UWwJ0U1zMExoL32YdYskkfV4KKAiN5Xen9&X-Amz-Signature=cb816232e8cf715ab46760e4493000c818dfe087f7af78188be97fe4f9b2cd07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTF7R5KF%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq8q%2FYA6pDhCe%2Fn6R7ZVUI1fS8BXfWPYBNTM9YkTRR7AiBxJzkbSgTpjndIUmDh3eeUXPb6TZksxa%2Brl8t89LXJiiqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJT1SUfQqZDSD%2Bz7pKtwD%2FRh36ZL9VW7PSdevklt%2BgGdiGjH14ogC8hDIgbkoDXZp%2B2Z9kwfMQFQpPAErvHZfWviJKL%2Fjs2HhTmznYBqZPT23NJhtKq23C9N0JzP3CZ1lFGgm31R4lo8wD5w0wRHijLtTJ3iw2z%2BbEreIQGNzenfJY2%2Fcs6EE00%2BwFKO0T5QaGUhwCYoaDZlJBowjqsQdHdWJ83Xlc4xhJ9pQB2HaGq2SYdshgMnyotrv0t7YHS56LDYIdJ6A7zUoR%2Fyq2wfh2bCUGD6Iw%2BPRnPQpZu4Bo2C3WMjsWSSzZjRZeDRz%2BPkgTVS20g2UaW%2B6C3U7cjpZSlGS0B21LPzsQHAHoE4mikJV4OWTd2Acl86I1W4FYXhHUuUD7%2Fdju9R%2FMaWm7sfBAcDnmd7MFART5VrrPRj76ndo6KYNYYKN%2BjNh8auz2HAOR%2BTNXepKG4jPA0MmSIv0RRRWR1xgWIyF3dFFVAL%2Fs3PJyf0qTLI6tlo7kB6ewchfps6mBj%2FikKdXRiW4vBIlrMB%2Foe9nz0vfPsyOWH0TGlROaE2L6864AL9Gh8cyWtCCsMKLAn5QCq1hiDPg6585GoluhagUD9mIF7SCN9UWBXSBLkDDimuVtzqhhjtr4Zb74S0wW8BvJuz9tNAwqfXRygY6pgFBfLHy37l2mF48UYs1CHIMlzk%2F0cJHegPJH5TCAedMtKhJDo6zgKxD8L770yPm9C8Jm0eFBwWWqq0%2FzGR3vKaDLNimTHj0CZeKUP7vqNtlVV81ZQG5J2jhrQLxC3wfis18z2JDXySnWDL2h3x6Lnhaex1L6LMd6ipuHP6zE5KZrYxP6NOqyQGC5LmIh9UWwJ0U1zMExoL32YdYskkfV4KKAiN5Xen9&X-Amz-Signature=16f58110d54a1a45800e88606deababf4da7357f248d856b8cd3fcad3e6bad7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

