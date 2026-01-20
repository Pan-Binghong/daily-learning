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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SPZWRGI%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFfVVx0cDIgtlfUJ%2FGVjonX%2BH%2FWRi1o2D%2F5XIhCKMZSjAiEA3dSyySD0oMJMeLjecQRHV1aaPJLVeTD%2BSICR2IpR9lUqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOQCjGpXAO%2FSOXXmTircA%2BYVUyIRly%2FBVGVCjgbrRWwBrmA4LlX4CCIyPlg9WtGHVklimJGXvJdlbDHYED0b%2FUPuxnNMcbHMRAQyb32II8Iu5gpzxfD%2F1toPnuN9oQmrcHTArvQQNeBxT%2BZbHC84aqinxb1peyk8O03Cop5E77apA6g8riPctFcwdIFTQwUqSbAusrLj3Tt0rMspuVuosJOjuD5EK7M%2B1et3Q2uZtCY%2B4MBL39evn7o2PFrrNmNakvgWRv7iFj4hh%2FNHmcSVdwgHnN61I1rWT6qoVDCTjmSIuddsoqLB7zZ6PPge6fD8yJu%2F56gps2C4p2Oy86YNCSeYbPlLpqruEq2WVkhXPkF4mO67OH9bBeLVPqyJidTXcxvF4pQb5wxQuKZz6RPerUJHqAlSLq4iubxeb86hyavDxDNN9orRvPEbB4HaThc9dylMhJDLdhQFCX8%2F3tVw4gezMtBAHePT1cW17zyo0IIxTSIe3G1bHYp%2BIQH71JKrkrhPguYBj1IGXhNAqd%2BEGBm4UAGJZv%2BOX7XtIcrGRF4yqAMUKGFyTFRtL9o%2Bhpmfhd%2FE9NHE3FLsPNVrfRJ5QJGCfmFsQTKMmuKl8bo65FLCVHeBnhs0XgnEqXz9tuV0cbuN6lY4HCvC00qAMPD0ussGOqUBQ7rUqj4hOOWCUWxluG8OqEbet77jxFARovZiPAcdm9l6EWII4o3%2FRbDK9TKzru3GfEyA7kao3hiHOAkyd7CRqm23hswewfLYWuuqJwMkY8PnxP9ChFQaqAM5AbmkI3TIhO1WkNqDs3of0adyUUSAXYbAPSPZTLPq%2FSd82hRjQXwykJJ2YeSCteMr4oyXBPqd4%2BJyZCRCyR6zAM4eIB2KwLtTFhdj&X-Amz-Signature=7e6c777c9754cb0ebf444fe68bb96dbe524fe32f505598f41cce587c5fc69858&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SPZWRGI%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFfVVx0cDIgtlfUJ%2FGVjonX%2BH%2FWRi1o2D%2F5XIhCKMZSjAiEA3dSyySD0oMJMeLjecQRHV1aaPJLVeTD%2BSICR2IpR9lUqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOQCjGpXAO%2FSOXXmTircA%2BYVUyIRly%2FBVGVCjgbrRWwBrmA4LlX4CCIyPlg9WtGHVklimJGXvJdlbDHYED0b%2FUPuxnNMcbHMRAQyb32II8Iu5gpzxfD%2F1toPnuN9oQmrcHTArvQQNeBxT%2BZbHC84aqinxb1peyk8O03Cop5E77apA6g8riPctFcwdIFTQwUqSbAusrLj3Tt0rMspuVuosJOjuD5EK7M%2B1et3Q2uZtCY%2B4MBL39evn7o2PFrrNmNakvgWRv7iFj4hh%2FNHmcSVdwgHnN61I1rWT6qoVDCTjmSIuddsoqLB7zZ6PPge6fD8yJu%2F56gps2C4p2Oy86YNCSeYbPlLpqruEq2WVkhXPkF4mO67OH9bBeLVPqyJidTXcxvF4pQb5wxQuKZz6RPerUJHqAlSLq4iubxeb86hyavDxDNN9orRvPEbB4HaThc9dylMhJDLdhQFCX8%2F3tVw4gezMtBAHePT1cW17zyo0IIxTSIe3G1bHYp%2BIQH71JKrkrhPguYBj1IGXhNAqd%2BEGBm4UAGJZv%2BOX7XtIcrGRF4yqAMUKGFyTFRtL9o%2Bhpmfhd%2FE9NHE3FLsPNVrfRJ5QJGCfmFsQTKMmuKl8bo65FLCVHeBnhs0XgnEqXz9tuV0cbuN6lY4HCvC00qAMPD0ussGOqUBQ7rUqj4hOOWCUWxluG8OqEbet77jxFARovZiPAcdm9l6EWII4o3%2FRbDK9TKzru3GfEyA7kao3hiHOAkyd7CRqm23hswewfLYWuuqJwMkY8PnxP9ChFQaqAM5AbmkI3TIhO1WkNqDs3of0adyUUSAXYbAPSPZTLPq%2FSd82hRjQXwykJJ2YeSCteMr4oyXBPqd4%2BJyZCRCyR6zAM4eIB2KwLtTFhdj&X-Amz-Signature=f4ca87c24ff79d8821dffb98235df6ad890d2f2ce5d53bba43e39efffeff8ad9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

