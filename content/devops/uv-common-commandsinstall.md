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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YU362RSV%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDffIs4dbMcHtc72Efzw4OaG1DVsz%2FTaor3qTmDijDErAiBbMJEzRespnjs1i8P9W0Bjr35yBARM3FRpKx9OWGqyOiqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMipNl0tuJGZ%2BPvubhKtwDRTamIHPd84yBV1UN1GLPtBroEU2yvo%2Fb%2Fd%2BVoNKX%2F5QKklj4nYPXTt0CAX6LA5hunIvTkTrd8N6TsQompVzON2DNohCZoJOiG9XZFUNyQ7%2Fv%2F75Hdf52H6Jb2cSau5rcUwSnVTNBreTixYwkd8l0Fp4Qoy7LPlaiDiDO7A7FMClWrvhW1aN%2FMcmoU4o4mshAWpbqVhyDlSTHb82SEeerpwULwtT8fZ8nw1gzB2oKlV9Ud7tlkl0%2Fay5Sqcb1zBy04ddmi%2BIUISaj%2FbNfU9GKs%2Bebrq1%2FEhvGhsN%2BUSgw19YjrKHGGszZ0RIcfXb9cFC7qJ9llAdqtx%2BP8qceY067d7BIZbIJHM2WkdcyH2nibo2j51hw38JAcDLjqIGgKMmfCA4B%2FlNWS6tLfFNS7rr%2FSZhvNnATFFYWrYtQeJA9KlNgBb%2F7%2FL%2F3avZhVR%2FS3fIAKG1ZM2ep7ZebiNjtyMxQ67G1M2Ao56ZdmrEam%2B4%2FAcAmTOzQdPF3uGT%2F7s724wU34blP3oODUcZSJBz5qlE9pO607KCtQsLyBBgVQLIf02bPWqtf1uupNJIpc%2BBnBIsPf9TQiEwNDvXN9%2FmLO0g15qvwAFibB%2FVwgEvpsVf1zvsJ9si0Lab73OQrvB8wwbjNzQY6pgGxHWw7wnrbSbABno55KS%2FRUUCk9owsvL49KSxTQQRdILwQ14LAnneKQQ3FD6dzxTAYGA7kUeZb3d3foeeCXQgr59v76%2Bv0hizOZQSoxcAMQ8t0n1F472bV2FpDili1rDpLThteq1BZ2NLPbeVxRRNVI81hiHa1CRvIGwJ%2FDQfpuSEuAaqpQq7rkmD7ZtYK%2Fn6D5x5JhiDTt2fEqeT%2BxUiBm6HFYByn&X-Amz-Signature=e173eab5b6c044d60eecfc285701ef665f079e1b7742c809851bfed4373140a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YU362RSV%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDffIs4dbMcHtc72Efzw4OaG1DVsz%2FTaor3qTmDijDErAiBbMJEzRespnjs1i8P9W0Bjr35yBARM3FRpKx9OWGqyOiqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMipNl0tuJGZ%2BPvubhKtwDRTamIHPd84yBV1UN1GLPtBroEU2yvo%2Fb%2Fd%2BVoNKX%2F5QKklj4nYPXTt0CAX6LA5hunIvTkTrd8N6TsQompVzON2DNohCZoJOiG9XZFUNyQ7%2Fv%2F75Hdf52H6Jb2cSau5rcUwSnVTNBreTixYwkd8l0Fp4Qoy7LPlaiDiDO7A7FMClWrvhW1aN%2FMcmoU4o4mshAWpbqVhyDlSTHb82SEeerpwULwtT8fZ8nw1gzB2oKlV9Ud7tlkl0%2Fay5Sqcb1zBy04ddmi%2BIUISaj%2FbNfU9GKs%2Bebrq1%2FEhvGhsN%2BUSgw19YjrKHGGszZ0RIcfXb9cFC7qJ9llAdqtx%2BP8qceY067d7BIZbIJHM2WkdcyH2nibo2j51hw38JAcDLjqIGgKMmfCA4B%2FlNWS6tLfFNS7rr%2FSZhvNnATFFYWrYtQeJA9KlNgBb%2F7%2FL%2F3avZhVR%2FS3fIAKG1ZM2ep7ZebiNjtyMxQ67G1M2Ao56ZdmrEam%2B4%2FAcAmTOzQdPF3uGT%2F7s724wU34blP3oODUcZSJBz5qlE9pO607KCtQsLyBBgVQLIf02bPWqtf1uupNJIpc%2BBnBIsPf9TQiEwNDvXN9%2FmLO0g15qvwAFibB%2FVwgEvpsVf1zvsJ9si0Lab73OQrvB8wwbjNzQY6pgGxHWw7wnrbSbABno55KS%2FRUUCk9owsvL49KSxTQQRdILwQ14LAnneKQQ3FD6dzxTAYGA7kUeZb3d3foeeCXQgr59v76%2Bv0hizOZQSoxcAMQ8t0n1F472bV2FpDili1rDpLThteq1BZ2NLPbeVxRRNVI81hiHa1CRvIGwJ%2FDQfpuSEuAaqpQq7rkmD7ZtYK%2Fn6D5x5JhiDTt2fEqeT%2BxUiBm6HFYByn&X-Amz-Signature=9f1a4ebe5233614217516c4bd513130d89aa182df906b0b28c0a69d5c1b1e634&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YU362RSV%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDffIs4dbMcHtc72Efzw4OaG1DVsz%2FTaor3qTmDijDErAiBbMJEzRespnjs1i8P9W0Bjr35yBARM3FRpKx9OWGqyOiqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMipNl0tuJGZ%2BPvubhKtwDRTamIHPd84yBV1UN1GLPtBroEU2yvo%2Fb%2Fd%2BVoNKX%2F5QKklj4nYPXTt0CAX6LA5hunIvTkTrd8N6TsQompVzON2DNohCZoJOiG9XZFUNyQ7%2Fv%2F75Hdf52H6Jb2cSau5rcUwSnVTNBreTixYwkd8l0Fp4Qoy7LPlaiDiDO7A7FMClWrvhW1aN%2FMcmoU4o4mshAWpbqVhyDlSTHb82SEeerpwULwtT8fZ8nw1gzB2oKlV9Ud7tlkl0%2Fay5Sqcb1zBy04ddmi%2BIUISaj%2FbNfU9GKs%2Bebrq1%2FEhvGhsN%2BUSgw19YjrKHGGszZ0RIcfXb9cFC7qJ9llAdqtx%2BP8qceY067d7BIZbIJHM2WkdcyH2nibo2j51hw38JAcDLjqIGgKMmfCA4B%2FlNWS6tLfFNS7rr%2FSZhvNnATFFYWrYtQeJA9KlNgBb%2F7%2FL%2F3avZhVR%2FS3fIAKG1ZM2ep7ZebiNjtyMxQ67G1M2Ao56ZdmrEam%2B4%2FAcAmTOzQdPF3uGT%2F7s724wU34blP3oODUcZSJBz5qlE9pO607KCtQsLyBBgVQLIf02bPWqtf1uupNJIpc%2BBnBIsPf9TQiEwNDvXN9%2FmLO0g15qvwAFibB%2FVwgEvpsVf1zvsJ9si0Lab73OQrvB8wwbjNzQY6pgGxHWw7wnrbSbABno55KS%2FRUUCk9owsvL49KSxTQQRdILwQ14LAnneKQQ3FD6dzxTAYGA7kUeZb3d3foeeCXQgr59v76%2Bv0hizOZQSoxcAMQ8t0n1F472bV2FpDili1rDpLThteq1BZ2NLPbeVxRRNVI81hiHa1CRvIGwJ%2FDQfpuSEuAaqpQq7rkmD7ZtYK%2Fn6D5x5JhiDTt2fEqeT%2BxUiBm6HFYByn&X-Amz-Signature=b84a266807415569309192cf25ed602ae06537cb1506e92fb1a10621d1cbcc8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

