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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XY4I2XTJ%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDh9U6KI4wVophF2D3EIgt13b1mkDahDjfqGJ0z1OJH9gIgGIHKCUTSoLMI6JX9ZYiRHqv%2BLbQiZ9wjjp2WtHQ7TaEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFRbGWKBHe1o7%2BRojyrcAzyldx%2BYD%2FAFOCHpJbmI%2BvN7A4UdlWnAFucSbizi8fFbC%2FWnCzCRivvtBlK2u1LvFZoDCevSGSnEAZ29lyuF%2BEIH0e3yebTdX%2FCuD6nH0vchgW%2FG%2BfAqL9eErfxpKOhbuJfwo7WMEuwjpcrd47NRwCIQ%2Bul6d%2FcOanf0r9cJ7gnLzE78BXP43rrxxu%2F42jTZr%2FZkXyvebFBaWatLJHUVDVGJicIaBGFHV%2Fnnn8OIfd4iGU50JzzMVxcEI83%2BdZI9GAIU0XkKoYyKNp9g9pfRhhTAJgMRWfAiI229lM%2BuFRgOesnCT4B2rerOBWLFOD%2B9xGEvbslSrVVdiJ67SM%2F%2FKRnTvk%2F3G9QjHtsSxunQKn8sMK2P%2B8CEWGWuepG8Wb0TLzX3QTCldVQpuZxyk%2FvxAU%2F7UspUvg7booA1H739dgz%2BDYwGmG2%2BOl%2BDh1jCRJulrnv1AG70ksDzjTzjAnIHk1QXntwE7iNvP%2Fw5CHL5pC8mkjX06TutQuBDwqk4f2eJWhfugMlPgjGhx%2B%2BpwpPjI6WAC0FY68tmThNZkxxHpNkcarPaoLyjBHdQXQP5JLJ6xeZtFDsOhUKfcZfmueYYHpsm3zJmLNG6%2BfZ7ipKwW%2Fn1L45mgTZi4Z94VN4zMIPLr8wGOqUBw44yXHv%2B3ejes1aIMPuJMob9gcaAzjI4O9hDavETimHwUPkUIJkUqD2ZFKmBKvKt2AtI992%2FqpU8bDr7BCVG3uKkVw74cr2p3ehdJHqNHhKttiziN%2BzLO%2F83jKkeugfIgTTDjJzfSVsZuzKa7NbQqmC%2F%2Bx0TsLAqsjpz4v2EOi3%2FX5hNeytYns11VzEfnQcZn%2Fleg1hlWRDwuikqQA4SZ%2FI30%2FS0&X-Amz-Signature=2cd0e0bb815b1da287923fca73783e72c254dbb894122879b4b2cd9937d7dbb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XY4I2XTJ%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDh9U6KI4wVophF2D3EIgt13b1mkDahDjfqGJ0z1OJH9gIgGIHKCUTSoLMI6JX9ZYiRHqv%2BLbQiZ9wjjp2WtHQ7TaEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFRbGWKBHe1o7%2BRojyrcAzyldx%2BYD%2FAFOCHpJbmI%2BvN7A4UdlWnAFucSbizi8fFbC%2FWnCzCRivvtBlK2u1LvFZoDCevSGSnEAZ29lyuF%2BEIH0e3yebTdX%2FCuD6nH0vchgW%2FG%2BfAqL9eErfxpKOhbuJfwo7WMEuwjpcrd47NRwCIQ%2Bul6d%2FcOanf0r9cJ7gnLzE78BXP43rrxxu%2F42jTZr%2FZkXyvebFBaWatLJHUVDVGJicIaBGFHV%2Fnnn8OIfd4iGU50JzzMVxcEI83%2BdZI9GAIU0XkKoYyKNp9g9pfRhhTAJgMRWfAiI229lM%2BuFRgOesnCT4B2rerOBWLFOD%2B9xGEvbslSrVVdiJ67SM%2F%2FKRnTvk%2F3G9QjHtsSxunQKn8sMK2P%2B8CEWGWuepG8Wb0TLzX3QTCldVQpuZxyk%2FvxAU%2F7UspUvg7booA1H739dgz%2BDYwGmG2%2BOl%2BDh1jCRJulrnv1AG70ksDzjTzjAnIHk1QXntwE7iNvP%2Fw5CHL5pC8mkjX06TutQuBDwqk4f2eJWhfugMlPgjGhx%2B%2BpwpPjI6WAC0FY68tmThNZkxxHpNkcarPaoLyjBHdQXQP5JLJ6xeZtFDsOhUKfcZfmueYYHpsm3zJmLNG6%2BfZ7ipKwW%2Fn1L45mgTZi4Z94VN4zMIPLr8wGOqUBw44yXHv%2B3ejes1aIMPuJMob9gcaAzjI4O9hDavETimHwUPkUIJkUqD2ZFKmBKvKt2AtI992%2FqpU8bDr7BCVG3uKkVw74cr2p3ehdJHqNHhKttiziN%2BzLO%2F83jKkeugfIgTTDjJzfSVsZuzKa7NbQqmC%2F%2Bx0TsLAqsjpz4v2EOi3%2FX5hNeytYns11VzEfnQcZn%2Fleg1hlWRDwuikqQA4SZ%2FI30%2FS0&X-Amz-Signature=ec4fc7a6fbd65f2b042c3f6ccc4f8bfd1de66055b901efd9f7f41e8ce82b3a00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XY4I2XTJ%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDh9U6KI4wVophF2D3EIgt13b1mkDahDjfqGJ0z1OJH9gIgGIHKCUTSoLMI6JX9ZYiRHqv%2BLbQiZ9wjjp2WtHQ7TaEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFRbGWKBHe1o7%2BRojyrcAzyldx%2BYD%2FAFOCHpJbmI%2BvN7A4UdlWnAFucSbizi8fFbC%2FWnCzCRivvtBlK2u1LvFZoDCevSGSnEAZ29lyuF%2BEIH0e3yebTdX%2FCuD6nH0vchgW%2FG%2BfAqL9eErfxpKOhbuJfwo7WMEuwjpcrd47NRwCIQ%2Bul6d%2FcOanf0r9cJ7gnLzE78BXP43rrxxu%2F42jTZr%2FZkXyvebFBaWatLJHUVDVGJicIaBGFHV%2Fnnn8OIfd4iGU50JzzMVxcEI83%2BdZI9GAIU0XkKoYyKNp9g9pfRhhTAJgMRWfAiI229lM%2BuFRgOesnCT4B2rerOBWLFOD%2B9xGEvbslSrVVdiJ67SM%2F%2FKRnTvk%2F3G9QjHtsSxunQKn8sMK2P%2B8CEWGWuepG8Wb0TLzX3QTCldVQpuZxyk%2FvxAU%2F7UspUvg7booA1H739dgz%2BDYwGmG2%2BOl%2BDh1jCRJulrnv1AG70ksDzjTzjAnIHk1QXntwE7iNvP%2Fw5CHL5pC8mkjX06TutQuBDwqk4f2eJWhfugMlPgjGhx%2B%2BpwpPjI6WAC0FY68tmThNZkxxHpNkcarPaoLyjBHdQXQP5JLJ6xeZtFDsOhUKfcZfmueYYHpsm3zJmLNG6%2BfZ7ipKwW%2Fn1L45mgTZi4Z94VN4zMIPLr8wGOqUBw44yXHv%2B3ejes1aIMPuJMob9gcaAzjI4O9hDavETimHwUPkUIJkUqD2ZFKmBKvKt2AtI992%2FqpU8bDr7BCVG3uKkVw74cr2p3ehdJHqNHhKttiziN%2BzLO%2F83jKkeugfIgTTDjJzfSVsZuzKa7NbQqmC%2F%2Bx0TsLAqsjpz4v2EOi3%2FX5hNeytYns11VzEfnQcZn%2Fleg1hlWRDwuikqQA4SZ%2FI30%2FS0&X-Amz-Signature=4ebd3c5930810f41199220afdeceb6e065e66896963d720a8ca0df4a3e34d6a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

