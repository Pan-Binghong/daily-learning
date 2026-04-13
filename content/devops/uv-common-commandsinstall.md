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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EPARYO6%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDy16ikQ2wMzXNDSYmHk2UpP%2FP3HT1Jn1gDwUU0u8kh8QIhAIiQo2MdjQOxVmMPuLWvkZagFb7mkl%2BKbTTp1JxB6ChcKv8DCGwQABoMNjM3NDIzMTgzODA1IgygsCRUx%2FcPvb6J82Iq3APYMJmQo7uhbXKHKTKmRcq67a9KUG8RdxWQozj2BNE8ktYo1%2FU9u2vICNDFliA13usVe1K1ZE%2FJgbo4kaI8gEgVZlJhhR%2Bb%2F%2FvVdBT3tAf1n1rXiu0AfLBF3RlYGNNyOpvJM4%2F9c3WqCxoAjzJnSCTQzJ3sEgUW81p9185geVouXW%2BOEAFR5V1sx22eqmTh20%2BceILDDhVHQeW5hx8vUxdAv%2Fx77FnDqMQCF3zmDIHjkGaygqO9XbpDoZVbRGDGVvforO%2BccDkoaxeX9fRtQSZcxg640OlHtcnMVPssoHcdvdeEaHbM0EdByCtP6fr6MX%2BEiRqnTdtwQ8QqVRVc3gHm0S7KtYw%2BOeHxl316rUTQXZt6gL6K%2F7Xme2MnyMmFzpRLOOP2zIQm04bQ%2B0FsFycMJEfD8sxYEWUPaVdQ52urfRgMxEVNqe0E686CBBxT2xFrxUer11jWapIuKeEVr0oM4mMPnpFgqCgjy5l2qJ7ClWnoTiGYsQF4ijODdu5t1TpOz%2Fgp0FpNzAhFEpxZDf1aQoDJDEVfXCJhd%2FLRSjHpJ4T429NN3sarhSYmwf1hAOacfjOTLbe1271iSinWQljZDaqA13WGmWCo5mMxek9R5Yrwln%2FpWr6RTZRREjDusfHOBjqkAaBP5NA5ugpaPnqnBKPSujQaT9Zp0cBgJvs3acSF%2BmVknS%2F7Z2uIvSA05Ne22O7rCmoIQZkqkF0peF25M7xsATqedL7WM5xAViX202ULALhayfsqn3zTXcWoBJXBuUg5m%2Fz5H754LS9zBd9pvSuuiLcviXSvVwmTWstiP4NmphpscJeoBKl1i8W3AR3aCTVP9V83DRdzr8tfyvux%2BwqYL3ULcGo1&X-Amz-Signature=b584098b8dfc415afb0fea5c2964516ea827a0ab5b8827d125178f2a7b1d087e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EPARYO6%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDy16ikQ2wMzXNDSYmHk2UpP%2FP3HT1Jn1gDwUU0u8kh8QIhAIiQo2MdjQOxVmMPuLWvkZagFb7mkl%2BKbTTp1JxB6ChcKv8DCGwQABoMNjM3NDIzMTgzODA1IgygsCRUx%2FcPvb6J82Iq3APYMJmQo7uhbXKHKTKmRcq67a9KUG8RdxWQozj2BNE8ktYo1%2FU9u2vICNDFliA13usVe1K1ZE%2FJgbo4kaI8gEgVZlJhhR%2Bb%2F%2FvVdBT3tAf1n1rXiu0AfLBF3RlYGNNyOpvJM4%2F9c3WqCxoAjzJnSCTQzJ3sEgUW81p9185geVouXW%2BOEAFR5V1sx22eqmTh20%2BceILDDhVHQeW5hx8vUxdAv%2Fx77FnDqMQCF3zmDIHjkGaygqO9XbpDoZVbRGDGVvforO%2BccDkoaxeX9fRtQSZcxg640OlHtcnMVPssoHcdvdeEaHbM0EdByCtP6fr6MX%2BEiRqnTdtwQ8QqVRVc3gHm0S7KtYw%2BOeHxl316rUTQXZt6gL6K%2F7Xme2MnyMmFzpRLOOP2zIQm04bQ%2B0FsFycMJEfD8sxYEWUPaVdQ52urfRgMxEVNqe0E686CBBxT2xFrxUer11jWapIuKeEVr0oM4mMPnpFgqCgjy5l2qJ7ClWnoTiGYsQF4ijODdu5t1TpOz%2Fgp0FpNzAhFEpxZDf1aQoDJDEVfXCJhd%2FLRSjHpJ4T429NN3sarhSYmwf1hAOacfjOTLbe1271iSinWQljZDaqA13WGmWCo5mMxek9R5Yrwln%2FpWr6RTZRREjDusfHOBjqkAaBP5NA5ugpaPnqnBKPSujQaT9Zp0cBgJvs3acSF%2BmVknS%2F7Z2uIvSA05Ne22O7rCmoIQZkqkF0peF25M7xsATqedL7WM5xAViX202ULALhayfsqn3zTXcWoBJXBuUg5m%2Fz5H754LS9zBd9pvSuuiLcviXSvVwmTWstiP4NmphpscJeoBKl1i8W3AR3aCTVP9V83DRdzr8tfyvux%2BwqYL3ULcGo1&X-Amz-Signature=c63c5d11b689fa26a2d3f6cfc4b4532ac7522f3bdf9a820eb9fa4ac6b3034179&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EPARYO6%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDy16ikQ2wMzXNDSYmHk2UpP%2FP3HT1Jn1gDwUU0u8kh8QIhAIiQo2MdjQOxVmMPuLWvkZagFb7mkl%2BKbTTp1JxB6ChcKv8DCGwQABoMNjM3NDIzMTgzODA1IgygsCRUx%2FcPvb6J82Iq3APYMJmQo7uhbXKHKTKmRcq67a9KUG8RdxWQozj2BNE8ktYo1%2FU9u2vICNDFliA13usVe1K1ZE%2FJgbo4kaI8gEgVZlJhhR%2Bb%2F%2FvVdBT3tAf1n1rXiu0AfLBF3RlYGNNyOpvJM4%2F9c3WqCxoAjzJnSCTQzJ3sEgUW81p9185geVouXW%2BOEAFR5V1sx22eqmTh20%2BceILDDhVHQeW5hx8vUxdAv%2Fx77FnDqMQCF3zmDIHjkGaygqO9XbpDoZVbRGDGVvforO%2BccDkoaxeX9fRtQSZcxg640OlHtcnMVPssoHcdvdeEaHbM0EdByCtP6fr6MX%2BEiRqnTdtwQ8QqVRVc3gHm0S7KtYw%2BOeHxl316rUTQXZt6gL6K%2F7Xme2MnyMmFzpRLOOP2zIQm04bQ%2B0FsFycMJEfD8sxYEWUPaVdQ52urfRgMxEVNqe0E686CBBxT2xFrxUer11jWapIuKeEVr0oM4mMPnpFgqCgjy5l2qJ7ClWnoTiGYsQF4ijODdu5t1TpOz%2Fgp0FpNzAhFEpxZDf1aQoDJDEVfXCJhd%2FLRSjHpJ4T429NN3sarhSYmwf1hAOacfjOTLbe1271iSinWQljZDaqA13WGmWCo5mMxek9R5Yrwln%2FpWr6RTZRREjDusfHOBjqkAaBP5NA5ugpaPnqnBKPSujQaT9Zp0cBgJvs3acSF%2BmVknS%2F7Z2uIvSA05Ne22O7rCmoIQZkqkF0peF25M7xsATqedL7WM5xAViX202ULALhayfsqn3zTXcWoBJXBuUg5m%2Fz5H754LS9zBd9pvSuuiLcviXSvVwmTWstiP4NmphpscJeoBKl1i8W3AR3aCTVP9V83DRdzr8tfyvux%2BwqYL3ULcGo1&X-Amz-Signature=50042f40fc58184b15ae09b429d53066a250b7e23b6f7e417d187b28b38db8d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

