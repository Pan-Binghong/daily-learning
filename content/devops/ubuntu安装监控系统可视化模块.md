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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPHN27OB%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQCy2M7TfNeg5neDEJseF1CwjkXtYIhaM44%2F%2BfNFvCpMTQIgQzbgsE81E0MSOfTL%2BVyGSI9%2FNCPcNcg49nIrC693pf8qiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNoWDDQAaQNLuSigCrcA8q%2Fda%2B51lo2SBEhi8EN8%2BQQ0Et%2F0nlBC3a2VDPmUuPmmmi9hfAgyX2py%2BN2eZWX2x5MZoSiUXgUFXxBKhR7YYsQTT5VHj%2Fsd%2F5LyzcG6kYwD%2B1S4ST05odSiSXP0%2FcDqby0LwTspeaWGf1wAWUL0iKJX7ITeEwuIALmoNfztoovebCtppbB5ZVf5uFXshwHldIZeptUx2jr6Mth8pp9bipM5olkGXEQM7R3QS9zvRhtkAJiLZcyNLZxzLNfC%2BlgD1pJJKpsjl%2BK9DTV0bdpqu0drGBa2oR9OalSmengHR8nqvgoYvEHbPWWS%2BeqE2VQF1esOuBOfG7ppH5Hs%2BkcQvzkxH%2FJgptRImUvHPt3Ebg80Zwt7qK5Q%2FYdyLjsIFnRBHvFWlTGsVnETnCptwTTcAeY5WdJd3sRTDGHo5qaZ5JiFf8n6xuR4KETbyNBCYWDgTxPZ83%2FXLkZw6KVxDtr%2BXna22S7a%2F3AMDvC1bn7baLw9KWW6ol129k5qC3gzkrrtQ72m8oYstIlsIRHxPnD1TZlIgBin%2FfJC5w3aD30aUiZcGTzsMVwGXaBwvw4nOB91vkxcovVdvZ0YKiX6PVNqUYb%2BVeF29LQsdmK8FdwtR%2FySv0JYyN8gCIAH7tYMJPAv8wGOqUBkMGSBPXjrN6DDp2iKQ10baw%2FrTLf9vPU30aN5YykQvY3LyLDJuuAem%2F79XfHVmPZsskhcFm86WUKkjcvxoSvWANgRM%2BHlG54XIKShyCcMmDzPB1NRNDgrb2NGqwTo1LEdH4WLCmQHVaWZQstHJG2Beh6pugB3C1GUY1WnWEnm3v3t7aUBAtfofYKU%2FQ9AxOhXzvJSgonn5IPEiETT4xzgGBmos6O&X-Amz-Signature=0e1d48095c0eeea90d48519d7a6036cf3483583e3cdce3649a1dfbde4ad170ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPHN27OB%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQCy2M7TfNeg5neDEJseF1CwjkXtYIhaM44%2F%2BfNFvCpMTQIgQzbgsE81E0MSOfTL%2BVyGSI9%2FNCPcNcg49nIrC693pf8qiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNoWDDQAaQNLuSigCrcA8q%2Fda%2B51lo2SBEhi8EN8%2BQQ0Et%2F0nlBC3a2VDPmUuPmmmi9hfAgyX2py%2BN2eZWX2x5MZoSiUXgUFXxBKhR7YYsQTT5VHj%2Fsd%2F5LyzcG6kYwD%2B1S4ST05odSiSXP0%2FcDqby0LwTspeaWGf1wAWUL0iKJX7ITeEwuIALmoNfztoovebCtppbB5ZVf5uFXshwHldIZeptUx2jr6Mth8pp9bipM5olkGXEQM7R3QS9zvRhtkAJiLZcyNLZxzLNfC%2BlgD1pJJKpsjl%2BK9DTV0bdpqu0drGBa2oR9OalSmengHR8nqvgoYvEHbPWWS%2BeqE2VQF1esOuBOfG7ppH5Hs%2BkcQvzkxH%2FJgptRImUvHPt3Ebg80Zwt7qK5Q%2FYdyLjsIFnRBHvFWlTGsVnETnCptwTTcAeY5WdJd3sRTDGHo5qaZ5JiFf8n6xuR4KETbyNBCYWDgTxPZ83%2FXLkZw6KVxDtr%2BXna22S7a%2F3AMDvC1bn7baLw9KWW6ol129k5qC3gzkrrtQ72m8oYstIlsIRHxPnD1TZlIgBin%2FfJC5w3aD30aUiZcGTzsMVwGXaBwvw4nOB91vkxcovVdvZ0YKiX6PVNqUYb%2BVeF29LQsdmK8FdwtR%2FySv0JYyN8gCIAH7tYMJPAv8wGOqUBkMGSBPXjrN6DDp2iKQ10baw%2FrTLf9vPU30aN5YykQvY3LyLDJuuAem%2F79XfHVmPZsskhcFm86WUKkjcvxoSvWANgRM%2BHlG54XIKShyCcMmDzPB1NRNDgrb2NGqwTo1LEdH4WLCmQHVaWZQstHJG2Beh6pugB3C1GUY1WnWEnm3v3t7aUBAtfofYKU%2FQ9AxOhXzvJSgonn5IPEiETT4xzgGBmos6O&X-Amz-Signature=b4f4db0359175c2fda138d2f1d3e47353a9551b4f74d341aeca8d7dc13d14f1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPHN27OB%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQCy2M7TfNeg5neDEJseF1CwjkXtYIhaM44%2F%2BfNFvCpMTQIgQzbgsE81E0MSOfTL%2BVyGSI9%2FNCPcNcg49nIrC693pf8qiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNoWDDQAaQNLuSigCrcA8q%2Fda%2B51lo2SBEhi8EN8%2BQQ0Et%2F0nlBC3a2VDPmUuPmmmi9hfAgyX2py%2BN2eZWX2x5MZoSiUXgUFXxBKhR7YYsQTT5VHj%2Fsd%2F5LyzcG6kYwD%2B1S4ST05odSiSXP0%2FcDqby0LwTspeaWGf1wAWUL0iKJX7ITeEwuIALmoNfztoovebCtppbB5ZVf5uFXshwHldIZeptUx2jr6Mth8pp9bipM5olkGXEQM7R3QS9zvRhtkAJiLZcyNLZxzLNfC%2BlgD1pJJKpsjl%2BK9DTV0bdpqu0drGBa2oR9OalSmengHR8nqvgoYvEHbPWWS%2BeqE2VQF1esOuBOfG7ppH5Hs%2BkcQvzkxH%2FJgptRImUvHPt3Ebg80Zwt7qK5Q%2FYdyLjsIFnRBHvFWlTGsVnETnCptwTTcAeY5WdJd3sRTDGHo5qaZ5JiFf8n6xuR4KETbyNBCYWDgTxPZ83%2FXLkZw6KVxDtr%2BXna22S7a%2F3AMDvC1bn7baLw9KWW6ol129k5qC3gzkrrtQ72m8oYstIlsIRHxPnD1TZlIgBin%2FfJC5w3aD30aUiZcGTzsMVwGXaBwvw4nOB91vkxcovVdvZ0YKiX6PVNqUYb%2BVeF29LQsdmK8FdwtR%2FySv0JYyN8gCIAH7tYMJPAv8wGOqUBkMGSBPXjrN6DDp2iKQ10baw%2FrTLf9vPU30aN5YykQvY3LyLDJuuAem%2F79XfHVmPZsskhcFm86WUKkjcvxoSvWANgRM%2BHlG54XIKShyCcMmDzPB1NRNDgrb2NGqwTo1LEdH4WLCmQHVaWZQstHJG2Beh6pugB3C1GUY1WnWEnm3v3t7aUBAtfofYKU%2FQ9AxOhXzvJSgonn5IPEiETT4xzgGBmos6O&X-Amz-Signature=ca4189d9187a2a4fec40394a11a252c8c87fc7a28edfa8128b39ef5656bc0b64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPHN27OB%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQCy2M7TfNeg5neDEJseF1CwjkXtYIhaM44%2F%2BfNFvCpMTQIgQzbgsE81E0MSOfTL%2BVyGSI9%2FNCPcNcg49nIrC693pf8qiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNoWDDQAaQNLuSigCrcA8q%2Fda%2B51lo2SBEhi8EN8%2BQQ0Et%2F0nlBC3a2VDPmUuPmmmi9hfAgyX2py%2BN2eZWX2x5MZoSiUXgUFXxBKhR7YYsQTT5VHj%2Fsd%2F5LyzcG6kYwD%2B1S4ST05odSiSXP0%2FcDqby0LwTspeaWGf1wAWUL0iKJX7ITeEwuIALmoNfztoovebCtppbB5ZVf5uFXshwHldIZeptUx2jr6Mth8pp9bipM5olkGXEQM7R3QS9zvRhtkAJiLZcyNLZxzLNfC%2BlgD1pJJKpsjl%2BK9DTV0bdpqu0drGBa2oR9OalSmengHR8nqvgoYvEHbPWWS%2BeqE2VQF1esOuBOfG7ppH5Hs%2BkcQvzkxH%2FJgptRImUvHPt3Ebg80Zwt7qK5Q%2FYdyLjsIFnRBHvFWlTGsVnETnCptwTTcAeY5WdJd3sRTDGHo5qaZ5JiFf8n6xuR4KETbyNBCYWDgTxPZ83%2FXLkZw6KVxDtr%2BXna22S7a%2F3AMDvC1bn7baLw9KWW6ol129k5qC3gzkrrtQ72m8oYstIlsIRHxPnD1TZlIgBin%2FfJC5w3aD30aUiZcGTzsMVwGXaBwvw4nOB91vkxcovVdvZ0YKiX6PVNqUYb%2BVeF29LQsdmK8FdwtR%2FySv0JYyN8gCIAH7tYMJPAv8wGOqUBkMGSBPXjrN6DDp2iKQ10baw%2FrTLf9vPU30aN5YykQvY3LyLDJuuAem%2F79XfHVmPZsskhcFm86WUKkjcvxoSvWANgRM%2BHlG54XIKShyCcMmDzPB1NRNDgrb2NGqwTo1LEdH4WLCmQHVaWZQstHJG2Beh6pugB3C1GUY1WnWEnm3v3t7aUBAtfofYKU%2FQ9AxOhXzvJSgonn5IPEiETT4xzgGBmos6O&X-Amz-Signature=36fea46ad3aba432781e942be688ea38f55eea880f2109d0cbddc1e979678da2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPHN27OB%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQCy2M7TfNeg5neDEJseF1CwjkXtYIhaM44%2F%2BfNFvCpMTQIgQzbgsE81E0MSOfTL%2BVyGSI9%2FNCPcNcg49nIrC693pf8qiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNoWDDQAaQNLuSigCrcA8q%2Fda%2B51lo2SBEhi8EN8%2BQQ0Et%2F0nlBC3a2VDPmUuPmmmi9hfAgyX2py%2BN2eZWX2x5MZoSiUXgUFXxBKhR7YYsQTT5VHj%2Fsd%2F5LyzcG6kYwD%2B1S4ST05odSiSXP0%2FcDqby0LwTspeaWGf1wAWUL0iKJX7ITeEwuIALmoNfztoovebCtppbB5ZVf5uFXshwHldIZeptUx2jr6Mth8pp9bipM5olkGXEQM7R3QS9zvRhtkAJiLZcyNLZxzLNfC%2BlgD1pJJKpsjl%2BK9DTV0bdpqu0drGBa2oR9OalSmengHR8nqvgoYvEHbPWWS%2BeqE2VQF1esOuBOfG7ppH5Hs%2BkcQvzkxH%2FJgptRImUvHPt3Ebg80Zwt7qK5Q%2FYdyLjsIFnRBHvFWlTGsVnETnCptwTTcAeY5WdJd3sRTDGHo5qaZ5JiFf8n6xuR4KETbyNBCYWDgTxPZ83%2FXLkZw6KVxDtr%2BXna22S7a%2F3AMDvC1bn7baLw9KWW6ol129k5qC3gzkrrtQ72m8oYstIlsIRHxPnD1TZlIgBin%2FfJC5w3aD30aUiZcGTzsMVwGXaBwvw4nOB91vkxcovVdvZ0YKiX6PVNqUYb%2BVeF29LQsdmK8FdwtR%2FySv0JYyN8gCIAH7tYMJPAv8wGOqUBkMGSBPXjrN6DDp2iKQ10baw%2FrTLf9vPU30aN5YykQvY3LyLDJuuAem%2F79XfHVmPZsskhcFm86WUKkjcvxoSvWANgRM%2BHlG54XIKShyCcMmDzPB1NRNDgrb2NGqwTo1LEdH4WLCmQHVaWZQstHJG2Beh6pugB3C1GUY1WnWEnm3v3t7aUBAtfofYKU%2FQ9AxOhXzvJSgonn5IPEiETT4xzgGBmos6O&X-Amz-Signature=d3e9e9fdc851d585036ef2819beff8ae1fd4a12f3a11eb8656a45019ed631c5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPHN27OB%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQCy2M7TfNeg5neDEJseF1CwjkXtYIhaM44%2F%2BfNFvCpMTQIgQzbgsE81E0MSOfTL%2BVyGSI9%2FNCPcNcg49nIrC693pf8qiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNoWDDQAaQNLuSigCrcA8q%2Fda%2B51lo2SBEhi8EN8%2BQQ0Et%2F0nlBC3a2VDPmUuPmmmi9hfAgyX2py%2BN2eZWX2x5MZoSiUXgUFXxBKhR7YYsQTT5VHj%2Fsd%2F5LyzcG6kYwD%2B1S4ST05odSiSXP0%2FcDqby0LwTspeaWGf1wAWUL0iKJX7ITeEwuIALmoNfztoovebCtppbB5ZVf5uFXshwHldIZeptUx2jr6Mth8pp9bipM5olkGXEQM7R3QS9zvRhtkAJiLZcyNLZxzLNfC%2BlgD1pJJKpsjl%2BK9DTV0bdpqu0drGBa2oR9OalSmengHR8nqvgoYvEHbPWWS%2BeqE2VQF1esOuBOfG7ppH5Hs%2BkcQvzkxH%2FJgptRImUvHPt3Ebg80Zwt7qK5Q%2FYdyLjsIFnRBHvFWlTGsVnETnCptwTTcAeY5WdJd3sRTDGHo5qaZ5JiFf8n6xuR4KETbyNBCYWDgTxPZ83%2FXLkZw6KVxDtr%2BXna22S7a%2F3AMDvC1bn7baLw9KWW6ol129k5qC3gzkrrtQ72m8oYstIlsIRHxPnD1TZlIgBin%2FfJC5w3aD30aUiZcGTzsMVwGXaBwvw4nOB91vkxcovVdvZ0YKiX6PVNqUYb%2BVeF29LQsdmK8FdwtR%2FySv0JYyN8gCIAH7tYMJPAv8wGOqUBkMGSBPXjrN6DDp2iKQ10baw%2FrTLf9vPU30aN5YykQvY3LyLDJuuAem%2F79XfHVmPZsskhcFm86WUKkjcvxoSvWANgRM%2BHlG54XIKShyCcMmDzPB1NRNDgrb2NGqwTo1LEdH4WLCmQHVaWZQstHJG2Beh6pugB3C1GUY1WnWEnm3v3t7aUBAtfofYKU%2FQ9AxOhXzvJSgonn5IPEiETT4xzgGBmos6O&X-Amz-Signature=f4cdaa114a9fe199dad2328b08c97017b44c533b10368a527fa4966d554820c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPHN27OB%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQCy2M7TfNeg5neDEJseF1CwjkXtYIhaM44%2F%2BfNFvCpMTQIgQzbgsE81E0MSOfTL%2BVyGSI9%2FNCPcNcg49nIrC693pf8qiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNoWDDQAaQNLuSigCrcA8q%2Fda%2B51lo2SBEhi8EN8%2BQQ0Et%2F0nlBC3a2VDPmUuPmmmi9hfAgyX2py%2BN2eZWX2x5MZoSiUXgUFXxBKhR7YYsQTT5VHj%2Fsd%2F5LyzcG6kYwD%2B1S4ST05odSiSXP0%2FcDqby0LwTspeaWGf1wAWUL0iKJX7ITeEwuIALmoNfztoovebCtppbB5ZVf5uFXshwHldIZeptUx2jr6Mth8pp9bipM5olkGXEQM7R3QS9zvRhtkAJiLZcyNLZxzLNfC%2BlgD1pJJKpsjl%2BK9DTV0bdpqu0drGBa2oR9OalSmengHR8nqvgoYvEHbPWWS%2BeqE2VQF1esOuBOfG7ppH5Hs%2BkcQvzkxH%2FJgptRImUvHPt3Ebg80Zwt7qK5Q%2FYdyLjsIFnRBHvFWlTGsVnETnCptwTTcAeY5WdJd3sRTDGHo5qaZ5JiFf8n6xuR4KETbyNBCYWDgTxPZ83%2FXLkZw6KVxDtr%2BXna22S7a%2F3AMDvC1bn7baLw9KWW6ol129k5qC3gzkrrtQ72m8oYstIlsIRHxPnD1TZlIgBin%2FfJC5w3aD30aUiZcGTzsMVwGXaBwvw4nOB91vkxcovVdvZ0YKiX6PVNqUYb%2BVeF29LQsdmK8FdwtR%2FySv0JYyN8gCIAH7tYMJPAv8wGOqUBkMGSBPXjrN6DDp2iKQ10baw%2FrTLf9vPU30aN5YykQvY3LyLDJuuAem%2F79XfHVmPZsskhcFm86WUKkjcvxoSvWANgRM%2BHlG54XIKShyCcMmDzPB1NRNDgrb2NGqwTo1LEdH4WLCmQHVaWZQstHJG2Beh6pugB3C1GUY1WnWEnm3v3t7aUBAtfofYKU%2FQ9AxOhXzvJSgonn5IPEiETT4xzgGBmos6O&X-Amz-Signature=380e1b0375fe73f00ce8483b9feaa2f5127b3422c789c1219832e598be134f28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

