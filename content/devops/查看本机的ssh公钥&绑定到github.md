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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663GIKLQR%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032701Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOAqreDmUqx%2BU9ol93s9eR3TRcG0%2FRK0SAmhoKWUs6tQIgMvtvZI9bpqKGPG36BJpDYHBXYZJNuA%2F1Ad47J0pCjC4qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNjeC9rCXJV8aDWUaircA1x8rVj4RaRcbvRwo434LmORk0vK5ieQS6x6EueCYXusIylqV6Z660AwVTWCDgtNZGOQZHaB0Y88NEw2mIMcOdYnXOzW0hdbcmLc8SmiLhNUu9Rel8uzTZ9rTpWpNZPQyLdEhcuFQCJspV9VS8nwWAQ3408SREcCWGfA565FpP8QM1cG6uFtUWzzXPwmPsGne%2BwdSOFNQJbMQQns8PMpsl32HHh2HdA84jx%2BOgtkbj5SCgkVyaFO9Ll%2FQv6oqhPYKMOzKvAG%2BU1SgJJXIOIzDHIxn0gBxu81ARYzkW6Gh6kTCBa%2Bgeo%2FsN68aTG620vqFKaotZRw0yI9sll5%2FpVj6%2F4ge5utmyTgF3mlJhey3wR1nAilyAtL%2B5C4jnybc%2BBG0%2BWqv795DkUyT8bAEkOveOOkWsbv4yRHo3GRZ5VHKjdHn9QcvAx2LHCDtftc66xCs6G5IfyyAMcYzR7EhClZajF%2FGJMpNzb5zly4UNlyVt4TVilrs84RKC790GrXrGlQK29%2FaufZqcGbxpRzm2IjAk3A0njTblklSLHEdG%2F2YixuIcq3Ay3Yag6HgJHSC76AwtfcuRJ0Sz%2Bc8Q%2FgDhv80xqQLv%2F8lGS69bq2gQi0CQ7FwpSbD1bQJxLLfBKEMIu95MwGOqUBX4nDBlIKsbQhGgdPNNQ8Nr5duIE3WRO2PPdVQhsPCBE%2Frw%2BspvmoDa94DWc4TVkBwVnCMZ%2FXxFJU%2B5L1hPhw6SSbd9eLy4Gaj7CTxrUBPonNhBlSb9FP%2F87o8wzG%2FSJTJa23QaCAsOXGmMGexMSFFA8jnLTCK1M%2B3Z93Q%2FEvbpYEQm53Aep4OW%2F1G2FulvPwFaPHwgHAZxyDvaSNnEMB6dyXp9iv&X-Amz-Signature=9703a21e94afdb7d509127fc66ad5b70595b87f56e3344a4918762749d781b61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663GIKLQR%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032701Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOAqreDmUqx%2BU9ol93s9eR3TRcG0%2FRK0SAmhoKWUs6tQIgMvtvZI9bpqKGPG36BJpDYHBXYZJNuA%2F1Ad47J0pCjC4qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNjeC9rCXJV8aDWUaircA1x8rVj4RaRcbvRwo434LmORk0vK5ieQS6x6EueCYXusIylqV6Z660AwVTWCDgtNZGOQZHaB0Y88NEw2mIMcOdYnXOzW0hdbcmLc8SmiLhNUu9Rel8uzTZ9rTpWpNZPQyLdEhcuFQCJspV9VS8nwWAQ3408SREcCWGfA565FpP8QM1cG6uFtUWzzXPwmPsGne%2BwdSOFNQJbMQQns8PMpsl32HHh2HdA84jx%2BOgtkbj5SCgkVyaFO9Ll%2FQv6oqhPYKMOzKvAG%2BU1SgJJXIOIzDHIxn0gBxu81ARYzkW6Gh6kTCBa%2Bgeo%2FsN68aTG620vqFKaotZRw0yI9sll5%2FpVj6%2F4ge5utmyTgF3mlJhey3wR1nAilyAtL%2B5C4jnybc%2BBG0%2BWqv795DkUyT8bAEkOveOOkWsbv4yRHo3GRZ5VHKjdHn9QcvAx2LHCDtftc66xCs6G5IfyyAMcYzR7EhClZajF%2FGJMpNzb5zly4UNlyVt4TVilrs84RKC790GrXrGlQK29%2FaufZqcGbxpRzm2IjAk3A0njTblklSLHEdG%2F2YixuIcq3Ay3Yag6HgJHSC76AwtfcuRJ0Sz%2Bc8Q%2FgDhv80xqQLv%2F8lGS69bq2gQi0CQ7FwpSbD1bQJxLLfBKEMIu95MwGOqUBX4nDBlIKsbQhGgdPNNQ8Nr5duIE3WRO2PPdVQhsPCBE%2Frw%2BspvmoDa94DWc4TVkBwVnCMZ%2FXxFJU%2B5L1hPhw6SSbd9eLy4Gaj7CTxrUBPonNhBlSb9FP%2F87o8wzG%2FSJTJa23QaCAsOXGmMGexMSFFA8jnLTCK1M%2B3Z93Q%2FEvbpYEQm53Aep4OW%2F1G2FulvPwFaPHwgHAZxyDvaSNnEMB6dyXp9iv&X-Amz-Signature=2481c3238caef68958bc5740599b8de033ce0837e50fac7f8a827571656b419c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

