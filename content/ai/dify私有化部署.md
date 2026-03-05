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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3QXU3DG%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9E6fkwWal%2FsnTe%2Frm35PfYiu27ip1Sn4sCcrMLFSAtAiAZ21FcOaGQ6zRF4mhfMl1ODOT9%2F5LLaYvn7LMg7d8ByCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDwIT3j5qKLFpDCuFKtwDCasOzjoF3DfrEQsljLMG%2F6Rn9LscpC1mK0vKQ%2F%2BLY3Tz7rXRZePo4EOtTk0uEr%2B5r%2FmPKa9csBgMjG4p7%2B5aciRlP%2BbACqLQPmqkhzQxqHrNmOMmuqjLKoTBnagtBwa1Z8Irs0K9q%2BubHPBSHULWCFH5q0GxtICnITZHY4zFpBU595gfXfrkzdmt6LFP6h9zCPTLOdK8zuoC669ThxGUMkavOzxJ%2BNnNrBjfNrLKox5A1w4UEygYBM6gUvcj%2F%2FVdNy6eK8El0uJzn5%2FcjuusOSRuDSYWCRFDddnXdKqZT6CDOvPAQwdOOlU3S7%2FwhU4LF1%2BfHPjfS6NPhV%2F6dnd5yJxAWczh8BnzD0FpA8L244N0gCJKjaNOl1tJWbTNsx9TjiJ0SZsTYckWEV57p4ryjUNiZo987ytMwijnPSGuQkTBEiGZngP8bgYiyctxbUb9MPEIPzMBQACyMYMf%2BPRXGg4slAavYLtQefZ%2FdeZr3lvXwImIw3rSnBSb0P3AoKH4e6bRHu8T4QUYfUPFI2I7qM8KGzVDvTunmHZRfvm4MrmEO3VefIoJHjKjZXun5dZWTWcEvLMOL4obnzVKulhwbEJlGCMTYPatU8QJSbqwEWi0SrRzn4RcfYBmPT4wk9%2BjzQY6pgGl369M5hChwE9aBnsEx9lWhL9uzlLwpTQCGg%2BF%2FuWWkCFXjNB8JH5tDOgaPnVi0hVLd0Pg%2BHfSD0tqljPv6gZLM3L2tK224MJHHY4MLZ9ESjPegBfQkSi6fNxxNQcHW5Pi2kFkJ3Wcn5kp6%2FInmhBOtxobecCPHnIZcG%2FNugjCxc765z2xekQqi6Ie%2FX7vFiq5sxHHOqJalnVdWLsEPJG7Ok3BvO6b&X-Amz-Signature=560595bcd441605f568f565b174a75e2904c42dd3740d0d3e7ee80b8dace4a88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3QXU3DG%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9E6fkwWal%2FsnTe%2Frm35PfYiu27ip1Sn4sCcrMLFSAtAiAZ21FcOaGQ6zRF4mhfMl1ODOT9%2F5LLaYvn7LMg7d8ByCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDwIT3j5qKLFpDCuFKtwDCasOzjoF3DfrEQsljLMG%2F6Rn9LscpC1mK0vKQ%2F%2BLY3Tz7rXRZePo4EOtTk0uEr%2B5r%2FmPKa9csBgMjG4p7%2B5aciRlP%2BbACqLQPmqkhzQxqHrNmOMmuqjLKoTBnagtBwa1Z8Irs0K9q%2BubHPBSHULWCFH5q0GxtICnITZHY4zFpBU595gfXfrkzdmt6LFP6h9zCPTLOdK8zuoC669ThxGUMkavOzxJ%2BNnNrBjfNrLKox5A1w4UEygYBM6gUvcj%2F%2FVdNy6eK8El0uJzn5%2FcjuusOSRuDSYWCRFDddnXdKqZT6CDOvPAQwdOOlU3S7%2FwhU4LF1%2BfHPjfS6NPhV%2F6dnd5yJxAWczh8BnzD0FpA8L244N0gCJKjaNOl1tJWbTNsx9TjiJ0SZsTYckWEV57p4ryjUNiZo987ytMwijnPSGuQkTBEiGZngP8bgYiyctxbUb9MPEIPzMBQACyMYMf%2BPRXGg4slAavYLtQefZ%2FdeZr3lvXwImIw3rSnBSb0P3AoKH4e6bRHu8T4QUYfUPFI2I7qM8KGzVDvTunmHZRfvm4MrmEO3VefIoJHjKjZXun5dZWTWcEvLMOL4obnzVKulhwbEJlGCMTYPatU8QJSbqwEWi0SrRzn4RcfYBmPT4wk9%2BjzQY6pgGl369M5hChwE9aBnsEx9lWhL9uzlLwpTQCGg%2BF%2FuWWkCFXjNB8JH5tDOgaPnVi0hVLd0Pg%2BHfSD0tqljPv6gZLM3L2tK224MJHHY4MLZ9ESjPegBfQkSi6fNxxNQcHW5Pi2kFkJ3Wcn5kp6%2FInmhBOtxobecCPHnIZcG%2FNugjCxc765z2xekQqi6Ie%2FX7vFiq5sxHHOqJalnVdWLsEPJG7Ok3BvO6b&X-Amz-Signature=159f9690611567765208a6d0fbef37ed13260398323fca59ac5fb2bd96d8a0dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3QXU3DG%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9E6fkwWal%2FsnTe%2Frm35PfYiu27ip1Sn4sCcrMLFSAtAiAZ21FcOaGQ6zRF4mhfMl1ODOT9%2F5LLaYvn7LMg7d8ByCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDwIT3j5qKLFpDCuFKtwDCasOzjoF3DfrEQsljLMG%2F6Rn9LscpC1mK0vKQ%2F%2BLY3Tz7rXRZePo4EOtTk0uEr%2B5r%2FmPKa9csBgMjG4p7%2B5aciRlP%2BbACqLQPmqkhzQxqHrNmOMmuqjLKoTBnagtBwa1Z8Irs0K9q%2BubHPBSHULWCFH5q0GxtICnITZHY4zFpBU595gfXfrkzdmt6LFP6h9zCPTLOdK8zuoC669ThxGUMkavOzxJ%2BNnNrBjfNrLKox5A1w4UEygYBM6gUvcj%2F%2FVdNy6eK8El0uJzn5%2FcjuusOSRuDSYWCRFDddnXdKqZT6CDOvPAQwdOOlU3S7%2FwhU4LF1%2BfHPjfS6NPhV%2F6dnd5yJxAWczh8BnzD0FpA8L244N0gCJKjaNOl1tJWbTNsx9TjiJ0SZsTYckWEV57p4ryjUNiZo987ytMwijnPSGuQkTBEiGZngP8bgYiyctxbUb9MPEIPzMBQACyMYMf%2BPRXGg4slAavYLtQefZ%2FdeZr3lvXwImIw3rSnBSb0P3AoKH4e6bRHu8T4QUYfUPFI2I7qM8KGzVDvTunmHZRfvm4MrmEO3VefIoJHjKjZXun5dZWTWcEvLMOL4obnzVKulhwbEJlGCMTYPatU8QJSbqwEWi0SrRzn4RcfYBmPT4wk9%2BjzQY6pgGl369M5hChwE9aBnsEx9lWhL9uzlLwpTQCGg%2BF%2FuWWkCFXjNB8JH5tDOgaPnVi0hVLd0Pg%2BHfSD0tqljPv6gZLM3L2tK224MJHHY4MLZ9ESjPegBfQkSi6fNxxNQcHW5Pi2kFkJ3Wcn5kp6%2FInmhBOtxobecCPHnIZcG%2FNugjCxc765z2xekQqi6Ie%2FX7vFiq5sxHHOqJalnVdWLsEPJG7Ok3BvO6b&X-Amz-Signature=76f4469ed2e1310a5412c192ce0fd9182b01cfc692320a325c506964a5c8a366&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3QXU3DG%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9E6fkwWal%2FsnTe%2Frm35PfYiu27ip1Sn4sCcrMLFSAtAiAZ21FcOaGQ6zRF4mhfMl1ODOT9%2F5LLaYvn7LMg7d8ByCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDwIT3j5qKLFpDCuFKtwDCasOzjoF3DfrEQsljLMG%2F6Rn9LscpC1mK0vKQ%2F%2BLY3Tz7rXRZePo4EOtTk0uEr%2B5r%2FmPKa9csBgMjG4p7%2B5aciRlP%2BbACqLQPmqkhzQxqHrNmOMmuqjLKoTBnagtBwa1Z8Irs0K9q%2BubHPBSHULWCFH5q0GxtICnITZHY4zFpBU595gfXfrkzdmt6LFP6h9zCPTLOdK8zuoC669ThxGUMkavOzxJ%2BNnNrBjfNrLKox5A1w4UEygYBM6gUvcj%2F%2FVdNy6eK8El0uJzn5%2FcjuusOSRuDSYWCRFDddnXdKqZT6CDOvPAQwdOOlU3S7%2FwhU4LF1%2BfHPjfS6NPhV%2F6dnd5yJxAWczh8BnzD0FpA8L244N0gCJKjaNOl1tJWbTNsx9TjiJ0SZsTYckWEV57p4ryjUNiZo987ytMwijnPSGuQkTBEiGZngP8bgYiyctxbUb9MPEIPzMBQACyMYMf%2BPRXGg4slAavYLtQefZ%2FdeZr3lvXwImIw3rSnBSb0P3AoKH4e6bRHu8T4QUYfUPFI2I7qM8KGzVDvTunmHZRfvm4MrmEO3VefIoJHjKjZXun5dZWTWcEvLMOL4obnzVKulhwbEJlGCMTYPatU8QJSbqwEWi0SrRzn4RcfYBmPT4wk9%2BjzQY6pgGl369M5hChwE9aBnsEx9lWhL9uzlLwpTQCGg%2BF%2FuWWkCFXjNB8JH5tDOgaPnVi0hVLd0Pg%2BHfSD0tqljPv6gZLM3L2tK224MJHHY4MLZ9ESjPegBfQkSi6fNxxNQcHW5Pi2kFkJ3Wcn5kp6%2FInmhBOtxobecCPHnIZcG%2FNugjCxc765z2xekQqi6Ie%2FX7vFiq5sxHHOqJalnVdWLsEPJG7Ok3BvO6b&X-Amz-Signature=f8ae25d71d7bce00760ccc077b420551cf44da308f6ef1bfa2df72f21ce42d72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3QXU3DG%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9E6fkwWal%2FsnTe%2Frm35PfYiu27ip1Sn4sCcrMLFSAtAiAZ21FcOaGQ6zRF4mhfMl1ODOT9%2F5LLaYvn7LMg7d8ByCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDwIT3j5qKLFpDCuFKtwDCasOzjoF3DfrEQsljLMG%2F6Rn9LscpC1mK0vKQ%2F%2BLY3Tz7rXRZePo4EOtTk0uEr%2B5r%2FmPKa9csBgMjG4p7%2B5aciRlP%2BbACqLQPmqkhzQxqHrNmOMmuqjLKoTBnagtBwa1Z8Irs0K9q%2BubHPBSHULWCFH5q0GxtICnITZHY4zFpBU595gfXfrkzdmt6LFP6h9zCPTLOdK8zuoC669ThxGUMkavOzxJ%2BNnNrBjfNrLKox5A1w4UEygYBM6gUvcj%2F%2FVdNy6eK8El0uJzn5%2FcjuusOSRuDSYWCRFDddnXdKqZT6CDOvPAQwdOOlU3S7%2FwhU4LF1%2BfHPjfS6NPhV%2F6dnd5yJxAWczh8BnzD0FpA8L244N0gCJKjaNOl1tJWbTNsx9TjiJ0SZsTYckWEV57p4ryjUNiZo987ytMwijnPSGuQkTBEiGZngP8bgYiyctxbUb9MPEIPzMBQACyMYMf%2BPRXGg4slAavYLtQefZ%2FdeZr3lvXwImIw3rSnBSb0P3AoKH4e6bRHu8T4QUYfUPFI2I7qM8KGzVDvTunmHZRfvm4MrmEO3VefIoJHjKjZXun5dZWTWcEvLMOL4obnzVKulhwbEJlGCMTYPatU8QJSbqwEWi0SrRzn4RcfYBmPT4wk9%2BjzQY6pgGl369M5hChwE9aBnsEx9lWhL9uzlLwpTQCGg%2BF%2FuWWkCFXjNB8JH5tDOgaPnVi0hVLd0Pg%2BHfSD0tqljPv6gZLM3L2tK224MJHHY4MLZ9ESjPegBfQkSi6fNxxNQcHW5Pi2kFkJ3Wcn5kp6%2FInmhBOtxobecCPHnIZcG%2FNugjCxc765z2xekQqi6Ie%2FX7vFiq5sxHHOqJalnVdWLsEPJG7Ok3BvO6b&X-Amz-Signature=0b9b9b0df326f2fb68b3e15b650df61cced00a85ea81df65f4985b88eaea5092&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3QXU3DG%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9E6fkwWal%2FsnTe%2Frm35PfYiu27ip1Sn4sCcrMLFSAtAiAZ21FcOaGQ6zRF4mhfMl1ODOT9%2F5LLaYvn7LMg7d8ByCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDwIT3j5qKLFpDCuFKtwDCasOzjoF3DfrEQsljLMG%2F6Rn9LscpC1mK0vKQ%2F%2BLY3Tz7rXRZePo4EOtTk0uEr%2B5r%2FmPKa9csBgMjG4p7%2B5aciRlP%2BbACqLQPmqkhzQxqHrNmOMmuqjLKoTBnagtBwa1Z8Irs0K9q%2BubHPBSHULWCFH5q0GxtICnITZHY4zFpBU595gfXfrkzdmt6LFP6h9zCPTLOdK8zuoC669ThxGUMkavOzxJ%2BNnNrBjfNrLKox5A1w4UEygYBM6gUvcj%2F%2FVdNy6eK8El0uJzn5%2FcjuusOSRuDSYWCRFDddnXdKqZT6CDOvPAQwdOOlU3S7%2FwhU4LF1%2BfHPjfS6NPhV%2F6dnd5yJxAWczh8BnzD0FpA8L244N0gCJKjaNOl1tJWbTNsx9TjiJ0SZsTYckWEV57p4ryjUNiZo987ytMwijnPSGuQkTBEiGZngP8bgYiyctxbUb9MPEIPzMBQACyMYMf%2BPRXGg4slAavYLtQefZ%2FdeZr3lvXwImIw3rSnBSb0P3AoKH4e6bRHu8T4QUYfUPFI2I7qM8KGzVDvTunmHZRfvm4MrmEO3VefIoJHjKjZXun5dZWTWcEvLMOL4obnzVKulhwbEJlGCMTYPatU8QJSbqwEWi0SrRzn4RcfYBmPT4wk9%2BjzQY6pgGl369M5hChwE9aBnsEx9lWhL9uzlLwpTQCGg%2BF%2FuWWkCFXjNB8JH5tDOgaPnVi0hVLd0Pg%2BHfSD0tqljPv6gZLM3L2tK224MJHHY4MLZ9ESjPegBfQkSi6fNxxNQcHW5Pi2kFkJ3Wcn5kp6%2FInmhBOtxobecCPHnIZcG%2FNugjCxc765z2xekQqi6Ie%2FX7vFiq5sxHHOqJalnVdWLsEPJG7Ok3BvO6b&X-Amz-Signature=b7a2d2888157949ff13b457c4b5496368af14d872970d771c3e3231861409295&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3QXU3DG%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9E6fkwWal%2FsnTe%2Frm35PfYiu27ip1Sn4sCcrMLFSAtAiAZ21FcOaGQ6zRF4mhfMl1ODOT9%2F5LLaYvn7LMg7d8ByCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDwIT3j5qKLFpDCuFKtwDCasOzjoF3DfrEQsljLMG%2F6Rn9LscpC1mK0vKQ%2F%2BLY3Tz7rXRZePo4EOtTk0uEr%2B5r%2FmPKa9csBgMjG4p7%2B5aciRlP%2BbACqLQPmqkhzQxqHrNmOMmuqjLKoTBnagtBwa1Z8Irs0K9q%2BubHPBSHULWCFH5q0GxtICnITZHY4zFpBU595gfXfrkzdmt6LFP6h9zCPTLOdK8zuoC669ThxGUMkavOzxJ%2BNnNrBjfNrLKox5A1w4UEygYBM6gUvcj%2F%2FVdNy6eK8El0uJzn5%2FcjuusOSRuDSYWCRFDddnXdKqZT6CDOvPAQwdOOlU3S7%2FwhU4LF1%2BfHPjfS6NPhV%2F6dnd5yJxAWczh8BnzD0FpA8L244N0gCJKjaNOl1tJWbTNsx9TjiJ0SZsTYckWEV57p4ryjUNiZo987ytMwijnPSGuQkTBEiGZngP8bgYiyctxbUb9MPEIPzMBQACyMYMf%2BPRXGg4slAavYLtQefZ%2FdeZr3lvXwImIw3rSnBSb0P3AoKH4e6bRHu8T4QUYfUPFI2I7qM8KGzVDvTunmHZRfvm4MrmEO3VefIoJHjKjZXun5dZWTWcEvLMOL4obnzVKulhwbEJlGCMTYPatU8QJSbqwEWi0SrRzn4RcfYBmPT4wk9%2BjzQY6pgGl369M5hChwE9aBnsEx9lWhL9uzlLwpTQCGg%2BF%2FuWWkCFXjNB8JH5tDOgaPnVi0hVLd0Pg%2BHfSD0tqljPv6gZLM3L2tK224MJHHY4MLZ9ESjPegBfQkSi6fNxxNQcHW5Pi2kFkJ3Wcn5kp6%2FInmhBOtxobecCPHnIZcG%2FNugjCxc765z2xekQqi6Ie%2FX7vFiq5sxHHOqJalnVdWLsEPJG7Ok3BvO6b&X-Amz-Signature=66677349d32f6d750b240b3705bf6e9c5983a7b794a60a485b6fef81f4e25022&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3QXU3DG%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9E6fkwWal%2FsnTe%2Frm35PfYiu27ip1Sn4sCcrMLFSAtAiAZ21FcOaGQ6zRF4mhfMl1ODOT9%2F5LLaYvn7LMg7d8ByCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDwIT3j5qKLFpDCuFKtwDCasOzjoF3DfrEQsljLMG%2F6Rn9LscpC1mK0vKQ%2F%2BLY3Tz7rXRZePo4EOtTk0uEr%2B5r%2FmPKa9csBgMjG4p7%2B5aciRlP%2BbACqLQPmqkhzQxqHrNmOMmuqjLKoTBnagtBwa1Z8Irs0K9q%2BubHPBSHULWCFH5q0GxtICnITZHY4zFpBU595gfXfrkzdmt6LFP6h9zCPTLOdK8zuoC669ThxGUMkavOzxJ%2BNnNrBjfNrLKox5A1w4UEygYBM6gUvcj%2F%2FVdNy6eK8El0uJzn5%2FcjuusOSRuDSYWCRFDddnXdKqZT6CDOvPAQwdOOlU3S7%2FwhU4LF1%2BfHPjfS6NPhV%2F6dnd5yJxAWczh8BnzD0FpA8L244N0gCJKjaNOl1tJWbTNsx9TjiJ0SZsTYckWEV57p4ryjUNiZo987ytMwijnPSGuQkTBEiGZngP8bgYiyctxbUb9MPEIPzMBQACyMYMf%2BPRXGg4slAavYLtQefZ%2FdeZr3lvXwImIw3rSnBSb0P3AoKH4e6bRHu8T4QUYfUPFI2I7qM8KGzVDvTunmHZRfvm4MrmEO3VefIoJHjKjZXun5dZWTWcEvLMOL4obnzVKulhwbEJlGCMTYPatU8QJSbqwEWi0SrRzn4RcfYBmPT4wk9%2BjzQY6pgGl369M5hChwE9aBnsEx9lWhL9uzlLwpTQCGg%2BF%2FuWWkCFXjNB8JH5tDOgaPnVi0hVLd0Pg%2BHfSD0tqljPv6gZLM3L2tK224MJHHY4MLZ9ESjPegBfQkSi6fNxxNQcHW5Pi2kFkJ3Wcn5kp6%2FInmhBOtxobecCPHnIZcG%2FNugjCxc765z2xekQqi6Ie%2FX7vFiq5sxHHOqJalnVdWLsEPJG7Ok3BvO6b&X-Amz-Signature=7eb088c4c6648d6865fccc522fce3a851570047f107a3be174c166d0f556d106&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3QXU3DG%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9E6fkwWal%2FsnTe%2Frm35PfYiu27ip1Sn4sCcrMLFSAtAiAZ21FcOaGQ6zRF4mhfMl1ODOT9%2F5LLaYvn7LMg7d8ByCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDwIT3j5qKLFpDCuFKtwDCasOzjoF3DfrEQsljLMG%2F6Rn9LscpC1mK0vKQ%2F%2BLY3Tz7rXRZePo4EOtTk0uEr%2B5r%2FmPKa9csBgMjG4p7%2B5aciRlP%2BbACqLQPmqkhzQxqHrNmOMmuqjLKoTBnagtBwa1Z8Irs0K9q%2BubHPBSHULWCFH5q0GxtICnITZHY4zFpBU595gfXfrkzdmt6LFP6h9zCPTLOdK8zuoC669ThxGUMkavOzxJ%2BNnNrBjfNrLKox5A1w4UEygYBM6gUvcj%2F%2FVdNy6eK8El0uJzn5%2FcjuusOSRuDSYWCRFDddnXdKqZT6CDOvPAQwdOOlU3S7%2FwhU4LF1%2BfHPjfS6NPhV%2F6dnd5yJxAWczh8BnzD0FpA8L244N0gCJKjaNOl1tJWbTNsx9TjiJ0SZsTYckWEV57p4ryjUNiZo987ytMwijnPSGuQkTBEiGZngP8bgYiyctxbUb9MPEIPzMBQACyMYMf%2BPRXGg4slAavYLtQefZ%2FdeZr3lvXwImIw3rSnBSb0P3AoKH4e6bRHu8T4QUYfUPFI2I7qM8KGzVDvTunmHZRfvm4MrmEO3VefIoJHjKjZXun5dZWTWcEvLMOL4obnzVKulhwbEJlGCMTYPatU8QJSbqwEWi0SrRzn4RcfYBmPT4wk9%2BjzQY6pgGl369M5hChwE9aBnsEx9lWhL9uzlLwpTQCGg%2BF%2FuWWkCFXjNB8JH5tDOgaPnVi0hVLd0Pg%2BHfSD0tqljPv6gZLM3L2tK224MJHHY4MLZ9ESjPegBfQkSi6fNxxNQcHW5Pi2kFkJ3Wcn5kp6%2FInmhBOtxobecCPHnIZcG%2FNugjCxc765z2xekQqi6Ie%2FX7vFiq5sxHHOqJalnVdWLsEPJG7Ok3BvO6b&X-Amz-Signature=b9b584acb995d7f8f506331ffa8712c9e4fb03b8bfda38d8fbe1963c37c6df60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3QXU3DG%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9E6fkwWal%2FsnTe%2Frm35PfYiu27ip1Sn4sCcrMLFSAtAiAZ21FcOaGQ6zRF4mhfMl1ODOT9%2F5LLaYvn7LMg7d8ByCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDwIT3j5qKLFpDCuFKtwDCasOzjoF3DfrEQsljLMG%2F6Rn9LscpC1mK0vKQ%2F%2BLY3Tz7rXRZePo4EOtTk0uEr%2B5r%2FmPKa9csBgMjG4p7%2B5aciRlP%2BbACqLQPmqkhzQxqHrNmOMmuqjLKoTBnagtBwa1Z8Irs0K9q%2BubHPBSHULWCFH5q0GxtICnITZHY4zFpBU595gfXfrkzdmt6LFP6h9zCPTLOdK8zuoC669ThxGUMkavOzxJ%2BNnNrBjfNrLKox5A1w4UEygYBM6gUvcj%2F%2FVdNy6eK8El0uJzn5%2FcjuusOSRuDSYWCRFDddnXdKqZT6CDOvPAQwdOOlU3S7%2FwhU4LF1%2BfHPjfS6NPhV%2F6dnd5yJxAWczh8BnzD0FpA8L244N0gCJKjaNOl1tJWbTNsx9TjiJ0SZsTYckWEV57p4ryjUNiZo987ytMwijnPSGuQkTBEiGZngP8bgYiyctxbUb9MPEIPzMBQACyMYMf%2BPRXGg4slAavYLtQefZ%2FdeZr3lvXwImIw3rSnBSb0P3AoKH4e6bRHu8T4QUYfUPFI2I7qM8KGzVDvTunmHZRfvm4MrmEO3VefIoJHjKjZXun5dZWTWcEvLMOL4obnzVKulhwbEJlGCMTYPatU8QJSbqwEWi0SrRzn4RcfYBmPT4wk9%2BjzQY6pgGl369M5hChwE9aBnsEx9lWhL9uzlLwpTQCGg%2BF%2FuWWkCFXjNB8JH5tDOgaPnVi0hVLd0Pg%2BHfSD0tqljPv6gZLM3L2tK224MJHHY4MLZ9ESjPegBfQkSi6fNxxNQcHW5Pi2kFkJ3Wcn5kp6%2FInmhBOtxobecCPHnIZcG%2FNugjCxc765z2xekQqi6Ie%2FX7vFiq5sxHHOqJalnVdWLsEPJG7Ok3BvO6b&X-Amz-Signature=f017f1e85a727c8cb3d8cdfc27ea3cb8cb8751540fccec0a71b354638260ecf7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

