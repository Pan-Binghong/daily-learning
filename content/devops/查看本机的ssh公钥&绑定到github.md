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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKDLOIKX%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeC34PYjX12BMjRXlvh8Fq40mkXZwCpf7a5FKWp5IVtAIhAICawlzW7cr42ep6lT%2F8gsdJbwT9y5cxjYpAJD46urc0KogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxiYT4jJ3QfG0HRx7wq3APpk1ixn%2ByFEFOX3XwOhqjlsMHjrdrieAjyVX5rfnrdEvets9%2BlAs8yC0XF0%2BHTaJAHuJqnjJvWEZalDnkJgdnNv%2FYgJIvJrGAHAeQqafQv6z1I%2F%2FB%2F%2BOaPmPrhDrNtc5vpRVUNYdMTXbRtxk57YCZdIX1%2FWyjbOXmhbZ9%2BKMHdC9bHeH06RH%2BwAX6xuSxzKgJdjSx3YOtYY%2FpDAUMlxMD1D29HDWOEspFQsPglisqcz4%2FkpK0JTSYUhwAMHb%2BXiLBt0b6lTO3zAsfGcVspklRy7QGh8qP%2BOtjXw9c8i3AVBjOVStH8D8HyoXwOMXPxldFllUP0XB951Ix7QBzCnoW95XqaWAeC1itI8%2BaDl3%2Bh51hZA9HhrFrhoGMoFIbhW3s6Y2J3utKlPwAyOnDSchBIsyLxvzTgxEk8pnXLkGHLmFFQsyaK91DTi6phiSJlm3BGnQ8HFzGBu8mIkEoG6BW8s5c%2FKQs7h%2Fji4vb31UFHRTo0sE2misNx0bBjdQi79Pf8VbKcxmBtqIKf0%2BLwe9ngC1Jrz3WFyOjQwoWxJatLYmar9ENjwwWMwieG2qCftNWYj%2F2mvCFzp6aI%2FdVqXK5kBORcNSZU7alW74PQVY%2Fhkv%2BZFMEwvPeJnkyfTjD2kNjNBjqkAU4ZYmAJuMQDghAPVYQP%2B2mzzQhX9srj6P6BWo8ohTsKx87pkC1rO%2FbAfTNDjtH18t5Zv5gGBpbQrXR%2FgAIW9nhlfQ5I9wpX9NCTDYqEGcvI9EGOhZ297msPCVk6R4Xj7i9UqrU1hbC6%2Fgo1hV%2FyUnJa8ysLhnS4bvdjQq904FoOCJlPrQq7UE6kWU1GRQif9TbhaklYKffQZnRtCli8aHz2Pk1V&X-Amz-Signature=8844af57946758442989ecf448d12397a6604785007b1a783a90cbabe7c91dd1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKDLOIKX%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeC34PYjX12BMjRXlvh8Fq40mkXZwCpf7a5FKWp5IVtAIhAICawlzW7cr42ep6lT%2F8gsdJbwT9y5cxjYpAJD46urc0KogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxiYT4jJ3QfG0HRx7wq3APpk1ixn%2ByFEFOX3XwOhqjlsMHjrdrieAjyVX5rfnrdEvets9%2BlAs8yC0XF0%2BHTaJAHuJqnjJvWEZalDnkJgdnNv%2FYgJIvJrGAHAeQqafQv6z1I%2F%2FB%2F%2BOaPmPrhDrNtc5vpRVUNYdMTXbRtxk57YCZdIX1%2FWyjbOXmhbZ9%2BKMHdC9bHeH06RH%2BwAX6xuSxzKgJdjSx3YOtYY%2FpDAUMlxMD1D29HDWOEspFQsPglisqcz4%2FkpK0JTSYUhwAMHb%2BXiLBt0b6lTO3zAsfGcVspklRy7QGh8qP%2BOtjXw9c8i3AVBjOVStH8D8HyoXwOMXPxldFllUP0XB951Ix7QBzCnoW95XqaWAeC1itI8%2BaDl3%2Bh51hZA9HhrFrhoGMoFIbhW3s6Y2J3utKlPwAyOnDSchBIsyLxvzTgxEk8pnXLkGHLmFFQsyaK91DTi6phiSJlm3BGnQ8HFzGBu8mIkEoG6BW8s5c%2FKQs7h%2Fji4vb31UFHRTo0sE2misNx0bBjdQi79Pf8VbKcxmBtqIKf0%2BLwe9ngC1Jrz3WFyOjQwoWxJatLYmar9ENjwwWMwieG2qCftNWYj%2F2mvCFzp6aI%2FdVqXK5kBORcNSZU7alW74PQVY%2Fhkv%2BZFMEwvPeJnkyfTjD2kNjNBjqkAU4ZYmAJuMQDghAPVYQP%2B2mzzQhX9srj6P6BWo8ohTsKx87pkC1rO%2FbAfTNDjtH18t5Zv5gGBpbQrXR%2FgAIW9nhlfQ5I9wpX9NCTDYqEGcvI9EGOhZ297msPCVk6R4Xj7i9UqrU1hbC6%2Fgo1hV%2FyUnJa8ysLhnS4bvdjQq904FoOCJlPrQq7UE6kWU1GRQif9TbhaklYKffQZnRtCli8aHz2Pk1V&X-Amz-Signature=2a9527532ba06312672ea3fa98066e93980263744f3eadb1259e1e4de103f57d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

