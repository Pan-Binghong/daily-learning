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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HFM6YJL%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T033033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCdpF5c%2Bi1YFEea47tW6v1lkNjyijJ%2BAe4JRoznCQuZXQIhAP0o%2BpSYFjsXO2nBJzJDWERd8IsD88VqaDIGszA3k%2BP0KogECNr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGa15K%2BmglZt58pkUq3ANJ54Bbn4QbtpmHcAl%2B%2F1htYDai2ZfbUkxX2ip%2Banb29xTqmf92AGu5nA2m9qCAa8HVm3LUDPsFG6612IMNzikxU%2BBoXrlwrxeyAq83p2AW9apUYmvO2PI%2By6wqmgxpv2olutFGLFPsrD%2F%2Fhmv7xr0wdxAgxX6fSLInoLhGbg616DdPVGQ1VIDownbl1cHt%2Bnf%2FPDXMvTdw5F2o1A4Uv1o4dpI8H%2Bhxaa5RBu2dgwONhOqbkRJZsgkkyAPpYERdnCpl59KFFCNFdiF3UhQeZ9E6mKo%2BkNvBDRFhvkJFK0xIP1wUthKB8EQ5HxJueUQpntuAp6GaBy8CBIn4Z57ya3A71AhDMoJdfsyT57t6qZioA%2F2eWDbqn04N9uVqtJxWpb4DkRTDl38RS5u20Dohlc1opkvyal4WCesz%2Bgk9Iup2JaeTeHrltK8GiN%2B5j1QCOoGP8X6wTiLm8%2BMSLMshOncKGUlktljEcY3WVHiY0LY56BXp1%2FogFusecAKn9DvWusBrs5R80N0lIVy4APQ5ryfGmg9T0J59Aju1dnKawjoRAl6wWyxaGsugEAmo1%2FkC41EBvQFuVfQ78vaaQ5%2FleMpB%2Fvf%2FZJavhwlTHnCiLgA8X312GuGpLF3mcOHX%2FzDez6jNBjqkAeBE7EOw3bIa3XdLNGm7LFHBfZDwTeT8IQHbnPjVYRE6IzE%2BnhH%2BSgPnCwwqpNqXf%2BOS7kVtHiadQY2qrWeatuDUdXRk8QKdWWZnEh6VfydZM0SDYSCoQKOKuJ%2BG%2BJuYw1y1Ro9%2Bi36CEB4pJr5GEXrSAoaWd0grkNmgZ%2BpXLuu4qCrEfgkQ3LoOVj2u4HfWIhI0MAGMU7ULhQaD1dcZxNhcYzus&X-Amz-Signature=0a8b0e1abf3a15ec82b0207044a5d4f53e1f2c0adc11ead5cb80e92093721e0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HFM6YJL%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T033033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCdpF5c%2Bi1YFEea47tW6v1lkNjyijJ%2BAe4JRoznCQuZXQIhAP0o%2BpSYFjsXO2nBJzJDWERd8IsD88VqaDIGszA3k%2BP0KogECNr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGa15K%2BmglZt58pkUq3ANJ54Bbn4QbtpmHcAl%2B%2F1htYDai2ZfbUkxX2ip%2Banb29xTqmf92AGu5nA2m9qCAa8HVm3LUDPsFG6612IMNzikxU%2BBoXrlwrxeyAq83p2AW9apUYmvO2PI%2By6wqmgxpv2olutFGLFPsrD%2F%2Fhmv7xr0wdxAgxX6fSLInoLhGbg616DdPVGQ1VIDownbl1cHt%2Bnf%2FPDXMvTdw5F2o1A4Uv1o4dpI8H%2Bhxaa5RBu2dgwONhOqbkRJZsgkkyAPpYERdnCpl59KFFCNFdiF3UhQeZ9E6mKo%2BkNvBDRFhvkJFK0xIP1wUthKB8EQ5HxJueUQpntuAp6GaBy8CBIn4Z57ya3A71AhDMoJdfsyT57t6qZioA%2F2eWDbqn04N9uVqtJxWpb4DkRTDl38RS5u20Dohlc1opkvyal4WCesz%2Bgk9Iup2JaeTeHrltK8GiN%2B5j1QCOoGP8X6wTiLm8%2BMSLMshOncKGUlktljEcY3WVHiY0LY56BXp1%2FogFusecAKn9DvWusBrs5R80N0lIVy4APQ5ryfGmg9T0J59Aju1dnKawjoRAl6wWyxaGsugEAmo1%2FkC41EBvQFuVfQ78vaaQ5%2FleMpB%2Fvf%2FZJavhwlTHnCiLgA8X312GuGpLF3mcOHX%2FzDez6jNBjqkAeBE7EOw3bIa3XdLNGm7LFHBfZDwTeT8IQHbnPjVYRE6IzE%2BnhH%2BSgPnCwwqpNqXf%2BOS7kVtHiadQY2qrWeatuDUdXRk8QKdWWZnEh6VfydZM0SDYSCoQKOKuJ%2BG%2BJuYw1y1Ro9%2Bi36CEB4pJr5GEXrSAoaWd0grkNmgZ%2BpXLuu4qCrEfgkQ3LoOVj2u4HfWIhI0MAGMU7ULhQaD1dcZxNhcYzus&X-Amz-Signature=ea689fe3e60f2bb1f7ecf49f01bc2873370bb0fa464644224fb87ad7182a6645&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









