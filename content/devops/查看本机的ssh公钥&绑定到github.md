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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJM5XIJH%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQCqjyiNPymLQVDN3k56REdaFe7zuYWLk6%2FYc%2FgY4%2FFWKAIhANfZmqrWJzGXcI11Cti2r6owy%2FEsRIX7%2FIorz%2Fd1e7cTKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgygVHOkIGV6gGWK5bQq3APWttldyWZH20%2BKB5XMMUbzdg0wankQrKHS20zZV3UvZVww4D%2BXIp2XRMwIb9c2iy8duP50D7Ufw%2FUs87ODoDkO044g%2BRB4TLhdQN4Caq8haElG3PrIqv0fdiHzLYin78ZZv5mpF4y%2FTtHk8GXpEc8bwf46Tm7XlKGeO2Zedbd%2BeGUBV1kRQoWOhPkUYfyNZDodJY34KQmMNXWshlus2eqNdZ9t%2FcOfRDDXThkEVMvC6%2B%2Fh8siaBDIj%2BIogrzkX3IfRpS44FisZ6bYXcyfRIyIB%2F8oMyU6koYGQklrIh6sAw1HKN1FftjEh%2Fg9povm7Uk1TwE9yNmLC4NKhe3yjk3P69CQ%2Fh%2BeyezfQiUVxNcp8Pju12ith4nSViNiQKXrWtLy3ONJDJv19b4YDNU2I6HXC875XyFgUeOu3BxlgIZe3Jkq3Xw30bDS65h8vEidsqlVaX6oKCspYOp5GCaBuZJ%2BJWX5lhDvIxIzouG2t3KJURSX4URMOUzH78gs%2FMQ6pP%2BDbwzYTczkbDu9xG3HQN3GfRHPWvbJf4TXCWi8rxpketFXunpTVm6N3QCJ61%2F%2F2yDD5Hsfrl8vUVjEyTJ00hjURxkFN7sun4HFHNzC5SP1vdiDjg%2F3sIgZeRRqpoTC89dHOBjqkAT90An%2BOMtHaWzjp22UG8IwbB5LN7HUEVk7Ki576fvDm26qQCxy%2BMVzID6qJjhVHRkH4QnUw8Yx5cQ%2B8K1JHrbjSImrMVb0FG6yJifXhmKotiSbbHqQ5bP4OfnxlAfzdVflz94wEaLKPXHNkYOTzr3IYH8Q4ui1eIaLsmK1kLTtUG80G4KNjGfLZzSx3Xek7E9U%2FQBcCIWdKMwaw3LtMuF3AVt8q&X-Amz-Signature=8151a3c8eff06a7d709b009ac8c85bf00556099fbb1c9373215972d88f6a175f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJM5XIJH%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQCqjyiNPymLQVDN3k56REdaFe7zuYWLk6%2FYc%2FgY4%2FFWKAIhANfZmqrWJzGXcI11Cti2r6owy%2FEsRIX7%2FIorz%2Fd1e7cTKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgygVHOkIGV6gGWK5bQq3APWttldyWZH20%2BKB5XMMUbzdg0wankQrKHS20zZV3UvZVww4D%2BXIp2XRMwIb9c2iy8duP50D7Ufw%2FUs87ODoDkO044g%2BRB4TLhdQN4Caq8haElG3PrIqv0fdiHzLYin78ZZv5mpF4y%2FTtHk8GXpEc8bwf46Tm7XlKGeO2Zedbd%2BeGUBV1kRQoWOhPkUYfyNZDodJY34KQmMNXWshlus2eqNdZ9t%2FcOfRDDXThkEVMvC6%2B%2Fh8siaBDIj%2BIogrzkX3IfRpS44FisZ6bYXcyfRIyIB%2F8oMyU6koYGQklrIh6sAw1HKN1FftjEh%2Fg9povm7Uk1TwE9yNmLC4NKhe3yjk3P69CQ%2Fh%2BeyezfQiUVxNcp8Pju12ith4nSViNiQKXrWtLy3ONJDJv19b4YDNU2I6HXC875XyFgUeOu3BxlgIZe3Jkq3Xw30bDS65h8vEidsqlVaX6oKCspYOp5GCaBuZJ%2BJWX5lhDvIxIzouG2t3KJURSX4URMOUzH78gs%2FMQ6pP%2BDbwzYTczkbDu9xG3HQN3GfRHPWvbJf4TXCWi8rxpketFXunpTVm6N3QCJ61%2F%2F2yDD5Hsfrl8vUVjEyTJ00hjURxkFN7sun4HFHNzC5SP1vdiDjg%2F3sIgZeRRqpoTC89dHOBjqkAT90An%2BOMtHaWzjp22UG8IwbB5LN7HUEVk7Ki576fvDm26qQCxy%2BMVzID6qJjhVHRkH4QnUw8Yx5cQ%2B8K1JHrbjSImrMVb0FG6yJifXhmKotiSbbHqQ5bP4OfnxlAfzdVflz94wEaLKPXHNkYOTzr3IYH8Q4ui1eIaLsmK1kLTtUG80G4KNjGfLZzSx3Xek7E9U%2FQBcCIWdKMwaw3LtMuF3AVt8q&X-Amz-Signature=88bb249a115587dbb49556883c198de7ea60da28c1c6b4db7fc372024cd4c400&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

