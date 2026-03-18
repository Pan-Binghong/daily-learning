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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RH4GW2R7%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIGq5Z3%2B3xyAkz%2BGre0tGqONXMWIk2qQC9j330Kds0m5kAiATNNQFf16RQMLM1sIfKf%2BIBxLjNMeLWWKBSE46cHZYyiqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMk%2FZVFC1ppfoDtznvKtwDLWgA1NwLIQHcwlszShZnpjdYOErHNAK97a9lVhfWPM4D8t5rw5e4w1RMH1buVMQvbghA6Lc9FE2zb5js4TlkQn8%2FOmeD1eFBtvR2mtik2IqcDHEKEutFUlpl247TJZS6PfJ7BZhzmPRTG0qulXrziBnPp8NFwqEg09l8cII19Jk6UIZtZ6ss4eR%2Bgga1%2F6cPirHxkRrKvPUx%2BDq328WbxnVsc126aAAwlZEWG94pXTEC4BB6FakeuudbYIVgLC%2FGhlQolVYqCnnDES3HviJnIipELCS88AA9aypqK1RzTwVcfOnw1hfr0LZErgcoLfJQy08zZVp6uh4BxE0RRmdea8z2NCz4SHih%2F3DSzsxz75tbx9fZBoM7EFV0TWO9m7rfI%2B4hY7Rxqfp8ltj8lTArs0O4IDfmhA7TTTI3k1RgYs27Jo%2By5BkUkhbi9Q3YaMqo7igbICcQftdUymBfoN88RYh3nkzmSzQj1Hm3kpisMSGZUWD9QhkE4%2FkrhIYvV1MiL7Ib3tNzF1bjPMWltnnqvEB9EHgR5Bb89UQA47BmQe1EVhYNC097mg4dlKuxldSfv7wlS1wiBZHUcztvgPXu9C9nUzpq2xSa87AKavwmrtBlC8O8o%2BpGDCeMVc4wz6bozQY6pgEvUIPmq9x2h3QqVaV3wzXgv80xiS%2Fw9agBdfhtcausBzhQjPKIC%2BmZiEXJX46UkcxjJs8TmbuyN0Bn6Y%2F4CJC4Dvl570Vqhzjw9giwQknouIqH3BdY%2F0lgU3kEUN4rx%2BPPXnXZufp6tPUZN2PnzM9jkKA1PwE%2Bsq7TDjW%2Fk4YmwohA7P3g9nxkd6mYUFxwF55jL9C2UoGyP5ADqWixT%2BlX3Uov8C%2F0&X-Amz-Signature=753295acec4bd9c961129cfe6bec26a46b82aa4175a27d8632370842ca82440d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RH4GW2R7%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIGq5Z3%2B3xyAkz%2BGre0tGqONXMWIk2qQC9j330Kds0m5kAiATNNQFf16RQMLM1sIfKf%2BIBxLjNMeLWWKBSE46cHZYyiqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMk%2FZVFC1ppfoDtznvKtwDLWgA1NwLIQHcwlszShZnpjdYOErHNAK97a9lVhfWPM4D8t5rw5e4w1RMH1buVMQvbghA6Lc9FE2zb5js4TlkQn8%2FOmeD1eFBtvR2mtik2IqcDHEKEutFUlpl247TJZS6PfJ7BZhzmPRTG0qulXrziBnPp8NFwqEg09l8cII19Jk6UIZtZ6ss4eR%2Bgga1%2F6cPirHxkRrKvPUx%2BDq328WbxnVsc126aAAwlZEWG94pXTEC4BB6FakeuudbYIVgLC%2FGhlQolVYqCnnDES3HviJnIipELCS88AA9aypqK1RzTwVcfOnw1hfr0LZErgcoLfJQy08zZVp6uh4BxE0RRmdea8z2NCz4SHih%2F3DSzsxz75tbx9fZBoM7EFV0TWO9m7rfI%2B4hY7Rxqfp8ltj8lTArs0O4IDfmhA7TTTI3k1RgYs27Jo%2By5BkUkhbi9Q3YaMqo7igbICcQftdUymBfoN88RYh3nkzmSzQj1Hm3kpisMSGZUWD9QhkE4%2FkrhIYvV1MiL7Ib3tNzF1bjPMWltnnqvEB9EHgR5Bb89UQA47BmQe1EVhYNC097mg4dlKuxldSfv7wlS1wiBZHUcztvgPXu9C9nUzpq2xSa87AKavwmrtBlC8O8o%2BpGDCeMVc4wz6bozQY6pgEvUIPmq9x2h3QqVaV3wzXgv80xiS%2Fw9agBdfhtcausBzhQjPKIC%2BmZiEXJX46UkcxjJs8TmbuyN0Bn6Y%2F4CJC4Dvl570Vqhzjw9giwQknouIqH3BdY%2F0lgU3kEUN4rx%2BPPXnXZufp6tPUZN2PnzM9jkKA1PwE%2Bsq7TDjW%2Fk4YmwohA7P3g9nxkd6mYUFxwF55jL9C2UoGyP5ADqWixT%2BlX3Uov8C%2F0&X-Amz-Signature=4eb71ca974649a18c793eb212d4f591eacad09a1be6ab484d31df0d2770a1bce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

