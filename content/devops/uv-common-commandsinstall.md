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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOBBJFUY%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB3Dq0Wq7GXlKHLSPkRbaa%2FYKUQ8CT8OpjXrAh0nkQ5GAiBICT2uixWiUrCjf%2BSwmzbKKLF2QN%2B%2F2A27z8WNO6u73Cr%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMvJ%2BDzonpaK3eUR1CKtwDPCIdRqZucb2u47kr%2FLE1A6RnwWlFizYMfNgYEWaoSQyFZlXwZgnr0BomD%2FBk%2FoJeLqu5Aa8R0vmmAPzMSFq71IRv3hcdLBmCME6fZ2ie1ZblUN0mqQGLgn4RGlFMGZiWfL7kJgXCf70%2FTBItwudhnYdAybLH%2FWSUnbpeiUaA5QnVrKerhlwLyUgPVbSyCvjrremJklOfB4kGkNuMJtOL%2Fep7N5gDAZeLtCNGe0Rs2g80NlLvdnH1WkdJviTzgNlA0EYl8CQ9G9a7HzzaK3C9rehpIctTBHP7r3As%2Bwh6bVmAGZdMt3dXkr5kMmb%2FitSeDmCriouyfP1rwMkuD4QZI1Bq8QwF%2BA0e9FVBGoPi1uY5e%2FasyhbYp31N7HShw0519eGDjh%2BGdGBgMM9yoC%2BBHjt%2BYznKd8hJf3u6AzsuE7%2FgKMkyjDZF7LQgvsr9FJred7TpiOFpGA6rc%2BcJtmmY%2B0U%2BPhJKTbIfkizj2H6KTsobMVqa5DiDvxcVD2mMYlsVx5WbzYQvONcqYhuj8QOBgEFBhNbY%2B2Xp9YVin2SYSH4%2FJRMR0LyabOZZ63PQefehr0IhMDYYfoJ50VTN4v6ZNVd4KWZXGEzpTKMH0RbZ0xJmmrRZm%2Fo9KKoKQkowrvPCzQY6pgEp%2F4uW83%2Bei%2BgpaWQgNe50P1lKiFpxktV7h00g5IUb2VfJdVUdoRUyhkA8oJhSxFh1uty%2BflJBlJNEkUcygWzh8Bb0HsUq2PCXct9g6nwjXM2updjruN100ccBASqmgWVW7NBU%2BKuf8XJ%2BM8lyJDTEIP7TxQX2rYIRscxjRfXbQYFUeuBj6qAPsqYUu2z37EnrDOzwu1aa22JfR1cK2r9qvioBop7x&X-Amz-Signature=afc74b24852ee29431de3ff9f427dcd458ab4684e40ed8d54bcacfb94b7e85e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOBBJFUY%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB3Dq0Wq7GXlKHLSPkRbaa%2FYKUQ8CT8OpjXrAh0nkQ5GAiBICT2uixWiUrCjf%2BSwmzbKKLF2QN%2B%2F2A27z8WNO6u73Cr%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMvJ%2BDzonpaK3eUR1CKtwDPCIdRqZucb2u47kr%2FLE1A6RnwWlFizYMfNgYEWaoSQyFZlXwZgnr0BomD%2FBk%2FoJeLqu5Aa8R0vmmAPzMSFq71IRv3hcdLBmCME6fZ2ie1ZblUN0mqQGLgn4RGlFMGZiWfL7kJgXCf70%2FTBItwudhnYdAybLH%2FWSUnbpeiUaA5QnVrKerhlwLyUgPVbSyCvjrremJklOfB4kGkNuMJtOL%2Fep7N5gDAZeLtCNGe0Rs2g80NlLvdnH1WkdJviTzgNlA0EYl8CQ9G9a7HzzaK3C9rehpIctTBHP7r3As%2Bwh6bVmAGZdMt3dXkr5kMmb%2FitSeDmCriouyfP1rwMkuD4QZI1Bq8QwF%2BA0e9FVBGoPi1uY5e%2FasyhbYp31N7HShw0519eGDjh%2BGdGBgMM9yoC%2BBHjt%2BYznKd8hJf3u6AzsuE7%2FgKMkyjDZF7LQgvsr9FJred7TpiOFpGA6rc%2BcJtmmY%2B0U%2BPhJKTbIfkizj2H6KTsobMVqa5DiDvxcVD2mMYlsVx5WbzYQvONcqYhuj8QOBgEFBhNbY%2B2Xp9YVin2SYSH4%2FJRMR0LyabOZZ63PQefehr0IhMDYYfoJ50VTN4v6ZNVd4KWZXGEzpTKMH0RbZ0xJmmrRZm%2Fo9KKoKQkowrvPCzQY6pgEp%2F4uW83%2Bei%2BgpaWQgNe50P1lKiFpxktV7h00g5IUb2VfJdVUdoRUyhkA8oJhSxFh1uty%2BflJBlJNEkUcygWzh8Bb0HsUq2PCXct9g6nwjXM2updjruN100ccBASqmgWVW7NBU%2BKuf8XJ%2BM8lyJDTEIP7TxQX2rYIRscxjRfXbQYFUeuBj6qAPsqYUu2z37EnrDOzwu1aa22JfR1cK2r9qvioBop7x&X-Amz-Signature=1af80c47bee591fe9885b2c23486a0b23c401ac3e6a98e2da33e6c5b7dd1b5ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOBBJFUY%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB3Dq0Wq7GXlKHLSPkRbaa%2FYKUQ8CT8OpjXrAh0nkQ5GAiBICT2uixWiUrCjf%2BSwmzbKKLF2QN%2B%2F2A27z8WNO6u73Cr%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMvJ%2BDzonpaK3eUR1CKtwDPCIdRqZucb2u47kr%2FLE1A6RnwWlFizYMfNgYEWaoSQyFZlXwZgnr0BomD%2FBk%2FoJeLqu5Aa8R0vmmAPzMSFq71IRv3hcdLBmCME6fZ2ie1ZblUN0mqQGLgn4RGlFMGZiWfL7kJgXCf70%2FTBItwudhnYdAybLH%2FWSUnbpeiUaA5QnVrKerhlwLyUgPVbSyCvjrremJklOfB4kGkNuMJtOL%2Fep7N5gDAZeLtCNGe0Rs2g80NlLvdnH1WkdJviTzgNlA0EYl8CQ9G9a7HzzaK3C9rehpIctTBHP7r3As%2Bwh6bVmAGZdMt3dXkr5kMmb%2FitSeDmCriouyfP1rwMkuD4QZI1Bq8QwF%2BA0e9FVBGoPi1uY5e%2FasyhbYp31N7HShw0519eGDjh%2BGdGBgMM9yoC%2BBHjt%2BYznKd8hJf3u6AzsuE7%2FgKMkyjDZF7LQgvsr9FJred7TpiOFpGA6rc%2BcJtmmY%2B0U%2BPhJKTbIfkizj2H6KTsobMVqa5DiDvxcVD2mMYlsVx5WbzYQvONcqYhuj8QOBgEFBhNbY%2B2Xp9YVin2SYSH4%2FJRMR0LyabOZZ63PQefehr0IhMDYYfoJ50VTN4v6ZNVd4KWZXGEzpTKMH0RbZ0xJmmrRZm%2Fo9KKoKQkowrvPCzQY6pgEp%2F4uW83%2Bei%2BgpaWQgNe50P1lKiFpxktV7h00g5IUb2VfJdVUdoRUyhkA8oJhSxFh1uty%2BflJBlJNEkUcygWzh8Bb0HsUq2PCXct9g6nwjXM2updjruN100ccBASqmgWVW7NBU%2BKuf8XJ%2BM8lyJDTEIP7TxQX2rYIRscxjRfXbQYFUeuBj6qAPsqYUu2z37EnrDOzwu1aa22JfR1cK2r9qvioBop7x&X-Amz-Signature=833c45a9b3dca564767c9039f20869814bceea669db4e18f8c961ed310ce8861&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

