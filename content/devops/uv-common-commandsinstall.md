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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XR2RCR7W%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEWnpaNRwNujRK%2BVx%2Bouel8LSsTHXKhJa0KPZrA4Cv3NAiBd1GyJ9cS22ckwNQJeC1mocU1pN4AxhzXEriL0Fo0AVyr%2FAwhPEAAaDDYzNzQyMzE4MzgwNSIMf3jaYuo3N0tlgygmKtwDKFfe3gdC69HoYRYPxi45bdKKRjStkSaEySWqpqnUDRy9a3AR6QipSpe5x01ZtLug%2B1fWIzQbjaVpxm1cA08d0Kfj%2BabbG30v7o%2BsO7tAudAZAqeu596G%2FiwB9mfL6ugxpSDtDZS7zvpEub58ObtTlIHMHxBOG6DYsJNh5V2ZC6TZBLWQDjIZx9ZL4M15yxzBFKiKMfGs88YzmHEe2mlJQNVDiTgjdzasLncDpKUcfbV7vf5qMHAcQ0xJtbzc3%2FBltrgX9wEqhnpCIHZS9Y61K3WpBfyk9hAhj89s7Yanka%2Fa7qBWBZqP33ZxChAb%2BWgsAJFOvRqpJO3A2%2FBynM4ezQdCwrMuKutru%2B0kiaXV2K637I3ZWec%2FIt3vNEBoSjqi6lu0NXEiFnlTm4DTgNSB7W5hQztGP%2FGxOrl5ZY6SYQsLipyRieCUaj1EUUM2XxZWF4n1ci8VpJhtfNu6paz0hAP7DtNZZCdPSRVUBaSMZh2T%2BA%2B0WQwajLmgBsz8kw6pYJWJEdAcT5HrgtbT8ztKEmisEfL4xXTXV2KbbxXKMTZhiRLBSV2RCvArdQk2baz3VEoX5kWlz%2FO4D3QnnyVqNwV6zVKJg5FYZt1OLiaJi4y1XIA3FrzHbbwSPxYww4zIyQY6pgEDg8XlZdqaZA2meeyeAksJMsbFOPZNZrztloXy0MS%2Bu6rYOvo5t0lsIOkKz0zQn4aXFuDS5d2fF930cRRFvWxTmRZgmI%2BDK6RQ34xUVnZSuInvceG3vd11Aj9YAuJa1dGZUe1Xd5iZ4v0pH27xEdGJevrJSp2RFQBhoM8g%2FYNoCibqMZE2AqSts%2Fd7Z3hBA03DUhuO7DbjnBlVPQsnHhPdwmE%2FItMp&X-Amz-Signature=d1231aaf7a3a6d581722628449ac95a4b86b91f042d522ec1ddc629759d0f644&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XR2RCR7W%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEWnpaNRwNujRK%2BVx%2Bouel8LSsTHXKhJa0KPZrA4Cv3NAiBd1GyJ9cS22ckwNQJeC1mocU1pN4AxhzXEriL0Fo0AVyr%2FAwhPEAAaDDYzNzQyMzE4MzgwNSIMf3jaYuo3N0tlgygmKtwDKFfe3gdC69HoYRYPxi45bdKKRjStkSaEySWqpqnUDRy9a3AR6QipSpe5x01ZtLug%2B1fWIzQbjaVpxm1cA08d0Kfj%2BabbG30v7o%2BsO7tAudAZAqeu596G%2FiwB9mfL6ugxpSDtDZS7zvpEub58ObtTlIHMHxBOG6DYsJNh5V2ZC6TZBLWQDjIZx9ZL4M15yxzBFKiKMfGs88YzmHEe2mlJQNVDiTgjdzasLncDpKUcfbV7vf5qMHAcQ0xJtbzc3%2FBltrgX9wEqhnpCIHZS9Y61K3WpBfyk9hAhj89s7Yanka%2Fa7qBWBZqP33ZxChAb%2BWgsAJFOvRqpJO3A2%2FBynM4ezQdCwrMuKutru%2B0kiaXV2K637I3ZWec%2FIt3vNEBoSjqi6lu0NXEiFnlTm4DTgNSB7W5hQztGP%2FGxOrl5ZY6SYQsLipyRieCUaj1EUUM2XxZWF4n1ci8VpJhtfNu6paz0hAP7DtNZZCdPSRVUBaSMZh2T%2BA%2B0WQwajLmgBsz8kw6pYJWJEdAcT5HrgtbT8ztKEmisEfL4xXTXV2KbbxXKMTZhiRLBSV2RCvArdQk2baz3VEoX5kWlz%2FO4D3QnnyVqNwV6zVKJg5FYZt1OLiaJi4y1XIA3FrzHbbwSPxYww4zIyQY6pgEDg8XlZdqaZA2meeyeAksJMsbFOPZNZrztloXy0MS%2Bu6rYOvo5t0lsIOkKz0zQn4aXFuDS5d2fF930cRRFvWxTmRZgmI%2BDK6RQ34xUVnZSuInvceG3vd11Aj9YAuJa1dGZUe1Xd5iZ4v0pH27xEdGJevrJSp2RFQBhoM8g%2FYNoCibqMZE2AqSts%2Fd7Z3hBA03DUhuO7DbjnBlVPQsnHhPdwmE%2FItMp&X-Amz-Signature=95fbc9a7d2a614ac46eeb97336a5eb3bfefd281f4c16d9ec012980522bd8c4b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XR2RCR7W%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEWnpaNRwNujRK%2BVx%2Bouel8LSsTHXKhJa0KPZrA4Cv3NAiBd1GyJ9cS22ckwNQJeC1mocU1pN4AxhzXEriL0Fo0AVyr%2FAwhPEAAaDDYzNzQyMzE4MzgwNSIMf3jaYuo3N0tlgygmKtwDKFfe3gdC69HoYRYPxi45bdKKRjStkSaEySWqpqnUDRy9a3AR6QipSpe5x01ZtLug%2B1fWIzQbjaVpxm1cA08d0Kfj%2BabbG30v7o%2BsO7tAudAZAqeu596G%2FiwB9mfL6ugxpSDtDZS7zvpEub58ObtTlIHMHxBOG6DYsJNh5V2ZC6TZBLWQDjIZx9ZL4M15yxzBFKiKMfGs88YzmHEe2mlJQNVDiTgjdzasLncDpKUcfbV7vf5qMHAcQ0xJtbzc3%2FBltrgX9wEqhnpCIHZS9Y61K3WpBfyk9hAhj89s7Yanka%2Fa7qBWBZqP33ZxChAb%2BWgsAJFOvRqpJO3A2%2FBynM4ezQdCwrMuKutru%2B0kiaXV2K637I3ZWec%2FIt3vNEBoSjqi6lu0NXEiFnlTm4DTgNSB7W5hQztGP%2FGxOrl5ZY6SYQsLipyRieCUaj1EUUM2XxZWF4n1ci8VpJhtfNu6paz0hAP7DtNZZCdPSRVUBaSMZh2T%2BA%2B0WQwajLmgBsz8kw6pYJWJEdAcT5HrgtbT8ztKEmisEfL4xXTXV2KbbxXKMTZhiRLBSV2RCvArdQk2baz3VEoX5kWlz%2FO4D3QnnyVqNwV6zVKJg5FYZt1OLiaJi4y1XIA3FrzHbbwSPxYww4zIyQY6pgEDg8XlZdqaZA2meeyeAksJMsbFOPZNZrztloXy0MS%2Bu6rYOvo5t0lsIOkKz0zQn4aXFuDS5d2fF930cRRFvWxTmRZgmI%2BDK6RQ34xUVnZSuInvceG3vd11Aj9YAuJa1dGZUe1Xd5iZ4v0pH27xEdGJevrJSp2RFQBhoM8g%2FYNoCibqMZE2AqSts%2Fd7Z3hBA03DUhuO7DbjnBlVPQsnHhPdwmE%2FItMp&X-Amz-Signature=85a083082e03f57801ed7372ec30ec8f5c6f2b9e5c8ee0b10696875070359426&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

