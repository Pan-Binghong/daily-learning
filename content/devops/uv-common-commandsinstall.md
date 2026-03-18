---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ENXEIDY%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIDmwwdptCs4dL0C%2BT%2Bgz%2FIUbtApP1mwOTww%2FDVJT9KzaAiBSE5xuc8dvpJ5XWLfVWSY4aH3k6a1uWn8sTk80GvGU%2FiqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBgepl5qSARhjX%2FMKKtwD9bgtXaoChPdLR5Ji5FgRC%2Ft0buEDLL9YpRKP8iCMDVhXratwHSPKvbHi8zmC0brTzAdyGbga0X1fPBp%2FdVUiYsx3Keti3WXkvKPkcK8Us3eVbGFBn%2FdhcoUH9KLCYMrtK%2FmznMZyrJI4NlsRO%2Bsz8j%2F8pTXnLGpBEKADXx9OAIBANPAkLbjYznrJcpBxWMGaCOywb6NrHWZO0mke1v1fSKYqZ%2FdZZxZQO9dgF8wbwLuHwn370Z11nbtJoMSdmyS3OH8coXve0IlzorVJA7r5y7yXtoMxb%2BMxd4lioHzlacdWVbuJ%2Fadfkh9IJp%2B4Kvly%2BOE1wwyJTAI9jGQoSLBAv%2F1lQeWzJZucqy%2FpayeK2oALj5Az%2Bucltrv3l5Bqpdbyfi9IcyBi3%2FWVm%2BHf979CJHV3dutZH3D9Rznqk%2B8H1lmmr6tP%2B6Rz8NvaRKwpAC2T985YBZAVNZZYNMLEMr45SF2h44TTsZxWms5kmBKtdicTukaNB1NkVL%2F8CvpDzc0xK22X2cmT1xICiN4Twjzanf73IVk6L8vDZCw65e%2BDwms4qW5fs%2FSZ93dGOAXXXGTP3wvXQJrWHFT6wqR79S0nJYsYbCOASQInQ0dXm70i69h0%2FEXUADiNSZEdqoIwp6fozQY6pgFMsRX9ytAzp7pvXW80iNqDTAgV0s0ho2EMq17VdHZ2sbiQ1NCQyhYWHWChKTWvGIruYNh7j%2Bp%2FPV6%2Bgh4ISv1EvNuqKPMIgHSJKQ%2BPq51d7kAeWJFLbouKp9fHHCTmQwnWrF6O3fD%2BwnCv8J%2Ffrxka%2BpTmrmfuO8upyIJc%2FaFK2yL6EZYK2YKVdj%2BU8UD1tyMv9%2FRH8VNx57AIYkGdTaTns8CPd481&X-Amz-Signature=0e27dde7aa9c7849f46921a4dc487fe30d03c786582cb63d339ce6660c70c255&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ENXEIDY%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIDmwwdptCs4dL0C%2BT%2Bgz%2FIUbtApP1mwOTww%2FDVJT9KzaAiBSE5xuc8dvpJ5XWLfVWSY4aH3k6a1uWn8sTk80GvGU%2FiqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBgepl5qSARhjX%2FMKKtwD9bgtXaoChPdLR5Ji5FgRC%2Ft0buEDLL9YpRKP8iCMDVhXratwHSPKvbHi8zmC0brTzAdyGbga0X1fPBp%2FdVUiYsx3Keti3WXkvKPkcK8Us3eVbGFBn%2FdhcoUH9KLCYMrtK%2FmznMZyrJI4NlsRO%2Bsz8j%2F8pTXnLGpBEKADXx9OAIBANPAkLbjYznrJcpBxWMGaCOywb6NrHWZO0mke1v1fSKYqZ%2FdZZxZQO9dgF8wbwLuHwn370Z11nbtJoMSdmyS3OH8coXve0IlzorVJA7r5y7yXtoMxb%2BMxd4lioHzlacdWVbuJ%2Fadfkh9IJp%2B4Kvly%2BOE1wwyJTAI9jGQoSLBAv%2F1lQeWzJZucqy%2FpayeK2oALj5Az%2Bucltrv3l5Bqpdbyfi9IcyBi3%2FWVm%2BHf979CJHV3dutZH3D9Rznqk%2B8H1lmmr6tP%2B6Rz8NvaRKwpAC2T985YBZAVNZZYNMLEMr45SF2h44TTsZxWms5kmBKtdicTukaNB1NkVL%2F8CvpDzc0xK22X2cmT1xICiN4Twjzanf73IVk6L8vDZCw65e%2BDwms4qW5fs%2FSZ93dGOAXXXGTP3wvXQJrWHFT6wqR79S0nJYsYbCOASQInQ0dXm70i69h0%2FEXUADiNSZEdqoIwp6fozQY6pgFMsRX9ytAzp7pvXW80iNqDTAgV0s0ho2EMq17VdHZ2sbiQ1NCQyhYWHWChKTWvGIruYNh7j%2Bp%2FPV6%2Bgh4ISv1EvNuqKPMIgHSJKQ%2BPq51d7kAeWJFLbouKp9fHHCTmQwnWrF6O3fD%2BwnCv8J%2Ffrxka%2BpTmrmfuO8upyIJc%2FaFK2yL6EZYK2YKVdj%2BU8UD1tyMv9%2FRH8VNx57AIYkGdTaTns8CPd481&X-Amz-Signature=40f86c41b50b9136372b51959c163878f33fcdb5033d975fc3704cc5f2702fd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ENXEIDY%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIDmwwdptCs4dL0C%2BT%2Bgz%2FIUbtApP1mwOTww%2FDVJT9KzaAiBSE5xuc8dvpJ5XWLfVWSY4aH3k6a1uWn8sTk80GvGU%2FiqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBgepl5qSARhjX%2FMKKtwD9bgtXaoChPdLR5Ji5FgRC%2Ft0buEDLL9YpRKP8iCMDVhXratwHSPKvbHi8zmC0brTzAdyGbga0X1fPBp%2FdVUiYsx3Keti3WXkvKPkcK8Us3eVbGFBn%2FdhcoUH9KLCYMrtK%2FmznMZyrJI4NlsRO%2Bsz8j%2F8pTXnLGpBEKADXx9OAIBANPAkLbjYznrJcpBxWMGaCOywb6NrHWZO0mke1v1fSKYqZ%2FdZZxZQO9dgF8wbwLuHwn370Z11nbtJoMSdmyS3OH8coXve0IlzorVJA7r5y7yXtoMxb%2BMxd4lioHzlacdWVbuJ%2Fadfkh9IJp%2B4Kvly%2BOE1wwyJTAI9jGQoSLBAv%2F1lQeWzJZucqy%2FpayeK2oALj5Az%2Bucltrv3l5Bqpdbyfi9IcyBi3%2FWVm%2BHf979CJHV3dutZH3D9Rznqk%2B8H1lmmr6tP%2B6Rz8NvaRKwpAC2T985YBZAVNZZYNMLEMr45SF2h44TTsZxWms5kmBKtdicTukaNB1NkVL%2F8CvpDzc0xK22X2cmT1xICiN4Twjzanf73IVk6L8vDZCw65e%2BDwms4qW5fs%2FSZ93dGOAXXXGTP3wvXQJrWHFT6wqR79S0nJYsYbCOASQInQ0dXm70i69h0%2FEXUADiNSZEdqoIwp6fozQY6pgFMsRX9ytAzp7pvXW80iNqDTAgV0s0ho2EMq17VdHZ2sbiQ1NCQyhYWHWChKTWvGIruYNh7j%2Bp%2FPV6%2Bgh4ISv1EvNuqKPMIgHSJKQ%2BPq51d7kAeWJFLbouKp9fHHCTmQwnWrF6O3fD%2BwnCv8J%2Ffrxka%2BpTmrmfuO8upyIJc%2FaFK2yL6EZYK2YKVdj%2BU8UD1tyMv9%2FRH8VNx57AIYkGdTaTns8CPd481&X-Amz-Signature=03c7b2edb9c0d264a27b5cd1063334a339ca500ace2f773a5bf5d47b734283a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

