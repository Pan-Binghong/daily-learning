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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRS6VHUC%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDf71xG7Tmg0B%2FpleM0LrGRnUlHURgqQYxOZYPQengq6wIgNHCYDK3e0vqp8N0yay6zaMoplwYT9yL7ulVjPWAyU08q%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDI5P4sfeKCh62MT0EyrcA%2BCBpl%2Bgitm5jFt7oO9ukBTtO8VvgdUswjasFLN9GSI1p04DrCqJXdXUwflhcj0u%2BRJkpU%2BYCjXp%2BWNrOrnwU8omocjFZ6MUbLFd1LrGcaRsv2quXmVH22Rw%2F3g7QsMigJlcd0znmg0bXqdkX9exYox2mrwl%2FG8dwbnA5sWZ%2BQQPb%2FgQYWJqnLh9HIDW95kyIyffpP9TK9VIQxtEsHSX%2FEvcjTowN1GBDpP4t1UsaOEvHUFl2cn0a9fSgRKP%2BYWqz0U6b2Rcqa1nNEQgctqNJjL6wrLVsgiuYe3DW1tHGHKN%2FjGpmaqDWuvdIECQJWlAUYnH7I7gC88ZLyswBEon8YmmZ%2F5LBwjQ26Ti8A9AFSSG%2FC5%2FNpj1CHTaSRNBrvAGZUy1ALkLU7uQG7Tlu9FCWFeXMMeCjrtA7ySoMAYYZ%2BvdWT%2BQGLEngjh%2BuU4IM%2F%2Fa4Q0E9tz73w40XUhF1HPwj8X3VKG9QJ7fVpTHwPAILFFrGdJrsLAwQgvsM1BI7CsMUhNFUm%2Fi%2FzvIHFxhxoDej%2FAib5fJJSzYhAcan74QfuPKzRJcPQtHdgg5Wpuqfhd6AhgBzP0E6dUAYP%2Fo4rkGAJPRkqI%2BiKPgyhcSbX3PHY0oBwTjLAxG92j31GAjMLu7lcwGOqUBw6MIdGKQpN1T6wRrkMN%2FZFK4KArYJoWjXCrl74pI14EcksnbtukcFXA%2F5CjjYM%2FCAO01bcr0Lq4a1Nod74fGn%2BF%2Fsy0BgifhHkOeAfHRG2tJPWY7A8KlzPouekRcxMcNXYIAtzBOqAoUvkstpt5NUS2Rv0Vwp5U%2FA0bSSWaAFHu%2Figjf5OciQWXsB2vEicj7NM%2FjJ7y0K7q%2FM3WR%2FTmQZnGnU4SW&X-Amz-Signature=6b0c12109369755c88b724caab20a9dd066b6f40675d2c76839d31bc6bbf8e2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRS6VHUC%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDf71xG7Tmg0B%2FpleM0LrGRnUlHURgqQYxOZYPQengq6wIgNHCYDK3e0vqp8N0yay6zaMoplwYT9yL7ulVjPWAyU08q%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDI5P4sfeKCh62MT0EyrcA%2BCBpl%2Bgitm5jFt7oO9ukBTtO8VvgdUswjasFLN9GSI1p04DrCqJXdXUwflhcj0u%2BRJkpU%2BYCjXp%2BWNrOrnwU8omocjFZ6MUbLFd1LrGcaRsv2quXmVH22Rw%2F3g7QsMigJlcd0znmg0bXqdkX9exYox2mrwl%2FG8dwbnA5sWZ%2BQQPb%2FgQYWJqnLh9HIDW95kyIyffpP9TK9VIQxtEsHSX%2FEvcjTowN1GBDpP4t1UsaOEvHUFl2cn0a9fSgRKP%2BYWqz0U6b2Rcqa1nNEQgctqNJjL6wrLVsgiuYe3DW1tHGHKN%2FjGpmaqDWuvdIECQJWlAUYnH7I7gC88ZLyswBEon8YmmZ%2F5LBwjQ26Ti8A9AFSSG%2FC5%2FNpj1CHTaSRNBrvAGZUy1ALkLU7uQG7Tlu9FCWFeXMMeCjrtA7ySoMAYYZ%2BvdWT%2BQGLEngjh%2BuU4IM%2F%2Fa4Q0E9tz73w40XUhF1HPwj8X3VKG9QJ7fVpTHwPAILFFrGdJrsLAwQgvsM1BI7CsMUhNFUm%2Fi%2FzvIHFxhxoDej%2FAib5fJJSzYhAcan74QfuPKzRJcPQtHdgg5Wpuqfhd6AhgBzP0E6dUAYP%2Fo4rkGAJPRkqI%2BiKPgyhcSbX3PHY0oBwTjLAxG92j31GAjMLu7lcwGOqUBw6MIdGKQpN1T6wRrkMN%2FZFK4KArYJoWjXCrl74pI14EcksnbtukcFXA%2F5CjjYM%2FCAO01bcr0Lq4a1Nod74fGn%2BF%2Fsy0BgifhHkOeAfHRG2tJPWY7A8KlzPouekRcxMcNXYIAtzBOqAoUvkstpt5NUS2Rv0Vwp5U%2FA0bSSWaAFHu%2Figjf5OciQWXsB2vEicj7NM%2FjJ7y0K7q%2FM3WR%2FTmQZnGnU4SW&X-Amz-Signature=546a9a8f65f1acc295473bd4d531d3f6632f301c4203c621f6dcfcce6c766ebf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRS6VHUC%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDf71xG7Tmg0B%2FpleM0LrGRnUlHURgqQYxOZYPQengq6wIgNHCYDK3e0vqp8N0yay6zaMoplwYT9yL7ulVjPWAyU08q%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDI5P4sfeKCh62MT0EyrcA%2BCBpl%2Bgitm5jFt7oO9ukBTtO8VvgdUswjasFLN9GSI1p04DrCqJXdXUwflhcj0u%2BRJkpU%2BYCjXp%2BWNrOrnwU8omocjFZ6MUbLFd1LrGcaRsv2quXmVH22Rw%2F3g7QsMigJlcd0znmg0bXqdkX9exYox2mrwl%2FG8dwbnA5sWZ%2BQQPb%2FgQYWJqnLh9HIDW95kyIyffpP9TK9VIQxtEsHSX%2FEvcjTowN1GBDpP4t1UsaOEvHUFl2cn0a9fSgRKP%2BYWqz0U6b2Rcqa1nNEQgctqNJjL6wrLVsgiuYe3DW1tHGHKN%2FjGpmaqDWuvdIECQJWlAUYnH7I7gC88ZLyswBEon8YmmZ%2F5LBwjQ26Ti8A9AFSSG%2FC5%2FNpj1CHTaSRNBrvAGZUy1ALkLU7uQG7Tlu9FCWFeXMMeCjrtA7ySoMAYYZ%2BvdWT%2BQGLEngjh%2BuU4IM%2F%2Fa4Q0E9tz73w40XUhF1HPwj8X3VKG9QJ7fVpTHwPAILFFrGdJrsLAwQgvsM1BI7CsMUhNFUm%2Fi%2FzvIHFxhxoDej%2FAib5fJJSzYhAcan74QfuPKzRJcPQtHdgg5Wpuqfhd6AhgBzP0E6dUAYP%2Fo4rkGAJPRkqI%2BiKPgyhcSbX3PHY0oBwTjLAxG92j31GAjMLu7lcwGOqUBw6MIdGKQpN1T6wRrkMN%2FZFK4KArYJoWjXCrl74pI14EcksnbtukcFXA%2F5CjjYM%2FCAO01bcr0Lq4a1Nod74fGn%2BF%2Fsy0BgifhHkOeAfHRG2tJPWY7A8KlzPouekRcxMcNXYIAtzBOqAoUvkstpt5NUS2Rv0Vwp5U%2FA0bSSWaAFHu%2Figjf5OciQWXsB2vEicj7NM%2FjJ7y0K7q%2FM3WR%2FTmQZnGnU4SW&X-Amz-Signature=6d360f1cc825d6abe074600995316d595f312b53355d57432976db449992033a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

