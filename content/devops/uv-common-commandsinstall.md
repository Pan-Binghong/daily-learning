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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCQWDKFC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIAbQFaJfWZ4YQuGkyrPCDKHeSSR%2F202yowqU%2FaHaMc4VAiBZBT1W4%2F0giHvV8j3KN%2BRjlArEpKDujofsOs%2BkpYaztSr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMmHRPDp%2BPsB9QcwusKtwDfSv9QifgNQLVnMr6RYH%2BA4Ull%2FVbeWl41B0orSpb3SCqlmKlwPKM%2BJEFOkHrdTjPNsQveY9SLrmPDFPfDWrwtbXtH0hDf6dhlJIvBFO2el2FURA85MrmuUjjsmZRrKbj%2Fw%2Bf%2FZqqxLFa5SHPalnp0cCkcWhss5KKFIkXK7jrFVc1jPFdUIW61ajym7OD6MCpUCCl4b5sshXU9Cp5vh0AjbywFQUDF%2FBQzTqMeiGjNdC4enWxwAFWj%2BL9gu9zUkRQA4oqByQ8mhyMwJhc12cdbTErKdCTWooK6pKj8%2FhCM7IbWSlS13OYUOMEVrUChAs4blJcPDUrSvAeLA2dq8bOD4xPQsQUN9hyfiyoUY4n8VOuDCCDVG3wjAbQv%2FsPiSeoY907%2B%2BgJ7S%2BWGnQkhljYLZgxZm4rLeFlsbWDPDB5syGXo5tdv1zllhRwmJz%2B3WSl8Z1vshhmMIoZF6lEMGG7ourzb40qbuTsEzwdlyrDzt%2FsY6ZS7MIZQupf0LgQvbHESgPdZE0cLG84mzFcE217Ys3asJrGRtXPy4nskulw%2FfxF5eTEOHskoK2Vm%2FxCZSmCqdefauO4byD%2BjmoSdLn7hnqxKamv7US6XCO0nvxNiRcT8vdG5J9IbwVcgQgwvo3zyQY6pgG6wR1jc8I3owEWd8%2BT7H%2FWn8yBhfb2jCHn%2BRC5n9tl59Vjj6fGU2WpuWaYd%2BTv5MMLz5%2Bccq3%2BaZsYr1CQ3kpjZZqPtGIyUjzahmpMCrsEULIWwY9PPNxxssiEFaUxdfHL%2BbIlgkgY1RZvv4V9M6p7w81shVWmO6DPApD6SHuErB85Z3820icHL%2B2nONfUS4vM7%2F4e1gX4qFKu%2F%2BilGJfQLlMM4AIy&X-Amz-Signature=1669edcd01ad95f10734fd9b5a75e5cf20fd5c07bd3be96ba50165a258643bc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCQWDKFC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIAbQFaJfWZ4YQuGkyrPCDKHeSSR%2F202yowqU%2FaHaMc4VAiBZBT1W4%2F0giHvV8j3KN%2BRjlArEpKDujofsOs%2BkpYaztSr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMmHRPDp%2BPsB9QcwusKtwDfSv9QifgNQLVnMr6RYH%2BA4Ull%2FVbeWl41B0orSpb3SCqlmKlwPKM%2BJEFOkHrdTjPNsQveY9SLrmPDFPfDWrwtbXtH0hDf6dhlJIvBFO2el2FURA85MrmuUjjsmZRrKbj%2Fw%2Bf%2FZqqxLFa5SHPalnp0cCkcWhss5KKFIkXK7jrFVc1jPFdUIW61ajym7OD6MCpUCCl4b5sshXU9Cp5vh0AjbywFQUDF%2FBQzTqMeiGjNdC4enWxwAFWj%2BL9gu9zUkRQA4oqByQ8mhyMwJhc12cdbTErKdCTWooK6pKj8%2FhCM7IbWSlS13OYUOMEVrUChAs4blJcPDUrSvAeLA2dq8bOD4xPQsQUN9hyfiyoUY4n8VOuDCCDVG3wjAbQv%2FsPiSeoY907%2B%2BgJ7S%2BWGnQkhljYLZgxZm4rLeFlsbWDPDB5syGXo5tdv1zllhRwmJz%2B3WSl8Z1vshhmMIoZF6lEMGG7ourzb40qbuTsEzwdlyrDzt%2FsY6ZS7MIZQupf0LgQvbHESgPdZE0cLG84mzFcE217Ys3asJrGRtXPy4nskulw%2FfxF5eTEOHskoK2Vm%2FxCZSmCqdefauO4byD%2BjmoSdLn7hnqxKamv7US6XCO0nvxNiRcT8vdG5J9IbwVcgQgwvo3zyQY6pgG6wR1jc8I3owEWd8%2BT7H%2FWn8yBhfb2jCHn%2BRC5n9tl59Vjj6fGU2WpuWaYd%2BTv5MMLz5%2Bccq3%2BaZsYr1CQ3kpjZZqPtGIyUjzahmpMCrsEULIWwY9PPNxxssiEFaUxdfHL%2BbIlgkgY1RZvv4V9M6p7w81shVWmO6DPApD6SHuErB85Z3820icHL%2B2nONfUS4vM7%2F4e1gX4qFKu%2F%2BilGJfQLlMM4AIy&X-Amz-Signature=1ae271cd0e211134f2b07a6de9e2cce88a1a1bfb1e6ad24757dd255cc8605a0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCQWDKFC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIAbQFaJfWZ4YQuGkyrPCDKHeSSR%2F202yowqU%2FaHaMc4VAiBZBT1W4%2F0giHvV8j3KN%2BRjlArEpKDujofsOs%2BkpYaztSr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMmHRPDp%2BPsB9QcwusKtwDfSv9QifgNQLVnMr6RYH%2BA4Ull%2FVbeWl41B0orSpb3SCqlmKlwPKM%2BJEFOkHrdTjPNsQveY9SLrmPDFPfDWrwtbXtH0hDf6dhlJIvBFO2el2FURA85MrmuUjjsmZRrKbj%2Fw%2Bf%2FZqqxLFa5SHPalnp0cCkcWhss5KKFIkXK7jrFVc1jPFdUIW61ajym7OD6MCpUCCl4b5sshXU9Cp5vh0AjbywFQUDF%2FBQzTqMeiGjNdC4enWxwAFWj%2BL9gu9zUkRQA4oqByQ8mhyMwJhc12cdbTErKdCTWooK6pKj8%2FhCM7IbWSlS13OYUOMEVrUChAs4blJcPDUrSvAeLA2dq8bOD4xPQsQUN9hyfiyoUY4n8VOuDCCDVG3wjAbQv%2FsPiSeoY907%2B%2BgJ7S%2BWGnQkhljYLZgxZm4rLeFlsbWDPDB5syGXo5tdv1zllhRwmJz%2B3WSl8Z1vshhmMIoZF6lEMGG7ourzb40qbuTsEzwdlyrDzt%2FsY6ZS7MIZQupf0LgQvbHESgPdZE0cLG84mzFcE217Ys3asJrGRtXPy4nskulw%2FfxF5eTEOHskoK2Vm%2FxCZSmCqdefauO4byD%2BjmoSdLn7hnqxKamv7US6XCO0nvxNiRcT8vdG5J9IbwVcgQgwvo3zyQY6pgG6wR1jc8I3owEWd8%2BT7H%2FWn8yBhfb2jCHn%2BRC5n9tl59Vjj6fGU2WpuWaYd%2BTv5MMLz5%2Bccq3%2BaZsYr1CQ3kpjZZqPtGIyUjzahmpMCrsEULIWwY9PPNxxssiEFaUxdfHL%2BbIlgkgY1RZvv4V9M6p7w81shVWmO6DPApD6SHuErB85Z3820icHL%2B2nONfUS4vM7%2F4e1gX4qFKu%2F%2BilGJfQLlMM4AIy&X-Amz-Signature=55237f6cfe112b3f546ff51a7e3b0fec1c6b1fd73f2c99a3649952944223380a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

