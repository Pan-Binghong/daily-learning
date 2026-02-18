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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VA5CIKZM%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJItZo05NsQ4y72yX8o%2FSzOZfK1ehZVz2Sfdd%2FKfmIbQIhAKjMFXrLuR7nGw0lbo0tIrEehdDyWSaC6uDM6nAjvQATKv8DCFoQABoMNjM3NDIzMTgzODA1IgwnQ3S4%2BJTrRvE%2F0psq3AMQ3hSBxOrLQr2LcrQ6hl7lyiyNy0spxWd9TJUoMoadAOvl%2BOhVVzWfn3ojeyke%2FCZcpprrtxkTHkPnS8HzH4Lqv6QF2aw9ogy2UOuEaYJhHjiCtTLDbFvSZSbLSt0fBVzBpEi2eEn%2FFgHDVVjS4iUpJF0aO8DMm79bs15jkvN79YaMd%2FsdcPJFePmnr9gXpXD%2F2QAI6ami6RVK5z1lm28RsZQGS4thLexBZSHp4GplRW5q2yefMfaPQHp6MsU%2F7kD46DPlxj5A46eyEKJu8LzeWUUVJHJgWQVPrRWXypMSt29u6LUMHoTbLB7R78llgUHdFCHJZsOOnkq8t8k%2F%2BxbXRbov8799DIas3CTexJ66xDiYaULfKCXQD5Ug%2Fds3HQdqVLX3tmmsqkp6jnSbfXnU11GXynEJZyXUka81XH2Z8PdZbMBWuUKROb60w3SC2zC4v1DvpG80ZmGbRONCbwi3ygSFOJUQGMFcTQv7SG2vRRoAPC6z84zXrHo5Slsjevs%2B5ZNHyLJduEIY8XqYY7lH4LBHnIzlNooT39WyYvaToqz7ct5a6gHbJDU18EPWrl6xVPwTIT9usFGNi7kmW7YRyGEosiKLespbVfu3WZ2kh3gJwuNX%2F9O8Q4GkozDQn9TMBjqkAXYisOYDofbjkWKJ3LJ6NOxm3T8WjIkO%2BeL8WWsAfbeg%2FsBJNyKHcuKLYiHRhWBRC3cbE%2B10t6MOy5dtE%2B0jrPLfFepMu%2BglgYIh20VLcqsQKaqqkJ%2FDvIcF6CnoE61fsg1PMxv5jMSNmYnxzwJ%2FZqnzMYgjAY9OwCivbRMnxuTqhRFzRBAbjR9vyecVxPVvUt9HLfpk9LSUYpfhP0yfunocsQHK&X-Amz-Signature=4878de26eedf50f45f32697481d778ad63e4ed238e7ac88aafd852815d5be81d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VA5CIKZM%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJItZo05NsQ4y72yX8o%2FSzOZfK1ehZVz2Sfdd%2FKfmIbQIhAKjMFXrLuR7nGw0lbo0tIrEehdDyWSaC6uDM6nAjvQATKv8DCFoQABoMNjM3NDIzMTgzODA1IgwnQ3S4%2BJTrRvE%2F0psq3AMQ3hSBxOrLQr2LcrQ6hl7lyiyNy0spxWd9TJUoMoadAOvl%2BOhVVzWfn3ojeyke%2FCZcpprrtxkTHkPnS8HzH4Lqv6QF2aw9ogy2UOuEaYJhHjiCtTLDbFvSZSbLSt0fBVzBpEi2eEn%2FFgHDVVjS4iUpJF0aO8DMm79bs15jkvN79YaMd%2FsdcPJFePmnr9gXpXD%2F2QAI6ami6RVK5z1lm28RsZQGS4thLexBZSHp4GplRW5q2yefMfaPQHp6MsU%2F7kD46DPlxj5A46eyEKJu8LzeWUUVJHJgWQVPrRWXypMSt29u6LUMHoTbLB7R78llgUHdFCHJZsOOnkq8t8k%2F%2BxbXRbov8799DIas3CTexJ66xDiYaULfKCXQD5Ug%2Fds3HQdqVLX3tmmsqkp6jnSbfXnU11GXynEJZyXUka81XH2Z8PdZbMBWuUKROb60w3SC2zC4v1DvpG80ZmGbRONCbwi3ygSFOJUQGMFcTQv7SG2vRRoAPC6z84zXrHo5Slsjevs%2B5ZNHyLJduEIY8XqYY7lH4LBHnIzlNooT39WyYvaToqz7ct5a6gHbJDU18EPWrl6xVPwTIT9usFGNi7kmW7YRyGEosiKLespbVfu3WZ2kh3gJwuNX%2F9O8Q4GkozDQn9TMBjqkAXYisOYDofbjkWKJ3LJ6NOxm3T8WjIkO%2BeL8WWsAfbeg%2FsBJNyKHcuKLYiHRhWBRC3cbE%2B10t6MOy5dtE%2B0jrPLfFepMu%2BglgYIh20VLcqsQKaqqkJ%2FDvIcF6CnoE61fsg1PMxv5jMSNmYnxzwJ%2FZqnzMYgjAY9OwCivbRMnxuTqhRFzRBAbjR9vyecVxPVvUt9HLfpk9LSUYpfhP0yfunocsQHK&X-Amz-Signature=77a67a6119a54f064b9e84f5c740210461b67191154a308a771462699e9cffca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

