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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R43KYDBY%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAsAHKiBzOjRv69ekAP6gnOL%2B7IGth35MErS%2Bxj5uV4fAiADIDNlStHWUav9dqFCzfmCQjCz4n6QoI%2B91hXd6o89MiqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqIRfSeDauwH3GaumKtwDhJxrrYRq5ZdGpHDgpieqRXuXxe%2FTFetcsAZ47a4tIQVgDQBGHrXn9TrH%2F%2F%2BJiARLFlQfdWIrWDctBr7SP77CssslANvsmn7428xUZZqErep5QZBFjgwEauCY2CZevl9KRUyYivI%2Fg14a68BpEzQEoLfG3dOKJHRx7FyrdXCRhSOwYJXAcFDNYsmfHYksxWaJH1asQ43vpC9j3bmtBMiGJcyetElKca0DjzqInobqKpRB6htBa5ep3bChQz%2BJFR3uXnIDRPsCsa23z4U2noCmPn3akUPDm02Y9tNnA4Hvyw95MJ%2FZG1Y4wcgT3GSQvtD7ihtVTFtKb7w0mI463HVnueEn%2BKQ5jcBM1rJ%2BEvbaWnUS5Cw69MF2XpaXdgqLQ6nK5wOrvo9rraDABUR2RB9Dou1F3zue3grKV2ThUPn3wVS0Z27cF%2Bh6agPoDYR1TstFH4Tm5v2vF0CwJ1WPAzYUzVcNdW2HZENU9wmShqCh3h1k%2FKCsET7SATpAqB9rwSfyF9%2Fr8xa7RWN4S1hj3JOC8LJnQnzBHuh4XsBNDaMdk%2BVnbPLW85yWrD%2F9uWitYjKFAik0TEAxkHWa68TtVFK8Rbp3%2FV9XfpczSid6LoTInA7yOffMe4xOvCm004ow7fCvyAY6pgE0Wj0iWSKRyyMvjrHRT%2Fz%2BM1%2FXX1l0%2Bd%2B7t7ft%2BQZjKdzBQKTUU8c6MdRS2rJZ76f2%2Bvgb9g5JdbyYqGu9WcJ6eht9ysnr%2BVvKmKsdTiU5ddqKi8nVU9WDCdpm7xZd%2FYa3COPteTQtIDua0qSCw39RV3Qh7tfxGMR6SJ5mxrg8jf7tfSm4roA%2F77kItyGXXrfaszRF4EWTGiByBcIcklCPClr19xh1&X-Amz-Signature=74991720fb703e62b2aaa9dbffd0779be18e796783f1c23b3a7e804aff514fed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R43KYDBY%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAsAHKiBzOjRv69ekAP6gnOL%2B7IGth35MErS%2Bxj5uV4fAiADIDNlStHWUav9dqFCzfmCQjCz4n6QoI%2B91hXd6o89MiqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqIRfSeDauwH3GaumKtwDhJxrrYRq5ZdGpHDgpieqRXuXxe%2FTFetcsAZ47a4tIQVgDQBGHrXn9TrH%2F%2F%2BJiARLFlQfdWIrWDctBr7SP77CssslANvsmn7428xUZZqErep5QZBFjgwEauCY2CZevl9KRUyYivI%2Fg14a68BpEzQEoLfG3dOKJHRx7FyrdXCRhSOwYJXAcFDNYsmfHYksxWaJH1asQ43vpC9j3bmtBMiGJcyetElKca0DjzqInobqKpRB6htBa5ep3bChQz%2BJFR3uXnIDRPsCsa23z4U2noCmPn3akUPDm02Y9tNnA4Hvyw95MJ%2FZG1Y4wcgT3GSQvtD7ihtVTFtKb7w0mI463HVnueEn%2BKQ5jcBM1rJ%2BEvbaWnUS5Cw69MF2XpaXdgqLQ6nK5wOrvo9rraDABUR2RB9Dou1F3zue3grKV2ThUPn3wVS0Z27cF%2Bh6agPoDYR1TstFH4Tm5v2vF0CwJ1WPAzYUzVcNdW2HZENU9wmShqCh3h1k%2FKCsET7SATpAqB9rwSfyF9%2Fr8xa7RWN4S1hj3JOC8LJnQnzBHuh4XsBNDaMdk%2BVnbPLW85yWrD%2F9uWitYjKFAik0TEAxkHWa68TtVFK8Rbp3%2FV9XfpczSid6LoTInA7yOffMe4xOvCm004ow7fCvyAY6pgE0Wj0iWSKRyyMvjrHRT%2Fz%2BM1%2FXX1l0%2Bd%2B7t7ft%2BQZjKdzBQKTUU8c6MdRS2rJZ76f2%2Bvgb9g5JdbyYqGu9WcJ6eht9ysnr%2BVvKmKsdTiU5ddqKi8nVU9WDCdpm7xZd%2FYa3COPteTQtIDua0qSCw39RV3Qh7tfxGMR6SJ5mxrg8jf7tfSm4roA%2F77kItyGXXrfaszRF4EWTGiByBcIcklCPClr19xh1&X-Amz-Signature=1b5a3865bffa7f93df5af40a1fe5c1d23903ef6903f1347dd63d24575f38e9d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R43KYDBY%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAsAHKiBzOjRv69ekAP6gnOL%2B7IGth35MErS%2Bxj5uV4fAiADIDNlStHWUav9dqFCzfmCQjCz4n6QoI%2B91hXd6o89MiqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqIRfSeDauwH3GaumKtwDhJxrrYRq5ZdGpHDgpieqRXuXxe%2FTFetcsAZ47a4tIQVgDQBGHrXn9TrH%2F%2F%2BJiARLFlQfdWIrWDctBr7SP77CssslANvsmn7428xUZZqErep5QZBFjgwEauCY2CZevl9KRUyYivI%2Fg14a68BpEzQEoLfG3dOKJHRx7FyrdXCRhSOwYJXAcFDNYsmfHYksxWaJH1asQ43vpC9j3bmtBMiGJcyetElKca0DjzqInobqKpRB6htBa5ep3bChQz%2BJFR3uXnIDRPsCsa23z4U2noCmPn3akUPDm02Y9tNnA4Hvyw95MJ%2FZG1Y4wcgT3GSQvtD7ihtVTFtKb7w0mI463HVnueEn%2BKQ5jcBM1rJ%2BEvbaWnUS5Cw69MF2XpaXdgqLQ6nK5wOrvo9rraDABUR2RB9Dou1F3zue3grKV2ThUPn3wVS0Z27cF%2Bh6agPoDYR1TstFH4Tm5v2vF0CwJ1WPAzYUzVcNdW2HZENU9wmShqCh3h1k%2FKCsET7SATpAqB9rwSfyF9%2Fr8xa7RWN4S1hj3JOC8LJnQnzBHuh4XsBNDaMdk%2BVnbPLW85yWrD%2F9uWitYjKFAik0TEAxkHWa68TtVFK8Rbp3%2FV9XfpczSid6LoTInA7yOffMe4xOvCm004ow7fCvyAY6pgE0Wj0iWSKRyyMvjrHRT%2Fz%2BM1%2FXX1l0%2Bd%2B7t7ft%2BQZjKdzBQKTUU8c6MdRS2rJZ76f2%2Bvgb9g5JdbyYqGu9WcJ6eht9ysnr%2BVvKmKsdTiU5ddqKi8nVU9WDCdpm7xZd%2FYa3COPteTQtIDua0qSCw39RV3Qh7tfxGMR6SJ5mxrg8jf7tfSm4roA%2F77kItyGXXrfaszRF4EWTGiByBcIcklCPClr19xh1&X-Amz-Signature=3de6e8cfc312ad7f97e60472b89a8ca35b38603a589d86d02a5b58670f894bc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

