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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6M466AY%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJGMEQCIEeRwhPJjD3E%2F89CtGIbBseBXeyiV3iZ5EyH3oshGREGAiBfhAODJw8pdNGvbr2Cgj2aHNOy3iySmenHwOT9kY1i9Cr%2FAwgLEAAaDDYzNzQyMzE4MzgwNSIMK5o5q6QrxruOJh4YKtwD0vUp3GBGoIDLNto4SQYOpnmpDkKS9bfJ1ZW%2BYv1m7m%2FLhY5N%2BfhiqIW8HS6hS4wkF8v%2BmWgyGpS%2Fgg9WUa1BsP%2BvsTEaS7%2FFdYF2V62WOfMdKNG1yOH%2BXCgVMY%2F4WiRqrF4r7%2Bci5KerddSZqCGc7RQo5mPJU7ZrtCaURFdc92LfpUPvuHnptdrPVqvwNB4UTK1vWAIsCenHGOvnwYVcwX9S2OfPOYuwZ4dPy5sH%2FRFFXkxlfSUkcumc8Rd7qwa79bCKzYYBJZBbZGjTYY70TOsdkQKXdtOZS2gWostjjU5FXv5DgDC9DVufDNMhtTi3XYkEYpBnVjh%2FXNR8vTDP%2F5YCRjAzX5L9%2F24sqhHk5D4yKNQFogLoWorrSr421BCOaOfooH55hRkouwDCrMO8Kw4pHuOO9cpEPifZaiNM%2FVVV1KVKxmfmuNgE0%2Bpqe1VfdC6CBtdM5G4bAkpQj9clEMATOrXaX%2BtrHmEN%2FvLbFryQHEo0GphnN6w%2B3sDokEeMSBk0kiV2rcDsFCdpSeRNmNHep7mCep9FYUHchgmjlOWfeCa13II%2BsejbOc3GGxKAFDFPnkwntjYcO7x7V3ar7zc28x1sCSHgPpmDJ4jgS3WVs%2FfzuWNknYlnkRIwtOzhygY6pgF%2FdfcUgsrzYLtIqgXvF1%2BWAr9eAe3YuES5rNHMf43chnN1%2FjOOlcY8DmE65ydr28RimH%2F6AMbkm9pzQfulyrYRNdG1R%2F2q2qrfjRpVcN1SOzRlTqsaDzXvlL3ARQGPEl0wIV8co9todZ171YhElBP1d5Cpv7q6mq7l1z4IY%2F4FrE8oTtS7QIJFbCgHibwhrMrosd8HRpcJ%2BiFATuNzzH2S0KHWs6cI&X-Amz-Signature=284960ddea7b924c8a37f797304eca74cb3a714b48f69893e96cbe3393da677a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6M466AY%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJGMEQCIEeRwhPJjD3E%2F89CtGIbBseBXeyiV3iZ5EyH3oshGREGAiBfhAODJw8pdNGvbr2Cgj2aHNOy3iySmenHwOT9kY1i9Cr%2FAwgLEAAaDDYzNzQyMzE4MzgwNSIMK5o5q6QrxruOJh4YKtwD0vUp3GBGoIDLNto4SQYOpnmpDkKS9bfJ1ZW%2BYv1m7m%2FLhY5N%2BfhiqIW8HS6hS4wkF8v%2BmWgyGpS%2Fgg9WUa1BsP%2BvsTEaS7%2FFdYF2V62WOfMdKNG1yOH%2BXCgVMY%2F4WiRqrF4r7%2Bci5KerddSZqCGc7RQo5mPJU7ZrtCaURFdc92LfpUPvuHnptdrPVqvwNB4UTK1vWAIsCenHGOvnwYVcwX9S2OfPOYuwZ4dPy5sH%2FRFFXkxlfSUkcumc8Rd7qwa79bCKzYYBJZBbZGjTYY70TOsdkQKXdtOZS2gWostjjU5FXv5DgDC9DVufDNMhtTi3XYkEYpBnVjh%2FXNR8vTDP%2F5YCRjAzX5L9%2F24sqhHk5D4yKNQFogLoWorrSr421BCOaOfooH55hRkouwDCrMO8Kw4pHuOO9cpEPifZaiNM%2FVVV1KVKxmfmuNgE0%2Bpqe1VfdC6CBtdM5G4bAkpQj9clEMATOrXaX%2BtrHmEN%2FvLbFryQHEo0GphnN6w%2B3sDokEeMSBk0kiV2rcDsFCdpSeRNmNHep7mCep9FYUHchgmjlOWfeCa13II%2BsejbOc3GGxKAFDFPnkwntjYcO7x7V3ar7zc28x1sCSHgPpmDJ4jgS3WVs%2FfzuWNknYlnkRIwtOzhygY6pgF%2FdfcUgsrzYLtIqgXvF1%2BWAr9eAe3YuES5rNHMf43chnN1%2FjOOlcY8DmE65ydr28RimH%2F6AMbkm9pzQfulyrYRNdG1R%2F2q2qrfjRpVcN1SOzRlTqsaDzXvlL3ARQGPEl0wIV8co9todZ171YhElBP1d5Cpv7q6mq7l1z4IY%2F4FrE8oTtS7QIJFbCgHibwhrMrosd8HRpcJ%2BiFATuNzzH2S0KHWs6cI&X-Amz-Signature=8004a78cf52f28931651a6eefdb794018ad31048960c6b6157438dcc9e5ad0d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









