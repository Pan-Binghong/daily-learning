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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZTPOOHB%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQCU%2BHM0zc2Sb3OdTsYjQzluYH7SYAj0znVSJx07kHLMhQIgUeNXZB1dwOv0h0mRE%2FK%2BEg8CMPr2LujMykCfLrD1wlcq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDJvlyxb0ict%2Ftb040CrcAy%2BzOa2Suf7MXS0Lxjw45uavmcJr4B6g4J%2FGoDqkrSMqneXarrpoPixyfwWBTXvA1lj3GxWY%2FcJgctM5jROHhXxMYe0cVLlIV%2BddxB5wv15%2F0YzrWjkHm7jJv4t8lYnNye8OQ4FKQgKpuoWLECnxIy3yHpFdWrZP1iisUxUmdOZzogsaywp9RPeC8Rl6TCFrcT48hdcXBhm2S2LWIBlrs3Vwj3I13Dr7DyRnuTf5EvALknqrcIOhOIvbwGiESJ4NNYZbAaYVRvZ336UyjFdVzZ02EsPJjVBCsy4DcarVWpKh%2BD%2FEQ1VAkIEPvpaa5vL5pg4q28j5zrD6%2BfOUiQ8VogoVp3DdFZwKwfIQ83yAf5aQRs7QXnAF%2BWe6ws1hDU40j3fyRSLDTA6Nbw71sooj8ec32ZvJL6kyq2R%2FS6FQGmCWqA1RKDiCRy09WAogsAMrT%2B2RetYd8IGDldKrbU%2FCHaDoRKjyXSsk4zTVVEYW5cXqayIy5LGGmjMMa1dSAmlU5bAhQLHpCMC4h0I2V7LD3NuIy78kAr3o6zjqCAo1R3DCNfQrthiapLNn1Vo542xeBp9d3RnJ3EyWWB9NPai9Uvo8i1NR88eqku3bMquipmzdaoBPGMsufCRt0l2vMJmUkMwGOqUB0kLdfOv9pRbgIT8eRipzlmly%2FTHMiNJ3YlWGy%2BYlst3qkTLZBXJJcxgyh8xG%2FFpX3f3ZnU45BftC9%2FtpklA%2FpC80vimt82t1g1AotQiXdA5rm%2Fb9tqOF0bDZ9FrKmDn%2FbIL8kkUaxisHjccEAHE0mzg6JXiKV8281hYIhGMy5B9t0NysjhnZAKCuhdzbngQDXwVNdoi4fVHSU3AxpdwFWCcRdiTX&X-Amz-Signature=57d6590280cd2d3efe9dcc529941123bd90bdbcdd1df03c1e28d1e9390fc0ad1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZTPOOHB%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQCU%2BHM0zc2Sb3OdTsYjQzluYH7SYAj0znVSJx07kHLMhQIgUeNXZB1dwOv0h0mRE%2FK%2BEg8CMPr2LujMykCfLrD1wlcq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDJvlyxb0ict%2Ftb040CrcAy%2BzOa2Suf7MXS0Lxjw45uavmcJr4B6g4J%2FGoDqkrSMqneXarrpoPixyfwWBTXvA1lj3GxWY%2FcJgctM5jROHhXxMYe0cVLlIV%2BddxB5wv15%2F0YzrWjkHm7jJv4t8lYnNye8OQ4FKQgKpuoWLECnxIy3yHpFdWrZP1iisUxUmdOZzogsaywp9RPeC8Rl6TCFrcT48hdcXBhm2S2LWIBlrs3Vwj3I13Dr7DyRnuTf5EvALknqrcIOhOIvbwGiESJ4NNYZbAaYVRvZ336UyjFdVzZ02EsPJjVBCsy4DcarVWpKh%2BD%2FEQ1VAkIEPvpaa5vL5pg4q28j5zrD6%2BfOUiQ8VogoVp3DdFZwKwfIQ83yAf5aQRs7QXnAF%2BWe6ws1hDU40j3fyRSLDTA6Nbw71sooj8ec32ZvJL6kyq2R%2FS6FQGmCWqA1RKDiCRy09WAogsAMrT%2B2RetYd8IGDldKrbU%2FCHaDoRKjyXSsk4zTVVEYW5cXqayIy5LGGmjMMa1dSAmlU5bAhQLHpCMC4h0I2V7LD3NuIy78kAr3o6zjqCAo1R3DCNfQrthiapLNn1Vo542xeBp9d3RnJ3EyWWB9NPai9Uvo8i1NR88eqku3bMquipmzdaoBPGMsufCRt0l2vMJmUkMwGOqUB0kLdfOv9pRbgIT8eRipzlmly%2FTHMiNJ3YlWGy%2BYlst3qkTLZBXJJcxgyh8xG%2FFpX3f3ZnU45BftC9%2FtpklA%2FpC80vimt82t1g1AotQiXdA5rm%2Fb9tqOF0bDZ9FrKmDn%2FbIL8kkUaxisHjccEAHE0mzg6JXiKV8281hYIhGMy5B9t0NysjhnZAKCuhdzbngQDXwVNdoi4fVHSU3AxpdwFWCcRdiTX&X-Amz-Signature=e5b623853b049763402558b8a1f0b119e7db5cfa1caa2058a5054b46213bec7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZTPOOHB%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQCU%2BHM0zc2Sb3OdTsYjQzluYH7SYAj0znVSJx07kHLMhQIgUeNXZB1dwOv0h0mRE%2FK%2BEg8CMPr2LujMykCfLrD1wlcq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDJvlyxb0ict%2Ftb040CrcAy%2BzOa2Suf7MXS0Lxjw45uavmcJr4B6g4J%2FGoDqkrSMqneXarrpoPixyfwWBTXvA1lj3GxWY%2FcJgctM5jROHhXxMYe0cVLlIV%2BddxB5wv15%2F0YzrWjkHm7jJv4t8lYnNye8OQ4FKQgKpuoWLECnxIy3yHpFdWrZP1iisUxUmdOZzogsaywp9RPeC8Rl6TCFrcT48hdcXBhm2S2LWIBlrs3Vwj3I13Dr7DyRnuTf5EvALknqrcIOhOIvbwGiESJ4NNYZbAaYVRvZ336UyjFdVzZ02EsPJjVBCsy4DcarVWpKh%2BD%2FEQ1VAkIEPvpaa5vL5pg4q28j5zrD6%2BfOUiQ8VogoVp3DdFZwKwfIQ83yAf5aQRs7QXnAF%2BWe6ws1hDU40j3fyRSLDTA6Nbw71sooj8ec32ZvJL6kyq2R%2FS6FQGmCWqA1RKDiCRy09WAogsAMrT%2B2RetYd8IGDldKrbU%2FCHaDoRKjyXSsk4zTVVEYW5cXqayIy5LGGmjMMa1dSAmlU5bAhQLHpCMC4h0I2V7LD3NuIy78kAr3o6zjqCAo1R3DCNfQrthiapLNn1Vo542xeBp9d3RnJ3EyWWB9NPai9Uvo8i1NR88eqku3bMquipmzdaoBPGMsufCRt0l2vMJmUkMwGOqUB0kLdfOv9pRbgIT8eRipzlmly%2FTHMiNJ3YlWGy%2BYlst3qkTLZBXJJcxgyh8xG%2FFpX3f3ZnU45BftC9%2FtpklA%2FpC80vimt82t1g1AotQiXdA5rm%2Fb9tqOF0bDZ9FrKmDn%2FbIL8kkUaxisHjccEAHE0mzg6JXiKV8281hYIhGMy5B9t0NysjhnZAKCuhdzbngQDXwVNdoi4fVHSU3AxpdwFWCcRdiTX&X-Amz-Signature=f7c06fb1d73175fb348df545a38f053bb3ab9b402dbf2205da77413e5a32ea40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

