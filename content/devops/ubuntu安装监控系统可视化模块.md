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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCJIORS6%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAOf%2Fjus3SkJnXJAnOdmO6xe5vUKaTljFf6BRVvlKoNoAiEArBRtoYCe2GJsnFYxP0vrqhz2SFqWMsCPv0xTrunTFDUqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPJJISFEH%2B5enukwGCrcA3PT%2B%2FIcpxuILyO3Omq3NfMdC7o1jLhwS%2F8zxk%2FDOgF71FNw%2BXtMGnTPeXOzVulGdWBIGCYwu8nKdESILarb3jqIzllf1YhCaIUPt2C3IjraQomBNugbtftDN8SMgoAquUwOjVWNESAuf%2BYvG6qHcT3Y32nVaTCNtzWJUYt%2BtWv0ht9lKO6jcHHc49WzP1FFfEXwOquOKkMZ4u88pCyK1k7rpbXVr5q148w8ts8qPRMhGenIhJ6IMd00esF9PQqzT9MqA3NZWxuqICPa89F7WtWqHXBcrUG3Ri6GZKCwsM4fs0V3hv1rm%2F7qZkOC72vbsrdUGDl1dMkqv7uAsCyHuLiCtsUkzgD5Q4A3DtMh7lzNEASB0oOzlGrk72FOAhumlIVFXFX5gkA7Vcc2VpRodF3StgwwMbhaQ3Sf5iGt%2BhsrpW7oaCYgNW4Uus0guGnRF%2BLJm%2BpD2D80%2FvlCgpxg%2BsHGSqisz9RyfjV1%2FQZE5GoJO3xCzUl7vkSVxKp3E1hlM2g%2BsntjrGAcBqoArZIvQaETUAtiyQ8j%2FT2jqMHYFqFz2hmnTQfKiaYESYcPfYHr8L7ztCk52QrBD5j%2BbzIhUcYfCHUNvDEWzW6VSukF2QlNfdQMxBGRgo%2BXotWFMMv90skGOqUB%2FMrbumiS1%2BK9bIWWK3EWbd6kdYwlEBdZ%2BQhzzg%2BZG40LVEA49foZmrM%2F%2F9rsiBB%2BcSW9jKPoGok5x0JOGFTg35qDP1z7B3F3evq5Q6K8BSUsqkOlhl%2FezzqcJcjcwnluDmjBdKL0lzdBQak4YTU0ZNwwk%2Bq8ndd%2FYWmcToSaSvelcC4z1Uh1Vq7yWd0HGHY5%2BQ2zu9%2B9Cm88AkM8PfEsva%2BGi4EN&X-Amz-Signature=256a1018ce6ff7ea92e469244039dc5da5615cc27e1fcf590ec5f98a07f3f095&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCJIORS6%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAOf%2Fjus3SkJnXJAnOdmO6xe5vUKaTljFf6BRVvlKoNoAiEArBRtoYCe2GJsnFYxP0vrqhz2SFqWMsCPv0xTrunTFDUqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPJJISFEH%2B5enukwGCrcA3PT%2B%2FIcpxuILyO3Omq3NfMdC7o1jLhwS%2F8zxk%2FDOgF71FNw%2BXtMGnTPeXOzVulGdWBIGCYwu8nKdESILarb3jqIzllf1YhCaIUPt2C3IjraQomBNugbtftDN8SMgoAquUwOjVWNESAuf%2BYvG6qHcT3Y32nVaTCNtzWJUYt%2BtWv0ht9lKO6jcHHc49WzP1FFfEXwOquOKkMZ4u88pCyK1k7rpbXVr5q148w8ts8qPRMhGenIhJ6IMd00esF9PQqzT9MqA3NZWxuqICPa89F7WtWqHXBcrUG3Ri6GZKCwsM4fs0V3hv1rm%2F7qZkOC72vbsrdUGDl1dMkqv7uAsCyHuLiCtsUkzgD5Q4A3DtMh7lzNEASB0oOzlGrk72FOAhumlIVFXFX5gkA7Vcc2VpRodF3StgwwMbhaQ3Sf5iGt%2BhsrpW7oaCYgNW4Uus0guGnRF%2BLJm%2BpD2D80%2FvlCgpxg%2BsHGSqisz9RyfjV1%2FQZE5GoJO3xCzUl7vkSVxKp3E1hlM2g%2BsntjrGAcBqoArZIvQaETUAtiyQ8j%2FT2jqMHYFqFz2hmnTQfKiaYESYcPfYHr8L7ztCk52QrBD5j%2BbzIhUcYfCHUNvDEWzW6VSukF2QlNfdQMxBGRgo%2BXotWFMMv90skGOqUB%2FMrbumiS1%2BK9bIWWK3EWbd6kdYwlEBdZ%2BQhzzg%2BZG40LVEA49foZmrM%2F%2F9rsiBB%2BcSW9jKPoGok5x0JOGFTg35qDP1z7B3F3evq5Q6K8BSUsqkOlhl%2FezzqcJcjcwnluDmjBdKL0lzdBQak4YTU0ZNwwk%2Bq8ndd%2FYWmcToSaSvelcC4z1Uh1Vq7yWd0HGHY5%2BQ2zu9%2B9Cm88AkM8PfEsva%2BGi4EN&X-Amz-Signature=1f52126903a9f9180932dc0b366a1dac0333d187726c3defd904a659cc807cf3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCJIORS6%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAOf%2Fjus3SkJnXJAnOdmO6xe5vUKaTljFf6BRVvlKoNoAiEArBRtoYCe2GJsnFYxP0vrqhz2SFqWMsCPv0xTrunTFDUqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPJJISFEH%2B5enukwGCrcA3PT%2B%2FIcpxuILyO3Omq3NfMdC7o1jLhwS%2F8zxk%2FDOgF71FNw%2BXtMGnTPeXOzVulGdWBIGCYwu8nKdESILarb3jqIzllf1YhCaIUPt2C3IjraQomBNugbtftDN8SMgoAquUwOjVWNESAuf%2BYvG6qHcT3Y32nVaTCNtzWJUYt%2BtWv0ht9lKO6jcHHc49WzP1FFfEXwOquOKkMZ4u88pCyK1k7rpbXVr5q148w8ts8qPRMhGenIhJ6IMd00esF9PQqzT9MqA3NZWxuqICPa89F7WtWqHXBcrUG3Ri6GZKCwsM4fs0V3hv1rm%2F7qZkOC72vbsrdUGDl1dMkqv7uAsCyHuLiCtsUkzgD5Q4A3DtMh7lzNEASB0oOzlGrk72FOAhumlIVFXFX5gkA7Vcc2VpRodF3StgwwMbhaQ3Sf5iGt%2BhsrpW7oaCYgNW4Uus0guGnRF%2BLJm%2BpD2D80%2FvlCgpxg%2BsHGSqisz9RyfjV1%2FQZE5GoJO3xCzUl7vkSVxKp3E1hlM2g%2BsntjrGAcBqoArZIvQaETUAtiyQ8j%2FT2jqMHYFqFz2hmnTQfKiaYESYcPfYHr8L7ztCk52QrBD5j%2BbzIhUcYfCHUNvDEWzW6VSukF2QlNfdQMxBGRgo%2BXotWFMMv90skGOqUB%2FMrbumiS1%2BK9bIWWK3EWbd6kdYwlEBdZ%2BQhzzg%2BZG40LVEA49foZmrM%2F%2F9rsiBB%2BcSW9jKPoGok5x0JOGFTg35qDP1z7B3F3evq5Q6K8BSUsqkOlhl%2FezzqcJcjcwnluDmjBdKL0lzdBQak4YTU0ZNwwk%2Bq8ndd%2FYWmcToSaSvelcC4z1Uh1Vq7yWd0HGHY5%2BQ2zu9%2B9Cm88AkM8PfEsva%2BGi4EN&X-Amz-Signature=6cf28463850a4095dcfa8d7cefd4a149d81f68f9761e0672160b99e3575def42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCJIORS6%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAOf%2Fjus3SkJnXJAnOdmO6xe5vUKaTljFf6BRVvlKoNoAiEArBRtoYCe2GJsnFYxP0vrqhz2SFqWMsCPv0xTrunTFDUqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPJJISFEH%2B5enukwGCrcA3PT%2B%2FIcpxuILyO3Omq3NfMdC7o1jLhwS%2F8zxk%2FDOgF71FNw%2BXtMGnTPeXOzVulGdWBIGCYwu8nKdESILarb3jqIzllf1YhCaIUPt2C3IjraQomBNugbtftDN8SMgoAquUwOjVWNESAuf%2BYvG6qHcT3Y32nVaTCNtzWJUYt%2BtWv0ht9lKO6jcHHc49WzP1FFfEXwOquOKkMZ4u88pCyK1k7rpbXVr5q148w8ts8qPRMhGenIhJ6IMd00esF9PQqzT9MqA3NZWxuqICPa89F7WtWqHXBcrUG3Ri6GZKCwsM4fs0V3hv1rm%2F7qZkOC72vbsrdUGDl1dMkqv7uAsCyHuLiCtsUkzgD5Q4A3DtMh7lzNEASB0oOzlGrk72FOAhumlIVFXFX5gkA7Vcc2VpRodF3StgwwMbhaQ3Sf5iGt%2BhsrpW7oaCYgNW4Uus0guGnRF%2BLJm%2BpD2D80%2FvlCgpxg%2BsHGSqisz9RyfjV1%2FQZE5GoJO3xCzUl7vkSVxKp3E1hlM2g%2BsntjrGAcBqoArZIvQaETUAtiyQ8j%2FT2jqMHYFqFz2hmnTQfKiaYESYcPfYHr8L7ztCk52QrBD5j%2BbzIhUcYfCHUNvDEWzW6VSukF2QlNfdQMxBGRgo%2BXotWFMMv90skGOqUB%2FMrbumiS1%2BK9bIWWK3EWbd6kdYwlEBdZ%2BQhzzg%2BZG40LVEA49foZmrM%2F%2F9rsiBB%2BcSW9jKPoGok5x0JOGFTg35qDP1z7B3F3evq5Q6K8BSUsqkOlhl%2FezzqcJcjcwnluDmjBdKL0lzdBQak4YTU0ZNwwk%2Bq8ndd%2FYWmcToSaSvelcC4z1Uh1Vq7yWd0HGHY5%2BQ2zu9%2B9Cm88AkM8PfEsva%2BGi4EN&X-Amz-Signature=79375188237a4a19b2e3c807c2ff3d756249749e6577015e01dc6cb76b557457&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCJIORS6%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAOf%2Fjus3SkJnXJAnOdmO6xe5vUKaTljFf6BRVvlKoNoAiEArBRtoYCe2GJsnFYxP0vrqhz2SFqWMsCPv0xTrunTFDUqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPJJISFEH%2B5enukwGCrcA3PT%2B%2FIcpxuILyO3Omq3NfMdC7o1jLhwS%2F8zxk%2FDOgF71FNw%2BXtMGnTPeXOzVulGdWBIGCYwu8nKdESILarb3jqIzllf1YhCaIUPt2C3IjraQomBNugbtftDN8SMgoAquUwOjVWNESAuf%2BYvG6qHcT3Y32nVaTCNtzWJUYt%2BtWv0ht9lKO6jcHHc49WzP1FFfEXwOquOKkMZ4u88pCyK1k7rpbXVr5q148w8ts8qPRMhGenIhJ6IMd00esF9PQqzT9MqA3NZWxuqICPa89F7WtWqHXBcrUG3Ri6GZKCwsM4fs0V3hv1rm%2F7qZkOC72vbsrdUGDl1dMkqv7uAsCyHuLiCtsUkzgD5Q4A3DtMh7lzNEASB0oOzlGrk72FOAhumlIVFXFX5gkA7Vcc2VpRodF3StgwwMbhaQ3Sf5iGt%2BhsrpW7oaCYgNW4Uus0guGnRF%2BLJm%2BpD2D80%2FvlCgpxg%2BsHGSqisz9RyfjV1%2FQZE5GoJO3xCzUl7vkSVxKp3E1hlM2g%2BsntjrGAcBqoArZIvQaETUAtiyQ8j%2FT2jqMHYFqFz2hmnTQfKiaYESYcPfYHr8L7ztCk52QrBD5j%2BbzIhUcYfCHUNvDEWzW6VSukF2QlNfdQMxBGRgo%2BXotWFMMv90skGOqUB%2FMrbumiS1%2BK9bIWWK3EWbd6kdYwlEBdZ%2BQhzzg%2BZG40LVEA49foZmrM%2F%2F9rsiBB%2BcSW9jKPoGok5x0JOGFTg35qDP1z7B3F3evq5Q6K8BSUsqkOlhl%2FezzqcJcjcwnluDmjBdKL0lzdBQak4YTU0ZNwwk%2Bq8ndd%2FYWmcToSaSvelcC4z1Uh1Vq7yWd0HGHY5%2BQ2zu9%2B9Cm88AkM8PfEsva%2BGi4EN&X-Amz-Signature=aa6d3eebaf8afa4c5306d02c991c5f03c71db23be6a35607bd493be4b953856d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCJIORS6%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAOf%2Fjus3SkJnXJAnOdmO6xe5vUKaTljFf6BRVvlKoNoAiEArBRtoYCe2GJsnFYxP0vrqhz2SFqWMsCPv0xTrunTFDUqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPJJISFEH%2B5enukwGCrcA3PT%2B%2FIcpxuILyO3Omq3NfMdC7o1jLhwS%2F8zxk%2FDOgF71FNw%2BXtMGnTPeXOzVulGdWBIGCYwu8nKdESILarb3jqIzllf1YhCaIUPt2C3IjraQomBNugbtftDN8SMgoAquUwOjVWNESAuf%2BYvG6qHcT3Y32nVaTCNtzWJUYt%2BtWv0ht9lKO6jcHHc49WzP1FFfEXwOquOKkMZ4u88pCyK1k7rpbXVr5q148w8ts8qPRMhGenIhJ6IMd00esF9PQqzT9MqA3NZWxuqICPa89F7WtWqHXBcrUG3Ri6GZKCwsM4fs0V3hv1rm%2F7qZkOC72vbsrdUGDl1dMkqv7uAsCyHuLiCtsUkzgD5Q4A3DtMh7lzNEASB0oOzlGrk72FOAhumlIVFXFX5gkA7Vcc2VpRodF3StgwwMbhaQ3Sf5iGt%2BhsrpW7oaCYgNW4Uus0guGnRF%2BLJm%2BpD2D80%2FvlCgpxg%2BsHGSqisz9RyfjV1%2FQZE5GoJO3xCzUl7vkSVxKp3E1hlM2g%2BsntjrGAcBqoArZIvQaETUAtiyQ8j%2FT2jqMHYFqFz2hmnTQfKiaYESYcPfYHr8L7ztCk52QrBD5j%2BbzIhUcYfCHUNvDEWzW6VSukF2QlNfdQMxBGRgo%2BXotWFMMv90skGOqUB%2FMrbumiS1%2BK9bIWWK3EWbd6kdYwlEBdZ%2BQhzzg%2BZG40LVEA49foZmrM%2F%2F9rsiBB%2BcSW9jKPoGok5x0JOGFTg35qDP1z7B3F3evq5Q6K8BSUsqkOlhl%2FezzqcJcjcwnluDmjBdKL0lzdBQak4YTU0ZNwwk%2Bq8ndd%2FYWmcToSaSvelcC4z1Uh1Vq7yWd0HGHY5%2BQ2zu9%2B9Cm88AkM8PfEsva%2BGi4EN&X-Amz-Signature=d9b4d6423cc7927e30e4e76d15a725cd4d42b980e43f488ffdb4207d9f9a24fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCJIORS6%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAOf%2Fjus3SkJnXJAnOdmO6xe5vUKaTljFf6BRVvlKoNoAiEArBRtoYCe2GJsnFYxP0vrqhz2SFqWMsCPv0xTrunTFDUqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPJJISFEH%2B5enukwGCrcA3PT%2B%2FIcpxuILyO3Omq3NfMdC7o1jLhwS%2F8zxk%2FDOgF71FNw%2BXtMGnTPeXOzVulGdWBIGCYwu8nKdESILarb3jqIzllf1YhCaIUPt2C3IjraQomBNugbtftDN8SMgoAquUwOjVWNESAuf%2BYvG6qHcT3Y32nVaTCNtzWJUYt%2BtWv0ht9lKO6jcHHc49WzP1FFfEXwOquOKkMZ4u88pCyK1k7rpbXVr5q148w8ts8qPRMhGenIhJ6IMd00esF9PQqzT9MqA3NZWxuqICPa89F7WtWqHXBcrUG3Ri6GZKCwsM4fs0V3hv1rm%2F7qZkOC72vbsrdUGDl1dMkqv7uAsCyHuLiCtsUkzgD5Q4A3DtMh7lzNEASB0oOzlGrk72FOAhumlIVFXFX5gkA7Vcc2VpRodF3StgwwMbhaQ3Sf5iGt%2BhsrpW7oaCYgNW4Uus0guGnRF%2BLJm%2BpD2D80%2FvlCgpxg%2BsHGSqisz9RyfjV1%2FQZE5GoJO3xCzUl7vkSVxKp3E1hlM2g%2BsntjrGAcBqoArZIvQaETUAtiyQ8j%2FT2jqMHYFqFz2hmnTQfKiaYESYcPfYHr8L7ztCk52QrBD5j%2BbzIhUcYfCHUNvDEWzW6VSukF2QlNfdQMxBGRgo%2BXotWFMMv90skGOqUB%2FMrbumiS1%2BK9bIWWK3EWbd6kdYwlEBdZ%2BQhzzg%2BZG40LVEA49foZmrM%2F%2F9rsiBB%2BcSW9jKPoGok5x0JOGFTg35qDP1z7B3F3evq5Q6K8BSUsqkOlhl%2FezzqcJcjcwnluDmjBdKL0lzdBQak4YTU0ZNwwk%2Bq8ndd%2FYWmcToSaSvelcC4z1Uh1Vq7yWd0HGHY5%2BQ2zu9%2B9Cm88AkM8PfEsva%2BGi4EN&X-Amz-Signature=d938a2a42a1351c8958f6891525160ee2456cc7ee32e5214dde028e27bf5793c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

