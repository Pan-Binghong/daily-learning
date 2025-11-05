---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
标签:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFW72LLM%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbH3a0APJksCFJAVJZWpfeTu15DeQnFu%2FEIiDHj8tbQgIhAPpPt4PIZxcwS9qr%2BA1GpyrWxakRqBQ53i%2FtlZ8IMn%2B0KogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVw1PUJH8mbycHpsIq3AMLsdYqoWXApTdpJduVPNi8QAmzVcooZKCKzqIDM6ME5rN1nNiOs19yzRKZbErZhgKIyKHMCb2rO0OXwc3h1YdpdRFBpi9fSp4eASqkekUR5%2Fuo%2BeqiVU5ylWRDH8OhTMYkhUYggSND2UIW50jFljxwJM9tbcvDtOjeK9MTcS4WG7b9SsgBkA7TFcHSScdWMskgi1MGgZsl3vdGdhmYqSZG%2FLrJvEpRlTkvboKewo%2B1M3ZS5PZbfzSZQJuHJA11kydIlU94qgPl1EDDoe1XbMw4qqB6vSGV%2Bd1iB%2FsTcX0nOYpl5iTBXR2uoRR6wqKaHEhIh0lEU15J5bo69cn8i1Xmi%2BjeNzthl9C6JE3VkUId%2FZ%2BoyI3b87wOLT%2B1XroGqj3q4Wum4NyYZKlLS3r8EYGhS4JBe4bU1R56jSrSg7nmmZwXirETtXWmQuUqNnyBpwMvEikY6JIj5jcFXlJCBSpqRGYU3BGvaeLKYY3mUC0%2FCcf6A6KguhUjsT1Wsw7p2w69YJHPndWYZ7cBdxU%2FuF9bSRKmnSElhmJXEmUzhaMaPQJWNOBTDtkvwV7LEZltpwG2vYfsW%2FiZdwzfEBEX952vMn%2FYG4DDI17l8znlBWlu6Fl2kyGIWXf%2FZPa5UTCwoqzIBjqkAcMmJh3Qn8ZRiwL1Cwhb2BK179NNeE4MosZQlaZqWTAi%2Bfn%2ByXN%2BFhhCMDrKNLh6FNbwSbVQvYG5%2FFLHHagGTPbB0QjiRGEmRnbP2RxKfdFFiBJWxmV2wkPq%2FGhoCWUwaNJ0REPC4hMQmgSdMOtICSmrUCBV2B84%2BgQuAKcnCR%2BQ56YDRYG1CUxQ05tDqVhEm%2FTPykLK5bH%2B61XA2gSmhT6r65%2Fm&X-Amz-Signature=7a20edc5b67b673dfa70a1c0f227422d3bb5f72a5dfcc5fb440237e28003873f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFW72LLM%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbH3a0APJksCFJAVJZWpfeTu15DeQnFu%2FEIiDHj8tbQgIhAPpPt4PIZxcwS9qr%2BA1GpyrWxakRqBQ53i%2FtlZ8IMn%2B0KogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVw1PUJH8mbycHpsIq3AMLsdYqoWXApTdpJduVPNi8QAmzVcooZKCKzqIDM6ME5rN1nNiOs19yzRKZbErZhgKIyKHMCb2rO0OXwc3h1YdpdRFBpi9fSp4eASqkekUR5%2Fuo%2BeqiVU5ylWRDH8OhTMYkhUYggSND2UIW50jFljxwJM9tbcvDtOjeK9MTcS4WG7b9SsgBkA7TFcHSScdWMskgi1MGgZsl3vdGdhmYqSZG%2FLrJvEpRlTkvboKewo%2B1M3ZS5PZbfzSZQJuHJA11kydIlU94qgPl1EDDoe1XbMw4qqB6vSGV%2Bd1iB%2FsTcX0nOYpl5iTBXR2uoRR6wqKaHEhIh0lEU15J5bo69cn8i1Xmi%2BjeNzthl9C6JE3VkUId%2FZ%2BoyI3b87wOLT%2B1XroGqj3q4Wum4NyYZKlLS3r8EYGhS4JBe4bU1R56jSrSg7nmmZwXirETtXWmQuUqNnyBpwMvEikY6JIj5jcFXlJCBSpqRGYU3BGvaeLKYY3mUC0%2FCcf6A6KguhUjsT1Wsw7p2w69YJHPndWYZ7cBdxU%2FuF9bSRKmnSElhmJXEmUzhaMaPQJWNOBTDtkvwV7LEZltpwG2vYfsW%2FiZdwzfEBEX952vMn%2FYG4DDI17l8znlBWlu6Fl2kyGIWXf%2FZPa5UTCwoqzIBjqkAcMmJh3Qn8ZRiwL1Cwhb2BK179NNeE4MosZQlaZqWTAi%2Bfn%2ByXN%2BFhhCMDrKNLh6FNbwSbVQvYG5%2FFLHHagGTPbB0QjiRGEmRnbP2RxKfdFFiBJWxmV2wkPq%2FGhoCWUwaNJ0REPC4hMQmgSdMOtICSmrUCBV2B84%2BgQuAKcnCR%2BQ56YDRYG1CUxQ05tDqVhEm%2FTPykLK5bH%2B61XA2gSmhT6r65%2Fm&X-Amz-Signature=7dbd795ed28aa3e4d85c9a542c0a9eb1675a649a7e5c15fe1d2f4c39a80d9a1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

