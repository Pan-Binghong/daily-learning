---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
tags:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF6LCJUV%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIFcY35Day6AZlNXFNCo2SdN3Gxpnft45qVkDCUpO2LGbAiEAmOMqh3mzQLhp2rc8I3R%2FFlGo6jtUflrDgCqXX8sJeM0q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDOgMKo5l8ADenmUuiyrcAzr24YVwcTJeb3c9G6zk8t%2B6NY9tPKeN%2BPAata1JcREYzF2U7mQNXlpHoWkJFxl%2FGjGpQN6JFl%2FtFD4epUz4IIY8JpDLrf%2Bl8p5L9V4LWG2%2Bdfbj7ONyC5pT3nYy%2BZ3bLAj%2Bg%2BSuWe6axBoCOK3WG5cjdoj4hRqgLqVZyjrLXfxcBl1LVMapl3YUQyIi95S74p2yNCA8l2nlGEfHL%2Ftg9y75QJOKF9lAm5kNA74Il8REas4Bi4b9BbuKpPotV7Y0NGcrHwP3gMreFTca7m7YuhezhiBXTEWipv%2FSmGB1L04rudSulwWEFJnVfht6rOJNRGYhA1RNfB%2BytUo7To3Q3kOJp5EwKRyX%2FFR7DFf9hsQ6lj3xt1j1qOGHmAetrh5M5Ibm5xYtULcruSF6nHg8kKDq5E8pXq3kZlr2sajQQeO80qMFWSUT0JUpUT38t0cIzx7UL4XSLB25NcRoaG%2B7Abm7zig%2BIyA4%2FsGqLO%2FZVoFoEvv7BFECbXXeKISIbMXtaryYAQMzGk4PrUUP8dC6BVyMoQhWTmJSj728rhBrdsnyr405JyBg1og34Zzn2I5j%2B30Xmn0nYkL1hnoRTayCRCGGGP2aIsolujNwHr%2B5Pmz92M%2FBdjxxF4AF2Lq0MLnx1MgGOqUB6%2BE4xUqUtrxuAmeztFc37wYx%2Bs0qPNPyTUhXk6RFlKJU1SNbLpGh3IVIyZut%2BqLFf45F%2Byixm4oWLzPiJPK3NbRVu3qx6V%2BRIi00ItHR2lqkWsXOEQgArobCgus8NMr5Qkfr%2BiQZoVLG2hrd5xHYE8q8QOgZso3rytZuAFFNnrOUi7S9WXyHEiAq3Cvys19QqtIjakrONP2yuY0K%2BwdfLR6PthTP&X-Amz-Signature=333f1d7d62ea6c0eb3db0ccb1595037768174e722c8bd4b5d6a8c997e4c7814f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 安装

```python
pip install nvitop
```

---

## 查看gpu状态

```python
nvitop
```

> 查看更加详细的gpu内容

```python
nvitop -m full
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF6LCJUV%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIFcY35Day6AZlNXFNCo2SdN3Gxpnft45qVkDCUpO2LGbAiEAmOMqh3mzQLhp2rc8I3R%2FFlGo6jtUflrDgCqXX8sJeM0q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDOgMKo5l8ADenmUuiyrcAzr24YVwcTJeb3c9G6zk8t%2B6NY9tPKeN%2BPAata1JcREYzF2U7mQNXlpHoWkJFxl%2FGjGpQN6JFl%2FtFD4epUz4IIY8JpDLrf%2Bl8p5L9V4LWG2%2Bdfbj7ONyC5pT3nYy%2BZ3bLAj%2Bg%2BSuWe6axBoCOK3WG5cjdoj4hRqgLqVZyjrLXfxcBl1LVMapl3YUQyIi95S74p2yNCA8l2nlGEfHL%2Ftg9y75QJOKF9lAm5kNA74Il8REas4Bi4b9BbuKpPotV7Y0NGcrHwP3gMreFTca7m7YuhezhiBXTEWipv%2FSmGB1L04rudSulwWEFJnVfht6rOJNRGYhA1RNfB%2BytUo7To3Q3kOJp5EwKRyX%2FFR7DFf9hsQ6lj3xt1j1qOGHmAetrh5M5Ibm5xYtULcruSF6nHg8kKDq5E8pXq3kZlr2sajQQeO80qMFWSUT0JUpUT38t0cIzx7UL4XSLB25NcRoaG%2B7Abm7zig%2BIyA4%2FsGqLO%2FZVoFoEvv7BFECbXXeKISIbMXtaryYAQMzGk4PrUUP8dC6BVyMoQhWTmJSj728rhBrdsnyr405JyBg1og34Zzn2I5j%2B30Xmn0nYkL1hnoRTayCRCGGGP2aIsolujNwHr%2B5Pmz92M%2FBdjxxF4AF2Lq0MLnx1MgGOqUB6%2BE4xUqUtrxuAmeztFc37wYx%2Bs0qPNPyTUhXk6RFlKJU1SNbLpGh3IVIyZut%2BqLFf45F%2Byixm4oWLzPiJPK3NbRVu3qx6V%2BRIi00ItHR2lqkWsXOEQgArobCgus8NMr5Qkfr%2BiQZoVLG2hrd5xHYE8q8QOgZso3rytZuAFFNnrOUi7S9WXyHEiAq3Cvys19QqtIjakrONP2yuY0K%2BwdfLR6PthTP&X-Amz-Signature=45c707eeafa2fc43483197dedda03e6974010a44b3bc1af214db252bd4dad237&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









