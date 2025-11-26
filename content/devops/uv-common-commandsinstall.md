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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUMV5YRO%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDnrWDny7HdtkbSRuu8rSQYXVGDLfTi8C5j3NhdUyuJQAIhAJ6rh4oyts0mzZMo1upU60PYHO2y2154j2khjamHYwUDKv8DCHsQABoMNjM3NDIzMTgzODA1Igw%2Bq9pJuSiZwNz8oScq3AP2867l1J7fhSC8KGKamE5gYHPCRMHbUvKhjh9iONFbZBlXBD6HnAyL%2BYz1WpvIqtFkKbZzeoQKT0FJCgr0MApvteOE%2BQ8bgUhFV9xlo%2FJviuVB6mtRhb7voW5rJwgCbslJBdMXjrfbfJqP%2BTmdBTg16jNyaiuembFNaHVE%2BQ5KuhZp8Mi0J%2Fy%2FSz%2F%2FTRkuaxUCWNhUvD3N2W3XENHd%2F9KW7ZozBp11e2si4aRKutj5jHagp142GKQ4ulXVpWzgAVU8AHAKVmruXlpSo1QRd8LqUwUpMmiOnPHRgoh8w6UjKkUzMzUF30OMN0Oi0ilHgrEh7aS%2BbWMiBhk7VbeVAKvyffr%2FTK7z8jg3NrbWIcauLAO0BWCdEjjrE4OQs%2FcRc9TUnHESzTtJ3QG6hfGlr5lkUvI6Va9%2F72kQMErF3c60%2FTh%2BBvt3AtPwVQH3ZDU3c1OvjGQWQnkN9NSFl4gr82ym4HnBNhULeD5ISEkIMOURiRLKm53P7fUjqTB4qETqWlk4RJ%2FaBs3%2BtOjFETNnx2DcSPaxVptMCljdHw61DiRe09X0Map%2BURfNuWSWjaEaW5jcgdvj4EduRjMneLT4eFJTJPzVX%2BbmoFUtA4qFAEQg%2FezuFYJVq6LRfczeJDCBsJnJBjqkAWJIp5EJ1zEwqCVtEFTBGyQCrHPacyFxEpNp91DfWsg0hd56yWQb170nQ97%2Ftdm1PdgXx2mOBK1MK4RhwivctXSc2%2BmcjcAukZteQVEjFhad9up09J3VRqIG1HQSyFxxvUQoLz0MEfxkOWi2iGv51H91lp%2Fw2mR3LHt%2B8mIPnfYrzn9SwANhSMtiDJIi%2BAfWG1nthefopzrIbvMs5zVm4%2BRLYb7W&X-Amz-Signature=20ec3cdc1fe1da8f6d9fbc44100e98fd7be529f080284cf423023cef017e3327&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUMV5YRO%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDnrWDny7HdtkbSRuu8rSQYXVGDLfTi8C5j3NhdUyuJQAIhAJ6rh4oyts0mzZMo1upU60PYHO2y2154j2khjamHYwUDKv8DCHsQABoMNjM3NDIzMTgzODA1Igw%2Bq9pJuSiZwNz8oScq3AP2867l1J7fhSC8KGKamE5gYHPCRMHbUvKhjh9iONFbZBlXBD6HnAyL%2BYz1WpvIqtFkKbZzeoQKT0FJCgr0MApvteOE%2BQ8bgUhFV9xlo%2FJviuVB6mtRhb7voW5rJwgCbslJBdMXjrfbfJqP%2BTmdBTg16jNyaiuembFNaHVE%2BQ5KuhZp8Mi0J%2Fy%2FSz%2F%2FTRkuaxUCWNhUvD3N2W3XENHd%2F9KW7ZozBp11e2si4aRKutj5jHagp142GKQ4ulXVpWzgAVU8AHAKVmruXlpSo1QRd8LqUwUpMmiOnPHRgoh8w6UjKkUzMzUF30OMN0Oi0ilHgrEh7aS%2BbWMiBhk7VbeVAKvyffr%2FTK7z8jg3NrbWIcauLAO0BWCdEjjrE4OQs%2FcRc9TUnHESzTtJ3QG6hfGlr5lkUvI6Va9%2F72kQMErF3c60%2FTh%2BBvt3AtPwVQH3ZDU3c1OvjGQWQnkN9NSFl4gr82ym4HnBNhULeD5ISEkIMOURiRLKm53P7fUjqTB4qETqWlk4RJ%2FaBs3%2BtOjFETNnx2DcSPaxVptMCljdHw61DiRe09X0Map%2BURfNuWSWjaEaW5jcgdvj4EduRjMneLT4eFJTJPzVX%2BbmoFUtA4qFAEQg%2FezuFYJVq6LRfczeJDCBsJnJBjqkAWJIp5EJ1zEwqCVtEFTBGyQCrHPacyFxEpNp91DfWsg0hd56yWQb170nQ97%2Ftdm1PdgXx2mOBK1MK4RhwivctXSc2%2BmcjcAukZteQVEjFhad9up09J3VRqIG1HQSyFxxvUQoLz0MEfxkOWi2iGv51H91lp%2Fw2mR3LHt%2B8mIPnfYrzn9SwANhSMtiDJIi%2BAfWG1nthefopzrIbvMs5zVm4%2BRLYb7W&X-Amz-Signature=d48ccd490fde10f30b1164a98ae94dd03b329b3c181cde2cb29f138e61d40ef0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUMV5YRO%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDnrWDny7HdtkbSRuu8rSQYXVGDLfTi8C5j3NhdUyuJQAIhAJ6rh4oyts0mzZMo1upU60PYHO2y2154j2khjamHYwUDKv8DCHsQABoMNjM3NDIzMTgzODA1Igw%2Bq9pJuSiZwNz8oScq3AP2867l1J7fhSC8KGKamE5gYHPCRMHbUvKhjh9iONFbZBlXBD6HnAyL%2BYz1WpvIqtFkKbZzeoQKT0FJCgr0MApvteOE%2BQ8bgUhFV9xlo%2FJviuVB6mtRhb7voW5rJwgCbslJBdMXjrfbfJqP%2BTmdBTg16jNyaiuembFNaHVE%2BQ5KuhZp8Mi0J%2Fy%2FSz%2F%2FTRkuaxUCWNhUvD3N2W3XENHd%2F9KW7ZozBp11e2si4aRKutj5jHagp142GKQ4ulXVpWzgAVU8AHAKVmruXlpSo1QRd8LqUwUpMmiOnPHRgoh8w6UjKkUzMzUF30OMN0Oi0ilHgrEh7aS%2BbWMiBhk7VbeVAKvyffr%2FTK7z8jg3NrbWIcauLAO0BWCdEjjrE4OQs%2FcRc9TUnHESzTtJ3QG6hfGlr5lkUvI6Va9%2F72kQMErF3c60%2FTh%2BBvt3AtPwVQH3ZDU3c1OvjGQWQnkN9NSFl4gr82ym4HnBNhULeD5ISEkIMOURiRLKm53P7fUjqTB4qETqWlk4RJ%2FaBs3%2BtOjFETNnx2DcSPaxVptMCljdHw61DiRe09X0Map%2BURfNuWSWjaEaW5jcgdvj4EduRjMneLT4eFJTJPzVX%2BbmoFUtA4qFAEQg%2FezuFYJVq6LRfczeJDCBsJnJBjqkAWJIp5EJ1zEwqCVtEFTBGyQCrHPacyFxEpNp91DfWsg0hd56yWQb170nQ97%2Ftdm1PdgXx2mOBK1MK4RhwivctXSc2%2BmcjcAukZteQVEjFhad9up09J3VRqIG1HQSyFxxvUQoLz0MEfxkOWi2iGv51H91lp%2Fw2mR3LHt%2B8mIPnfYrzn9SwANhSMtiDJIi%2BAfWG1nthefopzrIbvMs5zVm4%2BRLYb7W&X-Amz-Signature=529bc08ab7fecdc384d75cae8c924894ccac687606656355d4d45b1e871f3429&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

