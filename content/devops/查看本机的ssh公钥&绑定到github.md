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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMFHRUMO%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQDe1IphkSHeUleVkIx6S7bz%2FHn0hZStAtYnE7cYA4dfzAIgDtAD89Z9uVFPZ7KsetnkCzPImmjQR2335Bk8KJ18%2FPEq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDBynqSWRkoscY%2FRVJircA2jpndNJriIXQJLWZtblgAdVNzguG8tKXXa1dJR7nEEPhpyekjt%2B12fFnI0NRMe3%2Bo1yXI%2B25DpjvXkOnTJxbgY5ozMlf1SA7nj6Xzf4LhcQbYyOROFiTr8OaSvABSxoSTe69scKMpfDsKMeI7LeCv1Gix75oNRJaJyWqQ6qr3kcjwFEciKOa7%2BIEjsLsj%2B1sfJ4ST1Er6kaosRSQu%2FRbJfP3X1m9rftrYQmAR52JU1HV%2BXiSBoajO%2BjSnJopRldlMrGrwunH5s8QevyN6JuM4Eja40c5nnlsIEiX8rYDvYBSh0iy46KxuEqhgGnPBMe02lCqaJlJUc0rY59q11UgQindTyaSkKe9Dpvkj44YnwvVXi64%2Buk1KAFH6ghnmTAEDr7qCqkQj4I4cwy89p8AvOmbG2TCNdd0M6x6wuK5whwibLmF2%2BxRl2PBX2JWI%2BmKnYFeXFPgrxLMDJVSbkdZgVbA%2BlR8ilKTjks4SCUQkezeJDN9zFi482Nh5w81VIJqobKaXCq14eb3lqcxG6sQJB2FtA%2BmuxiutjJJ52F%2F9pc9YBbCN1d9PYprX9SW8%2BD3RMK0GfEVcEw8Pk8UW6mrpZALeG7lsJaxLwQIF4fkGcrC65m71JXW3R6kMpEMP7Vm88GOqUBu9MlORt4gVy15RcmwIzUxMrEaoMNKtx83uJVeLS385i7Z3a8sLi5W3cNCYXQcL1JRUgqxTKXvybdOeCz%2F76EyS07JsmiBcsAl9sqeu%2B9mwwLKXOelklz2gQbURbVllwz271s%2B7DMWDC9t%2BO3atR5zfjTkg2wdhGLUuEhyfotnbdc9khVoorIdl%2Fq4w2yFWoRxhewGbGVj6yNS%2FQZ2hYjPs%2FZAz7E&X-Amz-Signature=3889705440066fb747b60d6319dd5e2daf6d55bd125c68d94e22aa755d9f6b1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMFHRUMO%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQDe1IphkSHeUleVkIx6S7bz%2FHn0hZStAtYnE7cYA4dfzAIgDtAD89Z9uVFPZ7KsetnkCzPImmjQR2335Bk8KJ18%2FPEq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDBynqSWRkoscY%2FRVJircA2jpndNJriIXQJLWZtblgAdVNzguG8tKXXa1dJR7nEEPhpyekjt%2B12fFnI0NRMe3%2Bo1yXI%2B25DpjvXkOnTJxbgY5ozMlf1SA7nj6Xzf4LhcQbYyOROFiTr8OaSvABSxoSTe69scKMpfDsKMeI7LeCv1Gix75oNRJaJyWqQ6qr3kcjwFEciKOa7%2BIEjsLsj%2B1sfJ4ST1Er6kaosRSQu%2FRbJfP3X1m9rftrYQmAR52JU1HV%2BXiSBoajO%2BjSnJopRldlMrGrwunH5s8QevyN6JuM4Eja40c5nnlsIEiX8rYDvYBSh0iy46KxuEqhgGnPBMe02lCqaJlJUc0rY59q11UgQindTyaSkKe9Dpvkj44YnwvVXi64%2Buk1KAFH6ghnmTAEDr7qCqkQj4I4cwy89p8AvOmbG2TCNdd0M6x6wuK5whwibLmF2%2BxRl2PBX2JWI%2BmKnYFeXFPgrxLMDJVSbkdZgVbA%2BlR8ilKTjks4SCUQkezeJDN9zFi482Nh5w81VIJqobKaXCq14eb3lqcxG6sQJB2FtA%2BmuxiutjJJ52F%2F9pc9YBbCN1d9PYprX9SW8%2BD3RMK0GfEVcEw8Pk8UW6mrpZALeG7lsJaxLwQIF4fkGcrC65m71JXW3R6kMpEMP7Vm88GOqUBu9MlORt4gVy15RcmwIzUxMrEaoMNKtx83uJVeLS385i7Z3a8sLi5W3cNCYXQcL1JRUgqxTKXvybdOeCz%2F76EyS07JsmiBcsAl9sqeu%2B9mwwLKXOelklz2gQbURbVllwz271s%2B7DMWDC9t%2BO3atR5zfjTkg2wdhGLUuEhyfotnbdc9khVoorIdl%2Fq4w2yFWoRxhewGbGVj6yNS%2FQZ2hYjPs%2FZAz7E&X-Amz-Signature=41daadf21ec0668ed0d0d203d82951b7db6a86f6ecfa343b62e3678d4600af0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

