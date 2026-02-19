---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
tags:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R23OJACA%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T034058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGnNWSgoxBwQ0t6JFSx4lBNRZECyg%2BnJeevU%2FWEfXSf9AiEA4G2av%2B0IdGKePRiD2lF4kfVvb47Qko6%2F74Xi7r3884Yq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDKWiFQxYDQnmWykHLCrcA%2Bqs1ZyrZlGqiEGJnHpz0znQXr9Uz5NacPxULQ2eHnUC7VGg%2FbJrBb%2BRgRaEYB%2BjRuc8pGzR8uxiA3%2FraRUWDAb3o09Xl9oX23PwgpIdlaHIEStNpA8djy0DbBNDJO%2FA2992ZBnjL8rjDWx38QOUQHd8Zr7d8kgmjgo91o11LoZbpQE6xSTa87EKOs6ULmyeP72qK9odnM%2B9NipCSR0vB6%2F%2BHwxEpNSwWEKWO2ztUHRFFcVrwr115A1CwCamZ5n2YfBw3Y7RRIIp1ysd1eogEq%2FzvmqL6ptyZEnPdQXeBzDW6nTx4sQjOqUu7V8N9R0Mi7FcHkklJAOp3BwMpwPycuQ6ygXgsKhaYkd2Kgf0B%2BhDF1UGre3jqCBtgZevUU792Dhmol8C1P%2BHfmeRjnQ%2FAYVSPnFh%2FVVIUawyNATunhfr%2Bd7jeMNIKCKUq1R2wvOxUQjCOsq%2ByeIhoQh0W9Pf14RifLC4NJWtp2zPlWgTRyKA%2B1zP1%2F1uD1m5zAEZD%2Fj18b5a6hBx1iE0qoxSGsy5kYUP%2Fy2dCXIRAagLF%2FkQsp0hb%2FbxaJWmCwcVyq3CrPQ8Hp9gmZOXf1VMoPfuhFJ14Wuw29cFyRUkYERQk6ujxiqgM86ERxZqc%2BhSQoQnMJ3y2cwGOqUBG36egXsCL%2Bs%2Fx%2FAVk2joM%2B4IUkzEIKEzGyK3l7H8e8CAehYUaHMqSC7B3R24WxzDot5loeH4CEK29sL5%2F2%2FwL4MBTVRFT0GN65bbH4FTRasikg2wTbk4qARUSKjtpwazfXVbsh5SfyGtIODq3orKZDNMb5n8e2V85fW8q1DWD1z%2F9l1bs1SIvJ4tY%2F%2FuJf%2Br3eGmYFrXT0YU195bhXIiDp9Bxoge&X-Amz-Signature=f5b2c1a3868576af219b09510e2aabaeb52b2ab7ea899720c49a7d909a0487ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 安装

```python
pip install nvitop
```

---

## 查看gpu状态

```python
nvitop
```

> 查看更加详细的gpu内容

```python
nvitop -m full
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R23OJACA%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T034058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGnNWSgoxBwQ0t6JFSx4lBNRZECyg%2BnJeevU%2FWEfXSf9AiEA4G2av%2B0IdGKePRiD2lF4kfVvb47Qko6%2F74Xi7r3884Yq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDKWiFQxYDQnmWykHLCrcA%2Bqs1ZyrZlGqiEGJnHpz0znQXr9Uz5NacPxULQ2eHnUC7VGg%2FbJrBb%2BRgRaEYB%2BjRuc8pGzR8uxiA3%2FraRUWDAb3o09Xl9oX23PwgpIdlaHIEStNpA8djy0DbBNDJO%2FA2992ZBnjL8rjDWx38QOUQHd8Zr7d8kgmjgo91o11LoZbpQE6xSTa87EKOs6ULmyeP72qK9odnM%2B9NipCSR0vB6%2F%2BHwxEpNSwWEKWO2ztUHRFFcVrwr115A1CwCamZ5n2YfBw3Y7RRIIp1ysd1eogEq%2FzvmqL6ptyZEnPdQXeBzDW6nTx4sQjOqUu7V8N9R0Mi7FcHkklJAOp3BwMpwPycuQ6ygXgsKhaYkd2Kgf0B%2BhDF1UGre3jqCBtgZevUU792Dhmol8C1P%2BHfmeRjnQ%2FAYVSPnFh%2FVVIUawyNATunhfr%2Bd7jeMNIKCKUq1R2wvOxUQjCOsq%2ByeIhoQh0W9Pf14RifLC4NJWtp2zPlWgTRyKA%2B1zP1%2F1uD1m5zAEZD%2Fj18b5a6hBx1iE0qoxSGsy5kYUP%2Fy2dCXIRAagLF%2FkQsp0hb%2FbxaJWmCwcVyq3CrPQ8Hp9gmZOXf1VMoPfuhFJ14Wuw29cFyRUkYERQk6ujxiqgM86ERxZqc%2BhSQoQnMJ3y2cwGOqUBG36egXsCL%2Bs%2Fx%2FAVk2joM%2B4IUkzEIKEzGyK3l7H8e8CAehYUaHMqSC7B3R24WxzDot5loeH4CEK29sL5%2F2%2FwL4MBTVRFT0GN65bbH4FTRasikg2wTbk4qARUSKjtpwazfXVbsh5SfyGtIODq3orKZDNMb5n8e2V85fW8q1DWD1z%2F9l1bs1SIvJ4tY%2F%2FuJf%2Br3eGmYFrXT0YU195bhXIiDp9Bxoge&X-Amz-Signature=9fcdf5484b056229834edae606f2e0a91e505177620799d212c5a932316ef733&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









