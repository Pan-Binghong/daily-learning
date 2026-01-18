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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ND3VAN3%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9RvSBpx0LEBxqZr0ZXl17WArDpO26TlqIlJsh58O7VQIhAJCz45ec%2BIGUeQrlaUsnzh4Vr%2BMwtMa10lSv%2B09ksJS8Kv8DCHMQABoMNjM3NDIzMTgzODA1IgzOiwr0xxvseIAhBiYq3APEYEpyFiXVd1SYHtzyTGQZtAg3Bt5LEcCoQWw73yK%2FL4MG8PSa%2B%2B7Hp7BrZ9f0eQlUIiDb%2BK%2FmwPkKxyh1UUoXhbRVn3k0bAvdr9TIuI1h0zuBBJNbaLd9u3eePuirW1IvXwVSVpA0rphenL0UcQsGP5kVXdiNPWXXMexQUoruQJQN8OIKDueFKZVLHlqtNrLNK8mBk5F%2BKXCvDtsvyA%2FhODIG3xuKjoahonio6ONVyf%2BRCvAYJ8NgScdugTJ%2B2wbP6SVd88US2d%2FknV6U3AJni8MpEQIJgdkG%2B%2FUIAsFYtC4VSbMpCDk7ajqnAQcHsQq862ahGLFzozoMZovnYSlGvh8Fu2E7Dmwi33KN6cBUw3BxnhehXg2p9hN0fbce5benbQwG7pAGbF0BYtgh5oRA6QYX2pPKKbQ5IXN3UlDv9cjdIcH4D%2FkInvndWiH0p65fcbpblygZm%2F3SVstP2Oa7SvRy9LBKGLk1o0x4xD1QeKIybCUOQKrYboeYnnxX%2BQ5NYS9cJMJQEyEXCXrfdlEGVAUDRIWrTYsuHGixKdP1QXJOmOc32y5ywKpMZHGw2qr996%2Fx6A59i41rQjbuDobt3iF5m7BOvJ0HMHalDiqI2bjPXf3JhAXajgbPpTCSgrHLBjqkAVHHc12ZFGCImQYNH0L9d4Oxsa9WcG5sojbFaPPqZgLuKlyu%2F7vBKe%2BdMJXYVyGCxWgWlkIkyzn5kKhUsDdQOg%2FNSbTedn8MgyMB4KJTOyHDFLQSOqPMEesMVA0WODdh6dpchhlnKWmEhQEa94q3kYq0KJS6iGES%2B1Uh66U653%2BKP13sexbE1pSNKUZpoxR0yeWC%2Bwfq33m3yfJQqmqqy3BjmW2J&X-Amz-Signature=f3cfbc8229f2d30f23b0c915937f090792750e23db18ddb8e39950f45017fc92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ND3VAN3%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9RvSBpx0LEBxqZr0ZXl17WArDpO26TlqIlJsh58O7VQIhAJCz45ec%2BIGUeQrlaUsnzh4Vr%2BMwtMa10lSv%2B09ksJS8Kv8DCHMQABoMNjM3NDIzMTgzODA1IgzOiwr0xxvseIAhBiYq3APEYEpyFiXVd1SYHtzyTGQZtAg3Bt5LEcCoQWw73yK%2FL4MG8PSa%2B%2B7Hp7BrZ9f0eQlUIiDb%2BK%2FmwPkKxyh1UUoXhbRVn3k0bAvdr9TIuI1h0zuBBJNbaLd9u3eePuirW1IvXwVSVpA0rphenL0UcQsGP5kVXdiNPWXXMexQUoruQJQN8OIKDueFKZVLHlqtNrLNK8mBk5F%2BKXCvDtsvyA%2FhODIG3xuKjoahonio6ONVyf%2BRCvAYJ8NgScdugTJ%2B2wbP6SVd88US2d%2FknV6U3AJni8MpEQIJgdkG%2B%2FUIAsFYtC4VSbMpCDk7ajqnAQcHsQq862ahGLFzozoMZovnYSlGvh8Fu2E7Dmwi33KN6cBUw3BxnhehXg2p9hN0fbce5benbQwG7pAGbF0BYtgh5oRA6QYX2pPKKbQ5IXN3UlDv9cjdIcH4D%2FkInvndWiH0p65fcbpblygZm%2F3SVstP2Oa7SvRy9LBKGLk1o0x4xD1QeKIybCUOQKrYboeYnnxX%2BQ5NYS9cJMJQEyEXCXrfdlEGVAUDRIWrTYsuHGixKdP1QXJOmOc32y5ywKpMZHGw2qr996%2Fx6A59i41rQjbuDobt3iF5m7BOvJ0HMHalDiqI2bjPXf3JhAXajgbPpTCSgrHLBjqkAVHHc12ZFGCImQYNH0L9d4Oxsa9WcG5sojbFaPPqZgLuKlyu%2F7vBKe%2BdMJXYVyGCxWgWlkIkyzn5kKhUsDdQOg%2FNSbTedn8MgyMB4KJTOyHDFLQSOqPMEesMVA0WODdh6dpchhlnKWmEhQEa94q3kYq0KJS6iGES%2B1Uh66U653%2BKP13sexbE1pSNKUZpoxR0yeWC%2Bwfq33m3yfJQqmqqy3BjmW2J&X-Amz-Signature=02abfc58ae4eb096adb2577d1d159faa53a691bd371c9fb57fe42c2ede2c0ddd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ND3VAN3%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9RvSBpx0LEBxqZr0ZXl17WArDpO26TlqIlJsh58O7VQIhAJCz45ec%2BIGUeQrlaUsnzh4Vr%2BMwtMa10lSv%2B09ksJS8Kv8DCHMQABoMNjM3NDIzMTgzODA1IgzOiwr0xxvseIAhBiYq3APEYEpyFiXVd1SYHtzyTGQZtAg3Bt5LEcCoQWw73yK%2FL4MG8PSa%2B%2B7Hp7BrZ9f0eQlUIiDb%2BK%2FmwPkKxyh1UUoXhbRVn3k0bAvdr9TIuI1h0zuBBJNbaLd9u3eePuirW1IvXwVSVpA0rphenL0UcQsGP5kVXdiNPWXXMexQUoruQJQN8OIKDueFKZVLHlqtNrLNK8mBk5F%2BKXCvDtsvyA%2FhODIG3xuKjoahonio6ONVyf%2BRCvAYJ8NgScdugTJ%2B2wbP6SVd88US2d%2FknV6U3AJni8MpEQIJgdkG%2B%2FUIAsFYtC4VSbMpCDk7ajqnAQcHsQq862ahGLFzozoMZovnYSlGvh8Fu2E7Dmwi33KN6cBUw3BxnhehXg2p9hN0fbce5benbQwG7pAGbF0BYtgh5oRA6QYX2pPKKbQ5IXN3UlDv9cjdIcH4D%2FkInvndWiH0p65fcbpblygZm%2F3SVstP2Oa7SvRy9LBKGLk1o0x4xD1QeKIybCUOQKrYboeYnnxX%2BQ5NYS9cJMJQEyEXCXrfdlEGVAUDRIWrTYsuHGixKdP1QXJOmOc32y5ywKpMZHGw2qr996%2Fx6A59i41rQjbuDobt3iF5m7BOvJ0HMHalDiqI2bjPXf3JhAXajgbPpTCSgrHLBjqkAVHHc12ZFGCImQYNH0L9d4Oxsa9WcG5sojbFaPPqZgLuKlyu%2F7vBKe%2BdMJXYVyGCxWgWlkIkyzn5kKhUsDdQOg%2FNSbTedn8MgyMB4KJTOyHDFLQSOqPMEesMVA0WODdh6dpchhlnKWmEhQEa94q3kYq0KJS6iGES%2B1Uh66U653%2BKP13sexbE1pSNKUZpoxR0yeWC%2Bwfq33m3yfJQqmqqy3BjmW2J&X-Amz-Signature=fea44c77e312e46eb2170a69bbd601a43f4efc5eb9b383363bafd429cdf15f51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

