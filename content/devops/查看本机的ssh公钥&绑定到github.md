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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4QNEZBH%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDmmyq9B588YnBxz2i0HNHbYAhqdhAnSbPQ4DTA35sKtAiEAkDH1GJzBOGE%2FlhgH9V8vOGEFcC6jMrR0eKQlR%2BgBcZQq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDL3yzJ5ISzs%2Bsj8nGircA%2Bwn0bV5wIXFr%2B6ywcUFiCqeYE9HcXskIoSpv7QpbHXQVkZAY5qvhgY8wwDum66WGFiIzOl7KC0YHC7i0I%2B%2FelCplV5T0OiFdyxXm6ArIZ5VUxviKQlBoRw6PMZeVaYIGh%2F%2B0AUyf%2BVnGqJQtmHMg2OCw8QaexfFoIBdziXGcGQzsRBHUayjMPjbAxeAqHymu8RFO6obbmRo%2BtiKeU2BJoXKnkFnIoUdrlMSmORfXm8rqbLj3ugEdAwY7KwEVLZInCW6VJgFH%2FHQ7puYCLQDf3ww%2BpIIAALB9bQ59ou1oNdOAqCXI%2BZHvPfzdL%2FftyJvcUNFY3ZgmBEvQrypt6t1ov8N%2BpPAdRVyhrgZbUsGbqd0xAibt%2BSQ8iTUp7j9vRFDgMdW0bZyZxsibdHqhnesODO3sNzvfOxiipIyQpmYtwi%2FeYNwdhTksrLbnA%2F0YAScchXMhcSsqL9k%2BlOfM%2FvtqQK0OMcDZ6QyEt3w5pu3gmZoVAmWmkcksgRIZ8zpsHsX1GQFd6fDrPDm8oHZ9tJz1S5WlOGfxNN1S%2FU5vDk%2FeC4PUWR2Aut12v9zK0opEwHdyowLgzZJeSV1AG8bEhPIZOjlliHguh%2FqF16%2BjmII%2F%2BspF6AUcsD4cmsB7xQTMNTyws0GOqUBIbfcly8mGpY4LCJqpC0cE75za8PFEBENFMJPTeq6YmZ8y%2B8eUR%2BPnB2jeZj0XnBWKkMT4kxzdbl4wmzvzBMDn3O4AZdtiKl1fJXLUofR%2BIW1zt3MCMUvuAT%2Bm4x5z%2BZOQWMGnDXTzUIyrIb%2FybPUncylSEhVGpedRAzGMLgQ3MTt7GV8CP9SSfY7U%2B6M49NheLVAP4FG%2BbVwDd%2BMnmdvwwSxxCee&X-Amz-Signature=e9aaf4e42b5847f848447d0ce565bd81bab86e291df790e15aad8e62377db481&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4QNEZBH%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDmmyq9B588YnBxz2i0HNHbYAhqdhAnSbPQ4DTA35sKtAiEAkDH1GJzBOGE%2FlhgH9V8vOGEFcC6jMrR0eKQlR%2BgBcZQq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDL3yzJ5ISzs%2Bsj8nGircA%2Bwn0bV5wIXFr%2B6ywcUFiCqeYE9HcXskIoSpv7QpbHXQVkZAY5qvhgY8wwDum66WGFiIzOl7KC0YHC7i0I%2B%2FelCplV5T0OiFdyxXm6ArIZ5VUxviKQlBoRw6PMZeVaYIGh%2F%2B0AUyf%2BVnGqJQtmHMg2OCw8QaexfFoIBdziXGcGQzsRBHUayjMPjbAxeAqHymu8RFO6obbmRo%2BtiKeU2BJoXKnkFnIoUdrlMSmORfXm8rqbLj3ugEdAwY7KwEVLZInCW6VJgFH%2FHQ7puYCLQDf3ww%2BpIIAALB9bQ59ou1oNdOAqCXI%2BZHvPfzdL%2FftyJvcUNFY3ZgmBEvQrypt6t1ov8N%2BpPAdRVyhrgZbUsGbqd0xAibt%2BSQ8iTUp7j9vRFDgMdW0bZyZxsibdHqhnesODO3sNzvfOxiipIyQpmYtwi%2FeYNwdhTksrLbnA%2F0YAScchXMhcSsqL9k%2BlOfM%2FvtqQK0OMcDZ6QyEt3w5pu3gmZoVAmWmkcksgRIZ8zpsHsX1GQFd6fDrPDm8oHZ9tJz1S5WlOGfxNN1S%2FU5vDk%2FeC4PUWR2Aut12v9zK0opEwHdyowLgzZJeSV1AG8bEhPIZOjlliHguh%2FqF16%2BjmII%2F%2BspF6AUcsD4cmsB7xQTMNTyws0GOqUBIbfcly8mGpY4LCJqpC0cE75za8PFEBENFMJPTeq6YmZ8y%2B8eUR%2BPnB2jeZj0XnBWKkMT4kxzdbl4wmzvzBMDn3O4AZdtiKl1fJXLUofR%2BIW1zt3MCMUvuAT%2Bm4x5z%2BZOQWMGnDXTzUIyrIb%2FybPUncylSEhVGpedRAzGMLgQ3MTt7GV8CP9SSfY7U%2B6M49NheLVAP4FG%2BbVwDd%2BMnmdvwwSxxCee&X-Amz-Signature=5022c04e02820e96f3072647483d277b2dece8b3d093910664c08e98ccc2ac23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

