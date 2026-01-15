---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637FKSA6V%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIHzqSxrDAW2PHf%2BFKV%2BoZrx81ROUO5Rs7dojT93ZPI5HAiEAjz%2B%2FwFz14h39%2FZG9UmR%2Fw0P8uv80RjVO3xZTjvSbE%2Foq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDN509aro0B6c1yuCoircA7zo%2BdidZZRvzXsdr%2BFyPIYyiqRhkrQH1XD6OTpPCjo8roWTYboUep%2FOCDbyP%2B%2BqC1Xi8QKizm%2FpMsZla6LKpHGzYnNIiaZJAkmbhZcBjavvQxu7qq6cNKJXlffdYh0NSTYALa4XFlnuYs%2F%2FJAKFDpgNNbzeiNX%2FRtO4lwVq9HwG%2FfXTbxpm5Qs%2B3zegwkYb62JiVSoQ9XmgnUpzP9kc3z20Ye44I1MzYkMMEF4lDijiMYr8z4gdu2msvDzpmkX1J9TRY8VIS9GVvxZcjShTK8mQCoeorHdEZKrX7Q3wM6yYjCb6%2FLwX5v7XJoS4tmGskzc6jdcWdcB%2B0JI17UIKAQ2XNfD0X6MuWey9qG5%2F6yoYps0yt4JISDxNiv15FTTDBbj6O0D0yBPtddwbaZG1RAXn%2FlZwQdsl6bWwVQ5CmhJ67j1q9rzRmP%2FBQDEq4zcnM%2FrhV28M%2BaNzNhQ7bRnBQfC6c1wdYg9aN9ZsDZRzv%2BVE6ZRdPKmA6CMFsFNmlpcQt45ADfX%2FQ%2Be%2BVyZLaVH4V9hSB3%2BQWBlEDTTHIM6%2BVJyvT1XnFGdTroMlCmMvFZafTCGMfto04jHzmsxKZ2kJMrhezNo%2Fq0z%2FUEJMNbRWVpOfuwm6YhvBJDc8JTvWMP6aocsGOqUB44AVaFJ3bqafHQOONh5yUZaLi3yXZP8%2FDjVTjFMABgy8CwYtplZO9aoTFbSBhR%2FloJepNFeQ%2FIGQutsnRayEttTZ%2Fx56Rv%2FvD4XlgssPyglgKmz%2BgB4BXcP%2Fmy%2BXw3dFmkMygMw2oXsL0wJ3c3Ub42k2QpbjPtzKCdauxCsUdytq0frwRGfpTsZNwRI9FSXjY8Omk5CRfmurpromDTaHwqoVeNTM&X-Amz-Signature=48fc0aea69bf16886ae0982bb1390d6bb3adbe996a268d21ca1af2378d33764f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637FKSA6V%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIHzqSxrDAW2PHf%2BFKV%2BoZrx81ROUO5Rs7dojT93ZPI5HAiEAjz%2B%2FwFz14h39%2FZG9UmR%2Fw0P8uv80RjVO3xZTjvSbE%2Foq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDN509aro0B6c1yuCoircA7zo%2BdidZZRvzXsdr%2BFyPIYyiqRhkrQH1XD6OTpPCjo8roWTYboUep%2FOCDbyP%2B%2BqC1Xi8QKizm%2FpMsZla6LKpHGzYnNIiaZJAkmbhZcBjavvQxu7qq6cNKJXlffdYh0NSTYALa4XFlnuYs%2F%2FJAKFDpgNNbzeiNX%2FRtO4lwVq9HwG%2FfXTbxpm5Qs%2B3zegwkYb62JiVSoQ9XmgnUpzP9kc3z20Ye44I1MzYkMMEF4lDijiMYr8z4gdu2msvDzpmkX1J9TRY8VIS9GVvxZcjShTK8mQCoeorHdEZKrX7Q3wM6yYjCb6%2FLwX5v7XJoS4tmGskzc6jdcWdcB%2B0JI17UIKAQ2XNfD0X6MuWey9qG5%2F6yoYps0yt4JISDxNiv15FTTDBbj6O0D0yBPtddwbaZG1RAXn%2FlZwQdsl6bWwVQ5CmhJ67j1q9rzRmP%2FBQDEq4zcnM%2FrhV28M%2BaNzNhQ7bRnBQfC6c1wdYg9aN9ZsDZRzv%2BVE6ZRdPKmA6CMFsFNmlpcQt45ADfX%2FQ%2Be%2BVyZLaVH4V9hSB3%2BQWBlEDTTHIM6%2BVJyvT1XnFGdTroMlCmMvFZafTCGMfto04jHzmsxKZ2kJMrhezNo%2Fq0z%2FUEJMNbRWVpOfuwm6YhvBJDc8JTvWMP6aocsGOqUB44AVaFJ3bqafHQOONh5yUZaLi3yXZP8%2FDjVTjFMABgy8CwYtplZO9aoTFbSBhR%2FloJepNFeQ%2FIGQutsnRayEttTZ%2Fx56Rv%2FvD4XlgssPyglgKmz%2BgB4BXcP%2Fmy%2BXw3dFmkMygMw2oXsL0wJ3c3Ub42k2QpbjPtzKCdauxCsUdytq0frwRGfpTsZNwRI9FSXjY8Omk5CRfmurpromDTaHwqoVeNTM&X-Amz-Signature=389693adb5b7abb8651fa0c490cb30e35b532ea7e2c0c6e9cdfa6a3a5c335568&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



