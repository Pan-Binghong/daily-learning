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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWFYJSAV%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T032050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQDDYAVqQLtO5rX5prIjOryCDEC0selqjqLIewATh5yxPAIhAIFhPiEMGD6yROzfoKlkI9geU7CkCM3sEAYER5RUr2jBKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxK74fi0Sxdk45S3xoq3AOCrixqiTJ%2BNYPoqSCWUdxWULEt0U%2Fym1H7X43dfghslsF6kVvq%2Fl%2B%2FboZGtStAassImIWf88UqYRv9Kz%2Ft8%2BFg0hQTnVQ7J%2BM6RFof6jTGb8NMatBpmYyzHRT4LaKoKNkAzQLmIloyMTc0s4kfG0puaKk97PMctTRpxFOmwMi4x9x%2B6xFs%2B1eVj24ZuNElVwkDo6Po79p7ssUz1VqvghbIlnqVBDDJpq5bwPjndVM4wQgFuZdDho6GDdxubtuEyM7WC1m%2FZ77oq3km1bmXude1gGYleFN%2FX3LMUD%2BdsWuh54j%2F8hWouIlbd0elHsPZXuHOrigrcOH%2B6ryrBW5AloLzawORNZ00dYSZsgqz1GpPqJY51XO%2BqQHylhC%2BnbfG4fGIWZvjwEU6XJXgyXi%2BREhHQ1PlK94XDOWY1ZDcuZiEIT4SWUWfGDt2Ja1bpc78I%2FYAVICJWE47pLwjc6IfoMqAYNXuUHjDZoyTixofglia99d988df9VrAxxAjllfp6fyRaQqygd66c7q5pjdf1ZxJO026%2FwZP7RQMrsUvh%2F3gKy%2Fg6tzi4mZAdz97or3%2Fq08O%2FUrxEPI4bY08rdfVd5uggMFSQ94J%2FAhPtuwrhKDqQRRhEb7c3Q5bSgFf2DCGlK7NBjqkAWgWTDxcGhIAEoXOZkpQAi0o6C5Yimkgr6zeoD%2FRWmzbv1LpPy0FlE646jGlgd1h5F1uM5qEi9vm56Wz1TAQ1wqpcrN%2FZXERPidUduMbiVnKVqjJNyrk6Eic8%2FytKE0AoU3y5NXWjaJhQ9rRueuXli6AV4yhKoQ0RMex7WYxlkvZ9O6kA0yL82fDM2sTqJoW%2Bg3gwGPduNSZJYKGW%2FtnaVrViBhP&X-Amz-Signature=881bc8b18c1671a0c4209dab8accf6f17d89f226a6feed56daa691a6180ed7ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWFYJSAV%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T032050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQDDYAVqQLtO5rX5prIjOryCDEC0selqjqLIewATh5yxPAIhAIFhPiEMGD6yROzfoKlkI9geU7CkCM3sEAYER5RUr2jBKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxK74fi0Sxdk45S3xoq3AOCrixqiTJ%2BNYPoqSCWUdxWULEt0U%2Fym1H7X43dfghslsF6kVvq%2Fl%2B%2FboZGtStAassImIWf88UqYRv9Kz%2Ft8%2BFg0hQTnVQ7J%2BM6RFof6jTGb8NMatBpmYyzHRT4LaKoKNkAzQLmIloyMTc0s4kfG0puaKk97PMctTRpxFOmwMi4x9x%2B6xFs%2B1eVj24ZuNElVwkDo6Po79p7ssUz1VqvghbIlnqVBDDJpq5bwPjndVM4wQgFuZdDho6GDdxubtuEyM7WC1m%2FZ77oq3km1bmXude1gGYleFN%2FX3LMUD%2BdsWuh54j%2F8hWouIlbd0elHsPZXuHOrigrcOH%2B6ryrBW5AloLzawORNZ00dYSZsgqz1GpPqJY51XO%2BqQHylhC%2BnbfG4fGIWZvjwEU6XJXgyXi%2BREhHQ1PlK94XDOWY1ZDcuZiEIT4SWUWfGDt2Ja1bpc78I%2FYAVICJWE47pLwjc6IfoMqAYNXuUHjDZoyTixofglia99d988df9VrAxxAjllfp6fyRaQqygd66c7q5pjdf1ZxJO026%2FwZP7RQMrsUvh%2F3gKy%2Fg6tzi4mZAdz97or3%2Fq08O%2FUrxEPI4bY08rdfVd5uggMFSQ94J%2FAhPtuwrhKDqQRRhEb7c3Q5bSgFf2DCGlK7NBjqkAWgWTDxcGhIAEoXOZkpQAi0o6C5Yimkgr6zeoD%2FRWmzbv1LpPy0FlE646jGlgd1h5F1uM5qEi9vm56Wz1TAQ1wqpcrN%2FZXERPidUduMbiVnKVqjJNyrk6Eic8%2FytKE0AoU3y5NXWjaJhQ9rRueuXli6AV4yhKoQ0RMex7WYxlkvZ9O6kA0yL82fDM2sTqJoW%2Bg3gwGPduNSZJYKGW%2FtnaVrViBhP&X-Amz-Signature=6acc6c869b04820d144189e6a7c87d83866810cb72a46bba3ef6d7a411976a52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

