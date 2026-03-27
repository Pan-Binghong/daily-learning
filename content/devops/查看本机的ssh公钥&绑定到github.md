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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7B5UHZE%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCZeJpoGV8VfQKQFReDX3d6fwsenXcunYydHfZpn7JyvgIhAKYkg68mda5PXzVsrejwu2wcAkcU3DdefSlDNt1ByvUsKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBUbS62rrh5kLiSM0q3ANQYRhMSn8U8B8ipHF8eb38bBxXpafMafL6QIVhKHXJMShK0vX1Elw0Rm9R1494tx29TJo5qztkbgWFdQcvFZ8OmY%2BoRbkZvFR5oe48ovHHl3A6WjIq63%2Bo%2FdW19I%2FJSIyyr2SOSo%2BqHf3cx1kV%2F3X8ewzu8uUp%2FbC3e3s6xxRqQTBkDvOXHAXQqkDP0293ikRxndyTOQwOWHxQ5ksoNQMTGgHdna0IuuxYq8sHLmbEPusgoYtA90aH%2BmMmqoH1TJmk9ayFzmMPj005sosO8BpUBL7R0a0v2Ls1OiGn54hD06jdYSExf1kVa%2B%2Be8pxv9gdk3gSQ5dc3ciX%2Fi9TWMWPRr0VL3zZ0CWTIsKMWVyb74A7p1PdheZ1paJXccMc13Hru72U0q0sdVZLTveZ6yLm18IRdnL4AEFt0ZJ98MeWLVFX3DK99d0CM8XrMncMSGynhTcDKT3hID4Nsf6htCP9nXjyGokIvTNWcLS7Ns9c0BQwSHeq68bejtfKQxvQCzKpOgLGvDfql5T9JIYCRkxK7MsFX3vgZ37%2FgkzARgakCtqwzgWkL%2Bi0xROzGVjuA%2FaD68AHEgTtvFn4vv66RlbMjP8hGi4jlSv0MBO0hlrHqcHEiGxDS7yVBHMyCTjC69JbOBjqkATGhDCDLHm43NqEykJ9LXFEMqEvmfwW7a1xYitNAUEntkk4L0RFCG15wwsAcCzEk5zACAIxuwlGR7tOj2tz3FuJLmuKORZ2NHl2pKIptgnXngae8d9T%2FPe%2BK4ckkK9jjzH7c9eYEZ0Bv%2BZlS9IfbgpTzM5nlZP2gSQIujQrAsYbNjt7nQJ4lFZ0Dp53aW6XqZthQJZWC1gwu1R8GIOTthhLEPE33&X-Amz-Signature=bebfb1e9674f55e6622c4791199b2b7f62e0adacff66df7a9a0ef1210a3001ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7B5UHZE%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCZeJpoGV8VfQKQFReDX3d6fwsenXcunYydHfZpn7JyvgIhAKYkg68mda5PXzVsrejwu2wcAkcU3DdefSlDNt1ByvUsKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBUbS62rrh5kLiSM0q3ANQYRhMSn8U8B8ipHF8eb38bBxXpafMafL6QIVhKHXJMShK0vX1Elw0Rm9R1494tx29TJo5qztkbgWFdQcvFZ8OmY%2BoRbkZvFR5oe48ovHHl3A6WjIq63%2Bo%2FdW19I%2FJSIyyr2SOSo%2BqHf3cx1kV%2F3X8ewzu8uUp%2FbC3e3s6xxRqQTBkDvOXHAXQqkDP0293ikRxndyTOQwOWHxQ5ksoNQMTGgHdna0IuuxYq8sHLmbEPusgoYtA90aH%2BmMmqoH1TJmk9ayFzmMPj005sosO8BpUBL7R0a0v2Ls1OiGn54hD06jdYSExf1kVa%2B%2Be8pxv9gdk3gSQ5dc3ciX%2Fi9TWMWPRr0VL3zZ0CWTIsKMWVyb74A7p1PdheZ1paJXccMc13Hru72U0q0sdVZLTveZ6yLm18IRdnL4AEFt0ZJ98MeWLVFX3DK99d0CM8XrMncMSGynhTcDKT3hID4Nsf6htCP9nXjyGokIvTNWcLS7Ns9c0BQwSHeq68bejtfKQxvQCzKpOgLGvDfql5T9JIYCRkxK7MsFX3vgZ37%2FgkzARgakCtqwzgWkL%2Bi0xROzGVjuA%2FaD68AHEgTtvFn4vv66RlbMjP8hGi4jlSv0MBO0hlrHqcHEiGxDS7yVBHMyCTjC69JbOBjqkATGhDCDLHm43NqEykJ9LXFEMqEvmfwW7a1xYitNAUEntkk4L0RFCG15wwsAcCzEk5zACAIxuwlGR7tOj2tz3FuJLmuKORZ2NHl2pKIptgnXngae8d9T%2FPe%2BK4ckkK9jjzH7c9eYEZ0Bv%2BZlS9IfbgpTzM5nlZP2gSQIujQrAsYbNjt7nQJ4lFZ0Dp53aW6XqZthQJZWC1gwu1R8GIOTthhLEPE33&X-Amz-Signature=55526e426419233237ccb961344d572c05a2f0f94f278aadc8d916c407854f49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

