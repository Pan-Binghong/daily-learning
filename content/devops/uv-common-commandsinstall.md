---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
标签:
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFRAYQPX%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICorcguCMlxXMUwdD6hLeCAtUMsVXFUYPnnkKRf4F8puAiBDnqOJ1%2BkvvE6mXb2R9E6QrN2Hv79z4QDJ%2FE12rekHBiqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdbxutfiGG42gVt53KtwDxu4SQpVPZhNPmWQzsbo4GC1wrp0FQRkbqn7Oq2Mc%2FRPeWL6N3TN%2BZCFeLZQpOb4mxJgK4PMDlRwQHWanX994YN5BG%2FRtXuqD8dBpm1gNt9G21wVsmropZwES0ujf90%2BbOvRc9pxvbNhWX%2FsMm84gDSGAdYJQb93V%2BTwL33S%2F6UvfH0hrNLxtZ9KvGxxam9ta%2FL1etLyNt2sFe3R0jVOPXm4XP8BNtTdIyuEJgxOmsRASYajZQIyijNmgmQ9eTkCs7BRu9FuEfLLd64KO0T7gyng4WIQpUBx6%2FIzgsksbee4m8MeU%2FJm5OMxX3BIYmUdIVDVDAVpMtFIR4yFFQFvby7%2FZCIT91VYiqGjk6TiIC2%2FXQhbEFhP8WLI4%2BKnwBfrALbVpOUWViyY4RUWf%2FU0oC5XAQ0vwf035GNI9myjoyovL0IYrEYeQASHW4FC625kq6S2GWh3K54OU%2F2HSiCOi9CwWOVZihKiyYZWHJjZyAJC8M0dvHLuq%2BfwB0C%2FDbEtckKSO%2FpoORjWKSRygbaiVV5bCzBSzBWXw8hGU6AI6T%2FQsyMwNl7jwDAl1Hg5BarD2s2uxl63Z3uyB8pbUu1YixIeo63PYSMMlXSYVBVkDaZMVRpGC8zyZuv1DkiAwvKOsyAY6pgHxGK3FUpZt7FDmFuRz9povu1nGIID0amtADjWWrgFEyNJTbg15Ko9AmJkSg%2F95sTvnFSTz6aj4NOHA%2FMi0QbHE1OVuP3Vj2auAyL%2FVwj6BKezekmGLknZxXoeEfs8PT%2FvLuCwbJJ26gaMp6AyQmMfblDxs3mlM%2Fs1uwFIq4k7VvPG7S6pMp91F2gpOrtAm6%2BW8eBbCTJjZ3TacQc7vcPTfErtkzz83&X-Amz-Signature=8a27e7351b66511d4b97b3d2642f8cb1304d18edb5f5b37c2e1d1ad575ed1fd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFRAYQPX%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICorcguCMlxXMUwdD6hLeCAtUMsVXFUYPnnkKRf4F8puAiBDnqOJ1%2BkvvE6mXb2R9E6QrN2Hv79z4QDJ%2FE12rekHBiqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdbxutfiGG42gVt53KtwDxu4SQpVPZhNPmWQzsbo4GC1wrp0FQRkbqn7Oq2Mc%2FRPeWL6N3TN%2BZCFeLZQpOb4mxJgK4PMDlRwQHWanX994YN5BG%2FRtXuqD8dBpm1gNt9G21wVsmropZwES0ujf90%2BbOvRc9pxvbNhWX%2FsMm84gDSGAdYJQb93V%2BTwL33S%2F6UvfH0hrNLxtZ9KvGxxam9ta%2FL1etLyNt2sFe3R0jVOPXm4XP8BNtTdIyuEJgxOmsRASYajZQIyijNmgmQ9eTkCs7BRu9FuEfLLd64KO0T7gyng4WIQpUBx6%2FIzgsksbee4m8MeU%2FJm5OMxX3BIYmUdIVDVDAVpMtFIR4yFFQFvby7%2FZCIT91VYiqGjk6TiIC2%2FXQhbEFhP8WLI4%2BKnwBfrALbVpOUWViyY4RUWf%2FU0oC5XAQ0vwf035GNI9myjoyovL0IYrEYeQASHW4FC625kq6S2GWh3K54OU%2F2HSiCOi9CwWOVZihKiyYZWHJjZyAJC8M0dvHLuq%2BfwB0C%2FDbEtckKSO%2FpoORjWKSRygbaiVV5bCzBSzBWXw8hGU6AI6T%2FQsyMwNl7jwDAl1Hg5BarD2s2uxl63Z3uyB8pbUu1YixIeo63PYSMMlXSYVBVkDaZMVRpGC8zyZuv1DkiAwvKOsyAY6pgHxGK3FUpZt7FDmFuRz9povu1nGIID0amtADjWWrgFEyNJTbg15Ko9AmJkSg%2F95sTvnFSTz6aj4NOHA%2FMi0QbHE1OVuP3Vj2auAyL%2FVwj6BKezekmGLknZxXoeEfs8PT%2FvLuCwbJJ26gaMp6AyQmMfblDxs3mlM%2Fs1uwFIq4k7VvPG7S6pMp91F2gpOrtAm6%2BW8eBbCTJjZ3TacQc7vcPTfErtkzz83&X-Amz-Signature=6e3ac525b59502f53801563338e4fabdef996fcd6723e8e080bbd41ee3ca0b54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFRAYQPX%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICorcguCMlxXMUwdD6hLeCAtUMsVXFUYPnnkKRf4F8puAiBDnqOJ1%2BkvvE6mXb2R9E6QrN2Hv79z4QDJ%2FE12rekHBiqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdbxutfiGG42gVt53KtwDxu4SQpVPZhNPmWQzsbo4GC1wrp0FQRkbqn7Oq2Mc%2FRPeWL6N3TN%2BZCFeLZQpOb4mxJgK4PMDlRwQHWanX994YN5BG%2FRtXuqD8dBpm1gNt9G21wVsmropZwES0ujf90%2BbOvRc9pxvbNhWX%2FsMm84gDSGAdYJQb93V%2BTwL33S%2F6UvfH0hrNLxtZ9KvGxxam9ta%2FL1etLyNt2sFe3R0jVOPXm4XP8BNtTdIyuEJgxOmsRASYajZQIyijNmgmQ9eTkCs7BRu9FuEfLLd64KO0T7gyng4WIQpUBx6%2FIzgsksbee4m8MeU%2FJm5OMxX3BIYmUdIVDVDAVpMtFIR4yFFQFvby7%2FZCIT91VYiqGjk6TiIC2%2FXQhbEFhP8WLI4%2BKnwBfrALbVpOUWViyY4RUWf%2FU0oC5XAQ0vwf035GNI9myjoyovL0IYrEYeQASHW4FC625kq6S2GWh3K54OU%2F2HSiCOi9CwWOVZihKiyYZWHJjZyAJC8M0dvHLuq%2BfwB0C%2FDbEtckKSO%2FpoORjWKSRygbaiVV5bCzBSzBWXw8hGU6AI6T%2FQsyMwNl7jwDAl1Hg5BarD2s2uxl63Z3uyB8pbUu1YixIeo63PYSMMlXSYVBVkDaZMVRpGC8zyZuv1DkiAwvKOsyAY6pgHxGK3FUpZt7FDmFuRz9povu1nGIID0amtADjWWrgFEyNJTbg15Ko9AmJkSg%2F95sTvnFSTz6aj4NOHA%2FMi0QbHE1OVuP3Vj2auAyL%2FVwj6BKezekmGLknZxXoeEfs8PT%2FvLuCwbJJ26gaMp6AyQmMfblDxs3mlM%2Fs1uwFIq4k7VvPG7S6pMp91F2gpOrtAm6%2BW8eBbCTJjZ3TacQc7vcPTfErtkzz83&X-Amz-Signature=f95acd83aff9354ee5d100de90b981a080cf94907616ffe53b6bde8bea276478&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

