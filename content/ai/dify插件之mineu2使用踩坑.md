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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GDQCAXR%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCQ5IcK2lvUpMvKuS2%2ByF5a4gKeicXeWb69qp%2BDWwEI6AIgc0WG4X65vm8WbwUTaCAJi9Z6%2FqwK%2Brn5qJ30pCSxOjsq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDL07f5goG23BwpkkPyrcA60ymVmQCyek6ubqnlhNr5haJ%2F%2Bcmd2K%2BDWw3iBGTGTxfPT%2BK%2FfVk7dl4NAwinUm7k80bRDVfaZl%2FiqtzHAy7fRtdHOACeW1xD23pUaJMuwk4xt6%2FOfcPfGX7yuEZFkP4AE%2BLDUg9zr3iHVEjDY2c9I1Mc0Mxhn%2BlOHhLS0%2FIfo3%2B0YF5tUStuiYma5IyhnMS%2FBRQqk%2FasylB0BMo9IQubN6VG5HmEfCvXwGMvLlKy1UkWX6ZaqcPDx%2B6R6s1PBRkzxeyVwhVmqHkjUWlghhu9Y3KLlhyNSVsBvcbpcMxFJsk5mRZJlYZSAaQ%2BBahPo%2Fm3QXaXt78HTFWPgwloYW4cXQSKCKZJA%2FKnVeVgi0XOIs%2BVECCx6H9LJya0phaS4w7ROd8EaE2ZMxsVy00F18uLSeu1SHJ1VjBrwF5oJGX0YN%2F99%2BmbovJMDd62onzXKvoD9G9O1mHh5IAwsG7qOgD9OyTLnOhf%2F%2Fyjhuae8tOPjlmBUsYAWjTnnTVSYgrCmzE%2BPQah%2Bf5OuBDKMzHwjONLJPaE6Ksr88InUvPyLD%2B6VEKuBGcaC1GXx%2F9FVsVQ9ikCBGIR5q4VnzU1MwuMHKrwtU%2BGtW9OCI%2FE%2F2MiJw7uNwuOL2rgFpVQfdZ2tKMObu68oGOqUBuT98moa6xuREnwDgwI9d3EZP63zPHmiaxIEQWkqhv%2Fchsw3IF79%2F4EMXbTiNI4b6ofa9dh27yXPDIK3ZH3kE39p71%2FN2SluHteU%2FeYwcf%2B5uCtbKjRRosY4ukxVzjfu8NWnvrd2pMUUw6HgmVBFU48Sxeh9bgP2tgtSPe1qVx2L%2B0gUd0KycvDaGVkoe7aZwpbL3SO0CU0P3Ug3w7GEAdmSR08Eo&X-Amz-Signature=4631a6122539445920f42da509e86845c6a5f763fc6e26a607067c0fe3d321f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GDQCAXR%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCQ5IcK2lvUpMvKuS2%2ByF5a4gKeicXeWb69qp%2BDWwEI6AIgc0WG4X65vm8WbwUTaCAJi9Z6%2FqwK%2Brn5qJ30pCSxOjsq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDL07f5goG23BwpkkPyrcA60ymVmQCyek6ubqnlhNr5haJ%2F%2Bcmd2K%2BDWw3iBGTGTxfPT%2BK%2FfVk7dl4NAwinUm7k80bRDVfaZl%2FiqtzHAy7fRtdHOACeW1xD23pUaJMuwk4xt6%2FOfcPfGX7yuEZFkP4AE%2BLDUg9zr3iHVEjDY2c9I1Mc0Mxhn%2BlOHhLS0%2FIfo3%2B0YF5tUStuiYma5IyhnMS%2FBRQqk%2FasylB0BMo9IQubN6VG5HmEfCvXwGMvLlKy1UkWX6ZaqcPDx%2B6R6s1PBRkzxeyVwhVmqHkjUWlghhu9Y3KLlhyNSVsBvcbpcMxFJsk5mRZJlYZSAaQ%2BBahPo%2Fm3QXaXt78HTFWPgwloYW4cXQSKCKZJA%2FKnVeVgi0XOIs%2BVECCx6H9LJya0phaS4w7ROd8EaE2ZMxsVy00F18uLSeu1SHJ1VjBrwF5oJGX0YN%2F99%2BmbovJMDd62onzXKvoD9G9O1mHh5IAwsG7qOgD9OyTLnOhf%2F%2Fyjhuae8tOPjlmBUsYAWjTnnTVSYgrCmzE%2BPQah%2Bf5OuBDKMzHwjONLJPaE6Ksr88InUvPyLD%2B6VEKuBGcaC1GXx%2F9FVsVQ9ikCBGIR5q4VnzU1MwuMHKrwtU%2BGtW9OCI%2FE%2F2MiJw7uNwuOL2rgFpVQfdZ2tKMObu68oGOqUBuT98moa6xuREnwDgwI9d3EZP63zPHmiaxIEQWkqhv%2Fchsw3IF79%2F4EMXbTiNI4b6ofa9dh27yXPDIK3ZH3kE39p71%2FN2SluHteU%2FeYwcf%2B5uCtbKjRRosY4ukxVzjfu8NWnvrd2pMUUw6HgmVBFU48Sxeh9bgP2tgtSPe1qVx2L%2B0gUd0KycvDaGVkoe7aZwpbL3SO0CU0P3Ug3w7GEAdmSR08Eo&X-Amz-Signature=bcd9278b29cd3a54e8a543460385113170714226221a51283b4a47d43c8bfde2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



