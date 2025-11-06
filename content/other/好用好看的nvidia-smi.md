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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7MIM3TP%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T021006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBng1M4JvadTTqFtwGXveqlG8UrxlPMpdPxF2RmvbcNhAiAjlRJUKOeDl76dL98hdYrVyNgKhz2gfZ5K6DPrtCBMvSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRRBFFV%2FcB3LewXjGKtwD7IDlph3t8dz9%2Bfzfn8vgaHnATL5XjKK6TJqV1xC8Mf7MxxzjvAm%2Fv83lUxiR2PjwT27tDwWDDjEHE24wj0DNZdxJjBg%2B7ziX%2BuHZ%2FUDJlL1wrkpqGhdDzlDv6oUj5zPQt37pLU63tPS6bEmU8SG6eq0Md5xqBzcmAfjZPKhELDXKicnoU2mwM%2F%2FK4XjU4VDz0D2%2BdK8yYvciTsJtWHTIpsx4dT1WZCciwr85G%2BkLNIZEmkzSvRBdz9m9UrMnHP80ixd8aRVKDidH08ASuHWKEA0ENaP3M5o69QvLzSCOlTyhXrgmOmmiIV3B4pAcaIcbggAU4ZT0QUNakeGwdyUPhk2EGyc93ogAUiMU8NGAJnlOm8mg4rVjBiE2OnhJS%2F8WqVeWy487cqAe4bOqktIUdq73Jo%2B1ZvfOeRdZqxKrruhVadviKfZ7rWw1%2FWPEEHXCfz1Yy4wxDMnv1qS%2FyqbcZ02OUtDbr%2FUmjiPX37gVSyJ3XPcnCpQKp2fGcD3xHnhYiBC6WdWdsvTdQkI349IUwAsfzXsrWly3m5VoaAUE11cwmblM2%2BqtWdvwcSc7I6EB0X4hgvsZ5BP4xP4uTwCe8JXnyiFcP3M1acTFox4yttQVFZpbUgaFX9BnY0kw%2B%2FGvyAY6pgF79vMb5QirDoZ3v7CZfdZ%2FjTMSb2VSi96O1DQx3ka15dl2eb4SmoLwf3FtQLluQcVb0Rd6s1A7gUnNLU%2FcXnT4IK3M5Fj4MNbnLnjRp4AZ1zDUl%2FqO8ZxD6U7CLnyADQlc2zCBg%2BfHnRoRtZn1Jlq5fosjU5EAMMri2Pt%2BkSCV2OUXyu3QR6Z%2F4aZX3vD8EvxSu%2F8HLXE8GgEkHkQFfTax2b%2BF4V3N&X-Amz-Signature=88c9ce78bb9b57f36bedaa7fd524ad45f51f8bbead98747f8e83c1a88c441a5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7MIM3TP%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T021006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBng1M4JvadTTqFtwGXveqlG8UrxlPMpdPxF2RmvbcNhAiAjlRJUKOeDl76dL98hdYrVyNgKhz2gfZ5K6DPrtCBMvSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRRBFFV%2FcB3LewXjGKtwD7IDlph3t8dz9%2Bfzfn8vgaHnATL5XjKK6TJqV1xC8Mf7MxxzjvAm%2Fv83lUxiR2PjwT27tDwWDDjEHE24wj0DNZdxJjBg%2B7ziX%2BuHZ%2FUDJlL1wrkpqGhdDzlDv6oUj5zPQt37pLU63tPS6bEmU8SG6eq0Md5xqBzcmAfjZPKhELDXKicnoU2mwM%2F%2FK4XjU4VDz0D2%2BdK8yYvciTsJtWHTIpsx4dT1WZCciwr85G%2BkLNIZEmkzSvRBdz9m9UrMnHP80ixd8aRVKDidH08ASuHWKEA0ENaP3M5o69QvLzSCOlTyhXrgmOmmiIV3B4pAcaIcbggAU4ZT0QUNakeGwdyUPhk2EGyc93ogAUiMU8NGAJnlOm8mg4rVjBiE2OnhJS%2F8WqVeWy487cqAe4bOqktIUdq73Jo%2B1ZvfOeRdZqxKrruhVadviKfZ7rWw1%2FWPEEHXCfz1Yy4wxDMnv1qS%2FyqbcZ02OUtDbr%2FUmjiPX37gVSyJ3XPcnCpQKp2fGcD3xHnhYiBC6WdWdsvTdQkI349IUwAsfzXsrWly3m5VoaAUE11cwmblM2%2BqtWdvwcSc7I6EB0X4hgvsZ5BP4xP4uTwCe8JXnyiFcP3M1acTFox4yttQVFZpbUgaFX9BnY0kw%2B%2FGvyAY6pgF79vMb5QirDoZ3v7CZfdZ%2FjTMSb2VSi96O1DQx3ka15dl2eb4SmoLwf3FtQLluQcVb0Rd6s1A7gUnNLU%2FcXnT4IK3M5Fj4MNbnLnjRp4AZ1zDUl%2FqO8ZxD6U7CLnyADQlc2zCBg%2BfHnRoRtZn1Jlq5fosjU5EAMMri2Pt%2BkSCV2OUXyu3QR6Z%2F4aZX3vD8EvxSu%2F8HLXE8GgEkHkQFfTax2b%2BF4V3N&X-Amz-Signature=4e52dadae0e392e786ffa7e9582859ff752a23a1dcaf097ad6f60c44eb775c4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









