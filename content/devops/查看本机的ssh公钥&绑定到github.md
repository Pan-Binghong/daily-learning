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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD3VLNGT%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIHQJa5i5nL0x4zY7P2FaBwVTOrZfzgGLM3E9Qsmu%2FrPJAiEAp1uLryTQG%2BWKxl7Wb8ny%2Fi21IJyodqrzJoATGqtalocq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDKr81Lhrjo6D15PJ4yrcA2%2Buzcv2MkHAFTpqZvqKiW7H8MvKniL8zBA403KBaDrXEjq%2FlYAcMsyUYO5r4WDyTlDNjYmtEeiPGXqVaompag3r0Ks6NDvjmUnRhXyHORYQBUfdj8mErUTr5IsQfHk4QsX8OhS3stje8CydDdEBltViRm%2FIWebRLFnk4Za0M5kMRD8sbOgDkYFGH7O07%2Bz8KzY1p6Yg2%2B%2BQ146U0SJ1u1u2J4HRjXMKu%2Bi1U8JrOI37Xr0ShiPIwOIYFxvKnayDIFiFpN0Y%2Bvh8A%2FSNrzCKJshnFZ0rIwwv5R2AhdkWMfR25KCAVaEBgSf9ZJKKKIWewPbAuca6ijalTCJVr2NCHtlhrAmAnuyKUt%2FOy86g%2Fg3nFPT34PDhUDj5%2FI9yZ4MkRGN7QzntkMLftOtdJyKHsjcMD%2BM4EbAeRvaZiY1H73ppfIV15pFz3IYsYR5qIWc13xZxj195R9dFVOpgSSCPsORjt1BUU1Mizj0LxG7x0TsQaqy9tJ%2FyIvj3zUeAf45rguQj7T9uQ22erOeRAe6H5udnFO0FGQdALJddXzmuK1gs3QRS77lQgmTzyK9IG9kT8eFsO36CWecJDDHFk8MjZxvnFikhTgQbINY9IYvIFpx3Qrxhw6rZMTc92l15MP%2F8uM0GOqUBrYhofuhGM6y5mFxlL4x%2BfJ988tQNnV%2Fi%2B38hEvpZeBM4S1onInaRjm3b0id4FaUJFaFHh4W3Csj1i6qFVG4d%2BlKZjzn5bAxkCVnj7VzhdUo2YamBviDJYwRGVzTf3aDJ42PLtVdqNl66XQ2je%2BJF4KiGQm7DvDfZu7Oog8lJD7V%2F2WqMReLJtAMqogv7BEE9JwkVyGuzaGukr%2FBGSu8iscO21LOF&X-Amz-Signature=52e676aa212671e81a46a6224c15b2ad4ae55246a10cb2af26222af2aa27524d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD3VLNGT%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIHQJa5i5nL0x4zY7P2FaBwVTOrZfzgGLM3E9Qsmu%2FrPJAiEAp1uLryTQG%2BWKxl7Wb8ny%2Fi21IJyodqrzJoATGqtalocq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDKr81Lhrjo6D15PJ4yrcA2%2Buzcv2MkHAFTpqZvqKiW7H8MvKniL8zBA403KBaDrXEjq%2FlYAcMsyUYO5r4WDyTlDNjYmtEeiPGXqVaompag3r0Ks6NDvjmUnRhXyHORYQBUfdj8mErUTr5IsQfHk4QsX8OhS3stje8CydDdEBltViRm%2FIWebRLFnk4Za0M5kMRD8sbOgDkYFGH7O07%2Bz8KzY1p6Yg2%2B%2BQ146U0SJ1u1u2J4HRjXMKu%2Bi1U8JrOI37Xr0ShiPIwOIYFxvKnayDIFiFpN0Y%2Bvh8A%2FSNrzCKJshnFZ0rIwwv5R2AhdkWMfR25KCAVaEBgSf9ZJKKKIWewPbAuca6ijalTCJVr2NCHtlhrAmAnuyKUt%2FOy86g%2Fg3nFPT34PDhUDj5%2FI9yZ4MkRGN7QzntkMLftOtdJyKHsjcMD%2BM4EbAeRvaZiY1H73ppfIV15pFz3IYsYR5qIWc13xZxj195R9dFVOpgSSCPsORjt1BUU1Mizj0LxG7x0TsQaqy9tJ%2FyIvj3zUeAf45rguQj7T9uQ22erOeRAe6H5udnFO0FGQdALJddXzmuK1gs3QRS77lQgmTzyK9IG9kT8eFsO36CWecJDDHFk8MjZxvnFikhTgQbINY9IYvIFpx3Qrxhw6rZMTc92l15MP%2F8uM0GOqUBrYhofuhGM6y5mFxlL4x%2BfJ988tQNnV%2Fi%2B38hEvpZeBM4S1onInaRjm3b0id4FaUJFaFHh4W3Csj1i6qFVG4d%2BlKZjzn5bAxkCVnj7VzhdUo2YamBviDJYwRGVzTf3aDJ42PLtVdqNl66XQ2je%2BJF4KiGQm7DvDfZu7Oog8lJD7V%2F2WqMReLJtAMqogv7BEE9JwkVyGuzaGukr%2FBGSu8iscO21LOF&X-Amz-Signature=e3c2df5c09985f7ed331c2a434e3b06db166dbc5984bac974bbbe212adb81f7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

