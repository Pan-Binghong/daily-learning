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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644HZWYWB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDm9KubK0sHL1VDJ2Mi1w%2FLF9NlLwzV2%2FXuqNg2ZNSOxgIgXwkAXriH2KpR%2B0I9pLTkfqNEPD6LolEDRyuczldFWFgqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH3V9CRZZWuOoRyCOSrcA6ULG7O0P%2FHKipKMVOKt6HDlxKM%2Bu5nYS9oS%2FE97t%2FUTltHO7uXQ8IWaOdr3hvPCz9CTfa2s8F17ArVC8hBospOkQcLm%2BCRCvx1A7T1ix5j9U3pM4RNYTeYAV6ZS3mojompWEEk%2F4wi9iVNncNXnmGIsqlDP02LnooZsQUW3vhalLXTdKbWhoxad%2FmhBSMLUfdCuvVwMrX%2F4XSi%2FGzp3J5PGqnEcku0FRJxIMx0oaO4NuHlG1fCaYyxuN4Grte7%2FElVqcbAk3G7gyBDYV00ktDIseAtih06gQYsZ2t9KxIcJS%2B1HkSbAFWrsdd0x9MfhNsaYJK7OscJIJbnezjyhZBbnh6cfr2u2VaMPD5XCzF%2By4J%2FOpIeJHc3N42wLHLIRr%2F4GSkzo5z863NKnUY9vEC39Cih4BzYInCFN7pog%2B0A1U33dylOli058c5LpoItJylN2X%2FjsrOJKYgeNP1A349r%2B%2B%2B0QssQuKCpke%2F%2FV%2FKo3WcrEl0AxeA8lkTzBV9rFwvLSqt1SAnrenM0Oy9cHsUcMJEziLZp4K2v2pE8%2FHE8f7m7R54%2BggXa6zt0V2tBZbtzBP01bsm3sKdTQEdl5XdfyB0JN78E0p9QnQmNKZSfyhvGihQPTL2pwrE%2FAMMvwr8gGOqUBrmd4wVAbvuTALYHj%2Bg99sdDLuwgB9Tqj5VidtV8Ikq19Kt8lReK0Ll4oXsv2NgYf8nNErEgWKNVtq4iHHuJrUfNNyOiFKrlp184W%2FpjgqLpY%2BhQf8%2B7CO2zjvm2bD8kpJZd20SHUyWKUw28qYImi6QW6G%2FreNsEfzbXjJrv%2BfdP97W%2FYeTPA8As%2F2tQlo1ei9UJR0Z8N7%2B2XtVa9G5%2FRbqxBFCsL&X-Amz-Signature=440613e53fcc8da6e47bf97636ee9970df3068aaaf150f9040d672568e141e91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644HZWYWB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDm9KubK0sHL1VDJ2Mi1w%2FLF9NlLwzV2%2FXuqNg2ZNSOxgIgXwkAXriH2KpR%2B0I9pLTkfqNEPD6LolEDRyuczldFWFgqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH3V9CRZZWuOoRyCOSrcA6ULG7O0P%2FHKipKMVOKt6HDlxKM%2Bu5nYS9oS%2FE97t%2FUTltHO7uXQ8IWaOdr3hvPCz9CTfa2s8F17ArVC8hBospOkQcLm%2BCRCvx1A7T1ix5j9U3pM4RNYTeYAV6ZS3mojompWEEk%2F4wi9iVNncNXnmGIsqlDP02LnooZsQUW3vhalLXTdKbWhoxad%2FmhBSMLUfdCuvVwMrX%2F4XSi%2FGzp3J5PGqnEcku0FRJxIMx0oaO4NuHlG1fCaYyxuN4Grte7%2FElVqcbAk3G7gyBDYV00ktDIseAtih06gQYsZ2t9KxIcJS%2B1HkSbAFWrsdd0x9MfhNsaYJK7OscJIJbnezjyhZBbnh6cfr2u2VaMPD5XCzF%2By4J%2FOpIeJHc3N42wLHLIRr%2F4GSkzo5z863NKnUY9vEC39Cih4BzYInCFN7pog%2B0A1U33dylOli058c5LpoItJylN2X%2FjsrOJKYgeNP1A349r%2B%2B%2B0QssQuKCpke%2F%2FV%2FKo3WcrEl0AxeA8lkTzBV9rFwvLSqt1SAnrenM0Oy9cHsUcMJEziLZp4K2v2pE8%2FHE8f7m7R54%2BggXa6zt0V2tBZbtzBP01bsm3sKdTQEdl5XdfyB0JN78E0p9QnQmNKZSfyhvGihQPTL2pwrE%2FAMMvwr8gGOqUBrmd4wVAbvuTALYHj%2Bg99sdDLuwgB9Tqj5VidtV8Ikq19Kt8lReK0Ll4oXsv2NgYf8nNErEgWKNVtq4iHHuJrUfNNyOiFKrlp184W%2FpjgqLpY%2BhQf8%2B7CO2zjvm2bD8kpJZd20SHUyWKUw28qYImi6QW6G%2FreNsEfzbXjJrv%2BfdP97W%2FYeTPA8As%2F2tQlo1ei9UJR0Z8N7%2B2XtVa9G5%2FRbqxBFCsL&X-Amz-Signature=5393fca837d1cfee312a541df0a2850ad5e0f9b1b92e82d01c85fde22e3f285d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644HZWYWB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDm9KubK0sHL1VDJ2Mi1w%2FLF9NlLwzV2%2FXuqNg2ZNSOxgIgXwkAXriH2KpR%2B0I9pLTkfqNEPD6LolEDRyuczldFWFgqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH3V9CRZZWuOoRyCOSrcA6ULG7O0P%2FHKipKMVOKt6HDlxKM%2Bu5nYS9oS%2FE97t%2FUTltHO7uXQ8IWaOdr3hvPCz9CTfa2s8F17ArVC8hBospOkQcLm%2BCRCvx1A7T1ix5j9U3pM4RNYTeYAV6ZS3mojompWEEk%2F4wi9iVNncNXnmGIsqlDP02LnooZsQUW3vhalLXTdKbWhoxad%2FmhBSMLUfdCuvVwMrX%2F4XSi%2FGzp3J5PGqnEcku0FRJxIMx0oaO4NuHlG1fCaYyxuN4Grte7%2FElVqcbAk3G7gyBDYV00ktDIseAtih06gQYsZ2t9KxIcJS%2B1HkSbAFWrsdd0x9MfhNsaYJK7OscJIJbnezjyhZBbnh6cfr2u2VaMPD5XCzF%2By4J%2FOpIeJHc3N42wLHLIRr%2F4GSkzo5z863NKnUY9vEC39Cih4BzYInCFN7pog%2B0A1U33dylOli058c5LpoItJylN2X%2FjsrOJKYgeNP1A349r%2B%2B%2B0QssQuKCpke%2F%2FV%2FKo3WcrEl0AxeA8lkTzBV9rFwvLSqt1SAnrenM0Oy9cHsUcMJEziLZp4K2v2pE8%2FHE8f7m7R54%2BggXa6zt0V2tBZbtzBP01bsm3sKdTQEdl5XdfyB0JN78E0p9QnQmNKZSfyhvGihQPTL2pwrE%2FAMMvwr8gGOqUBrmd4wVAbvuTALYHj%2Bg99sdDLuwgB9Tqj5VidtV8Ikq19Kt8lReK0Ll4oXsv2NgYf8nNErEgWKNVtq4iHHuJrUfNNyOiFKrlp184W%2FpjgqLpY%2BhQf8%2B7CO2zjvm2bD8kpJZd20SHUyWKUw28qYImi6QW6G%2FreNsEfzbXjJrv%2BfdP97W%2FYeTPA8As%2F2tQlo1ei9UJR0Z8N7%2B2XtVa9G5%2FRbqxBFCsL&X-Amz-Signature=cce899aa26e542913bac1e1dd52b4cc7e50728edab11ce84d2f26e7ad3cc8e43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644HZWYWB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDm9KubK0sHL1VDJ2Mi1w%2FLF9NlLwzV2%2FXuqNg2ZNSOxgIgXwkAXriH2KpR%2B0I9pLTkfqNEPD6LolEDRyuczldFWFgqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH3V9CRZZWuOoRyCOSrcA6ULG7O0P%2FHKipKMVOKt6HDlxKM%2Bu5nYS9oS%2FE97t%2FUTltHO7uXQ8IWaOdr3hvPCz9CTfa2s8F17ArVC8hBospOkQcLm%2BCRCvx1A7T1ix5j9U3pM4RNYTeYAV6ZS3mojompWEEk%2F4wi9iVNncNXnmGIsqlDP02LnooZsQUW3vhalLXTdKbWhoxad%2FmhBSMLUfdCuvVwMrX%2F4XSi%2FGzp3J5PGqnEcku0FRJxIMx0oaO4NuHlG1fCaYyxuN4Grte7%2FElVqcbAk3G7gyBDYV00ktDIseAtih06gQYsZ2t9KxIcJS%2B1HkSbAFWrsdd0x9MfhNsaYJK7OscJIJbnezjyhZBbnh6cfr2u2VaMPD5XCzF%2By4J%2FOpIeJHc3N42wLHLIRr%2F4GSkzo5z863NKnUY9vEC39Cih4BzYInCFN7pog%2B0A1U33dylOli058c5LpoItJylN2X%2FjsrOJKYgeNP1A349r%2B%2B%2B0QssQuKCpke%2F%2FV%2FKo3WcrEl0AxeA8lkTzBV9rFwvLSqt1SAnrenM0Oy9cHsUcMJEziLZp4K2v2pE8%2FHE8f7m7R54%2BggXa6zt0V2tBZbtzBP01bsm3sKdTQEdl5XdfyB0JN78E0p9QnQmNKZSfyhvGihQPTL2pwrE%2FAMMvwr8gGOqUBrmd4wVAbvuTALYHj%2Bg99sdDLuwgB9Tqj5VidtV8Ikq19Kt8lReK0Ll4oXsv2NgYf8nNErEgWKNVtq4iHHuJrUfNNyOiFKrlp184W%2FpjgqLpY%2BhQf8%2B7CO2zjvm2bD8kpJZd20SHUyWKUw28qYImi6QW6G%2FreNsEfzbXjJrv%2BfdP97W%2FYeTPA8As%2F2tQlo1ei9UJR0Z8N7%2B2XtVa9G5%2FRbqxBFCsL&X-Amz-Signature=c95832e08f6a750aaad4488e2ef82fae71ca6b7fff4e54d322d813bc1109b888&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644HZWYWB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDm9KubK0sHL1VDJ2Mi1w%2FLF9NlLwzV2%2FXuqNg2ZNSOxgIgXwkAXriH2KpR%2B0I9pLTkfqNEPD6LolEDRyuczldFWFgqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH3V9CRZZWuOoRyCOSrcA6ULG7O0P%2FHKipKMVOKt6HDlxKM%2Bu5nYS9oS%2FE97t%2FUTltHO7uXQ8IWaOdr3hvPCz9CTfa2s8F17ArVC8hBospOkQcLm%2BCRCvx1A7T1ix5j9U3pM4RNYTeYAV6ZS3mojompWEEk%2F4wi9iVNncNXnmGIsqlDP02LnooZsQUW3vhalLXTdKbWhoxad%2FmhBSMLUfdCuvVwMrX%2F4XSi%2FGzp3J5PGqnEcku0FRJxIMx0oaO4NuHlG1fCaYyxuN4Grte7%2FElVqcbAk3G7gyBDYV00ktDIseAtih06gQYsZ2t9KxIcJS%2B1HkSbAFWrsdd0x9MfhNsaYJK7OscJIJbnezjyhZBbnh6cfr2u2VaMPD5XCzF%2By4J%2FOpIeJHc3N42wLHLIRr%2F4GSkzo5z863NKnUY9vEC39Cih4BzYInCFN7pog%2B0A1U33dylOli058c5LpoItJylN2X%2FjsrOJKYgeNP1A349r%2B%2B%2B0QssQuKCpke%2F%2FV%2FKo3WcrEl0AxeA8lkTzBV9rFwvLSqt1SAnrenM0Oy9cHsUcMJEziLZp4K2v2pE8%2FHE8f7m7R54%2BggXa6zt0V2tBZbtzBP01bsm3sKdTQEdl5XdfyB0JN78E0p9QnQmNKZSfyhvGihQPTL2pwrE%2FAMMvwr8gGOqUBrmd4wVAbvuTALYHj%2Bg99sdDLuwgB9Tqj5VidtV8Ikq19Kt8lReK0Ll4oXsv2NgYf8nNErEgWKNVtq4iHHuJrUfNNyOiFKrlp184W%2FpjgqLpY%2BhQf8%2B7CO2zjvm2bD8kpJZd20SHUyWKUw28qYImi6QW6G%2FreNsEfzbXjJrv%2BfdP97W%2FYeTPA8As%2F2tQlo1ei9UJR0Z8N7%2B2XtVa9G5%2FRbqxBFCsL&X-Amz-Signature=431fcb92ac600fc939c906d5c7d77de32de7fcb21fbea8f448da20636fb3f574&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644HZWYWB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDm9KubK0sHL1VDJ2Mi1w%2FLF9NlLwzV2%2FXuqNg2ZNSOxgIgXwkAXriH2KpR%2B0I9pLTkfqNEPD6LolEDRyuczldFWFgqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH3V9CRZZWuOoRyCOSrcA6ULG7O0P%2FHKipKMVOKt6HDlxKM%2Bu5nYS9oS%2FE97t%2FUTltHO7uXQ8IWaOdr3hvPCz9CTfa2s8F17ArVC8hBospOkQcLm%2BCRCvx1A7T1ix5j9U3pM4RNYTeYAV6ZS3mojompWEEk%2F4wi9iVNncNXnmGIsqlDP02LnooZsQUW3vhalLXTdKbWhoxad%2FmhBSMLUfdCuvVwMrX%2F4XSi%2FGzp3J5PGqnEcku0FRJxIMx0oaO4NuHlG1fCaYyxuN4Grte7%2FElVqcbAk3G7gyBDYV00ktDIseAtih06gQYsZ2t9KxIcJS%2B1HkSbAFWrsdd0x9MfhNsaYJK7OscJIJbnezjyhZBbnh6cfr2u2VaMPD5XCzF%2By4J%2FOpIeJHc3N42wLHLIRr%2F4GSkzo5z863NKnUY9vEC39Cih4BzYInCFN7pog%2B0A1U33dylOli058c5LpoItJylN2X%2FjsrOJKYgeNP1A349r%2B%2B%2B0QssQuKCpke%2F%2FV%2FKo3WcrEl0AxeA8lkTzBV9rFwvLSqt1SAnrenM0Oy9cHsUcMJEziLZp4K2v2pE8%2FHE8f7m7R54%2BggXa6zt0V2tBZbtzBP01bsm3sKdTQEdl5XdfyB0JN78E0p9QnQmNKZSfyhvGihQPTL2pwrE%2FAMMvwr8gGOqUBrmd4wVAbvuTALYHj%2Bg99sdDLuwgB9Tqj5VidtV8Ikq19Kt8lReK0Ll4oXsv2NgYf8nNErEgWKNVtq4iHHuJrUfNNyOiFKrlp184W%2FpjgqLpY%2BhQf8%2B7CO2zjvm2bD8kpJZd20SHUyWKUw28qYImi6QW6G%2FreNsEfzbXjJrv%2BfdP97W%2FYeTPA8As%2F2tQlo1ei9UJR0Z8N7%2B2XtVa9G5%2FRbqxBFCsL&X-Amz-Signature=509eebd1c84b54ddc1ae429dbd025723df7ca7602a3949bdd810e1a33e0bfc7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644HZWYWB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDm9KubK0sHL1VDJ2Mi1w%2FLF9NlLwzV2%2FXuqNg2ZNSOxgIgXwkAXriH2KpR%2B0I9pLTkfqNEPD6LolEDRyuczldFWFgqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH3V9CRZZWuOoRyCOSrcA6ULG7O0P%2FHKipKMVOKt6HDlxKM%2Bu5nYS9oS%2FE97t%2FUTltHO7uXQ8IWaOdr3hvPCz9CTfa2s8F17ArVC8hBospOkQcLm%2BCRCvx1A7T1ix5j9U3pM4RNYTeYAV6ZS3mojompWEEk%2F4wi9iVNncNXnmGIsqlDP02LnooZsQUW3vhalLXTdKbWhoxad%2FmhBSMLUfdCuvVwMrX%2F4XSi%2FGzp3J5PGqnEcku0FRJxIMx0oaO4NuHlG1fCaYyxuN4Grte7%2FElVqcbAk3G7gyBDYV00ktDIseAtih06gQYsZ2t9KxIcJS%2B1HkSbAFWrsdd0x9MfhNsaYJK7OscJIJbnezjyhZBbnh6cfr2u2VaMPD5XCzF%2By4J%2FOpIeJHc3N42wLHLIRr%2F4GSkzo5z863NKnUY9vEC39Cih4BzYInCFN7pog%2B0A1U33dylOli058c5LpoItJylN2X%2FjsrOJKYgeNP1A349r%2B%2B%2B0QssQuKCpke%2F%2FV%2FKo3WcrEl0AxeA8lkTzBV9rFwvLSqt1SAnrenM0Oy9cHsUcMJEziLZp4K2v2pE8%2FHE8f7m7R54%2BggXa6zt0V2tBZbtzBP01bsm3sKdTQEdl5XdfyB0JN78E0p9QnQmNKZSfyhvGihQPTL2pwrE%2FAMMvwr8gGOqUBrmd4wVAbvuTALYHj%2Bg99sdDLuwgB9Tqj5VidtV8Ikq19Kt8lReK0Ll4oXsv2NgYf8nNErEgWKNVtq4iHHuJrUfNNyOiFKrlp184W%2FpjgqLpY%2BhQf8%2B7CO2zjvm2bD8kpJZd20SHUyWKUw28qYImi6QW6G%2FreNsEfzbXjJrv%2BfdP97W%2FYeTPA8As%2F2tQlo1ei9UJR0Z8N7%2B2XtVa9G5%2FRbqxBFCsL&X-Amz-Signature=d379c5cc2756dfa5c2be5f99db2b5ebd5916cfdd5db46abd51ab168b16134530&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

