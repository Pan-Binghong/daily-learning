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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNHKKS72%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T030118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCbXomHOSKIf2f5om0PjgNY3bO%2F6%2BAkSnlkS81F1PaPAgIhANc34rQBxFR0miFoQGVlhi294oNS6FPYnkqi93XGXdJ7Kv8DCCsQABoMNjM3NDIzMTgzODA1IgznW2HaJWs86U2r7AYq3ANDLrNCXV9yCFQYaLe60ZY1AQfE1gy229HTpiJacn947quq0fJz5dU0nyb4kSlrz4K%2F52Be1tqGsDr7Edm6P45quoRVu94dkJO6%2BNF5I%2BCtjLjjDnXdzGdakjXdNUK4LwSvgqsqIedtFrAjeOojpheuibXpZubnharWn5Z6ItBtP71MPtl5DpAYmkTvh%2BDIAfKOOL6lqKzQEMnSHQm%2FN%2Bn0RQr%2F%2FP%2FXVHyacEmBs04xLBRB4AMb9YW7wMm04NNRzhqkTls9B2fyXavcdA3h7w8LiECwCGOlOlZiPknTkK0BIpzukFa5JctJBhE1ARFC6iegfPzrY0gKe2lqqsPJ3cwEETym7vEh40sQC27AMiab2%2FKH9ImW2mJEgbh7enxSIAYgt%2Bg9I27kr3WAVMe30%2BKDOs9J1CRmR%2BThrLAhbF10MI%2BTf7eWlqg1rwaBPsrxNUCY581TMd0yogUUc8aYXlfUEB7geoeKLNgB%2BG2sf8AhVuN%2F16XyCf9ZJphQIBe0MylYNudiPsImEgO5K0FtU%2F8%2BguyPtShzcNEKyxCFnJO867iuf%2BFxpeQ3zsw3%2FxDXaSW0nGjtbuEuqVMQ8kkxksGUm%2FXSiHP1GtdgwNopys1qHzr3nRB54b8g2MHMOTC5sPjJBjqkAVGDSru%2FuRPdSzSpgUq4hrfm8%2BMl5PaNNPNO5MypOqJEf5kbrg6nvryP8gvG7qyYOHHz1jgJYs%2BIbKmvI86hXqH%2FPQpaEYMPMPUZWoGdGoIfwroWCwnsp317ONurHRapyi6WA04T9MmvxObbdEbuT2jxpbtxsAAy4uM1MF5JK5i%2B7rdySXhyAunlqLQ%2B5vi4DJ8P5PZxFltF65lODQD7oqfg9DFP&X-Amz-Signature=2cdaeeef35d57e450639e6ed4cb9fc36fa365c86b9263a52c07e8d48fb7e0072&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNHKKS72%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T030118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCbXomHOSKIf2f5om0PjgNY3bO%2F6%2BAkSnlkS81F1PaPAgIhANc34rQBxFR0miFoQGVlhi294oNS6FPYnkqi93XGXdJ7Kv8DCCsQABoMNjM3NDIzMTgzODA1IgznW2HaJWs86U2r7AYq3ANDLrNCXV9yCFQYaLe60ZY1AQfE1gy229HTpiJacn947quq0fJz5dU0nyb4kSlrz4K%2F52Be1tqGsDr7Edm6P45quoRVu94dkJO6%2BNF5I%2BCtjLjjDnXdzGdakjXdNUK4LwSvgqsqIedtFrAjeOojpheuibXpZubnharWn5Z6ItBtP71MPtl5DpAYmkTvh%2BDIAfKOOL6lqKzQEMnSHQm%2FN%2Bn0RQr%2F%2FP%2FXVHyacEmBs04xLBRB4AMb9YW7wMm04NNRzhqkTls9B2fyXavcdA3h7w8LiECwCGOlOlZiPknTkK0BIpzukFa5JctJBhE1ARFC6iegfPzrY0gKe2lqqsPJ3cwEETym7vEh40sQC27AMiab2%2FKH9ImW2mJEgbh7enxSIAYgt%2Bg9I27kr3WAVMe30%2BKDOs9J1CRmR%2BThrLAhbF10MI%2BTf7eWlqg1rwaBPsrxNUCY581TMd0yogUUc8aYXlfUEB7geoeKLNgB%2BG2sf8AhVuN%2F16XyCf9ZJphQIBe0MylYNudiPsImEgO5K0FtU%2F8%2BguyPtShzcNEKyxCFnJO867iuf%2BFxpeQ3zsw3%2FxDXaSW0nGjtbuEuqVMQ8kkxksGUm%2FXSiHP1GtdgwNopys1qHzr3nRB54b8g2MHMOTC5sPjJBjqkAVGDSru%2FuRPdSzSpgUq4hrfm8%2BMl5PaNNPNO5MypOqJEf5kbrg6nvryP8gvG7qyYOHHz1jgJYs%2BIbKmvI86hXqH%2FPQpaEYMPMPUZWoGdGoIfwroWCwnsp317ONurHRapyi6WA04T9MmvxObbdEbuT2jxpbtxsAAy4uM1MF5JK5i%2B7rdySXhyAunlqLQ%2B5vi4DJ8P5PZxFltF65lODQD7oqfg9DFP&X-Amz-Signature=4872ff3ca12d67a308dece0342b4b0d73ce06195c9bf8c947fe2036c0837a5b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









