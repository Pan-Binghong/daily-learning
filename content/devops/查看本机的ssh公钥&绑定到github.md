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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652Y4UJGG%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T041111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIAzorYtteNbjCjwOBC7I33Gksd3p4I7hduxk4%2Bk%2Baiu%2FAiEAkWd6ypspxMVjGsaeqQ%2FOP9Snhi3da2RShU48QFk%2Fi%2BIq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDCz773Ejaf4BOPYxHircA1fBextilG4z5URRE5UOXadU9nRm7Z5%2BnQP4dnyIbp8GrpDLvKMDq3JmafbqEwqfwBS%2Bwl%2B2HdAJ2GZ5Xs6Mts1yFq8j42ISqP5r3vrx7A7godAbBHleFH76q5t5536hEGZhC9OGqav%2BDCF4sA2Sji5NtSf0boWAaHvoJxkIwDq9tDxmHnkUPhFgi7hIbA0pCpxmrcZCF4SXOZaUQF6psnkQ5X5e0oE4PtsWuChBHFbTbtMSH8iQ8KT9P20aj45ff8hSvkNCb7ny7lVY0xr258CJO1fGDcPqlnnPhUGW3WzbfFi4usu8TPs3EdfZSzO3rgTBcjK6mIOnGBGVZY2bovpdQ8Qn5nKb6%2Bf5R15fTh94p2mgShB6%2BbohZ%2BQQ1JwIh0vReIWvNNjiaUo0vek7tjDj9QaenWb4FM3K0VsbnPGLCKz24xnoR7Zj0sWjQjb5HzORTd86IJXp7O7qtAEnq1%2FPvNNkybPt22O6ETf3KFMQ16zV0BMGg2FMWV%2FvIpVOQuuZxxsyccXstijHUskttg6o1xU8ThiteTHUtNiGvmCF7CiVOcahVa38xTeLa8DWbXh0piS%2BdzY0tjiARnp%2BWYtUDmnN0z8iY0SZYQ6CoOoM7WKU%2BYPtiCsmb3lyMIjq4c4GOqUBmEHhqvo%2BvWaV9H49Rur3fZPEv%2Bi7TRGGEYcN2UkfC65Y6P34gaaCAVMYh9aYgdZ1FMuyzrFE4x3Xwhv1%2FmbIi0cOWkEIlD%2FqhWoFeRK04XCXBUMiToY1JOwXk%2B9TIAH%2FWZK76KEVAoAZUmCH71UCjzpqA3mwU0QdJnre1EKnzU4c3fRQ43fcWGh7rsDyM1FjQbGp%2BGhw5T4cqvprbTM6oIkBpuP8&X-Amz-Signature=cd770b34a1d3b7e55c4ea49decb256a6c4af34de7dbd72e3247d8096e4e47338&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652Y4UJGG%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T041111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIAzorYtteNbjCjwOBC7I33Gksd3p4I7hduxk4%2Bk%2Baiu%2FAiEAkWd6ypspxMVjGsaeqQ%2FOP9Snhi3da2RShU48QFk%2Fi%2BIq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDCz773Ejaf4BOPYxHircA1fBextilG4z5URRE5UOXadU9nRm7Z5%2BnQP4dnyIbp8GrpDLvKMDq3JmafbqEwqfwBS%2Bwl%2B2HdAJ2GZ5Xs6Mts1yFq8j42ISqP5r3vrx7A7godAbBHleFH76q5t5536hEGZhC9OGqav%2BDCF4sA2Sji5NtSf0boWAaHvoJxkIwDq9tDxmHnkUPhFgi7hIbA0pCpxmrcZCF4SXOZaUQF6psnkQ5X5e0oE4PtsWuChBHFbTbtMSH8iQ8KT9P20aj45ff8hSvkNCb7ny7lVY0xr258CJO1fGDcPqlnnPhUGW3WzbfFi4usu8TPs3EdfZSzO3rgTBcjK6mIOnGBGVZY2bovpdQ8Qn5nKb6%2Bf5R15fTh94p2mgShB6%2BbohZ%2BQQ1JwIh0vReIWvNNjiaUo0vek7tjDj9QaenWb4FM3K0VsbnPGLCKz24xnoR7Zj0sWjQjb5HzORTd86IJXp7O7qtAEnq1%2FPvNNkybPt22O6ETf3KFMQ16zV0BMGg2FMWV%2FvIpVOQuuZxxsyccXstijHUskttg6o1xU8ThiteTHUtNiGvmCF7CiVOcahVa38xTeLa8DWbXh0piS%2BdzY0tjiARnp%2BWYtUDmnN0z8iY0SZYQ6CoOoM7WKU%2BYPtiCsmb3lyMIjq4c4GOqUBmEHhqvo%2BvWaV9H49Rur3fZPEv%2Bi7TRGGEYcN2UkfC65Y6P34gaaCAVMYh9aYgdZ1FMuyzrFE4x3Xwhv1%2FmbIi0cOWkEIlD%2FqhWoFeRK04XCXBUMiToY1JOwXk%2B9TIAH%2FWZK76KEVAoAZUmCH71UCjzpqA3mwU0QdJnre1EKnzU4c3fRQ43fcWGh7rsDyM1FjQbGp%2BGhw5T4cqvprbTM6oIkBpuP8&X-Amz-Signature=dcc245b9ada1524f376a05070d12b70e2b16723c8020c6aac88cd4cc86a9c2f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

