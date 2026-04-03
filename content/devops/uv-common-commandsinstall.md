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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD7YVN7P%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXouaOHzL7%2BtroYF7My3y7VsKzJLXIDKGB6HONx6AN%2FgIgLl9LnTfO3l87RF6UDWn5doc%2FnwcXzZAfgy3gLBbaHGYq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDPG1PYknhsj0eZ2zOSrcA204RxqU70PSyKit7ZLjuStN29rzk04Edp4Qm4y0cu0f6qgkOOk5WLqXvh%2BNAjfMOuauvk6hTzAFewiHQcUhvGwAerkgtZDwvYdE9FQ0y4js%2FlSb8VgOsUxmnXLLz9Km5F2ihLhbVHHl8BeqyS3KTkNAFHOUa6mQAbWCutwzPS5H%2FT4YMavxRkbnJAmnXiBiX9albGnEJi7qd%2FlqRqx2OZu14YSrqNNBh48BMpBY0LYXuBgXuWwKUa%2FlECqeN%2BDCKjTE%2BkQLemFh90EvOYTUtaAQSRQigCvgAU146Xt84nSHLjdcc4OBIPHYOwY2S1cb9d4Tr386e80T0%2FW0zkjtC5a2Oloujvm8okn0wqzkahZ0cHrvvo2wSMFxXKTKu60%2BGhiS5ZY0%2B%2Fi1X1owmQji8AGGUk%2BzI3MhBvH%2BNbq9SnK92oriZbIlpdS%2Bn4J4IEE4b9JagjimgWzU1l3iBLEzjp5AwhkleXcaOcY8N8sjWAXctUm4qf0VVAQrN%2Ftfr2qQCzLmnf3jTjlSxUtHlIN8z6DGBzQU%2FyJYGzv7rdl5YDMMp15MBqqXOR%2FEZxt5XmuEk4wakue2EPRAxHhTI3iBP%2F55UFWYsT5jRaY8aJBT8mJVk7sl8UCpvyjwSn%2B7MP%2Bsvc4GOqUBIPtuSGMqnPDT8UwojvSfGz88VRT4vn348JzQ1zsmkCttOl4mhHqacINzfql2fCI22cpj5C9WpdDAc2GlZrXclo1BYfzWn3tHNYTnpbNjJ03XepcBREx57wJkAE3U6PkeR0TMEMk1n3pf0L8m9quXX64BLHquTEkEvyXTpqajny4wJHXf0xTTnBGinnlwI6RhpVNrHBxkxrboEvuEQ1BEb5RADJd4&X-Amz-Signature=5efa3ba830337c00e268a6cc06364e52c3860cdb16fbdd576ac3746c05a79cf4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD7YVN7P%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXouaOHzL7%2BtroYF7My3y7VsKzJLXIDKGB6HONx6AN%2FgIgLl9LnTfO3l87RF6UDWn5doc%2FnwcXzZAfgy3gLBbaHGYq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDPG1PYknhsj0eZ2zOSrcA204RxqU70PSyKit7ZLjuStN29rzk04Edp4Qm4y0cu0f6qgkOOk5WLqXvh%2BNAjfMOuauvk6hTzAFewiHQcUhvGwAerkgtZDwvYdE9FQ0y4js%2FlSb8VgOsUxmnXLLz9Km5F2ihLhbVHHl8BeqyS3KTkNAFHOUa6mQAbWCutwzPS5H%2FT4YMavxRkbnJAmnXiBiX9albGnEJi7qd%2FlqRqx2OZu14YSrqNNBh48BMpBY0LYXuBgXuWwKUa%2FlECqeN%2BDCKjTE%2BkQLemFh90EvOYTUtaAQSRQigCvgAU146Xt84nSHLjdcc4OBIPHYOwY2S1cb9d4Tr386e80T0%2FW0zkjtC5a2Oloujvm8okn0wqzkahZ0cHrvvo2wSMFxXKTKu60%2BGhiS5ZY0%2B%2Fi1X1owmQji8AGGUk%2BzI3MhBvH%2BNbq9SnK92oriZbIlpdS%2Bn4J4IEE4b9JagjimgWzU1l3iBLEzjp5AwhkleXcaOcY8N8sjWAXctUm4qf0VVAQrN%2Ftfr2qQCzLmnf3jTjlSxUtHlIN8z6DGBzQU%2FyJYGzv7rdl5YDMMp15MBqqXOR%2FEZxt5XmuEk4wakue2EPRAxHhTI3iBP%2F55UFWYsT5jRaY8aJBT8mJVk7sl8UCpvyjwSn%2B7MP%2Bsvc4GOqUBIPtuSGMqnPDT8UwojvSfGz88VRT4vn348JzQ1zsmkCttOl4mhHqacINzfql2fCI22cpj5C9WpdDAc2GlZrXclo1BYfzWn3tHNYTnpbNjJ03XepcBREx57wJkAE3U6PkeR0TMEMk1n3pf0L8m9quXX64BLHquTEkEvyXTpqajny4wJHXf0xTTnBGinnlwI6RhpVNrHBxkxrboEvuEQ1BEb5RADJd4&X-Amz-Signature=52e00427c241733bda417437ea725535d4542ad18480ae5448197d448fb087e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD7YVN7P%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXouaOHzL7%2BtroYF7My3y7VsKzJLXIDKGB6HONx6AN%2FgIgLl9LnTfO3l87RF6UDWn5doc%2FnwcXzZAfgy3gLBbaHGYq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDPG1PYknhsj0eZ2zOSrcA204RxqU70PSyKit7ZLjuStN29rzk04Edp4Qm4y0cu0f6qgkOOk5WLqXvh%2BNAjfMOuauvk6hTzAFewiHQcUhvGwAerkgtZDwvYdE9FQ0y4js%2FlSb8VgOsUxmnXLLz9Km5F2ihLhbVHHl8BeqyS3KTkNAFHOUa6mQAbWCutwzPS5H%2FT4YMavxRkbnJAmnXiBiX9albGnEJi7qd%2FlqRqx2OZu14YSrqNNBh48BMpBY0LYXuBgXuWwKUa%2FlECqeN%2BDCKjTE%2BkQLemFh90EvOYTUtaAQSRQigCvgAU146Xt84nSHLjdcc4OBIPHYOwY2S1cb9d4Tr386e80T0%2FW0zkjtC5a2Oloujvm8okn0wqzkahZ0cHrvvo2wSMFxXKTKu60%2BGhiS5ZY0%2B%2Fi1X1owmQji8AGGUk%2BzI3MhBvH%2BNbq9SnK92oriZbIlpdS%2Bn4J4IEE4b9JagjimgWzU1l3iBLEzjp5AwhkleXcaOcY8N8sjWAXctUm4qf0VVAQrN%2Ftfr2qQCzLmnf3jTjlSxUtHlIN8z6DGBzQU%2FyJYGzv7rdl5YDMMp15MBqqXOR%2FEZxt5XmuEk4wakue2EPRAxHhTI3iBP%2F55UFWYsT5jRaY8aJBT8mJVk7sl8UCpvyjwSn%2B7MP%2Bsvc4GOqUBIPtuSGMqnPDT8UwojvSfGz88VRT4vn348JzQ1zsmkCttOl4mhHqacINzfql2fCI22cpj5C9WpdDAc2GlZrXclo1BYfzWn3tHNYTnpbNjJ03XepcBREx57wJkAE3U6PkeR0TMEMk1n3pf0L8m9quXX64BLHquTEkEvyXTpqajny4wJHXf0xTTnBGinnlwI6RhpVNrHBxkxrboEvuEQ1BEb5RADJd4&X-Amz-Signature=6f504e09c8404cf03d40f45944c76c87efe9b2c4d92344438c0450eb4655ff67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

