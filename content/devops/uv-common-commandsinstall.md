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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJHPMGBF%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKAr9xS3Bh0dOt%2FaKCqL65Lof%2BwKo8XbVWrlPmxjKWwAiBBt4na1gJtdcICvtEvJceDtB7lnZC8ipg7gY2X7UwCwyr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIM88jifrNA3nJUmGB4KtwDLQHbwXZiQ0XlYSatcMzfxYDIlcsgFO1oTIskhIcXE1phA5k6no6b9LcCRJQJKbYz%2BJEQDDyCTyYnknjP8HdxNjKyc6Pizbffq9EsFh5WSGyOxv%2BBy0RNmypxYlNMcy4cWMCeGkA3Hfny84r%2B%2F8iPiiJgMMgvI%2FL3aWFKur2zZueewwh2rsXUeHPTekHVh%2Bhl%2BSq8v%2Fcob89sdxErd6mZM%2BE2zkL7SKtcufB1VMUl4L0THD9XO3eiN3B%2FuSad2%2ByVEGg9OwP43GtwbOeYezAK5X3m9vYNuI1%2FQbQatbPSyTEP3ujP8lU%2BQHlSdOQOX3I0n0Z6LyT63z0z758%2FoyU5elRnu8Fy%2BOkcJAxTnrOOxuDGLh4bMgZwqoZhfLbRH7xZot1SeZ0Sxt27n4h1bhWEerEIC3Psjb5Y8UeFKOmDU8YVPucp3krbQTu%2BDGi%2BtI5AbH4UjqftCh7VXaaoQmTLKzi0trYKCKB3SLoeCyKirNcGOaWGuYoi54gf17JuHmZGqBmzN86EBXzYD7N7jNwD%2B%2FzJ%2BcwHOMXHPckG2R1gSeKp%2F1Tc1oLt12MDz%2BANC0oh%2Ba2nPttl5GOXV0wA4zDoIikpQHawD5zuNw4VhnGTQXEOdukaQEntC950KREwgIjszgY6pgFn%2BLIEQNbYeGSy5sUFDBnUwEjDXPZ7Tmov377%2Bt4AyLXv3FA5nSbzwkfCtNg3KwzEaQM2Z3jCFzHqNdufxrnRFiRP%2FJphDkW4mLQejFxYlodF6uA1s%2Fuv%2FFqy7yCceqPTbBzq4rLSFpxFC76lQ2sIGTpB4KavW4zDpgyRE6A%2FO4Jpvcwfdoq%2BZ3hYUD47fw67%2F%2FxUvarK5DqoEqh5KlN9I%2FsaGHubC&X-Amz-Signature=f8f597caf8d658b82845172be6a847d6dd8e82b612f2a547e4470004db3d49ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJHPMGBF%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKAr9xS3Bh0dOt%2FaKCqL65Lof%2BwKo8XbVWrlPmxjKWwAiBBt4na1gJtdcICvtEvJceDtB7lnZC8ipg7gY2X7UwCwyr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIM88jifrNA3nJUmGB4KtwDLQHbwXZiQ0XlYSatcMzfxYDIlcsgFO1oTIskhIcXE1phA5k6no6b9LcCRJQJKbYz%2BJEQDDyCTyYnknjP8HdxNjKyc6Pizbffq9EsFh5WSGyOxv%2BBy0RNmypxYlNMcy4cWMCeGkA3Hfny84r%2B%2F8iPiiJgMMgvI%2FL3aWFKur2zZueewwh2rsXUeHPTekHVh%2Bhl%2BSq8v%2Fcob89sdxErd6mZM%2BE2zkL7SKtcufB1VMUl4L0THD9XO3eiN3B%2FuSad2%2ByVEGg9OwP43GtwbOeYezAK5X3m9vYNuI1%2FQbQatbPSyTEP3ujP8lU%2BQHlSdOQOX3I0n0Z6LyT63z0z758%2FoyU5elRnu8Fy%2BOkcJAxTnrOOxuDGLh4bMgZwqoZhfLbRH7xZot1SeZ0Sxt27n4h1bhWEerEIC3Psjb5Y8UeFKOmDU8YVPucp3krbQTu%2BDGi%2BtI5AbH4UjqftCh7VXaaoQmTLKzi0trYKCKB3SLoeCyKirNcGOaWGuYoi54gf17JuHmZGqBmzN86EBXzYD7N7jNwD%2B%2FzJ%2BcwHOMXHPckG2R1gSeKp%2F1Tc1oLt12MDz%2BANC0oh%2Ba2nPttl5GOXV0wA4zDoIikpQHawD5zuNw4VhnGTQXEOdukaQEntC950KREwgIjszgY6pgFn%2BLIEQNbYeGSy5sUFDBnUwEjDXPZ7Tmov377%2Bt4AyLXv3FA5nSbzwkfCtNg3KwzEaQM2Z3jCFzHqNdufxrnRFiRP%2FJphDkW4mLQejFxYlodF6uA1s%2Fuv%2FFqy7yCceqPTbBzq4rLSFpxFC76lQ2sIGTpB4KavW4zDpgyRE6A%2FO4Jpvcwfdoq%2BZ3hYUD47fw67%2F%2FxUvarK5DqoEqh5KlN9I%2FsaGHubC&X-Amz-Signature=09175fb9f458886b0ef4145ad8d64a2b06a7bc7017f8868f2851885ca9322663&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJHPMGBF%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKAr9xS3Bh0dOt%2FaKCqL65Lof%2BwKo8XbVWrlPmxjKWwAiBBt4na1gJtdcICvtEvJceDtB7lnZC8ipg7gY2X7UwCwyr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIM88jifrNA3nJUmGB4KtwDLQHbwXZiQ0XlYSatcMzfxYDIlcsgFO1oTIskhIcXE1phA5k6no6b9LcCRJQJKbYz%2BJEQDDyCTyYnknjP8HdxNjKyc6Pizbffq9EsFh5WSGyOxv%2BBy0RNmypxYlNMcy4cWMCeGkA3Hfny84r%2B%2F8iPiiJgMMgvI%2FL3aWFKur2zZueewwh2rsXUeHPTekHVh%2Bhl%2BSq8v%2Fcob89sdxErd6mZM%2BE2zkL7SKtcufB1VMUl4L0THD9XO3eiN3B%2FuSad2%2ByVEGg9OwP43GtwbOeYezAK5X3m9vYNuI1%2FQbQatbPSyTEP3ujP8lU%2BQHlSdOQOX3I0n0Z6LyT63z0z758%2FoyU5elRnu8Fy%2BOkcJAxTnrOOxuDGLh4bMgZwqoZhfLbRH7xZot1SeZ0Sxt27n4h1bhWEerEIC3Psjb5Y8UeFKOmDU8YVPucp3krbQTu%2BDGi%2BtI5AbH4UjqftCh7VXaaoQmTLKzi0trYKCKB3SLoeCyKirNcGOaWGuYoi54gf17JuHmZGqBmzN86EBXzYD7N7jNwD%2B%2FzJ%2BcwHOMXHPckG2R1gSeKp%2F1Tc1oLt12MDz%2BANC0oh%2Ba2nPttl5GOXV0wA4zDoIikpQHawD5zuNw4VhnGTQXEOdukaQEntC950KREwgIjszgY6pgFn%2BLIEQNbYeGSy5sUFDBnUwEjDXPZ7Tmov377%2Bt4AyLXv3FA5nSbzwkfCtNg3KwzEaQM2Z3jCFzHqNdufxrnRFiRP%2FJphDkW4mLQejFxYlodF6uA1s%2Fuv%2FFqy7yCceqPTbBzq4rLSFpxFC76lQ2sIGTpB4KavW4zDpgyRE6A%2FO4Jpvcwfdoq%2BZ3hYUD47fw67%2F%2FxUvarK5DqoEqh5KlN9I%2FsaGHubC&X-Amz-Signature=e720bc658aa901a27a7a6979e1fde956daaaa44d7a6b437c43af8103e566ffea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

