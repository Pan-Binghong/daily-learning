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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPLCKL4J%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIBzMeSj5ILXLDaspeDkzsl4LE3uJJLQsyEKNWOc29KieAiEAuKm25joyTqFzwvCF5EsemvmG8eoaorK%2B5AY8RCnvqCYqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKb4TJ2EzjdISYpszSrcA21SauYcRISrHZAD3MGILMEqjzbX4q6LiXp0pGvwJNPvH3OC7JWhC3rSqwQaJSRx6nIQ8p%2BrqL6naiYDcnCCynzn8FAvar4OIrEQ%2BVplhWzMlTgDFAm9HkhRG9VkWtdx2KR%2Fh3oKfojfRbLtmuXpKoIc5SHSHeKs0KMP3BcR0TVAV5Ai8W6dJn6jq9lo1ak9lhJUyQRxJF6FjSfOC4lRJZgMqGSIvJOwFx16KC34ajaOn5z3OxRum03%2FE3i9wKikH6zqDp7H9Wh86zJL9Ka5%2BX1MNhyYCFwuk%2By6q%2FF4sV4UevXyU6RzonlBMEZzwUYxaaOSsxu0eZY4dUy%2FZYZEa0Nfr5dAD7xNnZNHyqxgIPslD%2BZYZqELcrPcIEdKsJrX6shGT6rEqMgYST31TU%2B%2Bxua6DKSrz%2FF940oPSvHDC1BDV3eZGyjkXEjhXFoqdp0o9AHE0%2BJQVgx%2BXYgZTnScDwQTRDi874nFmk2Bmtgyi9Z2ftgEx10Ru%2F9EVKmG4Iz0zxDDGIDydNYea%2BfjzLde7N8oxZLUpF1ZSFVsovKguHLLXprxYAP9Co76Jc53NBaaukXynvF5IfW%2B%2Fr4ydQ%2Bh87L7fXeZLpdOsobpRPx0r%2FK0aWHt7OlblxmBM87QMPHA3c0GOqUBBN2YjH2YV8wsh6OzK3JZE6a2w6XfbjpGkkcN7XTAkg8Jsqf3pjJMrgD%2BDXJmwY06HDrryu20hc332ivReafRDxP6kyJfnie2ezpBCfUKsT9fjiYYg80vQ46QCLpkp5ilJTp3vjsV6XYqt0JK6znw5n8bXoT4cxJ5OM%2BZhJtfec8cdr8Y4AgMjNbxHGLP1MKhjIHZhLkFNkIKPQgKWMNTc0YQusP2&X-Amz-Signature=03c4cb9d61faf3b1ea98ac2a4494b0d8331176fc25abc4c4ec1d8d57d9338a6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPLCKL4J%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIBzMeSj5ILXLDaspeDkzsl4LE3uJJLQsyEKNWOc29KieAiEAuKm25joyTqFzwvCF5EsemvmG8eoaorK%2B5AY8RCnvqCYqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKb4TJ2EzjdISYpszSrcA21SauYcRISrHZAD3MGILMEqjzbX4q6LiXp0pGvwJNPvH3OC7JWhC3rSqwQaJSRx6nIQ8p%2BrqL6naiYDcnCCynzn8FAvar4OIrEQ%2BVplhWzMlTgDFAm9HkhRG9VkWtdx2KR%2Fh3oKfojfRbLtmuXpKoIc5SHSHeKs0KMP3BcR0TVAV5Ai8W6dJn6jq9lo1ak9lhJUyQRxJF6FjSfOC4lRJZgMqGSIvJOwFx16KC34ajaOn5z3OxRum03%2FE3i9wKikH6zqDp7H9Wh86zJL9Ka5%2BX1MNhyYCFwuk%2By6q%2FF4sV4UevXyU6RzonlBMEZzwUYxaaOSsxu0eZY4dUy%2FZYZEa0Nfr5dAD7xNnZNHyqxgIPslD%2BZYZqELcrPcIEdKsJrX6shGT6rEqMgYST31TU%2B%2Bxua6DKSrz%2FF940oPSvHDC1BDV3eZGyjkXEjhXFoqdp0o9AHE0%2BJQVgx%2BXYgZTnScDwQTRDi874nFmk2Bmtgyi9Z2ftgEx10Ru%2F9EVKmG4Iz0zxDDGIDydNYea%2BfjzLde7N8oxZLUpF1ZSFVsovKguHLLXprxYAP9Co76Jc53NBaaukXynvF5IfW%2B%2Fr4ydQ%2Bh87L7fXeZLpdOsobpRPx0r%2FK0aWHt7OlblxmBM87QMPHA3c0GOqUBBN2YjH2YV8wsh6OzK3JZE6a2w6XfbjpGkkcN7XTAkg8Jsqf3pjJMrgD%2BDXJmwY06HDrryu20hc332ivReafRDxP6kyJfnie2ezpBCfUKsT9fjiYYg80vQ46QCLpkp5ilJTp3vjsV6XYqt0JK6znw5n8bXoT4cxJ5OM%2BZhJtfec8cdr8Y4AgMjNbxHGLP1MKhjIHZhLkFNkIKPQgKWMNTc0YQusP2&X-Amz-Signature=c70393b1cc25510fab4193d54d925bebbfef038a424cc95e9543a9e5dde65c0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

