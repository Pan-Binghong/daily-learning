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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WKQRHM3%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIQDTXjNYsV7fVjwWTGrHohnXMEcHsCkNwc1SHrXIvBHjUwIgUjZhF%2B48jZzSr2WcCGwsJjvy%2FqZi8Tzy7bf9tEw0oV0qiAQI8f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJe8H5qxODIbopt0ZCrcAzx9L5MMHcTpzagF2RslPAtwKIkdjc6nFVNyR%2Bx29m3CxQIjkwEbyHizGVKEC1Y%2Fi9ee8RSLK4Mj0AfQt%2BJzJ6pO0mZf5jtgixNBXMsvjtbvOaVye4S4lTBh50YIDdEsALJSRXmF60baoqnuYTUlfVTFVWr7eDMYrjpBe6xeqqbvhefzzC0qQj%2Fv%2BtaBRaB5lOtUb%2B1YIctG5sdxNW8ZqzQNR2aLVJBG%2BEYvcLoiDNbwjI%2FDV1vUHut0WyYjQu4ZMWwDsOCRypNIDkpHhFd7LIZFnPF73JC71td0FQeDsDncbFtnOK6LnxEKkKe1qj8qQI02xp8o7Ckou8EysTMlGxku%2BkuXrR2kvjBFQ%2Fy6%2BeBXP7JBdEn8vEbyS86E3DUPvSadmLBMMfYldgL%2B8E%2FjbN%2BmLQY66FJM57tID82IpkZFUyRJ%2B7oylTCQBkUPdOEaWkvhgztFgZp9XbRayYKjeGEJ%2BvhkOyJaP6BmUYkgnb5zXXV3ptCWWerfJskUOUmeYuu8sWvgJ1GrN5DA3dGLSau2tQfU63tViEqUGyy2gQCZ144MRse6D8U51%2BCAQAfaZWb%2F92X4sO224ix19Yd6AkAV3Fciv4V7eH3k6xHT78%2BJybD8kyKoWf0QNr2zMJmI3MoGOqUBR8YbW%2FJg3jbiSocAtqcqHvsXzPwcbTRy7VUx8rluFA%2BZ2MbAtTYj3M68N5DhJB4DFoAOY85jUCYwLfuj4e%2FRqNHt7tRzgm4jbsVU6H7%2FUNocZsxy0rTkRprwBXVMkEzpGQdBEINVsnxE8WwbGTMRzjU26BBUG%2Br8hWSfZba%2Ff8LDiLz2kWPefARC%2BW%2BRESELocODU%2FxgkduJZdtnSYUNTY%2BS5SVF&X-Amz-Signature=4fc7645b047a1eb8968d5a7f348f113a1edf6d400dd952253bb30067f7892016&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

