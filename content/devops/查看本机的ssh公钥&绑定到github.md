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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVTRSI4F%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd4s1tlzQfer1aWTvdr0y3Iit6AgrYlh1pSE%2BE3V1HpQIgVV%2BxMuOUx34mVddlE%2BcSAytkQjRjrqy1go9q7LUeHWYqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLvefMbblYR8EIC15ircAxJFZzkuMm4cj5bfhf7xHjcwnlPr9a7ZIXbRuQsAu6cJkFPITmbWTnnP%2FLSpf1rEP%2BZdHVr9Y2QC0O4OqhUoNIslbH5fOXipJRsf3hlSPKU1qlmzTTv7c2gXeDEWJiVT3lLw704Fj5dN%2FUN5MHY812d3D2989%2FqWdzS0ncEE0Y7baDi4vQ9I1DlCUz6ydPJ6hIZJO6lXIxd0fNFqCcYWLl9jGz6c9W8jsTPD1FEt6w7i3D%2B9bI9glFkDMa109n1fusPktSUZ3Ro9ap7Q6gyHfOCOE8NHvH3p39ReMWkjOXV%2FQdOkNHef8EjuLSaAboYKapHsS8%2FMEF9UXds2eNP8fMfeOHGNHt1LR4wkAJSuK0TnIlvHZuiPv86ASHrb3jHNMoLq8rVyDSg%2B%2BMuodlkYkehRin00O6ZlVEGAJfFZ%2F8vmTiaPN9LzXd3vkTYlnsrX3vtdylzc3Wj%2BDMcv2O3v86nsfxtk1TQaOA0g6w9%2BNFUc%2FRLXk0ZE0uanW4wpW%2F1XfxrTUngz5PPCOnTmC0B264wd7%2BP4J7VfNu0PlKtntvxpP4f38SWlnO8TbulytcStnisq34EOpqRuEFEDD2WiS9fflT8MSqWJ8U6ZZfia5xxwZtlm9R8w21IrFAywMMfJks4GOqUBzfJgNalXgDAvocFH0wd7wuab3eLGYGv8DqBK1eFR1MnQevXyw4Yl%2BIwtesdkBqfhL%2FEc7R7qwwA1T7GfK7vvCr5KggR4K41pDwKHPS7qIhwYvSCor4XI4F%2F2csw4U2v0jTUj1cf9wTSrMISu1mIM4LZOS4wu9loXKswId7eJja42i3MjeCwhg%2F%2BRGUAplz%2B8R0%2BvU%2BG5iJeW5999mWEIbVzLliz9&X-Amz-Signature=e0ccc9bcd42867eca89bbafec16675bd75d76a23840dcf28f56d0fb418818be7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVTRSI4F%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd4s1tlzQfer1aWTvdr0y3Iit6AgrYlh1pSE%2BE3V1HpQIgVV%2BxMuOUx34mVddlE%2BcSAytkQjRjrqy1go9q7LUeHWYqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLvefMbblYR8EIC15ircAxJFZzkuMm4cj5bfhf7xHjcwnlPr9a7ZIXbRuQsAu6cJkFPITmbWTnnP%2FLSpf1rEP%2BZdHVr9Y2QC0O4OqhUoNIslbH5fOXipJRsf3hlSPKU1qlmzTTv7c2gXeDEWJiVT3lLw704Fj5dN%2FUN5MHY812d3D2989%2FqWdzS0ncEE0Y7baDi4vQ9I1DlCUz6ydPJ6hIZJO6lXIxd0fNFqCcYWLl9jGz6c9W8jsTPD1FEt6w7i3D%2B9bI9glFkDMa109n1fusPktSUZ3Ro9ap7Q6gyHfOCOE8NHvH3p39ReMWkjOXV%2FQdOkNHef8EjuLSaAboYKapHsS8%2FMEF9UXds2eNP8fMfeOHGNHt1LR4wkAJSuK0TnIlvHZuiPv86ASHrb3jHNMoLq8rVyDSg%2B%2BMuodlkYkehRin00O6ZlVEGAJfFZ%2F8vmTiaPN9LzXd3vkTYlnsrX3vtdylzc3Wj%2BDMcv2O3v86nsfxtk1TQaOA0g6w9%2BNFUc%2FRLXk0ZE0uanW4wpW%2F1XfxrTUngz5PPCOnTmC0B264wd7%2BP4J7VfNu0PlKtntvxpP4f38SWlnO8TbulytcStnisq34EOpqRuEFEDD2WiS9fflT8MSqWJ8U6ZZfia5xxwZtlm9R8w21IrFAywMMfJks4GOqUBzfJgNalXgDAvocFH0wd7wuab3eLGYGv8DqBK1eFR1MnQevXyw4Yl%2BIwtesdkBqfhL%2FEc7R7qwwA1T7GfK7vvCr5KggR4K41pDwKHPS7qIhwYvSCor4XI4F%2F2csw4U2v0jTUj1cf9wTSrMISu1mIM4LZOS4wu9loXKswId7eJja42i3MjeCwhg%2F%2BRGUAplz%2B8R0%2BvU%2BG5iJeW5999mWEIbVzLliz9&X-Amz-Signature=8e4acadc2d083936927981be5bf2b12b7b5c79937312070532a48fad2a3c1c70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

