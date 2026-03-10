---
title: 查看本机的SSH公钥&绑定到Github
date: '2026-02-03T02:14:00.000Z'
lastmod: '2026-02-03T03:32:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 配置Git使用SSH方式, 本文环境：windows + powershell + git guissh 

---

## 查看

```json
ls  ~/.ssh
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SADHN5YU%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQCaXnSqWrgPQKRfmFuGU7vh1QsDO6EjJiaJ6N8lk9UvCQIhAJT4q%2F9XIUFw0tsMdT6GT2vfGj81hZn8ytclJxQ5wBTzKv8DCDwQABoMNjM3NDIzMTgzODA1IgxXBQGlL5vUfU9NEfwq3APBO9tJKdgo2cpayC7Yh2WPHboyrI7jKcnQ2TMM%2FoyuRPjldvCkuHdrolNKbHDW8GkGipvjAbMtefrPWZ4wlebELD3NjGhYKFeB32UKtiGUqps2%2BUZZPqJZCRh5v%2Bi4oZpYY0Mo88ejAtK%2FsLHPzGpb7dWl3g2ZJ%2FftOhUerW4f8yXn4ijypLz0HICW5zWUwLF3akEYHUyCu5TLH%2BO%2F9YSziJaR2gJ%2Bxbl91NwtPnL55BCeyp28F%2FSnrBoLtX01EHk4%2Bbro99TFgBRGorH7AiSVSwk6jAhV3ia32Xi3C8b%2F9LxdR2rDILWbrLXJNy9Wlyvtax3rpDf9t7DblBKG9p8GhaQitPzQf1WISfzb1c7TLtD0W8sMQmmXcf%2Bc7wjV0oTYl5M4ORFGXetrIMMILL%2FQvqNs2YqH9sDKP3s8xQ1ZDDzeAJJ8MRrhqyZowUu%2Fvqr3UjzU0i4e796EGACbDCN%2FgLIYfRxGo4OisWxfonZneCHINXobwdg2mlNX8%2FdnnxghdomFwiShNS8Kl7%2FX5UfoYIgUp%2FflTbR5cgoQUw434ux1D%2BjIz1ORUUrQD%2B9%2BvpdqrKk3S%2FIueEbrlj52CBapjy%2BVBu4EVM6MA%2BIRmtZAV1CkLuz5Zky0a4x1RzD5j77NBjqkAbEqEUkBcSyAQMzw7LLTypNtPCyUSStpIUJ5073jfcSxcF4DMrR4ebpTTl6gguNyWISnVNwYm%2FgY2tHkwwG%2FUnrQr8Lsvg1Hm4zuDBZ%2FRpVNgWt2AtGzn8nYNuiboxesGxMRj0udvcvkna69y2ESFMDRfhpybSBIIEzXBZlkRjqWbD82LyumX7hQpj5o8vyRWjaDFrO%2Bo9RbQ44Z6hrr%2FfFQQQkn&X-Amz-Signature=dec211f3065d90dd504c316da87414f5cda99e219d51aad086e703045ede4c0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 创建

```json
# 推荐使用Ed25519算法
ssh-keygen -t ed25519 -C "your_email@example.com"

# 备选
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

---

## 配置

```json
# 将ssh密钥添加到ssh-agent
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
ssh-add .\.ssh\id_ed25519

# 查看是否添加成功
ssh-add -l
```

### 安装gh（github cli）

```json
# 打开powershell
choco install gh

# 登录
gh auth login
```

## 打开GIT/提交

```json
gh ssh-key add ~/.ssh/id_ed25519.pub --title "公司主机"
```

## 验证

```json
ssh -T git@github.com
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SADHN5YU%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQCaXnSqWrgPQKRfmFuGU7vh1QsDO6EjJiaJ6N8lk9UvCQIhAJT4q%2F9XIUFw0tsMdT6GT2vfGj81hZn8ytclJxQ5wBTzKv8DCDwQABoMNjM3NDIzMTgzODA1IgxXBQGlL5vUfU9NEfwq3APBO9tJKdgo2cpayC7Yh2WPHboyrI7jKcnQ2TMM%2FoyuRPjldvCkuHdrolNKbHDW8GkGipvjAbMtefrPWZ4wlebELD3NjGhYKFeB32UKtiGUqps2%2BUZZPqJZCRh5v%2Bi4oZpYY0Mo88ejAtK%2FsLHPzGpb7dWl3g2ZJ%2FftOhUerW4f8yXn4ijypLz0HICW5zWUwLF3akEYHUyCu5TLH%2BO%2F9YSziJaR2gJ%2Bxbl91NwtPnL55BCeyp28F%2FSnrBoLtX01EHk4%2Bbro99TFgBRGorH7AiSVSwk6jAhV3ia32Xi3C8b%2F9LxdR2rDILWbrLXJNy9Wlyvtax3rpDf9t7DblBKG9p8GhaQitPzQf1WISfzb1c7TLtD0W8sMQmmXcf%2Bc7wjV0oTYl5M4ORFGXetrIMMILL%2FQvqNs2YqH9sDKP3s8xQ1ZDDzeAJJ8MRrhqyZowUu%2Fvqr3UjzU0i4e796EGACbDCN%2FgLIYfRxGo4OisWxfonZneCHINXobwdg2mlNX8%2FdnnxghdomFwiShNS8Kl7%2FX5UfoYIgUp%2FflTbR5cgoQUw434ux1D%2BjIz1ORUUrQD%2B9%2BvpdqrKk3S%2FIueEbrlj52CBapjy%2BVBu4EVM6MA%2BIRmtZAV1CkLuz5Zky0a4x1RzD5j77NBjqkAbEqEUkBcSyAQMzw7LLTypNtPCyUSStpIUJ5073jfcSxcF4DMrR4ebpTTl6gguNyWISnVNwYm%2FgY2tHkwwG%2FUnrQr8Lsvg1Hm4zuDBZ%2FRpVNgWt2AtGzn8nYNuiboxesGxMRj0udvcvkna69y2ESFMDRfhpybSBIIEzXBZlkRjqWbD82LyumX7hQpj5o8vyRWjaDFrO%2Bo9RbQ44Z6hrr%2FfFQQQkn&X-Amz-Signature=d0fda73e38fec215afcc2bf0eecf9e3ee50adf7fb45c62c201176fdd5975ebc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

