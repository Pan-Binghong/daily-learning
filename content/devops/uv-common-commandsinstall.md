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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TS2UYH65%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIATUAa3iaIGXrYvyhDl2GNHas4DWtvK4uq31Vl009WyeAiEA7NqlkYBismvcLRZ6UrV8dPTwnWKdmVTa3b3opGeG9nQq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDKFypK%2BMlYrPmq4f9CrcA5KyQO%2FsQwnxKaMccOoQFaQr4PbR9VPtAU%2FMbFic0USyKbnJDf0DTCG0XIQ4OjU2dC1vsJ%2Bjqk18jITnJ7UKTQ4sgWMa3uxd1%2Ff%2Bt%2FpvEYbigKMe%2FXq9vJZ33gE1ivDBPmlSG5W3vG%2BuYZk46ka8tN4Wm%2BZIkDqcHcmg6GJBtQf4da%2FLPenD6DifrHCVmjcRMuZsLIbRH5rrGZqI%2B%2Bf5BUmPMhwW%2FoYBAjHK8UxFkRRdRsFqXIsaR3rPrtMSA4CpZMVrEUrslki4vX8SpwbV0lBLrHC0jF%2BdrKEtrS3V3hTkDIcBE0Z19Q%2Bd%2FT1MmEY3m2bZ0kkwkqpyryFupRuoMkcL5iZ1aiiAB86uyDB42rrsZf43Eq29NDY3qvMXMEnki%2FXEP1j7gf3Rb22ojmtIukIaS6hT8gNMXyFeuJfmIA90WDmItH%2BZjGZ8%2Fj2d0K4QdOKZ6kxkHb6KUj1wYkXEFrkFOX%2BvoWcpSNsVYG%2FEUlb0wIaV7jwpc7EXodKdch4aL1r2v6PUY3Q%2FmKrdzzfv42XVf9gothvEPgQdWOT492sWXrVhQFFOVVrw7S2jgOYgDrMB6APaMBwYLzhcwMbdKPSh38tl231uVTYW9BTDRjBpwloP2wbzGoMOPcKYMIiE%2BcwGOqUBn6xwQg2MONw1KA6yIPOvVUvtye%2F%2FyTiTkLVQUewWlpE%2FPf%2BAj8JjGwZ0A8ZQ%2FutYVZobzBI8osms2nYaoc2CUCiLf2ymzM8cKLEiIFfKnzsXJ0Qb2LU3Hm3NPSxiYRFQwBdxwJe0BXyqvomkW8lk62jeuopg8%2BaehVFHMIy8zm%2F0UFJqe7z2%2Faa4H6YbIlrLZ3r%2FYTdsgaj%2FHtGm2TRFpg7Jas0a&X-Amz-Signature=88d431ee23bca2785a90d6f3ee7be43fe33697c388b38f4fc82dc7f52e3eef1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TS2UYH65%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIATUAa3iaIGXrYvyhDl2GNHas4DWtvK4uq31Vl009WyeAiEA7NqlkYBismvcLRZ6UrV8dPTwnWKdmVTa3b3opGeG9nQq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDKFypK%2BMlYrPmq4f9CrcA5KyQO%2FsQwnxKaMccOoQFaQr4PbR9VPtAU%2FMbFic0USyKbnJDf0DTCG0XIQ4OjU2dC1vsJ%2Bjqk18jITnJ7UKTQ4sgWMa3uxd1%2Ff%2Bt%2FpvEYbigKMe%2FXq9vJZ33gE1ivDBPmlSG5W3vG%2BuYZk46ka8tN4Wm%2BZIkDqcHcmg6GJBtQf4da%2FLPenD6DifrHCVmjcRMuZsLIbRH5rrGZqI%2B%2Bf5BUmPMhwW%2FoYBAjHK8UxFkRRdRsFqXIsaR3rPrtMSA4CpZMVrEUrslki4vX8SpwbV0lBLrHC0jF%2BdrKEtrS3V3hTkDIcBE0Z19Q%2Bd%2FT1MmEY3m2bZ0kkwkqpyryFupRuoMkcL5iZ1aiiAB86uyDB42rrsZf43Eq29NDY3qvMXMEnki%2FXEP1j7gf3Rb22ojmtIukIaS6hT8gNMXyFeuJfmIA90WDmItH%2BZjGZ8%2Fj2d0K4QdOKZ6kxkHb6KUj1wYkXEFrkFOX%2BvoWcpSNsVYG%2FEUlb0wIaV7jwpc7EXodKdch4aL1r2v6PUY3Q%2FmKrdzzfv42XVf9gothvEPgQdWOT492sWXrVhQFFOVVrw7S2jgOYgDrMB6APaMBwYLzhcwMbdKPSh38tl231uVTYW9BTDRjBpwloP2wbzGoMOPcKYMIiE%2BcwGOqUBn6xwQg2MONw1KA6yIPOvVUvtye%2F%2FyTiTkLVQUewWlpE%2FPf%2BAj8JjGwZ0A8ZQ%2FutYVZobzBI8osms2nYaoc2CUCiLf2ymzM8cKLEiIFfKnzsXJ0Qb2LU3Hm3NPSxiYRFQwBdxwJe0BXyqvomkW8lk62jeuopg8%2BaehVFHMIy8zm%2F0UFJqe7z2%2Faa4H6YbIlrLZ3r%2FYTdsgaj%2FHtGm2TRFpg7Jas0a&X-Amz-Signature=b5a69ea66ca838bad8db09307aba85cd2923c7a00c6e54002c6b8d83cd7e82b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TS2UYH65%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIATUAa3iaIGXrYvyhDl2GNHas4DWtvK4uq31Vl009WyeAiEA7NqlkYBismvcLRZ6UrV8dPTwnWKdmVTa3b3opGeG9nQq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDKFypK%2BMlYrPmq4f9CrcA5KyQO%2FsQwnxKaMccOoQFaQr4PbR9VPtAU%2FMbFic0USyKbnJDf0DTCG0XIQ4OjU2dC1vsJ%2Bjqk18jITnJ7UKTQ4sgWMa3uxd1%2Ff%2Bt%2FpvEYbigKMe%2FXq9vJZ33gE1ivDBPmlSG5W3vG%2BuYZk46ka8tN4Wm%2BZIkDqcHcmg6GJBtQf4da%2FLPenD6DifrHCVmjcRMuZsLIbRH5rrGZqI%2B%2Bf5BUmPMhwW%2FoYBAjHK8UxFkRRdRsFqXIsaR3rPrtMSA4CpZMVrEUrslki4vX8SpwbV0lBLrHC0jF%2BdrKEtrS3V3hTkDIcBE0Z19Q%2Bd%2FT1MmEY3m2bZ0kkwkqpyryFupRuoMkcL5iZ1aiiAB86uyDB42rrsZf43Eq29NDY3qvMXMEnki%2FXEP1j7gf3Rb22ojmtIukIaS6hT8gNMXyFeuJfmIA90WDmItH%2BZjGZ8%2Fj2d0K4QdOKZ6kxkHb6KUj1wYkXEFrkFOX%2BvoWcpSNsVYG%2FEUlb0wIaV7jwpc7EXodKdch4aL1r2v6PUY3Q%2FmKrdzzfv42XVf9gothvEPgQdWOT492sWXrVhQFFOVVrw7S2jgOYgDrMB6APaMBwYLzhcwMbdKPSh38tl231uVTYW9BTDRjBpwloP2wbzGoMOPcKYMIiE%2BcwGOqUBn6xwQg2MONw1KA6yIPOvVUvtye%2F%2FyTiTkLVQUewWlpE%2FPf%2BAj8JjGwZ0A8ZQ%2FutYVZobzBI8osms2nYaoc2CUCiLf2ymzM8cKLEiIFfKnzsXJ0Qb2LU3Hm3NPSxiYRFQwBdxwJe0BXyqvomkW8lk62jeuopg8%2BaehVFHMIy8zm%2F0UFJqe7z2%2Faa4H6YbIlrLZ3r%2FYTdsgaj%2FHtGm2TRFpg7Jas0a&X-Amz-Signature=ad59bf8a0eb038151e4de186e45d553940dacd7f57bf2bce8cfc9fca4e2f161a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

