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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSN7ZEBP%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDjaVHELF1CDQwGTnZavHlfrmeqbPj3cnc99oxJBKUzOAiEAvXpgLeS8xuddQG9BihVCc4IIO1sBbTPrDp%2BE%2FjZB5GMqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIbAGjg1Py3svjwu%2BCrcAyqJ9Tz0u34xdUi82dY%2FF9hfREiyoiiPGJx5ltnJZrQ8xoumpz6eiM2EaEgWxy4zhb9piVBltxpOUKazL679HU2lXBtrVF39yrZxGEp2OrR13OuFLRIQ8c3tIJT5b2tWwtaLEuRileLsHsbKwijjQnMWf9Qr66Fe%2BcGYA1hZpAKlEYnh54y4EuahBcWVu9NT0uWoq3pvlaGbnEWaxaCJ6ec26gt3Iup1gtVx2vY%2Fgi5GOfkDc0%2BIwDv4V4Dig8gJYpCIaNHs66C3g5dpEH%2BbSapjuiiUB6HUmKOHKA3fOHyDIGwnaEIvIC30oYISNQ2Jxp0%2BZ8o9ncQDbzYh48o7axcePMU9IB7KKmErF4AXteBRFxII06IKpYgjMzxOXScD5%2BB9vjJRH7KQ5g8qJBEOk2TtICN5BlZE7YvmlGESZ8oXwsmLsh8sXM9KUydIvOR%2F4gHHjMHiiV7ywxcgx1gsqPs0BWDcwEyNiYt7uy60o%2BhSxG4hawjNv0m7bmdbJzUoeN37WrmOkhLuOCxHdUpLEgA%2BrWyhvoS53RCzpZYQBKVKrZDc1EmcMZrryI4ve4LBUcaC52%2FacbUhlr7mlqVQAMRbP5LBLz02xAqeB0RGnYfwTr3avPPz%2B9LVJgkqMMLz6cwGOqUB7XM%2BiupKEyPa42o3oC%2FifxobN3q6w7oYOlLIH1r5tvFTRoSoUBstcHQlW2NVF5tAj9ftNtACDVDJn7IOb536ue6Df9gTVEN8S7lYXKUJ67c8O%2BTcuD22ImAgxDcTxJ%2Fks18CB9pzbP0gfVMMGOSI8AbyzBHCalPVku7Vptw4QhwU7seRskuD4CUV%2FZCFP9g2iMuk60UXA5sf99ZQMpmHBNavfvxi&X-Amz-Signature=dc5e068de791a472d824d451246b1f5c676fd18a5f29ae355ae4122234a832a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSN7ZEBP%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDjaVHELF1CDQwGTnZavHlfrmeqbPj3cnc99oxJBKUzOAiEAvXpgLeS8xuddQG9BihVCc4IIO1sBbTPrDp%2BE%2FjZB5GMqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIbAGjg1Py3svjwu%2BCrcAyqJ9Tz0u34xdUi82dY%2FF9hfREiyoiiPGJx5ltnJZrQ8xoumpz6eiM2EaEgWxy4zhb9piVBltxpOUKazL679HU2lXBtrVF39yrZxGEp2OrR13OuFLRIQ8c3tIJT5b2tWwtaLEuRileLsHsbKwijjQnMWf9Qr66Fe%2BcGYA1hZpAKlEYnh54y4EuahBcWVu9NT0uWoq3pvlaGbnEWaxaCJ6ec26gt3Iup1gtVx2vY%2Fgi5GOfkDc0%2BIwDv4V4Dig8gJYpCIaNHs66C3g5dpEH%2BbSapjuiiUB6HUmKOHKA3fOHyDIGwnaEIvIC30oYISNQ2Jxp0%2BZ8o9ncQDbzYh48o7axcePMU9IB7KKmErF4AXteBRFxII06IKpYgjMzxOXScD5%2BB9vjJRH7KQ5g8qJBEOk2TtICN5BlZE7YvmlGESZ8oXwsmLsh8sXM9KUydIvOR%2F4gHHjMHiiV7ywxcgx1gsqPs0BWDcwEyNiYt7uy60o%2BhSxG4hawjNv0m7bmdbJzUoeN37WrmOkhLuOCxHdUpLEgA%2BrWyhvoS53RCzpZYQBKVKrZDc1EmcMZrryI4ve4LBUcaC52%2FacbUhlr7mlqVQAMRbP5LBLz02xAqeB0RGnYfwTr3avPPz%2B9LVJgkqMMLz6cwGOqUB7XM%2BiupKEyPa42o3oC%2FifxobN3q6w7oYOlLIH1r5tvFTRoSoUBstcHQlW2NVF5tAj9ftNtACDVDJn7IOb536ue6Df9gTVEN8S7lYXKUJ67c8O%2BTcuD22ImAgxDcTxJ%2Fks18CB9pzbP0gfVMMGOSI8AbyzBHCalPVku7Vptw4QhwU7seRskuD4CUV%2FZCFP9g2iMuk60UXA5sf99ZQMpmHBNavfvxi&X-Amz-Signature=7469433acdfdfa5369336dfad18fe942e507ce7abc62d32ff526d78098cc3ce9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

