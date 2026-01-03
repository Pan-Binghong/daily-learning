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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Y7B42YJ%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDI9m8fQDLSEI0Qp2J%2BNN4wBzUwsVlRrjvEm9WIVk1sgQIgBCI5E6nG9UDK6aL08T50sj3VRoP6vCG1%2BvmMTRnQEnAq%2FwMIBxAAGgw2Mzc0MjMxODM4MDUiDJBsazmfo8bs4hYQmircA8BReOQilTgj3Z%2BjMR89QnfXza8hm946BCebnutll9aSB20W31rqO2cwpe6AYU0aKckjqNmkiafBf9StlXFwMrSe3B0oX6TJHCypy4b716k%2FXgPPFnE3%2Boyca0JBwHXc2ru5R9XD7eJBwLJ7P7O9uT5xTGeyh5KkYOfdKY0TaGJaTImSqYzLylMSVKo5NUCj%2ByJ8VXO6mDk3EbPt6pRgFyYJaPfzPmKDMZoKitvOJF2BXHEYG1HlpGQ65aAFGAm%2BrM2KGtQ%2FaCfJlQ7Rl1Ax99dT607SvlyeWLOIKXDQymFYF169N5ZFs3Y%2B565FeiJwbdy8e1S0v1bYAxPcPf4Rcp%2FoDlobhRnaMeBU2cE0mqXhoH7AOErsuDJfGp0yHVilzuJCmqaT8gbK%2BcqphC8UUMoydpUwPuHcGRYtBOmPpc58Dl1MvWrnP2zMoUHOSMpsks4O5upkv%2FAzsLXorpB99Vasbmq8Y7GCwUQveXxiPJoH6LOz4uCyOGW5pmXnI%2FzY5%2FhQfh4mECu2%2FOAQkI03YAW0eXSxEtQnZuMUrdDfyCdP8rqOpSZzfecRmQ9dDyxLO0aQ5kEShPnZXLnM%2BGS7Ga4fdotu8eQzHMsIRn6VEedoQ76jcaah%2BpY4yks4MPuH4coGOqUBkGgSShx9nDSfiaM8pAjdonBbhFalKUSZ%2BAMEu0r0h74H5dbXdC8Zzei1Do9sdEyBtmE%2FybSWh4p1nRtFFLAKpJgcMYvurT7xUOV11NB6ONp2sRZfwB8ugR6g82LSgTz7I9LkcUAzeegn4kM7fSOuiIWv2QzqlWF%2F38sNYVKwutfmhUUszBL84uSZDXIE%2FA8z6esXNu8LbFon4qNIxxTFyUGz0ULd&X-Amz-Signature=a44b00f8af1bc7c614b0acb1d15757d47143f0252b36c42d947a7515a7a034a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Y7B42YJ%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDI9m8fQDLSEI0Qp2J%2BNN4wBzUwsVlRrjvEm9WIVk1sgQIgBCI5E6nG9UDK6aL08T50sj3VRoP6vCG1%2BvmMTRnQEnAq%2FwMIBxAAGgw2Mzc0MjMxODM4MDUiDJBsazmfo8bs4hYQmircA8BReOQilTgj3Z%2BjMR89QnfXza8hm946BCebnutll9aSB20W31rqO2cwpe6AYU0aKckjqNmkiafBf9StlXFwMrSe3B0oX6TJHCypy4b716k%2FXgPPFnE3%2Boyca0JBwHXc2ru5R9XD7eJBwLJ7P7O9uT5xTGeyh5KkYOfdKY0TaGJaTImSqYzLylMSVKo5NUCj%2ByJ8VXO6mDk3EbPt6pRgFyYJaPfzPmKDMZoKitvOJF2BXHEYG1HlpGQ65aAFGAm%2BrM2KGtQ%2FaCfJlQ7Rl1Ax99dT607SvlyeWLOIKXDQymFYF169N5ZFs3Y%2B565FeiJwbdy8e1S0v1bYAxPcPf4Rcp%2FoDlobhRnaMeBU2cE0mqXhoH7AOErsuDJfGp0yHVilzuJCmqaT8gbK%2BcqphC8UUMoydpUwPuHcGRYtBOmPpc58Dl1MvWrnP2zMoUHOSMpsks4O5upkv%2FAzsLXorpB99Vasbmq8Y7GCwUQveXxiPJoH6LOz4uCyOGW5pmXnI%2FzY5%2FhQfh4mECu2%2FOAQkI03YAW0eXSxEtQnZuMUrdDfyCdP8rqOpSZzfecRmQ9dDyxLO0aQ5kEShPnZXLnM%2BGS7Ga4fdotu8eQzHMsIRn6VEedoQ76jcaah%2BpY4yks4MPuH4coGOqUBkGgSShx9nDSfiaM8pAjdonBbhFalKUSZ%2BAMEu0r0h74H5dbXdC8Zzei1Do9sdEyBtmE%2FybSWh4p1nRtFFLAKpJgcMYvurT7xUOV11NB6ONp2sRZfwB8ugR6g82LSgTz7I9LkcUAzeegn4kM7fSOuiIWv2QzqlWF%2F38sNYVKwutfmhUUszBL84uSZDXIE%2FA8z6esXNu8LbFon4qNIxxTFyUGz0ULd&X-Amz-Signature=286170c585646eb5d6020806eb788310daab986d14a4fb5d6bd34319b0bf734c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Y7B42YJ%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDI9m8fQDLSEI0Qp2J%2BNN4wBzUwsVlRrjvEm9WIVk1sgQIgBCI5E6nG9UDK6aL08T50sj3VRoP6vCG1%2BvmMTRnQEnAq%2FwMIBxAAGgw2Mzc0MjMxODM4MDUiDJBsazmfo8bs4hYQmircA8BReOQilTgj3Z%2BjMR89QnfXza8hm946BCebnutll9aSB20W31rqO2cwpe6AYU0aKckjqNmkiafBf9StlXFwMrSe3B0oX6TJHCypy4b716k%2FXgPPFnE3%2Boyca0JBwHXc2ru5R9XD7eJBwLJ7P7O9uT5xTGeyh5KkYOfdKY0TaGJaTImSqYzLylMSVKo5NUCj%2ByJ8VXO6mDk3EbPt6pRgFyYJaPfzPmKDMZoKitvOJF2BXHEYG1HlpGQ65aAFGAm%2BrM2KGtQ%2FaCfJlQ7Rl1Ax99dT607SvlyeWLOIKXDQymFYF169N5ZFs3Y%2B565FeiJwbdy8e1S0v1bYAxPcPf4Rcp%2FoDlobhRnaMeBU2cE0mqXhoH7AOErsuDJfGp0yHVilzuJCmqaT8gbK%2BcqphC8UUMoydpUwPuHcGRYtBOmPpc58Dl1MvWrnP2zMoUHOSMpsks4O5upkv%2FAzsLXorpB99Vasbmq8Y7GCwUQveXxiPJoH6LOz4uCyOGW5pmXnI%2FzY5%2FhQfh4mECu2%2FOAQkI03YAW0eXSxEtQnZuMUrdDfyCdP8rqOpSZzfecRmQ9dDyxLO0aQ5kEShPnZXLnM%2BGS7Ga4fdotu8eQzHMsIRn6VEedoQ76jcaah%2BpY4yks4MPuH4coGOqUBkGgSShx9nDSfiaM8pAjdonBbhFalKUSZ%2BAMEu0r0h74H5dbXdC8Zzei1Do9sdEyBtmE%2FybSWh4p1nRtFFLAKpJgcMYvurT7xUOV11NB6ONp2sRZfwB8ugR6g82LSgTz7I9LkcUAzeegn4kM7fSOuiIWv2QzqlWF%2F38sNYVKwutfmhUUszBL84uSZDXIE%2FA8z6esXNu8LbFon4qNIxxTFyUGz0ULd&X-Amz-Signature=d1e75b44c775d8045df5d7603449d0f5f4a0d0833614bbfa97fe43d4690ae6bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

