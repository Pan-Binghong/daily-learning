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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKUISPTO%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDEz%2Fkfn1%2FOOzWcFmQ7ow%2FPWE4BgInZ4caZcEIbq0cfwAiEA2se5bVwNzwtgdPiCog950nhLpI00IrqVM%2F8Dvk3Ktg8qiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGhw4i2Kcr5ba9dJHSrcAyAU0w5S6uXhDlrK7SlvUEjW%2F8uncgsEMwPkduESKjzRgy05XaBEnI0NXXsyiULT6SnUrnMmgPZeMLMgnApgdfXNOF8IpcT2AA4ijCj3jhnDEBN5GneZMN2nwXome%2BGZSakI%2BX0ARXJvClS0vIaYHmAqVgP20Wr%2BLI8WYSFi9ohJAw24%2Bb4KrFxPPXisMO6k5UxwD%2B%2Bd4IbP30MCJPwa06wqO0le7AH3WZ2ZjiujJiZPNPNnXYU%2FTqL9eKIATtHhqh26peQxtgkcYF1hEkwEqjxWx%2BzhQcipYR7ILdPJA1%2BvAMpzjhdrOSrOny4tTGAj3mBX%2B8f6agPkV6R2SoOLhdgam2URchk7rhheJgZMFVPELiBBN%2BS18x1HSvL1yuD0iJqSq%2FEIBeqYYorAMMwB%2BSL86Ln3sXHfP8p15gXByZa%2FVK6cL67jlBlDvp%2FauP0BSiaZu5E716AyLC9RHZlfd5YOeeDcBpfKpz3C9tep3IfssmvzVN24grL%2FyY4VL4qPlDch4BDpUGFOc8iH8WsnN23NF0g15Igth5hjO8C6Fh0GeU7mxeQU%2BYq6PeIi5seQEp1qSHf6GEJCsAx7NPEb4u5MwuIKodj0J7R9f8b3AsWae56YZTlvAm1Fk6SLMPHQvc4GOqUBOCv7GlJE1cA04EgLfwtosUiBvuFWeAvSgXmQFZ9emDp1ec3v1k9zPyPzU1XjOsy9WY6R5TqhJTEdPdIsU0jl0dAzS%2BFQAp6kq%2FsKU%2BTn9%2FYoa9%2B7j5RwUE9Rfll9tdsCIrdhPPv76Un9h88a3HOhVaxOIzSFEH9bliy14QyOECrivzZh6YP2YT00jGpCctfb4ImgVYFlxLgRF8QEpe%2FDZq%2BjOUXF&X-Amz-Signature=e24777221c1c1094e2b31c141cdf2a4fa8e2e99bd9b370ad4bef0efb554a2f21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKUISPTO%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDEz%2Fkfn1%2FOOzWcFmQ7ow%2FPWE4BgInZ4caZcEIbq0cfwAiEA2se5bVwNzwtgdPiCog950nhLpI00IrqVM%2F8Dvk3Ktg8qiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGhw4i2Kcr5ba9dJHSrcAyAU0w5S6uXhDlrK7SlvUEjW%2F8uncgsEMwPkduESKjzRgy05XaBEnI0NXXsyiULT6SnUrnMmgPZeMLMgnApgdfXNOF8IpcT2AA4ijCj3jhnDEBN5GneZMN2nwXome%2BGZSakI%2BX0ARXJvClS0vIaYHmAqVgP20Wr%2BLI8WYSFi9ohJAw24%2Bb4KrFxPPXisMO6k5UxwD%2B%2Bd4IbP30MCJPwa06wqO0le7AH3WZ2ZjiujJiZPNPNnXYU%2FTqL9eKIATtHhqh26peQxtgkcYF1hEkwEqjxWx%2BzhQcipYR7ILdPJA1%2BvAMpzjhdrOSrOny4tTGAj3mBX%2B8f6agPkV6R2SoOLhdgam2URchk7rhheJgZMFVPELiBBN%2BS18x1HSvL1yuD0iJqSq%2FEIBeqYYorAMMwB%2BSL86Ln3sXHfP8p15gXByZa%2FVK6cL67jlBlDvp%2FauP0BSiaZu5E716AyLC9RHZlfd5YOeeDcBpfKpz3C9tep3IfssmvzVN24grL%2FyY4VL4qPlDch4BDpUGFOc8iH8WsnN23NF0g15Igth5hjO8C6Fh0GeU7mxeQU%2BYq6PeIi5seQEp1qSHf6GEJCsAx7NPEb4u5MwuIKodj0J7R9f8b3AsWae56YZTlvAm1Fk6SLMPHQvc4GOqUBOCv7GlJE1cA04EgLfwtosUiBvuFWeAvSgXmQFZ9emDp1ec3v1k9zPyPzU1XjOsy9WY6R5TqhJTEdPdIsU0jl0dAzS%2BFQAp6kq%2FsKU%2BTn9%2FYoa9%2B7j5RwUE9Rfll9tdsCIrdhPPv76Un9h88a3HOhVaxOIzSFEH9bliy14QyOECrivzZh6YP2YT00jGpCctfb4ImgVYFlxLgRF8QEpe%2FDZq%2BjOUXF&X-Amz-Signature=0614b2031720fba0a0e64b847b246b88d3ce7d3e91f87c99bb9ba3157060440a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKUISPTO%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDEz%2Fkfn1%2FOOzWcFmQ7ow%2FPWE4BgInZ4caZcEIbq0cfwAiEA2se5bVwNzwtgdPiCog950nhLpI00IrqVM%2F8Dvk3Ktg8qiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGhw4i2Kcr5ba9dJHSrcAyAU0w5S6uXhDlrK7SlvUEjW%2F8uncgsEMwPkduESKjzRgy05XaBEnI0NXXsyiULT6SnUrnMmgPZeMLMgnApgdfXNOF8IpcT2AA4ijCj3jhnDEBN5GneZMN2nwXome%2BGZSakI%2BX0ARXJvClS0vIaYHmAqVgP20Wr%2BLI8WYSFi9ohJAw24%2Bb4KrFxPPXisMO6k5UxwD%2B%2Bd4IbP30MCJPwa06wqO0le7AH3WZ2ZjiujJiZPNPNnXYU%2FTqL9eKIATtHhqh26peQxtgkcYF1hEkwEqjxWx%2BzhQcipYR7ILdPJA1%2BvAMpzjhdrOSrOny4tTGAj3mBX%2B8f6agPkV6R2SoOLhdgam2URchk7rhheJgZMFVPELiBBN%2BS18x1HSvL1yuD0iJqSq%2FEIBeqYYorAMMwB%2BSL86Ln3sXHfP8p15gXByZa%2FVK6cL67jlBlDvp%2FauP0BSiaZu5E716AyLC9RHZlfd5YOeeDcBpfKpz3C9tep3IfssmvzVN24grL%2FyY4VL4qPlDch4BDpUGFOc8iH8WsnN23NF0g15Igth5hjO8C6Fh0GeU7mxeQU%2BYq6PeIi5seQEp1qSHf6GEJCsAx7NPEb4u5MwuIKodj0J7R9f8b3AsWae56YZTlvAm1Fk6SLMPHQvc4GOqUBOCv7GlJE1cA04EgLfwtosUiBvuFWeAvSgXmQFZ9emDp1ec3v1k9zPyPzU1XjOsy9WY6R5TqhJTEdPdIsU0jl0dAzS%2BFQAp6kq%2FsKU%2BTn9%2FYoa9%2B7j5RwUE9Rfll9tdsCIrdhPPv76Un9h88a3HOhVaxOIzSFEH9bliy14QyOECrivzZh6YP2YT00jGpCctfb4ImgVYFlxLgRF8QEpe%2FDZq%2BjOUXF&X-Amz-Signature=786480fc277df3fb454929b44cad575ec4f42f2a4910590a6a4ef284ba201b90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

