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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YEBMFNZ%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCGSsADeZnMeKjM3EV%2F1qohm8scoe1OiTGjZWtjbbwplgIhAI%2BwECmPlYJVmpb8S8qPTbT5yGmJHG5bVoM%2BPjiSX7zYKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwxStLHgJ1Uts2z1dkq3AMlF3ep%2F7Uc8nDeYP8DR3Im0Og3oYRdjBiCjlp1yarJ7hww9ZRa5uHp90AUlw2LzE1f%2FJEIAvGzdJTW7bUka8gVbWmwSwQuoPKqadsW1j4exL8oghWN2wHDk20eMcbB19tpS3thWmnMAcEXwfzBkULcbzG%2FiswvulB0NKtyGHh%2BVxgCcwF%2FfBhhibabhWw757h8Ia%2BcIXOZdenPrO7WQ3hlTd4flLxjFS7ks9cJtGmkMv6tAKRVy5UH9%2B1x5YSuQBB%2F%2Bi1lOnR4hyWIsKFNTVGQ2JugoK%2FB0rukOsZhl4gHIK3xeFO7oxeDHSl45JJsNNlA%2FwS1uYprPEMl8ih%2FG8B7VmUH%2Bf6hS9hOJYWOss2EI0o44bRydVAf%2FTqnthGqyqM3%2BeeleGxel0T9prRE8Ju4h3AXf%2B8wTQ%2BU7C1oeyFu8YjT6T0dsd6ovWihsfyyEJlZWsXYo9uIEyY5s0fV7Qc58BIYo3lTjEmZs%2FvXBOCO9j7wC7l3JAgTu4p46PBH8AJLgwKXadMIcag6CsK2G9FX3B11CwMI29MpSxqS0PRyxm3sIFQRTdeTI8KEG4R2MsBoVQa6NMZvMJ2vzVam9VPLjVSHM1sK835W4uXi4q7I9txJv5G4RAW1pJP%2BujD2rYvPBjqkARVtQKitxpMBZV3tGaquiuHIGh%2FiE%2FvRcDo%2B2yic1gjCICSffvI%2Bx5bmm2ooEzpPppE9WS%2BFPEBkMFVWKfLVj7BGHFBmXAuF0YEWp8IoDRNyJXFAU%2FX1r0mUEZNaz6HzNvytzqWPRy6auFzMS6Ho4FwxcmPEu6VsFD%2Bt7Q6jZ7ZnS%2BgRaDnMyAjJZrpK7EKgAduBPEi4A8kmSSdHbXFhGaW8S62X&X-Amz-Signature=52395f3dd4f54574375582800d91dc2fcbd462f4b5310b2103b75f3287c77924&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YEBMFNZ%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCGSsADeZnMeKjM3EV%2F1qohm8scoe1OiTGjZWtjbbwplgIhAI%2BwECmPlYJVmpb8S8qPTbT5yGmJHG5bVoM%2BPjiSX7zYKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwxStLHgJ1Uts2z1dkq3AMlF3ep%2F7Uc8nDeYP8DR3Im0Og3oYRdjBiCjlp1yarJ7hww9ZRa5uHp90AUlw2LzE1f%2FJEIAvGzdJTW7bUka8gVbWmwSwQuoPKqadsW1j4exL8oghWN2wHDk20eMcbB19tpS3thWmnMAcEXwfzBkULcbzG%2FiswvulB0NKtyGHh%2BVxgCcwF%2FfBhhibabhWw757h8Ia%2BcIXOZdenPrO7WQ3hlTd4flLxjFS7ks9cJtGmkMv6tAKRVy5UH9%2B1x5YSuQBB%2F%2Bi1lOnR4hyWIsKFNTVGQ2JugoK%2FB0rukOsZhl4gHIK3xeFO7oxeDHSl45JJsNNlA%2FwS1uYprPEMl8ih%2FG8B7VmUH%2Bf6hS9hOJYWOss2EI0o44bRydVAf%2FTqnthGqyqM3%2BeeleGxel0T9prRE8Ju4h3AXf%2B8wTQ%2BU7C1oeyFu8YjT6T0dsd6ovWihsfyyEJlZWsXYo9uIEyY5s0fV7Qc58BIYo3lTjEmZs%2FvXBOCO9j7wC7l3JAgTu4p46PBH8AJLgwKXadMIcag6CsK2G9FX3B11CwMI29MpSxqS0PRyxm3sIFQRTdeTI8KEG4R2MsBoVQa6NMZvMJ2vzVam9VPLjVSHM1sK835W4uXi4q7I9txJv5G4RAW1pJP%2BujD2rYvPBjqkARVtQKitxpMBZV3tGaquiuHIGh%2FiE%2FvRcDo%2B2yic1gjCICSffvI%2Bx5bmm2ooEzpPppE9WS%2BFPEBkMFVWKfLVj7BGHFBmXAuF0YEWp8IoDRNyJXFAU%2FX1r0mUEZNaz6HzNvytzqWPRy6auFzMS6Ho4FwxcmPEu6VsFD%2Bt7Q6jZ7ZnS%2BgRaDnMyAjJZrpK7EKgAduBPEi4A8kmSSdHbXFhGaW8S62X&X-Amz-Signature=05ffe754792a7a9f9cdf272bef2301563761cdebf1613ef1585231caf1d51d2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YEBMFNZ%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCGSsADeZnMeKjM3EV%2F1qohm8scoe1OiTGjZWtjbbwplgIhAI%2BwECmPlYJVmpb8S8qPTbT5yGmJHG5bVoM%2BPjiSX7zYKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwxStLHgJ1Uts2z1dkq3AMlF3ep%2F7Uc8nDeYP8DR3Im0Og3oYRdjBiCjlp1yarJ7hww9ZRa5uHp90AUlw2LzE1f%2FJEIAvGzdJTW7bUka8gVbWmwSwQuoPKqadsW1j4exL8oghWN2wHDk20eMcbB19tpS3thWmnMAcEXwfzBkULcbzG%2FiswvulB0NKtyGHh%2BVxgCcwF%2FfBhhibabhWw757h8Ia%2BcIXOZdenPrO7WQ3hlTd4flLxjFS7ks9cJtGmkMv6tAKRVy5UH9%2B1x5YSuQBB%2F%2Bi1lOnR4hyWIsKFNTVGQ2JugoK%2FB0rukOsZhl4gHIK3xeFO7oxeDHSl45JJsNNlA%2FwS1uYprPEMl8ih%2FG8B7VmUH%2Bf6hS9hOJYWOss2EI0o44bRydVAf%2FTqnthGqyqM3%2BeeleGxel0T9prRE8Ju4h3AXf%2B8wTQ%2BU7C1oeyFu8YjT6T0dsd6ovWihsfyyEJlZWsXYo9uIEyY5s0fV7Qc58BIYo3lTjEmZs%2FvXBOCO9j7wC7l3JAgTu4p46PBH8AJLgwKXadMIcag6CsK2G9FX3B11CwMI29MpSxqS0PRyxm3sIFQRTdeTI8KEG4R2MsBoVQa6NMZvMJ2vzVam9VPLjVSHM1sK835W4uXi4q7I9txJv5G4RAW1pJP%2BujD2rYvPBjqkARVtQKitxpMBZV3tGaquiuHIGh%2FiE%2FvRcDo%2B2yic1gjCICSffvI%2Bx5bmm2ooEzpPppE9WS%2BFPEBkMFVWKfLVj7BGHFBmXAuF0YEWp8IoDRNyJXFAU%2FX1r0mUEZNaz6HzNvytzqWPRy6auFzMS6Ho4FwxcmPEu6VsFD%2Bt7Q6jZ7ZnS%2BgRaDnMyAjJZrpK7EKgAduBPEi4A8kmSSdHbXFhGaW8S62X&X-Amz-Signature=beeba2bd4bc9d46ec95e89eaed5f4e2fc14c87de01aa7fc5e33b2a1f302c84da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YEBMFNZ%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCGSsADeZnMeKjM3EV%2F1qohm8scoe1OiTGjZWtjbbwplgIhAI%2BwECmPlYJVmpb8S8qPTbT5yGmJHG5bVoM%2BPjiSX7zYKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwxStLHgJ1Uts2z1dkq3AMlF3ep%2F7Uc8nDeYP8DR3Im0Og3oYRdjBiCjlp1yarJ7hww9ZRa5uHp90AUlw2LzE1f%2FJEIAvGzdJTW7bUka8gVbWmwSwQuoPKqadsW1j4exL8oghWN2wHDk20eMcbB19tpS3thWmnMAcEXwfzBkULcbzG%2FiswvulB0NKtyGHh%2BVxgCcwF%2FfBhhibabhWw757h8Ia%2BcIXOZdenPrO7WQ3hlTd4flLxjFS7ks9cJtGmkMv6tAKRVy5UH9%2B1x5YSuQBB%2F%2Bi1lOnR4hyWIsKFNTVGQ2JugoK%2FB0rukOsZhl4gHIK3xeFO7oxeDHSl45JJsNNlA%2FwS1uYprPEMl8ih%2FG8B7VmUH%2Bf6hS9hOJYWOss2EI0o44bRydVAf%2FTqnthGqyqM3%2BeeleGxel0T9prRE8Ju4h3AXf%2B8wTQ%2BU7C1oeyFu8YjT6T0dsd6ovWihsfyyEJlZWsXYo9uIEyY5s0fV7Qc58BIYo3lTjEmZs%2FvXBOCO9j7wC7l3JAgTu4p46PBH8AJLgwKXadMIcag6CsK2G9FX3B11CwMI29MpSxqS0PRyxm3sIFQRTdeTI8KEG4R2MsBoVQa6NMZvMJ2vzVam9VPLjVSHM1sK835W4uXi4q7I9txJv5G4RAW1pJP%2BujD2rYvPBjqkARVtQKitxpMBZV3tGaquiuHIGh%2FiE%2FvRcDo%2B2yic1gjCICSffvI%2Bx5bmm2ooEzpPppE9WS%2BFPEBkMFVWKfLVj7BGHFBmXAuF0YEWp8IoDRNyJXFAU%2FX1r0mUEZNaz6HzNvytzqWPRy6auFzMS6Ho4FwxcmPEu6VsFD%2Bt7Q6jZ7ZnS%2BgRaDnMyAjJZrpK7EKgAduBPEi4A8kmSSdHbXFhGaW8S62X&X-Amz-Signature=206ea606afb4145dbc8be1f3dfc9f34e77ddbf6e94bd81f9b152ce954cf694b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YEBMFNZ%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCGSsADeZnMeKjM3EV%2F1qohm8scoe1OiTGjZWtjbbwplgIhAI%2BwECmPlYJVmpb8S8qPTbT5yGmJHG5bVoM%2BPjiSX7zYKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwxStLHgJ1Uts2z1dkq3AMlF3ep%2F7Uc8nDeYP8DR3Im0Og3oYRdjBiCjlp1yarJ7hww9ZRa5uHp90AUlw2LzE1f%2FJEIAvGzdJTW7bUka8gVbWmwSwQuoPKqadsW1j4exL8oghWN2wHDk20eMcbB19tpS3thWmnMAcEXwfzBkULcbzG%2FiswvulB0NKtyGHh%2BVxgCcwF%2FfBhhibabhWw757h8Ia%2BcIXOZdenPrO7WQ3hlTd4flLxjFS7ks9cJtGmkMv6tAKRVy5UH9%2B1x5YSuQBB%2F%2Bi1lOnR4hyWIsKFNTVGQ2JugoK%2FB0rukOsZhl4gHIK3xeFO7oxeDHSl45JJsNNlA%2FwS1uYprPEMl8ih%2FG8B7VmUH%2Bf6hS9hOJYWOss2EI0o44bRydVAf%2FTqnthGqyqM3%2BeeleGxel0T9prRE8Ju4h3AXf%2B8wTQ%2BU7C1oeyFu8YjT6T0dsd6ovWihsfyyEJlZWsXYo9uIEyY5s0fV7Qc58BIYo3lTjEmZs%2FvXBOCO9j7wC7l3JAgTu4p46PBH8AJLgwKXadMIcag6CsK2G9FX3B11CwMI29MpSxqS0PRyxm3sIFQRTdeTI8KEG4R2MsBoVQa6NMZvMJ2vzVam9VPLjVSHM1sK835W4uXi4q7I9txJv5G4RAW1pJP%2BujD2rYvPBjqkARVtQKitxpMBZV3tGaquiuHIGh%2FiE%2FvRcDo%2B2yic1gjCICSffvI%2Bx5bmm2ooEzpPppE9WS%2BFPEBkMFVWKfLVj7BGHFBmXAuF0YEWp8IoDRNyJXFAU%2FX1r0mUEZNaz6HzNvytzqWPRy6auFzMS6Ho4FwxcmPEu6VsFD%2Bt7Q6jZ7ZnS%2BgRaDnMyAjJZrpK7EKgAduBPEi4A8kmSSdHbXFhGaW8S62X&X-Amz-Signature=45cdf713581bef10aa6f0c05f1f452aafebca5281fce7d818f8ab9d90ddc4f05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YEBMFNZ%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCGSsADeZnMeKjM3EV%2F1qohm8scoe1OiTGjZWtjbbwplgIhAI%2BwECmPlYJVmpb8S8qPTbT5yGmJHG5bVoM%2BPjiSX7zYKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwxStLHgJ1Uts2z1dkq3AMlF3ep%2F7Uc8nDeYP8DR3Im0Og3oYRdjBiCjlp1yarJ7hww9ZRa5uHp90AUlw2LzE1f%2FJEIAvGzdJTW7bUka8gVbWmwSwQuoPKqadsW1j4exL8oghWN2wHDk20eMcbB19tpS3thWmnMAcEXwfzBkULcbzG%2FiswvulB0NKtyGHh%2BVxgCcwF%2FfBhhibabhWw757h8Ia%2BcIXOZdenPrO7WQ3hlTd4flLxjFS7ks9cJtGmkMv6tAKRVy5UH9%2B1x5YSuQBB%2F%2Bi1lOnR4hyWIsKFNTVGQ2JugoK%2FB0rukOsZhl4gHIK3xeFO7oxeDHSl45JJsNNlA%2FwS1uYprPEMl8ih%2FG8B7VmUH%2Bf6hS9hOJYWOss2EI0o44bRydVAf%2FTqnthGqyqM3%2BeeleGxel0T9prRE8Ju4h3AXf%2B8wTQ%2BU7C1oeyFu8YjT6T0dsd6ovWihsfyyEJlZWsXYo9uIEyY5s0fV7Qc58BIYo3lTjEmZs%2FvXBOCO9j7wC7l3JAgTu4p46PBH8AJLgwKXadMIcag6CsK2G9FX3B11CwMI29MpSxqS0PRyxm3sIFQRTdeTI8KEG4R2MsBoVQa6NMZvMJ2vzVam9VPLjVSHM1sK835W4uXi4q7I9txJv5G4RAW1pJP%2BujD2rYvPBjqkARVtQKitxpMBZV3tGaquiuHIGh%2FiE%2FvRcDo%2B2yic1gjCICSffvI%2Bx5bmm2ooEzpPppE9WS%2BFPEBkMFVWKfLVj7BGHFBmXAuF0YEWp8IoDRNyJXFAU%2FX1r0mUEZNaz6HzNvytzqWPRy6auFzMS6Ho4FwxcmPEu6VsFD%2Bt7Q6jZ7ZnS%2BgRaDnMyAjJZrpK7EKgAduBPEi4A8kmSSdHbXFhGaW8S62X&X-Amz-Signature=73c4715c1cd22d88c5754fcbc23d6151fcc1976d719131749ff5059935a981bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YEBMFNZ%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCGSsADeZnMeKjM3EV%2F1qohm8scoe1OiTGjZWtjbbwplgIhAI%2BwECmPlYJVmpb8S8qPTbT5yGmJHG5bVoM%2BPjiSX7zYKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwxStLHgJ1Uts2z1dkq3AMlF3ep%2F7Uc8nDeYP8DR3Im0Og3oYRdjBiCjlp1yarJ7hww9ZRa5uHp90AUlw2LzE1f%2FJEIAvGzdJTW7bUka8gVbWmwSwQuoPKqadsW1j4exL8oghWN2wHDk20eMcbB19tpS3thWmnMAcEXwfzBkULcbzG%2FiswvulB0NKtyGHh%2BVxgCcwF%2FfBhhibabhWw757h8Ia%2BcIXOZdenPrO7WQ3hlTd4flLxjFS7ks9cJtGmkMv6tAKRVy5UH9%2B1x5YSuQBB%2F%2Bi1lOnR4hyWIsKFNTVGQ2JugoK%2FB0rukOsZhl4gHIK3xeFO7oxeDHSl45JJsNNlA%2FwS1uYprPEMl8ih%2FG8B7VmUH%2Bf6hS9hOJYWOss2EI0o44bRydVAf%2FTqnthGqyqM3%2BeeleGxel0T9prRE8Ju4h3AXf%2B8wTQ%2BU7C1oeyFu8YjT6T0dsd6ovWihsfyyEJlZWsXYo9uIEyY5s0fV7Qc58BIYo3lTjEmZs%2FvXBOCO9j7wC7l3JAgTu4p46PBH8AJLgwKXadMIcag6CsK2G9FX3B11CwMI29MpSxqS0PRyxm3sIFQRTdeTI8KEG4R2MsBoVQa6NMZvMJ2vzVam9VPLjVSHM1sK835W4uXi4q7I9txJv5G4RAW1pJP%2BujD2rYvPBjqkARVtQKitxpMBZV3tGaquiuHIGh%2FiE%2FvRcDo%2B2yic1gjCICSffvI%2Bx5bmm2ooEzpPppE9WS%2BFPEBkMFVWKfLVj7BGHFBmXAuF0YEWp8IoDRNyJXFAU%2FX1r0mUEZNaz6HzNvytzqWPRy6auFzMS6Ho4FwxcmPEu6VsFD%2Bt7Q6jZ7ZnS%2BgRaDnMyAjJZrpK7EKgAduBPEi4A8kmSSdHbXFhGaW8S62X&X-Amz-Signature=3a8141f8fd3b0f78a2f47d15b4ea1d8583f87e770caa9bdd0a86a945a18ea308&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

