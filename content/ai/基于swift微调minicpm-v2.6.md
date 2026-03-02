---
title: 基于Swift微调MiniCPM-v2.6
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- MiniCPM
- Fine Tuning
categories:
- AI
---

记录本人使用自定义数据, 从处理文本/图片, 到构建Train.jsonl, 最终使用SwiftLora微调MiniCPM-v-2.6的全部过程.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662X342G7D%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmuHObbTijIVlC5QXZktV4GPY0cwQmGleGz0dx1qajVgIgCPF%2BlC5%2F90b%2B0kETePsPnPYFwz4vsIVp7LM%2FEV3mgCEq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDCOohWv8R%2F5zzK1FlircA%2FOGEiXpbKtLdR1FCYLFCGK7wTHYuDoYogYgm7zE108DBYY4Brnrr6SsJ%2FisxAsgr48I0FobDrSeZ4i2Dc%2FbyG61lkcafpLlF1I0uk7dO9qN9CjiNTiOD17cl%2Bgwk4IBpNO5woQx1505Y1Iqyv%2Fj3U1Bqxw%2BX%2FMuH%2BKSLVZnBJLGDVWosyrkHW2aBR40IE7p9X%2BVgp1ABz61F2tIW3QcjIU1JLbpCumYK8NDuYjgsRhILt%2BfTER8nBxAbwvVGblU4LhXyoVFiFsClBhmXstziDlq1riNGCZNm5Vwqh4boarUsm%2FMjism3ROH0dF3AUqVXgglHnHsJcnMLoLr4h3UE19r4TZJxS5z8hIufxX%2FvI74cqiFDuNcLUTQWsJakJyqvtousYaGlAosCxhmZnzqtzSkeudLd5j%2B%2B7pNw%2FQKpvAiVPq0TRJ4pgo2hF2pXeEWkP54k6MCzeDLHos1NCppRa5u2YxGrnFEWaA2Wd%2Fq%2FmEtd5HlVALhSIc15yD%2FOTJ0zmnGcXOHYLI4eAeJP%2Ff34CUnCFzATPAhT9%2B4r2bLX7QT%2BqEGW6AEDqe7yCcYEf41IoIbaggGTYuGListb7fGC%2BPp8QJX%2FqmXitvdh7AhS%2F%2FUcXu9P0njgfzqxGVpMIL%2Fk80GOqUBMv%2FNH5j%2FiK74fDViQmfBMMC1Eld%2BpjxyDSSfqUa7SmrCrxBxX6IwqTdgkzORuHeQIIt2d0TieerxArMurbfU5H3u2Snm1jxngUewEcBJTxfDc9Vh1oQzz8sx%2Fl3lcNtDKFZyxWqIKz%2Ff5OhTsv8HWbOZPRcp02bGNLtk0QxZGtzghxwpx82mdTjDFnPMM4CH5Yv7sySL1Rd9b5oOEp%2B03e5yNMoe&X-Amz-Signature=8b74aa3da43588f6049862cb16f2b937bcd7ea4c63a57c3c06b502309fe0a036&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 下载模型

- 方法一(手动下载):
- 方法二(huggingface-cli):
---

### 安装推理/训练框架(Swift)

- 源码安装
---

### 数据处理

- 使用自己的数据, 需要最终处理为jsonl格式, 考虑到数据保密, 在此不展示真实数据.
- 数据集格式可以自定义为以下几种格式 :
- 处理为train.jsonl的最终截图：
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662X342G7D%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmuHObbTijIVlC5QXZktV4GPY0cwQmGleGz0dx1qajVgIgCPF%2BlC5%2F90b%2B0kETePsPnPYFwz4vsIVp7LM%2FEV3mgCEq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDCOohWv8R%2F5zzK1FlircA%2FOGEiXpbKtLdR1FCYLFCGK7wTHYuDoYogYgm7zE108DBYY4Brnrr6SsJ%2FisxAsgr48I0FobDrSeZ4i2Dc%2FbyG61lkcafpLlF1I0uk7dO9qN9CjiNTiOD17cl%2Bgwk4IBpNO5woQx1505Y1Iqyv%2Fj3U1Bqxw%2BX%2FMuH%2BKSLVZnBJLGDVWosyrkHW2aBR40IE7p9X%2BVgp1ABz61F2tIW3QcjIU1JLbpCumYK8NDuYjgsRhILt%2BfTER8nBxAbwvVGblU4LhXyoVFiFsClBhmXstziDlq1riNGCZNm5Vwqh4boarUsm%2FMjism3ROH0dF3AUqVXgglHnHsJcnMLoLr4h3UE19r4TZJxS5z8hIufxX%2FvI74cqiFDuNcLUTQWsJakJyqvtousYaGlAosCxhmZnzqtzSkeudLd5j%2B%2B7pNw%2FQKpvAiVPq0TRJ4pgo2hF2pXeEWkP54k6MCzeDLHos1NCppRa5u2YxGrnFEWaA2Wd%2Fq%2FmEtd5HlVALhSIc15yD%2FOTJ0zmnGcXOHYLI4eAeJP%2Ff34CUnCFzATPAhT9%2B4r2bLX7QT%2BqEGW6AEDqe7yCcYEf41IoIbaggGTYuGListb7fGC%2BPp8QJX%2FqmXitvdh7AhS%2F%2FUcXu9P0njgfzqxGVpMIL%2Fk80GOqUBMv%2FNH5j%2FiK74fDViQmfBMMC1Eld%2BpjxyDSSfqUa7SmrCrxBxX6IwqTdgkzORuHeQIIt2d0TieerxArMurbfU5H3u2Snm1jxngUewEcBJTxfDc9Vh1oQzz8sx%2Fl3lcNtDKFZyxWqIKz%2Ff5OhTsv8HWbOZPRcp02bGNLtk0QxZGtzghxwpx82mdTjDFnPMM4CH5Yv7sySL1Rd9b5oOEp%2B03e5yNMoe&X-Amz-Signature=e0abb740d245f5078f86e2119e8bfe7e9c9f5602ef346a3d86607be8c723e70d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662X342G7D%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmuHObbTijIVlC5QXZktV4GPY0cwQmGleGz0dx1qajVgIgCPF%2BlC5%2F90b%2B0kETePsPnPYFwz4vsIVp7LM%2FEV3mgCEq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDCOohWv8R%2F5zzK1FlircA%2FOGEiXpbKtLdR1FCYLFCGK7wTHYuDoYogYgm7zE108DBYY4Brnrr6SsJ%2FisxAsgr48I0FobDrSeZ4i2Dc%2FbyG61lkcafpLlF1I0uk7dO9qN9CjiNTiOD17cl%2Bgwk4IBpNO5woQx1505Y1Iqyv%2Fj3U1Bqxw%2BX%2FMuH%2BKSLVZnBJLGDVWosyrkHW2aBR40IE7p9X%2BVgp1ABz61F2tIW3QcjIU1JLbpCumYK8NDuYjgsRhILt%2BfTER8nBxAbwvVGblU4LhXyoVFiFsClBhmXstziDlq1riNGCZNm5Vwqh4boarUsm%2FMjism3ROH0dF3AUqVXgglHnHsJcnMLoLr4h3UE19r4TZJxS5z8hIufxX%2FvI74cqiFDuNcLUTQWsJakJyqvtousYaGlAosCxhmZnzqtzSkeudLd5j%2B%2B7pNw%2FQKpvAiVPq0TRJ4pgo2hF2pXeEWkP54k6MCzeDLHos1NCppRa5u2YxGrnFEWaA2Wd%2Fq%2FmEtd5HlVALhSIc15yD%2FOTJ0zmnGcXOHYLI4eAeJP%2Ff34CUnCFzATPAhT9%2B4r2bLX7QT%2BqEGW6AEDqe7yCcYEf41IoIbaggGTYuGListb7fGC%2BPp8QJX%2FqmXitvdh7AhS%2F%2FUcXu9P0njgfzqxGVpMIL%2Fk80GOqUBMv%2FNH5j%2FiK74fDViQmfBMMC1Eld%2BpjxyDSSfqUa7SmrCrxBxX6IwqTdgkzORuHeQIIt2d0TieerxArMurbfU5H3u2Snm1jxngUewEcBJTxfDc9Vh1oQzz8sx%2Fl3lcNtDKFZyxWqIKz%2Ff5OhTsv8HWbOZPRcp02bGNLtk0QxZGtzghxwpx82mdTjDFnPMM4CH5Yv7sySL1Rd9b5oOEp%2B03e5yNMoe&X-Amz-Signature=9688b3afd4c38b1c7d2c852da9148bd346df756bf23df3a414ff17a674805069&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 合并权重+推理

- 运行推理命令
- ckpt_dir 微调后的模型权重地址
---

### 效果演示

> 根据上一步合并, 已经得到了新的模型权重, 位置在/你的服务器地址/root/autodl-tmp/.autodl/output/minicpm-v-v2_6-chat/v0-xxx/checkpoint-xxx-merged

- 使用Swift的web-ui推理演示
- 使用Swift的cli推理演示
- 使用MiniCPM代码库的web-ui推理演示
- 使用Python代码推理演示
> reference

