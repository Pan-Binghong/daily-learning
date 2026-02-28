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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNMIIV4X%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuVGSFPcg3pxl4KbaCzGw7dAoUM%2FD%2BnLQRni9Nh%2BwVZgIhAPpKdIPL0xeJGvjN3o7fGwgrvinf6Phdp5mbMA4uc0Y6Kv8DCEsQABoMNjM3NDIzMTgzODA1IgxDWToVtc7TawPfvZ8q3ANqRolksLU8BWZQliODI%2FkNbLLkh3GUg62w%2FONh4UbovzzHh6x2vHrMElporWa1L4Df6VwFPl7LwyvM2IfyTcK2plBs%2F9ksuDadAFixECNLiFzlBJelQlEvlS9KNF1idzjKkMZTOXqTxYHlNKOwT5k3ntrvKMIHaxELZ3r9LuJyZh%2FjvJIFyXZ0YM%2BIuqxyWk%2FfvUp3Jb%2FSQoRyF6azrEOT2G%2B35ZRfwZh5dv%2FxhwW3ub2sRm5lZoG4j0IDOlgEHKvz0aZhObZVyNzErTPQQlOUIfAhi%2B1UwOBynzO6JorsOID92XC%2FlIZpNGIDy4QrBXGPWldSJm0dOc6S8TFzqVUSI3QUMP5x3lhORC6w2ADRpZfxX6HFj0nqqZZzmZPfTGSrZB%2FQQn%2FHO%2BGjBOHclgySn264U7D6VXuwBOqMlqDKbX5obFMdRxu8X%2Fjk6uO3D%2FJiLph04w8sVz1IitRvXMy2zKEbhu%2BRuAmlb7yC4xMWpmRReCO%2FQZC9%2Barfd2L2hA6PvQfCob0d48T5M3IXR1zbIdzBFK4wE4P%2FZXoMrGu%2Fzy74aJx6mhYLthz0LZAdiOaNxlajNr53l8QrTE9by9q5siIZEz1cvTAWXnGwZ%2FuPel1MvtgQ1BNQ%2BWgcWzDDlonNBjqkAXvrNZplthMlZ1mCIX%2BGoGAA%2F3ibyARFxs4g3M5tf4GoIa1SbLEgMZc9e3o4m%2FqwDgrAiVblL2YJiYcUDe1MPrFEQH1JMFNEQe2H9hJdYgIbDyCrVkYBDJI4jpuGnZ0QBIQTxxBMjBnLS1WvcqKuOiDraxkvL1QFjTtQA1lyQTlQ8Im%2Fom64zSiOFkXdi34IWulDTua5OQahRiGkfEo%2F2t3uI7ux&X-Amz-Signature=b213979fda95dd2317857fbff742010445a75035985f7d9421c088d7bebc491c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNMIIV4X%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuVGSFPcg3pxl4KbaCzGw7dAoUM%2FD%2BnLQRni9Nh%2BwVZgIhAPpKdIPL0xeJGvjN3o7fGwgrvinf6Phdp5mbMA4uc0Y6Kv8DCEsQABoMNjM3NDIzMTgzODA1IgxDWToVtc7TawPfvZ8q3ANqRolksLU8BWZQliODI%2FkNbLLkh3GUg62w%2FONh4UbovzzHh6x2vHrMElporWa1L4Df6VwFPl7LwyvM2IfyTcK2plBs%2F9ksuDadAFixECNLiFzlBJelQlEvlS9KNF1idzjKkMZTOXqTxYHlNKOwT5k3ntrvKMIHaxELZ3r9LuJyZh%2FjvJIFyXZ0YM%2BIuqxyWk%2FfvUp3Jb%2FSQoRyF6azrEOT2G%2B35ZRfwZh5dv%2FxhwW3ub2sRm5lZoG4j0IDOlgEHKvz0aZhObZVyNzErTPQQlOUIfAhi%2B1UwOBynzO6JorsOID92XC%2FlIZpNGIDy4QrBXGPWldSJm0dOc6S8TFzqVUSI3QUMP5x3lhORC6w2ADRpZfxX6HFj0nqqZZzmZPfTGSrZB%2FQQn%2FHO%2BGjBOHclgySn264U7D6VXuwBOqMlqDKbX5obFMdRxu8X%2Fjk6uO3D%2FJiLph04w8sVz1IitRvXMy2zKEbhu%2BRuAmlb7yC4xMWpmRReCO%2FQZC9%2Barfd2L2hA6PvQfCob0d48T5M3IXR1zbIdzBFK4wE4P%2FZXoMrGu%2Fzy74aJx6mhYLthz0LZAdiOaNxlajNr53l8QrTE9by9q5siIZEz1cvTAWXnGwZ%2FuPel1MvtgQ1BNQ%2BWgcWzDDlonNBjqkAXvrNZplthMlZ1mCIX%2BGoGAA%2F3ibyARFxs4g3M5tf4GoIa1SbLEgMZc9e3o4m%2FqwDgrAiVblL2YJiYcUDe1MPrFEQH1JMFNEQe2H9hJdYgIbDyCrVkYBDJI4jpuGnZ0QBIQTxxBMjBnLS1WvcqKuOiDraxkvL1QFjTtQA1lyQTlQ8Im%2Fom64zSiOFkXdi34IWulDTua5OQahRiGkfEo%2F2t3uI7ux&X-Amz-Signature=a31cfe59881cdd17ec1109379e16e27a363ff680a7939db8d7c2cadb264b9db6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

