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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPM3OL2A%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNXk%2BYPo0tLu0EkBUW23dtHjN50Ke7MOWtis7hmhKofQIgfRYELFk7JT%2FsjCfbKFH3le%2BdrWE9m3sIOYMlLQKKkQ8qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJmPYlDuL%2F%2BKiPObiircAwWoy7wfFgkWRie3GfhyrkHUN5cRgHtGfrKsIEAYKxZB4OysWoK2EOoO%2BWxV5ozhMRWCGuTRCc7VyWmmkc7QnIfIuWudA8toNgT2pd8xEhvbVPSg39YdpKSMVyUXAtDmlbm3RUPsPrHuAwfbMH91kuYmxhTvCLo8ormA2rqQZUMbFdtnFUHQbav3ffQWm%2BY2PSYVlHlUqA0GtcOvhi5XvV3u8I9AvgiswCIiwS9shb1E2oRsyo%2FL9AYP1KAiUI3ik50WNFUOuOGuHV5FecsBGeNsAnTiF7GlvyYDihIHJUefMjGriAB0x54PpvwF%2FmNRK7%2BBlju4NLgN5CBM2tXb7Kq1X53OuxWBwB1sRi5LJiKkpynHwknoPKrjRDiWcs7sqZXifmp5ETaha413Idw%2BjohJz1JUZB%2B8qbbFRVmaY%2FTkBTSYJZUurP5H8kthkGJopwMcDuFKBz1XnH9pkwGnvZJb3%2BRZHYEpfUZRbciWqPYNDln%2BKqZdc%2BDMm1vHnfwtSCbVp0zqRHSqMEug%2BuP7xcS51pFaAycKumXsojou9gxpP1PbPZACgYJpzS2PTJoqhU3KcKTi3pw3LVKxAYlGy6B3r9un93RMwYB4ZBA4ZQ14sP%2BVQRAhmYrRPF0hMKSW%2B8sGOqUBBmf3YmLo4LrvWRrpsCPcZcaxO4lEfBbhqS2wf7ackCqAUikEFhjLF3xGDraLi4tia72Lo8UqHyY3iQT2O3PYYmNXeHyru13Yw35C%2Bqz0MgN0U57Rb1JglVidpqLJHMprpCRtWfEA5avWCYQnbwIeVaAyn5qD8h4ALwQNIED1ARbEppb4tITcPMfNcnUbkQDENXRnd8k6PePMhpfMPKAy5FsfDEFo&X-Amz-Signature=b1d4077fb5ca61f8814d824603f2bcd3979c18aed2b80433167c1b5675ad8505&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPM3OL2A%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNXk%2BYPo0tLu0EkBUW23dtHjN50Ke7MOWtis7hmhKofQIgfRYELFk7JT%2FsjCfbKFH3le%2BdrWE9m3sIOYMlLQKKkQ8qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJmPYlDuL%2F%2BKiPObiircAwWoy7wfFgkWRie3GfhyrkHUN5cRgHtGfrKsIEAYKxZB4OysWoK2EOoO%2BWxV5ozhMRWCGuTRCc7VyWmmkc7QnIfIuWudA8toNgT2pd8xEhvbVPSg39YdpKSMVyUXAtDmlbm3RUPsPrHuAwfbMH91kuYmxhTvCLo8ormA2rqQZUMbFdtnFUHQbav3ffQWm%2BY2PSYVlHlUqA0GtcOvhi5XvV3u8I9AvgiswCIiwS9shb1E2oRsyo%2FL9AYP1KAiUI3ik50WNFUOuOGuHV5FecsBGeNsAnTiF7GlvyYDihIHJUefMjGriAB0x54PpvwF%2FmNRK7%2BBlju4NLgN5CBM2tXb7Kq1X53OuxWBwB1sRi5LJiKkpynHwknoPKrjRDiWcs7sqZXifmp5ETaha413Idw%2BjohJz1JUZB%2B8qbbFRVmaY%2FTkBTSYJZUurP5H8kthkGJopwMcDuFKBz1XnH9pkwGnvZJb3%2BRZHYEpfUZRbciWqPYNDln%2BKqZdc%2BDMm1vHnfwtSCbVp0zqRHSqMEug%2BuP7xcS51pFaAycKumXsojou9gxpP1PbPZACgYJpzS2PTJoqhU3KcKTi3pw3LVKxAYlGy6B3r9un93RMwYB4ZBA4ZQ14sP%2BVQRAhmYrRPF0hMKSW%2B8sGOqUBBmf3YmLo4LrvWRrpsCPcZcaxO4lEfBbhqS2wf7ackCqAUikEFhjLF3xGDraLi4tia72Lo8UqHyY3iQT2O3PYYmNXeHyru13Yw35C%2Bqz0MgN0U57Rb1JglVidpqLJHMprpCRtWfEA5avWCYQnbwIeVaAyn5qD8h4ALwQNIED1ARbEppb4tITcPMfNcnUbkQDENXRnd8k6PePMhpfMPKAy5FsfDEFo&X-Amz-Signature=161f4dda5033517be54ff69232d94e1335a76033351de41e636961329e527142&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPM3OL2A%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNXk%2BYPo0tLu0EkBUW23dtHjN50Ke7MOWtis7hmhKofQIgfRYELFk7JT%2FsjCfbKFH3le%2BdrWE9m3sIOYMlLQKKkQ8qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJmPYlDuL%2F%2BKiPObiircAwWoy7wfFgkWRie3GfhyrkHUN5cRgHtGfrKsIEAYKxZB4OysWoK2EOoO%2BWxV5ozhMRWCGuTRCc7VyWmmkc7QnIfIuWudA8toNgT2pd8xEhvbVPSg39YdpKSMVyUXAtDmlbm3RUPsPrHuAwfbMH91kuYmxhTvCLo8ormA2rqQZUMbFdtnFUHQbav3ffQWm%2BY2PSYVlHlUqA0GtcOvhi5XvV3u8I9AvgiswCIiwS9shb1E2oRsyo%2FL9AYP1KAiUI3ik50WNFUOuOGuHV5FecsBGeNsAnTiF7GlvyYDihIHJUefMjGriAB0x54PpvwF%2FmNRK7%2BBlju4NLgN5CBM2tXb7Kq1X53OuxWBwB1sRi5LJiKkpynHwknoPKrjRDiWcs7sqZXifmp5ETaha413Idw%2BjohJz1JUZB%2B8qbbFRVmaY%2FTkBTSYJZUurP5H8kthkGJopwMcDuFKBz1XnH9pkwGnvZJb3%2BRZHYEpfUZRbciWqPYNDln%2BKqZdc%2BDMm1vHnfwtSCbVp0zqRHSqMEug%2BuP7xcS51pFaAycKumXsojou9gxpP1PbPZACgYJpzS2PTJoqhU3KcKTi3pw3LVKxAYlGy6B3r9un93RMwYB4ZBA4ZQ14sP%2BVQRAhmYrRPF0hMKSW%2B8sGOqUBBmf3YmLo4LrvWRrpsCPcZcaxO4lEfBbhqS2wf7ackCqAUikEFhjLF3xGDraLi4tia72Lo8UqHyY3iQT2O3PYYmNXeHyru13Yw35C%2Bqz0MgN0U57Rb1JglVidpqLJHMprpCRtWfEA5avWCYQnbwIeVaAyn5qD8h4ALwQNIED1ARbEppb4tITcPMfNcnUbkQDENXRnd8k6PePMhpfMPKAy5FsfDEFo&X-Amz-Signature=3ec1510388a63c2e7aede6ca5f0e532d7533d831f4bf2da31186624a0dc7399d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

