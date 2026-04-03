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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WBDCGJD%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG1kyx9Oz10IM6wM6nZokF%2FNrTZas%2BVPxZGVF1u8vIq%2BAiAajb6cu4yjFvll8gwpw4uB1tbhV1SfFjsCh8zkjUQPFyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMGqp%2BIXEREdWubsW3KtwDpEyxTHmTriBrzsgx5N6SsajBpUHg0YA%2B60AU8RdUT7DV4277Dqianlf4Ytnt2hPAsauS6jLC%2FaqM%2FHbp7fgxaHOmdMowQHLd6HhEdbxC44gjqv%2FW8FUH3KHcWQNqbOgmLi1GLY0TgtMYLRSghVWLNFb15BSXsDzd49atYRUr6ZLgxkf0WEQ2a1vgI%2B3c0dntQSysH5JAi8kSH%2B9RMS5A1EuXwieW34vbAuSnJlfFph9aukLr9hcSmJAABa63xPCvaWZZyHZ3qp5WWTHpIgwTXmPXyPl6AYDhXkjBq%2FW1Db53ywPk7UyRhcDCXYH%2FZ8Kur8iuRxQPwt9Nc93cLR1xu%2BghR61xYh8WAJnAwq1cSaJp7TRHSsquHnKBygJkE6Lyx13y99M3t9Rf%2BLOLf5yCDwF%2BjV6rdFcH9VOngMuWbGGUMiSZF1vkgjq2fhpL9mPShXXGU0dkHpLGlUjs1TC2BTR4iWXgU51bj2EsHTYhGwPAuI0GDzB1PP1QmqacPTe2PSihPki81135FZoQ4II9zCL2B1RbVTtra7ekslZw30rm%2BSZpHF%2Fr8N83Z2tZJqOT36W%2FONZ22R7a76XENfbxI4sH7Xmny5Z2Ul32TPCQE7YWtSW7JTbVF%2FTZgMswpK29zgY6pgGLL4XNmQvuk4OjehY14Rb%2BqQR81X8KleABD8EjTTL0EA0GX475geToYEqSscqdE5OyxnxELDXK89ML16IbREzoghiNBu5evJTAapR34eYEjEyGTi7nhI3foJhkcp8wFbmijntoG2v2tllndDxtRl2S3r7rdCLEu%2F2LpV0tUlpTVj5Wb9XCOVaUAi4QQC7OOXBNT07Xkae57SOJq9NnEQDjZUXlsaQc&X-Amz-Signature=582cf44d9592d80f65a3736bd6e8c123ae39384332642828912cabeeb6b00045&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WBDCGJD%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG1kyx9Oz10IM6wM6nZokF%2FNrTZas%2BVPxZGVF1u8vIq%2BAiAajb6cu4yjFvll8gwpw4uB1tbhV1SfFjsCh8zkjUQPFyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMGqp%2BIXEREdWubsW3KtwDpEyxTHmTriBrzsgx5N6SsajBpUHg0YA%2B60AU8RdUT7DV4277Dqianlf4Ytnt2hPAsauS6jLC%2FaqM%2FHbp7fgxaHOmdMowQHLd6HhEdbxC44gjqv%2FW8FUH3KHcWQNqbOgmLi1GLY0TgtMYLRSghVWLNFb15BSXsDzd49atYRUr6ZLgxkf0WEQ2a1vgI%2B3c0dntQSysH5JAi8kSH%2B9RMS5A1EuXwieW34vbAuSnJlfFph9aukLr9hcSmJAABa63xPCvaWZZyHZ3qp5WWTHpIgwTXmPXyPl6AYDhXkjBq%2FW1Db53ywPk7UyRhcDCXYH%2FZ8Kur8iuRxQPwt9Nc93cLR1xu%2BghR61xYh8WAJnAwq1cSaJp7TRHSsquHnKBygJkE6Lyx13y99M3t9Rf%2BLOLf5yCDwF%2BjV6rdFcH9VOngMuWbGGUMiSZF1vkgjq2fhpL9mPShXXGU0dkHpLGlUjs1TC2BTR4iWXgU51bj2EsHTYhGwPAuI0GDzB1PP1QmqacPTe2PSihPki81135FZoQ4II9zCL2B1RbVTtra7ekslZw30rm%2BSZpHF%2Fr8N83Z2tZJqOT36W%2FONZ22R7a76XENfbxI4sH7Xmny5Z2Ul32TPCQE7YWtSW7JTbVF%2FTZgMswpK29zgY6pgGLL4XNmQvuk4OjehY14Rb%2BqQR81X8KleABD8EjTTL0EA0GX475geToYEqSscqdE5OyxnxELDXK89ML16IbREzoghiNBu5evJTAapR34eYEjEyGTi7nhI3foJhkcp8wFbmijntoG2v2tllndDxtRl2S3r7rdCLEu%2F2LpV0tUlpTVj5Wb9XCOVaUAi4QQC7OOXBNT07Xkae57SOJq9NnEQDjZUXlsaQc&X-Amz-Signature=0c8a05b4ad737e86e3fc9fa53d9f16591603971fd8246f16883e163cd9b8f8dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WBDCGJD%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG1kyx9Oz10IM6wM6nZokF%2FNrTZas%2BVPxZGVF1u8vIq%2BAiAajb6cu4yjFvll8gwpw4uB1tbhV1SfFjsCh8zkjUQPFyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMGqp%2BIXEREdWubsW3KtwDpEyxTHmTriBrzsgx5N6SsajBpUHg0YA%2B60AU8RdUT7DV4277Dqianlf4Ytnt2hPAsauS6jLC%2FaqM%2FHbp7fgxaHOmdMowQHLd6HhEdbxC44gjqv%2FW8FUH3KHcWQNqbOgmLi1GLY0TgtMYLRSghVWLNFb15BSXsDzd49atYRUr6ZLgxkf0WEQ2a1vgI%2B3c0dntQSysH5JAi8kSH%2B9RMS5A1EuXwieW34vbAuSnJlfFph9aukLr9hcSmJAABa63xPCvaWZZyHZ3qp5WWTHpIgwTXmPXyPl6AYDhXkjBq%2FW1Db53ywPk7UyRhcDCXYH%2FZ8Kur8iuRxQPwt9Nc93cLR1xu%2BghR61xYh8WAJnAwq1cSaJp7TRHSsquHnKBygJkE6Lyx13y99M3t9Rf%2BLOLf5yCDwF%2BjV6rdFcH9VOngMuWbGGUMiSZF1vkgjq2fhpL9mPShXXGU0dkHpLGlUjs1TC2BTR4iWXgU51bj2EsHTYhGwPAuI0GDzB1PP1QmqacPTe2PSihPki81135FZoQ4II9zCL2B1RbVTtra7ekslZw30rm%2BSZpHF%2Fr8N83Z2tZJqOT36W%2FONZ22R7a76XENfbxI4sH7Xmny5Z2Ul32TPCQE7YWtSW7JTbVF%2FTZgMswpK29zgY6pgGLL4XNmQvuk4OjehY14Rb%2BqQR81X8KleABD8EjTTL0EA0GX475geToYEqSscqdE5OyxnxELDXK89ML16IbREzoghiNBu5evJTAapR34eYEjEyGTi7nhI3foJhkcp8wFbmijntoG2v2tllndDxtRl2S3r7rdCLEu%2F2LpV0tUlpTVj5Wb9XCOVaUAi4QQC7OOXBNT07Xkae57SOJq9NnEQDjZUXlsaQc&X-Amz-Signature=12dac103ce8e095c162d2f16157fc9dfaee31d123f7a02d526b86c8241bb9bd2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

