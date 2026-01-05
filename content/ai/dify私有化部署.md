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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYA66KGP%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCfM%2BRGRxr3XTA5sxWHhIa24vyYPhMWJd2BSgVhWBvndQIgO%2BTOodxplmREA2Ce3cBwZocaQSVdKbkXS3SDunSYqkkq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDNek%2B6M8Zkl6ryfO0CrcA8jrdEjAaMWCbGRUEzYY2ECDj0CXi1iQkV7KkhxSguZ7gveQa99XsgkL%2FaiAtae4P0hDmVSQn0peV9LK4h%2FXQIWluBkbgu%2FVNl8WMrMI3EHar2ByUgk7Hmy3T1Q3sbl091IecBsekws8kwqIUcI5HjDHXm%2Fg2AWujc86A2KGVkzS6hsGCueAOKTJ6OoOSwO6p3%2FpPxoRc0%2BV66s9enAUvVbbafe6kJs2CVuXuzYywHpLxBfmOO%2FuFwh8Z40UX9qNSuUUDOXCT%2B7cSDDwXnQqvDcZhjGscmFg7NLdhsKGlev%2BVLbuxGwjH6kxkbFX1GtVs0cUl%2FoIZ%2F99T3Hh7%2F%2F%2BYaaDpcdQK0xfJUuXVth6Rdhaw44%2BWbttUnW%2F%2FBskjOwOfm4KBQ60DUEVKvv%2BKil6xp1A%2FNsFuVYj%2BP9xV0EULZkv9sGggetfi1EvlXJFx6n9pzn39652VmUPEwENAymJrmSAtllSorc4fwyDosD%2FTFJGAVWv2ux42EbrYqr850WZ1VkmP5E8DfMUNfKOwUteyCw4o5VWKa1k1zTrClEeDQ9y2JIBy1spT3LUymt%2FOBh8b9nnd7YDy2pcEr6yt9y1VAdi6GHXu4j%2Fpl53BwW3%2FvhNl8k9J8G1UAG64SRyMKjv68oGOqUB%2BR4KK06WjtfDbeReTvoIvjwEFqDb%2FnTznuwCAnuoNYgAq0FR4f%2FEeETfiEXpX5TWv3Php86fIvb8yMWCPU7E0P1OCLH2zmaeOXWoGgSpcklKRWDtQ1stEsbP9njZzsIr1yvwU0RRoLwnLhPfP8XuvBw4Fz5FTl%2F7vWnRJthG2V%2BmTL9V9RSg7J%2BszxTBI2VY8aqHkVo9vEgjkmGlt5EOY2uxC6IS&X-Amz-Signature=dd86c7df93e31c26ceb62a9edc0eb2ae1c6e76c68b4a3520ed8dc6b08f6735e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYA66KGP%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCfM%2BRGRxr3XTA5sxWHhIa24vyYPhMWJd2BSgVhWBvndQIgO%2BTOodxplmREA2Ce3cBwZocaQSVdKbkXS3SDunSYqkkq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDNek%2B6M8Zkl6ryfO0CrcA8jrdEjAaMWCbGRUEzYY2ECDj0CXi1iQkV7KkhxSguZ7gveQa99XsgkL%2FaiAtae4P0hDmVSQn0peV9LK4h%2FXQIWluBkbgu%2FVNl8WMrMI3EHar2ByUgk7Hmy3T1Q3sbl091IecBsekws8kwqIUcI5HjDHXm%2Fg2AWujc86A2KGVkzS6hsGCueAOKTJ6OoOSwO6p3%2FpPxoRc0%2BV66s9enAUvVbbafe6kJs2CVuXuzYywHpLxBfmOO%2FuFwh8Z40UX9qNSuUUDOXCT%2B7cSDDwXnQqvDcZhjGscmFg7NLdhsKGlev%2BVLbuxGwjH6kxkbFX1GtVs0cUl%2FoIZ%2F99T3Hh7%2F%2F%2BYaaDpcdQK0xfJUuXVth6Rdhaw44%2BWbttUnW%2F%2FBskjOwOfm4KBQ60DUEVKvv%2BKil6xp1A%2FNsFuVYj%2BP9xV0EULZkv9sGggetfi1EvlXJFx6n9pzn39652VmUPEwENAymJrmSAtllSorc4fwyDosD%2FTFJGAVWv2ux42EbrYqr850WZ1VkmP5E8DfMUNfKOwUteyCw4o5VWKa1k1zTrClEeDQ9y2JIBy1spT3LUymt%2FOBh8b9nnd7YDy2pcEr6yt9y1VAdi6GHXu4j%2Fpl53BwW3%2FvhNl8k9J8G1UAG64SRyMKjv68oGOqUB%2BR4KK06WjtfDbeReTvoIvjwEFqDb%2FnTznuwCAnuoNYgAq0FR4f%2FEeETfiEXpX5TWv3Php86fIvb8yMWCPU7E0P1OCLH2zmaeOXWoGgSpcklKRWDtQ1stEsbP9njZzsIr1yvwU0RRoLwnLhPfP8XuvBw4Fz5FTl%2F7vWnRJthG2V%2BmTL9V9RSg7J%2BszxTBI2VY8aqHkVo9vEgjkmGlt5EOY2uxC6IS&X-Amz-Signature=dbf8339820a17ac8056348b1cc19444528c7257329b97307fe88f6d381e8f8bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYA66KGP%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCfM%2BRGRxr3XTA5sxWHhIa24vyYPhMWJd2BSgVhWBvndQIgO%2BTOodxplmREA2Ce3cBwZocaQSVdKbkXS3SDunSYqkkq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDNek%2B6M8Zkl6ryfO0CrcA8jrdEjAaMWCbGRUEzYY2ECDj0CXi1iQkV7KkhxSguZ7gveQa99XsgkL%2FaiAtae4P0hDmVSQn0peV9LK4h%2FXQIWluBkbgu%2FVNl8WMrMI3EHar2ByUgk7Hmy3T1Q3sbl091IecBsekws8kwqIUcI5HjDHXm%2Fg2AWujc86A2KGVkzS6hsGCueAOKTJ6OoOSwO6p3%2FpPxoRc0%2BV66s9enAUvVbbafe6kJs2CVuXuzYywHpLxBfmOO%2FuFwh8Z40UX9qNSuUUDOXCT%2B7cSDDwXnQqvDcZhjGscmFg7NLdhsKGlev%2BVLbuxGwjH6kxkbFX1GtVs0cUl%2FoIZ%2F99T3Hh7%2F%2F%2BYaaDpcdQK0xfJUuXVth6Rdhaw44%2BWbttUnW%2F%2FBskjOwOfm4KBQ60DUEVKvv%2BKil6xp1A%2FNsFuVYj%2BP9xV0EULZkv9sGggetfi1EvlXJFx6n9pzn39652VmUPEwENAymJrmSAtllSorc4fwyDosD%2FTFJGAVWv2ux42EbrYqr850WZ1VkmP5E8DfMUNfKOwUteyCw4o5VWKa1k1zTrClEeDQ9y2JIBy1spT3LUymt%2FOBh8b9nnd7YDy2pcEr6yt9y1VAdi6GHXu4j%2Fpl53BwW3%2FvhNl8k9J8G1UAG64SRyMKjv68oGOqUB%2BR4KK06WjtfDbeReTvoIvjwEFqDb%2FnTznuwCAnuoNYgAq0FR4f%2FEeETfiEXpX5TWv3Php86fIvb8yMWCPU7E0P1OCLH2zmaeOXWoGgSpcklKRWDtQ1stEsbP9njZzsIr1yvwU0RRoLwnLhPfP8XuvBw4Fz5FTl%2F7vWnRJthG2V%2BmTL9V9RSg7J%2BszxTBI2VY8aqHkVo9vEgjkmGlt5EOY2uxC6IS&X-Amz-Signature=e9a17d2163c6bce7c4640e84debc053853ef3203d4419fe0de0b81c1e9c31586&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYA66KGP%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCfM%2BRGRxr3XTA5sxWHhIa24vyYPhMWJd2BSgVhWBvndQIgO%2BTOodxplmREA2Ce3cBwZocaQSVdKbkXS3SDunSYqkkq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDNek%2B6M8Zkl6ryfO0CrcA8jrdEjAaMWCbGRUEzYY2ECDj0CXi1iQkV7KkhxSguZ7gveQa99XsgkL%2FaiAtae4P0hDmVSQn0peV9LK4h%2FXQIWluBkbgu%2FVNl8WMrMI3EHar2ByUgk7Hmy3T1Q3sbl091IecBsekws8kwqIUcI5HjDHXm%2Fg2AWujc86A2KGVkzS6hsGCueAOKTJ6OoOSwO6p3%2FpPxoRc0%2BV66s9enAUvVbbafe6kJs2CVuXuzYywHpLxBfmOO%2FuFwh8Z40UX9qNSuUUDOXCT%2B7cSDDwXnQqvDcZhjGscmFg7NLdhsKGlev%2BVLbuxGwjH6kxkbFX1GtVs0cUl%2FoIZ%2F99T3Hh7%2F%2F%2BYaaDpcdQK0xfJUuXVth6Rdhaw44%2BWbttUnW%2F%2FBskjOwOfm4KBQ60DUEVKvv%2BKil6xp1A%2FNsFuVYj%2BP9xV0EULZkv9sGggetfi1EvlXJFx6n9pzn39652VmUPEwENAymJrmSAtllSorc4fwyDosD%2FTFJGAVWv2ux42EbrYqr850WZ1VkmP5E8DfMUNfKOwUteyCw4o5VWKa1k1zTrClEeDQ9y2JIBy1spT3LUymt%2FOBh8b9nnd7YDy2pcEr6yt9y1VAdi6GHXu4j%2Fpl53BwW3%2FvhNl8k9J8G1UAG64SRyMKjv68oGOqUB%2BR4KK06WjtfDbeReTvoIvjwEFqDb%2FnTznuwCAnuoNYgAq0FR4f%2FEeETfiEXpX5TWv3Php86fIvb8yMWCPU7E0P1OCLH2zmaeOXWoGgSpcklKRWDtQ1stEsbP9njZzsIr1yvwU0RRoLwnLhPfP8XuvBw4Fz5FTl%2F7vWnRJthG2V%2BmTL9V9RSg7J%2BszxTBI2VY8aqHkVo9vEgjkmGlt5EOY2uxC6IS&X-Amz-Signature=5af57903c7eca31c778fb3774e2b5fe1c15986b2e1b387e0e17721c48aff9296&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYA66KGP%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCfM%2BRGRxr3XTA5sxWHhIa24vyYPhMWJd2BSgVhWBvndQIgO%2BTOodxplmREA2Ce3cBwZocaQSVdKbkXS3SDunSYqkkq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDNek%2B6M8Zkl6ryfO0CrcA8jrdEjAaMWCbGRUEzYY2ECDj0CXi1iQkV7KkhxSguZ7gveQa99XsgkL%2FaiAtae4P0hDmVSQn0peV9LK4h%2FXQIWluBkbgu%2FVNl8WMrMI3EHar2ByUgk7Hmy3T1Q3sbl091IecBsekws8kwqIUcI5HjDHXm%2Fg2AWujc86A2KGVkzS6hsGCueAOKTJ6OoOSwO6p3%2FpPxoRc0%2BV66s9enAUvVbbafe6kJs2CVuXuzYywHpLxBfmOO%2FuFwh8Z40UX9qNSuUUDOXCT%2B7cSDDwXnQqvDcZhjGscmFg7NLdhsKGlev%2BVLbuxGwjH6kxkbFX1GtVs0cUl%2FoIZ%2F99T3Hh7%2F%2F%2BYaaDpcdQK0xfJUuXVth6Rdhaw44%2BWbttUnW%2F%2FBskjOwOfm4KBQ60DUEVKvv%2BKil6xp1A%2FNsFuVYj%2BP9xV0EULZkv9sGggetfi1EvlXJFx6n9pzn39652VmUPEwENAymJrmSAtllSorc4fwyDosD%2FTFJGAVWv2ux42EbrYqr850WZ1VkmP5E8DfMUNfKOwUteyCw4o5VWKa1k1zTrClEeDQ9y2JIBy1spT3LUymt%2FOBh8b9nnd7YDy2pcEr6yt9y1VAdi6GHXu4j%2Fpl53BwW3%2FvhNl8k9J8G1UAG64SRyMKjv68oGOqUB%2BR4KK06WjtfDbeReTvoIvjwEFqDb%2FnTznuwCAnuoNYgAq0FR4f%2FEeETfiEXpX5TWv3Php86fIvb8yMWCPU7E0P1OCLH2zmaeOXWoGgSpcklKRWDtQ1stEsbP9njZzsIr1yvwU0RRoLwnLhPfP8XuvBw4Fz5FTl%2F7vWnRJthG2V%2BmTL9V9RSg7J%2BszxTBI2VY8aqHkVo9vEgjkmGlt5EOY2uxC6IS&X-Amz-Signature=f89452275fe58709bf302f35a44c2a8ac9906672191d61efadb8127a4629fa24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYA66KGP%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCfM%2BRGRxr3XTA5sxWHhIa24vyYPhMWJd2BSgVhWBvndQIgO%2BTOodxplmREA2Ce3cBwZocaQSVdKbkXS3SDunSYqkkq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDNek%2B6M8Zkl6ryfO0CrcA8jrdEjAaMWCbGRUEzYY2ECDj0CXi1iQkV7KkhxSguZ7gveQa99XsgkL%2FaiAtae4P0hDmVSQn0peV9LK4h%2FXQIWluBkbgu%2FVNl8WMrMI3EHar2ByUgk7Hmy3T1Q3sbl091IecBsekws8kwqIUcI5HjDHXm%2Fg2AWujc86A2KGVkzS6hsGCueAOKTJ6OoOSwO6p3%2FpPxoRc0%2BV66s9enAUvVbbafe6kJs2CVuXuzYywHpLxBfmOO%2FuFwh8Z40UX9qNSuUUDOXCT%2B7cSDDwXnQqvDcZhjGscmFg7NLdhsKGlev%2BVLbuxGwjH6kxkbFX1GtVs0cUl%2FoIZ%2F99T3Hh7%2F%2F%2BYaaDpcdQK0xfJUuXVth6Rdhaw44%2BWbttUnW%2F%2FBskjOwOfm4KBQ60DUEVKvv%2BKil6xp1A%2FNsFuVYj%2BP9xV0EULZkv9sGggetfi1EvlXJFx6n9pzn39652VmUPEwENAymJrmSAtllSorc4fwyDosD%2FTFJGAVWv2ux42EbrYqr850WZ1VkmP5E8DfMUNfKOwUteyCw4o5VWKa1k1zTrClEeDQ9y2JIBy1spT3LUymt%2FOBh8b9nnd7YDy2pcEr6yt9y1VAdi6GHXu4j%2Fpl53BwW3%2FvhNl8k9J8G1UAG64SRyMKjv68oGOqUB%2BR4KK06WjtfDbeReTvoIvjwEFqDb%2FnTznuwCAnuoNYgAq0FR4f%2FEeETfiEXpX5TWv3Php86fIvb8yMWCPU7E0P1OCLH2zmaeOXWoGgSpcklKRWDtQ1stEsbP9njZzsIr1yvwU0RRoLwnLhPfP8XuvBw4Fz5FTl%2F7vWnRJthG2V%2BmTL9V9RSg7J%2BszxTBI2VY8aqHkVo9vEgjkmGlt5EOY2uxC6IS&X-Amz-Signature=ca149260e3800c6c39e06856e0f2b1a72f146b89ab9d9359d31becae45a98e47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYA66KGP%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCfM%2BRGRxr3XTA5sxWHhIa24vyYPhMWJd2BSgVhWBvndQIgO%2BTOodxplmREA2Ce3cBwZocaQSVdKbkXS3SDunSYqkkq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDNek%2B6M8Zkl6ryfO0CrcA8jrdEjAaMWCbGRUEzYY2ECDj0CXi1iQkV7KkhxSguZ7gveQa99XsgkL%2FaiAtae4P0hDmVSQn0peV9LK4h%2FXQIWluBkbgu%2FVNl8WMrMI3EHar2ByUgk7Hmy3T1Q3sbl091IecBsekws8kwqIUcI5HjDHXm%2Fg2AWujc86A2KGVkzS6hsGCueAOKTJ6OoOSwO6p3%2FpPxoRc0%2BV66s9enAUvVbbafe6kJs2CVuXuzYywHpLxBfmOO%2FuFwh8Z40UX9qNSuUUDOXCT%2B7cSDDwXnQqvDcZhjGscmFg7NLdhsKGlev%2BVLbuxGwjH6kxkbFX1GtVs0cUl%2FoIZ%2F99T3Hh7%2F%2F%2BYaaDpcdQK0xfJUuXVth6Rdhaw44%2BWbttUnW%2F%2FBskjOwOfm4KBQ60DUEVKvv%2BKil6xp1A%2FNsFuVYj%2BP9xV0EULZkv9sGggetfi1EvlXJFx6n9pzn39652VmUPEwENAymJrmSAtllSorc4fwyDosD%2FTFJGAVWv2ux42EbrYqr850WZ1VkmP5E8DfMUNfKOwUteyCw4o5VWKa1k1zTrClEeDQ9y2JIBy1spT3LUymt%2FOBh8b9nnd7YDy2pcEr6yt9y1VAdi6GHXu4j%2Fpl53BwW3%2FvhNl8k9J8G1UAG64SRyMKjv68oGOqUB%2BR4KK06WjtfDbeReTvoIvjwEFqDb%2FnTznuwCAnuoNYgAq0FR4f%2FEeETfiEXpX5TWv3Php86fIvb8yMWCPU7E0P1OCLH2zmaeOXWoGgSpcklKRWDtQ1stEsbP9njZzsIr1yvwU0RRoLwnLhPfP8XuvBw4Fz5FTl%2F7vWnRJthG2V%2BmTL9V9RSg7J%2BszxTBI2VY8aqHkVo9vEgjkmGlt5EOY2uxC6IS&X-Amz-Signature=f946ae4598eb7f9454f12d918e3665b6c4f6ae284c8493c4e27b26cef1472a21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYA66KGP%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCfM%2BRGRxr3XTA5sxWHhIa24vyYPhMWJd2BSgVhWBvndQIgO%2BTOodxplmREA2Ce3cBwZocaQSVdKbkXS3SDunSYqkkq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDNek%2B6M8Zkl6ryfO0CrcA8jrdEjAaMWCbGRUEzYY2ECDj0CXi1iQkV7KkhxSguZ7gveQa99XsgkL%2FaiAtae4P0hDmVSQn0peV9LK4h%2FXQIWluBkbgu%2FVNl8WMrMI3EHar2ByUgk7Hmy3T1Q3sbl091IecBsekws8kwqIUcI5HjDHXm%2Fg2AWujc86A2KGVkzS6hsGCueAOKTJ6OoOSwO6p3%2FpPxoRc0%2BV66s9enAUvVbbafe6kJs2CVuXuzYywHpLxBfmOO%2FuFwh8Z40UX9qNSuUUDOXCT%2B7cSDDwXnQqvDcZhjGscmFg7NLdhsKGlev%2BVLbuxGwjH6kxkbFX1GtVs0cUl%2FoIZ%2F99T3Hh7%2F%2F%2BYaaDpcdQK0xfJUuXVth6Rdhaw44%2BWbttUnW%2F%2FBskjOwOfm4KBQ60DUEVKvv%2BKil6xp1A%2FNsFuVYj%2BP9xV0EULZkv9sGggetfi1EvlXJFx6n9pzn39652VmUPEwENAymJrmSAtllSorc4fwyDosD%2FTFJGAVWv2ux42EbrYqr850WZ1VkmP5E8DfMUNfKOwUteyCw4o5VWKa1k1zTrClEeDQ9y2JIBy1spT3LUymt%2FOBh8b9nnd7YDy2pcEr6yt9y1VAdi6GHXu4j%2Fpl53BwW3%2FvhNl8k9J8G1UAG64SRyMKjv68oGOqUB%2BR4KK06WjtfDbeReTvoIvjwEFqDb%2FnTznuwCAnuoNYgAq0FR4f%2FEeETfiEXpX5TWv3Php86fIvb8yMWCPU7E0P1OCLH2zmaeOXWoGgSpcklKRWDtQ1stEsbP9njZzsIr1yvwU0RRoLwnLhPfP8XuvBw4Fz5FTl%2F7vWnRJthG2V%2BmTL9V9RSg7J%2BszxTBI2VY8aqHkVo9vEgjkmGlt5EOY2uxC6IS&X-Amz-Signature=462a5afc3243a27057418572d22655b3cceba916d9d891aa158459734e3f8be9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYA66KGP%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCfM%2BRGRxr3XTA5sxWHhIa24vyYPhMWJd2BSgVhWBvndQIgO%2BTOodxplmREA2Ce3cBwZocaQSVdKbkXS3SDunSYqkkq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDNek%2B6M8Zkl6ryfO0CrcA8jrdEjAaMWCbGRUEzYY2ECDj0CXi1iQkV7KkhxSguZ7gveQa99XsgkL%2FaiAtae4P0hDmVSQn0peV9LK4h%2FXQIWluBkbgu%2FVNl8WMrMI3EHar2ByUgk7Hmy3T1Q3sbl091IecBsekws8kwqIUcI5HjDHXm%2Fg2AWujc86A2KGVkzS6hsGCueAOKTJ6OoOSwO6p3%2FpPxoRc0%2BV66s9enAUvVbbafe6kJs2CVuXuzYywHpLxBfmOO%2FuFwh8Z40UX9qNSuUUDOXCT%2B7cSDDwXnQqvDcZhjGscmFg7NLdhsKGlev%2BVLbuxGwjH6kxkbFX1GtVs0cUl%2FoIZ%2F99T3Hh7%2F%2F%2BYaaDpcdQK0xfJUuXVth6Rdhaw44%2BWbttUnW%2F%2FBskjOwOfm4KBQ60DUEVKvv%2BKil6xp1A%2FNsFuVYj%2BP9xV0EULZkv9sGggetfi1EvlXJFx6n9pzn39652VmUPEwENAymJrmSAtllSorc4fwyDosD%2FTFJGAVWv2ux42EbrYqr850WZ1VkmP5E8DfMUNfKOwUteyCw4o5VWKa1k1zTrClEeDQ9y2JIBy1spT3LUymt%2FOBh8b9nnd7YDy2pcEr6yt9y1VAdi6GHXu4j%2Fpl53BwW3%2FvhNl8k9J8G1UAG64SRyMKjv68oGOqUB%2BR4KK06WjtfDbeReTvoIvjwEFqDb%2FnTznuwCAnuoNYgAq0FR4f%2FEeETfiEXpX5TWv3Php86fIvb8yMWCPU7E0P1OCLH2zmaeOXWoGgSpcklKRWDtQ1stEsbP9njZzsIr1yvwU0RRoLwnLhPfP8XuvBw4Fz5FTl%2F7vWnRJthG2V%2BmTL9V9RSg7J%2BszxTBI2VY8aqHkVo9vEgjkmGlt5EOY2uxC6IS&X-Amz-Signature=cde08485cb627be7163d4c237c8085a372628217028ab9365ea57e722765b994&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYA66KGP%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCfM%2BRGRxr3XTA5sxWHhIa24vyYPhMWJd2BSgVhWBvndQIgO%2BTOodxplmREA2Ce3cBwZocaQSVdKbkXS3SDunSYqkkq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDNek%2B6M8Zkl6ryfO0CrcA8jrdEjAaMWCbGRUEzYY2ECDj0CXi1iQkV7KkhxSguZ7gveQa99XsgkL%2FaiAtae4P0hDmVSQn0peV9LK4h%2FXQIWluBkbgu%2FVNl8WMrMI3EHar2ByUgk7Hmy3T1Q3sbl091IecBsekws8kwqIUcI5HjDHXm%2Fg2AWujc86A2KGVkzS6hsGCueAOKTJ6OoOSwO6p3%2FpPxoRc0%2BV66s9enAUvVbbafe6kJs2CVuXuzYywHpLxBfmOO%2FuFwh8Z40UX9qNSuUUDOXCT%2B7cSDDwXnQqvDcZhjGscmFg7NLdhsKGlev%2BVLbuxGwjH6kxkbFX1GtVs0cUl%2FoIZ%2F99T3Hh7%2F%2F%2BYaaDpcdQK0xfJUuXVth6Rdhaw44%2BWbttUnW%2F%2FBskjOwOfm4KBQ60DUEVKvv%2BKil6xp1A%2FNsFuVYj%2BP9xV0EULZkv9sGggetfi1EvlXJFx6n9pzn39652VmUPEwENAymJrmSAtllSorc4fwyDosD%2FTFJGAVWv2ux42EbrYqr850WZ1VkmP5E8DfMUNfKOwUteyCw4o5VWKa1k1zTrClEeDQ9y2JIBy1spT3LUymt%2FOBh8b9nnd7YDy2pcEr6yt9y1VAdi6GHXu4j%2Fpl53BwW3%2FvhNl8k9J8G1UAG64SRyMKjv68oGOqUB%2BR4KK06WjtfDbeReTvoIvjwEFqDb%2FnTznuwCAnuoNYgAq0FR4f%2FEeETfiEXpX5TWv3Php86fIvb8yMWCPU7E0P1OCLH2zmaeOXWoGgSpcklKRWDtQ1stEsbP9njZzsIr1yvwU0RRoLwnLhPfP8XuvBw4Fz5FTl%2F7vWnRJthG2V%2BmTL9V9RSg7J%2BszxTBI2VY8aqHkVo9vEgjkmGlt5EOY2uxC6IS&X-Amz-Signature=5aed0de7879c5d4bcb7900ad5bf476ee572b2238945db581d20ad29ed1ae136e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

