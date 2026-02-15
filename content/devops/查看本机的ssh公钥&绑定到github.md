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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMDN5ZSF%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQDJCOLMGLThmhv%2BjKWC3koV2BmCUgXsf7awYRqI3OqxcwIgf12rRez4zlkEVcu%2F0TNtkltGlJlTh18KXrxh3XMOx%2Fwq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDDpMKw8HdV8HwLw99yrcA7h3%2FbJ9OUTmvN%2BZJNmc7SzFFGAcIcxHciCiC%2F5IcaIdEuHrsGPTVC2h1iDiNCCCzA1UN14RCC1rTeMdCPJLqPoPwkLtXeZwbOvSxrmZWabeMBjMZiWzZgUDgl4p%2F2pZapEDLfFOcZrItbrAkBefW5DygrIz%2BD%2FL9pcfy6zwrpcwEIvNp4evkHlxp4%2F0OTAqehNbyTMwo%2FXo8C9FbrQrPiJjbMBPtUv4kboDRk%2B7Iwgsx3UpZPb911ejykWVYTfTCH9Bzi5lHPJwGkM92kkd0pAaq3cd4nZ6oJSY5dVmPwPevrdqiUQbro2nV%2FCHJ1GSLOdsFLAJxrbiZxVl6bun6WXYyl56Ru%2BpXvhFJ33QdmMLQO9ZAoK%2FVsv1NCa8XwAHsoB4RXneUHx3uaOXHB1IoIgXSVqPDTHcxKz1paVruBi8Aqkef3kJrKJW%2FuL0e2vZW1fHgH0SmqNVX7JCesJXjITg0oRdZt44Hs0S6kO4ESgachIVaBlLeLEdY5CgM%2Bqz74SxxtPLfwme2%2FB%2Bh%2Ff0BeCQw1nB5Mu57mivUyLnJm9%2Ft3PaVe3ROflOe1cFq%2F2bkaIQjiGICY7PvNnUD9QJYzWzEjUbKtoB69nR7U2COJbDuuW1d36gfJQLbPPqMPSdxMwGOqUBErm46U56gSgsXXAFVqiMtREUFgeK%2F%2FMF3pmV46oGV%2Fg9SoCNqLWe5yAgW2wpGBiTWWE1wvmSkT5iWfJfpcPV881CLheKyIyeD8gnSBG2OE0XM%2FmQAL%2Bwia9%2BWsMlQsR2Qtu5lVElKuNEiGHE4cIBGPctK%2BR8c33QeIUWtAjKqRczWJQxoxNPx%2FJsyOCcau6ip%2F%2FdPGdn7KDMH4Yk25u%2B8ni73OGP&X-Amz-Signature=3660e6d3498edbf4796ce34676412f8e0ca6f0f3d252e161678f1c91cd9885a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMDN5ZSF%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQDJCOLMGLThmhv%2BjKWC3koV2BmCUgXsf7awYRqI3OqxcwIgf12rRez4zlkEVcu%2F0TNtkltGlJlTh18KXrxh3XMOx%2Fwq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDDpMKw8HdV8HwLw99yrcA7h3%2FbJ9OUTmvN%2BZJNmc7SzFFGAcIcxHciCiC%2F5IcaIdEuHrsGPTVC2h1iDiNCCCzA1UN14RCC1rTeMdCPJLqPoPwkLtXeZwbOvSxrmZWabeMBjMZiWzZgUDgl4p%2F2pZapEDLfFOcZrItbrAkBefW5DygrIz%2BD%2FL9pcfy6zwrpcwEIvNp4evkHlxp4%2F0OTAqehNbyTMwo%2FXo8C9FbrQrPiJjbMBPtUv4kboDRk%2B7Iwgsx3UpZPb911ejykWVYTfTCH9Bzi5lHPJwGkM92kkd0pAaq3cd4nZ6oJSY5dVmPwPevrdqiUQbro2nV%2FCHJ1GSLOdsFLAJxrbiZxVl6bun6WXYyl56Ru%2BpXvhFJ33QdmMLQO9ZAoK%2FVsv1NCa8XwAHsoB4RXneUHx3uaOXHB1IoIgXSVqPDTHcxKz1paVruBi8Aqkef3kJrKJW%2FuL0e2vZW1fHgH0SmqNVX7JCesJXjITg0oRdZt44Hs0S6kO4ESgachIVaBlLeLEdY5CgM%2Bqz74SxxtPLfwme2%2FB%2Bh%2Ff0BeCQw1nB5Mu57mivUyLnJm9%2Ft3PaVe3ROflOe1cFq%2F2bkaIQjiGICY7PvNnUD9QJYzWzEjUbKtoB69nR7U2COJbDuuW1d36gfJQLbPPqMPSdxMwGOqUBErm46U56gSgsXXAFVqiMtREUFgeK%2F%2FMF3pmV46oGV%2Fg9SoCNqLWe5yAgW2wpGBiTWWE1wvmSkT5iWfJfpcPV881CLheKyIyeD8gnSBG2OE0XM%2FmQAL%2Bwia9%2BWsMlQsR2Qtu5lVElKuNEiGHE4cIBGPctK%2BR8c33QeIUWtAjKqRczWJQxoxNPx%2FJsyOCcau6ip%2F%2FdPGdn7KDMH4Yk25u%2B8ni73OGP&X-Amz-Signature=94090c6074c677735e0fdc87e2f8cc62ebc90ac7a6239a25098405dfc3cb13b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

