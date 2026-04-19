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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666G55OXPL%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCoAziOLAaA2nGrHmqG%2FchYEjs9%2BRKqAihQgleW%2FH%2B9lgIgMwjt%2B%2FDi2amvVCYhozWm9b1SgbvYJMlSDBa9UHqJ3mwqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDgaJGNaR65tkuGteircA5MVOLWZqLYZZdCG2eWt9E574UVGVZ7Sp3jq9vOQGKftprcAZ90%2FsebjTQvBnxsfA1G%2FE%2BP4Ne%2FQNYAuQL1WmjraOEPZ2a5xXa8iKYn6z69WJIVmw6Lb88srnVCx2sjNHuEiBlUm%2FVtdf2eGQuWdHfFMTvTlfLmjuveplLIOnvOcHSGEgVAblahnEVYUCcNDTRRK8jDRmpvz5wgEYg7DF7OgWTk9lBa6AJQaXJI%2FLZn%2BtutElm4wQfCJp5Y9e%2B62rWSZnIDt0XyRhWLkonVZpZmGAGj6PiLGzIP3YyXAWMG24Abfe7vqJlYd8PxxiozjGhPWomzukj9fRkOnhOSLF%2FpV8SYlCrcHopAiVaEHX8QACQxeUWErR1HwOUBi7ShuZksam9z1v6Zf8b733u8ZJTaRmuwj9jGuhUWdgn0syNCcuKrCVDATUaM3r%2F3qUGA%2FuJXGIWlUnZntTPPQ6cIZIxIZJljMZEGpPSBX8GQJRRpm5TRCuUOXkmBrcZn7xJOVUb9Ehwanu18eyh2uvd2IHRMcgTVpznpwHYVoJw1HeEqi8wDmceeHb71RzQqUxbAcSt8kV2oLO6q348vltrLocbAvX%2F%2FJePEKtmcXSgXvAR75a2vxxKN6mLqxOGnxMLndkM8GOqUB%2B1CbL8b0jkYtweoY0EJnKwRWugvsWbNyzqA%2BVzgTtUKsxb8VQJ2LNffwYuOePs5KP1NwC8MS8kYvZ%2FBkUpnAR0d1sHcc9HjtteSw69Cz4BXOMzK%2FgBzf9N4zlFkgu5LTkdnLaq6Sl4NIKomNtsy7gUtPCuR3KoCgPLMLOe43hcy81q0i6Fq61oyWdWV0Ve8hA89EFvpHfHw65BBZTx1W8uxF87s3&X-Amz-Signature=cc1acfadb4b883bb9fc9d22c3326a311915b0150174501d33b533b90e289583f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666G55OXPL%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCoAziOLAaA2nGrHmqG%2FchYEjs9%2BRKqAihQgleW%2FH%2B9lgIgMwjt%2B%2FDi2amvVCYhozWm9b1SgbvYJMlSDBa9UHqJ3mwqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDgaJGNaR65tkuGteircA5MVOLWZqLYZZdCG2eWt9E574UVGVZ7Sp3jq9vOQGKftprcAZ90%2FsebjTQvBnxsfA1G%2FE%2BP4Ne%2FQNYAuQL1WmjraOEPZ2a5xXa8iKYn6z69WJIVmw6Lb88srnVCx2sjNHuEiBlUm%2FVtdf2eGQuWdHfFMTvTlfLmjuveplLIOnvOcHSGEgVAblahnEVYUCcNDTRRK8jDRmpvz5wgEYg7DF7OgWTk9lBa6AJQaXJI%2FLZn%2BtutElm4wQfCJp5Y9e%2B62rWSZnIDt0XyRhWLkonVZpZmGAGj6PiLGzIP3YyXAWMG24Abfe7vqJlYd8PxxiozjGhPWomzukj9fRkOnhOSLF%2FpV8SYlCrcHopAiVaEHX8QACQxeUWErR1HwOUBi7ShuZksam9z1v6Zf8b733u8ZJTaRmuwj9jGuhUWdgn0syNCcuKrCVDATUaM3r%2F3qUGA%2FuJXGIWlUnZntTPPQ6cIZIxIZJljMZEGpPSBX8GQJRRpm5TRCuUOXkmBrcZn7xJOVUb9Ehwanu18eyh2uvd2IHRMcgTVpznpwHYVoJw1HeEqi8wDmceeHb71RzQqUxbAcSt8kV2oLO6q348vltrLocbAvX%2F%2FJePEKtmcXSgXvAR75a2vxxKN6mLqxOGnxMLndkM8GOqUB%2B1CbL8b0jkYtweoY0EJnKwRWugvsWbNyzqA%2BVzgTtUKsxb8VQJ2LNffwYuOePs5KP1NwC8MS8kYvZ%2FBkUpnAR0d1sHcc9HjtteSw69Cz4BXOMzK%2FgBzf9N4zlFkgu5LTkdnLaq6Sl4NIKomNtsy7gUtPCuR3KoCgPLMLOe43hcy81q0i6Fq61oyWdWV0Ve8hA89EFvpHfHw65BBZTx1W8uxF87s3&X-Amz-Signature=c3044b83484edf1fa528e3321f8e544489599ad463464b795517026af424cd6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

