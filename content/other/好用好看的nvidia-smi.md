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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW2TXZVD%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQCH8Bx340ZtfmvRVRv52xf7p1C5ECkc03M%2BXtHSUyPAqwIgKRo%2BDMc%2B4QreL3TKclAeGpt0Bz0S0D%2FdJgAOmIp525wq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDHi7MduG811OhyP3lyrcAx%2B6V3tm2a41o2nOvTKiKYZ5evVoKGBDG1i6axyOu7n90SYYTYoKbG21oX95TmycMIbP42I8BTvpbd%2Bz2eLJN1xn4G%2F%2Fi97SW61z0gLJuLFgJf5Xte4MNCIDucPGLgfpo3XLulR3TFXg9s%2FaWtJRMd9vxeW2DZZA1x7bs0UTZxryO8wSEchry0w%2Fc9lkYLm8Q7DLb0gpgiCF7vjM7Q52sgWvy6LnNi%2BWJkWeRx0CiM4BxAt%2FbZRkrd5Av9A6veNeIE4%2F7A5kS2CTs8kiH1XkHxqKSHQxCwMTvjtG0JxHZ4rcEm1yUc3WBjFf75Gw9aADnwsr6V%2BlNFF52BNRJrBD5bkTfwrvmqjxjbGwCJhb8ZYmzl8tQI1cLLvoF77w4d2Yvg54OEAHbHxQx5xRohUcLRmLSDuk2PdkCfh9FtYdknNpa78tmKXtd8WXB%2Fm3M%2B2No1NRVExFTVwvotQcdUGnSpm1M2rYshe7JQ8P2NuQuoQOlHXCMfQdWrGNGMjnHu2GluolERDo0VXOGjqbhjQkDvO6CVaJxdCbnGZSQJ7%2BIeJupszT8axBMmcHuyEwRdYLyCwVe96TCkZTcpNTcqckkZf3naw18jkX%2Fr9pwensfu8aFbLpEyOHhMfWOwG4MNCPnMsGOqUBH5jhjlkp302cFthM71bIQ%2FN2nhgiJq8Y%2FSgia1OioqGQK%2FccS9RwzJ3KVedx0fDzmaBXF4FlPBkAPVu2Lv5JWXdY3NQUZJyhyjhA4Knf7JERz9vsph2EtHEiF%2Bn4PvlRmAIw3PExXTXHqKgvifhJBNfsMm9nJM7YfHAyRUDkOOQ5ieekxVc%2Fp48TjyOtlGpO9cW46lti4yGTPIjblK6Ok%2BWCBEdQ&X-Amz-Signature=7a8513da234fd5b651aae9f1bd927a01c5b240e0d6e1233d14aa5e77c85092dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW2TXZVD%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQCH8Bx340ZtfmvRVRv52xf7p1C5ECkc03M%2BXtHSUyPAqwIgKRo%2BDMc%2B4QreL3TKclAeGpt0Bz0S0D%2FdJgAOmIp525wq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDHi7MduG811OhyP3lyrcAx%2B6V3tm2a41o2nOvTKiKYZ5evVoKGBDG1i6axyOu7n90SYYTYoKbG21oX95TmycMIbP42I8BTvpbd%2Bz2eLJN1xn4G%2F%2Fi97SW61z0gLJuLFgJf5Xte4MNCIDucPGLgfpo3XLulR3TFXg9s%2FaWtJRMd9vxeW2DZZA1x7bs0UTZxryO8wSEchry0w%2Fc9lkYLm8Q7DLb0gpgiCF7vjM7Q52sgWvy6LnNi%2BWJkWeRx0CiM4BxAt%2FbZRkrd5Av9A6veNeIE4%2F7A5kS2CTs8kiH1XkHxqKSHQxCwMTvjtG0JxHZ4rcEm1yUc3WBjFf75Gw9aADnwsr6V%2BlNFF52BNRJrBD5bkTfwrvmqjxjbGwCJhb8ZYmzl8tQI1cLLvoF77w4d2Yvg54OEAHbHxQx5xRohUcLRmLSDuk2PdkCfh9FtYdknNpa78tmKXtd8WXB%2Fm3M%2B2No1NRVExFTVwvotQcdUGnSpm1M2rYshe7JQ8P2NuQuoQOlHXCMfQdWrGNGMjnHu2GluolERDo0VXOGjqbhjQkDvO6CVaJxdCbnGZSQJ7%2BIeJupszT8axBMmcHuyEwRdYLyCwVe96TCkZTcpNTcqckkZf3naw18jkX%2Fr9pwensfu8aFbLpEyOHhMfWOwG4MNCPnMsGOqUBH5jhjlkp302cFthM71bIQ%2FN2nhgiJq8Y%2FSgia1OioqGQK%2FccS9RwzJ3KVedx0fDzmaBXF4FlPBkAPVu2Lv5JWXdY3NQUZJyhyjhA4Knf7JERz9vsph2EtHEiF%2Bn4PvlRmAIw3PExXTXHqKgvifhJBNfsMm9nJM7YfHAyRUDkOOQ5ieekxVc%2Fp48TjyOtlGpO9cW46lti4yGTPIjblK6Ok%2BWCBEdQ&X-Amz-Signature=70ab9f46286107ae20744d4f61e5184edaf289b4ede9f17844929ec5d77e1815&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









