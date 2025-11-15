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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDUL266N%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T024013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FbimAbrmaUj29AgYIv0IDIZ2N1eNvIo%2FqxAG0HmtJIgIgCdV%2FuLDN%2FvK0vUf24Z0evReJcgt5%2Fpq3Mst07de%2Bk94q%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDIpY9BWYBPYuBdT%2BAircA9J%2BySjfffGBG5i9VMlVv6Y47EtKqxem%2BZj%2BCcDuSLpuWCAXpxoINihnZ3o7r%2BthQwQLM3mihSLpKtioX4b9%2FIr5H%2Bt1x0Ea0MHPakSjoLVWBivtxEu6MnTTLAw5Wdrbbkl8dFkueijD0zbO4RRAtsoXRQx320cL5vgzPs8VcSMPlNvy%2BqRGI355ZDlGbqpP%2F%2BFJ5m7uHdeBJ8PcwKc1L%2B8Lcvk4nFFaF08kOJMOZXvB3VbpliwXxRUn8IVUQlNXgpMkdcxJbjRl%2B3p3MpMu9oqZNlGsgo6lC0XjYl4KJvn%2BRWhfZv33kv4K4U1EpZtzm4ZpGGfl2iI%2BFOTAoRYxPveZRO6iXsJYrFob69hNHMOU2Jk1fsPF%2Fa%2B7ltsHaZex3eqy%2B2%2B8GQ3BLftcfK7f493VHWDkplQ5YgPoZ%2F91V5ri1j%2FG%2BMUYAQTQMug8IwLH2C8wYZPXBnljlC9BO0mPOfrfnb2Ern9c1wHA89F%2BBjCdhHUBwLrvfoxBZuTA6YASHQ0UUEgG7pj5ZHdMod38t%2BTnP2h1Ef0h1mph0ajEjxdS73SYBa%2B6kIYNBsGSrN0flmDxs3Wf0d%2FBdTpXNPPj%2BsZsnuDYwLkfpbmnNy72r3GJjbxEgkhHZI%2B6%2F%2BZKMJ3A38gGOqUBreuGgY%2FQMYw6s4P2fd0D3CB8LfKtwJexGLPrz30yWFWeETphKTEUV5YC9eMPJqXktqAUNLx%2FMbhjtFhf5Y88sMYJ9%2F5cvtuRPY7Mm5RPGjKr0UuhNveK%2BkVul%2BOUVMmUnQk%2B7YGteHNknO3JbosMJqlTqQohYQYWA52039g%2BXPSmNbbAPP%2B3N4N3zL6tpB3IafgoQxNa2wMJaf%2Bmulja9FBWC%2FLD&X-Amz-Signature=526e0fef6086c1a92f56f65711fc2f923be248119425a44e364a68930678b824&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDUL266N%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T024013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FbimAbrmaUj29AgYIv0IDIZ2N1eNvIo%2FqxAG0HmtJIgIgCdV%2FuLDN%2FvK0vUf24Z0evReJcgt5%2Fpq3Mst07de%2Bk94q%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDIpY9BWYBPYuBdT%2BAircA9J%2BySjfffGBG5i9VMlVv6Y47EtKqxem%2BZj%2BCcDuSLpuWCAXpxoINihnZ3o7r%2BthQwQLM3mihSLpKtioX4b9%2FIr5H%2Bt1x0Ea0MHPakSjoLVWBivtxEu6MnTTLAw5Wdrbbkl8dFkueijD0zbO4RRAtsoXRQx320cL5vgzPs8VcSMPlNvy%2BqRGI355ZDlGbqpP%2F%2BFJ5m7uHdeBJ8PcwKc1L%2B8Lcvk4nFFaF08kOJMOZXvB3VbpliwXxRUn8IVUQlNXgpMkdcxJbjRl%2B3p3MpMu9oqZNlGsgo6lC0XjYl4KJvn%2BRWhfZv33kv4K4U1EpZtzm4ZpGGfl2iI%2BFOTAoRYxPveZRO6iXsJYrFob69hNHMOU2Jk1fsPF%2Fa%2B7ltsHaZex3eqy%2B2%2B8GQ3BLftcfK7f493VHWDkplQ5YgPoZ%2F91V5ri1j%2FG%2BMUYAQTQMug8IwLH2C8wYZPXBnljlC9BO0mPOfrfnb2Ern9c1wHA89F%2BBjCdhHUBwLrvfoxBZuTA6YASHQ0UUEgG7pj5ZHdMod38t%2BTnP2h1Ef0h1mph0ajEjxdS73SYBa%2B6kIYNBsGSrN0flmDxs3Wf0d%2FBdTpXNPPj%2BsZsnuDYwLkfpbmnNy72r3GJjbxEgkhHZI%2B6%2F%2BZKMJ3A38gGOqUBreuGgY%2FQMYw6s4P2fd0D3CB8LfKtwJexGLPrz30yWFWeETphKTEUV5YC9eMPJqXktqAUNLx%2FMbhjtFhf5Y88sMYJ9%2F5cvtuRPY7Mm5RPGjKr0UuhNveK%2BkVul%2BOUVMmUnQk%2B7YGteHNknO3JbosMJqlTqQohYQYWA52039g%2BXPSmNbbAPP%2B3N4N3zL6tpB3IafgoQxNa2wMJaf%2Bmulja9FBWC%2FLD&X-Amz-Signature=64f1906f0729390cdb0012ac7c6a70da4d801e42ed22fc70f5df8483d070d324&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDUL266N%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T024013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FbimAbrmaUj29AgYIv0IDIZ2N1eNvIo%2FqxAG0HmtJIgIgCdV%2FuLDN%2FvK0vUf24Z0evReJcgt5%2Fpq3Mst07de%2Bk94q%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDIpY9BWYBPYuBdT%2BAircA9J%2BySjfffGBG5i9VMlVv6Y47EtKqxem%2BZj%2BCcDuSLpuWCAXpxoINihnZ3o7r%2BthQwQLM3mihSLpKtioX4b9%2FIr5H%2Bt1x0Ea0MHPakSjoLVWBivtxEu6MnTTLAw5Wdrbbkl8dFkueijD0zbO4RRAtsoXRQx320cL5vgzPs8VcSMPlNvy%2BqRGI355ZDlGbqpP%2F%2BFJ5m7uHdeBJ8PcwKc1L%2B8Lcvk4nFFaF08kOJMOZXvB3VbpliwXxRUn8IVUQlNXgpMkdcxJbjRl%2B3p3MpMu9oqZNlGsgo6lC0XjYl4KJvn%2BRWhfZv33kv4K4U1EpZtzm4ZpGGfl2iI%2BFOTAoRYxPveZRO6iXsJYrFob69hNHMOU2Jk1fsPF%2Fa%2B7ltsHaZex3eqy%2B2%2B8GQ3BLftcfK7f493VHWDkplQ5YgPoZ%2F91V5ri1j%2FG%2BMUYAQTQMug8IwLH2C8wYZPXBnljlC9BO0mPOfrfnb2Ern9c1wHA89F%2BBjCdhHUBwLrvfoxBZuTA6YASHQ0UUEgG7pj5ZHdMod38t%2BTnP2h1Ef0h1mph0ajEjxdS73SYBa%2B6kIYNBsGSrN0flmDxs3Wf0d%2FBdTpXNPPj%2BsZsnuDYwLkfpbmnNy72r3GJjbxEgkhHZI%2B6%2F%2BZKMJ3A38gGOqUBreuGgY%2FQMYw6s4P2fd0D3CB8LfKtwJexGLPrz30yWFWeETphKTEUV5YC9eMPJqXktqAUNLx%2FMbhjtFhf5Y88sMYJ9%2F5cvtuRPY7Mm5RPGjKr0UuhNveK%2BkVul%2BOUVMmUnQk%2B7YGteHNknO3JbosMJqlTqQohYQYWA52039g%2BXPSmNbbAPP%2B3N4N3zL6tpB3IafgoQxNa2wMJaf%2Bmulja9FBWC%2FLD&X-Amz-Signature=b9150a82cb9013a693201922d9e776e6e0f9132a6a3babe5192f4884680978c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

