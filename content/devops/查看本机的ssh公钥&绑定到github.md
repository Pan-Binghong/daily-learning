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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TWX74UN%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwyIR%2B47c1cZv20k5Dls9WrHed8gSEaAPwNJMf%2B35b7AiBZJwpXUN06XQyO8QUeO3xJlHrRBowGDHydaWpxvx5HmSr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIMZDRxCux0qh%2BtfG50KtwDPp9JCtLhd%2BQT1BxvQxHXBHpS7Bz47lMlWAiHfeKXFPgSBu%2BaCyevNgLzg2XacINrf4vT7Wdr5%2Fo8u%2Bgf45vQErHqm81b8yXz6fhBIz%2FgmH7kecEkOFV74NOSXBzaZvrGEefwdlz8UIfzED27kj8wOql82Ly9xkYlzlRIhmFtVLMwG9UI6FvkARtXhY7xSAaD54wvr5PNJyLmy0tw1uPgFDWGsQgW1u66fi7%2B1pbXF1k8noaXQSEX2FzP9dySvewhmiFgdzlCAxx1YpjmZCo408MmXv91Qv4XGpudjxGwBGBFIkJRKy%2FDEGycOTgurZxH%2BzkNSJVZatVmEJKVJFyTrHm0vEKlNLj4MQMVgVCg%2BLuXFrW1%2BiIKAqN8SYw8ikvU5TQCYnKXiMQqhnMtfs5iTj7ZglHG6r5rf%2BVIgOP5oXstE%2Fjj%2BKDH1J8JWCf%2BFUAigUkfRnibanYPiuWyJk2mgFDzT5BU4K%2Fip04yYnXSmqb8V%2B0kVSJuj764QjbKc7FHxe5d3BFBFsJq6Uqqej6AUcMVdJYza%2F7Xt594sfWl2LVa72pmXS%2Bvf9Jeoyt8LAEQe2LFkiH5uc%2ByVqE9rojkkOfW1DaBNyNtgqgnIyFSFvVzbZp71egd63YjqIYwjOSCzgY6pgEj11QB6RTtIonVVAw%2FVDNOq%2F%2BmEvvRw%2BbBc7o2MZe%2BW5J8HOWoOs8iR0OPXCb%2Bbk8e0%2BSkyeNP59I6CEJ54N4cQj2aIZkLkPWJl9UO%2FgWpTEK1Agh0yED%2BBOFE%2BDQcJpy0LsHeXZoYujfUzVAmInCXIQ0bSpNso6AMHXYgUcWt3tooj9BGYt0TrB6iWLkB6jHSyimvnhsGiZBMpJ1S6QkfX9wmJOnl&X-Amz-Signature=3b88e6a4294c81ed2fa51807e2cd1f509e5f90848b21a14a9cecb63aa317c4ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TWX74UN%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwyIR%2B47c1cZv20k5Dls9WrHed8gSEaAPwNJMf%2B35b7AiBZJwpXUN06XQyO8QUeO3xJlHrRBowGDHydaWpxvx5HmSr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIMZDRxCux0qh%2BtfG50KtwDPp9JCtLhd%2BQT1BxvQxHXBHpS7Bz47lMlWAiHfeKXFPgSBu%2BaCyevNgLzg2XacINrf4vT7Wdr5%2Fo8u%2Bgf45vQErHqm81b8yXz6fhBIz%2FgmH7kecEkOFV74NOSXBzaZvrGEefwdlz8UIfzED27kj8wOql82Ly9xkYlzlRIhmFtVLMwG9UI6FvkARtXhY7xSAaD54wvr5PNJyLmy0tw1uPgFDWGsQgW1u66fi7%2B1pbXF1k8noaXQSEX2FzP9dySvewhmiFgdzlCAxx1YpjmZCo408MmXv91Qv4XGpudjxGwBGBFIkJRKy%2FDEGycOTgurZxH%2BzkNSJVZatVmEJKVJFyTrHm0vEKlNLj4MQMVgVCg%2BLuXFrW1%2BiIKAqN8SYw8ikvU5TQCYnKXiMQqhnMtfs5iTj7ZglHG6r5rf%2BVIgOP5oXstE%2Fjj%2BKDH1J8JWCf%2BFUAigUkfRnibanYPiuWyJk2mgFDzT5BU4K%2Fip04yYnXSmqb8V%2B0kVSJuj764QjbKc7FHxe5d3BFBFsJq6Uqqej6AUcMVdJYza%2F7Xt594sfWl2LVa72pmXS%2Bvf9Jeoyt8LAEQe2LFkiH5uc%2ByVqE9rojkkOfW1DaBNyNtgqgnIyFSFvVzbZp71egd63YjqIYwjOSCzgY6pgEj11QB6RTtIonVVAw%2FVDNOq%2F%2BmEvvRw%2BbBc7o2MZe%2BW5J8HOWoOs8iR0OPXCb%2Bbk8e0%2BSkyeNP59I6CEJ54N4cQj2aIZkLkPWJl9UO%2FgWpTEK1Agh0yED%2BBOFE%2BDQcJpy0LsHeXZoYujfUzVAmInCXIQ0bSpNso6AMHXYgUcWt3tooj9BGYt0TrB6iWLkB6jHSyimvnhsGiZBMpJ1S6QkfX9wmJOnl&X-Amz-Signature=94833a253c5c414008831dbb8be470a7f3146496fcb9f3f96f907988b3497816&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

