---
title: Dify私有化部署
date: '2024-11-15T09:08:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- Dify
categories:
- AI
---

# 1.创建服务器准备工作

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ODWTU73%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWCy2r8FONoy5Qvjpka8gCt019DcWyv6CPpwHryLlxggIgO4EGAHUMgY3aZdrSnbPmXNy%2BUVFikcmd79ecf%2F8nOaQq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDAVlqPrCTtgYSE1R%2FSrcA%2FxQKCErZM9PG6xgT5up%2ByTf5HjNWnx5YMvqViv5f7Zq2a9x2UCKEicsk1%2FhQ92a8nXwIprA7w0yAnPh%2ByIVzXXNa3q1KHFm17NT1hR8Iu3fgmWk7%2BsjOgvGWCUMnx0rp%2B6fNUTuuesxt7t0Lyvf2pzfMFi3nUFo8oW4GSTLyyTF4BPgx15IG6Wtsi%2B52GbOEk23ktycBCRFwuOyF3YxaFJ8dYy2k5UTnYadBB5HO%2BDSMTUxWubRIEzX4uEf2YnyfH6DY8Pb1g7xIACX4VlDd0EV%2BRZ%2BSicDuwjiR0XYUep%2FLKWnTR%2BRIBvW9922MdYEPS5rZWv8gcpDxSeNr2Arfh%2Bqb6mNqCJyCdjkrioz2JIfwvdKLogtdrVvkvBFKccWvP%2FZcji2mCoLtwC5pMW7jfF2ciITJv0kWHgGoTBMmmmwA3i5a%2BZy09x47qebpjfOdFgNadIoTHO3B6KCoYw83akFTEg6RHZE1NAd9StVcWtLhu%2F0knNy4BcaGKJOgjltnBo2Inkr2oyzXdzKQDvJwEm1NQ5NrwQZnqZcGZPRejV9D3dubB8Y6YqBFWdgKJ8Abv3NGFgtSRCaoq4srdPQDgCo7TEdz2QoJ1T2%2F3eM1FLVc%2BAbWG3OrL3BayjyMPSLyMkGOqUBzFT6aUY%2Flxv6Bg1rkUOcI%2BNa8JlypukA%2BhagzhWF9at2zuTMUvJnNfDIL106xlv7BjD1q4Djimnh3l5qTYvcYGggCC69niC7PuvK16TS5yCKqvi%2Bi1uJHAiBzE7K8kAEPEGlfOtRG6ZtQuUtqQ%2F8eOi0OVA9pk20MINNKtlqSQLRYTcm%2Bkth6H8epdFL2rSigdkXL%2FnDYU6gk3IkmLaXVuIFIqq6&X-Amz-Signature=f3be1c5aa28c4941493f81b554f02df8adadacb7ab4aaf0c95e493573be9fbe4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ODWTU73%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWCy2r8FONoy5Qvjpka8gCt019DcWyv6CPpwHryLlxggIgO4EGAHUMgY3aZdrSnbPmXNy%2BUVFikcmd79ecf%2F8nOaQq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDAVlqPrCTtgYSE1R%2FSrcA%2FxQKCErZM9PG6xgT5up%2ByTf5HjNWnx5YMvqViv5f7Zq2a9x2UCKEicsk1%2FhQ92a8nXwIprA7w0yAnPh%2ByIVzXXNa3q1KHFm17NT1hR8Iu3fgmWk7%2BsjOgvGWCUMnx0rp%2B6fNUTuuesxt7t0Lyvf2pzfMFi3nUFo8oW4GSTLyyTF4BPgx15IG6Wtsi%2B52GbOEk23ktycBCRFwuOyF3YxaFJ8dYy2k5UTnYadBB5HO%2BDSMTUxWubRIEzX4uEf2YnyfH6DY8Pb1g7xIACX4VlDd0EV%2BRZ%2BSicDuwjiR0XYUep%2FLKWnTR%2BRIBvW9922MdYEPS5rZWv8gcpDxSeNr2Arfh%2Bqb6mNqCJyCdjkrioz2JIfwvdKLogtdrVvkvBFKccWvP%2FZcji2mCoLtwC5pMW7jfF2ciITJv0kWHgGoTBMmmmwA3i5a%2BZy09x47qebpjfOdFgNadIoTHO3B6KCoYw83akFTEg6RHZE1NAd9StVcWtLhu%2F0knNy4BcaGKJOgjltnBo2Inkr2oyzXdzKQDvJwEm1NQ5NrwQZnqZcGZPRejV9D3dubB8Y6YqBFWdgKJ8Abv3NGFgtSRCaoq4srdPQDgCo7TEdz2QoJ1T2%2F3eM1FLVc%2BAbWG3OrL3BayjyMPSLyMkGOqUBzFT6aUY%2Flxv6Bg1rkUOcI%2BNa8JlypukA%2BhagzhWF9at2zuTMUvJnNfDIL106xlv7BjD1q4Djimnh3l5qTYvcYGggCC69niC7PuvK16TS5yCKqvi%2Bi1uJHAiBzE7K8kAEPEGlfOtRG6ZtQuUtqQ%2F8eOi0OVA9pk20MINNKtlqSQLRYTcm%2Bkth6H8epdFL2rSigdkXL%2FnDYU6gk3IkmLaXVuIFIqq6&X-Amz-Signature=194a184c61c940f6fffbea00b817567c4954210a88a450d36881e7a4c2bc73dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

服务器的系统选择Ubuntu 22.04版本并且克隆 Dify 源代码至本地环境

```javascript
git clone https://github.com/langgenius/dify.git
```

# 2.安装docker和docker compose



## 首先，确保你的软件包是最新的：

```javascript
sudo apt-get update
sudo apt-get upgrade -y
```

## 安装docker

### 第一种方法(一键安装)

```javascript
curl -sSL get-docker.geekery.cn | bash
```

### 第二种方法

```javascript
# 安装必要的依赖，让apt支持https
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common

# 添加 Docker 的官方 GPG 密钥
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 添加 Docker APT 仓库
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 更新 APT 包索引
sudo apt-get update

# 安装 Docker CE
sudo apt-get install -y docker-ce
#验证安装
docker version
```



## 安装docker compose

### 下载最新的 Docker Compose 二进制文件

```javascript
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

```

### 为 Docker Compose 二进制文件添加执行权限

```javascript
sudo chmod +x /usr/local/bin/docker-compose
```

### 验证安装

```javascript
docker-compose --version
```



# 3.docker换源和配置DNS

## docker换源

首先输入

```javascript
vim /etc/docker/daemon.json 
```

按“I”进入编辑者模式之后把一下代码粘贴进去



```javascript
{
    "registry-mirrors": [
        "https://dockerproxy.cn",
        "https://docker.rainbond.cc",
        "https://docker.udayun.com",
        "https://docker.211678.top"
    ]
}
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ODWTU73%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWCy2r8FONoy5Qvjpka8gCt019DcWyv6CPpwHryLlxggIgO4EGAHUMgY3aZdrSnbPmXNy%2BUVFikcmd79ecf%2F8nOaQq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDAVlqPrCTtgYSE1R%2FSrcA%2FxQKCErZM9PG6xgT5up%2ByTf5HjNWnx5YMvqViv5f7Zq2a9x2UCKEicsk1%2FhQ92a8nXwIprA7w0yAnPh%2ByIVzXXNa3q1KHFm17NT1hR8Iu3fgmWk7%2BsjOgvGWCUMnx0rp%2B6fNUTuuesxt7t0Lyvf2pzfMFi3nUFo8oW4GSTLyyTF4BPgx15IG6Wtsi%2B52GbOEk23ktycBCRFwuOyF3YxaFJ8dYy2k5UTnYadBB5HO%2BDSMTUxWubRIEzX4uEf2YnyfH6DY8Pb1g7xIACX4VlDd0EV%2BRZ%2BSicDuwjiR0XYUep%2FLKWnTR%2BRIBvW9922MdYEPS5rZWv8gcpDxSeNr2Arfh%2Bqb6mNqCJyCdjkrioz2JIfwvdKLogtdrVvkvBFKccWvP%2FZcji2mCoLtwC5pMW7jfF2ciITJv0kWHgGoTBMmmmwA3i5a%2BZy09x47qebpjfOdFgNadIoTHO3B6KCoYw83akFTEg6RHZE1NAd9StVcWtLhu%2F0knNy4BcaGKJOgjltnBo2Inkr2oyzXdzKQDvJwEm1NQ5NrwQZnqZcGZPRejV9D3dubB8Y6YqBFWdgKJ8Abv3NGFgtSRCaoq4srdPQDgCo7TEdz2QoJ1T2%2F3eM1FLVc%2BAbWG3OrL3BayjyMPSLyMkGOqUBzFT6aUY%2Flxv6Bg1rkUOcI%2BNa8JlypukA%2BhagzhWF9at2zuTMUvJnNfDIL106xlv7BjD1q4Djimnh3l5qTYvcYGggCC69niC7PuvK16TS5yCKqvi%2Bi1uJHAiBzE7K8kAEPEGlfOtRG6ZtQuUtqQ%2F8eOi0OVA9pk20MINNKtlqSQLRYTcm%2Bkth6H8epdFL2rSigdkXL%2FnDYU6gk3IkmLaXVuIFIqq6&X-Amz-Signature=abdbd64bc398a73c0a3a58ad372bf3aadb6def7b0b5f00329c029ed0312e59d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

粘贴完成之后按“esc”键，在同时按“shift”和“;”进入上帝模式输入wq保存退出

最后重新启动docker

```javascript
systemctl restart docker
```



## 配置DNS



- 备份文件：
- 修改文件内容：
最后重新启动相关网络服务

```javascript
systemctl restart systemd-resolved
```

# 4.启动dify

### 进入 Dify 源代码的 Docker 目录

```plain text
cd dify/docker
```



### 启动 Docker 容器

根据你系统上的 Docker Compose 版本，选择合适的命令来启动容器。你可以通过 $ docker compose version 命令检查版本，详细说明请参考 Docker 官方文档：

- 如果版本是 Docker Compose V2，使用以下命令：
```plain text
docker compose up -d
```

- 如果版本是 Docker Compose V1，使用以下命令：
```plain text
docker-compose up -d
```



输入docker ps和docker compose ps看看是否启动

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ODWTU73%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWCy2r8FONoy5Qvjpka8gCt019DcWyv6CPpwHryLlxggIgO4EGAHUMgY3aZdrSnbPmXNy%2BUVFikcmd79ecf%2F8nOaQq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDAVlqPrCTtgYSE1R%2FSrcA%2FxQKCErZM9PG6xgT5up%2ByTf5HjNWnx5YMvqViv5f7Zq2a9x2UCKEicsk1%2FhQ92a8nXwIprA7w0yAnPh%2ByIVzXXNa3q1KHFm17NT1hR8Iu3fgmWk7%2BsjOgvGWCUMnx0rp%2B6fNUTuuesxt7t0Lyvf2pzfMFi3nUFo8oW4GSTLyyTF4BPgx15IG6Wtsi%2B52GbOEk23ktycBCRFwuOyF3YxaFJ8dYy2k5UTnYadBB5HO%2BDSMTUxWubRIEzX4uEf2YnyfH6DY8Pb1g7xIACX4VlDd0EV%2BRZ%2BSicDuwjiR0XYUep%2FLKWnTR%2BRIBvW9922MdYEPS5rZWv8gcpDxSeNr2Arfh%2Bqb6mNqCJyCdjkrioz2JIfwvdKLogtdrVvkvBFKccWvP%2FZcji2mCoLtwC5pMW7jfF2ciITJv0kWHgGoTBMmmmwA3i5a%2BZy09x47qebpjfOdFgNadIoTHO3B6KCoYw83akFTEg6RHZE1NAd9StVcWtLhu%2F0knNy4BcaGKJOgjltnBo2Inkr2oyzXdzKQDvJwEm1NQ5NrwQZnqZcGZPRejV9D3dubB8Y6YqBFWdgKJ8Abv3NGFgtSRCaoq4srdPQDgCo7TEdz2QoJ1T2%2F3eM1FLVc%2BAbWG3OrL3BayjyMPSLyMkGOqUBzFT6aUY%2Flxv6Bg1rkUOcI%2BNa8JlypukA%2BhagzhWF9at2zuTMUvJnNfDIL106xlv7BjD1q4Djimnh3l5qTYvcYGggCC69niC7PuvK16TS5yCKqvi%2Bi1uJHAiBzE7K8kAEPEGlfOtRG6ZtQuUtqQ%2F8eOi0OVA9pk20MINNKtlqSQLRYTcm%2Bkth6H8epdFL2rSigdkXL%2FnDYU6gk3IkmLaXVuIFIqq6&X-Amz-Signature=2e2dd9e58e431f130397918fe1b35c68c83b8904f94d3d587140cfdda0858899&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ODWTU73%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWCy2r8FONoy5Qvjpka8gCt019DcWyv6CPpwHryLlxggIgO4EGAHUMgY3aZdrSnbPmXNy%2BUVFikcmd79ecf%2F8nOaQq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDAVlqPrCTtgYSE1R%2FSrcA%2FxQKCErZM9PG6xgT5up%2ByTf5HjNWnx5YMvqViv5f7Zq2a9x2UCKEicsk1%2FhQ92a8nXwIprA7w0yAnPh%2ByIVzXXNa3q1KHFm17NT1hR8Iu3fgmWk7%2BsjOgvGWCUMnx0rp%2B6fNUTuuesxt7t0Lyvf2pzfMFi3nUFo8oW4GSTLyyTF4BPgx15IG6Wtsi%2B52GbOEk23ktycBCRFwuOyF3YxaFJ8dYy2k5UTnYadBB5HO%2BDSMTUxWubRIEzX4uEf2YnyfH6DY8Pb1g7xIACX4VlDd0EV%2BRZ%2BSicDuwjiR0XYUep%2FLKWnTR%2BRIBvW9922MdYEPS5rZWv8gcpDxSeNr2Arfh%2Bqb6mNqCJyCdjkrioz2JIfwvdKLogtdrVvkvBFKccWvP%2FZcji2mCoLtwC5pMW7jfF2ciITJv0kWHgGoTBMmmmwA3i5a%2BZy09x47qebpjfOdFgNadIoTHO3B6KCoYw83akFTEg6RHZE1NAd9StVcWtLhu%2F0knNy4BcaGKJOgjltnBo2Inkr2oyzXdzKQDvJwEm1NQ5NrwQZnqZcGZPRejV9D3dubB8Y6YqBFWdgKJ8Abv3NGFgtSRCaoq4srdPQDgCo7TEdz2QoJ1T2%2F3eM1FLVc%2BAbWG3OrL3BayjyMPSLyMkGOqUBzFT6aUY%2Flxv6Bg1rkUOcI%2BNa8JlypukA%2BhagzhWF9at2zuTMUvJnNfDIL106xlv7BjD1q4Djimnh3l5qTYvcYGggCC69niC7PuvK16TS5yCKqvi%2Bi1uJHAiBzE7K8kAEPEGlfOtRG6ZtQuUtqQ%2F8eOi0OVA9pk20MINNKtlqSQLRYTcm%2Bkth6H8epdFL2rSigdkXL%2FnDYU6gk3IkmLaXVuIFIqq6&X-Amz-Signature=b77798d3ae9b317b54f6a1d9aba5094ff01ded70f36ce3bc39eb84fedfe7de54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ODWTU73%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWCy2r8FONoy5Qvjpka8gCt019DcWyv6CPpwHryLlxggIgO4EGAHUMgY3aZdrSnbPmXNy%2BUVFikcmd79ecf%2F8nOaQq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDAVlqPrCTtgYSE1R%2FSrcA%2FxQKCErZM9PG6xgT5up%2ByTf5HjNWnx5YMvqViv5f7Zq2a9x2UCKEicsk1%2FhQ92a8nXwIprA7w0yAnPh%2ByIVzXXNa3q1KHFm17NT1hR8Iu3fgmWk7%2BsjOgvGWCUMnx0rp%2B6fNUTuuesxt7t0Lyvf2pzfMFi3nUFo8oW4GSTLyyTF4BPgx15IG6Wtsi%2B52GbOEk23ktycBCRFwuOyF3YxaFJ8dYy2k5UTnYadBB5HO%2BDSMTUxWubRIEzX4uEf2YnyfH6DY8Pb1g7xIACX4VlDd0EV%2BRZ%2BSicDuwjiR0XYUep%2FLKWnTR%2BRIBvW9922MdYEPS5rZWv8gcpDxSeNr2Arfh%2Bqb6mNqCJyCdjkrioz2JIfwvdKLogtdrVvkvBFKccWvP%2FZcji2mCoLtwC5pMW7jfF2ciITJv0kWHgGoTBMmmmwA3i5a%2BZy09x47qebpjfOdFgNadIoTHO3B6KCoYw83akFTEg6RHZE1NAd9StVcWtLhu%2F0knNy4BcaGKJOgjltnBo2Inkr2oyzXdzKQDvJwEm1NQ5NrwQZnqZcGZPRejV9D3dubB8Y6YqBFWdgKJ8Abv3NGFgtSRCaoq4srdPQDgCo7TEdz2QoJ1T2%2F3eM1FLVc%2BAbWG3OrL3BayjyMPSLyMkGOqUBzFT6aUY%2Flxv6Bg1rkUOcI%2BNa8JlypukA%2BhagzhWF9at2zuTMUvJnNfDIL106xlv7BjD1q4Djimnh3l5qTYvcYGggCC69niC7PuvK16TS5yCKqvi%2Bi1uJHAiBzE7K8kAEPEGlfOtRG6ZtQuUtqQ%2F8eOi0OVA9pk20MINNKtlqSQLRYTcm%2Bkth6H8epdFL2rSigdkXL%2FnDYU6gk3IkmLaXVuIFIqq6&X-Amz-Signature=afb4bc9a82c6b69381b7626495c2bd9203496d6a1cdc07d9f5c560fcb8e0b0df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ODWTU73%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWCy2r8FONoy5Qvjpka8gCt019DcWyv6CPpwHryLlxggIgO4EGAHUMgY3aZdrSnbPmXNy%2BUVFikcmd79ecf%2F8nOaQq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDAVlqPrCTtgYSE1R%2FSrcA%2FxQKCErZM9PG6xgT5up%2ByTf5HjNWnx5YMvqViv5f7Zq2a9x2UCKEicsk1%2FhQ92a8nXwIprA7w0yAnPh%2ByIVzXXNa3q1KHFm17NT1hR8Iu3fgmWk7%2BsjOgvGWCUMnx0rp%2B6fNUTuuesxt7t0Lyvf2pzfMFi3nUFo8oW4GSTLyyTF4BPgx15IG6Wtsi%2B52GbOEk23ktycBCRFwuOyF3YxaFJ8dYy2k5UTnYadBB5HO%2BDSMTUxWubRIEzX4uEf2YnyfH6DY8Pb1g7xIACX4VlDd0EV%2BRZ%2BSicDuwjiR0XYUep%2FLKWnTR%2BRIBvW9922MdYEPS5rZWv8gcpDxSeNr2Arfh%2Bqb6mNqCJyCdjkrioz2JIfwvdKLogtdrVvkvBFKccWvP%2FZcji2mCoLtwC5pMW7jfF2ciITJv0kWHgGoTBMmmmwA3i5a%2BZy09x47qebpjfOdFgNadIoTHO3B6KCoYw83akFTEg6RHZE1NAd9StVcWtLhu%2F0knNy4BcaGKJOgjltnBo2Inkr2oyzXdzKQDvJwEm1NQ5NrwQZnqZcGZPRejV9D3dubB8Y6YqBFWdgKJ8Abv3NGFgtSRCaoq4srdPQDgCo7TEdz2QoJ1T2%2F3eM1FLVc%2BAbWG3OrL3BayjyMPSLyMkGOqUBzFT6aUY%2Flxv6Bg1rkUOcI%2BNa8JlypukA%2BhagzhWF9at2zuTMUvJnNfDIL106xlv7BjD1q4Djimnh3l5qTYvcYGggCC69niC7PuvK16TS5yCKqvi%2Bi1uJHAiBzE7K8kAEPEGlfOtRG6ZtQuUtqQ%2F8eOi0OVA9pk20MINNKtlqSQLRYTcm%2Bkth6H8epdFL2rSigdkXL%2FnDYU6gk3IkmLaXVuIFIqq6&X-Amz-Signature=754f761ec804e3e9096502da71d29a1da8652112dafd0fcbbc540726e7c8861a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ODWTU73%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWCy2r8FONoy5Qvjpka8gCt019DcWyv6CPpwHryLlxggIgO4EGAHUMgY3aZdrSnbPmXNy%2BUVFikcmd79ecf%2F8nOaQq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDAVlqPrCTtgYSE1R%2FSrcA%2FxQKCErZM9PG6xgT5up%2ByTf5HjNWnx5YMvqViv5f7Zq2a9x2UCKEicsk1%2FhQ92a8nXwIprA7w0yAnPh%2ByIVzXXNa3q1KHFm17NT1hR8Iu3fgmWk7%2BsjOgvGWCUMnx0rp%2B6fNUTuuesxt7t0Lyvf2pzfMFi3nUFo8oW4GSTLyyTF4BPgx15IG6Wtsi%2B52GbOEk23ktycBCRFwuOyF3YxaFJ8dYy2k5UTnYadBB5HO%2BDSMTUxWubRIEzX4uEf2YnyfH6DY8Pb1g7xIACX4VlDd0EV%2BRZ%2BSicDuwjiR0XYUep%2FLKWnTR%2BRIBvW9922MdYEPS5rZWv8gcpDxSeNr2Arfh%2Bqb6mNqCJyCdjkrioz2JIfwvdKLogtdrVvkvBFKccWvP%2FZcji2mCoLtwC5pMW7jfF2ciITJv0kWHgGoTBMmmmwA3i5a%2BZy09x47qebpjfOdFgNadIoTHO3B6KCoYw83akFTEg6RHZE1NAd9StVcWtLhu%2F0knNy4BcaGKJOgjltnBo2Inkr2oyzXdzKQDvJwEm1NQ5NrwQZnqZcGZPRejV9D3dubB8Y6YqBFWdgKJ8Abv3NGFgtSRCaoq4srdPQDgCo7TEdz2QoJ1T2%2F3eM1FLVc%2BAbWG3OrL3BayjyMPSLyMkGOqUBzFT6aUY%2Flxv6Bg1rkUOcI%2BNa8JlypukA%2BhagzhWF9at2zuTMUvJnNfDIL106xlv7BjD1q4Djimnh3l5qTYvcYGggCC69niC7PuvK16TS5yCKqvi%2Bi1uJHAiBzE7K8kAEPEGlfOtRG6ZtQuUtqQ%2F8eOi0OVA9pk20MINNKtlqSQLRYTcm%2Bkth6H8epdFL2rSigdkXL%2FnDYU6gk3IkmLaXVuIFIqq6&X-Amz-Signature=686a829c061a739869376047d88d7eeb8b8ee816da6b64a4725385d263da17e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ODWTU73%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWCy2r8FONoy5Qvjpka8gCt019DcWyv6CPpwHryLlxggIgO4EGAHUMgY3aZdrSnbPmXNy%2BUVFikcmd79ecf%2F8nOaQq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDAVlqPrCTtgYSE1R%2FSrcA%2FxQKCErZM9PG6xgT5up%2ByTf5HjNWnx5YMvqViv5f7Zq2a9x2UCKEicsk1%2FhQ92a8nXwIprA7w0yAnPh%2ByIVzXXNa3q1KHFm17NT1hR8Iu3fgmWk7%2BsjOgvGWCUMnx0rp%2B6fNUTuuesxt7t0Lyvf2pzfMFi3nUFo8oW4GSTLyyTF4BPgx15IG6Wtsi%2B52GbOEk23ktycBCRFwuOyF3YxaFJ8dYy2k5UTnYadBB5HO%2BDSMTUxWubRIEzX4uEf2YnyfH6DY8Pb1g7xIACX4VlDd0EV%2BRZ%2BSicDuwjiR0XYUep%2FLKWnTR%2BRIBvW9922MdYEPS5rZWv8gcpDxSeNr2Arfh%2Bqb6mNqCJyCdjkrioz2JIfwvdKLogtdrVvkvBFKccWvP%2FZcji2mCoLtwC5pMW7jfF2ciITJv0kWHgGoTBMmmmwA3i5a%2BZy09x47qebpjfOdFgNadIoTHO3B6KCoYw83akFTEg6RHZE1NAd9StVcWtLhu%2F0knNy4BcaGKJOgjltnBo2Inkr2oyzXdzKQDvJwEm1NQ5NrwQZnqZcGZPRejV9D3dubB8Y6YqBFWdgKJ8Abv3NGFgtSRCaoq4srdPQDgCo7TEdz2QoJ1T2%2F3eM1FLVc%2BAbWG3OrL3BayjyMPSLyMkGOqUBzFT6aUY%2Flxv6Bg1rkUOcI%2BNa8JlypukA%2BhagzhWF9at2zuTMUvJnNfDIL106xlv7BjD1q4Djimnh3l5qTYvcYGggCC69niC7PuvK16TS5yCKqvi%2Bi1uJHAiBzE7K8kAEPEGlfOtRG6ZtQuUtqQ%2F8eOi0OVA9pk20MINNKtlqSQLRYTcm%2Bkth6H8epdFL2rSigdkXL%2FnDYU6gk3IkmLaXVuIFIqq6&X-Amz-Signature=057f1869189128650cce0c599100c44ef1b210496167bdf3edbb9b3cfbc50eb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ODWTU73%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWCy2r8FONoy5Qvjpka8gCt019DcWyv6CPpwHryLlxggIgO4EGAHUMgY3aZdrSnbPmXNy%2BUVFikcmd79ecf%2F8nOaQq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDAVlqPrCTtgYSE1R%2FSrcA%2FxQKCErZM9PG6xgT5up%2ByTf5HjNWnx5YMvqViv5f7Zq2a9x2UCKEicsk1%2FhQ92a8nXwIprA7w0yAnPh%2ByIVzXXNa3q1KHFm17NT1hR8Iu3fgmWk7%2BsjOgvGWCUMnx0rp%2B6fNUTuuesxt7t0Lyvf2pzfMFi3nUFo8oW4GSTLyyTF4BPgx15IG6Wtsi%2B52GbOEk23ktycBCRFwuOyF3YxaFJ8dYy2k5UTnYadBB5HO%2BDSMTUxWubRIEzX4uEf2YnyfH6DY8Pb1g7xIACX4VlDd0EV%2BRZ%2BSicDuwjiR0XYUep%2FLKWnTR%2BRIBvW9922MdYEPS5rZWv8gcpDxSeNr2Arfh%2Bqb6mNqCJyCdjkrioz2JIfwvdKLogtdrVvkvBFKccWvP%2FZcji2mCoLtwC5pMW7jfF2ciITJv0kWHgGoTBMmmmwA3i5a%2BZy09x47qebpjfOdFgNadIoTHO3B6KCoYw83akFTEg6RHZE1NAd9StVcWtLhu%2F0knNy4BcaGKJOgjltnBo2Inkr2oyzXdzKQDvJwEm1NQ5NrwQZnqZcGZPRejV9D3dubB8Y6YqBFWdgKJ8Abv3NGFgtSRCaoq4srdPQDgCo7TEdz2QoJ1T2%2F3eM1FLVc%2BAbWG3OrL3BayjyMPSLyMkGOqUBzFT6aUY%2Flxv6Bg1rkUOcI%2BNa8JlypukA%2BhagzhWF9at2zuTMUvJnNfDIL106xlv7BjD1q4Djimnh3l5qTYvcYGggCC69niC7PuvK16TS5yCKqvi%2Bi1uJHAiBzE7K8kAEPEGlfOtRG6ZtQuUtqQ%2F8eOi0OVA9pk20MINNKtlqSQLRYTcm%2Bkth6H8epdFL2rSigdkXL%2FnDYU6gk3IkmLaXVuIFIqq6&X-Amz-Signature=167e732e4f50fd0aa72e8f05bc22bdcb277c1ddf8a2c748f7ab7eb175d24047e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

