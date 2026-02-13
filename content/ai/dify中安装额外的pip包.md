---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ2HBQA6%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIFI%2BoTUBmGNRXJm38UL7DefI%2FP8e%2FOSa%2BzLTrvL5TpM7AiAN6CSyzjnamgkHy786zNq%2Bd97SadvtAyhlrA4W3FvQqSqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcSizxgW%2BaGLyE%2B3hKtwDmBGAag6fRNUyTiVD195O4bCbCPZVLoh5bfq1gJixwao6kVQ0ZCDcR%2BSe9akYz32OZvokNdG0ZwqMlw25OuUSURv9v%2Bn4q5rP3Ioe0i07I7q4DYqApQAIC3TKKXYTKx%2FBTeqiubZ%2Fg6J%2BVeekyIsoMyPhbqRnbUaztEEII9YcxND0EMRr49PLb785ep1%2FYtKAUsy4dAQBNHY9E1PAMiT06cj23A81jR4xMdT8073WXaqUXViUV6UHgarJtvz72kYFPUK43SKPhy0TFEJ0%2BWoaX1KGvS7ydik8v%2BUd3xzFTj6CnJMHZIdoDjXOImJTy5oN%2FRcUyFDqYbg3K9ljOi1uU%2B3STu3rLksOwENFJE3DI98Ukov1wnCtEnqht3SXI55IfVK1O0I1iw7rlUOM3oRiH6VHX%2Fq3i%2Fepf1RB827IwkfZ8IvpjgJHqbjpnVZV9J64UI7vQbzEVOwYWWUC%2Fu%2BEcpzP5Sdd3z8gHUZeATP31rulF0HUwHvq%2BCgy5wmVXUXR0jsrPu3p2evj334wO4796nGXqkp1LPmLjcW74ggmR9t4VTQTaM8natawiVNGWlgn9tmpuKrZYR3OPGzLVXTR00VzGfUP0xGggNmcHbC%2BF5Pu0XTWRxlFPmVHJWEwtJO6zAY6pgHotcQJKkppWI89Z227HhISdCx%2F4w345BKIbJMBteslBO9QzBT%2BL8MLuf4YpATpM0pTGbEmG2rownRcqMN%2FwkrL9PWm%2BgZzQh7D6sxbvoypJuF%2F7UYii7TjVFMDT5DsjpNezNIx5cgh17bz8xa8h7Rn4MKfHp9bGHmaVBKuYFKdz9vn4NLGXrSetSPbLUk4B2u85mg7MHX%2BKD5d%2BdmIjMsVzvatrZ1o&X-Amz-Signature=acb4f3aa1b7ec4e40845258af02d5b739f198f760d80332b14cd776d1a55479b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

