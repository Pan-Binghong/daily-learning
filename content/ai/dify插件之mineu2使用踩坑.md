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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRZAJKUX%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlcAxaKDdeAzpAVZmehNNmN2HhG9Um5qvKV7EtaOHVwgIgdyNkz%2B8tyHSP3nPLfRlsX8CJIggnh6tq5xrYCy4StjsqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPgLE7PaVebGI5j0USrcA3TrswjQMwguKRLlvxKBscyRDc48deYqWKI5XdmTtyeZpgO98o%2BIKgV4Lyk969fDN20E7UVrbbG8AT4pu%2FuWWopZzevXLzEtRnolFSCTDoFsckIgTSFUN9PdAhM1ZMLzYLPAi4gvZoo4c8SpwhBLKAZ6I6SIMSIFm5gKx3zPSZYINUl7zFNNnTk2huWsmxnCvUNllhLtg2jv150q9jEWwCVLrb5KmsNfx%2BUr%2FJYyeIrAKaZS7NYSIQOvFilUzY44pf4RxsZAxEWRD039xaTDXSHMLWzlx8RNEKhx0erUTbXl23AJdwePrDijyQfTpSC3deUVbLyXpt4L9Ai%2FycsLf1VBkDFsBfwLCkC7KSKHIppHesnCBxr2omA6U2HMi7C6KZk5sT70peyKx2VqbI9ewJ9SPT3%2FzqTuOL3AJn011ySIg6Sg0H6CgA7s46NtsYdoo2egA94VwYzAOVl127jpVfuh9UgG13vAJihxzjawc135DFnigzBlD0s06RdW8O%2FVCv8RknL2K0MeXhyy05L3HdI0u2ilYLXQjOfOQvBb7FOZrDr7FaD%2F5OaVn0T3YrJaUteoXnyfmw1%2BhBTtW4Avw%2FsHWuV5n6Zh8i6Kd2NlNdXEMUvhHqgao6C4ikk2MIHiksoGOqUBWHTador52aGoZe8EgxC0rmVEO7QxXU5keMFFR0EhUzcPEYk3apMd8%2BjYo68l%2FidNW6mjwE9EMHii8Xs9rYdj6ptOFM6iiHPsq5mPmNbhe%2FZc8IFjy7eFhc0Fu1Hamv2HNdtxIg9PeKip0d9QxghTFMQw2dhV9AQ%2FJzBTJFA84Enj51KmkGiqbBD3AW7QVcxFPUCpCi6NL3vddkgahzysUlCUUiVb&X-Amz-Signature=8faec3bc24b611813074fa7dd45d2fd0bc0e3295c51268fa6b4c77243d4e17e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRZAJKUX%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlcAxaKDdeAzpAVZmehNNmN2HhG9Um5qvKV7EtaOHVwgIgdyNkz%2B8tyHSP3nPLfRlsX8CJIggnh6tq5xrYCy4StjsqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPgLE7PaVebGI5j0USrcA3TrswjQMwguKRLlvxKBscyRDc48deYqWKI5XdmTtyeZpgO98o%2BIKgV4Lyk969fDN20E7UVrbbG8AT4pu%2FuWWopZzevXLzEtRnolFSCTDoFsckIgTSFUN9PdAhM1ZMLzYLPAi4gvZoo4c8SpwhBLKAZ6I6SIMSIFm5gKx3zPSZYINUl7zFNNnTk2huWsmxnCvUNllhLtg2jv150q9jEWwCVLrb5KmsNfx%2BUr%2FJYyeIrAKaZS7NYSIQOvFilUzY44pf4RxsZAxEWRD039xaTDXSHMLWzlx8RNEKhx0erUTbXl23AJdwePrDijyQfTpSC3deUVbLyXpt4L9Ai%2FycsLf1VBkDFsBfwLCkC7KSKHIppHesnCBxr2omA6U2HMi7C6KZk5sT70peyKx2VqbI9ewJ9SPT3%2FzqTuOL3AJn011ySIg6Sg0H6CgA7s46NtsYdoo2egA94VwYzAOVl127jpVfuh9UgG13vAJihxzjawc135DFnigzBlD0s06RdW8O%2FVCv8RknL2K0MeXhyy05L3HdI0u2ilYLXQjOfOQvBb7FOZrDr7FaD%2F5OaVn0T3YrJaUteoXnyfmw1%2BhBTtW4Avw%2FsHWuV5n6Zh8i6Kd2NlNdXEMUvhHqgao6C4ikk2MIHiksoGOqUBWHTador52aGoZe8EgxC0rmVEO7QxXU5keMFFR0EhUzcPEYk3apMd8%2BjYo68l%2FidNW6mjwE9EMHii8Xs9rYdj6ptOFM6iiHPsq5mPmNbhe%2FZc8IFjy7eFhc0Fu1Hamv2HNdtxIg9PeKip0d9QxghTFMQw2dhV9AQ%2FJzBTJFA84Enj51KmkGiqbBD3AW7QVcxFPUCpCi6NL3vddkgahzysUlCUUiVb&X-Amz-Signature=60a2a8663af53fe8dddfac2b5ebdc23f8c849d3ec2b17f0462c2237e419b763a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



