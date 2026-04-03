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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HQKKJZJ%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFoAoYezWvur6UEhARYVmILxDhWeipfODeHBgYuQsdcBAiEAiRLHngd3OWc%2Fs%2FFGZ6Ag1J4gVhQURtMgDwFGD4Y9B0oq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDJtBgBGxb%2Ff5FXdlRyrcA8MTFvLu0m3da5VJD%2Frc%2BAi0RpWhS7rFHujba6gafkL4nDjS8VghZzbEorpyUFmvDQSmjl400ljZ5qovDGwm0f7POhhYICCN7MRlgoLDBndbDn4psTxhq9sDdpBWiO1V%2FT7V14Qsx6vRxyhHd37sRcKve3LgBDuUhQmL%2F6xabzPK4V6Mfa3lB3TVc%2B68YDTnvFVjSu1HMPz7cd%2FzvUqng1HMxGJzPojVPwchCReOX6%2F%2BDbnEVy3EQLbyYXvsfoL121o2bcHzFYpWh%2ByPf8T0Q%2Fwuia2CSm7rK%2BdVBKxGSKBbXni7xXj%2FuhPaap3xw65GbKE2IwfnxDXSgWrNVteuxKBf9lnyGrEuZV88duNdl6yz7%2B%2B1K0QOfCJld3lqyyyjDOrwoVuvJHdg7lKxsOK08lvxJXABzav0MtOBLHCIi8RMrdB%2BHDxDbN2B%2FMyGBAGVnO85fkUoqIBIvmn1pbmrvDMK6AmLLn6onCVRTLxRgKm5lXVjL2aEnuV0nkn%2FcpdeYXKM4h68L3Vm6NIsS2cVT8EowKy7dXSdg6bUPaoZxZ0yJnGHdiLKNmoe5x5MpyhL87wS%2BlRbsoEttlNCRyK2wo2qzUyqjPDAb%2FdMUmQWVKK6cKSQvoPeLqqPRxmqMKWtvc4GOqUBm8v%2FU9dgHvGQJ3xiYeODXgTSrqKKrmhtcF22UTOnZADM112iQ5sSoPpDwOq1i7%2Buu5JQZs3R8rZEFfPYr%2FoMuthRwxmuLklp8eg%2B8vGgBoNc3EZG3g7xVKom%2BYX77CsrtKXwNV9w%2F%2FKvY0QcP8zA4S05yoUEHgF3Z%2BWMWrMP%2F4%2B4pwTX7YNggigAw4YpVXI3DC4DkB%2F2i93H7Xbm%2FpPhJlBEqgtn&X-Amz-Signature=abc7625fd5e0e99f2fde15056f2a25c64d7415665b792147650d9bce681461ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HQKKJZJ%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFoAoYezWvur6UEhARYVmILxDhWeipfODeHBgYuQsdcBAiEAiRLHngd3OWc%2Fs%2FFGZ6Ag1J4gVhQURtMgDwFGD4Y9B0oq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDJtBgBGxb%2Ff5FXdlRyrcA8MTFvLu0m3da5VJD%2Frc%2BAi0RpWhS7rFHujba6gafkL4nDjS8VghZzbEorpyUFmvDQSmjl400ljZ5qovDGwm0f7POhhYICCN7MRlgoLDBndbDn4psTxhq9sDdpBWiO1V%2FT7V14Qsx6vRxyhHd37sRcKve3LgBDuUhQmL%2F6xabzPK4V6Mfa3lB3TVc%2B68YDTnvFVjSu1HMPz7cd%2FzvUqng1HMxGJzPojVPwchCReOX6%2F%2BDbnEVy3EQLbyYXvsfoL121o2bcHzFYpWh%2ByPf8T0Q%2Fwuia2CSm7rK%2BdVBKxGSKBbXni7xXj%2FuhPaap3xw65GbKE2IwfnxDXSgWrNVteuxKBf9lnyGrEuZV88duNdl6yz7%2B%2B1K0QOfCJld3lqyyyjDOrwoVuvJHdg7lKxsOK08lvxJXABzav0MtOBLHCIi8RMrdB%2BHDxDbN2B%2FMyGBAGVnO85fkUoqIBIvmn1pbmrvDMK6AmLLn6onCVRTLxRgKm5lXVjL2aEnuV0nkn%2FcpdeYXKM4h68L3Vm6NIsS2cVT8EowKy7dXSdg6bUPaoZxZ0yJnGHdiLKNmoe5x5MpyhL87wS%2BlRbsoEttlNCRyK2wo2qzUyqjPDAb%2FdMUmQWVKK6cKSQvoPeLqqPRxmqMKWtvc4GOqUBm8v%2FU9dgHvGQJ3xiYeODXgTSrqKKrmhtcF22UTOnZADM112iQ5sSoPpDwOq1i7%2Buu5JQZs3R8rZEFfPYr%2FoMuthRwxmuLklp8eg%2B8vGgBoNc3EZG3g7xVKom%2BYX77CsrtKXwNV9w%2F%2FKvY0QcP8zA4S05yoUEHgF3Z%2BWMWrMP%2F4%2B4pwTX7YNggigAw4YpVXI3DC4DkB%2F2i93H7Xbm%2FpPhJlBEqgtn&X-Amz-Signature=d9d1f5050af5f73949056eb8dbee17330fba94e7e2e6b477335804820dbad417&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

