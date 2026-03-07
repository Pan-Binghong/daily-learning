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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WE2DCFY2%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T032046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCbwnqQraaHGcbbk3SytGolr9DmG%2BYrc4ayP9Wy2MfiGgIhAMtwzdMaDbywagF2vFJARsvno1zqsDAmI3K0XCXTCgUJKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlLRH9qDV116AM5RIq3ANcIjmtpDOXcLB3wmalLj9pwkYsBnzAoZ%2BC5c7%2BdBJIC8KMudo%2BSWOIus774Gmk768Rd45g84HZMG4RnhmVim1A9gWPwmZm%2Bn3L6Lti8HN2%2B86q8rwKkU1BbB0M9AokPj3Ph5SWAS00fZg0KGLw7RpAmyX91BR%2Bpgt9%2BWBR3jdti9Pi5gcZ9GeTXaDfDh0cufdzoWBlYvmi0CqEUhhvj4W7EmJyKejRGYFd17xFCQnmy5EenzOdartDpbf2G9iXUg28cNAPdJSZPJM1l1d8y1zDpqqob5lQZQ4s6aqBw1RugpYWQuH2vt6YOP7iTrafWqdHkfWoiwtqdWaG0YMyOxENt94mdVqOmufef5OzJ1LoHridRaMNIiJ4oywgVsnGP4fXqxBFXdEYUy5NjZM0XCwqRq0l7R80i1i9oeZSE6lPqHxRuZbV5SlUHTZ2846MIhPvRTULMzRqGQtS2rnhdQQyV0WJdmmu23EF0%2FKsRDOgKG7%2FO%2BpEHPpbJsvfE%2BbGJIz%2B4%2Fan3tdBYBEzHWx7a1ai0TzoGybNj%2B98IKRqSeAgtmO64DKWV%2BKzJ42hYmXcIAwWMkV1NNyBLrJpYSkCQm%2FGWYss1WNAYhK%2FPrBx1ZgyIlwmB9ZezZ96WdCk8TDNk67NBjqkASlnY3hDQDIcmLrquK7YnCqIkeIfvrBVGlQEELrpTERyVigjNIC5jk2mIUbVuUh2t7b2PsrX9Tk9GpMI5oNy4QtRxFd25%2FlLRmc9pefezYaMCDF1cYPzutYGkzCQBvkki70TfTeeWUCLRLQyH1sHQ%2BMX8uuHNcdupDBt2HupqOvggqx%2F8DznF78n8I8uqc4fU8z32SVMtMcl1FeV7SGpGTfOQ75F&X-Amz-Signature=d7d3fc3e6c6d890153ec91a76541c2c976c204c98d7096f8d40568b9a3637b81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WE2DCFY2%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T032046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCbwnqQraaHGcbbk3SytGolr9DmG%2BYrc4ayP9Wy2MfiGgIhAMtwzdMaDbywagF2vFJARsvno1zqsDAmI3K0XCXTCgUJKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlLRH9qDV116AM5RIq3ANcIjmtpDOXcLB3wmalLj9pwkYsBnzAoZ%2BC5c7%2BdBJIC8KMudo%2BSWOIus774Gmk768Rd45g84HZMG4RnhmVim1A9gWPwmZm%2Bn3L6Lti8HN2%2B86q8rwKkU1BbB0M9AokPj3Ph5SWAS00fZg0KGLw7RpAmyX91BR%2Bpgt9%2BWBR3jdti9Pi5gcZ9GeTXaDfDh0cufdzoWBlYvmi0CqEUhhvj4W7EmJyKejRGYFd17xFCQnmy5EenzOdartDpbf2G9iXUg28cNAPdJSZPJM1l1d8y1zDpqqob5lQZQ4s6aqBw1RugpYWQuH2vt6YOP7iTrafWqdHkfWoiwtqdWaG0YMyOxENt94mdVqOmufef5OzJ1LoHridRaMNIiJ4oywgVsnGP4fXqxBFXdEYUy5NjZM0XCwqRq0l7R80i1i9oeZSE6lPqHxRuZbV5SlUHTZ2846MIhPvRTULMzRqGQtS2rnhdQQyV0WJdmmu23EF0%2FKsRDOgKG7%2FO%2BpEHPpbJsvfE%2BbGJIz%2B4%2Fan3tdBYBEzHWx7a1ai0TzoGybNj%2B98IKRqSeAgtmO64DKWV%2BKzJ42hYmXcIAwWMkV1NNyBLrJpYSkCQm%2FGWYss1WNAYhK%2FPrBx1ZgyIlwmB9ZezZ96WdCk8TDNk67NBjqkASlnY3hDQDIcmLrquK7YnCqIkeIfvrBVGlQEELrpTERyVigjNIC5jk2mIUbVuUh2t7b2PsrX9Tk9GpMI5oNy4QtRxFd25%2FlLRmc9pefezYaMCDF1cYPzutYGkzCQBvkki70TfTeeWUCLRLQyH1sHQ%2BMX8uuHNcdupDBt2HupqOvggqx%2F8DznF78n8I8uqc4fU8z32SVMtMcl1FeV7SGpGTfOQ75F&X-Amz-Signature=a8122c703db84e6cbbb064d28d4033f28c4be516b7c73dca93c123155ff946ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WE2DCFY2%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T032046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCbwnqQraaHGcbbk3SytGolr9DmG%2BYrc4ayP9Wy2MfiGgIhAMtwzdMaDbywagF2vFJARsvno1zqsDAmI3K0XCXTCgUJKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlLRH9qDV116AM5RIq3ANcIjmtpDOXcLB3wmalLj9pwkYsBnzAoZ%2BC5c7%2BdBJIC8KMudo%2BSWOIus774Gmk768Rd45g84HZMG4RnhmVim1A9gWPwmZm%2Bn3L6Lti8HN2%2B86q8rwKkU1BbB0M9AokPj3Ph5SWAS00fZg0KGLw7RpAmyX91BR%2Bpgt9%2BWBR3jdti9Pi5gcZ9GeTXaDfDh0cufdzoWBlYvmi0CqEUhhvj4W7EmJyKejRGYFd17xFCQnmy5EenzOdartDpbf2G9iXUg28cNAPdJSZPJM1l1d8y1zDpqqob5lQZQ4s6aqBw1RugpYWQuH2vt6YOP7iTrafWqdHkfWoiwtqdWaG0YMyOxENt94mdVqOmufef5OzJ1LoHridRaMNIiJ4oywgVsnGP4fXqxBFXdEYUy5NjZM0XCwqRq0l7R80i1i9oeZSE6lPqHxRuZbV5SlUHTZ2846MIhPvRTULMzRqGQtS2rnhdQQyV0WJdmmu23EF0%2FKsRDOgKG7%2FO%2BpEHPpbJsvfE%2BbGJIz%2B4%2Fan3tdBYBEzHWx7a1ai0TzoGybNj%2B98IKRqSeAgtmO64DKWV%2BKzJ42hYmXcIAwWMkV1NNyBLrJpYSkCQm%2FGWYss1WNAYhK%2FPrBx1ZgyIlwmB9ZezZ96WdCk8TDNk67NBjqkASlnY3hDQDIcmLrquK7YnCqIkeIfvrBVGlQEELrpTERyVigjNIC5jk2mIUbVuUh2t7b2PsrX9Tk9GpMI5oNy4QtRxFd25%2FlLRmc9pefezYaMCDF1cYPzutYGkzCQBvkki70TfTeeWUCLRLQyH1sHQ%2BMX8uuHNcdupDBt2HupqOvggqx%2F8DznF78n8I8uqc4fU8z32SVMtMcl1FeV7SGpGTfOQ75F&X-Amz-Signature=379c079d536a19345f10f9780a95eb8dd494a87ddab0af416574330f2a548782&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

