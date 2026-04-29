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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQEHVN2W%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQD4E12VrzMI1EM7cZduWsOP3fYSPGzwVfqYC%2BsBjHZeygIhAJaI380WrvTPA%2FdwKYxdfk1ieyUpeWvHb9dcIs1IcXikKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxjUli7%2F4FeSK1jfDgq3ANRhd0crx9nl4HvvFBeHNp73%2Fv2lVo5e6nij8gVDJW%2BuzZAOZt7E13cDT8wnB1OCDJoVJeeEDP9sK8id4NJvrvcbPdgD%2BSCtF%2BfUWfRkMbjyAE5Q7AixuQ2Vh1jsFuBqWSKT0G19j4jwWEuOml97HzWNrm%2FpX4DFUD4rWNYECt0hakSnRShqAZZ%2Bhgkoio7p%2F5DMIFmiHFKEhlSoCab%2Bm0ssEj2ASJN1cE5Dtel1182pVbVg%2Bblg38S84XK9mo1CB%2BKbhmIsojr9Ss8Bca3L7awy1Dl3mGGivIOnumMoFjs6%2BeZtx92NEr2STOmjMR84bUddDt4QOvUt%2FGWQneDHHrTlQLhNUy9AWyvi%2F1OBslsZWZL5yPGsnrLRveVFEFrqJvuMqZagBLqyCbaJAei2CC5HfLoNtK%2BJxlWrku0ZfoiWPAQ6aQJCaHpHpO%2BmaqBXkXKuV6ja853JkdeOuH6EnlGhfTdwXJ0Vxwru7vFU5F87FODNALYXt5OpqKGeXC%2BgONAGhxellBEGAdlKPFvu7MqJKwINbnFA74y%2B5jFBPei%2B6D%2Fu3tGAdYsZTL7dk0gx3aLe6yZKGpMORNGf1QeCE6ifvTL66uvIOlnCbQbMO6krjGTeuOux6gMYceUajD%2B7cXPBjqkAT0JTbeolJVn6SvIcWJK8JV6fGc%2Bieb5G%2BTsOloU0c%2Bm360stF665bNeo23IZJ4%2F1clqpFQr8%2BO7i0Rg%2FXqsw9LHb%2B3E5po%2FxCVWJiMY95pdegYK6km9mCmzcg9D4z4Z2vWXRGYjJJciHfqwukh7Kk8LUzO4uLRk42mkKzpPJUU0%2BvLEmHjWkFCq58ZmKgLTofuWp0%2BIGVX2CPTk7x18deyFwprk&X-Amz-Signature=66a1c13a1aa7c3ff6674ebf8ad1f1486f4cbf85331eb27b9557542fb6ff9426b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQEHVN2W%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQD4E12VrzMI1EM7cZduWsOP3fYSPGzwVfqYC%2BsBjHZeygIhAJaI380WrvTPA%2FdwKYxdfk1ieyUpeWvHb9dcIs1IcXikKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxjUli7%2F4FeSK1jfDgq3ANRhd0crx9nl4HvvFBeHNp73%2Fv2lVo5e6nij8gVDJW%2BuzZAOZt7E13cDT8wnB1OCDJoVJeeEDP9sK8id4NJvrvcbPdgD%2BSCtF%2BfUWfRkMbjyAE5Q7AixuQ2Vh1jsFuBqWSKT0G19j4jwWEuOml97HzWNrm%2FpX4DFUD4rWNYECt0hakSnRShqAZZ%2Bhgkoio7p%2F5DMIFmiHFKEhlSoCab%2Bm0ssEj2ASJN1cE5Dtel1182pVbVg%2Bblg38S84XK9mo1CB%2BKbhmIsojr9Ss8Bca3L7awy1Dl3mGGivIOnumMoFjs6%2BeZtx92NEr2STOmjMR84bUddDt4QOvUt%2FGWQneDHHrTlQLhNUy9AWyvi%2F1OBslsZWZL5yPGsnrLRveVFEFrqJvuMqZagBLqyCbaJAei2CC5HfLoNtK%2BJxlWrku0ZfoiWPAQ6aQJCaHpHpO%2BmaqBXkXKuV6ja853JkdeOuH6EnlGhfTdwXJ0Vxwru7vFU5F87FODNALYXt5OpqKGeXC%2BgONAGhxellBEGAdlKPFvu7MqJKwINbnFA74y%2B5jFBPei%2B6D%2Fu3tGAdYsZTL7dk0gx3aLe6yZKGpMORNGf1QeCE6ifvTL66uvIOlnCbQbMO6krjGTeuOux6gMYceUajD%2B7cXPBjqkAT0JTbeolJVn6SvIcWJK8JV6fGc%2Bieb5G%2BTsOloU0c%2Bm360stF665bNeo23IZJ4%2F1clqpFQr8%2BO7i0Rg%2FXqsw9LHb%2B3E5po%2FxCVWJiMY95pdegYK6km9mCmzcg9D4z4Z2vWXRGYjJJciHfqwukh7Kk8LUzO4uLRk42mkKzpPJUU0%2BvLEmHjWkFCq58ZmKgLTofuWp0%2BIGVX2CPTk7x18deyFwprk&X-Amz-Signature=3263f1119c87cd463f10e9c2811127c7165a0900f18f6b7358f84f8a2ffda6f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









