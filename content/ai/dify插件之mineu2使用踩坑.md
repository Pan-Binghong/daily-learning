---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFRJKA4I%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIGNMHVEZ%2BvTd0w9BlLKNwNMncC3nYbgngimxEZ5QqYQNAiEAjrOoWNLD%2BlBbZgYZw9%2FMXnqAsKg5RG3Zkx1%2FCNfJjv0qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPrhEQhnIh4qEK1FrCrcA0IXju%2FFmx963Uufpf%2F12MpzXiSO8vmQocZifvb4PxBC135g%2BdjjHBrQAPvVlmQs27VoqbFfmd9ccZY1vt1HG85%2F%2BQUC9v5Pq%2BIR0Q5%2FSC81dbZNUfVYtb8Xoeg2IEeL5y9ubwBP26hueGImYpSpGrg89e7ArEsid4xgYwXbRmRi%2FuFJug%2BpMto8%2FE4ujIAiFpfvK2FhCFArL%2B1YquSC3J3to0gZRsxN833uSywZedw0WI7JOZo%2BPhupvnyARvf%2FFS9uST22ANHPDx3teCmnoJPriYJABltET3h9e2zrennuu6ML9ck9pWt6Kgl8DtzNaFPd3u4Ix4i4VfIbB2K%2F50bg5Ke5xEx4f5dTwttqqjH6rB645LIkMZXLnISIpkGlUZ%2FJoTmXXOcI9EbFkMubAVNtnsj3fctNFCumzepimZFSZXHlz8JN%2BacM%2FyHogPgDUOwvDn244ojQOvkfz6MB0rJujuSdx%2FaFunbF8dqyKgXZXIfZ1TQrSatR18ySJIdVSgKxF7Ra1NZ9xYOMJ5UGPCCABfviGTuP5JxUNuB9QZR3diw57MvZRu4qSqsPBX73fSy9CPGZ7dWTJHSsnAW8dew4u%2BlL5H%2BnxoGtD0hrMVEF9zKhjf1%2BqEsxnJ4MMNK5uswGOqUBDJksLJ27dnAH%2B%2FW1qbS8Azbmbxo7kLc7aYO8vkRfh0Qt0sGM9CRt7LJke7wt4UWZb%2BIYp%2BzNk2axdylfu7JvNEyQYC9IfQyIpB8D9yavsLTOpo72CvevluQQWCCUwMo1lIxdbQYtsH5VZp3Am5lcz4InKjcUSBF%2FsU1m9OdMB1HRJ0OSpMZ%2BzKcuHc6MvbtfqtyNDlcFR0uAdiKFveWpuQBRyVrR&X-Amz-Signature=02133340bdbf018f1952661a1d01ed777e253dd16ca6429c9a362ba4904f6a3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFRJKA4I%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIGNMHVEZ%2BvTd0w9BlLKNwNMncC3nYbgngimxEZ5QqYQNAiEAjrOoWNLD%2BlBbZgYZw9%2FMXnqAsKg5RG3Zkx1%2FCNfJjv0qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPrhEQhnIh4qEK1FrCrcA0IXju%2FFmx963Uufpf%2F12MpzXiSO8vmQocZifvb4PxBC135g%2BdjjHBrQAPvVlmQs27VoqbFfmd9ccZY1vt1HG85%2F%2BQUC9v5Pq%2BIR0Q5%2FSC81dbZNUfVYtb8Xoeg2IEeL5y9ubwBP26hueGImYpSpGrg89e7ArEsid4xgYwXbRmRi%2FuFJug%2BpMto8%2FE4ujIAiFpfvK2FhCFArL%2B1YquSC3J3to0gZRsxN833uSywZedw0WI7JOZo%2BPhupvnyARvf%2FFS9uST22ANHPDx3teCmnoJPriYJABltET3h9e2zrennuu6ML9ck9pWt6Kgl8DtzNaFPd3u4Ix4i4VfIbB2K%2F50bg5Ke5xEx4f5dTwttqqjH6rB645LIkMZXLnISIpkGlUZ%2FJoTmXXOcI9EbFkMubAVNtnsj3fctNFCumzepimZFSZXHlz8JN%2BacM%2FyHogPgDUOwvDn244ojQOvkfz6MB0rJujuSdx%2FaFunbF8dqyKgXZXIfZ1TQrSatR18ySJIdVSgKxF7Ra1NZ9xYOMJ5UGPCCABfviGTuP5JxUNuB9QZR3diw57MvZRu4qSqsPBX73fSy9CPGZ7dWTJHSsnAW8dew4u%2BlL5H%2BnxoGtD0hrMVEF9zKhjf1%2BqEsxnJ4MMNK5uswGOqUBDJksLJ27dnAH%2B%2FW1qbS8Azbmbxo7kLc7aYO8vkRfh0Qt0sGM9CRt7LJke7wt4UWZb%2BIYp%2BzNk2axdylfu7JvNEyQYC9IfQyIpB8D9yavsLTOpo72CvevluQQWCCUwMo1lIxdbQYtsH5VZp3Am5lcz4InKjcUSBF%2FsU1m9OdMB1HRJ0OSpMZ%2BzKcuHc6MvbtfqtyNDlcFR0uAdiKFveWpuQBRyVrR&X-Amz-Signature=4e09323dd7c75ae7fac39d58b58d3bf540f7417ab0720ce7b9ee049c0ff9ef81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



