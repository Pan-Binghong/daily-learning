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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667F6ONV6X%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIH8E9bsDCIPhX4bpWSP0Zks7w2r2b1vIlzTXvM7kew3YAiEAnzCBq9HlR0OStUZckh9lt6T%2Bd9wdlzJeo6d%2BniZ1scEq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDBcaZPOfdRM%2F3uElICrcA6BaZwTLotpaIX3sUxtNPqQsPRC9Q9MIp44SIs8Xj7ctqg9jcNZCEPMdcYjqEDQm9vhXOuxH3TOzs8Sadm%2BMRRkr9RnVZGX%2FgbA1dRTrOiA2w84dnuuWUNOVlv%2FF7xP8QeEstIies3i7o4hN%2BxR1TF%2FvBxceNxkH6g02CuwR7RFydr7eZLXE%2BY5i7or6Lbgv7EG1Stv9jq1YA1l1qKr%2FWUSbjZQBm2kDBHHhvjF%2F0ui4dRwXxzQco3QnG8%2BKxwE87aZsW4VtzcN1rER1HzFh7fTuw2iSohJbws9utIGgLKZRhMJ0ei3JQaf9ppx%2BPOXSq%2FdGtRVrdBpVLs2VmM8LlDxkOQv4jdvOjTqAH6GxwFaz3DERwZTKtill91wDbXsvIUWhqU%2BfNMD0rZVaBj9EDT%2BelS517nO2lYFmkt8%2BlMuwN0kC%2B63lhvGvMGOerDPieZR9SjIkvxVDk5mW5oIMT2otw9kRrwaaS4SJ8ppKS0zofMwgnlI9HVCRjkqtZPjVHHxE%2Fyf1Bo%2F4DtukMo%2B1s%2FpVAJsyvklmwerKRG1eWxULHTT%2FU%2FtdtH0tQ7JN4dNvgwsXmyrvm4z0tcE5vjLXN3ROsp48LZ4jF4GcVwTzopwVbfrekFtpFQ8ltF%2BrMOuO%2BM0GOqUB7Y%2BcyHo41wMoe5HZVgcKihnCxTd%2FbOwp4QmNZLNCfOZrpWyCPdml2N6QJ4jnhju%2BzYiEJg%2BFcaIEk5DBnRDOFyjyi8Msc8p7ELKTR%2Flg0gQWAZLfODDeh38AGQjFtBlJMTIgITz22CS%2B2mUTjUZdjqVvr6VklozIW%2BgLc%2BGO3KJct7i0iIXNkoIZszX2ebWfqr%2BlTwOnqKzorBVb04YVvJU1QYP8&X-Amz-Signature=798f76e815cae4ffc093aeb2dd2db9c5ec73d2c10bc0a19de527371ff5066299&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667F6ONV6X%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIH8E9bsDCIPhX4bpWSP0Zks7w2r2b1vIlzTXvM7kew3YAiEAnzCBq9HlR0OStUZckh9lt6T%2Bd9wdlzJeo6d%2BniZ1scEq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDBcaZPOfdRM%2F3uElICrcA6BaZwTLotpaIX3sUxtNPqQsPRC9Q9MIp44SIs8Xj7ctqg9jcNZCEPMdcYjqEDQm9vhXOuxH3TOzs8Sadm%2BMRRkr9RnVZGX%2FgbA1dRTrOiA2w84dnuuWUNOVlv%2FF7xP8QeEstIies3i7o4hN%2BxR1TF%2FvBxceNxkH6g02CuwR7RFydr7eZLXE%2BY5i7or6Lbgv7EG1Stv9jq1YA1l1qKr%2FWUSbjZQBm2kDBHHhvjF%2F0ui4dRwXxzQco3QnG8%2BKxwE87aZsW4VtzcN1rER1HzFh7fTuw2iSohJbws9utIGgLKZRhMJ0ei3JQaf9ppx%2BPOXSq%2FdGtRVrdBpVLs2VmM8LlDxkOQv4jdvOjTqAH6GxwFaz3DERwZTKtill91wDbXsvIUWhqU%2BfNMD0rZVaBj9EDT%2BelS517nO2lYFmkt8%2BlMuwN0kC%2B63lhvGvMGOerDPieZR9SjIkvxVDk5mW5oIMT2otw9kRrwaaS4SJ8ppKS0zofMwgnlI9HVCRjkqtZPjVHHxE%2Fyf1Bo%2F4DtukMo%2B1s%2FpVAJsyvklmwerKRG1eWxULHTT%2FU%2FtdtH0tQ7JN4dNvgwsXmyrvm4z0tcE5vjLXN3ROsp48LZ4jF4GcVwTzopwVbfrekFtpFQ8ltF%2BrMOuO%2BM0GOqUB7Y%2BcyHo41wMoe5HZVgcKihnCxTd%2FbOwp4QmNZLNCfOZrpWyCPdml2N6QJ4jnhju%2BzYiEJg%2BFcaIEk5DBnRDOFyjyi8Msc8p7ELKTR%2Flg0gQWAZLfODDeh38AGQjFtBlJMTIgITz22CS%2B2mUTjUZdjqVvr6VklozIW%2BgLc%2BGO3KJct7i0iIXNkoIZszX2ebWfqr%2BlTwOnqKzorBVb04YVvJU1QYP8&X-Amz-Signature=90a406da81b484b473d9575b4496902da1833a22a03e00475c21615ce8d74e46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

