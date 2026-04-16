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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5CMWEYU%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2BilJC%2BCttgcbIi66fysJMbB%2BEZU1tooMgvMH7%2FLznXAiBKiklYycvA%2BuPkhjR3bA%2FGo5JrdoRkE1rO9axURg086iqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvpuo%2BqP8VQTtvc3rKtwDnledRJL1zNe7pL4hHznNKO61ajkE42AIoQboUIIUCtSIyXnBQq%2FRIsISPyWCKoGXja6A7UCDGImvuhEtYymgeyeVeZCinVNZ4D0FGf6t0yO81dABLnvmpLIXtYSuPyhxUw2sGjeQti1AWsHMF78LvywaxOfFk8YhaME7%2FxvmeYR5YuSMPQZYQAF6iC0EZ1yBZ0Ma19QA6uzt6Et9ykkzmE%2B2oQaYVZ15%2B%2BZ9IIQGyVENedhAwEGVWkstNeD0hplvtwodEi6pmnTIhAaj1U4HJfc%2FsSALj1v03fmBB0U6OmdKzihjAfLd03lLbbhZeocBcAVzAEn6V8oAXwkeH3prG444NrMT5ZWXbEfLYYViDJwE0wPzkvVpm2Z8ehBGDOjDeNqAwbmt4JKvRHp1yyOf%2B9quJtlOASt0qmDldRB3l2f4ypSYRs3W6NggK3jxHl7YTlrW2d6wWdVjmQCzvAXlfmTkhjzZLxW7DIFzaIYHtzuKMmvE1umet4UzjHR1OLm3EiTrj0gFMi%2BNs550WlGDk5FToeITxM%2FjfqleBp7Jak3EpTXTpFs4GxsCSNDMXMMuN04jsZsLZTeqp8DTuj3Q2mWmX6E%2BDZLy9rS2m86njiMhZFRfv%2F5qgqbWKcEwj7SBzwY6pgEa3T2hgnbW2%2Bg12odNGb9MOauGP52C3TEN%2FWCPSPsxbpikWdDIEH60riNsMX2Fe2x%2BeHfeDLCMModoeCQuyfSZcxQfDB2cdrx%2BxIU3OqkvKsGvD2qv5EOhSepx0mLetmZ4o0Zt27uXJ24T%2Bl68GPIxuf6uRuzYex6LWkElpHsSelh9HCQ8rIp5FRQu2O41AQBpoM2M0j6Z1bzAI0DfLOZeulB%2FFodO&X-Amz-Signature=626d47a63b9eb054aef61ddbcaef8371904ed1ce042a6d5d679836de617d061b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5CMWEYU%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2BilJC%2BCttgcbIi66fysJMbB%2BEZU1tooMgvMH7%2FLznXAiBKiklYycvA%2BuPkhjR3bA%2FGo5JrdoRkE1rO9axURg086iqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvpuo%2BqP8VQTtvc3rKtwDnledRJL1zNe7pL4hHznNKO61ajkE42AIoQboUIIUCtSIyXnBQq%2FRIsISPyWCKoGXja6A7UCDGImvuhEtYymgeyeVeZCinVNZ4D0FGf6t0yO81dABLnvmpLIXtYSuPyhxUw2sGjeQti1AWsHMF78LvywaxOfFk8YhaME7%2FxvmeYR5YuSMPQZYQAF6iC0EZ1yBZ0Ma19QA6uzt6Et9ykkzmE%2B2oQaYVZ15%2B%2BZ9IIQGyVENedhAwEGVWkstNeD0hplvtwodEi6pmnTIhAaj1U4HJfc%2FsSALj1v03fmBB0U6OmdKzihjAfLd03lLbbhZeocBcAVzAEn6V8oAXwkeH3prG444NrMT5ZWXbEfLYYViDJwE0wPzkvVpm2Z8ehBGDOjDeNqAwbmt4JKvRHp1yyOf%2B9quJtlOASt0qmDldRB3l2f4ypSYRs3W6NggK3jxHl7YTlrW2d6wWdVjmQCzvAXlfmTkhjzZLxW7DIFzaIYHtzuKMmvE1umet4UzjHR1OLm3EiTrj0gFMi%2BNs550WlGDk5FToeITxM%2FjfqleBp7Jak3EpTXTpFs4GxsCSNDMXMMuN04jsZsLZTeqp8DTuj3Q2mWmX6E%2BDZLy9rS2m86njiMhZFRfv%2F5qgqbWKcEwj7SBzwY6pgEa3T2hgnbW2%2Bg12odNGb9MOauGP52C3TEN%2FWCPSPsxbpikWdDIEH60riNsMX2Fe2x%2BeHfeDLCMModoeCQuyfSZcxQfDB2cdrx%2BxIU3OqkvKsGvD2qv5EOhSepx0mLetmZ4o0Zt27uXJ24T%2Bl68GPIxuf6uRuzYex6LWkElpHsSelh9HCQ8rIp5FRQu2O41AQBpoM2M0j6Z1bzAI0DfLOZeulB%2FFodO&X-Amz-Signature=c108af40fe474afec9bfd288d06753f1ddac0513130d3aa9aee800ee37513694&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

