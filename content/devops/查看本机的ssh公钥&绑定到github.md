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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645TJ57QX%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQD7XM8kGohBK2NXJqOk%2F5H9NVnqp6ibSM7uYYfSjdX0wgIgDV%2B7ZD%2F33WbSmhQk%2BXof2K5UbWvT8yZwzGZZvL%2BNhOcq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDJsIykHrP2jYBczi%2FircA3MEd%2BjoB6QvuXQiBD6z%2BdEuTERELD8eATkThf2n%2Bw0alK9b8mIQUorTtE0Z0iqbnNgcqMZn3inW94GxYQGgRE7J4sh3IcRFFMWnCRqXGIAbkKXwyq6Nx%2B2aD%2FS%2BgbFqqhPyOx2o5S%2Fm4SAHFKU8lKFf5bY4g4Cr6Yga3QNyv0YzowDfyQ7tSr0wsOyLlDIfa2B852zexn9JyFEysLOO6V7y8WD3cakknxZIppIBKvMYtHL7rBT1aedBViFmXUlFik9xYuSmIirqxUA%2F4RJ8lLQKk8IhzswMKD%2FYiUaHJtFrkYJhqaXyqzan%2BEtxb0Tse%2Fm7hMTNJPZLjCqEU6sLCGudKIKAWOcZfYOyMXn2hngnwXvFcID1XslOZFM6lSue5x72crSiBbxyvNVMwYpJFCEXVhND4EDiZYRG51BP8PHJJl5IBurWYg%2FvIpj%2BBZzkntT3OoQyYpFILmRWDLPxySx2u5udzqeRG7wHuiMG1IwUCnYdbiMEX1IOWYEoGbYEokIg4635hXluUW0HsuP%2FUW8iCF7fQC6Ouxcw%2FL%2Bje8V4%2BbXktYta3Wthi4GpPhkBCL0QZZUrV7N47%2FX85CFIiRkn9RFL4aKtF6XbJGVCORh4sSwGdP0Zry5P8wmMMP%2B38s0GOqUBk84qfydcHa8VgLp3JrSDmya4f4uUaZKLVMSG9t90iNhyvO1Q6%2BlGc7rxbjAT1zZMo54Yxc%2Fr1Q1klSDloDmCJlBsN6S1Vma85gDvZTeAKbdvwfWMxiE6HAy52YpQh4FPtKSnp7buq69lxv4yJqZ48cYfo5spNmyjgZhfvyC0ggT9Vnc%2BeOOVGugdeyzJIm92bCQB1W8tjrKls6jgyxbMHKus6b5J&X-Amz-Signature=8fab2e037c8b155f44438777603db7421093a37f138e80825130842e52f42d58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645TJ57QX%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQD7XM8kGohBK2NXJqOk%2F5H9NVnqp6ibSM7uYYfSjdX0wgIgDV%2B7ZD%2F33WbSmhQk%2BXof2K5UbWvT8yZwzGZZvL%2BNhOcq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDJsIykHrP2jYBczi%2FircA3MEd%2BjoB6QvuXQiBD6z%2BdEuTERELD8eATkThf2n%2Bw0alK9b8mIQUorTtE0Z0iqbnNgcqMZn3inW94GxYQGgRE7J4sh3IcRFFMWnCRqXGIAbkKXwyq6Nx%2B2aD%2FS%2BgbFqqhPyOx2o5S%2Fm4SAHFKU8lKFf5bY4g4Cr6Yga3QNyv0YzowDfyQ7tSr0wsOyLlDIfa2B852zexn9JyFEysLOO6V7y8WD3cakknxZIppIBKvMYtHL7rBT1aedBViFmXUlFik9xYuSmIirqxUA%2F4RJ8lLQKk8IhzswMKD%2FYiUaHJtFrkYJhqaXyqzan%2BEtxb0Tse%2Fm7hMTNJPZLjCqEU6sLCGudKIKAWOcZfYOyMXn2hngnwXvFcID1XslOZFM6lSue5x72crSiBbxyvNVMwYpJFCEXVhND4EDiZYRG51BP8PHJJl5IBurWYg%2FvIpj%2BBZzkntT3OoQyYpFILmRWDLPxySx2u5udzqeRG7wHuiMG1IwUCnYdbiMEX1IOWYEoGbYEokIg4635hXluUW0HsuP%2FUW8iCF7fQC6Ouxcw%2FL%2Bje8V4%2BbXktYta3Wthi4GpPhkBCL0QZZUrV7N47%2FX85CFIiRkn9RFL4aKtF6XbJGVCORh4sSwGdP0Zry5P8wmMMP%2B38s0GOqUBk84qfydcHa8VgLp3JrSDmya4f4uUaZKLVMSG9t90iNhyvO1Q6%2BlGc7rxbjAT1zZMo54Yxc%2Fr1Q1klSDloDmCJlBsN6S1Vma85gDvZTeAKbdvwfWMxiE6HAy52YpQh4FPtKSnp7buq69lxv4yJqZ48cYfo5spNmyjgZhfvyC0ggT9Vnc%2BeOOVGugdeyzJIm92bCQB1W8tjrKls6jgyxbMHKus6b5J&X-Amz-Signature=6fbdd92123aa48733bab638c762ea6895e00b1362c22b4df0c661ae95b300301&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

