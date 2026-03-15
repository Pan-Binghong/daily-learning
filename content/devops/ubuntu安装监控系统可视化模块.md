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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRQB5W3U%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClSPzfDGDohTnYrjKKgVHV8WBvU6nyZSOMCs%2BCGifq2wIge7GvVSyDfXo%2Bvx%2F7lHkqVcnoek57PfcaRxl4b5dFISYqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPqXUknjYFvAgw7%2FxSrcA34LSgemRO8vvYzaaePdfitNk8hJpkEJrCRk73QMWjsKZNmndJEgE062qtZaKsWLg24WDY%2BS%2BE910RfS2NqWh4jfoJfTk1M4omQTyBXU1ICG1j%2BnZ3uQIiFg8kRX%2Fih%2BJUbUlUuAinbOzx6ou50WXhC4lshMiXo%2Bcyg0SLJRwha3AF3eOhmejFAqPuvzJ8vyVBembjCpj%2FXPc6HqzocUWCPvyUxHEP5AKT1pCYAUJ9qkYBh99g2uknvOag8ahbupGyt%2BbQ5AeplwMAz%2BI1cJOYSNvDCs9xIdBzQirDsLZojgTsBZonC%2BKWkEECShYOSpnaJEsvaXC9Y43eY9NMBYtxaMe9dPi3Ii5JrExASwjFTGKwBzm8E%2FDVUYm2u60EwmV1sA4qmOnBaA0IuRtpq85C8BvZv6f1q%2FBiH9Ls3u%2FBDKKabjCaFUOYaWKabKYk1%2B8aV0sp0kQbHD0BVs9mWRcbIxhn5tvgLKL9Q92iHdSVyOG5rcPR0NVpSb%2FDRYyEzPYPecTqkxqvDespZd3a0dEVpjB2%2FdzyLko9ABJIjazx5w6zEBhkCLGPki92rF7Hsl7hSqlWzFpMucoUnZqCMrx5rcMNmo%2F7Uc%2BOz0zE82QEz63rt3dJZmF8w670BDMLqQ2M0GOqUB%2Br62Isp2x2U5i13sKxtcNSu0afbgI1lHZB%2BjnTKDqi9LfyETE3Lti8KMT9ACEkKhj9xxdstyRZDC%2BxpANasMN6hVxrW3uPq30ev2Y2%2FJhM2w%2BBmKmTlEO%2BlcB%2Fvld70se63kOQB2HU1%2BLhaKLxM8du6tHVat9GpzVpZdlqWj2HFvGczqkKycwNcY4aFtd0DjDcsASv8%2F5RuoIKfyVtMa5omfA8PB&X-Amz-Signature=0611cce5c9f3d6d5a19739692859807a6453c7a917a2be14e99a68202f7439d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRQB5W3U%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClSPzfDGDohTnYrjKKgVHV8WBvU6nyZSOMCs%2BCGifq2wIge7GvVSyDfXo%2Bvx%2F7lHkqVcnoek57PfcaRxl4b5dFISYqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPqXUknjYFvAgw7%2FxSrcA34LSgemRO8vvYzaaePdfitNk8hJpkEJrCRk73QMWjsKZNmndJEgE062qtZaKsWLg24WDY%2BS%2BE910RfS2NqWh4jfoJfTk1M4omQTyBXU1ICG1j%2BnZ3uQIiFg8kRX%2Fih%2BJUbUlUuAinbOzx6ou50WXhC4lshMiXo%2Bcyg0SLJRwha3AF3eOhmejFAqPuvzJ8vyVBembjCpj%2FXPc6HqzocUWCPvyUxHEP5AKT1pCYAUJ9qkYBh99g2uknvOag8ahbupGyt%2BbQ5AeplwMAz%2BI1cJOYSNvDCs9xIdBzQirDsLZojgTsBZonC%2BKWkEECShYOSpnaJEsvaXC9Y43eY9NMBYtxaMe9dPi3Ii5JrExASwjFTGKwBzm8E%2FDVUYm2u60EwmV1sA4qmOnBaA0IuRtpq85C8BvZv6f1q%2FBiH9Ls3u%2FBDKKabjCaFUOYaWKabKYk1%2B8aV0sp0kQbHD0BVs9mWRcbIxhn5tvgLKL9Q92iHdSVyOG5rcPR0NVpSb%2FDRYyEzPYPecTqkxqvDespZd3a0dEVpjB2%2FdzyLko9ABJIjazx5w6zEBhkCLGPki92rF7Hsl7hSqlWzFpMucoUnZqCMrx5rcMNmo%2F7Uc%2BOz0zE82QEz63rt3dJZmF8w670BDMLqQ2M0GOqUB%2Br62Isp2x2U5i13sKxtcNSu0afbgI1lHZB%2BjnTKDqi9LfyETE3Lti8KMT9ACEkKhj9xxdstyRZDC%2BxpANasMN6hVxrW3uPq30ev2Y2%2FJhM2w%2BBmKmTlEO%2BlcB%2Fvld70se63kOQB2HU1%2BLhaKLxM8du6tHVat9GpzVpZdlqWj2HFvGczqkKycwNcY4aFtd0DjDcsASv8%2F5RuoIKfyVtMa5omfA8PB&X-Amz-Signature=7a578d61875e2cc5122cff589fe15ed977ccd9e690948213d4be8a7eff24f1de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRQB5W3U%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClSPzfDGDohTnYrjKKgVHV8WBvU6nyZSOMCs%2BCGifq2wIge7GvVSyDfXo%2Bvx%2F7lHkqVcnoek57PfcaRxl4b5dFISYqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPqXUknjYFvAgw7%2FxSrcA34LSgemRO8vvYzaaePdfitNk8hJpkEJrCRk73QMWjsKZNmndJEgE062qtZaKsWLg24WDY%2BS%2BE910RfS2NqWh4jfoJfTk1M4omQTyBXU1ICG1j%2BnZ3uQIiFg8kRX%2Fih%2BJUbUlUuAinbOzx6ou50WXhC4lshMiXo%2Bcyg0SLJRwha3AF3eOhmejFAqPuvzJ8vyVBembjCpj%2FXPc6HqzocUWCPvyUxHEP5AKT1pCYAUJ9qkYBh99g2uknvOag8ahbupGyt%2BbQ5AeplwMAz%2BI1cJOYSNvDCs9xIdBzQirDsLZojgTsBZonC%2BKWkEECShYOSpnaJEsvaXC9Y43eY9NMBYtxaMe9dPi3Ii5JrExASwjFTGKwBzm8E%2FDVUYm2u60EwmV1sA4qmOnBaA0IuRtpq85C8BvZv6f1q%2FBiH9Ls3u%2FBDKKabjCaFUOYaWKabKYk1%2B8aV0sp0kQbHD0BVs9mWRcbIxhn5tvgLKL9Q92iHdSVyOG5rcPR0NVpSb%2FDRYyEzPYPecTqkxqvDespZd3a0dEVpjB2%2FdzyLko9ABJIjazx5w6zEBhkCLGPki92rF7Hsl7hSqlWzFpMucoUnZqCMrx5rcMNmo%2F7Uc%2BOz0zE82QEz63rt3dJZmF8w670BDMLqQ2M0GOqUB%2Br62Isp2x2U5i13sKxtcNSu0afbgI1lHZB%2BjnTKDqi9LfyETE3Lti8KMT9ACEkKhj9xxdstyRZDC%2BxpANasMN6hVxrW3uPq30ev2Y2%2FJhM2w%2BBmKmTlEO%2BlcB%2Fvld70se63kOQB2HU1%2BLhaKLxM8du6tHVat9GpzVpZdlqWj2HFvGczqkKycwNcY4aFtd0DjDcsASv8%2F5RuoIKfyVtMa5omfA8PB&X-Amz-Signature=af3bc430ad3d76589fcbf95d2b9243dea4abd185514757ac019bfbd4b2f361b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRQB5W3U%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClSPzfDGDohTnYrjKKgVHV8WBvU6nyZSOMCs%2BCGifq2wIge7GvVSyDfXo%2Bvx%2F7lHkqVcnoek57PfcaRxl4b5dFISYqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPqXUknjYFvAgw7%2FxSrcA34LSgemRO8vvYzaaePdfitNk8hJpkEJrCRk73QMWjsKZNmndJEgE062qtZaKsWLg24WDY%2BS%2BE910RfS2NqWh4jfoJfTk1M4omQTyBXU1ICG1j%2BnZ3uQIiFg8kRX%2Fih%2BJUbUlUuAinbOzx6ou50WXhC4lshMiXo%2Bcyg0SLJRwha3AF3eOhmejFAqPuvzJ8vyVBembjCpj%2FXPc6HqzocUWCPvyUxHEP5AKT1pCYAUJ9qkYBh99g2uknvOag8ahbupGyt%2BbQ5AeplwMAz%2BI1cJOYSNvDCs9xIdBzQirDsLZojgTsBZonC%2BKWkEECShYOSpnaJEsvaXC9Y43eY9NMBYtxaMe9dPi3Ii5JrExASwjFTGKwBzm8E%2FDVUYm2u60EwmV1sA4qmOnBaA0IuRtpq85C8BvZv6f1q%2FBiH9Ls3u%2FBDKKabjCaFUOYaWKabKYk1%2B8aV0sp0kQbHD0BVs9mWRcbIxhn5tvgLKL9Q92iHdSVyOG5rcPR0NVpSb%2FDRYyEzPYPecTqkxqvDespZd3a0dEVpjB2%2FdzyLko9ABJIjazx5w6zEBhkCLGPki92rF7Hsl7hSqlWzFpMucoUnZqCMrx5rcMNmo%2F7Uc%2BOz0zE82QEz63rt3dJZmF8w670BDMLqQ2M0GOqUB%2Br62Isp2x2U5i13sKxtcNSu0afbgI1lHZB%2BjnTKDqi9LfyETE3Lti8KMT9ACEkKhj9xxdstyRZDC%2BxpANasMN6hVxrW3uPq30ev2Y2%2FJhM2w%2BBmKmTlEO%2BlcB%2Fvld70se63kOQB2HU1%2BLhaKLxM8du6tHVat9GpzVpZdlqWj2HFvGczqkKycwNcY4aFtd0DjDcsASv8%2F5RuoIKfyVtMa5omfA8PB&X-Amz-Signature=43ba850a5d17cb095dc0712ed945deddaa9b1e5920e6667df8b883c35a520807&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRQB5W3U%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClSPzfDGDohTnYrjKKgVHV8WBvU6nyZSOMCs%2BCGifq2wIge7GvVSyDfXo%2Bvx%2F7lHkqVcnoek57PfcaRxl4b5dFISYqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPqXUknjYFvAgw7%2FxSrcA34LSgemRO8vvYzaaePdfitNk8hJpkEJrCRk73QMWjsKZNmndJEgE062qtZaKsWLg24WDY%2BS%2BE910RfS2NqWh4jfoJfTk1M4omQTyBXU1ICG1j%2BnZ3uQIiFg8kRX%2Fih%2BJUbUlUuAinbOzx6ou50WXhC4lshMiXo%2Bcyg0SLJRwha3AF3eOhmejFAqPuvzJ8vyVBembjCpj%2FXPc6HqzocUWCPvyUxHEP5AKT1pCYAUJ9qkYBh99g2uknvOag8ahbupGyt%2BbQ5AeplwMAz%2BI1cJOYSNvDCs9xIdBzQirDsLZojgTsBZonC%2BKWkEECShYOSpnaJEsvaXC9Y43eY9NMBYtxaMe9dPi3Ii5JrExASwjFTGKwBzm8E%2FDVUYm2u60EwmV1sA4qmOnBaA0IuRtpq85C8BvZv6f1q%2FBiH9Ls3u%2FBDKKabjCaFUOYaWKabKYk1%2B8aV0sp0kQbHD0BVs9mWRcbIxhn5tvgLKL9Q92iHdSVyOG5rcPR0NVpSb%2FDRYyEzPYPecTqkxqvDespZd3a0dEVpjB2%2FdzyLko9ABJIjazx5w6zEBhkCLGPki92rF7Hsl7hSqlWzFpMucoUnZqCMrx5rcMNmo%2F7Uc%2BOz0zE82QEz63rt3dJZmF8w670BDMLqQ2M0GOqUB%2Br62Isp2x2U5i13sKxtcNSu0afbgI1lHZB%2BjnTKDqi9LfyETE3Lti8KMT9ACEkKhj9xxdstyRZDC%2BxpANasMN6hVxrW3uPq30ev2Y2%2FJhM2w%2BBmKmTlEO%2BlcB%2Fvld70se63kOQB2HU1%2BLhaKLxM8du6tHVat9GpzVpZdlqWj2HFvGczqkKycwNcY4aFtd0DjDcsASv8%2F5RuoIKfyVtMa5omfA8PB&X-Amz-Signature=9617fe995bd04251bf77b059e4aa10de14e34fc06ae6b59fa977232fef977fe0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRQB5W3U%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClSPzfDGDohTnYrjKKgVHV8WBvU6nyZSOMCs%2BCGifq2wIge7GvVSyDfXo%2Bvx%2F7lHkqVcnoek57PfcaRxl4b5dFISYqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPqXUknjYFvAgw7%2FxSrcA34LSgemRO8vvYzaaePdfitNk8hJpkEJrCRk73QMWjsKZNmndJEgE062qtZaKsWLg24WDY%2BS%2BE910RfS2NqWh4jfoJfTk1M4omQTyBXU1ICG1j%2BnZ3uQIiFg8kRX%2Fih%2BJUbUlUuAinbOzx6ou50WXhC4lshMiXo%2Bcyg0SLJRwha3AF3eOhmejFAqPuvzJ8vyVBembjCpj%2FXPc6HqzocUWCPvyUxHEP5AKT1pCYAUJ9qkYBh99g2uknvOag8ahbupGyt%2BbQ5AeplwMAz%2BI1cJOYSNvDCs9xIdBzQirDsLZojgTsBZonC%2BKWkEECShYOSpnaJEsvaXC9Y43eY9NMBYtxaMe9dPi3Ii5JrExASwjFTGKwBzm8E%2FDVUYm2u60EwmV1sA4qmOnBaA0IuRtpq85C8BvZv6f1q%2FBiH9Ls3u%2FBDKKabjCaFUOYaWKabKYk1%2B8aV0sp0kQbHD0BVs9mWRcbIxhn5tvgLKL9Q92iHdSVyOG5rcPR0NVpSb%2FDRYyEzPYPecTqkxqvDespZd3a0dEVpjB2%2FdzyLko9ABJIjazx5w6zEBhkCLGPki92rF7Hsl7hSqlWzFpMucoUnZqCMrx5rcMNmo%2F7Uc%2BOz0zE82QEz63rt3dJZmF8w670BDMLqQ2M0GOqUB%2Br62Isp2x2U5i13sKxtcNSu0afbgI1lHZB%2BjnTKDqi9LfyETE3Lti8KMT9ACEkKhj9xxdstyRZDC%2BxpANasMN6hVxrW3uPq30ev2Y2%2FJhM2w%2BBmKmTlEO%2BlcB%2Fvld70se63kOQB2HU1%2BLhaKLxM8du6tHVat9GpzVpZdlqWj2HFvGczqkKycwNcY4aFtd0DjDcsASv8%2F5RuoIKfyVtMa5omfA8PB&X-Amz-Signature=38f5f100c9f1064fdb93bf22d64c3570d59f4e2e98165141abed04e6c4955562&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRQB5W3U%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClSPzfDGDohTnYrjKKgVHV8WBvU6nyZSOMCs%2BCGifq2wIge7GvVSyDfXo%2Bvx%2F7lHkqVcnoek57PfcaRxl4b5dFISYqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPqXUknjYFvAgw7%2FxSrcA34LSgemRO8vvYzaaePdfitNk8hJpkEJrCRk73QMWjsKZNmndJEgE062qtZaKsWLg24WDY%2BS%2BE910RfS2NqWh4jfoJfTk1M4omQTyBXU1ICG1j%2BnZ3uQIiFg8kRX%2Fih%2BJUbUlUuAinbOzx6ou50WXhC4lshMiXo%2Bcyg0SLJRwha3AF3eOhmejFAqPuvzJ8vyVBembjCpj%2FXPc6HqzocUWCPvyUxHEP5AKT1pCYAUJ9qkYBh99g2uknvOag8ahbupGyt%2BbQ5AeplwMAz%2BI1cJOYSNvDCs9xIdBzQirDsLZojgTsBZonC%2BKWkEECShYOSpnaJEsvaXC9Y43eY9NMBYtxaMe9dPi3Ii5JrExASwjFTGKwBzm8E%2FDVUYm2u60EwmV1sA4qmOnBaA0IuRtpq85C8BvZv6f1q%2FBiH9Ls3u%2FBDKKabjCaFUOYaWKabKYk1%2B8aV0sp0kQbHD0BVs9mWRcbIxhn5tvgLKL9Q92iHdSVyOG5rcPR0NVpSb%2FDRYyEzPYPecTqkxqvDespZd3a0dEVpjB2%2FdzyLko9ABJIjazx5w6zEBhkCLGPki92rF7Hsl7hSqlWzFpMucoUnZqCMrx5rcMNmo%2F7Uc%2BOz0zE82QEz63rt3dJZmF8w670BDMLqQ2M0GOqUB%2Br62Isp2x2U5i13sKxtcNSu0afbgI1lHZB%2BjnTKDqi9LfyETE3Lti8KMT9ACEkKhj9xxdstyRZDC%2BxpANasMN6hVxrW3uPq30ev2Y2%2FJhM2w%2BBmKmTlEO%2BlcB%2Fvld70se63kOQB2HU1%2BLhaKLxM8du6tHVat9GpzVpZdlqWj2HFvGczqkKycwNcY4aFtd0DjDcsASv8%2F5RuoIKfyVtMa5omfA8PB&X-Amz-Signature=28e5eae4b9de35d1793914edfe2f91ba5062d2f81da0351e1a4d9fbff850c44f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

