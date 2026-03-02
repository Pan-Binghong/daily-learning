---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X5GOMJF%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDCblruI45p%2BaUtOP%2F3Sizg6OD2w1MzmwD0Tk2CwxpkHAiEAiqdt%2BFyDdipfcv%2Bb3jof0AJoHTnCrCJ4%2BuPJzsIhnK8q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDJpZb3KrvEhG9bzokSrcA7%2BCvyJaxXo9hMguLRKDvABXQIGbc5cetSO5XrCYWw33Bf6Pg6BBuu2E92Jm9DRzTVur%2B8JlRLOznilIerqUxA8otQz75RPABDgfliAPXAqDyJcBNoqyRp5b8CWUp8NN5phKquM7HH%2F71lraE9iparB1PvUAvWToblFb38R2X7Wa73VpgGAMjMLztplmYE2jy81t5DgaQibPTx10qe41h%2BUcu1eZv0IB5EJJq98aeo2kNs1fp8yAMVobBwz9R1GHFNNA2gJZQwBYA1FoMbR%2B2Zf5wmMpeguIga%2F%2BN1Tnd9uQ%2Bcmef%2F2L4Rtg4j4jjbm0j2qMVRlfooYCq%2FxPr7kn8fVRV3RvFbWzyhsIOUh%2BKPCciZoZy%2B3eUNofRWkuYNqJUlxadHShPqEvFdHT7YDGuaqn3QqHAxMtyztBYpbXuFdUUsENCtXUNW3vRLiYUR9MbKUbiXOmANu818chpFaSgr33HpaC4zkS%2Fk63LmoAB0uPIkzFfCdfmSY12gLWhi5VEfJIpw%2FQKqskD3WATveq%2Fe245lJ9adi1nwODD8oqRE%2FumHiayNzsOZMvQl3IkF23nasCivXoVdZ1gvTQ1hLukvjM7hgcPoa5uCkobfw%2Fz7KLwl%2FTMpZKlxIZMD4iMMn9k80GOqUBKVrENEF7RGYga2w4rgE5WBw93G5o3AAkurAGmGX2VDypADuo9iIQS5gkDh7%2FNYomHbivxTO8q30iExcRXgzBS%2FKRCjvHBkP33MWeGxkLDn06qV%2BCLudzk1PUHbcZlU5IKWugXAcsEPD4EsQna74huN0nhFIll2HlgAVRMswH7dEo6ZsreKdZCCXJNpsACiKyFSDz8odxuXgs%2BcJGllaF951GDhXz&X-Amz-Signature=6ba01b17e9732c424c606f780544a56aedb76412de1887abff201c4dc5d93b69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X5GOMJF%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDCblruI45p%2BaUtOP%2F3Sizg6OD2w1MzmwD0Tk2CwxpkHAiEAiqdt%2BFyDdipfcv%2Bb3jof0AJoHTnCrCJ4%2BuPJzsIhnK8q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDJpZb3KrvEhG9bzokSrcA7%2BCvyJaxXo9hMguLRKDvABXQIGbc5cetSO5XrCYWw33Bf6Pg6BBuu2E92Jm9DRzTVur%2B8JlRLOznilIerqUxA8otQz75RPABDgfliAPXAqDyJcBNoqyRp5b8CWUp8NN5phKquM7HH%2F71lraE9iparB1PvUAvWToblFb38R2X7Wa73VpgGAMjMLztplmYE2jy81t5DgaQibPTx10qe41h%2BUcu1eZv0IB5EJJq98aeo2kNs1fp8yAMVobBwz9R1GHFNNA2gJZQwBYA1FoMbR%2B2Zf5wmMpeguIga%2F%2BN1Tnd9uQ%2Bcmef%2F2L4Rtg4j4jjbm0j2qMVRlfooYCq%2FxPr7kn8fVRV3RvFbWzyhsIOUh%2BKPCciZoZy%2B3eUNofRWkuYNqJUlxadHShPqEvFdHT7YDGuaqn3QqHAxMtyztBYpbXuFdUUsENCtXUNW3vRLiYUR9MbKUbiXOmANu818chpFaSgr33HpaC4zkS%2Fk63LmoAB0uPIkzFfCdfmSY12gLWhi5VEfJIpw%2FQKqskD3WATveq%2Fe245lJ9adi1nwODD8oqRE%2FumHiayNzsOZMvQl3IkF23nasCivXoVdZ1gvTQ1hLukvjM7hgcPoa5uCkobfw%2Fz7KLwl%2FTMpZKlxIZMD4iMMn9k80GOqUBKVrENEF7RGYga2w4rgE5WBw93G5o3AAkurAGmGX2VDypADuo9iIQS5gkDh7%2FNYomHbivxTO8q30iExcRXgzBS%2FKRCjvHBkP33MWeGxkLDn06qV%2BCLudzk1PUHbcZlU5IKWugXAcsEPD4EsQna74huN0nhFIll2HlgAVRMswH7dEo6ZsreKdZCCXJNpsACiKyFSDz8odxuXgs%2BcJGllaF951GDhXz&X-Amz-Signature=9b3f1f4c071896bcbaf244a3533e38817074667884b2e222771128d13d60eb1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

