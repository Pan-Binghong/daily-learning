---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGL3WVZW%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041506Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAv%2BvQANZUbh8Z8U1miuJL2A3lu68BWfQI5rthAeyVlfAiEA%2F%2F2Xc4Gcq1CKkNghNFzSDBZTNG%2BjF5Z3qCswhrN2CA8q%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDIXZOLKDTs15DTE%2BcircAwgknH2BwbWNTHzdilFPk5kGxYFM1IX%2F23PI3p0aHYsfmNSO2Kvis11Pr3PIPuVUohpxChX4goo5LZfjarRERmT5HTMyKgAgqRIUg%2BQ%2FsZV3EY5fvpBn3NUiZi%2FoZnnX7pMMz9j4OKQLYl1gNGG1iafsfrsd0uY1kh%2BG86MfDwVMCuuMcGniO%2BCalWgkLy1yyF0Fl3USl9duZC5mJWfmjoIYY1GZVMUTwyQoCQ85G8VjdkC8e5N%2Bs6rOGka%2BxlJi6d5NCnXjojftlbF4Sl5NvY%2B%2BhKcIjfQMxXKXQWZnU147P3ONoODmwgbz3wivHUN5wcyW7yshd69xblkHgQl8htA%2FzTyinpRxWMEORhOmAPEa187U0J5J2jHSYOXgk%2FjiYHI2HMCnNRleKpfslgfGZ%2Bzg1Nmw0by87xlTnAQS133U3G8%2BuxuwS6LebmHPdk4tKxcjkgvpSdpOdML8JO%2BYQ0qZ4Zg1otlnkvC0doDIfGROUF4e3Ok6fvZN3Wb1gvb0NvpMvk9O8A4dmgbVA8rIWvOId6nOZLStC3tnVfjR8ZxEKIlfhUGBDgl9aqL%2BTBZjsnKT2UMr7FxyG8kouDu1zm02NiCZB8F7PB6eV3CpRY6G3NkOV%2FbgUCdZGZ0sMPagps8GOqUB5I6hBzVb0jCMwBK5r1oGPxcB8A1any5wegGdBGjpShO50LmHjXvncAxsH85sk07TiqqOaYtuzhFI7iETmLX0y2bMEni9KyaTStw1cocty16Y%2BGIc6MnzhcZUMrGsikwzGxlfVnOtGLaPF0wt1CJoMBi0aQMx9A8ZtdHQYjufokWXK%2FNOLfEP70E%2Bdhtwj4Z9yegNdTpam6YKsUZEgllmsl9i3qCi&X-Amz-Signature=0c6a8d54421ecb4d0877ac5e7faca92d3dfb5a67eda79aafb5c229e787a50602&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

