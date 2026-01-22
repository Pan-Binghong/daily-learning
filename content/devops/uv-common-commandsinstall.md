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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCGOV37U%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQCufDsjiyu1fGqqMDzGFGkxM%2FYqFN6b7hjJC9wfDg%2FuhQIhAMTJh5iYR%2FyG4XWG2fPJYfTwZyKeyWCsWIMh%2B6k96rZdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzRlteAegX6%2BracvrQq3AN9EuxHZ6fxtWo0hEnMOnkL3fVydkaTz6jIsD%2FyCNpBUPa9UoodwKPA9%2FG2FvQsN8wIusKz9XoUnl%2Fs0k%2BLz0wUY97skO9GQkqYRRfK7iOxLo2JRiwjnJbjw6UuiQ563tmCpT4Qtxbdq4M5v4x4kLYon9YHfe1xaJQkiWpG1%2FPV3QrFMRySJdvdVFdCcvbuyabn0Cwp88xGwEh9iJENKxKg6%2Fu%2FqifhMpUbQ%2BmTvaZeiIU9uojiJR53nm6VXFXNTVeCqTLgBjLDR1wlo7W67fXEwwBrnL7CLY4p3mXUkPsAqvrX5VZBygmJ%2FVxR%2BG4RWR2IzMzT50zIlLRW%2Flz%2BXIlHyuspsDkuRHGg17d%2FjnNU3JGgcQAg%2BHS1dHU6QXlg6gx%2F0HS4SEJwtCiQFDjUp7AK6tY9z%2FztqQ%2Bx0Nx%2Bk9M5cOBg0x8EA%2F6XRR%2BK%2B%2FIvloMNWjfyY%2F6p8DuPB1ajb2b9dtyMkMqByzBGE7iP37Jk4nAynNf1W8lBKkNeYLLL6dDbtetZkTigo%2BoCMmziWdpP%2B2fD%2Fs5Xho7fcqUhT7Zb3yfMOohxpEqNqy0prOt2SeOrHZ9RqDqqoo%2F%2Fpqh3aQazArZx1RLXTYVpqKAvUN%2FDIK1C1KAXcyX7dCNQdDDy18XLBjqkAQeiiNTisPoy9X%2FyJloNZSy2RqILhsyw%2FA1pwBLEKnIVeVh7lYkw8whjyk4r%2F%2BOCcWEzGyteibCtTPOKiC2BGbU4fUMOelXZLlh6aSyrFF4v7SU4mAuIliNThA5IzeTiNQ9eTHjNSDbtrDt8S5oeIm5CY5ylP7mQNM2kKZJXMBA4%2BxADnsl4TkOh7t%2ByiuMi5WO8M0g3WlliS4Vr2PpZGpfeT%2BRa&X-Amz-Signature=456c1f690b6efcc45d6213544985704cb0448f8347bb5726d8bc128a6ddc9740&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCGOV37U%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQCufDsjiyu1fGqqMDzGFGkxM%2FYqFN6b7hjJC9wfDg%2FuhQIhAMTJh5iYR%2FyG4XWG2fPJYfTwZyKeyWCsWIMh%2B6k96rZdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzRlteAegX6%2BracvrQq3AN9EuxHZ6fxtWo0hEnMOnkL3fVydkaTz6jIsD%2FyCNpBUPa9UoodwKPA9%2FG2FvQsN8wIusKz9XoUnl%2Fs0k%2BLz0wUY97skO9GQkqYRRfK7iOxLo2JRiwjnJbjw6UuiQ563tmCpT4Qtxbdq4M5v4x4kLYon9YHfe1xaJQkiWpG1%2FPV3QrFMRySJdvdVFdCcvbuyabn0Cwp88xGwEh9iJENKxKg6%2Fu%2FqifhMpUbQ%2BmTvaZeiIU9uojiJR53nm6VXFXNTVeCqTLgBjLDR1wlo7W67fXEwwBrnL7CLY4p3mXUkPsAqvrX5VZBygmJ%2FVxR%2BG4RWR2IzMzT50zIlLRW%2Flz%2BXIlHyuspsDkuRHGg17d%2FjnNU3JGgcQAg%2BHS1dHU6QXlg6gx%2F0HS4SEJwtCiQFDjUp7AK6tY9z%2FztqQ%2Bx0Nx%2Bk9M5cOBg0x8EA%2F6XRR%2BK%2B%2FIvloMNWjfyY%2F6p8DuPB1ajb2b9dtyMkMqByzBGE7iP37Jk4nAynNf1W8lBKkNeYLLL6dDbtetZkTigo%2BoCMmziWdpP%2B2fD%2Fs5Xho7fcqUhT7Zb3yfMOohxpEqNqy0prOt2SeOrHZ9RqDqqoo%2F%2Fpqh3aQazArZx1RLXTYVpqKAvUN%2FDIK1C1KAXcyX7dCNQdDDy18XLBjqkAQeiiNTisPoy9X%2FyJloNZSy2RqILhsyw%2FA1pwBLEKnIVeVh7lYkw8whjyk4r%2F%2BOCcWEzGyteibCtTPOKiC2BGbU4fUMOelXZLlh6aSyrFF4v7SU4mAuIliNThA5IzeTiNQ9eTHjNSDbtrDt8S5oeIm5CY5ylP7mQNM2kKZJXMBA4%2BxADnsl4TkOh7t%2ByiuMi5WO8M0g3WlliS4Vr2PpZGpfeT%2BRa&X-Amz-Signature=d6b959dddc7947821b2a3149498c5f67dd1340faedbc64c7d1239ee637620a04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCGOV37U%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQCufDsjiyu1fGqqMDzGFGkxM%2FYqFN6b7hjJC9wfDg%2FuhQIhAMTJh5iYR%2FyG4XWG2fPJYfTwZyKeyWCsWIMh%2B6k96rZdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzRlteAegX6%2BracvrQq3AN9EuxHZ6fxtWo0hEnMOnkL3fVydkaTz6jIsD%2FyCNpBUPa9UoodwKPA9%2FG2FvQsN8wIusKz9XoUnl%2Fs0k%2BLz0wUY97skO9GQkqYRRfK7iOxLo2JRiwjnJbjw6UuiQ563tmCpT4Qtxbdq4M5v4x4kLYon9YHfe1xaJQkiWpG1%2FPV3QrFMRySJdvdVFdCcvbuyabn0Cwp88xGwEh9iJENKxKg6%2Fu%2FqifhMpUbQ%2BmTvaZeiIU9uojiJR53nm6VXFXNTVeCqTLgBjLDR1wlo7W67fXEwwBrnL7CLY4p3mXUkPsAqvrX5VZBygmJ%2FVxR%2BG4RWR2IzMzT50zIlLRW%2Flz%2BXIlHyuspsDkuRHGg17d%2FjnNU3JGgcQAg%2BHS1dHU6QXlg6gx%2F0HS4SEJwtCiQFDjUp7AK6tY9z%2FztqQ%2Bx0Nx%2Bk9M5cOBg0x8EA%2F6XRR%2BK%2B%2FIvloMNWjfyY%2F6p8DuPB1ajb2b9dtyMkMqByzBGE7iP37Jk4nAynNf1W8lBKkNeYLLL6dDbtetZkTigo%2BoCMmziWdpP%2B2fD%2Fs5Xho7fcqUhT7Zb3yfMOohxpEqNqy0prOt2SeOrHZ9RqDqqoo%2F%2Fpqh3aQazArZx1RLXTYVpqKAvUN%2FDIK1C1KAXcyX7dCNQdDDy18XLBjqkAQeiiNTisPoy9X%2FyJloNZSy2RqILhsyw%2FA1pwBLEKnIVeVh7lYkw8whjyk4r%2F%2BOCcWEzGyteibCtTPOKiC2BGbU4fUMOelXZLlh6aSyrFF4v7SU4mAuIliNThA5IzeTiNQ9eTHjNSDbtrDt8S5oeIm5CY5ylP7mQNM2kKZJXMBA4%2BxADnsl4TkOh7t%2ByiuMi5WO8M0g3WlliS4Vr2PpZGpfeT%2BRa&X-Amz-Signature=af10d7041f168d0032d9bb4bbc85acf1e7b41e407d538df731929df0ee9f37cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

