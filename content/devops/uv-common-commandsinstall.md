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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XO4BFCLV%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIBcETT5ZwpUODut%2F6FwitZCRvYEGN0zROYmCKTxOOcvuAiBsPbgok7OCjQDHn2IlJsxFpC05iZ2DM2GeMjwKQFUGLSr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMwaXsaTE%2BsfcoRnS6KtwDwPAtrvSEQD60yWo8ZqRWzx7Xic7yNpE%2FG6oqWyXoYTMk4%2Bf53b%2Fn9ESVgaGe%2BYq00AQaxWoV8kTrn%2BADn4FZdLeVm0M%2F76FUClN5BqyZfik7s3IsMvDVx8oMaUjzx%2FyJlyWVIC76QjP0ktea3farrAzqw7oK4WV273YIeo%2FSnc%2FCNHQXTrlxlrFVsYc7mFeouhacWde3ptlsDDljBKD4Wbc3Yhy3GLdsr%2F2vLE%2FN7%2B%2BAInTos12ORU1YdooCU20PXjUlxVyKhtBzB35agJOnpBvRXr0WMONuaqVjdE70doMeIpqwkU7v%2BDdeiviwQhseXnFg0xRQlKtXk3SJB6XVAh%2BUCFmWT06m391kawaqE2%2FA4sdAu5CcTUQQHN57pU9oJfZX2LktPtgE3cGJxJQ5qFtgNiBIJ06eIxwjknBYdqVCWKLz7O%2BCxrkT%2B%2F0H2LRYne2%2BDnBJuV%2BjDyE9T2KZa07Ou18F3%2BljQ79v3XCyjZRG31xr4JbQ493ZDT%2F1rE7s3OUVRhYfghacV4RB7YhO8YxqQVarFm1Z6e71Uq5jn8NatZ%2BOazQAvfYRGNxxYRQZocawQhRLyUEPKobSL5sjdxMnIoDKymFKHAwI4giw9tosziN95KLfTLtNF1cwn%2F24zQY6pgFHo1enwlBdiB6KRohdKvSySVBJGVWd%2F6jgGhnsYuN0n8R%2BuAH3%2FzWMdD40tHnsdMAsBqs6ZzX76D7YwoVvHJ%2BablmqtSLvAjTuWqBTgoPgxf8d6gpVRd%2F%2BtukpciIolnsGMt1JS%2FL5jis%2BU2ufH0oGMVc7USO65ZCrhh0p2X4GOs6T036TcNViellLqu1ie0A9EXkjShBi%2BWRFc93SAeVD1N8RuNIQ&X-Amz-Signature=3735a9a190f5122b509854f8237e829d5f7818769456ac563ed851e49663eea0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XO4BFCLV%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIBcETT5ZwpUODut%2F6FwitZCRvYEGN0zROYmCKTxOOcvuAiBsPbgok7OCjQDHn2IlJsxFpC05iZ2DM2GeMjwKQFUGLSr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMwaXsaTE%2BsfcoRnS6KtwDwPAtrvSEQD60yWo8ZqRWzx7Xic7yNpE%2FG6oqWyXoYTMk4%2Bf53b%2Fn9ESVgaGe%2BYq00AQaxWoV8kTrn%2BADn4FZdLeVm0M%2F76FUClN5BqyZfik7s3IsMvDVx8oMaUjzx%2FyJlyWVIC76QjP0ktea3farrAzqw7oK4WV273YIeo%2FSnc%2FCNHQXTrlxlrFVsYc7mFeouhacWde3ptlsDDljBKD4Wbc3Yhy3GLdsr%2F2vLE%2FN7%2B%2BAInTos12ORU1YdooCU20PXjUlxVyKhtBzB35agJOnpBvRXr0WMONuaqVjdE70doMeIpqwkU7v%2BDdeiviwQhseXnFg0xRQlKtXk3SJB6XVAh%2BUCFmWT06m391kawaqE2%2FA4sdAu5CcTUQQHN57pU9oJfZX2LktPtgE3cGJxJQ5qFtgNiBIJ06eIxwjknBYdqVCWKLz7O%2BCxrkT%2B%2F0H2LRYne2%2BDnBJuV%2BjDyE9T2KZa07Ou18F3%2BljQ79v3XCyjZRG31xr4JbQ493ZDT%2F1rE7s3OUVRhYfghacV4RB7YhO8YxqQVarFm1Z6e71Uq5jn8NatZ%2BOazQAvfYRGNxxYRQZocawQhRLyUEPKobSL5sjdxMnIoDKymFKHAwI4giw9tosziN95KLfTLtNF1cwn%2F24zQY6pgFHo1enwlBdiB6KRohdKvSySVBJGVWd%2F6jgGhnsYuN0n8R%2BuAH3%2FzWMdD40tHnsdMAsBqs6ZzX76D7YwoVvHJ%2BablmqtSLvAjTuWqBTgoPgxf8d6gpVRd%2F%2BtukpciIolnsGMt1JS%2FL5jis%2BU2ufH0oGMVc7USO65ZCrhh0p2X4GOs6T036TcNViellLqu1ie0A9EXkjShBi%2BWRFc93SAeVD1N8RuNIQ&X-Amz-Signature=a1aa03e2a06df28a00833b3ae4b15615a50a9e21639ea19ed096c8dc4f4b8612&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XO4BFCLV%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIBcETT5ZwpUODut%2F6FwitZCRvYEGN0zROYmCKTxOOcvuAiBsPbgok7OCjQDHn2IlJsxFpC05iZ2DM2GeMjwKQFUGLSr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMwaXsaTE%2BsfcoRnS6KtwDwPAtrvSEQD60yWo8ZqRWzx7Xic7yNpE%2FG6oqWyXoYTMk4%2Bf53b%2Fn9ESVgaGe%2BYq00AQaxWoV8kTrn%2BADn4FZdLeVm0M%2F76FUClN5BqyZfik7s3IsMvDVx8oMaUjzx%2FyJlyWVIC76QjP0ktea3farrAzqw7oK4WV273YIeo%2FSnc%2FCNHQXTrlxlrFVsYc7mFeouhacWde3ptlsDDljBKD4Wbc3Yhy3GLdsr%2F2vLE%2FN7%2B%2BAInTos12ORU1YdooCU20PXjUlxVyKhtBzB35agJOnpBvRXr0WMONuaqVjdE70doMeIpqwkU7v%2BDdeiviwQhseXnFg0xRQlKtXk3SJB6XVAh%2BUCFmWT06m391kawaqE2%2FA4sdAu5CcTUQQHN57pU9oJfZX2LktPtgE3cGJxJQ5qFtgNiBIJ06eIxwjknBYdqVCWKLz7O%2BCxrkT%2B%2F0H2LRYne2%2BDnBJuV%2BjDyE9T2KZa07Ou18F3%2BljQ79v3XCyjZRG31xr4JbQ493ZDT%2F1rE7s3OUVRhYfghacV4RB7YhO8YxqQVarFm1Z6e71Uq5jn8NatZ%2BOazQAvfYRGNxxYRQZocawQhRLyUEPKobSL5sjdxMnIoDKymFKHAwI4giw9tosziN95KLfTLtNF1cwn%2F24zQY6pgFHo1enwlBdiB6KRohdKvSySVBJGVWd%2F6jgGhnsYuN0n8R%2BuAH3%2FzWMdD40tHnsdMAsBqs6ZzX76D7YwoVvHJ%2BablmqtSLvAjTuWqBTgoPgxf8d6gpVRd%2F%2BtukpciIolnsGMt1JS%2FL5jis%2BU2ufH0oGMVc7USO65ZCrhh0p2X4GOs6T036TcNViellLqu1ie0A9EXkjShBi%2BWRFc93SAeVD1N8RuNIQ&X-Amz-Signature=48d2c5c49a74e76070cbc841a01245fecdd116a71be7961df109bb07822490bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

