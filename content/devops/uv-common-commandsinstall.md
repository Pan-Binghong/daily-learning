---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
标签:
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SNSIRZA%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDL6EmYs5aNMJYsnQwYDIUy1skBwzNJIooREksWXdkqkAIgc8BYBQEsjaYbV0ZrwlH7lgNrG6HTk8a9u5vYTbK3psoqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI2ZP2UmWijpCBijNCrcA27Q3tPA0dt2M2tEcjeGY10Y7%2FrFl5o%2FciKT8uWyh%2F668sfDSGLtrwhLgIuRNgOaYLc8VhETty12EWuIof3ZfT%2FHFsaAH%2B3US9NfJ0BvdKxN7OZVlQwXBguKi%2F%2BtqyaNiwKasHWl8B1Tl%2Ff8EF31CW8bnfOakea3SeY8NK6fSrcA5BYN8avrWbWvJZj2ySe5zy%2FyphtP9yfet0gU6HRf8AjPGxj8BOYlmSgGhB%2BEG6fb2ly6Py%2BBaUdEHQilqvy9Ni7u34XGiFVx%2BmzNRezd%2BEy76DbgPWII0V0g4hJPNqLIMWlFXpyshyBIUrbJk6RxXI7VqCUVINKJB%2BG5eX2fajDdvU4y%2F3h2%2Blmkebu%2BYaK1MjPdf2xXmsGo%2BZJBppxlR2hbyzkuBGS%2B0yFEI3jKle9v86iw%2BVnm61FtyJJajICZ4o8KQEnrfznKxaNQQKUpZYzU8jiUCx%2FMLOY15q2bwhbMPlZM3VMv%2F%2BnhdWx2MKa0SY5%2BbOeRBctDZT7y5sBOq9uZ%2BdZ9fhKFQyAfl0hGgoluFo4rrEPoKR7MsLLSuhYkf%2BGF%2BFGqeVYDg2l8Iu8ojDAUdd3bZSQ1OOZ%2FNEQyS%2FLF1dampH8tOfsqg9DNVguMdV1B8ZHGf6z3%2BXh4MNCirMgGOqUBY%2BxLwNisFPPzcPjTSNTINXMLehsad7F2Ervok00DktKxTWeNGeQoo4bgki7wUfJ5LOvPskwDui64RYj%2FHLaoUFKEGgioO3tBohcN4PFb93qqUCQHIa0NltxP6neri6zsiQsUCscxht9KiLpiG1zYE49yBSXT93E1%2FaT1wSL9sJEeOq7z0hFLWIF%2FQMVMwWuIxOfaUmAuG6Rn3kVjEsENskrdlfy2&X-Amz-Signature=1f9e98692b7d4eaf2c5c8b58a971f1ff0f0b51f4fa2d731a4d92b3ae0fcfacd1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SNSIRZA%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDL6EmYs5aNMJYsnQwYDIUy1skBwzNJIooREksWXdkqkAIgc8BYBQEsjaYbV0ZrwlH7lgNrG6HTk8a9u5vYTbK3psoqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI2ZP2UmWijpCBijNCrcA27Q3tPA0dt2M2tEcjeGY10Y7%2FrFl5o%2FciKT8uWyh%2F668sfDSGLtrwhLgIuRNgOaYLc8VhETty12EWuIof3ZfT%2FHFsaAH%2B3US9NfJ0BvdKxN7OZVlQwXBguKi%2F%2BtqyaNiwKasHWl8B1Tl%2Ff8EF31CW8bnfOakea3SeY8NK6fSrcA5BYN8avrWbWvJZj2ySe5zy%2FyphtP9yfet0gU6HRf8AjPGxj8BOYlmSgGhB%2BEG6fb2ly6Py%2BBaUdEHQilqvy9Ni7u34XGiFVx%2BmzNRezd%2BEy76DbgPWII0V0g4hJPNqLIMWlFXpyshyBIUrbJk6RxXI7VqCUVINKJB%2BG5eX2fajDdvU4y%2F3h2%2Blmkebu%2BYaK1MjPdf2xXmsGo%2BZJBppxlR2hbyzkuBGS%2B0yFEI3jKle9v86iw%2BVnm61FtyJJajICZ4o8KQEnrfznKxaNQQKUpZYzU8jiUCx%2FMLOY15q2bwhbMPlZM3VMv%2F%2BnhdWx2MKa0SY5%2BbOeRBctDZT7y5sBOq9uZ%2BdZ9fhKFQyAfl0hGgoluFo4rrEPoKR7MsLLSuhYkf%2BGF%2BFGqeVYDg2l8Iu8ojDAUdd3bZSQ1OOZ%2FNEQyS%2FLF1dampH8tOfsqg9DNVguMdV1B8ZHGf6z3%2BXh4MNCirMgGOqUBY%2BxLwNisFPPzcPjTSNTINXMLehsad7F2Ervok00DktKxTWeNGeQoo4bgki7wUfJ5LOvPskwDui64RYj%2FHLaoUFKEGgioO3tBohcN4PFb93qqUCQHIa0NltxP6neri6zsiQsUCscxht9KiLpiG1zYE49yBSXT93E1%2FaT1wSL9sJEeOq7z0hFLWIF%2FQMVMwWuIxOfaUmAuG6Rn3kVjEsENskrdlfy2&X-Amz-Signature=86b146b1d18de11d83548b9a6cbb056e91969e87dcb596a0c5c2044fdce6b2c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SNSIRZA%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDL6EmYs5aNMJYsnQwYDIUy1skBwzNJIooREksWXdkqkAIgc8BYBQEsjaYbV0ZrwlH7lgNrG6HTk8a9u5vYTbK3psoqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI2ZP2UmWijpCBijNCrcA27Q3tPA0dt2M2tEcjeGY10Y7%2FrFl5o%2FciKT8uWyh%2F668sfDSGLtrwhLgIuRNgOaYLc8VhETty12EWuIof3ZfT%2FHFsaAH%2B3US9NfJ0BvdKxN7OZVlQwXBguKi%2F%2BtqyaNiwKasHWl8B1Tl%2Ff8EF31CW8bnfOakea3SeY8NK6fSrcA5BYN8avrWbWvJZj2ySe5zy%2FyphtP9yfet0gU6HRf8AjPGxj8BOYlmSgGhB%2BEG6fb2ly6Py%2BBaUdEHQilqvy9Ni7u34XGiFVx%2BmzNRezd%2BEy76DbgPWII0V0g4hJPNqLIMWlFXpyshyBIUrbJk6RxXI7VqCUVINKJB%2BG5eX2fajDdvU4y%2F3h2%2Blmkebu%2BYaK1MjPdf2xXmsGo%2BZJBppxlR2hbyzkuBGS%2B0yFEI3jKle9v86iw%2BVnm61FtyJJajICZ4o8KQEnrfznKxaNQQKUpZYzU8jiUCx%2FMLOY15q2bwhbMPlZM3VMv%2F%2BnhdWx2MKa0SY5%2BbOeRBctDZT7y5sBOq9uZ%2BdZ9fhKFQyAfl0hGgoluFo4rrEPoKR7MsLLSuhYkf%2BGF%2BFGqeVYDg2l8Iu8ojDAUdd3bZSQ1OOZ%2FNEQyS%2FLF1dampH8tOfsqg9DNVguMdV1B8ZHGf6z3%2BXh4MNCirMgGOqUBY%2BxLwNisFPPzcPjTSNTINXMLehsad7F2Ervok00DktKxTWeNGeQoo4bgki7wUfJ5LOvPskwDui64RYj%2FHLaoUFKEGgioO3tBohcN4PFb93qqUCQHIa0NltxP6neri6zsiQsUCscxht9KiLpiG1zYE49yBSXT93E1%2FaT1wSL9sJEeOq7z0hFLWIF%2FQMVMwWuIxOfaUmAuG6Rn3kVjEsENskrdlfy2&X-Amz-Signature=3919dbbe0a683c2e340a1a53a4eed5481f2bb8ee85568a13fc082d8d289d09aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

