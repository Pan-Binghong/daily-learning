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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXNCYITD%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGE1w2LgUTbSSPwUONo%2BdbTRoyLpYpHntfAS3%2F9%2BbVqzAiBkRnOX%2FJRTFesLr7Wns5GcP%2F1ZCb3%2FAYYx2WpmJ%2BREUir%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMvdXoezThJzJj599%2BKtwDDoC2DRZC429hoXrHFDMY%2BL21A3IwS30Y2TLE%2FXd%2FeziLYSfMrfG8wlmAULFsWBZs3ezPWWdMRhCnk8YTUOxDaYTL0fZp%2FCh%2ByzJEtGab8h5csaIn4xHCgR92rIlfhLyb2ZdCcNqA2GFN71w6EC7sPx%2BsQ0ltkv%2Blt6ledvqMtc%2F%2F2PmYbY82MCGS6A5DYw00l5qI88b%2Ffns%2FvvXCkpfMSnuumHHj8EqIeDnU6YNXN4kMIaZSy1hqBzsU3SXZBNkXIBtDVPTdHjpcXsEltTFlR%2F8Lu2F2rI9gULW8aqkyxUJH%2FxS794Pf%2FobDlApIjdjXD83lJ7g%2B7pZJ%2B2LM%2FppxyxDGn9d%2FzKhGHlPoHHWl9Kzo25PRtS%2FTrnxPEKXKh%2FNYHBfB6ZNmZXYtelduM0Hz%2FNIjO2crrbutfyDrmOBdUILgjqzExw40f%2Bb6sDzP1lFc0POSEIWiwasHXVhQr15CXbLRmXMA3U2VnDZ%2Bc%2F6XLW9jUKmaMc3jT5t%2FIY550wgKV7bGXAtkiMaPfQaft3WBufclaW7tCzR7Qv2G4yaFc0%2Bn2cFrYC66rbwniUiOp0O3Dk53UHNettlng4r%2BmeCnakvtjZ5RlnYIAdullqXopN19g2XWSzTfANxyfEAw%2FcDfyAY6pgHfcOTc2oxxHNNbRlC9PbF8EviTPOoTpF%2BmGEuoDoY117E11TbJ%2FR5MBe7%2F%2BuPE4cSCWuDJ7ifIz9%2BotuofT6pyYl%2FzwzDc9gINs5cvdiRpmv79IiH7YFvTAJ8Muk6FbEpd6DTxp5YPhCu%2F7aMMSfEc9kkqcPW6ODR3wgnKOohzxUEbYz4Rh7X66YD3He9FzL9T5tE0uW3baE2KcmUJ4uLIgSEnAEMc&X-Amz-Signature=6c45671eef1e5e114152e3959131ce26e4d862f19dd077a13f61b9fc49d85e30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXNCYITD%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGE1w2LgUTbSSPwUONo%2BdbTRoyLpYpHntfAS3%2F9%2BbVqzAiBkRnOX%2FJRTFesLr7Wns5GcP%2F1ZCb3%2FAYYx2WpmJ%2BREUir%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMvdXoezThJzJj599%2BKtwDDoC2DRZC429hoXrHFDMY%2BL21A3IwS30Y2TLE%2FXd%2FeziLYSfMrfG8wlmAULFsWBZs3ezPWWdMRhCnk8YTUOxDaYTL0fZp%2FCh%2ByzJEtGab8h5csaIn4xHCgR92rIlfhLyb2ZdCcNqA2GFN71w6EC7sPx%2BsQ0ltkv%2Blt6ledvqMtc%2F%2F2PmYbY82MCGS6A5DYw00l5qI88b%2Ffns%2FvvXCkpfMSnuumHHj8EqIeDnU6YNXN4kMIaZSy1hqBzsU3SXZBNkXIBtDVPTdHjpcXsEltTFlR%2F8Lu2F2rI9gULW8aqkyxUJH%2FxS794Pf%2FobDlApIjdjXD83lJ7g%2B7pZJ%2B2LM%2FppxyxDGn9d%2FzKhGHlPoHHWl9Kzo25PRtS%2FTrnxPEKXKh%2FNYHBfB6ZNmZXYtelduM0Hz%2FNIjO2crrbutfyDrmOBdUILgjqzExw40f%2Bb6sDzP1lFc0POSEIWiwasHXVhQr15CXbLRmXMA3U2VnDZ%2Bc%2F6XLW9jUKmaMc3jT5t%2FIY550wgKV7bGXAtkiMaPfQaft3WBufclaW7tCzR7Qv2G4yaFc0%2Bn2cFrYC66rbwniUiOp0O3Dk53UHNettlng4r%2BmeCnakvtjZ5RlnYIAdullqXopN19g2XWSzTfANxyfEAw%2FcDfyAY6pgHfcOTc2oxxHNNbRlC9PbF8EviTPOoTpF%2BmGEuoDoY117E11TbJ%2FR5MBe7%2F%2BuPE4cSCWuDJ7ifIz9%2BotuofT6pyYl%2FzwzDc9gINs5cvdiRpmv79IiH7YFvTAJ8Muk6FbEpd6DTxp5YPhCu%2F7aMMSfEc9kkqcPW6ODR3wgnKOohzxUEbYz4Rh7X66YD3He9FzL9T5tE0uW3baE2KcmUJ4uLIgSEnAEMc&X-Amz-Signature=9231636f899985164b2e71367ae15860279f651a9e1a75938ca5f38bcedabcd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



