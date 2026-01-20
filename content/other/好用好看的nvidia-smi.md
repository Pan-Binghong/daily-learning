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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOM7VVCI%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGgQYo4ll4UK5aryeZisGSyJFVxJQwk24Ood40VNd3ZnAiEAq1aYsLxecNk3uytWAMavDmOznn%2BIwI6BKKcLlsfr8hkqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIrP4cgmhjEsyed3SrcA0XOkZlHKYCDBjg6IebZzQnKW4d7EHWkt77uQfZQdy4JGVjpM3inEXtR2Ig56bSSz%2BZ014DRsIJxnBiLM%2Baet%2FjvJaO4A6b3Rjwqvj0HkbrH1N%2BduV0FDRxJMIokdFPpcpUQpOt69ZXKnO5MFsCC8dBT80ZJC56U9AEg6URzbKMTUuiGejQXl1HINsKlbsHnfn6D6PucMxSn7tbE2ObCUO8EsgFYfd93dTPi3gzGHddmqTqXxnDKdgpUmRK9N5WHaS9%2Ba6E7SSKaD2dN4Xn5dfd00RwIoaMtIaBXUASdXl%2BKPIW%2BF3JklRQCtLAK61PJzTFGVTFWwdVH36PesUSGrS%2BcXULE4aWBBnoteFxS4dP57jhim2TrOFgnP3BF6yFNhrVB%2BgEGVsMZ1tNFO%2Ba%2F4xQsNx%2FqfyL4mCLN18fEMRJBObRUTO28wlM%2FIi4SWp4peITic5nfXnVD%2FXHpUgrHvikY0f6Ju5bMdwXYEG5nQf9gJmjsvaXRC0XNIijkDBUk8pRg%2Fag%2FOgGxAh7vLMM9zc9Tr5LaOFlKxFQpvnJXQhE3KQFWXq8Svn84LpAn2CPerke%2FHW%2FrHqHeYFm0QeBQElwztB%2BEv3dcvVFKMhOFGg6FHxdQAnE6iTb0Zn4zMKb1ussGOqUBKVXXpuRHHuGifeo3mIEm0LEPF9LAgQ8gMappm0%2BgmQluBARd3WMEMFn4aElV6A%2BRKDXjWK99151KjkoPTqFfqNUEx%2Ftv4ZkWDGlIuKk4BqfPKoTF6gNklhxjg%2FxU%2BsJmg2isaAzEVPf5FSZtvIfziE8EANTTw93PtOhFfyPU4Dze%2B8qCDs24S7%2Bc6wHU1A3T7mS9lZXHaz%2FLN%2BhWTcYde6kR1Zjg&X-Amz-Signature=dedb859c01a186a9a00dec8f3c3ef5db9a9a5f6ad85e158096c78d92e80c9945&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOM7VVCI%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGgQYo4ll4UK5aryeZisGSyJFVxJQwk24Ood40VNd3ZnAiEAq1aYsLxecNk3uytWAMavDmOznn%2BIwI6BKKcLlsfr8hkqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIrP4cgmhjEsyed3SrcA0XOkZlHKYCDBjg6IebZzQnKW4d7EHWkt77uQfZQdy4JGVjpM3inEXtR2Ig56bSSz%2BZ014DRsIJxnBiLM%2Baet%2FjvJaO4A6b3Rjwqvj0HkbrH1N%2BduV0FDRxJMIokdFPpcpUQpOt69ZXKnO5MFsCC8dBT80ZJC56U9AEg6URzbKMTUuiGejQXl1HINsKlbsHnfn6D6PucMxSn7tbE2ObCUO8EsgFYfd93dTPi3gzGHddmqTqXxnDKdgpUmRK9N5WHaS9%2Ba6E7SSKaD2dN4Xn5dfd00RwIoaMtIaBXUASdXl%2BKPIW%2BF3JklRQCtLAK61PJzTFGVTFWwdVH36PesUSGrS%2BcXULE4aWBBnoteFxS4dP57jhim2TrOFgnP3BF6yFNhrVB%2BgEGVsMZ1tNFO%2Ba%2F4xQsNx%2FqfyL4mCLN18fEMRJBObRUTO28wlM%2FIi4SWp4peITic5nfXnVD%2FXHpUgrHvikY0f6Ju5bMdwXYEG5nQf9gJmjsvaXRC0XNIijkDBUk8pRg%2Fag%2FOgGxAh7vLMM9zc9Tr5LaOFlKxFQpvnJXQhE3KQFWXq8Svn84LpAn2CPerke%2FHW%2FrHqHeYFm0QeBQElwztB%2BEv3dcvVFKMhOFGg6FHxdQAnE6iTb0Zn4zMKb1ussGOqUBKVXXpuRHHuGifeo3mIEm0LEPF9LAgQ8gMappm0%2BgmQluBARd3WMEMFn4aElV6A%2BRKDXjWK99151KjkoPTqFfqNUEx%2Ftv4ZkWDGlIuKk4BqfPKoTF6gNklhxjg%2FxU%2BsJmg2isaAzEVPf5FSZtvIfziE8EANTTw93PtOhFfyPU4Dze%2B8qCDs24S7%2Bc6wHU1A3T7mS9lZXHaz%2FLN%2BhWTcYde6kR1Zjg&X-Amz-Signature=1cac250f30da5bab605bbe3c4edfadb1efde24ce2e276d4ec278b4aba1ad3e00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









