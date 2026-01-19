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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SG2SKRFW%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9kxsyJl1GBXQlWLkZfqN%2FYXWejwcZIlScBj1znDu7IQIgS79C2nK4G5baWBhtrhPSOd1MHjWyRAUd743XTz08hWsqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMeJGp%2FTEXnfDIZBSrcA0JAo%2BXnIRfHp3RvmXr557TXziauXDIFxrZL5%2Bp95HtEQCAnoOOmLQM9sgkrgeVHp6YjvXSbFITK5Zs2D8ZUVhKWDnESV9WHl%2BnEy7ffErajcFczbQf32WT0h9CnkqsVpZeiuknOaW9EXsQEk7a9KrQgR51VexrMrIPRFKYAXuQPwMBh2l%2F0jwsRwvqoLaYS5XrbKPjFQFnOReK8LeZgF4fS4fMMmmn%2BEwRAeMbRtOn1NzSx60YULooHz3mu1076KFdrZ%2FoGkw2wPJReuVVbCeBdScrlaWKKc06kyEoiUeeMztpPiwbptzpv1G8pZLQJ3uT9VQgP%2B6pSFqdWOJFN%2BfVefY95YUFH7R5NatQL36Zjnc83Z0SbDPi0M5X9lgRXeGddOCM7xBSC05z0Wwk%2FD317b2lk%2FkrwurW0xHnHVom8wmhmRpLWLV4SF799E%2BVD%2FfmH1xLwBHQ3KyeFcOAppQAewLjHBI6ZXqvKhZo5DT00sUhztoQy4rEXut1mQWSmc9074lPLu6V19I4%2FahF6tHXmt7tuBuI4rfDoA%2BZXuID%2F63y6zLtQ4gz%2Fg2G3qnmsAPu%2BPaPjSMF%2BID4vYOfDqt09w3QFObcPxZcPhgdXe5K8FZKBOlI8e8yu6HtJMKnctcsGOqUBlWBXZmQSQabFo%2F55RqsAE4OsylYQRFntBL6coStXcDKkwTJmDFYx%2FaQ7QeZaTy9M1lfAh%2BiU8xIK2x%2F0adV1wdoJUQtiPgc7x0UiD3zNlKBZCpLJUTQXqo0aOefUYciSX3ylJgvTKTnQ7s2oMX3eD%2F7o8klyELVakE9pxvb40e6oDTvaxmOT3%2FA4KYA532yR0UwX4mEK7EoOtOyxeuNqoSYYP3yS&X-Amz-Signature=09e8339741e7b27c2ee1b188902810e38948d36ac7fb8b22a76992cfc92c85dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SG2SKRFW%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9kxsyJl1GBXQlWLkZfqN%2FYXWejwcZIlScBj1znDu7IQIgS79C2nK4G5baWBhtrhPSOd1MHjWyRAUd743XTz08hWsqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMeJGp%2FTEXnfDIZBSrcA0JAo%2BXnIRfHp3RvmXr557TXziauXDIFxrZL5%2Bp95HtEQCAnoOOmLQM9sgkrgeVHp6YjvXSbFITK5Zs2D8ZUVhKWDnESV9WHl%2BnEy7ffErajcFczbQf32WT0h9CnkqsVpZeiuknOaW9EXsQEk7a9KrQgR51VexrMrIPRFKYAXuQPwMBh2l%2F0jwsRwvqoLaYS5XrbKPjFQFnOReK8LeZgF4fS4fMMmmn%2BEwRAeMbRtOn1NzSx60YULooHz3mu1076KFdrZ%2FoGkw2wPJReuVVbCeBdScrlaWKKc06kyEoiUeeMztpPiwbptzpv1G8pZLQJ3uT9VQgP%2B6pSFqdWOJFN%2BfVefY95YUFH7R5NatQL36Zjnc83Z0SbDPi0M5X9lgRXeGddOCM7xBSC05z0Wwk%2FD317b2lk%2FkrwurW0xHnHVom8wmhmRpLWLV4SF799E%2BVD%2FfmH1xLwBHQ3KyeFcOAppQAewLjHBI6ZXqvKhZo5DT00sUhztoQy4rEXut1mQWSmc9074lPLu6V19I4%2FahF6tHXmt7tuBuI4rfDoA%2BZXuID%2F63y6zLtQ4gz%2Fg2G3qnmsAPu%2BPaPjSMF%2BID4vYOfDqt09w3QFObcPxZcPhgdXe5K8FZKBOlI8e8yu6HtJMKnctcsGOqUBlWBXZmQSQabFo%2F55RqsAE4OsylYQRFntBL6coStXcDKkwTJmDFYx%2FaQ7QeZaTy9M1lfAh%2BiU8xIK2x%2F0adV1wdoJUQtiPgc7x0UiD3zNlKBZCpLJUTQXqo0aOefUYciSX3ylJgvTKTnQ7s2oMX3eD%2F7o8klyELVakE9pxvb40e6oDTvaxmOT3%2FA4KYA532yR0UwX4mEK7EoOtOyxeuNqoSYYP3yS&X-Amz-Signature=3f2124a7bf11371aff18432167be9fb910953920ec50efc60301cbe0bf03d439&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SG2SKRFW%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9kxsyJl1GBXQlWLkZfqN%2FYXWejwcZIlScBj1znDu7IQIgS79C2nK4G5baWBhtrhPSOd1MHjWyRAUd743XTz08hWsqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMeJGp%2FTEXnfDIZBSrcA0JAo%2BXnIRfHp3RvmXr557TXziauXDIFxrZL5%2Bp95HtEQCAnoOOmLQM9sgkrgeVHp6YjvXSbFITK5Zs2D8ZUVhKWDnESV9WHl%2BnEy7ffErajcFczbQf32WT0h9CnkqsVpZeiuknOaW9EXsQEk7a9KrQgR51VexrMrIPRFKYAXuQPwMBh2l%2F0jwsRwvqoLaYS5XrbKPjFQFnOReK8LeZgF4fS4fMMmmn%2BEwRAeMbRtOn1NzSx60YULooHz3mu1076KFdrZ%2FoGkw2wPJReuVVbCeBdScrlaWKKc06kyEoiUeeMztpPiwbptzpv1G8pZLQJ3uT9VQgP%2B6pSFqdWOJFN%2BfVefY95YUFH7R5NatQL36Zjnc83Z0SbDPi0M5X9lgRXeGddOCM7xBSC05z0Wwk%2FD317b2lk%2FkrwurW0xHnHVom8wmhmRpLWLV4SF799E%2BVD%2FfmH1xLwBHQ3KyeFcOAppQAewLjHBI6ZXqvKhZo5DT00sUhztoQy4rEXut1mQWSmc9074lPLu6V19I4%2FahF6tHXmt7tuBuI4rfDoA%2BZXuID%2F63y6zLtQ4gz%2Fg2G3qnmsAPu%2BPaPjSMF%2BID4vYOfDqt09w3QFObcPxZcPhgdXe5K8FZKBOlI8e8yu6HtJMKnctcsGOqUBlWBXZmQSQabFo%2F55RqsAE4OsylYQRFntBL6coStXcDKkwTJmDFYx%2FaQ7QeZaTy9M1lfAh%2BiU8xIK2x%2F0adV1wdoJUQtiPgc7x0UiD3zNlKBZCpLJUTQXqo0aOefUYciSX3ylJgvTKTnQ7s2oMX3eD%2F7o8klyELVakE9pxvb40e6oDTvaxmOT3%2FA4KYA532yR0UwX4mEK7EoOtOyxeuNqoSYYP3yS&X-Amz-Signature=4f0656d68a882729e5899c991b41969a05d051ad3326431eb8e4c3e0a5697827&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

