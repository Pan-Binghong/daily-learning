---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRETJBRY%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIFdmUdr0IB7vtLEtn9DdzgTrIVLU6CuJO%2BUk9tvbk%2BOZAiAqbmEudsV9AH72BcwW3mC8PpZkKXz5fFeOZhZBCvOBCSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYehGid5w6SYTnBR3KtwDTCnzPAYj6YUhcoS6MT2%2BBllgkCRbvmAJP72Vs1qaMqCOhfC2kWyT6yUoPEmnXew%2BrwotpJqHrAbpi4AFXocqXv4XMDWzEkWzy9sKinXQHYCoi1VH0dBEgpLhQzaUUOBzdyj36BNQaMCZTSS6qJYzsbdCtcFNtgT3h7kpBt43oYfNOJfBHLIHPxYxpcmMROafidIVEFzNITzDMdyh1kZjMA969D3ktMC%2FcvlmXBeYxbhpVivKKF1muR%2FPiJD0o1HtUiBuVfDp5RjdrtwDpcURo%2BCf80SFz504lsKPfVKQE4AKEDgZau22EEq5ue%2FekVo3TOA%2BA4I5ErysV4YOLuaG8jHOfWWnfmlkBeXool6Fv32ntrpQilX%2Bi7uwWrtblSBpyGwCjiii0wMzjHFpszRscqa8%2FRJfUmrr7pR9jc6pzOAviWIefy6vgJBSpLXjhSSxybZ55CvO1MEYhI8qzMU52Ft47%2F7NopSN9Ls7uqR90yax7TfhRsPLM0AIUn6eLC5Wo4BpaRi8IQcBpXRQnZ6xCmh5HDl4LaRPfhbie%2F7y%2FF8jnU134KRK8ArF5sLBoXpV3%2FBhztnGdMlXQcEVrToOXjoY5FT4%2BTIKJatVlalMTc15BfZU2K%2BBd9%2FiSmEwtsr0yAY6pgEPMvW%2Fpsk%2FKfH1m6YC8bNrARh0q%2Bq3e%2FxTg7NzN%2F2E3AUSpvWdro5RBni9OdXT9EEZVJup8F6cRsGDmoCMK3IJUh1x18uefmLDfagJFvoUjicF5HyS46b2XueLsZTRWbhIj%2BEMf3lEfwdG85CFk%2Bz08gg5e47JNj1R5dC3H1S0R1Psz2%2BERWcjBfnV%2Bh8N2EDJItJC66twvQ5Z50dn%2FmUDOugG6pTy&X-Amz-Signature=0a0f26c5e6d9ee85850b9a673336c499169da931faab42b4047b17bd42d8f3e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

