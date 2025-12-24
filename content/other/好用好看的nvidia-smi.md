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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WPAOGJU%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIBrqHm1jZebpePytv8ykspg74t0VovzumcM3n1Pg9z9RAiBWiBeb%2FY9IezXe29UF04Tc1TE%2BNV983mS57rDPT2pQWSr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMHWkHMf3ngvq6xX5iKtwD%2FjzGEa67gNnE1v%2Flp9jC9UueleHM2lyQN%2BTyVqbY57oib65JuCOp3paar4yba%2F2r5qysyb9Bv4L2l%2BjmQP4QvbjlKOAhxqMFW%2FG4uE79QuH5Wj8w%2FjK3S19%2FSnttsOTZyneQJUPbOXhCmvSie8kle4H6RzHgYFJTZ3QYDAvek1JDSdNO%2FItrFjI7imjpXKIHIRbQmpaZ4tDGXnt%2FC%2BkDH6uqcgE%2FZGk1ACDb6xzUVk9T1NYoTdGq8G1vYydREIpjFN2t7XlpJ%2BUaaenSErcifXy7WTTc1TjpDXHJjvhstoHdAYfn7icdUGhYLeCIe6CAnXYSbpyy54bCqrx3%2FtSNQ0UkM%2BIlf0tCWyEgDq996HqsQGiHwSz5r6QpV6eSoxKY6V9RWebk%2BXDtrM6NiFfeaezisvHhgsyHsvD1AxQSYuhluBKMxPUQRud%2FwNM8NWSS5vS7x27zpS6zYnF9P9FyGqENaVipF7zx8qwniIYuL7ZsE84j2wVFRQZIHnYKOm5Q3cqeIP%2Bq46F3LAwocYFLx5ECcbhP9uqab5th4vR3gGY4qZPxiIPRYTMyQ%2BKEQDrx5nRb1%2BUTbYhrpc5CKJ4L6GzIOKr7N5sXQobOlKxyFd9t%2BTFcM2suIn7a4iQwyOCsygY6pgHMEav80v3b6%2BQGpIv6jHwPDJAw9rd1lt1U%2FT%2Bic0RnHNdUSadLBsvOaL1nCIOWSUiaW1O37wu%2FroWlAoxhwt9SWIfYLukJTSpqGrS7yO0O%2F%2FwJB2l%2F84xlvh1%2FUCdOm7cqSXBRV%2BSroMr7TVH2gXTSbckuSchdGW8HaSCAm3UHVetfKxwvJyF8d3AwN%2BeKjUY2Q9aORVhoHOya%2FRO8fNoh5kGOEwpc&X-Amz-Signature=c0d6e1cd7a70c60c3b9334f1aeb232db9c6de1eafc38b656732566330213b9ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WPAOGJU%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIBrqHm1jZebpePytv8ykspg74t0VovzumcM3n1Pg9z9RAiBWiBeb%2FY9IezXe29UF04Tc1TE%2BNV983mS57rDPT2pQWSr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMHWkHMf3ngvq6xX5iKtwD%2FjzGEa67gNnE1v%2Flp9jC9UueleHM2lyQN%2BTyVqbY57oib65JuCOp3paar4yba%2F2r5qysyb9Bv4L2l%2BjmQP4QvbjlKOAhxqMFW%2FG4uE79QuH5Wj8w%2FjK3S19%2FSnttsOTZyneQJUPbOXhCmvSie8kle4H6RzHgYFJTZ3QYDAvek1JDSdNO%2FItrFjI7imjpXKIHIRbQmpaZ4tDGXnt%2FC%2BkDH6uqcgE%2FZGk1ACDb6xzUVk9T1NYoTdGq8G1vYydREIpjFN2t7XlpJ%2BUaaenSErcifXy7WTTc1TjpDXHJjvhstoHdAYfn7icdUGhYLeCIe6CAnXYSbpyy54bCqrx3%2FtSNQ0UkM%2BIlf0tCWyEgDq996HqsQGiHwSz5r6QpV6eSoxKY6V9RWebk%2BXDtrM6NiFfeaezisvHhgsyHsvD1AxQSYuhluBKMxPUQRud%2FwNM8NWSS5vS7x27zpS6zYnF9P9FyGqENaVipF7zx8qwniIYuL7ZsE84j2wVFRQZIHnYKOm5Q3cqeIP%2Bq46F3LAwocYFLx5ECcbhP9uqab5th4vR3gGY4qZPxiIPRYTMyQ%2BKEQDrx5nRb1%2BUTbYhrpc5CKJ4L6GzIOKr7N5sXQobOlKxyFd9t%2BTFcM2suIn7a4iQwyOCsygY6pgHMEav80v3b6%2BQGpIv6jHwPDJAw9rd1lt1U%2FT%2Bic0RnHNdUSadLBsvOaL1nCIOWSUiaW1O37wu%2FroWlAoxhwt9SWIfYLukJTSpqGrS7yO0O%2F%2FwJB2l%2F84xlvh1%2FUCdOm7cqSXBRV%2BSroMr7TVH2gXTSbckuSchdGW8HaSCAm3UHVetfKxwvJyF8d3AwN%2BeKjUY2Q9aORVhoHOya%2FRO8fNoh5kGOEwpc&X-Amz-Signature=e8a3a2bc3ba58d42e3dec1ebb756043ce374d3a870ab098e9cd0ab13cf7f1087&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









