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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXHZZEFL%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIDYhxnWAHYSIMg43M4r1bQcYrTcxVbJm4oUdUWWSzJsWAiABDcZ9AwQT9TAVdb%2Fvs1JB5WPTZ2l0sNJcHAjh8cO1OiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbYYKb2%2FWSBPxHZvhKtwDxsRV4Yp9Qa%2BcJzkCeLsQdWNdpMAS5zw1abCFAQ7q5NgTqNEeoo9%2F6UJPO1dZysTR%2BQ3kOzmhzFEeZ6j2Zk2Wb6hpn%2Bd1lL2%2FNNy7dPk3a6Ia96bJnwyxrzQoO4N6ToZpTAEAqv7Sk0WauTbx%2ByOQuxDlS7hBcBxSAg4XNoqeWTZPz8ee3TLqcPgjv8luGQ8d5QZL6JQk3m4fa4srETBol76Yddw0gWVgKlDO9lonFs%2Fpg8J9cAlrKXJ8Rfu3FU%2BpwkqlPhcJOXQx9AHOxK7BtJRckyrc2lFXZOZ9iKFvzu8C2fh7ffR9u1YBceeU0fd79zcHlU4CaY8oGAnsnmHH8EQck6sB%2B2fyCc3ND4KR8TxZthJShGqlo6aV3Cf%2B8V05ZnVsA8b580%2FLYnE1qwWRIcNxf75wRF9xloJmOgZVKMEcWlgQlXMZEyRlMxv%2Fs%2BIFEmfjm9ZOP7UFzv5iCw0XXI9VzpUxCLvbXx3SG4oBWm4jFtvD0bymtP66eADc%2FHQraPPj9Sa9YxVXKDgkBMx9fW%2FeIMkcab7Z7KHflP8VbaebVk8FhWWDwm0Df%2FCnjm13QAQxwxDQ7Zr4Y%2FejWcgv78zAZjcp53z4ErVPzlmS5Speqt5LB71pP%2FhSBhMw8JSdzgY6pgFrgRDXdCxNOQX%2BHzCNxWLYe7yh8c1FbhSxF9lDdvqZdkq2Ci1oOEcc6QF9ctQhqJBo4UR6jTSR5ySrntId2lJoaSbbX3dnStPgFRu1oP%2FstN%2FitPZD4pAvAzO2rzeYyIm%2Fk6y7kyULkX1nMb7QEFP0wfXBLBsNwbAj9dJ%2ByvZzUkeNT2UzH4q8WZcnqnKCNJo4AntKW4s3Q1BmXrTDaDELCGzP3osw&X-Amz-Signature=95000222ef9fb6af204b4344ab101b51d100dc4c35d2c411e724a071d668d266&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXHZZEFL%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIDYhxnWAHYSIMg43M4r1bQcYrTcxVbJm4oUdUWWSzJsWAiABDcZ9AwQT9TAVdb%2Fvs1JB5WPTZ2l0sNJcHAjh8cO1OiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbYYKb2%2FWSBPxHZvhKtwDxsRV4Yp9Qa%2BcJzkCeLsQdWNdpMAS5zw1abCFAQ7q5NgTqNEeoo9%2F6UJPO1dZysTR%2BQ3kOzmhzFEeZ6j2Zk2Wb6hpn%2Bd1lL2%2FNNy7dPk3a6Ia96bJnwyxrzQoO4N6ToZpTAEAqv7Sk0WauTbx%2ByOQuxDlS7hBcBxSAg4XNoqeWTZPz8ee3TLqcPgjv8luGQ8d5QZL6JQk3m4fa4srETBol76Yddw0gWVgKlDO9lonFs%2Fpg8J9cAlrKXJ8Rfu3FU%2BpwkqlPhcJOXQx9AHOxK7BtJRckyrc2lFXZOZ9iKFvzu8C2fh7ffR9u1YBceeU0fd79zcHlU4CaY8oGAnsnmHH8EQck6sB%2B2fyCc3ND4KR8TxZthJShGqlo6aV3Cf%2B8V05ZnVsA8b580%2FLYnE1qwWRIcNxf75wRF9xloJmOgZVKMEcWlgQlXMZEyRlMxv%2Fs%2BIFEmfjm9ZOP7UFzv5iCw0XXI9VzpUxCLvbXx3SG4oBWm4jFtvD0bymtP66eADc%2FHQraPPj9Sa9YxVXKDgkBMx9fW%2FeIMkcab7Z7KHflP8VbaebVk8FhWWDwm0Df%2FCnjm13QAQxwxDQ7Zr4Y%2FejWcgv78zAZjcp53z4ErVPzlmS5Speqt5LB71pP%2FhSBhMw8JSdzgY6pgFrgRDXdCxNOQX%2BHzCNxWLYe7yh8c1FbhSxF9lDdvqZdkq2Ci1oOEcc6QF9ctQhqJBo4UR6jTSR5ySrntId2lJoaSbbX3dnStPgFRu1oP%2FstN%2FitPZD4pAvAzO2rzeYyIm%2Fk6y7kyULkX1nMb7QEFP0wfXBLBsNwbAj9dJ%2ByvZzUkeNT2UzH4q8WZcnqnKCNJo4AntKW4s3Q1BmXrTDaDELCGzP3osw&X-Amz-Signature=949f94520e151c9d98b3b2972082696cf3aa3f4ebcb1a7c22d7c297651286527&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

