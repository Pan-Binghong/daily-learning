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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656PM6IV4%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH90IFcfPlBV62%2F5OVk2bPxIQcJKoOWt8wnp1pH8Sk0iAiAgbKHt6YDkCOYfvJE9D3%2FnaH%2F7sv1NtizslHo4WucBUCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLgeyHe%2FDh%2FDAl09IKtwDRdSPmskSQ1yrHp6Mx8veYcUJ7eM7Qj9hkqXdqgp%2FWvzvIWCzyIveu%2Byt9k5dHHl6qSgUumov6U0TjJhQVC5m6yrxqDdyKo2%2FuUiklswUtrNz3hFiO9G%2B%2FD2YCH7FuV%2FLhPxEFm8gxCMuRzl0zZCh%2BFJfotYqTW80Z4z3ituYkSoNKPvRCfMv4nHFNM5sH7emXWUSUPFjayqKG8ouJbEO6UXAKO%2BzRk7l42uiv%2B3Ve0JLw3q20FjhtVquW9CI6fMDTovGn4ePQH9WZN9sU%2FOtBJIMx7GBBx2Dm7%2FGKxRioFFLrRm4WPdTZ7PPFvFUQSj4MnquTr27z3Qo90zvIm52LYeBUen9bIHfH1Cu6UzTnAsbDoJRoQgqHnEXA18xL0KGAUe0H4EYRnepa8etMIkyY2Ekgm%2F8ut9LvOmHBwxG8o4jQhgirmu1pqn%2BkEObygd6neGmlM6YDDsti5vg7Em%2Bz%2BGaYY3SyH8%2Bmr6OT7IiCtCP0we4aiNVuSSu7za1XCGMWoVVyMCgGmHhKX2IV33Bq5nKarlR7tvv2shxCLvdjDm1i5payWze%2BGq9tykmxB8Mf7kirPFPlxi%2BkzR6CS1lmBKyBPBSiHQaViRkVAKdDfybIiYBDU41xq1Jnvkws%2FKvyAY6pgHqLivEmN3NKOZW091uNvy3mu5mZ0ZKbNSQTpHuc8g4xiZdCKjC%2BeXWd2OGAcjX6jlansQ1VoVTOIwOrA99IOerDCBFXa3p8NR0B%2FpzsFxjZKXzgtrGoiavhOMPNQ%2B2gCmBjBwg%2FSsAW%2Fab%2FqKdg%2B6HCvGGFRXTKlOtwri%2BiZV5deZiuXiTd9GPyTfYdtRe%2B4t01R2fGrtj1dPGiUsRR4eJgMHw2xLv&X-Amz-Signature=8ff4bccd248149ebce03b7a986c5fc47deba2916d9e13f5917c4f058a44a587c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656PM6IV4%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH90IFcfPlBV62%2F5OVk2bPxIQcJKoOWt8wnp1pH8Sk0iAiAgbKHt6YDkCOYfvJE9D3%2FnaH%2F7sv1NtizslHo4WucBUCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLgeyHe%2FDh%2FDAl09IKtwDRdSPmskSQ1yrHp6Mx8veYcUJ7eM7Qj9hkqXdqgp%2FWvzvIWCzyIveu%2Byt9k5dHHl6qSgUumov6U0TjJhQVC5m6yrxqDdyKo2%2FuUiklswUtrNz3hFiO9G%2B%2FD2YCH7FuV%2FLhPxEFm8gxCMuRzl0zZCh%2BFJfotYqTW80Z4z3ituYkSoNKPvRCfMv4nHFNM5sH7emXWUSUPFjayqKG8ouJbEO6UXAKO%2BzRk7l42uiv%2B3Ve0JLw3q20FjhtVquW9CI6fMDTovGn4ePQH9WZN9sU%2FOtBJIMx7GBBx2Dm7%2FGKxRioFFLrRm4WPdTZ7PPFvFUQSj4MnquTr27z3Qo90zvIm52LYeBUen9bIHfH1Cu6UzTnAsbDoJRoQgqHnEXA18xL0KGAUe0H4EYRnepa8etMIkyY2Ekgm%2F8ut9LvOmHBwxG8o4jQhgirmu1pqn%2BkEObygd6neGmlM6YDDsti5vg7Em%2Bz%2BGaYY3SyH8%2Bmr6OT7IiCtCP0we4aiNVuSSu7za1XCGMWoVVyMCgGmHhKX2IV33Bq5nKarlR7tvv2shxCLvdjDm1i5payWze%2BGq9tykmxB8Mf7kirPFPlxi%2BkzR6CS1lmBKyBPBSiHQaViRkVAKdDfybIiYBDU41xq1Jnvkws%2FKvyAY6pgHqLivEmN3NKOZW091uNvy3mu5mZ0ZKbNSQTpHuc8g4xiZdCKjC%2BeXWd2OGAcjX6jlansQ1VoVTOIwOrA99IOerDCBFXa3p8NR0B%2FpzsFxjZKXzgtrGoiavhOMPNQ%2B2gCmBjBwg%2FSsAW%2Fab%2FqKdg%2B6HCvGGFRXTKlOtwri%2BiZV5deZiuXiTd9GPyTfYdtRe%2B4t01R2fGrtj1dPGiUsRR4eJgMHw2xLv&X-Amz-Signature=d8c6cbfe2c955dd956ade1231b8efd755a9ffd5dd5957204f047d26a75d49abf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656PM6IV4%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH90IFcfPlBV62%2F5OVk2bPxIQcJKoOWt8wnp1pH8Sk0iAiAgbKHt6YDkCOYfvJE9D3%2FnaH%2F7sv1NtizslHo4WucBUCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLgeyHe%2FDh%2FDAl09IKtwDRdSPmskSQ1yrHp6Mx8veYcUJ7eM7Qj9hkqXdqgp%2FWvzvIWCzyIveu%2Byt9k5dHHl6qSgUumov6U0TjJhQVC5m6yrxqDdyKo2%2FuUiklswUtrNz3hFiO9G%2B%2FD2YCH7FuV%2FLhPxEFm8gxCMuRzl0zZCh%2BFJfotYqTW80Z4z3ituYkSoNKPvRCfMv4nHFNM5sH7emXWUSUPFjayqKG8ouJbEO6UXAKO%2BzRk7l42uiv%2B3Ve0JLw3q20FjhtVquW9CI6fMDTovGn4ePQH9WZN9sU%2FOtBJIMx7GBBx2Dm7%2FGKxRioFFLrRm4WPdTZ7PPFvFUQSj4MnquTr27z3Qo90zvIm52LYeBUen9bIHfH1Cu6UzTnAsbDoJRoQgqHnEXA18xL0KGAUe0H4EYRnepa8etMIkyY2Ekgm%2F8ut9LvOmHBwxG8o4jQhgirmu1pqn%2BkEObygd6neGmlM6YDDsti5vg7Em%2Bz%2BGaYY3SyH8%2Bmr6OT7IiCtCP0we4aiNVuSSu7za1XCGMWoVVyMCgGmHhKX2IV33Bq5nKarlR7tvv2shxCLvdjDm1i5payWze%2BGq9tykmxB8Mf7kirPFPlxi%2BkzR6CS1lmBKyBPBSiHQaViRkVAKdDfybIiYBDU41xq1Jnvkws%2FKvyAY6pgHqLivEmN3NKOZW091uNvy3mu5mZ0ZKbNSQTpHuc8g4xiZdCKjC%2BeXWd2OGAcjX6jlansQ1VoVTOIwOrA99IOerDCBFXa3p8NR0B%2FpzsFxjZKXzgtrGoiavhOMPNQ%2B2gCmBjBwg%2FSsAW%2Fab%2FqKdg%2B6HCvGGFRXTKlOtwri%2BiZV5deZiuXiTd9GPyTfYdtRe%2B4t01R2fGrtj1dPGiUsRR4eJgMHw2xLv&X-Amz-Signature=6835edbc2b8538f2450d053a61fb8cf7a9b1dd54e4626ae1e7af10aa4da41b24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656PM6IV4%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH90IFcfPlBV62%2F5OVk2bPxIQcJKoOWt8wnp1pH8Sk0iAiAgbKHt6YDkCOYfvJE9D3%2FnaH%2F7sv1NtizslHo4WucBUCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLgeyHe%2FDh%2FDAl09IKtwDRdSPmskSQ1yrHp6Mx8veYcUJ7eM7Qj9hkqXdqgp%2FWvzvIWCzyIveu%2Byt9k5dHHl6qSgUumov6U0TjJhQVC5m6yrxqDdyKo2%2FuUiklswUtrNz3hFiO9G%2B%2FD2YCH7FuV%2FLhPxEFm8gxCMuRzl0zZCh%2BFJfotYqTW80Z4z3ituYkSoNKPvRCfMv4nHFNM5sH7emXWUSUPFjayqKG8ouJbEO6UXAKO%2BzRk7l42uiv%2B3Ve0JLw3q20FjhtVquW9CI6fMDTovGn4ePQH9WZN9sU%2FOtBJIMx7GBBx2Dm7%2FGKxRioFFLrRm4WPdTZ7PPFvFUQSj4MnquTr27z3Qo90zvIm52LYeBUen9bIHfH1Cu6UzTnAsbDoJRoQgqHnEXA18xL0KGAUe0H4EYRnepa8etMIkyY2Ekgm%2F8ut9LvOmHBwxG8o4jQhgirmu1pqn%2BkEObygd6neGmlM6YDDsti5vg7Em%2Bz%2BGaYY3SyH8%2Bmr6OT7IiCtCP0we4aiNVuSSu7za1XCGMWoVVyMCgGmHhKX2IV33Bq5nKarlR7tvv2shxCLvdjDm1i5payWze%2BGq9tykmxB8Mf7kirPFPlxi%2BkzR6CS1lmBKyBPBSiHQaViRkVAKdDfybIiYBDU41xq1Jnvkws%2FKvyAY6pgHqLivEmN3NKOZW091uNvy3mu5mZ0ZKbNSQTpHuc8g4xiZdCKjC%2BeXWd2OGAcjX6jlansQ1VoVTOIwOrA99IOerDCBFXa3p8NR0B%2FpzsFxjZKXzgtrGoiavhOMPNQ%2B2gCmBjBwg%2FSsAW%2Fab%2FqKdg%2B6HCvGGFRXTKlOtwri%2BiZV5deZiuXiTd9GPyTfYdtRe%2B4t01R2fGrtj1dPGiUsRR4eJgMHw2xLv&X-Amz-Signature=35980c4f0dfc959fcd6e4a347cd4979e835f15a871cdce91d48cb7426407d703&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656PM6IV4%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH90IFcfPlBV62%2F5OVk2bPxIQcJKoOWt8wnp1pH8Sk0iAiAgbKHt6YDkCOYfvJE9D3%2FnaH%2F7sv1NtizslHo4WucBUCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLgeyHe%2FDh%2FDAl09IKtwDRdSPmskSQ1yrHp6Mx8veYcUJ7eM7Qj9hkqXdqgp%2FWvzvIWCzyIveu%2Byt9k5dHHl6qSgUumov6U0TjJhQVC5m6yrxqDdyKo2%2FuUiklswUtrNz3hFiO9G%2B%2FD2YCH7FuV%2FLhPxEFm8gxCMuRzl0zZCh%2BFJfotYqTW80Z4z3ituYkSoNKPvRCfMv4nHFNM5sH7emXWUSUPFjayqKG8ouJbEO6UXAKO%2BzRk7l42uiv%2B3Ve0JLw3q20FjhtVquW9CI6fMDTovGn4ePQH9WZN9sU%2FOtBJIMx7GBBx2Dm7%2FGKxRioFFLrRm4WPdTZ7PPFvFUQSj4MnquTr27z3Qo90zvIm52LYeBUen9bIHfH1Cu6UzTnAsbDoJRoQgqHnEXA18xL0KGAUe0H4EYRnepa8etMIkyY2Ekgm%2F8ut9LvOmHBwxG8o4jQhgirmu1pqn%2BkEObygd6neGmlM6YDDsti5vg7Em%2Bz%2BGaYY3SyH8%2Bmr6OT7IiCtCP0we4aiNVuSSu7za1XCGMWoVVyMCgGmHhKX2IV33Bq5nKarlR7tvv2shxCLvdjDm1i5payWze%2BGq9tykmxB8Mf7kirPFPlxi%2BkzR6CS1lmBKyBPBSiHQaViRkVAKdDfybIiYBDU41xq1Jnvkws%2FKvyAY6pgHqLivEmN3NKOZW091uNvy3mu5mZ0ZKbNSQTpHuc8g4xiZdCKjC%2BeXWd2OGAcjX6jlansQ1VoVTOIwOrA99IOerDCBFXa3p8NR0B%2FpzsFxjZKXzgtrGoiavhOMPNQ%2B2gCmBjBwg%2FSsAW%2Fab%2FqKdg%2B6HCvGGFRXTKlOtwri%2BiZV5deZiuXiTd9GPyTfYdtRe%2B4t01R2fGrtj1dPGiUsRR4eJgMHw2xLv&X-Amz-Signature=ed54b237b5c154f21bf1a6e7e32cf37ad6bf505219b180efbc8ef711d5d9aa23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656PM6IV4%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH90IFcfPlBV62%2F5OVk2bPxIQcJKoOWt8wnp1pH8Sk0iAiAgbKHt6YDkCOYfvJE9D3%2FnaH%2F7sv1NtizslHo4WucBUCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLgeyHe%2FDh%2FDAl09IKtwDRdSPmskSQ1yrHp6Mx8veYcUJ7eM7Qj9hkqXdqgp%2FWvzvIWCzyIveu%2Byt9k5dHHl6qSgUumov6U0TjJhQVC5m6yrxqDdyKo2%2FuUiklswUtrNz3hFiO9G%2B%2FD2YCH7FuV%2FLhPxEFm8gxCMuRzl0zZCh%2BFJfotYqTW80Z4z3ituYkSoNKPvRCfMv4nHFNM5sH7emXWUSUPFjayqKG8ouJbEO6UXAKO%2BzRk7l42uiv%2B3Ve0JLw3q20FjhtVquW9CI6fMDTovGn4ePQH9WZN9sU%2FOtBJIMx7GBBx2Dm7%2FGKxRioFFLrRm4WPdTZ7PPFvFUQSj4MnquTr27z3Qo90zvIm52LYeBUen9bIHfH1Cu6UzTnAsbDoJRoQgqHnEXA18xL0KGAUe0H4EYRnepa8etMIkyY2Ekgm%2F8ut9LvOmHBwxG8o4jQhgirmu1pqn%2BkEObygd6neGmlM6YDDsti5vg7Em%2Bz%2BGaYY3SyH8%2Bmr6OT7IiCtCP0we4aiNVuSSu7za1XCGMWoVVyMCgGmHhKX2IV33Bq5nKarlR7tvv2shxCLvdjDm1i5payWze%2BGq9tykmxB8Mf7kirPFPlxi%2BkzR6CS1lmBKyBPBSiHQaViRkVAKdDfybIiYBDU41xq1Jnvkws%2FKvyAY6pgHqLivEmN3NKOZW091uNvy3mu5mZ0ZKbNSQTpHuc8g4xiZdCKjC%2BeXWd2OGAcjX6jlansQ1VoVTOIwOrA99IOerDCBFXa3p8NR0B%2FpzsFxjZKXzgtrGoiavhOMPNQ%2B2gCmBjBwg%2FSsAW%2Fab%2FqKdg%2B6HCvGGFRXTKlOtwri%2BiZV5deZiuXiTd9GPyTfYdtRe%2B4t01R2fGrtj1dPGiUsRR4eJgMHw2xLv&X-Amz-Signature=27f6344728699601be642aa9613fe0ae002d041d739310de47da2e9c28008a76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656PM6IV4%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH90IFcfPlBV62%2F5OVk2bPxIQcJKoOWt8wnp1pH8Sk0iAiAgbKHt6YDkCOYfvJE9D3%2FnaH%2F7sv1NtizslHo4WucBUCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLgeyHe%2FDh%2FDAl09IKtwDRdSPmskSQ1yrHp6Mx8veYcUJ7eM7Qj9hkqXdqgp%2FWvzvIWCzyIveu%2Byt9k5dHHl6qSgUumov6U0TjJhQVC5m6yrxqDdyKo2%2FuUiklswUtrNz3hFiO9G%2B%2FD2YCH7FuV%2FLhPxEFm8gxCMuRzl0zZCh%2BFJfotYqTW80Z4z3ituYkSoNKPvRCfMv4nHFNM5sH7emXWUSUPFjayqKG8ouJbEO6UXAKO%2BzRk7l42uiv%2B3Ve0JLw3q20FjhtVquW9CI6fMDTovGn4ePQH9WZN9sU%2FOtBJIMx7GBBx2Dm7%2FGKxRioFFLrRm4WPdTZ7PPFvFUQSj4MnquTr27z3Qo90zvIm52LYeBUen9bIHfH1Cu6UzTnAsbDoJRoQgqHnEXA18xL0KGAUe0H4EYRnepa8etMIkyY2Ekgm%2F8ut9LvOmHBwxG8o4jQhgirmu1pqn%2BkEObygd6neGmlM6YDDsti5vg7Em%2Bz%2BGaYY3SyH8%2Bmr6OT7IiCtCP0we4aiNVuSSu7za1XCGMWoVVyMCgGmHhKX2IV33Bq5nKarlR7tvv2shxCLvdjDm1i5payWze%2BGq9tykmxB8Mf7kirPFPlxi%2BkzR6CS1lmBKyBPBSiHQaViRkVAKdDfybIiYBDU41xq1Jnvkws%2FKvyAY6pgHqLivEmN3NKOZW091uNvy3mu5mZ0ZKbNSQTpHuc8g4xiZdCKjC%2BeXWd2OGAcjX6jlansQ1VoVTOIwOrA99IOerDCBFXa3p8NR0B%2FpzsFxjZKXzgtrGoiavhOMPNQ%2B2gCmBjBwg%2FSsAW%2Fab%2FqKdg%2B6HCvGGFRXTKlOtwri%2BiZV5deZiuXiTd9GPyTfYdtRe%2B4t01R2fGrtj1dPGiUsRR4eJgMHw2xLv&X-Amz-Signature=4d0cb9fd5af9e613f2a510d490fc1b048cdec002984efe249ff71c6604ae00cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

