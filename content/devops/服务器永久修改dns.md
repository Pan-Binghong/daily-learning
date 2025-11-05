---
title: 服务器永久修改DNS
date: '2024-11-19T08:46:00.000Z'
lastmod: '2024-11-27T14:36:00.000Z'
draft: false
标签:
- Linux
categories:
- DevOps
---

> 💡 说了永久就是永久。

---

1. 打开DNS解析配置文件
1. 写入以下内容
1. 重启DNS服务器
1. 备份
1. 创建软链接
---

### 完整流程

```bash
# 1. 编辑 systemd-resolved 的配置文件
sudo vi /etc/systemd/resolved.conf

# 在文件中写入以下内容（根据需要调整）
DNS=114.114.114.114 8.8.8.8 8.8.4.4
FallbackDNs=8.8.8.8
# Domains=domain.com  # 根据需要启用

# 2. 重启 systemd-resolved 服务
sudo systemctl restart systemd-resolved

# 3. 备份原有的 resolv.conf
sudo mv /etc/resolv.conf /etc/resolv.conf_bak

# 4. 创建软链接指向 systemd-resolved 的配置
sudo ln -s /run/systemd/resolve/resolv.conf /etc/resolv.conf

# 5. 验证 DNS 配置
systemd-resolve --status
nslookup www.google.com

```



