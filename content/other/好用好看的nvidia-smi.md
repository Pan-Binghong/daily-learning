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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HGRFNAL%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBykrKoBeULFn4QC5p2f7oELay6P7Ud47LjJFNB2J20jAiEAqJNb9iLSrRedW%2FJQciihfTyeEDmPw9JivevmMaUjYxgqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2Fgag7q0uizBXxzOyrcA8FR0l%2FFI0GUoCgvr%2BXq08i6toHUSmlXtJZHVPxAKnwvJEUo6N%2FJBscRKM8uGV999pqJMOVOTlx550VfYfoXtRf3LJn%2FXG1JmbzdgCDNU4T%2Fu7qiptw8TsAqo2aj0cW3sJrKLVoFWwojX8QUO6JhmsyHdelyWEnIbsncAYsWyLTGqOzUvjxf%2F3gSo7nsG2D0FUuWhFRDyy96DqmvX39w73Xf3FJ%2BIuyQh7uzvX0WqQSQJFljZxNWmt0CnmWk2f6t4vnQb4DIS%2BSvbbO7R20I%2FHug5bx49ihe6QVzlQOXaICvOCtMR91CzQx0FwekViAq5j40JpYyF8l9eiuT5VuzL%2B4hewfrdsdM%2BNvs53zRlLJiO2aVewH%2BDmdYrXphWQiqmeWsEpv%2Fg3CHBu9muO820eu87FiKXrnDxiRFH0uN%2F8RoODl1DvMu83QHMmeNa4YB8m0UyMdbJnzjlDO%2BL715P0v6%2BC%2FSnMvtFTslVdmqPLASN6MjZ3BWvbLCJI9z9m2NcjPGDYdjlk3FEZDMD92EX91mdP7Qhs%2BUodWsUPGPwBRsZP7eNUV%2BLhCV8uovA1d6LXWgzkA%2Bgeka8h9LBIY3NuBMNtp2wVMPV2Iu65%2BBONpFacZYazwRAZGNkqojMIbao8kGOqUBdRsJplds7%2BidXDoWZbWrBd5T9Fjy1iXzA6OPVSx%2B5VbwRpkmymvjH4VnISEDbLIIn9dd1x0CFvVUiVYC8fRbOJl2WQiDDZifcxWKq8qfEfU82yqCazfod8bfqbFGqAchgZGVdfacOBx9R0%2BbI95iMzQbWCXEGSDlfKZascsG38c4bYFXuxEAg3Bdr7HsErrk3jenoIQKtyWRoHHGf%2BnXmwdHnzxe&X-Amz-Signature=27aa6b2291d7d856c5228a54466111672622ce1abcbd1309485dc1e082fdafad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HGRFNAL%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBykrKoBeULFn4QC5p2f7oELay6P7Ud47LjJFNB2J20jAiEAqJNb9iLSrRedW%2FJQciihfTyeEDmPw9JivevmMaUjYxgqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2Fgag7q0uizBXxzOyrcA8FR0l%2FFI0GUoCgvr%2BXq08i6toHUSmlXtJZHVPxAKnwvJEUo6N%2FJBscRKM8uGV999pqJMOVOTlx550VfYfoXtRf3LJn%2FXG1JmbzdgCDNU4T%2Fu7qiptw8TsAqo2aj0cW3sJrKLVoFWwojX8QUO6JhmsyHdelyWEnIbsncAYsWyLTGqOzUvjxf%2F3gSo7nsG2D0FUuWhFRDyy96DqmvX39w73Xf3FJ%2BIuyQh7uzvX0WqQSQJFljZxNWmt0CnmWk2f6t4vnQb4DIS%2BSvbbO7R20I%2FHug5bx49ihe6QVzlQOXaICvOCtMR91CzQx0FwekViAq5j40JpYyF8l9eiuT5VuzL%2B4hewfrdsdM%2BNvs53zRlLJiO2aVewH%2BDmdYrXphWQiqmeWsEpv%2Fg3CHBu9muO820eu87FiKXrnDxiRFH0uN%2F8RoODl1DvMu83QHMmeNa4YB8m0UyMdbJnzjlDO%2BL715P0v6%2BC%2FSnMvtFTslVdmqPLASN6MjZ3BWvbLCJI9z9m2NcjPGDYdjlk3FEZDMD92EX91mdP7Qhs%2BUodWsUPGPwBRsZP7eNUV%2BLhCV8uovA1d6LXWgzkA%2Bgeka8h9LBIY3NuBMNtp2wVMPV2Iu65%2BBONpFacZYazwRAZGNkqojMIbao8kGOqUBdRsJplds7%2BidXDoWZbWrBd5T9Fjy1iXzA6OPVSx%2B5VbwRpkmymvjH4VnISEDbLIIn9dd1x0CFvVUiVYC8fRbOJl2WQiDDZifcxWKq8qfEfU82yqCazfod8bfqbFGqAchgZGVdfacOBx9R0%2BbI95iMzQbWCXEGSDlfKZascsG38c4bYFXuxEAg3Bdr7HsErrk3jenoIQKtyWRoHHGf%2BnXmwdHnzxe&X-Amz-Signature=120e9473669952da5c7f2a693c27075cbce858cafe3e6366d93a4a8721f2820f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









