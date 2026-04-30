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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GROKOO2%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDP8lnUTuJxcmNsAQ%2Fl%2FXsYc3uVmZTIo6u317ICJHIMEAIgGTXNIyucxFBbDfvSdzeFBqgfVzhkxInHKNi%2BuZLKNnoq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDJC5kIpckJ4y41adWircA%2Fh%2FzUde9meicL0gHNqVJRAB2OmSOZBx0%2BkIM6BeibTuxIKYlA9qSacWHC1AwFvKxfKwmUJj7k6ORz6QLR34VRIdXHxZo2N5767%2FF%2FaW2%2F88t94Gl9HYZtPgN%2FQ9wxoHEpOH4y3e7qFmqFktoudoNfUI%2FaIwl8ghDYAXfeVZuAhJFhHlGOLNFP6sfUNIi1wgV9sO6jN3Zvy7jgi1ziAClATqHXqkn7%2Fhnm4S%2FoL42StvTk6rZ5d24sAobI%2B9ivHV7b8wYs3UQT1NH0gTso33Zl%2Bf9MDsjajl0aJZAyeCiFquGadV5n6nXVTMK2SAQ1Yg%2Fr32C%2BjR9e8ge%2BTIqtKME7KxNZnD3jKSnJNp%2FkS978nr1vVonWN6C8CprW0DcR1Lm1oH8EU5Mvh80n9fwbYqS0XHSaEh0vJpECOSGhMcNUIKLQ6ByxjmENmBl8UnbGu0Q1Lf8K9PvOKtp1K9VhyDloORsfRb9DpCf9VudkzWwOii%2BrNYuUdpncUKTZgFhjGxCc02j2D66OQPlUabj3MmpkqzFNz3VeM4xuCMPzUP5m62tgd%2BSC122zXpXY8fichItGo871Q%2BRDeebiezq4rxq%2FdQYtCm3Rat8swfC%2B1aNY%2FteQ3yu%2BvtMyrU9AYLMJubzM8GOqUBvj7vMh44phk%2FpVbUQF2FQxBPa47YSTogGgCZ42FNfZUKaiLg80bcg5KF25MRgobho9H3BPRXk9G%2BDOCeSshOxAtVZ%2FGx0m2BL%2FgiNcszxpPXnUM1rdoOS0dZxxrnotSHB1Dnes0aOmGf4tKKeeTPpEGH%2BhNB8NJpPXtVfBUitd0iGITWfihwbSvx530jiLDBqbk%2BjW176JFeEagdO3EuMkOKvRAU&X-Amz-Signature=3dfff70c23986555204051418f0d6a1bf1a76dc5b6ff93ecc36027382dd2f1a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GROKOO2%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDP8lnUTuJxcmNsAQ%2Fl%2FXsYc3uVmZTIo6u317ICJHIMEAIgGTXNIyucxFBbDfvSdzeFBqgfVzhkxInHKNi%2BuZLKNnoq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDJC5kIpckJ4y41adWircA%2Fh%2FzUde9meicL0gHNqVJRAB2OmSOZBx0%2BkIM6BeibTuxIKYlA9qSacWHC1AwFvKxfKwmUJj7k6ORz6QLR34VRIdXHxZo2N5767%2FF%2FaW2%2F88t94Gl9HYZtPgN%2FQ9wxoHEpOH4y3e7qFmqFktoudoNfUI%2FaIwl8ghDYAXfeVZuAhJFhHlGOLNFP6sfUNIi1wgV9sO6jN3Zvy7jgi1ziAClATqHXqkn7%2Fhnm4S%2FoL42StvTk6rZ5d24sAobI%2B9ivHV7b8wYs3UQT1NH0gTso33Zl%2Bf9MDsjajl0aJZAyeCiFquGadV5n6nXVTMK2SAQ1Yg%2Fr32C%2BjR9e8ge%2BTIqtKME7KxNZnD3jKSnJNp%2FkS978nr1vVonWN6C8CprW0DcR1Lm1oH8EU5Mvh80n9fwbYqS0XHSaEh0vJpECOSGhMcNUIKLQ6ByxjmENmBl8UnbGu0Q1Lf8K9PvOKtp1K9VhyDloORsfRb9DpCf9VudkzWwOii%2BrNYuUdpncUKTZgFhjGxCc02j2D66OQPlUabj3MmpkqzFNz3VeM4xuCMPzUP5m62tgd%2BSC122zXpXY8fichItGo871Q%2BRDeebiezq4rxq%2FdQYtCm3Rat8swfC%2B1aNY%2FteQ3yu%2BvtMyrU9AYLMJubzM8GOqUBvj7vMh44phk%2FpVbUQF2FQxBPa47YSTogGgCZ42FNfZUKaiLg80bcg5KF25MRgobho9H3BPRXk9G%2BDOCeSshOxAtVZ%2FGx0m2BL%2FgiNcszxpPXnUM1rdoOS0dZxxrnotSHB1Dnes0aOmGf4tKKeeTPpEGH%2BhNB8NJpPXtVfBUitd0iGITWfihwbSvx530jiLDBqbk%2BjW176JFeEagdO3EuMkOKvRAU&X-Amz-Signature=601f236813ce2185dd20bdd5037f71147daa2cba4b0f2069688e2209bf9268cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

