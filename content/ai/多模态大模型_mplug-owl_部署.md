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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNY3GZMN%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T024939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJHMEUCIQCMyHmjgzv0cKTI6Mf3u4OH5vHFGA8GFpnbJLxM%2B167eAIgEfoYTdDfII8et%2FbSnHEdJRBOWHNUGnaeOBXXy42G74Yq%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDHPvVpapQCoTVbt18SrcAw9yUO2QLYzTTmTS%2Bv953OzVDm31L%2FqaZEpjxm1t1HyK%2FsOzkVrtwTRvPhca8TRHgI9U5JKL%2FL%2BpzxZBOd9h60s%2FlJop2ApvzsPGpSU%2Fh0lXxqElnj2Zc2kCYiX95%2BSG%2F5ZMtb%2FDCKViAehlo%2Bk8CdwXyJdHpVjf9DB3BL%2B64pywzO6drhhTv7t2PS09tH9aC66Y7H762p3ClIEu6dxmIG9duhmWPkU0debnU%2FxjV76fQaErulXnehalIfRFVX%2FEMArHKvlDkyIJFozgogY8k9w2l6x95xN4D09cl20NMgmjarCmEVx%2B4Rfs84yKXYk5uOJxStTHkQ9t2LYhA4FthKFHceUW5XGMprHbS09c0TqK7Q1xyof97m4HcqHujtmT6Ug0AxfqTgFn5Zuf%2BrUzB6TDioUEo5INObuYjp0aRNgyyvRTYIKa14oUYeZAnXlRvMhyLrs4emCd4jGrKyKLz9OwuMXy9EjvaZjSB%2FfA2MrPDs9OD42I7I%2BUhfijv0SQeapoaTuLHbH1VWQV9MCN%2Fe3%2Bd3LUsHTYX7l85vnBJM9RGTwer0nzMqFMYJroCYYkwafEkjkMfi5W3vHfo0yvrH0cz7cRRqNclA5r9JhlEBXorhi1QdpHFDPC2IL0MKrUw8kGOqUBznNBBmUUSC7WJjU9xImpA%2BOq%2BNilbEapXOjGLNVkc%2FqjobvoZBojbU3SwA3ZDv%2FD9Z7gdTOo3cHh3SpKDB4%2BLyaOkpqtZWIzhLj6LBR5u2VG9vZOYwML2g%2B3RkEMSZl%2B5l63kP1Ydpn2xYI%2FD%2FP11JvPZCN4%2FWWYao%2ByDpI20GI38DtaksfRYucjd8YbjQaRocDLkuUsRrgMlumeYBvh4WhoonNg&X-Amz-Signature=d659fe9242280bb3734a3485252e5aa69dd5ef70815d877ad1100ce97849df0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNY3GZMN%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T024939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJHMEUCIQCMyHmjgzv0cKTI6Mf3u4OH5vHFGA8GFpnbJLxM%2B167eAIgEfoYTdDfII8et%2FbSnHEdJRBOWHNUGnaeOBXXy42G74Yq%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDHPvVpapQCoTVbt18SrcAw9yUO2QLYzTTmTS%2Bv953OzVDm31L%2FqaZEpjxm1t1HyK%2FsOzkVrtwTRvPhca8TRHgI9U5JKL%2FL%2BpzxZBOd9h60s%2FlJop2ApvzsPGpSU%2Fh0lXxqElnj2Zc2kCYiX95%2BSG%2F5ZMtb%2FDCKViAehlo%2Bk8CdwXyJdHpVjf9DB3BL%2B64pywzO6drhhTv7t2PS09tH9aC66Y7H762p3ClIEu6dxmIG9duhmWPkU0debnU%2FxjV76fQaErulXnehalIfRFVX%2FEMArHKvlDkyIJFozgogY8k9w2l6x95xN4D09cl20NMgmjarCmEVx%2B4Rfs84yKXYk5uOJxStTHkQ9t2LYhA4FthKFHceUW5XGMprHbS09c0TqK7Q1xyof97m4HcqHujtmT6Ug0AxfqTgFn5Zuf%2BrUzB6TDioUEo5INObuYjp0aRNgyyvRTYIKa14oUYeZAnXlRvMhyLrs4emCd4jGrKyKLz9OwuMXy9EjvaZjSB%2FfA2MrPDs9OD42I7I%2BUhfijv0SQeapoaTuLHbH1VWQV9MCN%2Fe3%2Bd3LUsHTYX7l85vnBJM9RGTwer0nzMqFMYJroCYYkwafEkjkMfi5W3vHfo0yvrH0cz7cRRqNclA5r9JhlEBXorhi1QdpHFDPC2IL0MKrUw8kGOqUBznNBBmUUSC7WJjU9xImpA%2BOq%2BNilbEapXOjGLNVkc%2FqjobvoZBojbU3SwA3ZDv%2FD9Z7gdTOo3cHh3SpKDB4%2BLyaOkpqtZWIzhLj6LBR5u2VG9vZOYwML2g%2B3RkEMSZl%2B5l63kP1Ydpn2xYI%2FD%2FP11JvPZCN4%2FWWYao%2ByDpI20GI38DtaksfRYucjd8YbjQaRocDLkuUsRrgMlumeYBvh4WhoonNg&X-Amz-Signature=077dce4c378044dcba6c1f6427e2f3dfc48ec74dad1b16a7be44a68bee01436d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

