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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RE6NUPIZ%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQD1y8U5AJUGB84x1Hfxcr6zYyKmFvdNX%2BAEDHKcSu9SHQIgV%2FExg68yMl5C%2Bj7dKTM42xXwC21ffBkzxFnBU0%2Fpf%2FYqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTOc24oskIZbl5XvCrcAyoiPTgwpOHwZXoEtNuCdPmk63L1zJpKhTTTUMxJA68s12HGf5Ut3fjVMskRLO0ZVKfL61CxWTZVjhne4TW6jRPRDs%2Fcn0e1XQ3rnoVik2m3gR%2BO7WubX2WaO%2BzOqhWXffdn33ZYKcuEPqc%2Fli7aIGmKgG5NyjerFQQ6H0rZEnEJLNe8QWfD0IsfE1DLCS6dm0s4Fg1IBYW2DV4FSFk7liSZtuz7ycbmha%2FDk1nPBXutWkCP4b0li0brSBKEHUEyqf6v%2FxLitZ512fKobYJ0dw8gj1jLmB9Dgmpcjmk9PJxNfNkUYHlX8IBdc2mnNBjSzIYKzFfXtrxh52d86L9yEgksl6VF%2FujLEGa3LgBaATJ8DciMU%2Bfv8TpJ%2Bd4cAcPiXtTMxXnsMa1lFZs85Y5ML915rIer0Ik2DS9Y11w8jNeW4QXItttrSpbTG0XC3seUtjvMNN%2FZksB70KxEjU%2FaBQXHPvqDdn1gpJ8sMtG%2F%2FQe483odrKImkrf20L8b51SJ5fm6fgHc9rLZWphdH1%2F1vbUtk1bAks3eGiSPtrBOOuKcANUELxQohWWXuqEXN%2Br9PM4HOUobYhGZEWWrmFl6yzVlHUL1pSawRCS9GTTMlCyvvTx07brG%2BhMIXaArMIXZhcwGOqUBLQhR83VF8vK4cj85%2B7h7%2Bg9FRwjdQ6toLGExbilSAW8uwVWbp7x8l6kunr2%2BRVPToSvXv6ag%2Bg3Wfb3TjNWnU%2Bv%2BbTLugQAu3sbiwrmeAl9ZDcUBG7T3ItuHM5ibcg497M8eBGQgQLMU8fA6hy%2F%2FXY7Sag1wsXTRDRgJtDHXHpV%2Fl741HYEure12kNKk6kdPE6RpxGbzFWJ73OKE3Fl%2Fy7FMC5cv&X-Amz-Signature=ef6c2d0c5cb76f6b23c7c737402f58f68b9b2449ebd16ec04b8837f56f6ac23a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RE6NUPIZ%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQD1y8U5AJUGB84x1Hfxcr6zYyKmFvdNX%2BAEDHKcSu9SHQIgV%2FExg68yMl5C%2Bj7dKTM42xXwC21ffBkzxFnBU0%2Fpf%2FYqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTOc24oskIZbl5XvCrcAyoiPTgwpOHwZXoEtNuCdPmk63L1zJpKhTTTUMxJA68s12HGf5Ut3fjVMskRLO0ZVKfL61CxWTZVjhne4TW6jRPRDs%2Fcn0e1XQ3rnoVik2m3gR%2BO7WubX2WaO%2BzOqhWXffdn33ZYKcuEPqc%2Fli7aIGmKgG5NyjerFQQ6H0rZEnEJLNe8QWfD0IsfE1DLCS6dm0s4Fg1IBYW2DV4FSFk7liSZtuz7ycbmha%2FDk1nPBXutWkCP4b0li0brSBKEHUEyqf6v%2FxLitZ512fKobYJ0dw8gj1jLmB9Dgmpcjmk9PJxNfNkUYHlX8IBdc2mnNBjSzIYKzFfXtrxh52d86L9yEgksl6VF%2FujLEGa3LgBaATJ8DciMU%2Bfv8TpJ%2Bd4cAcPiXtTMxXnsMa1lFZs85Y5ML915rIer0Ik2DS9Y11w8jNeW4QXItttrSpbTG0XC3seUtjvMNN%2FZksB70KxEjU%2FaBQXHPvqDdn1gpJ8sMtG%2F%2FQe483odrKImkrf20L8b51SJ5fm6fgHc9rLZWphdH1%2F1vbUtk1bAks3eGiSPtrBOOuKcANUELxQohWWXuqEXN%2Br9PM4HOUobYhGZEWWrmFl6yzVlHUL1pSawRCS9GTTMlCyvvTx07brG%2BhMIXaArMIXZhcwGOqUBLQhR83VF8vK4cj85%2B7h7%2Bg9FRwjdQ6toLGExbilSAW8uwVWbp7x8l6kunr2%2BRVPToSvXv6ag%2Bg3Wfb3TjNWnU%2Bv%2BbTLugQAu3sbiwrmeAl9ZDcUBG7T3ItuHM5ibcg497M8eBGQgQLMU8fA6hy%2F%2FXY7Sag1wsXTRDRgJtDHXHpV%2Fl741HYEure12kNKk6kdPE6RpxGbzFWJ73OKE3Fl%2Fy7FMC5cv&X-Amz-Signature=ddf2a13b48483cf82b4f8b6ad1a0ec37405be224c906334be7bd8bdc34138e19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RE6NUPIZ%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQD1y8U5AJUGB84x1Hfxcr6zYyKmFvdNX%2BAEDHKcSu9SHQIgV%2FExg68yMl5C%2Bj7dKTM42xXwC21ffBkzxFnBU0%2Fpf%2FYqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTOc24oskIZbl5XvCrcAyoiPTgwpOHwZXoEtNuCdPmk63L1zJpKhTTTUMxJA68s12HGf5Ut3fjVMskRLO0ZVKfL61CxWTZVjhne4TW6jRPRDs%2Fcn0e1XQ3rnoVik2m3gR%2BO7WubX2WaO%2BzOqhWXffdn33ZYKcuEPqc%2Fli7aIGmKgG5NyjerFQQ6H0rZEnEJLNe8QWfD0IsfE1DLCS6dm0s4Fg1IBYW2DV4FSFk7liSZtuz7ycbmha%2FDk1nPBXutWkCP4b0li0brSBKEHUEyqf6v%2FxLitZ512fKobYJ0dw8gj1jLmB9Dgmpcjmk9PJxNfNkUYHlX8IBdc2mnNBjSzIYKzFfXtrxh52d86L9yEgksl6VF%2FujLEGa3LgBaATJ8DciMU%2Bfv8TpJ%2Bd4cAcPiXtTMxXnsMa1lFZs85Y5ML915rIer0Ik2DS9Y11w8jNeW4QXItttrSpbTG0XC3seUtjvMNN%2FZksB70KxEjU%2FaBQXHPvqDdn1gpJ8sMtG%2F%2FQe483odrKImkrf20L8b51SJ5fm6fgHc9rLZWphdH1%2F1vbUtk1bAks3eGiSPtrBOOuKcANUELxQohWWXuqEXN%2Br9PM4HOUobYhGZEWWrmFl6yzVlHUL1pSawRCS9GTTMlCyvvTx07brG%2BhMIXaArMIXZhcwGOqUBLQhR83VF8vK4cj85%2B7h7%2Bg9FRwjdQ6toLGExbilSAW8uwVWbp7x8l6kunr2%2BRVPToSvXv6ag%2Bg3Wfb3TjNWnU%2Bv%2BbTLugQAu3sbiwrmeAl9ZDcUBG7T3ItuHM5ibcg497M8eBGQgQLMU8fA6hy%2F%2FXY7Sag1wsXTRDRgJtDHXHpV%2Fl741HYEure12kNKk6kdPE6RpxGbzFWJ73OKE3Fl%2Fy7FMC5cv&X-Amz-Signature=83e58cebe58ed9989d78448555d7995f2ebc293063d6b3270899a366f771e77e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RE6NUPIZ%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQD1y8U5AJUGB84x1Hfxcr6zYyKmFvdNX%2BAEDHKcSu9SHQIgV%2FExg68yMl5C%2Bj7dKTM42xXwC21ffBkzxFnBU0%2Fpf%2FYqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTOc24oskIZbl5XvCrcAyoiPTgwpOHwZXoEtNuCdPmk63L1zJpKhTTTUMxJA68s12HGf5Ut3fjVMskRLO0ZVKfL61CxWTZVjhne4TW6jRPRDs%2Fcn0e1XQ3rnoVik2m3gR%2BO7WubX2WaO%2BzOqhWXffdn33ZYKcuEPqc%2Fli7aIGmKgG5NyjerFQQ6H0rZEnEJLNe8QWfD0IsfE1DLCS6dm0s4Fg1IBYW2DV4FSFk7liSZtuz7ycbmha%2FDk1nPBXutWkCP4b0li0brSBKEHUEyqf6v%2FxLitZ512fKobYJ0dw8gj1jLmB9Dgmpcjmk9PJxNfNkUYHlX8IBdc2mnNBjSzIYKzFfXtrxh52d86L9yEgksl6VF%2FujLEGa3LgBaATJ8DciMU%2Bfv8TpJ%2Bd4cAcPiXtTMxXnsMa1lFZs85Y5ML915rIer0Ik2DS9Y11w8jNeW4QXItttrSpbTG0XC3seUtjvMNN%2FZksB70KxEjU%2FaBQXHPvqDdn1gpJ8sMtG%2F%2FQe483odrKImkrf20L8b51SJ5fm6fgHc9rLZWphdH1%2F1vbUtk1bAks3eGiSPtrBOOuKcANUELxQohWWXuqEXN%2Br9PM4HOUobYhGZEWWrmFl6yzVlHUL1pSawRCS9GTTMlCyvvTx07brG%2BhMIXaArMIXZhcwGOqUBLQhR83VF8vK4cj85%2B7h7%2Bg9FRwjdQ6toLGExbilSAW8uwVWbp7x8l6kunr2%2BRVPToSvXv6ag%2Bg3Wfb3TjNWnU%2Bv%2BbTLugQAu3sbiwrmeAl9ZDcUBG7T3ItuHM5ibcg497M8eBGQgQLMU8fA6hy%2F%2FXY7Sag1wsXTRDRgJtDHXHpV%2Fl741HYEure12kNKk6kdPE6RpxGbzFWJ73OKE3Fl%2Fy7FMC5cv&X-Amz-Signature=aa100fdae9cdec07144688b328a83a0746306261568b919801dd162a444b01b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RE6NUPIZ%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQD1y8U5AJUGB84x1Hfxcr6zYyKmFvdNX%2BAEDHKcSu9SHQIgV%2FExg68yMl5C%2Bj7dKTM42xXwC21ffBkzxFnBU0%2Fpf%2FYqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTOc24oskIZbl5XvCrcAyoiPTgwpOHwZXoEtNuCdPmk63L1zJpKhTTTUMxJA68s12HGf5Ut3fjVMskRLO0ZVKfL61CxWTZVjhne4TW6jRPRDs%2Fcn0e1XQ3rnoVik2m3gR%2BO7WubX2WaO%2BzOqhWXffdn33ZYKcuEPqc%2Fli7aIGmKgG5NyjerFQQ6H0rZEnEJLNe8QWfD0IsfE1DLCS6dm0s4Fg1IBYW2DV4FSFk7liSZtuz7ycbmha%2FDk1nPBXutWkCP4b0li0brSBKEHUEyqf6v%2FxLitZ512fKobYJ0dw8gj1jLmB9Dgmpcjmk9PJxNfNkUYHlX8IBdc2mnNBjSzIYKzFfXtrxh52d86L9yEgksl6VF%2FujLEGa3LgBaATJ8DciMU%2Bfv8TpJ%2Bd4cAcPiXtTMxXnsMa1lFZs85Y5ML915rIer0Ik2DS9Y11w8jNeW4QXItttrSpbTG0XC3seUtjvMNN%2FZksB70KxEjU%2FaBQXHPvqDdn1gpJ8sMtG%2F%2FQe483odrKImkrf20L8b51SJ5fm6fgHc9rLZWphdH1%2F1vbUtk1bAks3eGiSPtrBOOuKcANUELxQohWWXuqEXN%2Br9PM4HOUobYhGZEWWrmFl6yzVlHUL1pSawRCS9GTTMlCyvvTx07brG%2BhMIXaArMIXZhcwGOqUBLQhR83VF8vK4cj85%2B7h7%2Bg9FRwjdQ6toLGExbilSAW8uwVWbp7x8l6kunr2%2BRVPToSvXv6ag%2Bg3Wfb3TjNWnU%2Bv%2BbTLugQAu3sbiwrmeAl9ZDcUBG7T3ItuHM5ibcg497M8eBGQgQLMU8fA6hy%2F%2FXY7Sag1wsXTRDRgJtDHXHpV%2Fl741HYEure12kNKk6kdPE6RpxGbzFWJ73OKE3Fl%2Fy7FMC5cv&X-Amz-Signature=1dd022aa75b036d2f3ed401553b4f4ac6e18d171c016917d51ce12da69cc27ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RE6NUPIZ%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQD1y8U5AJUGB84x1Hfxcr6zYyKmFvdNX%2BAEDHKcSu9SHQIgV%2FExg68yMl5C%2Bj7dKTM42xXwC21ffBkzxFnBU0%2Fpf%2FYqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTOc24oskIZbl5XvCrcAyoiPTgwpOHwZXoEtNuCdPmk63L1zJpKhTTTUMxJA68s12HGf5Ut3fjVMskRLO0ZVKfL61CxWTZVjhne4TW6jRPRDs%2Fcn0e1XQ3rnoVik2m3gR%2BO7WubX2WaO%2BzOqhWXffdn33ZYKcuEPqc%2Fli7aIGmKgG5NyjerFQQ6H0rZEnEJLNe8QWfD0IsfE1DLCS6dm0s4Fg1IBYW2DV4FSFk7liSZtuz7ycbmha%2FDk1nPBXutWkCP4b0li0brSBKEHUEyqf6v%2FxLitZ512fKobYJ0dw8gj1jLmB9Dgmpcjmk9PJxNfNkUYHlX8IBdc2mnNBjSzIYKzFfXtrxh52d86L9yEgksl6VF%2FujLEGa3LgBaATJ8DciMU%2Bfv8TpJ%2Bd4cAcPiXtTMxXnsMa1lFZs85Y5ML915rIer0Ik2DS9Y11w8jNeW4QXItttrSpbTG0XC3seUtjvMNN%2FZksB70KxEjU%2FaBQXHPvqDdn1gpJ8sMtG%2F%2FQe483odrKImkrf20L8b51SJ5fm6fgHc9rLZWphdH1%2F1vbUtk1bAks3eGiSPtrBOOuKcANUELxQohWWXuqEXN%2Br9PM4HOUobYhGZEWWrmFl6yzVlHUL1pSawRCS9GTTMlCyvvTx07brG%2BhMIXaArMIXZhcwGOqUBLQhR83VF8vK4cj85%2B7h7%2Bg9FRwjdQ6toLGExbilSAW8uwVWbp7x8l6kunr2%2BRVPToSvXv6ag%2Bg3Wfb3TjNWnU%2Bv%2BbTLugQAu3sbiwrmeAl9ZDcUBG7T3ItuHM5ibcg497M8eBGQgQLMU8fA6hy%2F%2FXY7Sag1wsXTRDRgJtDHXHpV%2Fl741HYEure12kNKk6kdPE6RpxGbzFWJ73OKE3Fl%2Fy7FMC5cv&X-Amz-Signature=f2f7a27b2ff69b844edfd0b94451c15f1d7192bf6d3a3433ba0d5569c99d551c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RE6NUPIZ%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQD1y8U5AJUGB84x1Hfxcr6zYyKmFvdNX%2BAEDHKcSu9SHQIgV%2FExg68yMl5C%2Bj7dKTM42xXwC21ffBkzxFnBU0%2Fpf%2FYqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTOc24oskIZbl5XvCrcAyoiPTgwpOHwZXoEtNuCdPmk63L1zJpKhTTTUMxJA68s12HGf5Ut3fjVMskRLO0ZVKfL61CxWTZVjhne4TW6jRPRDs%2Fcn0e1XQ3rnoVik2m3gR%2BO7WubX2WaO%2BzOqhWXffdn33ZYKcuEPqc%2Fli7aIGmKgG5NyjerFQQ6H0rZEnEJLNe8QWfD0IsfE1DLCS6dm0s4Fg1IBYW2DV4FSFk7liSZtuz7ycbmha%2FDk1nPBXutWkCP4b0li0brSBKEHUEyqf6v%2FxLitZ512fKobYJ0dw8gj1jLmB9Dgmpcjmk9PJxNfNkUYHlX8IBdc2mnNBjSzIYKzFfXtrxh52d86L9yEgksl6VF%2FujLEGa3LgBaATJ8DciMU%2Bfv8TpJ%2Bd4cAcPiXtTMxXnsMa1lFZs85Y5ML915rIer0Ik2DS9Y11w8jNeW4QXItttrSpbTG0XC3seUtjvMNN%2FZksB70KxEjU%2FaBQXHPvqDdn1gpJ8sMtG%2F%2FQe483odrKImkrf20L8b51SJ5fm6fgHc9rLZWphdH1%2F1vbUtk1bAks3eGiSPtrBOOuKcANUELxQohWWXuqEXN%2Br9PM4HOUobYhGZEWWrmFl6yzVlHUL1pSawRCS9GTTMlCyvvTx07brG%2BhMIXaArMIXZhcwGOqUBLQhR83VF8vK4cj85%2B7h7%2Bg9FRwjdQ6toLGExbilSAW8uwVWbp7x8l6kunr2%2BRVPToSvXv6ag%2Bg3Wfb3TjNWnU%2Bv%2BbTLugQAu3sbiwrmeAl9ZDcUBG7T3ItuHM5ibcg497M8eBGQgQLMU8fA6hy%2F%2FXY7Sag1wsXTRDRgJtDHXHpV%2Fl741HYEure12kNKk6kdPE6RpxGbzFWJ73OKE3Fl%2Fy7FMC5cv&X-Amz-Signature=6375fa4a692451f8ce224384c2233ef7a3d57cb0dbdec9a9e60bb2c53a546f05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

