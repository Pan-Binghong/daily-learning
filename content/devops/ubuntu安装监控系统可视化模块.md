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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U33B2OSL%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIA4IuzBSKXCp0ffVK%2FMLcwv6nGiBW%2FMagtAO33yK4fpIAiAr5XGl%2FjGFMr8VfmJJKLyye%2BJZfFtFaucO8B8wyvqnJyr%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMw1UUrJJlPr8aCfosKtwDidYz1Iy4X0b3Xof8T629l%2BX2xvuaM%2BBr%2BuMcBFQDW1icP03Ov6lqqDD0c12d8lQsm3I2gv1WkO%2BSa69Qz1JT%2FhcyUas8RKidClFazokFbjjyPo8rsq9%2Fbdott7NdpT%2BZlWUB%2Bn1jLdiWWS6UlY51Y%2B8alFAh8zVSN6sS%2FNXUcqbb8KaKQcJ%2F9pk2oGhpz%2FQturxYJWBmnBakgwiuhh4PDQkvAO5wH85wat6LmIBoeF0EsrWODI5UpjQPNdPWhZOJiN1Zng6UfYaZJI1iGaUTfhKujSBlWGuHKbXK%2BtfKctyvb0Uyt85Tt6%2BHsfrv097R7%2FmlYw6fZegsGyFlpj2PJwD%2Fu7csCs6nh%2FlfmbH9dP%2BkOfOFAt3VSbAraAQ63rLTZoGOkvrbe%2FMdq4MgZsvtYy0sihLUSN3704HFoiP5tlGIrnGBNVTc9dEUlBdJqV7xRAugpFH4mOAiI3dB%2B15XYJwVOuo0hT0YBYaoALpQz2k5zVrlyUc4tA0RHFjCMfWzlL54%2FMYIdTVYW%2BvHjuHJ2PyCQ8TXyvOvS5SIskCXU8rGWU42vH%2FkKlj7RG5yyRbBhsWfBgdA0R5%2FlME1O7xM10h8vagPIRhRnRk9csQLZp%2BMKkKyUJxitDx1lEUwsLHaywY6pgGGbfu0qku1fnUL2xolhUyK7uaInJFLVfpfosAT%2BTXGafC8piwnH4WTEhGRHSre%2FHKlGulcc21XqFLJvDJhI0sWIkwnn2WqfWdLP5zp9e%2BjJTGtHJNAGfyChQ8yjyPtun1kr4i%2B2FNKoUiSybCnJ3Am3LYon2DzTnY0HndQzNfv%2BQOjC8Z1F2sG46dWYyI%2BlavxQqhpnMvtXMHvmmZhTdwwfAIRtumU&X-Amz-Signature=47adfae1b2c0354ad8e2703ad618c72cb2467fd79fa8ff6e5fb772cf00086fc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U33B2OSL%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIA4IuzBSKXCp0ffVK%2FMLcwv6nGiBW%2FMagtAO33yK4fpIAiAr5XGl%2FjGFMr8VfmJJKLyye%2BJZfFtFaucO8B8wyvqnJyr%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMw1UUrJJlPr8aCfosKtwDidYz1Iy4X0b3Xof8T629l%2BX2xvuaM%2BBr%2BuMcBFQDW1icP03Ov6lqqDD0c12d8lQsm3I2gv1WkO%2BSa69Qz1JT%2FhcyUas8RKidClFazokFbjjyPo8rsq9%2Fbdott7NdpT%2BZlWUB%2Bn1jLdiWWS6UlY51Y%2B8alFAh8zVSN6sS%2FNXUcqbb8KaKQcJ%2F9pk2oGhpz%2FQturxYJWBmnBakgwiuhh4PDQkvAO5wH85wat6LmIBoeF0EsrWODI5UpjQPNdPWhZOJiN1Zng6UfYaZJI1iGaUTfhKujSBlWGuHKbXK%2BtfKctyvb0Uyt85Tt6%2BHsfrv097R7%2FmlYw6fZegsGyFlpj2PJwD%2Fu7csCs6nh%2FlfmbH9dP%2BkOfOFAt3VSbAraAQ63rLTZoGOkvrbe%2FMdq4MgZsvtYy0sihLUSN3704HFoiP5tlGIrnGBNVTc9dEUlBdJqV7xRAugpFH4mOAiI3dB%2B15XYJwVOuo0hT0YBYaoALpQz2k5zVrlyUc4tA0RHFjCMfWzlL54%2FMYIdTVYW%2BvHjuHJ2PyCQ8TXyvOvS5SIskCXU8rGWU42vH%2FkKlj7RG5yyRbBhsWfBgdA0R5%2FlME1O7xM10h8vagPIRhRnRk9csQLZp%2BMKkKyUJxitDx1lEUwsLHaywY6pgGGbfu0qku1fnUL2xolhUyK7uaInJFLVfpfosAT%2BTXGafC8piwnH4WTEhGRHSre%2FHKlGulcc21XqFLJvDJhI0sWIkwnn2WqfWdLP5zp9e%2BjJTGtHJNAGfyChQ8yjyPtun1kr4i%2B2FNKoUiSybCnJ3Am3LYon2DzTnY0HndQzNfv%2BQOjC8Z1F2sG46dWYyI%2BlavxQqhpnMvtXMHvmmZhTdwwfAIRtumU&X-Amz-Signature=525f360af1fab4849d0e6a59036abf353681ab8a1cabdb6ad33d5bd79632f129&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U33B2OSL%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIA4IuzBSKXCp0ffVK%2FMLcwv6nGiBW%2FMagtAO33yK4fpIAiAr5XGl%2FjGFMr8VfmJJKLyye%2BJZfFtFaucO8B8wyvqnJyr%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMw1UUrJJlPr8aCfosKtwDidYz1Iy4X0b3Xof8T629l%2BX2xvuaM%2BBr%2BuMcBFQDW1icP03Ov6lqqDD0c12d8lQsm3I2gv1WkO%2BSa69Qz1JT%2FhcyUas8RKidClFazokFbjjyPo8rsq9%2Fbdott7NdpT%2BZlWUB%2Bn1jLdiWWS6UlY51Y%2B8alFAh8zVSN6sS%2FNXUcqbb8KaKQcJ%2F9pk2oGhpz%2FQturxYJWBmnBakgwiuhh4PDQkvAO5wH85wat6LmIBoeF0EsrWODI5UpjQPNdPWhZOJiN1Zng6UfYaZJI1iGaUTfhKujSBlWGuHKbXK%2BtfKctyvb0Uyt85Tt6%2BHsfrv097R7%2FmlYw6fZegsGyFlpj2PJwD%2Fu7csCs6nh%2FlfmbH9dP%2BkOfOFAt3VSbAraAQ63rLTZoGOkvrbe%2FMdq4MgZsvtYy0sihLUSN3704HFoiP5tlGIrnGBNVTc9dEUlBdJqV7xRAugpFH4mOAiI3dB%2B15XYJwVOuo0hT0YBYaoALpQz2k5zVrlyUc4tA0RHFjCMfWzlL54%2FMYIdTVYW%2BvHjuHJ2PyCQ8TXyvOvS5SIskCXU8rGWU42vH%2FkKlj7RG5yyRbBhsWfBgdA0R5%2FlME1O7xM10h8vagPIRhRnRk9csQLZp%2BMKkKyUJxitDx1lEUwsLHaywY6pgGGbfu0qku1fnUL2xolhUyK7uaInJFLVfpfosAT%2BTXGafC8piwnH4WTEhGRHSre%2FHKlGulcc21XqFLJvDJhI0sWIkwnn2WqfWdLP5zp9e%2BjJTGtHJNAGfyChQ8yjyPtun1kr4i%2B2FNKoUiSybCnJ3Am3LYon2DzTnY0HndQzNfv%2BQOjC8Z1F2sG46dWYyI%2BlavxQqhpnMvtXMHvmmZhTdwwfAIRtumU&X-Amz-Signature=524b9e0f43ca75723363bad892e04c6fda3e0093487a1c50fc5b9632debc6a6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U33B2OSL%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIA4IuzBSKXCp0ffVK%2FMLcwv6nGiBW%2FMagtAO33yK4fpIAiAr5XGl%2FjGFMr8VfmJJKLyye%2BJZfFtFaucO8B8wyvqnJyr%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMw1UUrJJlPr8aCfosKtwDidYz1Iy4X0b3Xof8T629l%2BX2xvuaM%2BBr%2BuMcBFQDW1icP03Ov6lqqDD0c12d8lQsm3I2gv1WkO%2BSa69Qz1JT%2FhcyUas8RKidClFazokFbjjyPo8rsq9%2Fbdott7NdpT%2BZlWUB%2Bn1jLdiWWS6UlY51Y%2B8alFAh8zVSN6sS%2FNXUcqbb8KaKQcJ%2F9pk2oGhpz%2FQturxYJWBmnBakgwiuhh4PDQkvAO5wH85wat6LmIBoeF0EsrWODI5UpjQPNdPWhZOJiN1Zng6UfYaZJI1iGaUTfhKujSBlWGuHKbXK%2BtfKctyvb0Uyt85Tt6%2BHsfrv097R7%2FmlYw6fZegsGyFlpj2PJwD%2Fu7csCs6nh%2FlfmbH9dP%2BkOfOFAt3VSbAraAQ63rLTZoGOkvrbe%2FMdq4MgZsvtYy0sihLUSN3704HFoiP5tlGIrnGBNVTc9dEUlBdJqV7xRAugpFH4mOAiI3dB%2B15XYJwVOuo0hT0YBYaoALpQz2k5zVrlyUc4tA0RHFjCMfWzlL54%2FMYIdTVYW%2BvHjuHJ2PyCQ8TXyvOvS5SIskCXU8rGWU42vH%2FkKlj7RG5yyRbBhsWfBgdA0R5%2FlME1O7xM10h8vagPIRhRnRk9csQLZp%2BMKkKyUJxitDx1lEUwsLHaywY6pgGGbfu0qku1fnUL2xolhUyK7uaInJFLVfpfosAT%2BTXGafC8piwnH4WTEhGRHSre%2FHKlGulcc21XqFLJvDJhI0sWIkwnn2WqfWdLP5zp9e%2BjJTGtHJNAGfyChQ8yjyPtun1kr4i%2B2FNKoUiSybCnJ3Am3LYon2DzTnY0HndQzNfv%2BQOjC8Z1F2sG46dWYyI%2BlavxQqhpnMvtXMHvmmZhTdwwfAIRtumU&X-Amz-Signature=13786472c0896b1258a54953ec90b3eceed9a24dd80e4306de8eb6e66b5205cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U33B2OSL%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIA4IuzBSKXCp0ffVK%2FMLcwv6nGiBW%2FMagtAO33yK4fpIAiAr5XGl%2FjGFMr8VfmJJKLyye%2BJZfFtFaucO8B8wyvqnJyr%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMw1UUrJJlPr8aCfosKtwDidYz1Iy4X0b3Xof8T629l%2BX2xvuaM%2BBr%2BuMcBFQDW1icP03Ov6lqqDD0c12d8lQsm3I2gv1WkO%2BSa69Qz1JT%2FhcyUas8RKidClFazokFbjjyPo8rsq9%2Fbdott7NdpT%2BZlWUB%2Bn1jLdiWWS6UlY51Y%2B8alFAh8zVSN6sS%2FNXUcqbb8KaKQcJ%2F9pk2oGhpz%2FQturxYJWBmnBakgwiuhh4PDQkvAO5wH85wat6LmIBoeF0EsrWODI5UpjQPNdPWhZOJiN1Zng6UfYaZJI1iGaUTfhKujSBlWGuHKbXK%2BtfKctyvb0Uyt85Tt6%2BHsfrv097R7%2FmlYw6fZegsGyFlpj2PJwD%2Fu7csCs6nh%2FlfmbH9dP%2BkOfOFAt3VSbAraAQ63rLTZoGOkvrbe%2FMdq4MgZsvtYy0sihLUSN3704HFoiP5tlGIrnGBNVTc9dEUlBdJqV7xRAugpFH4mOAiI3dB%2B15XYJwVOuo0hT0YBYaoALpQz2k5zVrlyUc4tA0RHFjCMfWzlL54%2FMYIdTVYW%2BvHjuHJ2PyCQ8TXyvOvS5SIskCXU8rGWU42vH%2FkKlj7RG5yyRbBhsWfBgdA0R5%2FlME1O7xM10h8vagPIRhRnRk9csQLZp%2BMKkKyUJxitDx1lEUwsLHaywY6pgGGbfu0qku1fnUL2xolhUyK7uaInJFLVfpfosAT%2BTXGafC8piwnH4WTEhGRHSre%2FHKlGulcc21XqFLJvDJhI0sWIkwnn2WqfWdLP5zp9e%2BjJTGtHJNAGfyChQ8yjyPtun1kr4i%2B2FNKoUiSybCnJ3Am3LYon2DzTnY0HndQzNfv%2BQOjC8Z1F2sG46dWYyI%2BlavxQqhpnMvtXMHvmmZhTdwwfAIRtumU&X-Amz-Signature=6df0e15eabde0fd927a70963ba1f44cfecc32050eccc3481d67341478ddc618d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U33B2OSL%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIA4IuzBSKXCp0ffVK%2FMLcwv6nGiBW%2FMagtAO33yK4fpIAiAr5XGl%2FjGFMr8VfmJJKLyye%2BJZfFtFaucO8B8wyvqnJyr%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMw1UUrJJlPr8aCfosKtwDidYz1Iy4X0b3Xof8T629l%2BX2xvuaM%2BBr%2BuMcBFQDW1icP03Ov6lqqDD0c12d8lQsm3I2gv1WkO%2BSa69Qz1JT%2FhcyUas8RKidClFazokFbjjyPo8rsq9%2Fbdott7NdpT%2BZlWUB%2Bn1jLdiWWS6UlY51Y%2B8alFAh8zVSN6sS%2FNXUcqbb8KaKQcJ%2F9pk2oGhpz%2FQturxYJWBmnBakgwiuhh4PDQkvAO5wH85wat6LmIBoeF0EsrWODI5UpjQPNdPWhZOJiN1Zng6UfYaZJI1iGaUTfhKujSBlWGuHKbXK%2BtfKctyvb0Uyt85Tt6%2BHsfrv097R7%2FmlYw6fZegsGyFlpj2PJwD%2Fu7csCs6nh%2FlfmbH9dP%2BkOfOFAt3VSbAraAQ63rLTZoGOkvrbe%2FMdq4MgZsvtYy0sihLUSN3704HFoiP5tlGIrnGBNVTc9dEUlBdJqV7xRAugpFH4mOAiI3dB%2B15XYJwVOuo0hT0YBYaoALpQz2k5zVrlyUc4tA0RHFjCMfWzlL54%2FMYIdTVYW%2BvHjuHJ2PyCQ8TXyvOvS5SIskCXU8rGWU42vH%2FkKlj7RG5yyRbBhsWfBgdA0R5%2FlME1O7xM10h8vagPIRhRnRk9csQLZp%2BMKkKyUJxitDx1lEUwsLHaywY6pgGGbfu0qku1fnUL2xolhUyK7uaInJFLVfpfosAT%2BTXGafC8piwnH4WTEhGRHSre%2FHKlGulcc21XqFLJvDJhI0sWIkwnn2WqfWdLP5zp9e%2BjJTGtHJNAGfyChQ8yjyPtun1kr4i%2B2FNKoUiSybCnJ3Am3LYon2DzTnY0HndQzNfv%2BQOjC8Z1F2sG46dWYyI%2BlavxQqhpnMvtXMHvmmZhTdwwfAIRtumU&X-Amz-Signature=b3361eb8eaa083665063bff722c255095f63ef1061c0066437546e623a57139d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U33B2OSL%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIA4IuzBSKXCp0ffVK%2FMLcwv6nGiBW%2FMagtAO33yK4fpIAiAr5XGl%2FjGFMr8VfmJJKLyye%2BJZfFtFaucO8B8wyvqnJyr%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMw1UUrJJlPr8aCfosKtwDidYz1Iy4X0b3Xof8T629l%2BX2xvuaM%2BBr%2BuMcBFQDW1icP03Ov6lqqDD0c12d8lQsm3I2gv1WkO%2BSa69Qz1JT%2FhcyUas8RKidClFazokFbjjyPo8rsq9%2Fbdott7NdpT%2BZlWUB%2Bn1jLdiWWS6UlY51Y%2B8alFAh8zVSN6sS%2FNXUcqbb8KaKQcJ%2F9pk2oGhpz%2FQturxYJWBmnBakgwiuhh4PDQkvAO5wH85wat6LmIBoeF0EsrWODI5UpjQPNdPWhZOJiN1Zng6UfYaZJI1iGaUTfhKujSBlWGuHKbXK%2BtfKctyvb0Uyt85Tt6%2BHsfrv097R7%2FmlYw6fZegsGyFlpj2PJwD%2Fu7csCs6nh%2FlfmbH9dP%2BkOfOFAt3VSbAraAQ63rLTZoGOkvrbe%2FMdq4MgZsvtYy0sihLUSN3704HFoiP5tlGIrnGBNVTc9dEUlBdJqV7xRAugpFH4mOAiI3dB%2B15XYJwVOuo0hT0YBYaoALpQz2k5zVrlyUc4tA0RHFjCMfWzlL54%2FMYIdTVYW%2BvHjuHJ2PyCQ8TXyvOvS5SIskCXU8rGWU42vH%2FkKlj7RG5yyRbBhsWfBgdA0R5%2FlME1O7xM10h8vagPIRhRnRk9csQLZp%2BMKkKyUJxitDx1lEUwsLHaywY6pgGGbfu0qku1fnUL2xolhUyK7uaInJFLVfpfosAT%2BTXGafC8piwnH4WTEhGRHSre%2FHKlGulcc21XqFLJvDJhI0sWIkwnn2WqfWdLP5zp9e%2BjJTGtHJNAGfyChQ8yjyPtun1kr4i%2B2FNKoUiSybCnJ3Am3LYon2DzTnY0HndQzNfv%2BQOjC8Z1F2sG46dWYyI%2BlavxQqhpnMvtXMHvmmZhTdwwfAIRtumU&X-Amz-Signature=a71be5317cb1e632a7e38a8b0f99c25f999d4ac8cba9ab90e24241f33799fe8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

