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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIXYKJMX%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIDggihBA%2BGaPUcuyAjfXcXosLkK4rkjWlGnT1fokPKC0AiEArxoiE05ATMBDgX3cS%2BuMXD%2BbKYr7x2%2BTzRZFwDX54OgqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQKWOhR7VxCF1S1PSrcAyj7xycQs9k2Kdb%2BydJmBRct4HIfsfcHe2W08oWQtCzaChVPqGgIY8wJOsiKnrpDHJiL4tgpT1wtWc5HkFG6qW67BYceeUzMII5cp2LcBnsQyEimICe0k2nbUW7i4sTKZphhZ82yw7ReTQssPTwkPqZgsc7jzlbWGFP7D9lUuEV%2FCV%2BpTI%2FgBOoktAK4JjxjrZFyrbKb2Wnshjdtb6maG%2FUkwnyTtmZacQi9SPMrFSGhpCDWx0MXV%2BX%2FBc4KEilBA5%2FYiR%2FyxqD%2BtzdT%2FooAxaWxTDlCwzlssVqGCmdGFBsPIuDO9hdGlVVYgKBlttgAhFp2Wd%2Baah6l%2Bs%2FUlTCsrdWOiXm6urVj%2FHVcG6aqp1lzj6U5466Jg%2Fh1ovmP3mtVlid%2BS3WWhwHeYmFhWQpztvpaM0v2RQRsT%2FXemY38Wv3NE5j86HLnX7ZWJis47XpuxXSoYwIb7vnVx9wS%2BveyVmN4DJzRFZt4pu8NVgs0P9b%2FB91vL2FGnI%2Fhrv%2FqURP4yS09IMVIpEL%2FBzpG53RJZQ05JJ2JnoX54NajFt62NMcYm%2BWvoGJc9INm18jBy6cSVd0NVIQT4DkwLfKf13Onew8uS8PXsX5GGgbG7PsSNB3B%2FEnI52LC%2BgKLUnS4MIjPqM0GOqUBc4JgdUuxdMXH8wdKc7JARKxJXcDEGcnaUtt1mRSFGwHUQhUFbvbhdQfsbF0wNSX1V8wtMfbK60Is672RtMAaonvJAvqFf2UKFLpoAhzKu6Z6EHQXIXLKxeb5Fua8DMikc6JeG6Z6yosr%2ByStzd8OdsjjIDv377KX3Njx6VYkn7Rx3xjdMwyJO8bCjNt%2FvQo9mOjffEib7OXTCwBsIAF6%2BOsfMOIP&X-Amz-Signature=b31a0033f4a91c4e4fe09e8522f61163b9a02b24d9e40b792911a21e0ac00e40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIXYKJMX%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIDggihBA%2BGaPUcuyAjfXcXosLkK4rkjWlGnT1fokPKC0AiEArxoiE05ATMBDgX3cS%2BuMXD%2BbKYr7x2%2BTzRZFwDX54OgqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQKWOhR7VxCF1S1PSrcAyj7xycQs9k2Kdb%2BydJmBRct4HIfsfcHe2W08oWQtCzaChVPqGgIY8wJOsiKnrpDHJiL4tgpT1wtWc5HkFG6qW67BYceeUzMII5cp2LcBnsQyEimICe0k2nbUW7i4sTKZphhZ82yw7ReTQssPTwkPqZgsc7jzlbWGFP7D9lUuEV%2FCV%2BpTI%2FgBOoktAK4JjxjrZFyrbKb2Wnshjdtb6maG%2FUkwnyTtmZacQi9SPMrFSGhpCDWx0MXV%2BX%2FBc4KEilBA5%2FYiR%2FyxqD%2BtzdT%2FooAxaWxTDlCwzlssVqGCmdGFBsPIuDO9hdGlVVYgKBlttgAhFp2Wd%2Baah6l%2Bs%2FUlTCsrdWOiXm6urVj%2FHVcG6aqp1lzj6U5466Jg%2Fh1ovmP3mtVlid%2BS3WWhwHeYmFhWQpztvpaM0v2RQRsT%2FXemY38Wv3NE5j86HLnX7ZWJis47XpuxXSoYwIb7vnVx9wS%2BveyVmN4DJzRFZt4pu8NVgs0P9b%2FB91vL2FGnI%2Fhrv%2FqURP4yS09IMVIpEL%2FBzpG53RJZQ05JJ2JnoX54NajFt62NMcYm%2BWvoGJc9INm18jBy6cSVd0NVIQT4DkwLfKf13Onew8uS8PXsX5GGgbG7PsSNB3B%2FEnI52LC%2BgKLUnS4MIjPqM0GOqUBc4JgdUuxdMXH8wdKc7JARKxJXcDEGcnaUtt1mRSFGwHUQhUFbvbhdQfsbF0wNSX1V8wtMfbK60Is672RtMAaonvJAvqFf2UKFLpoAhzKu6Z6EHQXIXLKxeb5Fua8DMikc6JeG6Z6yosr%2ByStzd8OdsjjIDv377KX3Njx6VYkn7Rx3xjdMwyJO8bCjNt%2FvQo9mOjffEib7OXTCwBsIAF6%2BOsfMOIP&X-Amz-Signature=be5cbbe3d33766d9c4fdbf58ff1908a9fcf3e0f103530e78ff7f39578be8242c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

