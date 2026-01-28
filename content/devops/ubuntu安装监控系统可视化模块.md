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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QX6K5QCF%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8CLrzg7l6YhK6dycCxxgnfjjJ%2F7Myntp9ibDABCS8fgIhAJPcDUcOtd3YRkg3VxH4QZtBUNv8VTPCq8Va0jUm6lnGKv8DCGEQABoMNjM3NDIzMTgzODA1IgxoZXH164GDLwgfrnMq3APRoRTZUVIAoT0wIrQrKGDeMIkLGZinGzlZ9LwhKQXuUpzMTSN8ye0C34tiiMLEn2hn7Ka%2Fnqgu78ouAktJcLZkW3gGT3CjRBq%2BwyhNpKn0sXr7Gl3JpDCO%2F%2BUnRSCOkVdHKyk%2FrHaZO%2F%2FIMk%2BLHs3I%2FXVoikwvT4hU4wJ9WznrRjNFt%2B6%2FjyuJoTMuVXvQ1YqGWcCWQvITAKa5eDWIGaDcc7hYYwT84njBaclpOW3wbNLJrmuc5qjzOaaCJEBjJhmzBvk9CGuaSVR9uVthiwC8KZIQEB%2B2jxxFr3lj977DxZpd2AqssdRbwoRmalWftRPIY%2Fv7WrYgy6cWQKLcQbLG8Ev946%2B0ixtkfKAMxg%2BIQ969QEYlWoTGkPfsofg%2FNE%2BEGz4eSkzUFV8Vt7i6QaUvRJna5ssff5EVAj2kwiSiVVH767OgnfKYNQzhmJKKh7ZWWLOij7ymudDX0p0y2i%2Fn70CkZpYJmN%2FSJIQhqlvVU9JFw0dX3CP3Vkp75%2BQjLVQo3SHNrQdvmGvUprcslCWD7Vfzo61dt6x1WZK5XUQezxnrAGTpUmDsRfFPtrwF6W36RZivHPN2mqw8sj3Pibv231N3Bl9nWBCE7P%2BS%2BoMnH6VDgwurja2RgyMm6zDyleXLBjqkAeYvJxoBQ7pM3QPVHS7q538XxbgSkDx39E7FWAo3DvhQf8H2JslqfLqrj3JrhDxKGUVatKFqWlD87RRVxyj49rzYPTKlUth215cgT6lmWtcRvaQeKMeUNqGksOtqHXjvde%2BQrVupAFX2o7bnBuYEJywwBoUwPMvAaxg7TPFApN3kg0DDM5gHv9DJE0d8nwSp8UlxMMhWMOaNZbzptSP%2FQQuJKI%2Bo&X-Amz-Signature=e5161621ab821278d6be962f82fccabbab7e73e2fbdf94d7d4a3724b3e2a6dda&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QX6K5QCF%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8CLrzg7l6YhK6dycCxxgnfjjJ%2F7Myntp9ibDABCS8fgIhAJPcDUcOtd3YRkg3VxH4QZtBUNv8VTPCq8Va0jUm6lnGKv8DCGEQABoMNjM3NDIzMTgzODA1IgxoZXH164GDLwgfrnMq3APRoRTZUVIAoT0wIrQrKGDeMIkLGZinGzlZ9LwhKQXuUpzMTSN8ye0C34tiiMLEn2hn7Ka%2Fnqgu78ouAktJcLZkW3gGT3CjRBq%2BwyhNpKn0sXr7Gl3JpDCO%2F%2BUnRSCOkVdHKyk%2FrHaZO%2F%2FIMk%2BLHs3I%2FXVoikwvT4hU4wJ9WznrRjNFt%2B6%2FjyuJoTMuVXvQ1YqGWcCWQvITAKa5eDWIGaDcc7hYYwT84njBaclpOW3wbNLJrmuc5qjzOaaCJEBjJhmzBvk9CGuaSVR9uVthiwC8KZIQEB%2B2jxxFr3lj977DxZpd2AqssdRbwoRmalWftRPIY%2Fv7WrYgy6cWQKLcQbLG8Ev946%2B0ixtkfKAMxg%2BIQ969QEYlWoTGkPfsofg%2FNE%2BEGz4eSkzUFV8Vt7i6QaUvRJna5ssff5EVAj2kwiSiVVH767OgnfKYNQzhmJKKh7ZWWLOij7ymudDX0p0y2i%2Fn70CkZpYJmN%2FSJIQhqlvVU9JFw0dX3CP3Vkp75%2BQjLVQo3SHNrQdvmGvUprcslCWD7Vfzo61dt6x1WZK5XUQezxnrAGTpUmDsRfFPtrwF6W36RZivHPN2mqw8sj3Pibv231N3Bl9nWBCE7P%2BS%2BoMnH6VDgwurja2RgyMm6zDyleXLBjqkAeYvJxoBQ7pM3QPVHS7q538XxbgSkDx39E7FWAo3DvhQf8H2JslqfLqrj3JrhDxKGUVatKFqWlD87RRVxyj49rzYPTKlUth215cgT6lmWtcRvaQeKMeUNqGksOtqHXjvde%2BQrVupAFX2o7bnBuYEJywwBoUwPMvAaxg7TPFApN3kg0DDM5gHv9DJE0d8nwSp8UlxMMhWMOaNZbzptSP%2FQQuJKI%2Bo&X-Amz-Signature=86cef74e313d5eda58f6d26391f839dd62ccbabcf1ff9e26aff7cad99e009121&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QX6K5QCF%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8CLrzg7l6YhK6dycCxxgnfjjJ%2F7Myntp9ibDABCS8fgIhAJPcDUcOtd3YRkg3VxH4QZtBUNv8VTPCq8Va0jUm6lnGKv8DCGEQABoMNjM3NDIzMTgzODA1IgxoZXH164GDLwgfrnMq3APRoRTZUVIAoT0wIrQrKGDeMIkLGZinGzlZ9LwhKQXuUpzMTSN8ye0C34tiiMLEn2hn7Ka%2Fnqgu78ouAktJcLZkW3gGT3CjRBq%2BwyhNpKn0sXr7Gl3JpDCO%2F%2BUnRSCOkVdHKyk%2FrHaZO%2F%2FIMk%2BLHs3I%2FXVoikwvT4hU4wJ9WznrRjNFt%2B6%2FjyuJoTMuVXvQ1YqGWcCWQvITAKa5eDWIGaDcc7hYYwT84njBaclpOW3wbNLJrmuc5qjzOaaCJEBjJhmzBvk9CGuaSVR9uVthiwC8KZIQEB%2B2jxxFr3lj977DxZpd2AqssdRbwoRmalWftRPIY%2Fv7WrYgy6cWQKLcQbLG8Ev946%2B0ixtkfKAMxg%2BIQ969QEYlWoTGkPfsofg%2FNE%2BEGz4eSkzUFV8Vt7i6QaUvRJna5ssff5EVAj2kwiSiVVH767OgnfKYNQzhmJKKh7ZWWLOij7ymudDX0p0y2i%2Fn70CkZpYJmN%2FSJIQhqlvVU9JFw0dX3CP3Vkp75%2BQjLVQo3SHNrQdvmGvUprcslCWD7Vfzo61dt6x1WZK5XUQezxnrAGTpUmDsRfFPtrwF6W36RZivHPN2mqw8sj3Pibv231N3Bl9nWBCE7P%2BS%2BoMnH6VDgwurja2RgyMm6zDyleXLBjqkAeYvJxoBQ7pM3QPVHS7q538XxbgSkDx39E7FWAo3DvhQf8H2JslqfLqrj3JrhDxKGUVatKFqWlD87RRVxyj49rzYPTKlUth215cgT6lmWtcRvaQeKMeUNqGksOtqHXjvde%2BQrVupAFX2o7bnBuYEJywwBoUwPMvAaxg7TPFApN3kg0DDM5gHv9DJE0d8nwSp8UlxMMhWMOaNZbzptSP%2FQQuJKI%2Bo&X-Amz-Signature=57ef6c3e6fd8155a95b79c02f861e1ff022df70fdc4f0a5415f6f7050612f0cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QX6K5QCF%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8CLrzg7l6YhK6dycCxxgnfjjJ%2F7Myntp9ibDABCS8fgIhAJPcDUcOtd3YRkg3VxH4QZtBUNv8VTPCq8Va0jUm6lnGKv8DCGEQABoMNjM3NDIzMTgzODA1IgxoZXH164GDLwgfrnMq3APRoRTZUVIAoT0wIrQrKGDeMIkLGZinGzlZ9LwhKQXuUpzMTSN8ye0C34tiiMLEn2hn7Ka%2Fnqgu78ouAktJcLZkW3gGT3CjRBq%2BwyhNpKn0sXr7Gl3JpDCO%2F%2BUnRSCOkVdHKyk%2FrHaZO%2F%2FIMk%2BLHs3I%2FXVoikwvT4hU4wJ9WznrRjNFt%2B6%2FjyuJoTMuVXvQ1YqGWcCWQvITAKa5eDWIGaDcc7hYYwT84njBaclpOW3wbNLJrmuc5qjzOaaCJEBjJhmzBvk9CGuaSVR9uVthiwC8KZIQEB%2B2jxxFr3lj977DxZpd2AqssdRbwoRmalWftRPIY%2Fv7WrYgy6cWQKLcQbLG8Ev946%2B0ixtkfKAMxg%2BIQ969QEYlWoTGkPfsofg%2FNE%2BEGz4eSkzUFV8Vt7i6QaUvRJna5ssff5EVAj2kwiSiVVH767OgnfKYNQzhmJKKh7ZWWLOij7ymudDX0p0y2i%2Fn70CkZpYJmN%2FSJIQhqlvVU9JFw0dX3CP3Vkp75%2BQjLVQo3SHNrQdvmGvUprcslCWD7Vfzo61dt6x1WZK5XUQezxnrAGTpUmDsRfFPtrwF6W36RZivHPN2mqw8sj3Pibv231N3Bl9nWBCE7P%2BS%2BoMnH6VDgwurja2RgyMm6zDyleXLBjqkAeYvJxoBQ7pM3QPVHS7q538XxbgSkDx39E7FWAo3DvhQf8H2JslqfLqrj3JrhDxKGUVatKFqWlD87RRVxyj49rzYPTKlUth215cgT6lmWtcRvaQeKMeUNqGksOtqHXjvde%2BQrVupAFX2o7bnBuYEJywwBoUwPMvAaxg7TPFApN3kg0DDM5gHv9DJE0d8nwSp8UlxMMhWMOaNZbzptSP%2FQQuJKI%2Bo&X-Amz-Signature=42712a7e1fb00966031f460213074534ce6b50686904bab3b0ce6df1a0118658&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QX6K5QCF%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8CLrzg7l6YhK6dycCxxgnfjjJ%2F7Myntp9ibDABCS8fgIhAJPcDUcOtd3YRkg3VxH4QZtBUNv8VTPCq8Va0jUm6lnGKv8DCGEQABoMNjM3NDIzMTgzODA1IgxoZXH164GDLwgfrnMq3APRoRTZUVIAoT0wIrQrKGDeMIkLGZinGzlZ9LwhKQXuUpzMTSN8ye0C34tiiMLEn2hn7Ka%2Fnqgu78ouAktJcLZkW3gGT3CjRBq%2BwyhNpKn0sXr7Gl3JpDCO%2F%2BUnRSCOkVdHKyk%2FrHaZO%2F%2FIMk%2BLHs3I%2FXVoikwvT4hU4wJ9WznrRjNFt%2B6%2FjyuJoTMuVXvQ1YqGWcCWQvITAKa5eDWIGaDcc7hYYwT84njBaclpOW3wbNLJrmuc5qjzOaaCJEBjJhmzBvk9CGuaSVR9uVthiwC8KZIQEB%2B2jxxFr3lj977DxZpd2AqssdRbwoRmalWftRPIY%2Fv7WrYgy6cWQKLcQbLG8Ev946%2B0ixtkfKAMxg%2BIQ969QEYlWoTGkPfsofg%2FNE%2BEGz4eSkzUFV8Vt7i6QaUvRJna5ssff5EVAj2kwiSiVVH767OgnfKYNQzhmJKKh7ZWWLOij7ymudDX0p0y2i%2Fn70CkZpYJmN%2FSJIQhqlvVU9JFw0dX3CP3Vkp75%2BQjLVQo3SHNrQdvmGvUprcslCWD7Vfzo61dt6x1WZK5XUQezxnrAGTpUmDsRfFPtrwF6W36RZivHPN2mqw8sj3Pibv231N3Bl9nWBCE7P%2BS%2BoMnH6VDgwurja2RgyMm6zDyleXLBjqkAeYvJxoBQ7pM3QPVHS7q538XxbgSkDx39E7FWAo3DvhQf8H2JslqfLqrj3JrhDxKGUVatKFqWlD87RRVxyj49rzYPTKlUth215cgT6lmWtcRvaQeKMeUNqGksOtqHXjvde%2BQrVupAFX2o7bnBuYEJywwBoUwPMvAaxg7TPFApN3kg0DDM5gHv9DJE0d8nwSp8UlxMMhWMOaNZbzptSP%2FQQuJKI%2Bo&X-Amz-Signature=71611ca8d42f2712af6df46df85727b1bec9b8605381222fa027b50183810223&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QX6K5QCF%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8CLrzg7l6YhK6dycCxxgnfjjJ%2F7Myntp9ibDABCS8fgIhAJPcDUcOtd3YRkg3VxH4QZtBUNv8VTPCq8Va0jUm6lnGKv8DCGEQABoMNjM3NDIzMTgzODA1IgxoZXH164GDLwgfrnMq3APRoRTZUVIAoT0wIrQrKGDeMIkLGZinGzlZ9LwhKQXuUpzMTSN8ye0C34tiiMLEn2hn7Ka%2Fnqgu78ouAktJcLZkW3gGT3CjRBq%2BwyhNpKn0sXr7Gl3JpDCO%2F%2BUnRSCOkVdHKyk%2FrHaZO%2F%2FIMk%2BLHs3I%2FXVoikwvT4hU4wJ9WznrRjNFt%2B6%2FjyuJoTMuVXvQ1YqGWcCWQvITAKa5eDWIGaDcc7hYYwT84njBaclpOW3wbNLJrmuc5qjzOaaCJEBjJhmzBvk9CGuaSVR9uVthiwC8KZIQEB%2B2jxxFr3lj977DxZpd2AqssdRbwoRmalWftRPIY%2Fv7WrYgy6cWQKLcQbLG8Ev946%2B0ixtkfKAMxg%2BIQ969QEYlWoTGkPfsofg%2FNE%2BEGz4eSkzUFV8Vt7i6QaUvRJna5ssff5EVAj2kwiSiVVH767OgnfKYNQzhmJKKh7ZWWLOij7ymudDX0p0y2i%2Fn70CkZpYJmN%2FSJIQhqlvVU9JFw0dX3CP3Vkp75%2BQjLVQo3SHNrQdvmGvUprcslCWD7Vfzo61dt6x1WZK5XUQezxnrAGTpUmDsRfFPtrwF6W36RZivHPN2mqw8sj3Pibv231N3Bl9nWBCE7P%2BS%2BoMnH6VDgwurja2RgyMm6zDyleXLBjqkAeYvJxoBQ7pM3QPVHS7q538XxbgSkDx39E7FWAo3DvhQf8H2JslqfLqrj3JrhDxKGUVatKFqWlD87RRVxyj49rzYPTKlUth215cgT6lmWtcRvaQeKMeUNqGksOtqHXjvde%2BQrVupAFX2o7bnBuYEJywwBoUwPMvAaxg7TPFApN3kg0DDM5gHv9DJE0d8nwSp8UlxMMhWMOaNZbzptSP%2FQQuJKI%2Bo&X-Amz-Signature=ca75bacfe353662ba5cba28ac11d991eb3fdefeaa1be0ed75dd4c2ea35973392&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QX6K5QCF%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8CLrzg7l6YhK6dycCxxgnfjjJ%2F7Myntp9ibDABCS8fgIhAJPcDUcOtd3YRkg3VxH4QZtBUNv8VTPCq8Va0jUm6lnGKv8DCGEQABoMNjM3NDIzMTgzODA1IgxoZXH164GDLwgfrnMq3APRoRTZUVIAoT0wIrQrKGDeMIkLGZinGzlZ9LwhKQXuUpzMTSN8ye0C34tiiMLEn2hn7Ka%2Fnqgu78ouAktJcLZkW3gGT3CjRBq%2BwyhNpKn0sXr7Gl3JpDCO%2F%2BUnRSCOkVdHKyk%2FrHaZO%2F%2FIMk%2BLHs3I%2FXVoikwvT4hU4wJ9WznrRjNFt%2B6%2FjyuJoTMuVXvQ1YqGWcCWQvITAKa5eDWIGaDcc7hYYwT84njBaclpOW3wbNLJrmuc5qjzOaaCJEBjJhmzBvk9CGuaSVR9uVthiwC8KZIQEB%2B2jxxFr3lj977DxZpd2AqssdRbwoRmalWftRPIY%2Fv7WrYgy6cWQKLcQbLG8Ev946%2B0ixtkfKAMxg%2BIQ969QEYlWoTGkPfsofg%2FNE%2BEGz4eSkzUFV8Vt7i6QaUvRJna5ssff5EVAj2kwiSiVVH767OgnfKYNQzhmJKKh7ZWWLOij7ymudDX0p0y2i%2Fn70CkZpYJmN%2FSJIQhqlvVU9JFw0dX3CP3Vkp75%2BQjLVQo3SHNrQdvmGvUprcslCWD7Vfzo61dt6x1WZK5XUQezxnrAGTpUmDsRfFPtrwF6W36RZivHPN2mqw8sj3Pibv231N3Bl9nWBCE7P%2BS%2BoMnH6VDgwurja2RgyMm6zDyleXLBjqkAeYvJxoBQ7pM3QPVHS7q538XxbgSkDx39E7FWAo3DvhQf8H2JslqfLqrj3JrhDxKGUVatKFqWlD87RRVxyj49rzYPTKlUth215cgT6lmWtcRvaQeKMeUNqGksOtqHXjvde%2BQrVupAFX2o7bnBuYEJywwBoUwPMvAaxg7TPFApN3kg0DDM5gHv9DJE0d8nwSp8UlxMMhWMOaNZbzptSP%2FQQuJKI%2Bo&X-Amz-Signature=ec32472a24a8f768f40bdf5de3ded4a7ff5b5b71d0c826e2f84a9d60e44263ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

