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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHZM72LL%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCyVrkQwKTR4k8qBtPCtZ77J1L32yOIX%2Bpq%2BRpvIcHQBAIgQ%2BG%2F8ermLl7VFk%2FgmUYjv6xBpEHDEXsrWfzqOPmLx4wqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOCmtzRGg%2BnlpUx17SrcA5INrw%2B4YLFVe14ymPJAYVUodbgz%2BBxkZ1lZ9zgkX95A%2BZUj%2B9KoUazH9Ni8N6XYXZhjYGCDi4ZzoCqICOZ%2BjJgKY0ynZV6FqGePNRgRvvoRPm1KatzeP9HO5R2NRVHlP4DTMDU9kKpY9HAVzIt%2Ftkvy4XXsI7R8t2iOb%2Fhh%2BmqWqXBOeqey%2FPbp4bWtYcHn9b5qFq1Xw90mld1DfY6aygUdNdVA6z0NK1xwOprcBORcgg3A996131bpbHnCr%2FcMf9Ugq9uwV6porF2eXWkvHTQtKioCtEOAhFTmCN87MTBhqwaIN6BMZVVm09jJ8oJV1%2F7bdFRFqTlBfE%2FWJoKYdxkEqOOJKm3EOPw9spx%2FkdFEvjmJSfoR0twtc1wZyALxGV2Vwog8RbZuVD3gx8M%2BeeT6gy6uGgmX8gvqRI%2B3IOYLBpM6fowGZxbVozK5Oi2KlHTzkksgEdCo%2Fod4Brms06mr8q5TazQDpZOtF6PfC7lDgp1VvztJid39Yg1l%2Bhx770dEfTz5dBITQPJbxddJf3Dj0rLBFUf1ugyls4FiH0IWBIw5DLgQzGGiEzxBwsSLNBbr4lCcstR7w0H0n27olOiYE2ALLkQHToOECemMzHZzVMqZ962jMXXv96zbMPaH184GOqUBIWjjZqP8J%2FZdlK20B%2FjnWNopdRIQG%2BnEgKzM5x1OQ41rKS6PJjAOn50DeuWt8UMi%2F7cSxjKFeyBjlmUSv3HHVd0MeozErTCFmY7TQ5drhgaHkx3tXb6xGyke9ff%2B52vyvS%2F9R5vCLpIAe5koE8eNJKaVcMslDZ2arJaGLciDVvxrrwEQJ4TbDCc4dJxGj9tdlunxJFARe7r%2FxjTPMsbGIeb7fQAu&X-Amz-Signature=c4e47f2f43613fab901bc6c4138dfc0b7fb17cdd22bc01519a1b775bc720773c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHZM72LL%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCyVrkQwKTR4k8qBtPCtZ77J1L32yOIX%2Bpq%2BRpvIcHQBAIgQ%2BG%2F8ermLl7VFk%2FgmUYjv6xBpEHDEXsrWfzqOPmLx4wqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOCmtzRGg%2BnlpUx17SrcA5INrw%2B4YLFVe14ymPJAYVUodbgz%2BBxkZ1lZ9zgkX95A%2BZUj%2B9KoUazH9Ni8N6XYXZhjYGCDi4ZzoCqICOZ%2BjJgKY0ynZV6FqGePNRgRvvoRPm1KatzeP9HO5R2NRVHlP4DTMDU9kKpY9HAVzIt%2Ftkvy4XXsI7R8t2iOb%2Fhh%2BmqWqXBOeqey%2FPbp4bWtYcHn9b5qFq1Xw90mld1DfY6aygUdNdVA6z0NK1xwOprcBORcgg3A996131bpbHnCr%2FcMf9Ugq9uwV6porF2eXWkvHTQtKioCtEOAhFTmCN87MTBhqwaIN6BMZVVm09jJ8oJV1%2F7bdFRFqTlBfE%2FWJoKYdxkEqOOJKm3EOPw9spx%2FkdFEvjmJSfoR0twtc1wZyALxGV2Vwog8RbZuVD3gx8M%2BeeT6gy6uGgmX8gvqRI%2B3IOYLBpM6fowGZxbVozK5Oi2KlHTzkksgEdCo%2Fod4Brms06mr8q5TazQDpZOtF6PfC7lDgp1VvztJid39Yg1l%2Bhx770dEfTz5dBITQPJbxddJf3Dj0rLBFUf1ugyls4FiH0IWBIw5DLgQzGGiEzxBwsSLNBbr4lCcstR7w0H0n27olOiYE2ALLkQHToOECemMzHZzVMqZ962jMXXv96zbMPaH184GOqUBIWjjZqP8J%2FZdlK20B%2FjnWNopdRIQG%2BnEgKzM5x1OQ41rKS6PJjAOn50DeuWt8UMi%2F7cSxjKFeyBjlmUSv3HHVd0MeozErTCFmY7TQ5drhgaHkx3tXb6xGyke9ff%2B52vyvS%2F9R5vCLpIAe5koE8eNJKaVcMslDZ2arJaGLciDVvxrrwEQJ4TbDCc4dJxGj9tdlunxJFARe7r%2FxjTPMsbGIeb7fQAu&X-Amz-Signature=15609c66e5a7ef80e8583523044ab4b51ddf660809d09f1370ffae1ebea06b09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

