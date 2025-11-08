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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUNMM5L4%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDx6XZzWtkHJ%2FwOJ7d8gnCPy5yQAo5Gh3HmiRjOO%2F8%2B4gIgHCJKSbkFobe9qMc2qiJiQzOKeu1eAq%2Fn6Fpv79HXX80qiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC92cSDarF8%2FCE8iISrcAwoDzrLRaGUZ5zb1xPqdsgmJa5KuuWxbGCoc%2Btk27GyCmhBKlMUnyfX0KUU3Fl5hMMIZtC%2BDudrS6br8BN0PO4rCAGXT4Sxvb0wuJ5KoBuMsHIuNgZsoA681WH%2F9rKm6V3CNGn468CzRRJVcjHiQdsZ9mU0BXmdcV6XhpSKyz3Qo8NaielViTGGYyKjv6DqBL929PLX%2Boed%2FqLrf%2FvMeiHMZtw7JHEtkpA2LTK63brBgxxy%2FDhvYHflDrapBeRVnAWTK68L94bU3uM5BnNkKiTXhKxcxoRluE54dD4TCsCc89JfN9RxtEhTvvQ%2FVM7IOhmoLD7RQGslP76ZdwDZockdMKw7pZfx6i3J2uLBpmXuQ6IUlohb8sRYp0w6rutaFdhoHv8OO0uOXABnXiyyi1ddMQvulbUAglJui7uYad4%2Bfc99WeVdW%2FlhoRvrU4eEyfb2Rky4yuefQkCf8bzAQSuGyLUzhRimCmIEf1XRNe9TDMRbZyRZpgcOW2GIWXtnIzPo6OhX%2FE7Vjw98sLv3yxG7T7i%2BeYsho79dCVl6nm4jZl4BTD7W%2FJ%2Bvpjc6sv0II1ilFWxedQ91%2Fo%2BKOuLOBpItDMHE99pdE3MbsFsigNQIVNhJ%2FIu3fbAzkLIXSMKHQusgGOqUBdv8U8352az7C%2F7FoA3xA5FQ3bmq1tnTw3cjd73rExrTgWnG1wfXaOaE0UlVS%2FLIZRiHuM9Tm1%2FP8lW5RaKbrPlFbbPO9YTXoZj%2F87sdFyXLsrHO%2BhRzS1b%2FiTMkYn1hqF8X74aRtYoaPtQl4hbIm0IJ8erxY7WmyR12Xi5zmkrIg0GurmMbcDeg8W%2FxAWlTl1DaCf0FHrBATK2vQZeSC1Ai3TwA9&X-Amz-Signature=c8807d162c490617297b71903d50843da4ffe9f6c884d1713883ceb83e456d79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUNMM5L4%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDx6XZzWtkHJ%2FwOJ7d8gnCPy5yQAo5Gh3HmiRjOO%2F8%2B4gIgHCJKSbkFobe9qMc2qiJiQzOKeu1eAq%2Fn6Fpv79HXX80qiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC92cSDarF8%2FCE8iISrcAwoDzrLRaGUZ5zb1xPqdsgmJa5KuuWxbGCoc%2Btk27GyCmhBKlMUnyfX0KUU3Fl5hMMIZtC%2BDudrS6br8BN0PO4rCAGXT4Sxvb0wuJ5KoBuMsHIuNgZsoA681WH%2F9rKm6V3CNGn468CzRRJVcjHiQdsZ9mU0BXmdcV6XhpSKyz3Qo8NaielViTGGYyKjv6DqBL929PLX%2Boed%2FqLrf%2FvMeiHMZtw7JHEtkpA2LTK63brBgxxy%2FDhvYHflDrapBeRVnAWTK68L94bU3uM5BnNkKiTXhKxcxoRluE54dD4TCsCc89JfN9RxtEhTvvQ%2FVM7IOhmoLD7RQGslP76ZdwDZockdMKw7pZfx6i3J2uLBpmXuQ6IUlohb8sRYp0w6rutaFdhoHv8OO0uOXABnXiyyi1ddMQvulbUAglJui7uYad4%2Bfc99WeVdW%2FlhoRvrU4eEyfb2Rky4yuefQkCf8bzAQSuGyLUzhRimCmIEf1XRNe9TDMRbZyRZpgcOW2GIWXtnIzPo6OhX%2FE7Vjw98sLv3yxG7T7i%2BeYsho79dCVl6nm4jZl4BTD7W%2FJ%2Bvpjc6sv0II1ilFWxedQ91%2Fo%2BKOuLOBpItDMHE99pdE3MbsFsigNQIVNhJ%2FIu3fbAzkLIXSMKHQusgGOqUBdv8U8352az7C%2F7FoA3xA5FQ3bmq1tnTw3cjd73rExrTgWnG1wfXaOaE0UlVS%2FLIZRiHuM9Tm1%2FP8lW5RaKbrPlFbbPO9YTXoZj%2F87sdFyXLsrHO%2BhRzS1b%2FiTMkYn1hqF8X74aRtYoaPtQl4hbIm0IJ8erxY7WmyR12Xi5zmkrIg0GurmMbcDeg8W%2FxAWlTl1DaCf0FHrBATK2vQZeSC1Ai3TwA9&X-Amz-Signature=b20a05acd0c99603e11f2e07f8ff549241b4ecb33d0469197872423a5c78a9b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUNMM5L4%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDx6XZzWtkHJ%2FwOJ7d8gnCPy5yQAo5Gh3HmiRjOO%2F8%2B4gIgHCJKSbkFobe9qMc2qiJiQzOKeu1eAq%2Fn6Fpv79HXX80qiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC92cSDarF8%2FCE8iISrcAwoDzrLRaGUZ5zb1xPqdsgmJa5KuuWxbGCoc%2Btk27GyCmhBKlMUnyfX0KUU3Fl5hMMIZtC%2BDudrS6br8BN0PO4rCAGXT4Sxvb0wuJ5KoBuMsHIuNgZsoA681WH%2F9rKm6V3CNGn468CzRRJVcjHiQdsZ9mU0BXmdcV6XhpSKyz3Qo8NaielViTGGYyKjv6DqBL929PLX%2Boed%2FqLrf%2FvMeiHMZtw7JHEtkpA2LTK63brBgxxy%2FDhvYHflDrapBeRVnAWTK68L94bU3uM5BnNkKiTXhKxcxoRluE54dD4TCsCc89JfN9RxtEhTvvQ%2FVM7IOhmoLD7RQGslP76ZdwDZockdMKw7pZfx6i3J2uLBpmXuQ6IUlohb8sRYp0w6rutaFdhoHv8OO0uOXABnXiyyi1ddMQvulbUAglJui7uYad4%2Bfc99WeVdW%2FlhoRvrU4eEyfb2Rky4yuefQkCf8bzAQSuGyLUzhRimCmIEf1XRNe9TDMRbZyRZpgcOW2GIWXtnIzPo6OhX%2FE7Vjw98sLv3yxG7T7i%2BeYsho79dCVl6nm4jZl4BTD7W%2FJ%2Bvpjc6sv0II1ilFWxedQ91%2Fo%2BKOuLOBpItDMHE99pdE3MbsFsigNQIVNhJ%2FIu3fbAzkLIXSMKHQusgGOqUBdv8U8352az7C%2F7FoA3xA5FQ3bmq1tnTw3cjd73rExrTgWnG1wfXaOaE0UlVS%2FLIZRiHuM9Tm1%2FP8lW5RaKbrPlFbbPO9YTXoZj%2F87sdFyXLsrHO%2BhRzS1b%2FiTMkYn1hqF8X74aRtYoaPtQl4hbIm0IJ8erxY7WmyR12Xi5zmkrIg0GurmMbcDeg8W%2FxAWlTl1DaCf0FHrBATK2vQZeSC1Ai3TwA9&X-Amz-Signature=c4010c4db01aa7cb182204642040c5dd1a81d670fb95415528c343247ab319d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUNMM5L4%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDx6XZzWtkHJ%2FwOJ7d8gnCPy5yQAo5Gh3HmiRjOO%2F8%2B4gIgHCJKSbkFobe9qMc2qiJiQzOKeu1eAq%2Fn6Fpv79HXX80qiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC92cSDarF8%2FCE8iISrcAwoDzrLRaGUZ5zb1xPqdsgmJa5KuuWxbGCoc%2Btk27GyCmhBKlMUnyfX0KUU3Fl5hMMIZtC%2BDudrS6br8BN0PO4rCAGXT4Sxvb0wuJ5KoBuMsHIuNgZsoA681WH%2F9rKm6V3CNGn468CzRRJVcjHiQdsZ9mU0BXmdcV6XhpSKyz3Qo8NaielViTGGYyKjv6DqBL929PLX%2Boed%2FqLrf%2FvMeiHMZtw7JHEtkpA2LTK63brBgxxy%2FDhvYHflDrapBeRVnAWTK68L94bU3uM5BnNkKiTXhKxcxoRluE54dD4TCsCc89JfN9RxtEhTvvQ%2FVM7IOhmoLD7RQGslP76ZdwDZockdMKw7pZfx6i3J2uLBpmXuQ6IUlohb8sRYp0w6rutaFdhoHv8OO0uOXABnXiyyi1ddMQvulbUAglJui7uYad4%2Bfc99WeVdW%2FlhoRvrU4eEyfb2Rky4yuefQkCf8bzAQSuGyLUzhRimCmIEf1XRNe9TDMRbZyRZpgcOW2GIWXtnIzPo6OhX%2FE7Vjw98sLv3yxG7T7i%2BeYsho79dCVl6nm4jZl4BTD7W%2FJ%2Bvpjc6sv0II1ilFWxedQ91%2Fo%2BKOuLOBpItDMHE99pdE3MbsFsigNQIVNhJ%2FIu3fbAzkLIXSMKHQusgGOqUBdv8U8352az7C%2F7FoA3xA5FQ3bmq1tnTw3cjd73rExrTgWnG1wfXaOaE0UlVS%2FLIZRiHuM9Tm1%2FP8lW5RaKbrPlFbbPO9YTXoZj%2F87sdFyXLsrHO%2BhRzS1b%2FiTMkYn1hqF8X74aRtYoaPtQl4hbIm0IJ8erxY7WmyR12Xi5zmkrIg0GurmMbcDeg8W%2FxAWlTl1DaCf0FHrBATK2vQZeSC1Ai3TwA9&X-Amz-Signature=29e53b5b15b0c33a179aa0a656525610de305925d8efb4ff2f519d2c99321ce3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUNMM5L4%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDx6XZzWtkHJ%2FwOJ7d8gnCPy5yQAo5Gh3HmiRjOO%2F8%2B4gIgHCJKSbkFobe9qMc2qiJiQzOKeu1eAq%2Fn6Fpv79HXX80qiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC92cSDarF8%2FCE8iISrcAwoDzrLRaGUZ5zb1xPqdsgmJa5KuuWxbGCoc%2Btk27GyCmhBKlMUnyfX0KUU3Fl5hMMIZtC%2BDudrS6br8BN0PO4rCAGXT4Sxvb0wuJ5KoBuMsHIuNgZsoA681WH%2F9rKm6V3CNGn468CzRRJVcjHiQdsZ9mU0BXmdcV6XhpSKyz3Qo8NaielViTGGYyKjv6DqBL929PLX%2Boed%2FqLrf%2FvMeiHMZtw7JHEtkpA2LTK63brBgxxy%2FDhvYHflDrapBeRVnAWTK68L94bU3uM5BnNkKiTXhKxcxoRluE54dD4TCsCc89JfN9RxtEhTvvQ%2FVM7IOhmoLD7RQGslP76ZdwDZockdMKw7pZfx6i3J2uLBpmXuQ6IUlohb8sRYp0w6rutaFdhoHv8OO0uOXABnXiyyi1ddMQvulbUAglJui7uYad4%2Bfc99WeVdW%2FlhoRvrU4eEyfb2Rky4yuefQkCf8bzAQSuGyLUzhRimCmIEf1XRNe9TDMRbZyRZpgcOW2GIWXtnIzPo6OhX%2FE7Vjw98sLv3yxG7T7i%2BeYsho79dCVl6nm4jZl4BTD7W%2FJ%2Bvpjc6sv0II1ilFWxedQ91%2Fo%2BKOuLOBpItDMHE99pdE3MbsFsigNQIVNhJ%2FIu3fbAzkLIXSMKHQusgGOqUBdv8U8352az7C%2F7FoA3xA5FQ3bmq1tnTw3cjd73rExrTgWnG1wfXaOaE0UlVS%2FLIZRiHuM9Tm1%2FP8lW5RaKbrPlFbbPO9YTXoZj%2F87sdFyXLsrHO%2BhRzS1b%2FiTMkYn1hqF8X74aRtYoaPtQl4hbIm0IJ8erxY7WmyR12Xi5zmkrIg0GurmMbcDeg8W%2FxAWlTl1DaCf0FHrBATK2vQZeSC1Ai3TwA9&X-Amz-Signature=41c8b542500c380f229ff77710823101a3223e893e875600b59aea6bda32ee8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUNMM5L4%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDx6XZzWtkHJ%2FwOJ7d8gnCPy5yQAo5Gh3HmiRjOO%2F8%2B4gIgHCJKSbkFobe9qMc2qiJiQzOKeu1eAq%2Fn6Fpv79HXX80qiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC92cSDarF8%2FCE8iISrcAwoDzrLRaGUZ5zb1xPqdsgmJa5KuuWxbGCoc%2Btk27GyCmhBKlMUnyfX0KUU3Fl5hMMIZtC%2BDudrS6br8BN0PO4rCAGXT4Sxvb0wuJ5KoBuMsHIuNgZsoA681WH%2F9rKm6V3CNGn468CzRRJVcjHiQdsZ9mU0BXmdcV6XhpSKyz3Qo8NaielViTGGYyKjv6DqBL929PLX%2Boed%2FqLrf%2FvMeiHMZtw7JHEtkpA2LTK63brBgxxy%2FDhvYHflDrapBeRVnAWTK68L94bU3uM5BnNkKiTXhKxcxoRluE54dD4TCsCc89JfN9RxtEhTvvQ%2FVM7IOhmoLD7RQGslP76ZdwDZockdMKw7pZfx6i3J2uLBpmXuQ6IUlohb8sRYp0w6rutaFdhoHv8OO0uOXABnXiyyi1ddMQvulbUAglJui7uYad4%2Bfc99WeVdW%2FlhoRvrU4eEyfb2Rky4yuefQkCf8bzAQSuGyLUzhRimCmIEf1XRNe9TDMRbZyRZpgcOW2GIWXtnIzPo6OhX%2FE7Vjw98sLv3yxG7T7i%2BeYsho79dCVl6nm4jZl4BTD7W%2FJ%2Bvpjc6sv0II1ilFWxedQ91%2Fo%2BKOuLOBpItDMHE99pdE3MbsFsigNQIVNhJ%2FIu3fbAzkLIXSMKHQusgGOqUBdv8U8352az7C%2F7FoA3xA5FQ3bmq1tnTw3cjd73rExrTgWnG1wfXaOaE0UlVS%2FLIZRiHuM9Tm1%2FP8lW5RaKbrPlFbbPO9YTXoZj%2F87sdFyXLsrHO%2BhRzS1b%2FiTMkYn1hqF8X74aRtYoaPtQl4hbIm0IJ8erxY7WmyR12Xi5zmkrIg0GurmMbcDeg8W%2FxAWlTl1DaCf0FHrBATK2vQZeSC1Ai3TwA9&X-Amz-Signature=dd4f99c1965b06ab903aa990108336f8d5cc70c60316d0f0075210e3f7ec3f7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUNMM5L4%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDx6XZzWtkHJ%2FwOJ7d8gnCPy5yQAo5Gh3HmiRjOO%2F8%2B4gIgHCJKSbkFobe9qMc2qiJiQzOKeu1eAq%2Fn6Fpv79HXX80qiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC92cSDarF8%2FCE8iISrcAwoDzrLRaGUZ5zb1xPqdsgmJa5KuuWxbGCoc%2Btk27GyCmhBKlMUnyfX0KUU3Fl5hMMIZtC%2BDudrS6br8BN0PO4rCAGXT4Sxvb0wuJ5KoBuMsHIuNgZsoA681WH%2F9rKm6V3CNGn468CzRRJVcjHiQdsZ9mU0BXmdcV6XhpSKyz3Qo8NaielViTGGYyKjv6DqBL929PLX%2Boed%2FqLrf%2FvMeiHMZtw7JHEtkpA2LTK63brBgxxy%2FDhvYHflDrapBeRVnAWTK68L94bU3uM5BnNkKiTXhKxcxoRluE54dD4TCsCc89JfN9RxtEhTvvQ%2FVM7IOhmoLD7RQGslP76ZdwDZockdMKw7pZfx6i3J2uLBpmXuQ6IUlohb8sRYp0w6rutaFdhoHv8OO0uOXABnXiyyi1ddMQvulbUAglJui7uYad4%2Bfc99WeVdW%2FlhoRvrU4eEyfb2Rky4yuefQkCf8bzAQSuGyLUzhRimCmIEf1XRNe9TDMRbZyRZpgcOW2GIWXtnIzPo6OhX%2FE7Vjw98sLv3yxG7T7i%2BeYsho79dCVl6nm4jZl4BTD7W%2FJ%2Bvpjc6sv0II1ilFWxedQ91%2Fo%2BKOuLOBpItDMHE99pdE3MbsFsigNQIVNhJ%2FIu3fbAzkLIXSMKHQusgGOqUBdv8U8352az7C%2F7FoA3xA5FQ3bmq1tnTw3cjd73rExrTgWnG1wfXaOaE0UlVS%2FLIZRiHuM9Tm1%2FP8lW5RaKbrPlFbbPO9YTXoZj%2F87sdFyXLsrHO%2BhRzS1b%2FiTMkYn1hqF8X74aRtYoaPtQl4hbIm0IJ8erxY7WmyR12Xi5zmkrIg0GurmMbcDeg8W%2FxAWlTl1DaCf0FHrBATK2vQZeSC1Ai3TwA9&X-Amz-Signature=e013c184874fadc58b658df37ef53842c21112935ec24b43e543d29a1ff5656b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

