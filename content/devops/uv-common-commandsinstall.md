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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4M3DJ34%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQDBjtSPl1kiaG6Ebo2OCrU74egUoYOMbyyu%2FE6cqtq42gIhAMN1wlhot3ncjZxrXafAwio4CvtbKaAxTuoSlrG7Zli6Kv8DCAwQABoMNjM3NDIzMTgzODA1IgxBdzEQTu0blsZcS6Mq3AM5LRC7Sj0J62TSCGikuTMKqzRIZeRLTMpVmAh2rkLlxDy4M7O4iv3leC755cfnhvkAN7PC08iGml6hUKH0xb%2Blay3pCfEGtrk%2F6Tt%2FpZ1lH6Izqn%2FSN3ejHsS23dNu0959ttP9q%2F60gUeaQEnL3r1UEXjlVY%2BzLyk0c7cMLGifWDDOz02Dzyc5zEd2pTNfrnQmUPIL4BvBq%2B8XyKS8uCPTyyhna2mjHlSfAfgRpJeQPb%2F7LMpgfL0DNuDueOPIYbTn9qZHCCTzQV8PNf80H8hfVBRpey5FwDche%2FyzNwmRkk5Z1GBVOIutKvelj0a4qgj7ayh3aqvvRoKHgQzADSKoT1G9sLFnmHo9TCpFW2Q16wwv3PmNhjxAPvdSLKs7jF3jfeH8CcqXeOoI2%2BFNj6ABveQ%2Bf%2BLzS285hb7z%2BTmo32rXGk9x1h%2FlfrhL1g72WQ%2Fz8X1Ytz7UcmDwm9IK17o5bDu1HIn7uazp5vY51yICLVzfbVdnMDnMlQ%2F87qxF8C4Wr%2FxbKNdJ20Ak9ZZzYEOOXNWP%2BgJ%2B5Wj7atczvY5lMxyMe%2B3ur210QcszDmBvI%2B%2BNCDx%2Bm3c5Imlm2%2BWy7LQ3WA8NmFPlLAhQmZ25bgo%2BiyOzNwNDFNF2rb4tvzCYwrPNBjqkAdMSNzxG%2B4egoQJT17Tix1iA7wsMcPWJQtGLikDIvdhBezWNlpF2UPFaxPASqhIRChIoZsGhyixjH6pwd22lfrRxoSvqTjLCHFih9pNvJU6o8w4mh%2BsjAkVGB0IDRnnNUIb2j5hJG%2FSSxp%2BOaw8S6QVrIU9E4SrmtPbekuGo%2BtdrJglaZ6WDQzdoL4TBtDcxf9lZQcBB3Xn%2BVzfNbtmXMn26zFmb&X-Amz-Signature=0f2e6a7ef0d723fbde579c713f7a9304f4f4151fa6d40a47b53e2d43c6848bdc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4M3DJ34%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQDBjtSPl1kiaG6Ebo2OCrU74egUoYOMbyyu%2FE6cqtq42gIhAMN1wlhot3ncjZxrXafAwio4CvtbKaAxTuoSlrG7Zli6Kv8DCAwQABoMNjM3NDIzMTgzODA1IgxBdzEQTu0blsZcS6Mq3AM5LRC7Sj0J62TSCGikuTMKqzRIZeRLTMpVmAh2rkLlxDy4M7O4iv3leC755cfnhvkAN7PC08iGml6hUKH0xb%2Blay3pCfEGtrk%2F6Tt%2FpZ1lH6Izqn%2FSN3ejHsS23dNu0959ttP9q%2F60gUeaQEnL3r1UEXjlVY%2BzLyk0c7cMLGifWDDOz02Dzyc5zEd2pTNfrnQmUPIL4BvBq%2B8XyKS8uCPTyyhna2mjHlSfAfgRpJeQPb%2F7LMpgfL0DNuDueOPIYbTn9qZHCCTzQV8PNf80H8hfVBRpey5FwDche%2FyzNwmRkk5Z1GBVOIutKvelj0a4qgj7ayh3aqvvRoKHgQzADSKoT1G9sLFnmHo9TCpFW2Q16wwv3PmNhjxAPvdSLKs7jF3jfeH8CcqXeOoI2%2BFNj6ABveQ%2Bf%2BLzS285hb7z%2BTmo32rXGk9x1h%2FlfrhL1g72WQ%2Fz8X1Ytz7UcmDwm9IK17o5bDu1HIn7uazp5vY51yICLVzfbVdnMDnMlQ%2F87qxF8C4Wr%2FxbKNdJ20Ak9ZZzYEOOXNWP%2BgJ%2B5Wj7atczvY5lMxyMe%2B3ur210QcszDmBvI%2B%2BNCDx%2Bm3c5Imlm2%2BWy7LQ3WA8NmFPlLAhQmZ25bgo%2BiyOzNwNDFNF2rb4tvzCYwrPNBjqkAdMSNzxG%2B4egoQJT17Tix1iA7wsMcPWJQtGLikDIvdhBezWNlpF2UPFaxPASqhIRChIoZsGhyixjH6pwd22lfrRxoSvqTjLCHFih9pNvJU6o8w4mh%2BsjAkVGB0IDRnnNUIb2j5hJG%2FSSxp%2BOaw8S6QVrIU9E4SrmtPbekuGo%2BtdrJglaZ6WDQzdoL4TBtDcxf9lZQcBB3Xn%2BVzfNbtmXMn26zFmb&X-Amz-Signature=2342f3fc70f5ee9e1f19f8c4fef0eb4049705b1a140f383b333f9f1996b0245c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4M3DJ34%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQDBjtSPl1kiaG6Ebo2OCrU74egUoYOMbyyu%2FE6cqtq42gIhAMN1wlhot3ncjZxrXafAwio4CvtbKaAxTuoSlrG7Zli6Kv8DCAwQABoMNjM3NDIzMTgzODA1IgxBdzEQTu0blsZcS6Mq3AM5LRC7Sj0J62TSCGikuTMKqzRIZeRLTMpVmAh2rkLlxDy4M7O4iv3leC755cfnhvkAN7PC08iGml6hUKH0xb%2Blay3pCfEGtrk%2F6Tt%2FpZ1lH6Izqn%2FSN3ejHsS23dNu0959ttP9q%2F60gUeaQEnL3r1UEXjlVY%2BzLyk0c7cMLGifWDDOz02Dzyc5zEd2pTNfrnQmUPIL4BvBq%2B8XyKS8uCPTyyhna2mjHlSfAfgRpJeQPb%2F7LMpgfL0DNuDueOPIYbTn9qZHCCTzQV8PNf80H8hfVBRpey5FwDche%2FyzNwmRkk5Z1GBVOIutKvelj0a4qgj7ayh3aqvvRoKHgQzADSKoT1G9sLFnmHo9TCpFW2Q16wwv3PmNhjxAPvdSLKs7jF3jfeH8CcqXeOoI2%2BFNj6ABveQ%2Bf%2BLzS285hb7z%2BTmo32rXGk9x1h%2FlfrhL1g72WQ%2Fz8X1Ytz7UcmDwm9IK17o5bDu1HIn7uazp5vY51yICLVzfbVdnMDnMlQ%2F87qxF8C4Wr%2FxbKNdJ20Ak9ZZzYEOOXNWP%2BgJ%2B5Wj7atczvY5lMxyMe%2B3ur210QcszDmBvI%2B%2BNCDx%2Bm3c5Imlm2%2BWy7LQ3WA8NmFPlLAhQmZ25bgo%2BiyOzNwNDFNF2rb4tvzCYwrPNBjqkAdMSNzxG%2B4egoQJT17Tix1iA7wsMcPWJQtGLikDIvdhBezWNlpF2UPFaxPASqhIRChIoZsGhyixjH6pwd22lfrRxoSvqTjLCHFih9pNvJU6o8w4mh%2BsjAkVGB0IDRnnNUIb2j5hJG%2FSSxp%2BOaw8S6QVrIU9E4SrmtPbekuGo%2BtdrJglaZ6WDQzdoL4TBtDcxf9lZQcBB3Xn%2BVzfNbtmXMn26zFmb&X-Amz-Signature=507760c664225d7c6f674eba95cdea2d3018ffbf426e344d8bee1cf94e64e78f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

