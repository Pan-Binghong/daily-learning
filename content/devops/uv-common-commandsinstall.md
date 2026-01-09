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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NWG3JFD%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID83o0CT4WTlqrZwRCsbErDJYff6COMUQYNprSj88WeRAiEAnJSdmwf1YIOHEcdpOOQtq6%2F53%2FBg23Z2Qil0Xt5532AqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNGSbszyeu4rvxQjSrcA6K%2BCIqDzikqKcFXpaLVRPV0jJ3PxNvjIk8vXmULuI8WHOgnwo4Z3by74jDe5wjnj5mWISuBadQzNCTcBInie%2FMjaU542p6t9EDYLxggU90rarxsEwNojy0pHoo6OraGOIU475OOv2Jx9u96zFawQeM2%2B4etFYJq9pvJfGGoZ90wuzafOxzurME9CtCuZyegOOw0%2Buo1RiMaO1p17xGkIsIIXE0%2FDfn16mpk63cwbrPZT%2BPPOROjYszdpAjkalCfwG%2BX5gkIPneXN0s%2FOAdqdIfpkfgeyHMmItfAStR01kQGRl11icUZbgIBXOkxJlVN%2FiRLEMVdnlDSJmY2S56r0R6AHlBaO%2FE90sIk359UrQIf2HsO1GwlhSGLlo%2BVkHasxkLhduUPDFV55ZgxZWefPGMKGv5P%2FXcyxQlbYZFt2Dep9ePvq0zfdjemy%2F7XQ%2BppCb0Syn%2BrRmTJlj7I26p5QH1frMH0Pqo33tPhhwFdXTMpKKJb3uQ16ipDjk049ShlEyLA%2BLJDWh32qDuL19I5hk2AfDugyfHsdvvyOOAhjMU%2FZwYsLx0YBEu3fsiP4mXy3ytZijlhqDP89DC85kahr2ga7veHdI%2FakQ33dBFJ5y2jWlPGAvM%2FPWRbhTQHMOjDgcsGOqUBI%2FXaum2KtHGhtTvySyN%2B1jU5Y%2B2V5RFiX%2Bo6xGzXAng0e1M6My9lMWmKtTYo4v3%2BaCxAcdIT8zNrKniSUxAT8DVZ5YN8ys%2BBAXBrpdFs2MvRzXZAJFPY9N1wvvRw%2Fq3VK73Kj2j0%2BdzUvMD%2FFxtOjsfJGjk77KLhWePrLjMcouF5g%2FYTOJo3a4C%2B9%2BFa32F96XZQn%2BO47aRb8Hetl7z4Ixaic%2Bhh&X-Amz-Signature=808f4bb45a301facc31c44ae5981cab4d99e4384e8e4380901a15e4dcffb2eca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NWG3JFD%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID83o0CT4WTlqrZwRCsbErDJYff6COMUQYNprSj88WeRAiEAnJSdmwf1YIOHEcdpOOQtq6%2F53%2FBg23Z2Qil0Xt5532AqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNGSbszyeu4rvxQjSrcA6K%2BCIqDzikqKcFXpaLVRPV0jJ3PxNvjIk8vXmULuI8WHOgnwo4Z3by74jDe5wjnj5mWISuBadQzNCTcBInie%2FMjaU542p6t9EDYLxggU90rarxsEwNojy0pHoo6OraGOIU475OOv2Jx9u96zFawQeM2%2B4etFYJq9pvJfGGoZ90wuzafOxzurME9CtCuZyegOOw0%2Buo1RiMaO1p17xGkIsIIXE0%2FDfn16mpk63cwbrPZT%2BPPOROjYszdpAjkalCfwG%2BX5gkIPneXN0s%2FOAdqdIfpkfgeyHMmItfAStR01kQGRl11icUZbgIBXOkxJlVN%2FiRLEMVdnlDSJmY2S56r0R6AHlBaO%2FE90sIk359UrQIf2HsO1GwlhSGLlo%2BVkHasxkLhduUPDFV55ZgxZWefPGMKGv5P%2FXcyxQlbYZFt2Dep9ePvq0zfdjemy%2F7XQ%2BppCb0Syn%2BrRmTJlj7I26p5QH1frMH0Pqo33tPhhwFdXTMpKKJb3uQ16ipDjk049ShlEyLA%2BLJDWh32qDuL19I5hk2AfDugyfHsdvvyOOAhjMU%2FZwYsLx0YBEu3fsiP4mXy3ytZijlhqDP89DC85kahr2ga7veHdI%2FakQ33dBFJ5y2jWlPGAvM%2FPWRbhTQHMOjDgcsGOqUBI%2FXaum2KtHGhtTvySyN%2B1jU5Y%2B2V5RFiX%2Bo6xGzXAng0e1M6My9lMWmKtTYo4v3%2BaCxAcdIT8zNrKniSUxAT8DVZ5YN8ys%2BBAXBrpdFs2MvRzXZAJFPY9N1wvvRw%2Fq3VK73Kj2j0%2BdzUvMD%2FFxtOjsfJGjk77KLhWePrLjMcouF5g%2FYTOJo3a4C%2B9%2BFa32F96XZQn%2BO47aRb8Hetl7z4Ixaic%2Bhh&X-Amz-Signature=a2b5601c3217e864a5b47ce4fa2926901fd279f4281331dd58378bd786261ce0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NWG3JFD%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID83o0CT4WTlqrZwRCsbErDJYff6COMUQYNprSj88WeRAiEAnJSdmwf1YIOHEcdpOOQtq6%2F53%2FBg23Z2Qil0Xt5532AqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNGSbszyeu4rvxQjSrcA6K%2BCIqDzikqKcFXpaLVRPV0jJ3PxNvjIk8vXmULuI8WHOgnwo4Z3by74jDe5wjnj5mWISuBadQzNCTcBInie%2FMjaU542p6t9EDYLxggU90rarxsEwNojy0pHoo6OraGOIU475OOv2Jx9u96zFawQeM2%2B4etFYJq9pvJfGGoZ90wuzafOxzurME9CtCuZyegOOw0%2Buo1RiMaO1p17xGkIsIIXE0%2FDfn16mpk63cwbrPZT%2BPPOROjYszdpAjkalCfwG%2BX5gkIPneXN0s%2FOAdqdIfpkfgeyHMmItfAStR01kQGRl11icUZbgIBXOkxJlVN%2FiRLEMVdnlDSJmY2S56r0R6AHlBaO%2FE90sIk359UrQIf2HsO1GwlhSGLlo%2BVkHasxkLhduUPDFV55ZgxZWefPGMKGv5P%2FXcyxQlbYZFt2Dep9ePvq0zfdjemy%2F7XQ%2BppCb0Syn%2BrRmTJlj7I26p5QH1frMH0Pqo33tPhhwFdXTMpKKJb3uQ16ipDjk049ShlEyLA%2BLJDWh32qDuL19I5hk2AfDugyfHsdvvyOOAhjMU%2FZwYsLx0YBEu3fsiP4mXy3ytZijlhqDP89DC85kahr2ga7veHdI%2FakQ33dBFJ5y2jWlPGAvM%2FPWRbhTQHMOjDgcsGOqUBI%2FXaum2KtHGhtTvySyN%2B1jU5Y%2B2V5RFiX%2Bo6xGzXAng0e1M6My9lMWmKtTYo4v3%2BaCxAcdIT8zNrKniSUxAT8DVZ5YN8ys%2BBAXBrpdFs2MvRzXZAJFPY9N1wvvRw%2Fq3VK73Kj2j0%2BdzUvMD%2FFxtOjsfJGjk77KLhWePrLjMcouF5g%2FYTOJo3a4C%2B9%2BFa32F96XZQn%2BO47aRb8Hetl7z4Ixaic%2Bhh&X-Amz-Signature=7e42ef6283f958f7771d190be2f16cfd76a5dd8551ef52408a6644b1c773ed27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

