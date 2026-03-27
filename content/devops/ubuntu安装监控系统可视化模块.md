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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMTCXIMD%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCGnNAyGpeJnmDeq34qN1aT79Vw%2B7deZHwNTGF1UrqS9AIhAM4LYWp4k%2FkS1q1wXqC7y7oAJvOYMIm%2FQs8Tlekn9j0%2FKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5gSID8mgSvCs19d8q3APqEe%2BtnxeRLP0MUv0SGmIkD9MwJyGx%2Fv6KjHGCE1l3hamLtwL6p35l5OZ7GaJOsza4Qsmu%2Bay1rE1NQ9ete7cZJtQtdxWijuyi9rKJkQwK1YBUkrMwOC1t9B4RowR%2Be%2F4qD%2BDhToVwIpqH23sUQfCHp8fUXBQXc9MyiFJ567sKJRiSK6q8aLjh4w0%2FW466rAQNQ5ze%2FWzdgknTuQLcJL5mgMeHCmMkb0drjqzJwJw17SbHWLwK8YoFDdBSHRbUyaa2AB6NbKFSzlvnvXAd5oTKuKXeIbATpk6jofT0f0uaZYmeofsZjc5tw9iPYEGZiSaBPsc1uk8LMggHUemuMU6EQnhjV3WJHO7J9LY1AKKoVj%2B%2FNAS1U60CFj2Jr%2BcssTixoPLVy7SuXzSusx0DyGUDpwaxODvWB7NI6N2SkdiFwzA06tb%2F5B203zEQKuMBlib%2B6j7FTwTLGh4JEU%2BmnGWwLf5dBmpHEDzT1z9P0vGOwehOaF25GcE%2BNZeQWvlRc5Xg5gsn4A%2FxyzzAi1ujPHQ7aReAQ%2B%2F%2BF1wtrHXELJd0p9ARytU5eFqGBDHprLPn4eRJ%2FDK7XXBBTjhkkxMYHSO2ERy6czvcSuvLH%2F46R1x37y2Th1f6zBMzetzC2TDY75bOBjqkAbTkWleT9N%2BgmrvcTNIPYPC3f2ef3S3wP63gzWXnlqFYtmeubcRESfhyZ52uS9A6ckDuaVcnG1DTxd1A8irKLYsxCC2fWfvDYlTNu3z%2F0m9a69Wy1xatpsY8594zCoh7D1fuP2LGNDfp9Lck5PsiORcC09y0qz7mJbEy2i6Z5oauKa%2FK5sJj1tW%2BsYrbZM6u91qm1DSaMsdYuWWj3h1bt0mPaWqG&X-Amz-Signature=d6381b67997a1cb49b625c1ce0528144e8972b52123b1300db7d018978ab3433&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMTCXIMD%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCGnNAyGpeJnmDeq34qN1aT79Vw%2B7deZHwNTGF1UrqS9AIhAM4LYWp4k%2FkS1q1wXqC7y7oAJvOYMIm%2FQs8Tlekn9j0%2FKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5gSID8mgSvCs19d8q3APqEe%2BtnxeRLP0MUv0SGmIkD9MwJyGx%2Fv6KjHGCE1l3hamLtwL6p35l5OZ7GaJOsza4Qsmu%2Bay1rE1NQ9ete7cZJtQtdxWijuyi9rKJkQwK1YBUkrMwOC1t9B4RowR%2Be%2F4qD%2BDhToVwIpqH23sUQfCHp8fUXBQXc9MyiFJ567sKJRiSK6q8aLjh4w0%2FW466rAQNQ5ze%2FWzdgknTuQLcJL5mgMeHCmMkb0drjqzJwJw17SbHWLwK8YoFDdBSHRbUyaa2AB6NbKFSzlvnvXAd5oTKuKXeIbATpk6jofT0f0uaZYmeofsZjc5tw9iPYEGZiSaBPsc1uk8LMggHUemuMU6EQnhjV3WJHO7J9LY1AKKoVj%2B%2FNAS1U60CFj2Jr%2BcssTixoPLVy7SuXzSusx0DyGUDpwaxODvWB7NI6N2SkdiFwzA06tb%2F5B203zEQKuMBlib%2B6j7FTwTLGh4JEU%2BmnGWwLf5dBmpHEDzT1z9P0vGOwehOaF25GcE%2BNZeQWvlRc5Xg5gsn4A%2FxyzzAi1ujPHQ7aReAQ%2B%2F%2BF1wtrHXELJd0p9ARytU5eFqGBDHprLPn4eRJ%2FDK7XXBBTjhkkxMYHSO2ERy6czvcSuvLH%2F46R1x37y2Th1f6zBMzetzC2TDY75bOBjqkAbTkWleT9N%2BgmrvcTNIPYPC3f2ef3S3wP63gzWXnlqFYtmeubcRESfhyZ52uS9A6ckDuaVcnG1DTxd1A8irKLYsxCC2fWfvDYlTNu3z%2F0m9a69Wy1xatpsY8594zCoh7D1fuP2LGNDfp9Lck5PsiORcC09y0qz7mJbEy2i6Z5oauKa%2FK5sJj1tW%2BsYrbZM6u91qm1DSaMsdYuWWj3h1bt0mPaWqG&X-Amz-Signature=f0980ca0341f18f76b7e80423413a2dd42450177a97172843f058e92c898d849&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMTCXIMD%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCGnNAyGpeJnmDeq34qN1aT79Vw%2B7deZHwNTGF1UrqS9AIhAM4LYWp4k%2FkS1q1wXqC7y7oAJvOYMIm%2FQs8Tlekn9j0%2FKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5gSID8mgSvCs19d8q3APqEe%2BtnxeRLP0MUv0SGmIkD9MwJyGx%2Fv6KjHGCE1l3hamLtwL6p35l5OZ7GaJOsza4Qsmu%2Bay1rE1NQ9ete7cZJtQtdxWijuyi9rKJkQwK1YBUkrMwOC1t9B4RowR%2Be%2F4qD%2BDhToVwIpqH23sUQfCHp8fUXBQXc9MyiFJ567sKJRiSK6q8aLjh4w0%2FW466rAQNQ5ze%2FWzdgknTuQLcJL5mgMeHCmMkb0drjqzJwJw17SbHWLwK8YoFDdBSHRbUyaa2AB6NbKFSzlvnvXAd5oTKuKXeIbATpk6jofT0f0uaZYmeofsZjc5tw9iPYEGZiSaBPsc1uk8LMggHUemuMU6EQnhjV3WJHO7J9LY1AKKoVj%2B%2FNAS1U60CFj2Jr%2BcssTixoPLVy7SuXzSusx0DyGUDpwaxODvWB7NI6N2SkdiFwzA06tb%2F5B203zEQKuMBlib%2B6j7FTwTLGh4JEU%2BmnGWwLf5dBmpHEDzT1z9P0vGOwehOaF25GcE%2BNZeQWvlRc5Xg5gsn4A%2FxyzzAi1ujPHQ7aReAQ%2B%2F%2BF1wtrHXELJd0p9ARytU5eFqGBDHprLPn4eRJ%2FDK7XXBBTjhkkxMYHSO2ERy6czvcSuvLH%2F46R1x37y2Th1f6zBMzetzC2TDY75bOBjqkAbTkWleT9N%2BgmrvcTNIPYPC3f2ef3S3wP63gzWXnlqFYtmeubcRESfhyZ52uS9A6ckDuaVcnG1DTxd1A8irKLYsxCC2fWfvDYlTNu3z%2F0m9a69Wy1xatpsY8594zCoh7D1fuP2LGNDfp9Lck5PsiORcC09y0qz7mJbEy2i6Z5oauKa%2FK5sJj1tW%2BsYrbZM6u91qm1DSaMsdYuWWj3h1bt0mPaWqG&X-Amz-Signature=6c5a27173653df4cc67d2ae9d5c19f5bf5f03a35643a54be3d5fb12aa2f019e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMTCXIMD%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCGnNAyGpeJnmDeq34qN1aT79Vw%2B7deZHwNTGF1UrqS9AIhAM4LYWp4k%2FkS1q1wXqC7y7oAJvOYMIm%2FQs8Tlekn9j0%2FKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5gSID8mgSvCs19d8q3APqEe%2BtnxeRLP0MUv0SGmIkD9MwJyGx%2Fv6KjHGCE1l3hamLtwL6p35l5OZ7GaJOsza4Qsmu%2Bay1rE1NQ9ete7cZJtQtdxWijuyi9rKJkQwK1YBUkrMwOC1t9B4RowR%2Be%2F4qD%2BDhToVwIpqH23sUQfCHp8fUXBQXc9MyiFJ567sKJRiSK6q8aLjh4w0%2FW466rAQNQ5ze%2FWzdgknTuQLcJL5mgMeHCmMkb0drjqzJwJw17SbHWLwK8YoFDdBSHRbUyaa2AB6NbKFSzlvnvXAd5oTKuKXeIbATpk6jofT0f0uaZYmeofsZjc5tw9iPYEGZiSaBPsc1uk8LMggHUemuMU6EQnhjV3WJHO7J9LY1AKKoVj%2B%2FNAS1U60CFj2Jr%2BcssTixoPLVy7SuXzSusx0DyGUDpwaxODvWB7NI6N2SkdiFwzA06tb%2F5B203zEQKuMBlib%2B6j7FTwTLGh4JEU%2BmnGWwLf5dBmpHEDzT1z9P0vGOwehOaF25GcE%2BNZeQWvlRc5Xg5gsn4A%2FxyzzAi1ujPHQ7aReAQ%2B%2F%2BF1wtrHXELJd0p9ARytU5eFqGBDHprLPn4eRJ%2FDK7XXBBTjhkkxMYHSO2ERy6czvcSuvLH%2F46R1x37y2Th1f6zBMzetzC2TDY75bOBjqkAbTkWleT9N%2BgmrvcTNIPYPC3f2ef3S3wP63gzWXnlqFYtmeubcRESfhyZ52uS9A6ckDuaVcnG1DTxd1A8irKLYsxCC2fWfvDYlTNu3z%2F0m9a69Wy1xatpsY8594zCoh7D1fuP2LGNDfp9Lck5PsiORcC09y0qz7mJbEy2i6Z5oauKa%2FK5sJj1tW%2BsYrbZM6u91qm1DSaMsdYuWWj3h1bt0mPaWqG&X-Amz-Signature=a2f082118060025d8fdf8d91a9e4809266b7ff1522ad8be1b8d194515258177a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMTCXIMD%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCGnNAyGpeJnmDeq34qN1aT79Vw%2B7deZHwNTGF1UrqS9AIhAM4LYWp4k%2FkS1q1wXqC7y7oAJvOYMIm%2FQs8Tlekn9j0%2FKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5gSID8mgSvCs19d8q3APqEe%2BtnxeRLP0MUv0SGmIkD9MwJyGx%2Fv6KjHGCE1l3hamLtwL6p35l5OZ7GaJOsza4Qsmu%2Bay1rE1NQ9ete7cZJtQtdxWijuyi9rKJkQwK1YBUkrMwOC1t9B4RowR%2Be%2F4qD%2BDhToVwIpqH23sUQfCHp8fUXBQXc9MyiFJ567sKJRiSK6q8aLjh4w0%2FW466rAQNQ5ze%2FWzdgknTuQLcJL5mgMeHCmMkb0drjqzJwJw17SbHWLwK8YoFDdBSHRbUyaa2AB6NbKFSzlvnvXAd5oTKuKXeIbATpk6jofT0f0uaZYmeofsZjc5tw9iPYEGZiSaBPsc1uk8LMggHUemuMU6EQnhjV3WJHO7J9LY1AKKoVj%2B%2FNAS1U60CFj2Jr%2BcssTixoPLVy7SuXzSusx0DyGUDpwaxODvWB7NI6N2SkdiFwzA06tb%2F5B203zEQKuMBlib%2B6j7FTwTLGh4JEU%2BmnGWwLf5dBmpHEDzT1z9P0vGOwehOaF25GcE%2BNZeQWvlRc5Xg5gsn4A%2FxyzzAi1ujPHQ7aReAQ%2B%2F%2BF1wtrHXELJd0p9ARytU5eFqGBDHprLPn4eRJ%2FDK7XXBBTjhkkxMYHSO2ERy6czvcSuvLH%2F46R1x37y2Th1f6zBMzetzC2TDY75bOBjqkAbTkWleT9N%2BgmrvcTNIPYPC3f2ef3S3wP63gzWXnlqFYtmeubcRESfhyZ52uS9A6ckDuaVcnG1DTxd1A8irKLYsxCC2fWfvDYlTNu3z%2F0m9a69Wy1xatpsY8594zCoh7D1fuP2LGNDfp9Lck5PsiORcC09y0qz7mJbEy2i6Z5oauKa%2FK5sJj1tW%2BsYrbZM6u91qm1DSaMsdYuWWj3h1bt0mPaWqG&X-Amz-Signature=d7427f3a733902d01c327ea00635befe37316b9bb280f2ae338968a07e27121e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMTCXIMD%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCGnNAyGpeJnmDeq34qN1aT79Vw%2B7deZHwNTGF1UrqS9AIhAM4LYWp4k%2FkS1q1wXqC7y7oAJvOYMIm%2FQs8Tlekn9j0%2FKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5gSID8mgSvCs19d8q3APqEe%2BtnxeRLP0MUv0SGmIkD9MwJyGx%2Fv6KjHGCE1l3hamLtwL6p35l5OZ7GaJOsza4Qsmu%2Bay1rE1NQ9ete7cZJtQtdxWijuyi9rKJkQwK1YBUkrMwOC1t9B4RowR%2Be%2F4qD%2BDhToVwIpqH23sUQfCHp8fUXBQXc9MyiFJ567sKJRiSK6q8aLjh4w0%2FW466rAQNQ5ze%2FWzdgknTuQLcJL5mgMeHCmMkb0drjqzJwJw17SbHWLwK8YoFDdBSHRbUyaa2AB6NbKFSzlvnvXAd5oTKuKXeIbATpk6jofT0f0uaZYmeofsZjc5tw9iPYEGZiSaBPsc1uk8LMggHUemuMU6EQnhjV3WJHO7J9LY1AKKoVj%2B%2FNAS1U60CFj2Jr%2BcssTixoPLVy7SuXzSusx0DyGUDpwaxODvWB7NI6N2SkdiFwzA06tb%2F5B203zEQKuMBlib%2B6j7FTwTLGh4JEU%2BmnGWwLf5dBmpHEDzT1z9P0vGOwehOaF25GcE%2BNZeQWvlRc5Xg5gsn4A%2FxyzzAi1ujPHQ7aReAQ%2B%2F%2BF1wtrHXELJd0p9ARytU5eFqGBDHprLPn4eRJ%2FDK7XXBBTjhkkxMYHSO2ERy6czvcSuvLH%2F46R1x37y2Th1f6zBMzetzC2TDY75bOBjqkAbTkWleT9N%2BgmrvcTNIPYPC3f2ef3S3wP63gzWXnlqFYtmeubcRESfhyZ52uS9A6ckDuaVcnG1DTxd1A8irKLYsxCC2fWfvDYlTNu3z%2F0m9a69Wy1xatpsY8594zCoh7D1fuP2LGNDfp9Lck5PsiORcC09y0qz7mJbEy2i6Z5oauKa%2FK5sJj1tW%2BsYrbZM6u91qm1DSaMsdYuWWj3h1bt0mPaWqG&X-Amz-Signature=74248334c226ddc740ffa4550b561fdd7b5d262a8b6eb065d4561a02236bbbbe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMTCXIMD%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCGnNAyGpeJnmDeq34qN1aT79Vw%2B7deZHwNTGF1UrqS9AIhAM4LYWp4k%2FkS1q1wXqC7y7oAJvOYMIm%2FQs8Tlekn9j0%2FKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5gSID8mgSvCs19d8q3APqEe%2BtnxeRLP0MUv0SGmIkD9MwJyGx%2Fv6KjHGCE1l3hamLtwL6p35l5OZ7GaJOsza4Qsmu%2Bay1rE1NQ9ete7cZJtQtdxWijuyi9rKJkQwK1YBUkrMwOC1t9B4RowR%2Be%2F4qD%2BDhToVwIpqH23sUQfCHp8fUXBQXc9MyiFJ567sKJRiSK6q8aLjh4w0%2FW466rAQNQ5ze%2FWzdgknTuQLcJL5mgMeHCmMkb0drjqzJwJw17SbHWLwK8YoFDdBSHRbUyaa2AB6NbKFSzlvnvXAd5oTKuKXeIbATpk6jofT0f0uaZYmeofsZjc5tw9iPYEGZiSaBPsc1uk8LMggHUemuMU6EQnhjV3WJHO7J9LY1AKKoVj%2B%2FNAS1U60CFj2Jr%2BcssTixoPLVy7SuXzSusx0DyGUDpwaxODvWB7NI6N2SkdiFwzA06tb%2F5B203zEQKuMBlib%2B6j7FTwTLGh4JEU%2BmnGWwLf5dBmpHEDzT1z9P0vGOwehOaF25GcE%2BNZeQWvlRc5Xg5gsn4A%2FxyzzAi1ujPHQ7aReAQ%2B%2F%2BF1wtrHXELJd0p9ARytU5eFqGBDHprLPn4eRJ%2FDK7XXBBTjhkkxMYHSO2ERy6czvcSuvLH%2F46R1x37y2Th1f6zBMzetzC2TDY75bOBjqkAbTkWleT9N%2BgmrvcTNIPYPC3f2ef3S3wP63gzWXnlqFYtmeubcRESfhyZ52uS9A6ckDuaVcnG1DTxd1A8irKLYsxCC2fWfvDYlTNu3z%2F0m9a69Wy1xatpsY8594zCoh7D1fuP2LGNDfp9Lck5PsiORcC09y0qz7mJbEy2i6Z5oauKa%2FK5sJj1tW%2BsYrbZM6u91qm1DSaMsdYuWWj3h1bt0mPaWqG&X-Amz-Signature=18a8453457ecddf6cd43e87292083befd3011655afc6839be708382e804cfa88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

