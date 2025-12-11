---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPB2DGYX%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIBQxbxKb%2BzAgHMFIplOsh1NU5ZJESWe%2FGuhUEGhyX0MmAiA7zCbXo6%2FPLlBDaTSIwha2M%2B4U%2BgHyPd6wt69Q2znapiqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIML50kuyqFxdEQ5i9RKtwDs7KBPAEMO20IIzYgvJeBQGYErPN5NT4BDnGctQPEj5EcxKL384jXww4tR97Mx8i2M9broBWMgLBb3GYUMcaFYd8%2FUub23r%2Fe9FQa1f6FVR0i3nJzqcIAIdu0z2Ua6g5JLON4ZYuqYn6Hqv4LFFeE0b2%2FfOwkOfaweUUNSVbil91vybb8GXC0ny7MZtVHkJ47wB7oYe5OEn9wBsdG%2Foz5w2TAV%2Fn%2FWWLo8nUXCi7cWphAu%2BDV%2B1qJ4EsBM18WOqdCmmARgFUVnKjxDHiy5c0%2BfYTgnOH%2F7z7QxG%2FBhMjYyWkXpfyR621s202VzcrF6P1K5FEywrikCRWEOEqAnOwsl0opmHGup8n7ROiWCCQr1rn9d9QX3KKWPaYU7LPT0j2x7S3CmWF87St76tpmGS32x3m9u9WrTb477EvTdQyYHL9sOwuX7A23MomfH8X6Uv0yaiJA4gPhpR0HTpn4UT9veoYY1E8Ni1xtSQidndF3Ya8KFhn2NyOU9mBpjpBOAKcU%2FTMIPJCFNqKjol0lKOxZXMUy%2BEO9zuog1aeYqptU9Kf4Kz40KbfQc675t1zslfAe1jLHrszFbQRYhMOIlvptwGg8%2FVeCSTsJfOAjP8UXYcAJOuqwPLU2c22jDa0w%2B7XoyQY6pgEwfLMcY4I9Y7ZEYoFv8%2FmgOrmNsZANtkPWDj%2BtQztnG4f9pIVweojTvMG3kapYZFhNqFZcVWO7n7DKR7lus3ZK%2BcH6RbCiofZ7y9nsA3uT%2BgjkRiQP5BdMNr1NwzUFXADqudLrGJagxTGZo0EDafHvJRS%2F6UD6HtqWUcYc0kKgoCuLLa59xHuiHv8QDE7%2BCn6LtsHC%2FfR11E4dNEb5QHMGSlKsoL3V&X-Amz-Signature=ea203da2b1c797300eb172fe42e726bd8619a3505dc27f942cc0727acfd2c77f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPB2DGYX%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIBQxbxKb%2BzAgHMFIplOsh1NU5ZJESWe%2FGuhUEGhyX0MmAiA7zCbXo6%2FPLlBDaTSIwha2M%2B4U%2BgHyPd6wt69Q2znapiqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIML50kuyqFxdEQ5i9RKtwDs7KBPAEMO20IIzYgvJeBQGYErPN5NT4BDnGctQPEj5EcxKL384jXww4tR97Mx8i2M9broBWMgLBb3GYUMcaFYd8%2FUub23r%2Fe9FQa1f6FVR0i3nJzqcIAIdu0z2Ua6g5JLON4ZYuqYn6Hqv4LFFeE0b2%2FfOwkOfaweUUNSVbil91vybb8GXC0ny7MZtVHkJ47wB7oYe5OEn9wBsdG%2Foz5w2TAV%2Fn%2FWWLo8nUXCi7cWphAu%2BDV%2B1qJ4EsBM18WOqdCmmARgFUVnKjxDHiy5c0%2BfYTgnOH%2F7z7QxG%2FBhMjYyWkXpfyR621s202VzcrF6P1K5FEywrikCRWEOEqAnOwsl0opmHGup8n7ROiWCCQr1rn9d9QX3KKWPaYU7LPT0j2x7S3CmWF87St76tpmGS32x3m9u9WrTb477EvTdQyYHL9sOwuX7A23MomfH8X6Uv0yaiJA4gPhpR0HTpn4UT9veoYY1E8Ni1xtSQidndF3Ya8KFhn2NyOU9mBpjpBOAKcU%2FTMIPJCFNqKjol0lKOxZXMUy%2BEO9zuog1aeYqptU9Kf4Kz40KbfQc675t1zslfAe1jLHrszFbQRYhMOIlvptwGg8%2FVeCSTsJfOAjP8UXYcAJOuqwPLU2c22jDa0w%2B7XoyQY6pgEwfLMcY4I9Y7ZEYoFv8%2FmgOrmNsZANtkPWDj%2BtQztnG4f9pIVweojTvMG3kapYZFhNqFZcVWO7n7DKR7lus3ZK%2BcH6RbCiofZ7y9nsA3uT%2BgjkRiQP5BdMNr1NwzUFXADqudLrGJagxTGZo0EDafHvJRS%2F6UD6HtqWUcYc0kKgoCuLLa59xHuiHv8QDE7%2BCn6LtsHC%2FfR11E4dNEb5QHMGSlKsoL3V&X-Amz-Signature=bb00024ce1034f21e27b0f5322b6ed71f32d20a1d9c7ad49cadce79cff6b2d3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPB2DGYX%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIBQxbxKb%2BzAgHMFIplOsh1NU5ZJESWe%2FGuhUEGhyX0MmAiA7zCbXo6%2FPLlBDaTSIwha2M%2B4U%2BgHyPd6wt69Q2znapiqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIML50kuyqFxdEQ5i9RKtwDs7KBPAEMO20IIzYgvJeBQGYErPN5NT4BDnGctQPEj5EcxKL384jXww4tR97Mx8i2M9broBWMgLBb3GYUMcaFYd8%2FUub23r%2Fe9FQa1f6FVR0i3nJzqcIAIdu0z2Ua6g5JLON4ZYuqYn6Hqv4LFFeE0b2%2FfOwkOfaweUUNSVbil91vybb8GXC0ny7MZtVHkJ47wB7oYe5OEn9wBsdG%2Foz5w2TAV%2Fn%2FWWLo8nUXCi7cWphAu%2BDV%2B1qJ4EsBM18WOqdCmmARgFUVnKjxDHiy5c0%2BfYTgnOH%2F7z7QxG%2FBhMjYyWkXpfyR621s202VzcrF6P1K5FEywrikCRWEOEqAnOwsl0opmHGup8n7ROiWCCQr1rn9d9QX3KKWPaYU7LPT0j2x7S3CmWF87St76tpmGS32x3m9u9WrTb477EvTdQyYHL9sOwuX7A23MomfH8X6Uv0yaiJA4gPhpR0HTpn4UT9veoYY1E8Ni1xtSQidndF3Ya8KFhn2NyOU9mBpjpBOAKcU%2FTMIPJCFNqKjol0lKOxZXMUy%2BEO9zuog1aeYqptU9Kf4Kz40KbfQc675t1zslfAe1jLHrszFbQRYhMOIlvptwGg8%2FVeCSTsJfOAjP8UXYcAJOuqwPLU2c22jDa0w%2B7XoyQY6pgEwfLMcY4I9Y7ZEYoFv8%2FmgOrmNsZANtkPWDj%2BtQztnG4f9pIVweojTvMG3kapYZFhNqFZcVWO7n7DKR7lus3ZK%2BcH6RbCiofZ7y9nsA3uT%2BgjkRiQP5BdMNr1NwzUFXADqudLrGJagxTGZo0EDafHvJRS%2F6UD6HtqWUcYc0kKgoCuLLa59xHuiHv8QDE7%2BCn6LtsHC%2FfR11E4dNEb5QHMGSlKsoL3V&X-Amz-Signature=d1b86db1ae5ec5cb927aa5414b8c4699cc2e18cd53a549e9204c25aa11a687b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

