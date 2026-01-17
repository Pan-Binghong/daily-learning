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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LHB623R%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHR4syJplTLZj8Iw8l3kx0zlpNtQD0PeJYtAmGyda4fQIhAKuMacagP2jZEfKjc5ofzHxkDxfvUxv9gtmdY7UIShjVKv8DCFsQABoMNjM3NDIzMTgzODA1IgzqF%2B%2BcQ4AmHMK02Ucq3AP85avpTigcCzIN2YGrOfVVmRl65v1VzS5sPg5Zas878exU7GR7qmSjGim9szamD3qi%2FQ3eSaDl7g4KDXddz6FIB1RWFFeveCBTawMQ7MYFxlKuw3XFvc18hhaFAoaidIt8mM7X1s6QpzgjffPS%2FVy2t5YusUaoI7mKzyi%2FEzPl3ygCg6rjOC3Wv0ZrbMpdnw%2BxycwcRN1FoirJAHWoAud9Z53lXV%2FXcRa%2FmmaAdiu2TJIhue4hMMElYqP6tYrLXeRBR0QY2ynrKJRojo5x70NJAgSaXzxUiBTorohNysWJaVLkwrZHETZ4Rskn1%2FMqXZkIIDri6DrQlEeyJQujWLtiJMhSeIWMa5EaR7E4H482Ua%2F0UOsusVf%2B5CoQ1%2FWpK%2F%2FF0sShqpeRZLCCYi7LAxP2P2eZKIcCL5rreixL9ANVVMARO2jOv3NLOwhtaZMCeIi8%2BwgfJzvWZvTUuUmH7IAXKTNuaUgbO5BAVQEWswS%2FYr80H0p9JRKDSJIoYX5ujSM0Af99cqqC4bhLESqRB5zmg0zp1m6HMyEfu8uyOMdLcLdIBp%2Blw4BqAj%2FuPQlTj5aOXOHf%2B5PN7quczNQIhxX43CTu23pa7efxyZ9%2BZgKUMXqfms%2FUhVDbGtZw4TDg0avLBjqkAX529%2FbcEbDh03iPf6HFkZUs7WKnfDBhzmNPTWF%2BtaKmnD15e2eH22FKvW0z9OYTKE3VSbrLGiFONjioniK6NSsyi5Z%2BjGEIp9uxy4KINBDJ%2BZvVdxsTGtJG0xc%2F4RGO1bPFCHJcS2Dkz44N1qx%2FXjX2LeBG3p08BCgW4QS3siatPHBcE%2FxzXIWqNcjanxa4YQxLHBHl15UhgDEtil8z9bhuFcSK&X-Amz-Signature=1fcc029d09d015119d9675496291b32f0dd0607ba24aba36d26cbc984b0816f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LHB623R%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHR4syJplTLZj8Iw8l3kx0zlpNtQD0PeJYtAmGyda4fQIhAKuMacagP2jZEfKjc5ofzHxkDxfvUxv9gtmdY7UIShjVKv8DCFsQABoMNjM3NDIzMTgzODA1IgzqF%2B%2BcQ4AmHMK02Ucq3AP85avpTigcCzIN2YGrOfVVmRl65v1VzS5sPg5Zas878exU7GR7qmSjGim9szamD3qi%2FQ3eSaDl7g4KDXddz6FIB1RWFFeveCBTawMQ7MYFxlKuw3XFvc18hhaFAoaidIt8mM7X1s6QpzgjffPS%2FVy2t5YusUaoI7mKzyi%2FEzPl3ygCg6rjOC3Wv0ZrbMpdnw%2BxycwcRN1FoirJAHWoAud9Z53lXV%2FXcRa%2FmmaAdiu2TJIhue4hMMElYqP6tYrLXeRBR0QY2ynrKJRojo5x70NJAgSaXzxUiBTorohNysWJaVLkwrZHETZ4Rskn1%2FMqXZkIIDri6DrQlEeyJQujWLtiJMhSeIWMa5EaR7E4H482Ua%2F0UOsusVf%2B5CoQ1%2FWpK%2F%2FF0sShqpeRZLCCYi7LAxP2P2eZKIcCL5rreixL9ANVVMARO2jOv3NLOwhtaZMCeIi8%2BwgfJzvWZvTUuUmH7IAXKTNuaUgbO5BAVQEWswS%2FYr80H0p9JRKDSJIoYX5ujSM0Af99cqqC4bhLESqRB5zmg0zp1m6HMyEfu8uyOMdLcLdIBp%2Blw4BqAj%2FuPQlTj5aOXOHf%2B5PN7quczNQIhxX43CTu23pa7efxyZ9%2BZgKUMXqfms%2FUhVDbGtZw4TDg0avLBjqkAX529%2FbcEbDh03iPf6HFkZUs7WKnfDBhzmNPTWF%2BtaKmnD15e2eH22FKvW0z9OYTKE3VSbrLGiFONjioniK6NSsyi5Z%2BjGEIp9uxy4KINBDJ%2BZvVdxsTGtJG0xc%2F4RGO1bPFCHJcS2Dkz44N1qx%2FXjX2LeBG3p08BCgW4QS3siatPHBcE%2FxzXIWqNcjanxa4YQxLHBHl15UhgDEtil8z9bhuFcSK&X-Amz-Signature=ad872606deaef9bba208ed7f38fb3f024eb97d10f769522d245023e29cf78125&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LHB623R%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHR4syJplTLZj8Iw8l3kx0zlpNtQD0PeJYtAmGyda4fQIhAKuMacagP2jZEfKjc5ofzHxkDxfvUxv9gtmdY7UIShjVKv8DCFsQABoMNjM3NDIzMTgzODA1IgzqF%2B%2BcQ4AmHMK02Ucq3AP85avpTigcCzIN2YGrOfVVmRl65v1VzS5sPg5Zas878exU7GR7qmSjGim9szamD3qi%2FQ3eSaDl7g4KDXddz6FIB1RWFFeveCBTawMQ7MYFxlKuw3XFvc18hhaFAoaidIt8mM7X1s6QpzgjffPS%2FVy2t5YusUaoI7mKzyi%2FEzPl3ygCg6rjOC3Wv0ZrbMpdnw%2BxycwcRN1FoirJAHWoAud9Z53lXV%2FXcRa%2FmmaAdiu2TJIhue4hMMElYqP6tYrLXeRBR0QY2ynrKJRojo5x70NJAgSaXzxUiBTorohNysWJaVLkwrZHETZ4Rskn1%2FMqXZkIIDri6DrQlEeyJQujWLtiJMhSeIWMa5EaR7E4H482Ua%2F0UOsusVf%2B5CoQ1%2FWpK%2F%2FF0sShqpeRZLCCYi7LAxP2P2eZKIcCL5rreixL9ANVVMARO2jOv3NLOwhtaZMCeIi8%2BwgfJzvWZvTUuUmH7IAXKTNuaUgbO5BAVQEWswS%2FYr80H0p9JRKDSJIoYX5ujSM0Af99cqqC4bhLESqRB5zmg0zp1m6HMyEfu8uyOMdLcLdIBp%2Blw4BqAj%2FuPQlTj5aOXOHf%2B5PN7quczNQIhxX43CTu23pa7efxyZ9%2BZgKUMXqfms%2FUhVDbGtZw4TDg0avLBjqkAX529%2FbcEbDh03iPf6HFkZUs7WKnfDBhzmNPTWF%2BtaKmnD15e2eH22FKvW0z9OYTKE3VSbrLGiFONjioniK6NSsyi5Z%2BjGEIp9uxy4KINBDJ%2BZvVdxsTGtJG0xc%2F4RGO1bPFCHJcS2Dkz44N1qx%2FXjX2LeBG3p08BCgW4QS3siatPHBcE%2FxzXIWqNcjanxa4YQxLHBHl15UhgDEtil8z9bhuFcSK&X-Amz-Signature=a953d857e77b680ab10fca86756152df9989c7de46bb71792a5712d71f02f7dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

