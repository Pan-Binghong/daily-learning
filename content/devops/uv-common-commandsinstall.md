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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRA74IMI%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIH8jv1FtjrR1G9HVJcaEjKIGtaoHfTSNABKQDa4rkjC9AiBp34J2sosPM6KOt%2BvkEphqaS44CShMsD5Lh2jkNJ4t5yr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMB%2Bl0H3usuK6iMBydKtwDEnhiDtW62WG%2FCGrGj6y%2B1zrCT5G8RMldAhbk31JFPgJ4d6bNazJjO4IQ9zUelkfhcCU%2BEqv5yROzYJbDGmFFp3UEW0U%2F%2BcIFaLB5Yz0JIacdueL2K9uQRXLeXDbES7zowQXw304PFKKBVK4DxjJcfJqkTn5r3In95%2BQ0BXXZxIg0DRHr99txEEXsftkqVajDP2oBFppOpsUr9MwOmwhfbBvoDypQGV9bm4a%2FNScgbguh2tTv0WrxaW3phnR4vqt1%2F1t0Dxfpo7JsKaMwW2LNudG5hF7rCNx4lsXPOBvC1KajfpRbwuHYIS4WLzfElg%2BvsfX2EgJU3AxKxJl7rUylfgk56FYsgxVVIXqhlv2i2danMAC9C4Rb3v6Ypx6evPKJBmDfjqYpQP1kwiVOroSN7SakXkbG7PEDKFMZtjiEuqqKbIHO62fUYehtFW%2FNZMUvhialCTgTxv3qGvpiMnNQhWCU6LYzoSoqJ8kBvqCKfPGc5xxrUgvem6pzZ8Sn4MLJ8t61SsEpaUw%2FOO%2FzLmdI8Fb2u0cP0hM0j6Qq%2BQjxQ7fl52kIgcfw4p98e1IIof87mP6zEgsgSYg0FfP3XSMVA%2BhfSZizVXm1xLg6jI0cvvKxfSbxgyHawV1PO5Ew%2F7%2BmywY6pgFZZRV8uW7Of9Wxr%2BqvV5Dz%2BGZhYV4udDA%2BH4dU8Xqt%2Fe%2BeEkVZ1l1l%2FdaWASI3dDnYq%2FQHSpdzyFjz2ZB2RnQl37q0NkzP6wl1srGCFlER1yDiK688m0%2FAKtGsCON%2FMmfN07UwFR%2FUDtKZny4GFVp7anmw%2FoQ6JDqTC9TWRsf7GfaojNnXijHMnon9MObEb3Jb5mTKr2dsVTA0Jw12xFVaRwm2qkzS&X-Amz-Signature=512a03e7714a0efd2c3db595526b3165cc201e81cae5c59d48454e9eee852199&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRA74IMI%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIH8jv1FtjrR1G9HVJcaEjKIGtaoHfTSNABKQDa4rkjC9AiBp34J2sosPM6KOt%2BvkEphqaS44CShMsD5Lh2jkNJ4t5yr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMB%2Bl0H3usuK6iMBydKtwDEnhiDtW62WG%2FCGrGj6y%2B1zrCT5G8RMldAhbk31JFPgJ4d6bNazJjO4IQ9zUelkfhcCU%2BEqv5yROzYJbDGmFFp3UEW0U%2F%2BcIFaLB5Yz0JIacdueL2K9uQRXLeXDbES7zowQXw304PFKKBVK4DxjJcfJqkTn5r3In95%2BQ0BXXZxIg0DRHr99txEEXsftkqVajDP2oBFppOpsUr9MwOmwhfbBvoDypQGV9bm4a%2FNScgbguh2tTv0WrxaW3phnR4vqt1%2F1t0Dxfpo7JsKaMwW2LNudG5hF7rCNx4lsXPOBvC1KajfpRbwuHYIS4WLzfElg%2BvsfX2EgJU3AxKxJl7rUylfgk56FYsgxVVIXqhlv2i2danMAC9C4Rb3v6Ypx6evPKJBmDfjqYpQP1kwiVOroSN7SakXkbG7PEDKFMZtjiEuqqKbIHO62fUYehtFW%2FNZMUvhialCTgTxv3qGvpiMnNQhWCU6LYzoSoqJ8kBvqCKfPGc5xxrUgvem6pzZ8Sn4MLJ8t61SsEpaUw%2FOO%2FzLmdI8Fb2u0cP0hM0j6Qq%2BQjxQ7fl52kIgcfw4p98e1IIof87mP6zEgsgSYg0FfP3XSMVA%2BhfSZizVXm1xLg6jI0cvvKxfSbxgyHawV1PO5Ew%2F7%2BmywY6pgFZZRV8uW7Of9Wxr%2BqvV5Dz%2BGZhYV4udDA%2BH4dU8Xqt%2Fe%2BeEkVZ1l1l%2FdaWASI3dDnYq%2FQHSpdzyFjz2ZB2RnQl37q0NkzP6wl1srGCFlER1yDiK688m0%2FAKtGsCON%2FMmfN07UwFR%2FUDtKZny4GFVp7anmw%2FoQ6JDqTC9TWRsf7GfaojNnXijHMnon9MObEb3Jb5mTKr2dsVTA0Jw12xFVaRwm2qkzS&X-Amz-Signature=746aee6fbc56b04b43c2782f6a7015e6fe0e4743a6cd4933057e3fe0922b9496&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRA74IMI%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIH8jv1FtjrR1G9HVJcaEjKIGtaoHfTSNABKQDa4rkjC9AiBp34J2sosPM6KOt%2BvkEphqaS44CShMsD5Lh2jkNJ4t5yr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMB%2Bl0H3usuK6iMBydKtwDEnhiDtW62WG%2FCGrGj6y%2B1zrCT5G8RMldAhbk31JFPgJ4d6bNazJjO4IQ9zUelkfhcCU%2BEqv5yROzYJbDGmFFp3UEW0U%2F%2BcIFaLB5Yz0JIacdueL2K9uQRXLeXDbES7zowQXw304PFKKBVK4DxjJcfJqkTn5r3In95%2BQ0BXXZxIg0DRHr99txEEXsftkqVajDP2oBFppOpsUr9MwOmwhfbBvoDypQGV9bm4a%2FNScgbguh2tTv0WrxaW3phnR4vqt1%2F1t0Dxfpo7JsKaMwW2LNudG5hF7rCNx4lsXPOBvC1KajfpRbwuHYIS4WLzfElg%2BvsfX2EgJU3AxKxJl7rUylfgk56FYsgxVVIXqhlv2i2danMAC9C4Rb3v6Ypx6evPKJBmDfjqYpQP1kwiVOroSN7SakXkbG7PEDKFMZtjiEuqqKbIHO62fUYehtFW%2FNZMUvhialCTgTxv3qGvpiMnNQhWCU6LYzoSoqJ8kBvqCKfPGc5xxrUgvem6pzZ8Sn4MLJ8t61SsEpaUw%2FOO%2FzLmdI8Fb2u0cP0hM0j6Qq%2BQjxQ7fl52kIgcfw4p98e1IIof87mP6zEgsgSYg0FfP3XSMVA%2BhfSZizVXm1xLg6jI0cvvKxfSbxgyHawV1PO5Ew%2F7%2BmywY6pgFZZRV8uW7Of9Wxr%2BqvV5Dz%2BGZhYV4udDA%2BH4dU8Xqt%2Fe%2BeEkVZ1l1l%2FdaWASI3dDnYq%2FQHSpdzyFjz2ZB2RnQl37q0NkzP6wl1srGCFlER1yDiK688m0%2FAKtGsCON%2FMmfN07UwFR%2FUDtKZny4GFVp7anmw%2FoQ6JDqTC9TWRsf7GfaojNnXijHMnon9MObEb3Jb5mTKr2dsVTA0Jw12xFVaRwm2qkzS&X-Amz-Signature=ae2e71cb97940e382192869881ebb1a8d7ddfc5f044627d2bce9af0b1095ff6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

