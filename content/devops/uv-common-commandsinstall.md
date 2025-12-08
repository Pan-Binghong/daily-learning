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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NTBHP2P%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDskGizjmZCeEnaBk15dOMOhEuw4chFG%2BqDBYxl%2FNR7QQIgI0JFtXsYhvHwtsJzV14yC%2FervHxzZ4VIN74WTu%2BLsoYqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqfRlj7jQg7JWDRXyrcAyVpuTxa86RpsKgwZTslAMy5MhAK3OHRXXKmbQrKxjOvQWQ%2B018sTWCxd8FTp5ojoTsjoyjW3fipg6WO40vbHDdjGLF6DfSe0aUuT3hgBcTk1d7e97dyswVD6hQAeyJ2cCi%2B7RO%2FLtJnSuvm3toviz%2FThHN5FjF9M0WBHA%2BjXptDBxlAbbxgdZZx7j6mLjDvB5o6l9zkBQ4fsMaZQV%2FiB%2BtLuJ2LsnNNPqaAIrD%2FSw31bS8UTQqhfC8ScZuYs%2BHWfeN8aRo6bWmShD1GTfJ7YubwkvkO3QX45%2BQFuWW5FehRDGMCteE%2FYp2HKAlfsE5cuJpH0AumbKBejsdAZNeWMXY1CSGiUon48wwf89Oogtu2K%2B3B5OkcdxRPmMH%2BB3YyYIAavnGsnQKDiDj6nlCu%2FaH%2B27y%2FHaC8vLE5WcnHaEGsWeupyzg3mTQSoWZTXyk95iFaaG%2FuvFdDcyiIgV6cNNo8NUI0TzEcYz2SwUXOSEOSKWU%2BPoPxD5clcQbNqLB0KBRM0rtaPo5nscR4m2opjj9BaX2eHO74kmC1E5zVwhsHrL%2Bwkub5LTLVPdTdHnn8nyZjTcKoMDs7CIxARgv4Is8Bs2AhJ%2BErvtNRZzkUVfP1cLnrLHznkUuENz%2FSMJfu2MkGOqUBTfku75d996cipRrQjvLCgTwk2LKE7pZGVZjkTVANbGFJpdbx%2F7O%2FVPvFcAybNm7tn3mgJXq9BPR%2BGGtTTxrTEn4UfxqL8J%2FgYKj7MtjcXJv3mt1Mace2Y8cSK03UlJhW1w3d65vkZ2%2FANDPcn6esCaEwrlxv6UxKNquybEOc41LDmIePSHytsSQeCqOm1tljL0IM57vVbNJGQtUnEseSzW7WK1cS&X-Amz-Signature=84c99043e34be5300d18835091b3721dd43c24d9a4ac87fd693131be41b53e52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NTBHP2P%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDskGizjmZCeEnaBk15dOMOhEuw4chFG%2BqDBYxl%2FNR7QQIgI0JFtXsYhvHwtsJzV14yC%2FervHxzZ4VIN74WTu%2BLsoYqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqfRlj7jQg7JWDRXyrcAyVpuTxa86RpsKgwZTslAMy5MhAK3OHRXXKmbQrKxjOvQWQ%2B018sTWCxd8FTp5ojoTsjoyjW3fipg6WO40vbHDdjGLF6DfSe0aUuT3hgBcTk1d7e97dyswVD6hQAeyJ2cCi%2B7RO%2FLtJnSuvm3toviz%2FThHN5FjF9M0WBHA%2BjXptDBxlAbbxgdZZx7j6mLjDvB5o6l9zkBQ4fsMaZQV%2FiB%2BtLuJ2LsnNNPqaAIrD%2FSw31bS8UTQqhfC8ScZuYs%2BHWfeN8aRo6bWmShD1GTfJ7YubwkvkO3QX45%2BQFuWW5FehRDGMCteE%2FYp2HKAlfsE5cuJpH0AumbKBejsdAZNeWMXY1CSGiUon48wwf89Oogtu2K%2B3B5OkcdxRPmMH%2BB3YyYIAavnGsnQKDiDj6nlCu%2FaH%2B27y%2FHaC8vLE5WcnHaEGsWeupyzg3mTQSoWZTXyk95iFaaG%2FuvFdDcyiIgV6cNNo8NUI0TzEcYz2SwUXOSEOSKWU%2BPoPxD5clcQbNqLB0KBRM0rtaPo5nscR4m2opjj9BaX2eHO74kmC1E5zVwhsHrL%2Bwkub5LTLVPdTdHnn8nyZjTcKoMDs7CIxARgv4Is8Bs2AhJ%2BErvtNRZzkUVfP1cLnrLHznkUuENz%2FSMJfu2MkGOqUBTfku75d996cipRrQjvLCgTwk2LKE7pZGVZjkTVANbGFJpdbx%2F7O%2FVPvFcAybNm7tn3mgJXq9BPR%2BGGtTTxrTEn4UfxqL8J%2FgYKj7MtjcXJv3mt1Mace2Y8cSK03UlJhW1w3d65vkZ2%2FANDPcn6esCaEwrlxv6UxKNquybEOc41LDmIePSHytsSQeCqOm1tljL0IM57vVbNJGQtUnEseSzW7WK1cS&X-Amz-Signature=a7e3db611e6527aac392008fd25a9e00f02aa93580e5680b8bd8deb1685bace7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NTBHP2P%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDskGizjmZCeEnaBk15dOMOhEuw4chFG%2BqDBYxl%2FNR7QQIgI0JFtXsYhvHwtsJzV14yC%2FervHxzZ4VIN74WTu%2BLsoYqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqfRlj7jQg7JWDRXyrcAyVpuTxa86RpsKgwZTslAMy5MhAK3OHRXXKmbQrKxjOvQWQ%2B018sTWCxd8FTp5ojoTsjoyjW3fipg6WO40vbHDdjGLF6DfSe0aUuT3hgBcTk1d7e97dyswVD6hQAeyJ2cCi%2B7RO%2FLtJnSuvm3toviz%2FThHN5FjF9M0WBHA%2BjXptDBxlAbbxgdZZx7j6mLjDvB5o6l9zkBQ4fsMaZQV%2FiB%2BtLuJ2LsnNNPqaAIrD%2FSw31bS8UTQqhfC8ScZuYs%2BHWfeN8aRo6bWmShD1GTfJ7YubwkvkO3QX45%2BQFuWW5FehRDGMCteE%2FYp2HKAlfsE5cuJpH0AumbKBejsdAZNeWMXY1CSGiUon48wwf89Oogtu2K%2B3B5OkcdxRPmMH%2BB3YyYIAavnGsnQKDiDj6nlCu%2FaH%2B27y%2FHaC8vLE5WcnHaEGsWeupyzg3mTQSoWZTXyk95iFaaG%2FuvFdDcyiIgV6cNNo8NUI0TzEcYz2SwUXOSEOSKWU%2BPoPxD5clcQbNqLB0KBRM0rtaPo5nscR4m2opjj9BaX2eHO74kmC1E5zVwhsHrL%2Bwkub5LTLVPdTdHnn8nyZjTcKoMDs7CIxARgv4Is8Bs2AhJ%2BErvtNRZzkUVfP1cLnrLHznkUuENz%2FSMJfu2MkGOqUBTfku75d996cipRrQjvLCgTwk2LKE7pZGVZjkTVANbGFJpdbx%2F7O%2FVPvFcAybNm7tn3mgJXq9BPR%2BGGtTTxrTEn4UfxqL8J%2FgYKj7MtjcXJv3mt1Mace2Y8cSK03UlJhW1w3d65vkZ2%2FANDPcn6esCaEwrlxv6UxKNquybEOc41LDmIePSHytsSQeCqOm1tljL0IM57vVbNJGQtUnEseSzW7WK1cS&X-Amz-Signature=76900be7398abb21164034338f7e5b931cd9573a7510a8e5e108b94d7d8648cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

