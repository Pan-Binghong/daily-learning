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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTXIUFXV%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDPLB9x0uiEEXCexmlPJ3TC3ZXiu71KUE4%2F5Ol6Su9i0gIgBt5jZoz75jexf5NkJW4Dx8lEaFijIwzku58HV2SM9NcqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoahZZNYvZGhrO1ZyrcA3qxgjHCu1sNELl2QFZciOwAQn%2BgvceyCcfSxw%2BBaonnGWVyKNTq3miuqtapiRUtBa6ndwKmaP9x0oykZDRBQEJWtpXP%2FLGKsywYOA8MTK9EYdos%2F1K33xGb7tXPRB6R5ZOqM867%2BwaCbH%2FHRXe2ck4brSA1dHXgqchoKroOeL5YGqaIZV1LJXOhCt6EmdYpv8KzAKE6IKzAFcDb4g8RrHLYo2Nup08dGBaxLdE6VQLpoNHdp7gXsqDg9v7E5qn1VUl6slm7igUBGeMhnCPcngk%2FIOvaHOtFdIWRZ78CHMlIzZg2aKUxBijxxzHE4PuOBXwz82Oj4rQNDs5MRCx4pKR%2FAXdBMVOa6lzEXuyWf%2BF2QXN5Fo%2By44p61DFMkneHx3HNWN%2BEPJ2Qb8VAj%2BVjHn4aJVk%2FbeQo5OvmGul9NieIVvEg0PKtNeE%2FhJG5JBSq6nf4W4lqOdRnLaIa3%2Bse%2FJ9M8mj%2F9FVxgoX5ktAKW0hjPYcwCFv4APfndpxRRe%2BWdLMeZhfidy5vj3cNLEHJcfIDToE2qRpJCMyOlRqOizt%2FOZ%2BnTeaLbWGBTOvBJ72uDCOJo6%2Fzm77xWKqtsgewc1IdvT2NNMkXiWQ%2ByVdc6laqNchRSejhUjWHD630ML73sskGOqUBxx8WhnbT0jmFN%2F2bqGxR5%2BOXKK%2BabSdT8fNjgajFdevsSyYaWpaVWAby6gxZAWuu6%2F%2BGva5VqO1kUQwOvmYCEfRCS2ecaBvLMySftnQD8KHgC6q8EcHXCA9NttntqGOpK4TChgIWDKaqkPojzJgOAp1aeI9N2KjMS4BUbh3sIhLGInWpEYWOSfaICQeK9bnssNwcmEoHuV2lPdBBIUfKLUJaIaaB&X-Amz-Signature=9c36b91e833a64a8cb533faf1cca4fbed0924bcc48649a3538c8274c1d3fc946&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTXIUFXV%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDPLB9x0uiEEXCexmlPJ3TC3ZXiu71KUE4%2F5Ol6Su9i0gIgBt5jZoz75jexf5NkJW4Dx8lEaFijIwzku58HV2SM9NcqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoahZZNYvZGhrO1ZyrcA3qxgjHCu1sNELl2QFZciOwAQn%2BgvceyCcfSxw%2BBaonnGWVyKNTq3miuqtapiRUtBa6ndwKmaP9x0oykZDRBQEJWtpXP%2FLGKsywYOA8MTK9EYdos%2F1K33xGb7tXPRB6R5ZOqM867%2BwaCbH%2FHRXe2ck4brSA1dHXgqchoKroOeL5YGqaIZV1LJXOhCt6EmdYpv8KzAKE6IKzAFcDb4g8RrHLYo2Nup08dGBaxLdE6VQLpoNHdp7gXsqDg9v7E5qn1VUl6slm7igUBGeMhnCPcngk%2FIOvaHOtFdIWRZ78CHMlIzZg2aKUxBijxxzHE4PuOBXwz82Oj4rQNDs5MRCx4pKR%2FAXdBMVOa6lzEXuyWf%2BF2QXN5Fo%2By44p61DFMkneHx3HNWN%2BEPJ2Qb8VAj%2BVjHn4aJVk%2FbeQo5OvmGul9NieIVvEg0PKtNeE%2FhJG5JBSq6nf4W4lqOdRnLaIa3%2Bse%2FJ9M8mj%2F9FVxgoX5ktAKW0hjPYcwCFv4APfndpxRRe%2BWdLMeZhfidy5vj3cNLEHJcfIDToE2qRpJCMyOlRqOizt%2FOZ%2BnTeaLbWGBTOvBJ72uDCOJo6%2Fzm77xWKqtsgewc1IdvT2NNMkXiWQ%2ByVdc6laqNchRSejhUjWHD630ML73sskGOqUBxx8WhnbT0jmFN%2F2bqGxR5%2BOXKK%2BabSdT8fNjgajFdevsSyYaWpaVWAby6gxZAWuu6%2F%2BGva5VqO1kUQwOvmYCEfRCS2ecaBvLMySftnQD8KHgC6q8EcHXCA9NttntqGOpK4TChgIWDKaqkPojzJgOAp1aeI9N2KjMS4BUbh3sIhLGInWpEYWOSfaICQeK9bnssNwcmEoHuV2lPdBBIUfKLUJaIaaB&X-Amz-Signature=8bc08c706a9f8b362b7752cfeadcfc163174ed8c593b8772bee4b20bedce6875&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTXIUFXV%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDPLB9x0uiEEXCexmlPJ3TC3ZXiu71KUE4%2F5Ol6Su9i0gIgBt5jZoz75jexf5NkJW4Dx8lEaFijIwzku58HV2SM9NcqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoahZZNYvZGhrO1ZyrcA3qxgjHCu1sNELl2QFZciOwAQn%2BgvceyCcfSxw%2BBaonnGWVyKNTq3miuqtapiRUtBa6ndwKmaP9x0oykZDRBQEJWtpXP%2FLGKsywYOA8MTK9EYdos%2F1K33xGb7tXPRB6R5ZOqM867%2BwaCbH%2FHRXe2ck4brSA1dHXgqchoKroOeL5YGqaIZV1LJXOhCt6EmdYpv8KzAKE6IKzAFcDb4g8RrHLYo2Nup08dGBaxLdE6VQLpoNHdp7gXsqDg9v7E5qn1VUl6slm7igUBGeMhnCPcngk%2FIOvaHOtFdIWRZ78CHMlIzZg2aKUxBijxxzHE4PuOBXwz82Oj4rQNDs5MRCx4pKR%2FAXdBMVOa6lzEXuyWf%2BF2QXN5Fo%2By44p61DFMkneHx3HNWN%2BEPJ2Qb8VAj%2BVjHn4aJVk%2FbeQo5OvmGul9NieIVvEg0PKtNeE%2FhJG5JBSq6nf4W4lqOdRnLaIa3%2Bse%2FJ9M8mj%2F9FVxgoX5ktAKW0hjPYcwCFv4APfndpxRRe%2BWdLMeZhfidy5vj3cNLEHJcfIDToE2qRpJCMyOlRqOizt%2FOZ%2BnTeaLbWGBTOvBJ72uDCOJo6%2Fzm77xWKqtsgewc1IdvT2NNMkXiWQ%2ByVdc6laqNchRSejhUjWHD630ML73sskGOqUBxx8WhnbT0jmFN%2F2bqGxR5%2BOXKK%2BabSdT8fNjgajFdevsSyYaWpaVWAby6gxZAWuu6%2F%2BGva5VqO1kUQwOvmYCEfRCS2ecaBvLMySftnQD8KHgC6q8EcHXCA9NttntqGOpK4TChgIWDKaqkPojzJgOAp1aeI9N2KjMS4BUbh3sIhLGInWpEYWOSfaICQeK9bnssNwcmEoHuV2lPdBBIUfKLUJaIaaB&X-Amz-Signature=164f1155a4bb0175b3e34b299402fb4ee7f7ae003e1d470785ce7365b7999c7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTXIUFXV%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDPLB9x0uiEEXCexmlPJ3TC3ZXiu71KUE4%2F5Ol6Su9i0gIgBt5jZoz75jexf5NkJW4Dx8lEaFijIwzku58HV2SM9NcqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoahZZNYvZGhrO1ZyrcA3qxgjHCu1sNELl2QFZciOwAQn%2BgvceyCcfSxw%2BBaonnGWVyKNTq3miuqtapiRUtBa6ndwKmaP9x0oykZDRBQEJWtpXP%2FLGKsywYOA8MTK9EYdos%2F1K33xGb7tXPRB6R5ZOqM867%2BwaCbH%2FHRXe2ck4brSA1dHXgqchoKroOeL5YGqaIZV1LJXOhCt6EmdYpv8KzAKE6IKzAFcDb4g8RrHLYo2Nup08dGBaxLdE6VQLpoNHdp7gXsqDg9v7E5qn1VUl6slm7igUBGeMhnCPcngk%2FIOvaHOtFdIWRZ78CHMlIzZg2aKUxBijxxzHE4PuOBXwz82Oj4rQNDs5MRCx4pKR%2FAXdBMVOa6lzEXuyWf%2BF2QXN5Fo%2By44p61DFMkneHx3HNWN%2BEPJ2Qb8VAj%2BVjHn4aJVk%2FbeQo5OvmGul9NieIVvEg0PKtNeE%2FhJG5JBSq6nf4W4lqOdRnLaIa3%2Bse%2FJ9M8mj%2F9FVxgoX5ktAKW0hjPYcwCFv4APfndpxRRe%2BWdLMeZhfidy5vj3cNLEHJcfIDToE2qRpJCMyOlRqOizt%2FOZ%2BnTeaLbWGBTOvBJ72uDCOJo6%2Fzm77xWKqtsgewc1IdvT2NNMkXiWQ%2ByVdc6laqNchRSejhUjWHD630ML73sskGOqUBxx8WhnbT0jmFN%2F2bqGxR5%2BOXKK%2BabSdT8fNjgajFdevsSyYaWpaVWAby6gxZAWuu6%2F%2BGva5VqO1kUQwOvmYCEfRCS2ecaBvLMySftnQD8KHgC6q8EcHXCA9NttntqGOpK4TChgIWDKaqkPojzJgOAp1aeI9N2KjMS4BUbh3sIhLGInWpEYWOSfaICQeK9bnssNwcmEoHuV2lPdBBIUfKLUJaIaaB&X-Amz-Signature=537e2bbfa9b1269ef4cb426b52e03b5aed54dd3703fd3b52ba53bd9ad71c54bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTXIUFXV%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDPLB9x0uiEEXCexmlPJ3TC3ZXiu71KUE4%2F5Ol6Su9i0gIgBt5jZoz75jexf5NkJW4Dx8lEaFijIwzku58HV2SM9NcqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoahZZNYvZGhrO1ZyrcA3qxgjHCu1sNELl2QFZciOwAQn%2BgvceyCcfSxw%2BBaonnGWVyKNTq3miuqtapiRUtBa6ndwKmaP9x0oykZDRBQEJWtpXP%2FLGKsywYOA8MTK9EYdos%2F1K33xGb7tXPRB6R5ZOqM867%2BwaCbH%2FHRXe2ck4brSA1dHXgqchoKroOeL5YGqaIZV1LJXOhCt6EmdYpv8KzAKE6IKzAFcDb4g8RrHLYo2Nup08dGBaxLdE6VQLpoNHdp7gXsqDg9v7E5qn1VUl6slm7igUBGeMhnCPcngk%2FIOvaHOtFdIWRZ78CHMlIzZg2aKUxBijxxzHE4PuOBXwz82Oj4rQNDs5MRCx4pKR%2FAXdBMVOa6lzEXuyWf%2BF2QXN5Fo%2By44p61DFMkneHx3HNWN%2BEPJ2Qb8VAj%2BVjHn4aJVk%2FbeQo5OvmGul9NieIVvEg0PKtNeE%2FhJG5JBSq6nf4W4lqOdRnLaIa3%2Bse%2FJ9M8mj%2F9FVxgoX5ktAKW0hjPYcwCFv4APfndpxRRe%2BWdLMeZhfidy5vj3cNLEHJcfIDToE2qRpJCMyOlRqOizt%2FOZ%2BnTeaLbWGBTOvBJ72uDCOJo6%2Fzm77xWKqtsgewc1IdvT2NNMkXiWQ%2ByVdc6laqNchRSejhUjWHD630ML73sskGOqUBxx8WhnbT0jmFN%2F2bqGxR5%2BOXKK%2BabSdT8fNjgajFdevsSyYaWpaVWAby6gxZAWuu6%2F%2BGva5VqO1kUQwOvmYCEfRCS2ecaBvLMySftnQD8KHgC6q8EcHXCA9NttntqGOpK4TChgIWDKaqkPojzJgOAp1aeI9N2KjMS4BUbh3sIhLGInWpEYWOSfaICQeK9bnssNwcmEoHuV2lPdBBIUfKLUJaIaaB&X-Amz-Signature=5e6d5677c411a77b011376dca0e03c9ca3d9d640521795cdd38e7274eeeaea7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTXIUFXV%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDPLB9x0uiEEXCexmlPJ3TC3ZXiu71KUE4%2F5Ol6Su9i0gIgBt5jZoz75jexf5NkJW4Dx8lEaFijIwzku58HV2SM9NcqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoahZZNYvZGhrO1ZyrcA3qxgjHCu1sNELl2QFZciOwAQn%2BgvceyCcfSxw%2BBaonnGWVyKNTq3miuqtapiRUtBa6ndwKmaP9x0oykZDRBQEJWtpXP%2FLGKsywYOA8MTK9EYdos%2F1K33xGb7tXPRB6R5ZOqM867%2BwaCbH%2FHRXe2ck4brSA1dHXgqchoKroOeL5YGqaIZV1LJXOhCt6EmdYpv8KzAKE6IKzAFcDb4g8RrHLYo2Nup08dGBaxLdE6VQLpoNHdp7gXsqDg9v7E5qn1VUl6slm7igUBGeMhnCPcngk%2FIOvaHOtFdIWRZ78CHMlIzZg2aKUxBijxxzHE4PuOBXwz82Oj4rQNDs5MRCx4pKR%2FAXdBMVOa6lzEXuyWf%2BF2QXN5Fo%2By44p61DFMkneHx3HNWN%2BEPJ2Qb8VAj%2BVjHn4aJVk%2FbeQo5OvmGul9NieIVvEg0PKtNeE%2FhJG5JBSq6nf4W4lqOdRnLaIa3%2Bse%2FJ9M8mj%2F9FVxgoX5ktAKW0hjPYcwCFv4APfndpxRRe%2BWdLMeZhfidy5vj3cNLEHJcfIDToE2qRpJCMyOlRqOizt%2FOZ%2BnTeaLbWGBTOvBJ72uDCOJo6%2Fzm77xWKqtsgewc1IdvT2NNMkXiWQ%2ByVdc6laqNchRSejhUjWHD630ML73sskGOqUBxx8WhnbT0jmFN%2F2bqGxR5%2BOXKK%2BabSdT8fNjgajFdevsSyYaWpaVWAby6gxZAWuu6%2F%2BGva5VqO1kUQwOvmYCEfRCS2ecaBvLMySftnQD8KHgC6q8EcHXCA9NttntqGOpK4TChgIWDKaqkPojzJgOAp1aeI9N2KjMS4BUbh3sIhLGInWpEYWOSfaICQeK9bnssNwcmEoHuV2lPdBBIUfKLUJaIaaB&X-Amz-Signature=67dd92d0cef85cdb8f54e9b7db4538958c9f93722b9561ffb0ba391d68336672&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTXIUFXV%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDPLB9x0uiEEXCexmlPJ3TC3ZXiu71KUE4%2F5Ol6Su9i0gIgBt5jZoz75jexf5NkJW4Dx8lEaFijIwzku58HV2SM9NcqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoahZZNYvZGhrO1ZyrcA3qxgjHCu1sNELl2QFZciOwAQn%2BgvceyCcfSxw%2BBaonnGWVyKNTq3miuqtapiRUtBa6ndwKmaP9x0oykZDRBQEJWtpXP%2FLGKsywYOA8MTK9EYdos%2F1K33xGb7tXPRB6R5ZOqM867%2BwaCbH%2FHRXe2ck4brSA1dHXgqchoKroOeL5YGqaIZV1LJXOhCt6EmdYpv8KzAKE6IKzAFcDb4g8RrHLYo2Nup08dGBaxLdE6VQLpoNHdp7gXsqDg9v7E5qn1VUl6slm7igUBGeMhnCPcngk%2FIOvaHOtFdIWRZ78CHMlIzZg2aKUxBijxxzHE4PuOBXwz82Oj4rQNDs5MRCx4pKR%2FAXdBMVOa6lzEXuyWf%2BF2QXN5Fo%2By44p61DFMkneHx3HNWN%2BEPJ2Qb8VAj%2BVjHn4aJVk%2FbeQo5OvmGul9NieIVvEg0PKtNeE%2FhJG5JBSq6nf4W4lqOdRnLaIa3%2Bse%2FJ9M8mj%2F9FVxgoX5ktAKW0hjPYcwCFv4APfndpxRRe%2BWdLMeZhfidy5vj3cNLEHJcfIDToE2qRpJCMyOlRqOizt%2FOZ%2BnTeaLbWGBTOvBJ72uDCOJo6%2Fzm77xWKqtsgewc1IdvT2NNMkXiWQ%2ByVdc6laqNchRSejhUjWHD630ML73sskGOqUBxx8WhnbT0jmFN%2F2bqGxR5%2BOXKK%2BabSdT8fNjgajFdevsSyYaWpaVWAby6gxZAWuu6%2F%2BGva5VqO1kUQwOvmYCEfRCS2ecaBvLMySftnQD8KHgC6q8EcHXCA9NttntqGOpK4TChgIWDKaqkPojzJgOAp1aeI9N2KjMS4BUbh3sIhLGInWpEYWOSfaICQeK9bnssNwcmEoHuV2lPdBBIUfKLUJaIaaB&X-Amz-Signature=629201cfb565cbfde1cdc3d48b307d0d5d125cdb3fd3581e93e4bfd7ead4908e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

