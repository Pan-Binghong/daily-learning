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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLDKSLAK%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPdoayBMps412oJiVVQm5sd1u7Tm18dliGYLJlV%2FhK2AiAZKNaiYUtRdzJGvlKRiYUg13ZuEtxIo5U0G%2FDfqAOl9yr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMr%2B435RPf3azl6KbzKtwDjPkEAFaB4fUMgLw8xO%2F6tF8FvEMZLx2%2F2XSEHXhxtnMa%2FwRdMkdGVJcmLACfcrv3j%2Fqx1Iwi%2BdgrPwj0kDX6BJ4GPjoVzMWd8%2BAuBZK2gyQyJdGYxPKUDDutxhmq%2F5eOjV%2BwzOCRYwO3cSgWtOhRl3pGcLDI6lyrFEwf8ovJ71wxW3YhloOtP9VPR%2BkRXjox8T7a1v9oOJzBbX269vaol9wMyEQiwUDGyDxZBbXl3xCZnRK1MK5mGGehhcOJzVBbUMCRj%2F%2B4uPoKwnaDfJqMyFOT6zFAM372k7fwtlpuuqfnmGmJeNre7jNV9KRbvJ%2F2NERAx3NuIfmXCkbko1WvgDbgJAtw5O39Bvb4jTyUt0bcOLEYc%2F91l3D4HamZOTo%2FDLyZUlKySwTLPMmwue6Er%2B6%2BP6AYG5kTxnBWwBc6EpRfMdMB3DxKJBFepP11ur%2BuVdPdOEb0tgDbaPej%2B3RkeGqZiW7%2FnpHbhmDuqYPK%2BMklSjb008hC7dJO9CDfC%2FjKA5L9mg9YCSadHjC2%2FPXs1lmayBPvSgQCyJwOJu9AdQoR1HM0A010Ko%2F3PP843uEJw7oNHRtun951AZRsPWPHpTJoUnFFiGqW%2Fr1%2BBB77CsGolbHeoah7w3ISU0kwpZblywY6pgF3IRw%2B0bZ54PIGhMwhJpw8tROC6IhsVHcfPHCVyK4Htu%2BRA6NKl1W85WRQphS43U7wmPIZqxwxUqxUicg4C3ZiAzARo4vofowG5pdP2BVFIEPkUh41FE4i2sCX6WSwjXM%2FaEyT%2B0EDUl4PEoskQDKJiQtyMi4nDNkvp7ktckZtwCyK3K7jxy6zbwfQabeuhsJsI9RFZLx6Bh0c1aatv1Nlhu2%2BUiaB&X-Amz-Signature=cf87797e86b2c5c0af8a4001927f30dd193ace1a07d32e75a2a3015108edc81a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLDKSLAK%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPdoayBMps412oJiVVQm5sd1u7Tm18dliGYLJlV%2FhK2AiAZKNaiYUtRdzJGvlKRiYUg13ZuEtxIo5U0G%2FDfqAOl9yr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMr%2B435RPf3azl6KbzKtwDjPkEAFaB4fUMgLw8xO%2F6tF8FvEMZLx2%2F2XSEHXhxtnMa%2FwRdMkdGVJcmLACfcrv3j%2Fqx1Iwi%2BdgrPwj0kDX6BJ4GPjoVzMWd8%2BAuBZK2gyQyJdGYxPKUDDutxhmq%2F5eOjV%2BwzOCRYwO3cSgWtOhRl3pGcLDI6lyrFEwf8ovJ71wxW3YhloOtP9VPR%2BkRXjox8T7a1v9oOJzBbX269vaol9wMyEQiwUDGyDxZBbXl3xCZnRK1MK5mGGehhcOJzVBbUMCRj%2F%2B4uPoKwnaDfJqMyFOT6zFAM372k7fwtlpuuqfnmGmJeNre7jNV9KRbvJ%2F2NERAx3NuIfmXCkbko1WvgDbgJAtw5O39Bvb4jTyUt0bcOLEYc%2F91l3D4HamZOTo%2FDLyZUlKySwTLPMmwue6Er%2B6%2BP6AYG5kTxnBWwBc6EpRfMdMB3DxKJBFepP11ur%2BuVdPdOEb0tgDbaPej%2B3RkeGqZiW7%2FnpHbhmDuqYPK%2BMklSjb008hC7dJO9CDfC%2FjKA5L9mg9YCSadHjC2%2FPXs1lmayBPvSgQCyJwOJu9AdQoR1HM0A010Ko%2F3PP843uEJw7oNHRtun951AZRsPWPHpTJoUnFFiGqW%2Fr1%2BBB77CsGolbHeoah7w3ISU0kwpZblywY6pgF3IRw%2B0bZ54PIGhMwhJpw8tROC6IhsVHcfPHCVyK4Htu%2BRA6NKl1W85WRQphS43U7wmPIZqxwxUqxUicg4C3ZiAzARo4vofowG5pdP2BVFIEPkUh41FE4i2sCX6WSwjXM%2FaEyT%2B0EDUl4PEoskQDKJiQtyMi4nDNkvp7ktckZtwCyK3K7jxy6zbwfQabeuhsJsI9RFZLx6Bh0c1aatv1Nlhu2%2BUiaB&X-Amz-Signature=54e10fd9778e3501eae4c9c88a5880f978d200b1cc38249ed3e82a4b0023532c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLDKSLAK%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPdoayBMps412oJiVVQm5sd1u7Tm18dliGYLJlV%2FhK2AiAZKNaiYUtRdzJGvlKRiYUg13ZuEtxIo5U0G%2FDfqAOl9yr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMr%2B435RPf3azl6KbzKtwDjPkEAFaB4fUMgLw8xO%2F6tF8FvEMZLx2%2F2XSEHXhxtnMa%2FwRdMkdGVJcmLACfcrv3j%2Fqx1Iwi%2BdgrPwj0kDX6BJ4GPjoVzMWd8%2BAuBZK2gyQyJdGYxPKUDDutxhmq%2F5eOjV%2BwzOCRYwO3cSgWtOhRl3pGcLDI6lyrFEwf8ovJ71wxW3YhloOtP9VPR%2BkRXjox8T7a1v9oOJzBbX269vaol9wMyEQiwUDGyDxZBbXl3xCZnRK1MK5mGGehhcOJzVBbUMCRj%2F%2B4uPoKwnaDfJqMyFOT6zFAM372k7fwtlpuuqfnmGmJeNre7jNV9KRbvJ%2F2NERAx3NuIfmXCkbko1WvgDbgJAtw5O39Bvb4jTyUt0bcOLEYc%2F91l3D4HamZOTo%2FDLyZUlKySwTLPMmwue6Er%2B6%2BP6AYG5kTxnBWwBc6EpRfMdMB3DxKJBFepP11ur%2BuVdPdOEb0tgDbaPej%2B3RkeGqZiW7%2FnpHbhmDuqYPK%2BMklSjb008hC7dJO9CDfC%2FjKA5L9mg9YCSadHjC2%2FPXs1lmayBPvSgQCyJwOJu9AdQoR1HM0A010Ko%2F3PP843uEJw7oNHRtun951AZRsPWPHpTJoUnFFiGqW%2Fr1%2BBB77CsGolbHeoah7w3ISU0kwpZblywY6pgF3IRw%2B0bZ54PIGhMwhJpw8tROC6IhsVHcfPHCVyK4Htu%2BRA6NKl1W85WRQphS43U7wmPIZqxwxUqxUicg4C3ZiAzARo4vofowG5pdP2BVFIEPkUh41FE4i2sCX6WSwjXM%2FaEyT%2B0EDUl4PEoskQDKJiQtyMi4nDNkvp7ktckZtwCyK3K7jxy6zbwfQabeuhsJsI9RFZLx6Bh0c1aatv1Nlhu2%2BUiaB&X-Amz-Signature=9e4251597a7e3599774610ee8e9359dd91386754446417d06588e023cf6d518e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

