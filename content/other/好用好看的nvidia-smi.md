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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QY76HR3%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDR4IsTxSpq45W7mM1b2DIitTCdK8HmjYRDlbgxKXTmswIgT3Ctw7RwfeujaDcugu3w1iEbShfuQI0yXt1q%2Fevrd8oqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKbasqg0b6S1TsjzUyrcA8fjtWqNuY62cKdzVqDrwavsSPQ4mnoUx%2Fvjmei5tcMsOiBbwMfjzeeZB%2B1kvD2LQ9pv95Hoow%2F3E9sxGLttgy6t0Tq18zlTWggFmAznC2w%2BarG6wmXoDC0cd7Xpg93JELrpV%2BR7V%2Fh%2BE9Ikzt96nq4mU0MT%2FZQhp3T41nPp632Z49Zqcq7ywnpJlSlQPF9URDpaqjSdUSBD4ZCSPV7%2BLCwGfw%2Fld%2Bpjdte5WI%2FVN370z4r1nQaHHm8ukyPBLPA4DG9%2F0GvYm1r6gDXMc38uQkNDhAX1kSQH3ojxPf4Rux6rt4N0TM5XQUyDnPvMlRIcEp9JCZOQ4eVrEwbKzOyB%2BZCwHA2EE0IFp9RRKwn9UqjZlXqQafVqPSww6I218uINXoeiacS3Cz%2B3VnEMDyHZqfptcGnWTl31OWjpAaB7g38yhORVmVH30ab0NsoQJTfSjw%2BB1MBmGwO1EJ5Dw6q6mIuU%2FAQz%2BLcrzbU%2BLnnu6lcS16Wz58aUtR1k%2BQaQ9oosi%2BdpvvEL%2F1K0hBNa0P247njO4pIK%2BaIIrxi82eE1tzVtXqE4jEAKg0iAmQA7pFpRlepVORo6VUMgnCl9fsrAuOV%2F%2BeeEpFTgDwjEXB%2FpPlnnN5xhfafcrnTHBxZjMKzysM8GOqUBKIAzaHRCc6bb9SKALt5Tcj6uF0pggIc89CyNtJGQ2P1KObfzZ9IKnlEcrswQ0CnMobuzOH5vH%2F3DcSalni%2FjPJN%2BpUrZR6gEqsnKeTpmCIwpJ0XXY0bf3%2BH1zLrrnYvHfreLscumULKKXqrTykJsjq%2FJVcO6Ejwj0i0FT127fAo9Xul8h8zj31lhZnE7lh65n1TxDSWxIq7F4gvnotQGobXE2e5J&X-Amz-Signature=823346e351cb2bb9bf398b14bad54acfebe32de2a769741b1f95a5fce1d6ba03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QY76HR3%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDR4IsTxSpq45W7mM1b2DIitTCdK8HmjYRDlbgxKXTmswIgT3Ctw7RwfeujaDcugu3w1iEbShfuQI0yXt1q%2Fevrd8oqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKbasqg0b6S1TsjzUyrcA8fjtWqNuY62cKdzVqDrwavsSPQ4mnoUx%2Fvjmei5tcMsOiBbwMfjzeeZB%2B1kvD2LQ9pv95Hoow%2F3E9sxGLttgy6t0Tq18zlTWggFmAznC2w%2BarG6wmXoDC0cd7Xpg93JELrpV%2BR7V%2Fh%2BE9Ikzt96nq4mU0MT%2FZQhp3T41nPp632Z49Zqcq7ywnpJlSlQPF9URDpaqjSdUSBD4ZCSPV7%2BLCwGfw%2Fld%2Bpjdte5WI%2FVN370z4r1nQaHHm8ukyPBLPA4DG9%2F0GvYm1r6gDXMc38uQkNDhAX1kSQH3ojxPf4Rux6rt4N0TM5XQUyDnPvMlRIcEp9JCZOQ4eVrEwbKzOyB%2BZCwHA2EE0IFp9RRKwn9UqjZlXqQafVqPSww6I218uINXoeiacS3Cz%2B3VnEMDyHZqfptcGnWTl31OWjpAaB7g38yhORVmVH30ab0NsoQJTfSjw%2BB1MBmGwO1EJ5Dw6q6mIuU%2FAQz%2BLcrzbU%2BLnnu6lcS16Wz58aUtR1k%2BQaQ9oosi%2BdpvvEL%2F1K0hBNa0P247njO4pIK%2BaIIrxi82eE1tzVtXqE4jEAKg0iAmQA7pFpRlepVORo6VUMgnCl9fsrAuOV%2F%2BeeEpFTgDwjEXB%2FpPlnnN5xhfafcrnTHBxZjMKzysM8GOqUBKIAzaHRCc6bb9SKALt5Tcj6uF0pggIc89CyNtJGQ2P1KObfzZ9IKnlEcrswQ0CnMobuzOH5vH%2F3DcSalni%2FjPJN%2BpUrZR6gEqsnKeTpmCIwpJ0XXY0bf3%2BH1zLrrnYvHfreLscumULKKXqrTykJsjq%2FJVcO6Ejwj0i0FT127fAo9Xul8h8zj31lhZnE7lh65n1TxDSWxIq7F4gvnotQGobXE2e5J&X-Amz-Signature=f99e8466c42913dbf006c0d115115306ff8dc0feb1bd2276bb1f5543d1895d15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









