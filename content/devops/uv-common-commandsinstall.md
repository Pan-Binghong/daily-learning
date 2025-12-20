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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466457OLGFO%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFC8tqqfB1MhqlK3n1SKiu%2B1CfIFA%2BheqJejE9zhdApgIhAIzuIsa9OjWqvqQYx%2FnrEe9M23EzlskmXbuI7oZIkiRGKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyXZtTgRZl7QhUcudoq3APIHwkYNO3yzpMpQTofTu9XpoPv72eY0PmhrG8fRHsQVfapF31GVGkLtI6yFa6lx6%2FouoxgjMWdv685%2FHX881KWeiFFItxaUAoPBkSp2fsnlbmbKnqVGC8KHmrYL4MTIKpV%2BTX1utRtYh1JkJxwSJ8E3mkQPfuEPcMVrRMk%2BGK9bVxruMkbqNdePuMmeaU6n7e4Rq%2F%2B2BLedUy%2Fd0BJVlSRw1RCC2iXJ9r1IL4uqx%2B1h7QGLSa98D3auqictAXd4Y9F2HdJPs1s9AajOSn%2FfmMGy0J4oj6roAQZ6OS47PLjnkMYm6K4J%2B3DViP18Lvq8lxsPydHLkI%2BhLtDlArLGafn1FqW3sxBLcRYVKHmPMfCO2xl%2Bq1vzNnCUuawxbzgbUFg9zq7E9ZPOiEyxOB1Xp6YpijyLQC3Wf27sziYCEXpwSdMrtvkWx%2By8tN0N5MYOGj6vMaKS63Ia3KeXD7o2E9tdcx5z5s0QzkPSJI%2BNgbQo4eqJFOINQ%2BNGBWu7CqhxW7mJnXnuD%2BIfmZ%2BLDVbr9QY56UwNoJ9NHi13UNKM%2BoDFCFeoLB4YF1FeUcIOXRsdOUwjjywSqsyd2LtzIvt8Z7jDuyRb03nyNwxa20XSTh9HVP6SJg8dZtJl0a5yDD%2BhZjKBjqkAdValsLq%2FI2L0fg%2FrctPbAYjKJ6wGwEAeHQOhAMw0WSMuGb%2BQHTRMg8Y9IBS6JQM%2FzTLUKDeenNq%2BxucQMSKerZkZn3eHHMs8e%2FUxikddc3oQxzQmkdtWFPhEOYdwuKklVvCx6aYsfcu8Zmns8JhTSLqRWbvMQ%2F17bR1YVe1xs6bwTtYcZOCwy9Uw%2FuD2Oayes%2FR7PojuvPaf8%2FKI4Xbf5MKW6wn&X-Amz-Signature=b01c4118096352cc507d3260a9c318a71e1150553f0469af28a7b72ce5638377&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466457OLGFO%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFC8tqqfB1MhqlK3n1SKiu%2B1CfIFA%2BheqJejE9zhdApgIhAIzuIsa9OjWqvqQYx%2FnrEe9M23EzlskmXbuI7oZIkiRGKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyXZtTgRZl7QhUcudoq3APIHwkYNO3yzpMpQTofTu9XpoPv72eY0PmhrG8fRHsQVfapF31GVGkLtI6yFa6lx6%2FouoxgjMWdv685%2FHX881KWeiFFItxaUAoPBkSp2fsnlbmbKnqVGC8KHmrYL4MTIKpV%2BTX1utRtYh1JkJxwSJ8E3mkQPfuEPcMVrRMk%2BGK9bVxruMkbqNdePuMmeaU6n7e4Rq%2F%2B2BLedUy%2Fd0BJVlSRw1RCC2iXJ9r1IL4uqx%2B1h7QGLSa98D3auqictAXd4Y9F2HdJPs1s9AajOSn%2FfmMGy0J4oj6roAQZ6OS47PLjnkMYm6K4J%2B3DViP18Lvq8lxsPydHLkI%2BhLtDlArLGafn1FqW3sxBLcRYVKHmPMfCO2xl%2Bq1vzNnCUuawxbzgbUFg9zq7E9ZPOiEyxOB1Xp6YpijyLQC3Wf27sziYCEXpwSdMrtvkWx%2By8tN0N5MYOGj6vMaKS63Ia3KeXD7o2E9tdcx5z5s0QzkPSJI%2BNgbQo4eqJFOINQ%2BNGBWu7CqhxW7mJnXnuD%2BIfmZ%2BLDVbr9QY56UwNoJ9NHi13UNKM%2BoDFCFeoLB4YF1FeUcIOXRsdOUwjjywSqsyd2LtzIvt8Z7jDuyRb03nyNwxa20XSTh9HVP6SJg8dZtJl0a5yDD%2BhZjKBjqkAdValsLq%2FI2L0fg%2FrctPbAYjKJ6wGwEAeHQOhAMw0WSMuGb%2BQHTRMg8Y9IBS6JQM%2FzTLUKDeenNq%2BxucQMSKerZkZn3eHHMs8e%2FUxikddc3oQxzQmkdtWFPhEOYdwuKklVvCx6aYsfcu8Zmns8JhTSLqRWbvMQ%2F17bR1YVe1xs6bwTtYcZOCwy9Uw%2FuD2Oayes%2FR7PojuvPaf8%2FKI4Xbf5MKW6wn&X-Amz-Signature=6ff90aece36b9a7909a24f1b3992e96f069da02c4706aa9359e7c4cef73c7007&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466457OLGFO%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFC8tqqfB1MhqlK3n1SKiu%2B1CfIFA%2BheqJejE9zhdApgIhAIzuIsa9OjWqvqQYx%2FnrEe9M23EzlskmXbuI7oZIkiRGKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyXZtTgRZl7QhUcudoq3APIHwkYNO3yzpMpQTofTu9XpoPv72eY0PmhrG8fRHsQVfapF31GVGkLtI6yFa6lx6%2FouoxgjMWdv685%2FHX881KWeiFFItxaUAoPBkSp2fsnlbmbKnqVGC8KHmrYL4MTIKpV%2BTX1utRtYh1JkJxwSJ8E3mkQPfuEPcMVrRMk%2BGK9bVxruMkbqNdePuMmeaU6n7e4Rq%2F%2B2BLedUy%2Fd0BJVlSRw1RCC2iXJ9r1IL4uqx%2B1h7QGLSa98D3auqictAXd4Y9F2HdJPs1s9AajOSn%2FfmMGy0J4oj6roAQZ6OS47PLjnkMYm6K4J%2B3DViP18Lvq8lxsPydHLkI%2BhLtDlArLGafn1FqW3sxBLcRYVKHmPMfCO2xl%2Bq1vzNnCUuawxbzgbUFg9zq7E9ZPOiEyxOB1Xp6YpijyLQC3Wf27sziYCEXpwSdMrtvkWx%2By8tN0N5MYOGj6vMaKS63Ia3KeXD7o2E9tdcx5z5s0QzkPSJI%2BNgbQo4eqJFOINQ%2BNGBWu7CqhxW7mJnXnuD%2BIfmZ%2BLDVbr9QY56UwNoJ9NHi13UNKM%2BoDFCFeoLB4YF1FeUcIOXRsdOUwjjywSqsyd2LtzIvt8Z7jDuyRb03nyNwxa20XSTh9HVP6SJg8dZtJl0a5yDD%2BhZjKBjqkAdValsLq%2FI2L0fg%2FrctPbAYjKJ6wGwEAeHQOhAMw0WSMuGb%2BQHTRMg8Y9IBS6JQM%2FzTLUKDeenNq%2BxucQMSKerZkZn3eHHMs8e%2FUxikddc3oQxzQmkdtWFPhEOYdwuKklVvCx6aYsfcu8Zmns8JhTSLqRWbvMQ%2F17bR1YVe1xs6bwTtYcZOCwy9Uw%2FuD2Oayes%2FR7PojuvPaf8%2FKI4Xbf5MKW6wn&X-Amz-Signature=9bb969d5e14a7692878d6fae6b1af74f59517391ea5afdba5858cd597ccd22e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

