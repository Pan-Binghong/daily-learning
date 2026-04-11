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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGXCOUDW%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T034029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIEkz5%2FJjRkgQ3vmHAHgs0G7VDOn%2ByWt4TxZG25RRFWh4AiA8ZJXa6NEZ2Q4kXteBv6sXpyM65XkcX8LJSQxpilRo9Cr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMNiGW0VwlpxWVO4%2FmKtwDik1gWjNbzA1HM8kO6N1zMGQxZX60kTq7PSiQVQA1duPkmbfBD5MdKP5LMDZL5okNw3XXcn4Pe3RAqlId7o0ppduz%2FVjiNhB6jTAGO2SS7kUqHm1vMcLQfQ%2BO%2B5Zb479ROT1o%2F9UxPKkdrE5y336cBTHL6sF%2F3SdiD87o7lZXKN%2FJ%2BSN58GgTiQJ7MpcIgQZu3VjeCqdnlnS0JUogBOKVLExQSVlvWSyzbfDKcSuaUdi93V5Qwyp%2BrLUTIR3l5K0a1wb2ThQGjkLhzwPMdxjiIE0F9PRH5NyilmUk5sj1EHeT35S1Z811ApuqSWMGiNoNHQVcFNPAg7If2Qq7CnNkYXMkQvLSXpHar%2FeucZ5C2MNw1yUZzIittJeGsK%2By9wy7qZYaFyrtNjKm4IBr3ZmdfUyLpwVIAwGyLghUSURbUEh98cNHoh4idsQp5KvXXXIrr%2FPjnhZ6GW7MiOrsdk2%2FH0VHVNdGxLZ%2BlCeKO%2By%2F20CQHfrHepAicr%2BT31w8mzKKLEEv3Sec1UbiU%2BZ9rYiB1AYULBEDudyZiHNDeq7ILCg%2FrPJKliLt6Jti8G19JOBHnkyFnKG9q3QJl5%2B77N3fAPBqxYC0AvpLUTquzQM2W70UfgppmldxRKtZM9MwgOrmzgY6pgHkHQ1PjC1Bi3fS6ycWT5nw1ySRZcla1gZmstTml%2FCT44IYqTTejGBv4Ua0SV1vcHwNGkor9diFkwiGQa%2BkTKq%2FB4G%2F0tMFyjn0AbYpMA7a3AKs32GmuSV1oQzrU8h47K9Va5ttWa8hdGzsF0Y0%2F%2Fut0eJXaxJImLGTrnhaBMNAcuQ9e5zhL89xhgHmV3w%2BZwmi8XxLSjpFFyThtuEqZEDIwOiF3lI5&X-Amz-Signature=2304f6293ff8deab617e02258f3ba25150d7af265ba5b6572e48b607904bc8e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGXCOUDW%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T034029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIEkz5%2FJjRkgQ3vmHAHgs0G7VDOn%2ByWt4TxZG25RRFWh4AiA8ZJXa6NEZ2Q4kXteBv6sXpyM65XkcX8LJSQxpilRo9Cr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMNiGW0VwlpxWVO4%2FmKtwDik1gWjNbzA1HM8kO6N1zMGQxZX60kTq7PSiQVQA1duPkmbfBD5MdKP5LMDZL5okNw3XXcn4Pe3RAqlId7o0ppduz%2FVjiNhB6jTAGO2SS7kUqHm1vMcLQfQ%2BO%2B5Zb479ROT1o%2F9UxPKkdrE5y336cBTHL6sF%2F3SdiD87o7lZXKN%2FJ%2BSN58GgTiQJ7MpcIgQZu3VjeCqdnlnS0JUogBOKVLExQSVlvWSyzbfDKcSuaUdi93V5Qwyp%2BrLUTIR3l5K0a1wb2ThQGjkLhzwPMdxjiIE0F9PRH5NyilmUk5sj1EHeT35S1Z811ApuqSWMGiNoNHQVcFNPAg7If2Qq7CnNkYXMkQvLSXpHar%2FeucZ5C2MNw1yUZzIittJeGsK%2By9wy7qZYaFyrtNjKm4IBr3ZmdfUyLpwVIAwGyLghUSURbUEh98cNHoh4idsQp5KvXXXIrr%2FPjnhZ6GW7MiOrsdk2%2FH0VHVNdGxLZ%2BlCeKO%2By%2F20CQHfrHepAicr%2BT31w8mzKKLEEv3Sec1UbiU%2BZ9rYiB1AYULBEDudyZiHNDeq7ILCg%2FrPJKliLt6Jti8G19JOBHnkyFnKG9q3QJl5%2B77N3fAPBqxYC0AvpLUTquzQM2W70UfgppmldxRKtZM9MwgOrmzgY6pgHkHQ1PjC1Bi3fS6ycWT5nw1ySRZcla1gZmstTml%2FCT44IYqTTejGBv4Ua0SV1vcHwNGkor9diFkwiGQa%2BkTKq%2FB4G%2F0tMFyjn0AbYpMA7a3AKs32GmuSV1oQzrU8h47K9Va5ttWa8hdGzsF0Y0%2F%2Fut0eJXaxJImLGTrnhaBMNAcuQ9e5zhL89xhgHmV3w%2BZwmi8XxLSjpFFyThtuEqZEDIwOiF3lI5&X-Amz-Signature=55ccd3b4cafb0b3982d942643918327c7451b1dade129c5b7ded3f24930c1f0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

