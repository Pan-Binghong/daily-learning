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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNGVVAAE%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDcxZgqoF92SXTz1CKqk6wPWwhLPKQY3rEeivrG9XT%2FUAiBrzzT%2FQ62UYHZYQKfNoudmGOHikb3kks5%2FJJC4nqVrISr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMwyYzRlN1fa63zSLLKtwDclRpFIUOMgkS7DANEJbqitOOPKItcJg1J%2FafcDhTvlR2c3ik0wmFqCa0qQdBuxp56s%2FcXwTx%2BAHu32JGCCDoU1Ua3cWUMS4PLTNAD8BO%2FhMq%2FI0sY0iqNzkTRgKYvJNvo05txmqP9nUQMr7UuI6oP72bMZyMYx0HnyDoxVED6%2BMRBctngm4%2FIdjsmZC4U7iby%2BJhuezO108h6HMw3pNmmw%2FQ1ecpQN6P3od6S06sZpdQ51CgSd1N9zUgNysfyRaQXmPZgOBppOQmZz%2BUx07eBNuREdHBYstIcbpDyx5uadOOHeq%2B72tbKLeHIdatN2Nvvkelh1moV5QSAOoY6cGHypGwICzDqDauTNfMYuSy62YSMbGCm7dRFCgRDzx1oELYJtggk%2BfV7KHDuqpomPd%2FAfXBq4Jt%2F%2FpS5diJ6suNE2lDH0RvNr%2BD08QxFuw7tmSlojV%2FQgVNFdWfPSBjKgkb84EyEYzKLfOToL1IhD7AZZLNXBYqC6aQzKpDCuvqsyC5clxhXEBKoPrIDiKlwnwR3kFBt2aYZCRpVDPKgotNgjT4Rq29bL3Y0Nqlk26cZK4dmL1ejfYIlAeSfXZh4zoGAS8qK8ccjqM7MHigmVUb2PuY%2FrBZX%2FnyGf2iMZEwxK%2B3zgY6pgEhWv5lwv6D%2BIXva1oDUQq5KLKTYEQRYkFilbKsmJ1%2B3FlzOAGwKZ2eoCugXSZRlHaUxbDWibvMX0QzGQLLTWDnWpiMKwzrJk%2FMlOIuvU78AUOkYXlYyD9iSiVS3MWb6%2BPQmlYGPbae4Sk%2FOSZ4e%2BRPsWY2PUIl%2FLQ4H4y%2FNY3szUCA%2F9mEcbZeAbAKU8U3vQkDP2SM3zxLy7dRoLShKejksHrrinnE&X-Amz-Signature=64201203a62dd5013a801bc4d07b23b58948f032ca043a8db05fe1da20a36a2a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNGVVAAE%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDcxZgqoF92SXTz1CKqk6wPWwhLPKQY3rEeivrG9XT%2FUAiBrzzT%2FQ62UYHZYQKfNoudmGOHikb3kks5%2FJJC4nqVrISr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMwyYzRlN1fa63zSLLKtwDclRpFIUOMgkS7DANEJbqitOOPKItcJg1J%2FafcDhTvlR2c3ik0wmFqCa0qQdBuxp56s%2FcXwTx%2BAHu32JGCCDoU1Ua3cWUMS4PLTNAD8BO%2FhMq%2FI0sY0iqNzkTRgKYvJNvo05txmqP9nUQMr7UuI6oP72bMZyMYx0HnyDoxVED6%2BMRBctngm4%2FIdjsmZC4U7iby%2BJhuezO108h6HMw3pNmmw%2FQ1ecpQN6P3od6S06sZpdQ51CgSd1N9zUgNysfyRaQXmPZgOBppOQmZz%2BUx07eBNuREdHBYstIcbpDyx5uadOOHeq%2B72tbKLeHIdatN2Nvvkelh1moV5QSAOoY6cGHypGwICzDqDauTNfMYuSy62YSMbGCm7dRFCgRDzx1oELYJtggk%2BfV7KHDuqpomPd%2FAfXBq4Jt%2F%2FpS5diJ6suNE2lDH0RvNr%2BD08QxFuw7tmSlojV%2FQgVNFdWfPSBjKgkb84EyEYzKLfOToL1IhD7AZZLNXBYqC6aQzKpDCuvqsyC5clxhXEBKoPrIDiKlwnwR3kFBt2aYZCRpVDPKgotNgjT4Rq29bL3Y0Nqlk26cZK4dmL1ejfYIlAeSfXZh4zoGAS8qK8ccjqM7MHigmVUb2PuY%2FrBZX%2FnyGf2iMZEwxK%2B3zgY6pgEhWv5lwv6D%2BIXva1oDUQq5KLKTYEQRYkFilbKsmJ1%2B3FlzOAGwKZ2eoCugXSZRlHaUxbDWibvMX0QzGQLLTWDnWpiMKwzrJk%2FMlOIuvU78AUOkYXlYyD9iSiVS3MWb6%2BPQmlYGPbae4Sk%2FOSZ4e%2BRPsWY2PUIl%2FLQ4H4y%2FNY3szUCA%2F9mEcbZeAbAKU8U3vQkDP2SM3zxLy7dRoLShKejksHrrinnE&X-Amz-Signature=310b5e7a9e6ced0754f12a00d0bdb2b78ac65d274eb7d24f5a04358275c4589a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNGVVAAE%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDcxZgqoF92SXTz1CKqk6wPWwhLPKQY3rEeivrG9XT%2FUAiBrzzT%2FQ62UYHZYQKfNoudmGOHikb3kks5%2FJJC4nqVrISr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMwyYzRlN1fa63zSLLKtwDclRpFIUOMgkS7DANEJbqitOOPKItcJg1J%2FafcDhTvlR2c3ik0wmFqCa0qQdBuxp56s%2FcXwTx%2BAHu32JGCCDoU1Ua3cWUMS4PLTNAD8BO%2FhMq%2FI0sY0iqNzkTRgKYvJNvo05txmqP9nUQMr7UuI6oP72bMZyMYx0HnyDoxVED6%2BMRBctngm4%2FIdjsmZC4U7iby%2BJhuezO108h6HMw3pNmmw%2FQ1ecpQN6P3od6S06sZpdQ51CgSd1N9zUgNysfyRaQXmPZgOBppOQmZz%2BUx07eBNuREdHBYstIcbpDyx5uadOOHeq%2B72tbKLeHIdatN2Nvvkelh1moV5QSAOoY6cGHypGwICzDqDauTNfMYuSy62YSMbGCm7dRFCgRDzx1oELYJtggk%2BfV7KHDuqpomPd%2FAfXBq4Jt%2F%2FpS5diJ6suNE2lDH0RvNr%2BD08QxFuw7tmSlojV%2FQgVNFdWfPSBjKgkb84EyEYzKLfOToL1IhD7AZZLNXBYqC6aQzKpDCuvqsyC5clxhXEBKoPrIDiKlwnwR3kFBt2aYZCRpVDPKgotNgjT4Rq29bL3Y0Nqlk26cZK4dmL1ejfYIlAeSfXZh4zoGAS8qK8ccjqM7MHigmVUb2PuY%2FrBZX%2FnyGf2iMZEwxK%2B3zgY6pgEhWv5lwv6D%2BIXva1oDUQq5KLKTYEQRYkFilbKsmJ1%2B3FlzOAGwKZ2eoCugXSZRlHaUxbDWibvMX0QzGQLLTWDnWpiMKwzrJk%2FMlOIuvU78AUOkYXlYyD9iSiVS3MWb6%2BPQmlYGPbae4Sk%2FOSZ4e%2BRPsWY2PUIl%2FLQ4H4y%2FNY3szUCA%2F9mEcbZeAbAKU8U3vQkDP2SM3zxLy7dRoLShKejksHrrinnE&X-Amz-Signature=b4f04dea9d75abfbf78a4ec59ebd485e0c26aa97a4ccd5924b9d23d8d8c45bf5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

