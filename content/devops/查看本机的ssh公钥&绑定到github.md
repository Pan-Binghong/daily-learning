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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RREDHXLL%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAL4j9masU8MHnTayMyTYpfPd9RWUkykTMMrE9kviz4sAiEAq9dQ1%2BP6cdjF%2FKcNLCqfIpD4RoSA7xd3wRJyjh7fwgcq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDN6ZqeirHsFZK2aDFircA0bsrg7vPkyqA8zHy5H8r720MdXx37CnGoPWUlmYOqPfA5DXUO4qiOrzUb4n1%2F6v4379qPGrnxNnBIQSKZoWBv4lsDp6p%2BLGL0K2MoiYIIikr0vPX7OWH8jb%2FW8retfQE%2BaaKrAAAex1tlqQ5eOz85KJCqdVx%2FjPGXd2O4Gbw%2F3DbbrRQBHPX3k%2BcfcQVJ2lbxpv3KOndo%2BHcwZT15KLdE%2FwDG%2F7AnO4nPN8DDKcmXrY%2BPwRjHeBH7K86J%2BvhOEzlhr%2BEXfvEBrBZHVvNUCrbi%2B4ACbBIgqeIlAPVPnYhD8Nd5zbrktB2LBpALcevha7IEVmdrWrFHHRmZQ1%2B0Nh1BlCBaRbAiiWD2SoubRbY2H093bBkRx5nW9FwCcXjtG2KIbsaSPWmSNReYluBLi2BbS9X6kvQ3BXGEm%2FuKSqwY9cq8SQpznT2xwMmtJ1pWsdevoDdY5qrjwgNGS1MO75U1cBqKUslcSmI%2BaBFMcjwLYZ3FYozIRWydbRzKv1LoBiWou3SLXtetf6cbuFWIzfk3B6IcG6HwXC0N4%2FlASL4BsOa9maGcDxnv3KCwhmovkIHFXu%2BykWOlXJdl1tY5HAGAkvgkwlL11AnflX1LVzS%2FE8NICRPEKolxFAOoGuMPucps8GOqUBUhfb2Hd0fk96IBQgS171hcG%2BcdJsvHG17Ylso6Llfh6ogcPAdK5L4YW8CkLfA3VEjziuQuH2rUswo339cMiwd6ES1%2Bmaks83%2BfX6QtMBnXnw0oTmRRMVdsZNXlGscrMjl6GF974jyrett9Muncra13g6QCa7QL11bzmcGD1olZQ%2BNh3q0wXwUzT7YVRLhw7d6sahcZhhouJj55XBfoSp%2Fib1Xbl7&X-Amz-Signature=e58a8766089167ae763e6b52639b4f727dad9b1ccbbde79271580db158023713&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RREDHXLL%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAL4j9masU8MHnTayMyTYpfPd9RWUkykTMMrE9kviz4sAiEAq9dQ1%2BP6cdjF%2FKcNLCqfIpD4RoSA7xd3wRJyjh7fwgcq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDN6ZqeirHsFZK2aDFircA0bsrg7vPkyqA8zHy5H8r720MdXx37CnGoPWUlmYOqPfA5DXUO4qiOrzUb4n1%2F6v4379qPGrnxNnBIQSKZoWBv4lsDp6p%2BLGL0K2MoiYIIikr0vPX7OWH8jb%2FW8retfQE%2BaaKrAAAex1tlqQ5eOz85KJCqdVx%2FjPGXd2O4Gbw%2F3DbbrRQBHPX3k%2BcfcQVJ2lbxpv3KOndo%2BHcwZT15KLdE%2FwDG%2F7AnO4nPN8DDKcmXrY%2BPwRjHeBH7K86J%2BvhOEzlhr%2BEXfvEBrBZHVvNUCrbi%2B4ACbBIgqeIlAPVPnYhD8Nd5zbrktB2LBpALcevha7IEVmdrWrFHHRmZQ1%2B0Nh1BlCBaRbAiiWD2SoubRbY2H093bBkRx5nW9FwCcXjtG2KIbsaSPWmSNReYluBLi2BbS9X6kvQ3BXGEm%2FuKSqwY9cq8SQpznT2xwMmtJ1pWsdevoDdY5qrjwgNGS1MO75U1cBqKUslcSmI%2BaBFMcjwLYZ3FYozIRWydbRzKv1LoBiWou3SLXtetf6cbuFWIzfk3B6IcG6HwXC0N4%2FlASL4BsOa9maGcDxnv3KCwhmovkIHFXu%2BykWOlXJdl1tY5HAGAkvgkwlL11AnflX1LVzS%2FE8NICRPEKolxFAOoGuMPucps8GOqUBUhfb2Hd0fk96IBQgS171hcG%2BcdJsvHG17Ylso6Llfh6ogcPAdK5L4YW8CkLfA3VEjziuQuH2rUswo339cMiwd6ES1%2Bmaks83%2BfX6QtMBnXnw0oTmRRMVdsZNXlGscrMjl6GF974jyrett9Muncra13g6QCa7QL11bzmcGD1olZQ%2BNh3q0wXwUzT7YVRLhw7d6sahcZhhouJj55XBfoSp%2Fib1Xbl7&X-Amz-Signature=8166f00e00daf71a460dfbf545f75b0e6e99a777d5507abbbcaff49f9a3d0ecb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

