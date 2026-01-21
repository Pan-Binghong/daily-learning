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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642JSI7J6%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDKCyFiSYkilHG4Ye24pDvejwft0jMWMSmroGmi6%2BGAbAiEA8nCsEAK2a4k74I4EjC%2F3fUCXIoaTgOuN%2B8xP9mrTm7wqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK29IRqH864WzLsQwyrcAwbiSGxCmo8gteOI%2Bd4kBJM9gZWbE8IJhNFXf3mZ%2FmKirrNJi%2FnCnX4YURYS8ayIIYmYBIQfya%2BjwIsJ9p0jqqdKidX4Ml%2FEeyoSuu0mJ63GNmqwRvFbqQwlyzPQ7qOF466y5V7stg0uAUad3F7aAPANGkLxFWKOarAfRNeakFdBFspPkRTgkF8vxCtDP10JBzh6fBn4tqlD3KjzGIUHVd2ikOAak4NW0TYlgJh5h23cEMhSyiotWn6KKrqWjX33gC7%2FA52FNY1UuASv1FkRvf5aUmrE2YruUx1Mw%2Bls4VnUdS4sTA6Hy9LkLQhRfDF0ln0Jhj6D63pFVIHi9ctNxjzy4MULzop78imufzX%2Fj8wEWzPpxg6fBW2NCg7DwpHwziAkC3z4gcK3D2ORGzGL5eetGXKQYncBj8ZyA4v1zhiLZ9EA2%2BzAA05DNInxXLMmQwcBkF9HDMse2SivgoMegTeVrfTuqDCXvgODWWx4B0vmo0t8xzwSzHQwzsea24jrFT26DASHLlvtQ%2BVHDz0gic%2BBktTX6pcFBZ0F4qllC1a6uez6qKVwAu4AKu9tYSIW2UFgXJN09WcK2VeWe3Pp%2FSQ5RWfLjhpBeQspWMHDfLOsN3ScGnKc1jCSQ3s8MJXZwMsGOqUB5TrZFZQew2%2FCC5dAWId9mFbJLCjH3Kk1jxyDy1MUm7XaOt2uuZAku2%2BAPQCpWxDvEwv%2BYiumNWLDJiGVn%2BDoo9LpgKbHufEskfGM7QfzpmlQJG%2FWPDd8fvdLCHuDMzKXcjoLHEyASiROJREppQv3Z5iD6hNApL3oLgswFh%2FaHTTQrCCe%2Byn6tDSUGcmM%2BF9H9ZEVjWLAvXGaqH4%2FOW%2FTQ85aTEBG&X-Amz-Signature=c668f9ccbdc90f66b660d3850b2ac929007d03045926ad7d4ab7227d649f2a58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642JSI7J6%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDKCyFiSYkilHG4Ye24pDvejwft0jMWMSmroGmi6%2BGAbAiEA8nCsEAK2a4k74I4EjC%2F3fUCXIoaTgOuN%2B8xP9mrTm7wqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK29IRqH864WzLsQwyrcAwbiSGxCmo8gteOI%2Bd4kBJM9gZWbE8IJhNFXf3mZ%2FmKirrNJi%2FnCnX4YURYS8ayIIYmYBIQfya%2BjwIsJ9p0jqqdKidX4Ml%2FEeyoSuu0mJ63GNmqwRvFbqQwlyzPQ7qOF466y5V7stg0uAUad3F7aAPANGkLxFWKOarAfRNeakFdBFspPkRTgkF8vxCtDP10JBzh6fBn4tqlD3KjzGIUHVd2ikOAak4NW0TYlgJh5h23cEMhSyiotWn6KKrqWjX33gC7%2FA52FNY1UuASv1FkRvf5aUmrE2YruUx1Mw%2Bls4VnUdS4sTA6Hy9LkLQhRfDF0ln0Jhj6D63pFVIHi9ctNxjzy4MULzop78imufzX%2Fj8wEWzPpxg6fBW2NCg7DwpHwziAkC3z4gcK3D2ORGzGL5eetGXKQYncBj8ZyA4v1zhiLZ9EA2%2BzAA05DNInxXLMmQwcBkF9HDMse2SivgoMegTeVrfTuqDCXvgODWWx4B0vmo0t8xzwSzHQwzsea24jrFT26DASHLlvtQ%2BVHDz0gic%2BBktTX6pcFBZ0F4qllC1a6uez6qKVwAu4AKu9tYSIW2UFgXJN09WcK2VeWe3Pp%2FSQ5RWfLjhpBeQspWMHDfLOsN3ScGnKc1jCSQ3s8MJXZwMsGOqUB5TrZFZQew2%2FCC5dAWId9mFbJLCjH3Kk1jxyDy1MUm7XaOt2uuZAku2%2BAPQCpWxDvEwv%2BYiumNWLDJiGVn%2BDoo9LpgKbHufEskfGM7QfzpmlQJG%2FWPDd8fvdLCHuDMzKXcjoLHEyASiROJREppQv3Z5iD6hNApL3oLgswFh%2FaHTTQrCCe%2Byn6tDSUGcmM%2BF9H9ZEVjWLAvXGaqH4%2FOW%2FTQ85aTEBG&X-Amz-Signature=956e8b8e38c05fa304711c46bdc49319730290ad08f311cc74001810051a4f7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642JSI7J6%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDKCyFiSYkilHG4Ye24pDvejwft0jMWMSmroGmi6%2BGAbAiEA8nCsEAK2a4k74I4EjC%2F3fUCXIoaTgOuN%2B8xP9mrTm7wqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK29IRqH864WzLsQwyrcAwbiSGxCmo8gteOI%2Bd4kBJM9gZWbE8IJhNFXf3mZ%2FmKirrNJi%2FnCnX4YURYS8ayIIYmYBIQfya%2BjwIsJ9p0jqqdKidX4Ml%2FEeyoSuu0mJ63GNmqwRvFbqQwlyzPQ7qOF466y5V7stg0uAUad3F7aAPANGkLxFWKOarAfRNeakFdBFspPkRTgkF8vxCtDP10JBzh6fBn4tqlD3KjzGIUHVd2ikOAak4NW0TYlgJh5h23cEMhSyiotWn6KKrqWjX33gC7%2FA52FNY1UuASv1FkRvf5aUmrE2YruUx1Mw%2Bls4VnUdS4sTA6Hy9LkLQhRfDF0ln0Jhj6D63pFVIHi9ctNxjzy4MULzop78imufzX%2Fj8wEWzPpxg6fBW2NCg7DwpHwziAkC3z4gcK3D2ORGzGL5eetGXKQYncBj8ZyA4v1zhiLZ9EA2%2BzAA05DNInxXLMmQwcBkF9HDMse2SivgoMegTeVrfTuqDCXvgODWWx4B0vmo0t8xzwSzHQwzsea24jrFT26DASHLlvtQ%2BVHDz0gic%2BBktTX6pcFBZ0F4qllC1a6uez6qKVwAu4AKu9tYSIW2UFgXJN09WcK2VeWe3Pp%2FSQ5RWfLjhpBeQspWMHDfLOsN3ScGnKc1jCSQ3s8MJXZwMsGOqUB5TrZFZQew2%2FCC5dAWId9mFbJLCjH3Kk1jxyDy1MUm7XaOt2uuZAku2%2BAPQCpWxDvEwv%2BYiumNWLDJiGVn%2BDoo9LpgKbHufEskfGM7QfzpmlQJG%2FWPDd8fvdLCHuDMzKXcjoLHEyASiROJREppQv3Z5iD6hNApL3oLgswFh%2FaHTTQrCCe%2Byn6tDSUGcmM%2BF9H9ZEVjWLAvXGaqH4%2FOW%2FTQ85aTEBG&X-Amz-Signature=75250c218c8a1f6c714790b7fb8417d6868bede76a44108d70d5550ee985976d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642JSI7J6%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDKCyFiSYkilHG4Ye24pDvejwft0jMWMSmroGmi6%2BGAbAiEA8nCsEAK2a4k74I4EjC%2F3fUCXIoaTgOuN%2B8xP9mrTm7wqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK29IRqH864WzLsQwyrcAwbiSGxCmo8gteOI%2Bd4kBJM9gZWbE8IJhNFXf3mZ%2FmKirrNJi%2FnCnX4YURYS8ayIIYmYBIQfya%2BjwIsJ9p0jqqdKidX4Ml%2FEeyoSuu0mJ63GNmqwRvFbqQwlyzPQ7qOF466y5V7stg0uAUad3F7aAPANGkLxFWKOarAfRNeakFdBFspPkRTgkF8vxCtDP10JBzh6fBn4tqlD3KjzGIUHVd2ikOAak4NW0TYlgJh5h23cEMhSyiotWn6KKrqWjX33gC7%2FA52FNY1UuASv1FkRvf5aUmrE2YruUx1Mw%2Bls4VnUdS4sTA6Hy9LkLQhRfDF0ln0Jhj6D63pFVIHi9ctNxjzy4MULzop78imufzX%2Fj8wEWzPpxg6fBW2NCg7DwpHwziAkC3z4gcK3D2ORGzGL5eetGXKQYncBj8ZyA4v1zhiLZ9EA2%2BzAA05DNInxXLMmQwcBkF9HDMse2SivgoMegTeVrfTuqDCXvgODWWx4B0vmo0t8xzwSzHQwzsea24jrFT26DASHLlvtQ%2BVHDz0gic%2BBktTX6pcFBZ0F4qllC1a6uez6qKVwAu4AKu9tYSIW2UFgXJN09WcK2VeWe3Pp%2FSQ5RWfLjhpBeQspWMHDfLOsN3ScGnKc1jCSQ3s8MJXZwMsGOqUB5TrZFZQew2%2FCC5dAWId9mFbJLCjH3Kk1jxyDy1MUm7XaOt2uuZAku2%2BAPQCpWxDvEwv%2BYiumNWLDJiGVn%2BDoo9LpgKbHufEskfGM7QfzpmlQJG%2FWPDd8fvdLCHuDMzKXcjoLHEyASiROJREppQv3Z5iD6hNApL3oLgswFh%2FaHTTQrCCe%2Byn6tDSUGcmM%2BF9H9ZEVjWLAvXGaqH4%2FOW%2FTQ85aTEBG&X-Amz-Signature=cc969bcea6d678faea6b562eb519e067b7e17d64de2a6a6efcaacdb4c2a444ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642JSI7J6%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDKCyFiSYkilHG4Ye24pDvejwft0jMWMSmroGmi6%2BGAbAiEA8nCsEAK2a4k74I4EjC%2F3fUCXIoaTgOuN%2B8xP9mrTm7wqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK29IRqH864WzLsQwyrcAwbiSGxCmo8gteOI%2Bd4kBJM9gZWbE8IJhNFXf3mZ%2FmKirrNJi%2FnCnX4YURYS8ayIIYmYBIQfya%2BjwIsJ9p0jqqdKidX4Ml%2FEeyoSuu0mJ63GNmqwRvFbqQwlyzPQ7qOF466y5V7stg0uAUad3F7aAPANGkLxFWKOarAfRNeakFdBFspPkRTgkF8vxCtDP10JBzh6fBn4tqlD3KjzGIUHVd2ikOAak4NW0TYlgJh5h23cEMhSyiotWn6KKrqWjX33gC7%2FA52FNY1UuASv1FkRvf5aUmrE2YruUx1Mw%2Bls4VnUdS4sTA6Hy9LkLQhRfDF0ln0Jhj6D63pFVIHi9ctNxjzy4MULzop78imufzX%2Fj8wEWzPpxg6fBW2NCg7DwpHwziAkC3z4gcK3D2ORGzGL5eetGXKQYncBj8ZyA4v1zhiLZ9EA2%2BzAA05DNInxXLMmQwcBkF9HDMse2SivgoMegTeVrfTuqDCXvgODWWx4B0vmo0t8xzwSzHQwzsea24jrFT26DASHLlvtQ%2BVHDz0gic%2BBktTX6pcFBZ0F4qllC1a6uez6qKVwAu4AKu9tYSIW2UFgXJN09WcK2VeWe3Pp%2FSQ5RWfLjhpBeQspWMHDfLOsN3ScGnKc1jCSQ3s8MJXZwMsGOqUB5TrZFZQew2%2FCC5dAWId9mFbJLCjH3Kk1jxyDy1MUm7XaOt2uuZAku2%2BAPQCpWxDvEwv%2BYiumNWLDJiGVn%2BDoo9LpgKbHufEskfGM7QfzpmlQJG%2FWPDd8fvdLCHuDMzKXcjoLHEyASiROJREppQv3Z5iD6hNApL3oLgswFh%2FaHTTQrCCe%2Byn6tDSUGcmM%2BF9H9ZEVjWLAvXGaqH4%2FOW%2FTQ85aTEBG&X-Amz-Signature=cb49c8e134ff5920c1e315dfae08a3f928b645a573129077c237c4ce00dd32c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642JSI7J6%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDKCyFiSYkilHG4Ye24pDvejwft0jMWMSmroGmi6%2BGAbAiEA8nCsEAK2a4k74I4EjC%2F3fUCXIoaTgOuN%2B8xP9mrTm7wqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK29IRqH864WzLsQwyrcAwbiSGxCmo8gteOI%2Bd4kBJM9gZWbE8IJhNFXf3mZ%2FmKirrNJi%2FnCnX4YURYS8ayIIYmYBIQfya%2BjwIsJ9p0jqqdKidX4Ml%2FEeyoSuu0mJ63GNmqwRvFbqQwlyzPQ7qOF466y5V7stg0uAUad3F7aAPANGkLxFWKOarAfRNeakFdBFspPkRTgkF8vxCtDP10JBzh6fBn4tqlD3KjzGIUHVd2ikOAak4NW0TYlgJh5h23cEMhSyiotWn6KKrqWjX33gC7%2FA52FNY1UuASv1FkRvf5aUmrE2YruUx1Mw%2Bls4VnUdS4sTA6Hy9LkLQhRfDF0ln0Jhj6D63pFVIHi9ctNxjzy4MULzop78imufzX%2Fj8wEWzPpxg6fBW2NCg7DwpHwziAkC3z4gcK3D2ORGzGL5eetGXKQYncBj8ZyA4v1zhiLZ9EA2%2BzAA05DNInxXLMmQwcBkF9HDMse2SivgoMegTeVrfTuqDCXvgODWWx4B0vmo0t8xzwSzHQwzsea24jrFT26DASHLlvtQ%2BVHDz0gic%2BBktTX6pcFBZ0F4qllC1a6uez6qKVwAu4AKu9tYSIW2UFgXJN09WcK2VeWe3Pp%2FSQ5RWfLjhpBeQspWMHDfLOsN3ScGnKc1jCSQ3s8MJXZwMsGOqUB5TrZFZQew2%2FCC5dAWId9mFbJLCjH3Kk1jxyDy1MUm7XaOt2uuZAku2%2BAPQCpWxDvEwv%2BYiumNWLDJiGVn%2BDoo9LpgKbHufEskfGM7QfzpmlQJG%2FWPDd8fvdLCHuDMzKXcjoLHEyASiROJREppQv3Z5iD6hNApL3oLgswFh%2FaHTTQrCCe%2Byn6tDSUGcmM%2BF9H9ZEVjWLAvXGaqH4%2FOW%2FTQ85aTEBG&X-Amz-Signature=9d9528ffc14741a8ca5c09d24c956c9e0e8488d236059a18dc951470e0fcc583&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642JSI7J6%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDKCyFiSYkilHG4Ye24pDvejwft0jMWMSmroGmi6%2BGAbAiEA8nCsEAK2a4k74I4EjC%2F3fUCXIoaTgOuN%2B8xP9mrTm7wqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK29IRqH864WzLsQwyrcAwbiSGxCmo8gteOI%2Bd4kBJM9gZWbE8IJhNFXf3mZ%2FmKirrNJi%2FnCnX4YURYS8ayIIYmYBIQfya%2BjwIsJ9p0jqqdKidX4Ml%2FEeyoSuu0mJ63GNmqwRvFbqQwlyzPQ7qOF466y5V7stg0uAUad3F7aAPANGkLxFWKOarAfRNeakFdBFspPkRTgkF8vxCtDP10JBzh6fBn4tqlD3KjzGIUHVd2ikOAak4NW0TYlgJh5h23cEMhSyiotWn6KKrqWjX33gC7%2FA52FNY1UuASv1FkRvf5aUmrE2YruUx1Mw%2Bls4VnUdS4sTA6Hy9LkLQhRfDF0ln0Jhj6D63pFVIHi9ctNxjzy4MULzop78imufzX%2Fj8wEWzPpxg6fBW2NCg7DwpHwziAkC3z4gcK3D2ORGzGL5eetGXKQYncBj8ZyA4v1zhiLZ9EA2%2BzAA05DNInxXLMmQwcBkF9HDMse2SivgoMegTeVrfTuqDCXvgODWWx4B0vmo0t8xzwSzHQwzsea24jrFT26DASHLlvtQ%2BVHDz0gic%2BBktTX6pcFBZ0F4qllC1a6uez6qKVwAu4AKu9tYSIW2UFgXJN09WcK2VeWe3Pp%2FSQ5RWfLjhpBeQspWMHDfLOsN3ScGnKc1jCSQ3s8MJXZwMsGOqUB5TrZFZQew2%2FCC5dAWId9mFbJLCjH3Kk1jxyDy1MUm7XaOt2uuZAku2%2BAPQCpWxDvEwv%2BYiumNWLDJiGVn%2BDoo9LpgKbHufEskfGM7QfzpmlQJG%2FWPDd8fvdLCHuDMzKXcjoLHEyASiROJREppQv3Z5iD6hNApL3oLgswFh%2FaHTTQrCCe%2Byn6tDSUGcmM%2BF9H9ZEVjWLAvXGaqH4%2FOW%2FTQ85aTEBG&X-Amz-Signature=549ff44b27a2dd6283b098922f18f27a90f9f4ea03c2f584f3d1986420b48bd2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

