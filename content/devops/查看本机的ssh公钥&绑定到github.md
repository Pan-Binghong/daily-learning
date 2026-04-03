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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2AEUJKP%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIERil8VcTF8KfdxM5BDpNFaGbi%2FI84Cv02NZ1W8rxVMpAiEAjFif%2F2mQKpGFQ0MNYlkS5N8KgJK9hQdRivIEukHFWNIq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDGnDQslz629apyb5FSrcA6Ubp3FHggV1Usi7g4kF9UAavSMXokQ0ZlLgTlgz%2Btz8bRUjGlhQ2Bz%2FOMD%2BpwxyViM6o2wxmV3mVPPHtYpaza2lNZ%2BO0Y2KqKC0u2zdtLhyaYRboJoYYlpadp9YXtnGO5tr6RSD65gIs7KAcWC%2BgGTnS1WvVshG1vCPLtRe7kH0PmVmvmxCbCgQaSLMKvnRZjWYkKhBw9ntd7GeQGqvn%2FYeh6sGUflvjfJlSj3ljm06pk0PS0KTgzdzkHqTFGXAGa91ww6yeIi8YeN5VrHX4t1G5V2Xjxo7eQf7WaNmk6%2FOGJ6IXPu3UaniQ%2FL65ZQAT5WiwGEy4jCnSdTWm0U7t0wAEL4G9xZYmdzF0bhYHDgQjvCIw1eieJT7dP8TBy3vwBvO8ickVwaiHYC4uLYodwtqOeU9fv%2Fps%2Fg3SQM%2BChf0HSl4jiWDpYxG1U%2BZrs%2Bi3tq8a1JSo17zjTtQC%2BtYjDaiMdi7GKqVHIFNyHKVyjZ12TT%2BX9NyxbyLARi9i1JrTEyiZZ43jBdgJFgf6geT64rB058DDtM9G8YszfnANDt3bSafJ75mC1SqEW1XkwkYAfhSVG1C7Ykbp0dlfM5AD5E3VdUdedWDuIryBTLk0DyxeW9kau4nHA9pYZa%2FMLblvM4GOqUBlhXkCPo1ADU99lZjcnJ6jmn9TOuEzD4RMrtsFYZ86idn6o2qNLpDF5LQUikp2B%2BvvnsxDHE39EZeXMetNts44FzYEnYeOZ8aeGIlcbhY%2FDjg%2FbOmf6u1hsprLRdD1YgQv1kIajA%2BNW0tvHDQOFAt9FnkMNsAxDmPduv0VkqTyocds%2F2r1l7ZhLXesXcIH9gYeEBGYwu%2BYop4lkO9D9qF15x5uPyI&X-Amz-Signature=2883636bc9589723c08cb929beb1bbd26770d5ab1f7f72c1dddaff1f51511402&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2AEUJKP%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIERil8VcTF8KfdxM5BDpNFaGbi%2FI84Cv02NZ1W8rxVMpAiEAjFif%2F2mQKpGFQ0MNYlkS5N8KgJK9hQdRivIEukHFWNIq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDGnDQslz629apyb5FSrcA6Ubp3FHggV1Usi7g4kF9UAavSMXokQ0ZlLgTlgz%2Btz8bRUjGlhQ2Bz%2FOMD%2BpwxyViM6o2wxmV3mVPPHtYpaza2lNZ%2BO0Y2KqKC0u2zdtLhyaYRboJoYYlpadp9YXtnGO5tr6RSD65gIs7KAcWC%2BgGTnS1WvVshG1vCPLtRe7kH0PmVmvmxCbCgQaSLMKvnRZjWYkKhBw9ntd7GeQGqvn%2FYeh6sGUflvjfJlSj3ljm06pk0PS0KTgzdzkHqTFGXAGa91ww6yeIi8YeN5VrHX4t1G5V2Xjxo7eQf7WaNmk6%2FOGJ6IXPu3UaniQ%2FL65ZQAT5WiwGEy4jCnSdTWm0U7t0wAEL4G9xZYmdzF0bhYHDgQjvCIw1eieJT7dP8TBy3vwBvO8ickVwaiHYC4uLYodwtqOeU9fv%2Fps%2Fg3SQM%2BChf0HSl4jiWDpYxG1U%2BZrs%2Bi3tq8a1JSo17zjTtQC%2BtYjDaiMdi7GKqVHIFNyHKVyjZ12TT%2BX9NyxbyLARi9i1JrTEyiZZ43jBdgJFgf6geT64rB058DDtM9G8YszfnANDt3bSafJ75mC1SqEW1XkwkYAfhSVG1C7Ykbp0dlfM5AD5E3VdUdedWDuIryBTLk0DyxeW9kau4nHA9pYZa%2FMLblvM4GOqUBlhXkCPo1ADU99lZjcnJ6jmn9TOuEzD4RMrtsFYZ86idn6o2qNLpDF5LQUikp2B%2BvvnsxDHE39EZeXMetNts44FzYEnYeOZ8aeGIlcbhY%2FDjg%2FbOmf6u1hsprLRdD1YgQv1kIajA%2BNW0tvHDQOFAt9FnkMNsAxDmPduv0VkqTyocds%2F2r1l7ZhLXesXcIH9gYeEBGYwu%2BYop4lkO9D9qF15x5uPyI&X-Amz-Signature=f788e96c4a11b350727d8021f282bd700ff670b6fc10f3048bc90a2bb050ab05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

