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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYOHYPIR%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T024948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIAML%2F63%2F8TZiNVjq9w3pos%2BD8J9TkINt%2B4rsw52Jez%2BlAiAWeApahxY32%2BMHy0Vfb7sm%2FnSrxQmVthTC0SRbZF4VtiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMx5yvA92Fp%2BVZ%2FXoKtwDpP2Hs9Hr2kGN%2FngCe42dTWErOinesgoCoFIIGr9qJyCA%2BIUN4dsv8YVcH8S0AgqWIIZKe8tjU4UGI%2Fce3wDVz9CrqDN5X6dDMPAsFqQCB3IYOSrdB33pYSvpJb6%2FVUNXvt2iGc6i7d%2Fe5xN9IvRF6N2JTTivz4Ctzlp2TEgWtmeY%2FPX%2FbuZYHCc8cwy%2FnTxKW0ZCZzJN331yJzL2CgU60%2FcoXGZji1UmSHKkvrXSCUmya0kuMvRpE2M0FD%2FzSAjunOvW99lA52WVNzM1HX8%2B7TxybaGuI07naxpWV7Pq2tc2OMhhaOb5YYp7A0U28lOBzRQXGEK4xBjDNcg8gtIOavjGSe9Gc74ysUFRiW%2FUKDJi81wIZqV%2F5X61OQ8Q%2FGxwdyju1UeDXNDnwT%2FHB8BKSJLNyGEbM36e5X7QqASgkpvlZ6gh3nDZA6ePuI0zdrpMd%2BsaWrhBmsXEburgZm2YiynNPOr2s5zpniyILov2zd8rqOpUvxS5wctLAVLvK8wF7jjzOju1UjePupGUSfZe50OhcjBHGfrCRw03b8tr2tvOUHOeQk928kNQ%2F6Lw%2B54EPU7jHLeGgqvdEYUbAtueor49ZzXFugMUSDcwGipwAHpwf0rebDhfy4B4LCIwjLXEyAY6pgEFenfJ1mNIIe6q7KZuK%2BdGs1x%2FvZIWQC5V1xQVnptqtr48HONbZokQTraGoo%2BzIlW9kOlRRtFmwzNF%2FS3N6wxN6ug12IuUjKRbz5W7kcQnaJTltOJY%2F53AFq3%2FtfLh45oJ9Zm0DLDqHdH3%2FmenzS5HhIcZUJDQuMpxH6KU9Z8yYixVAXjyV8uwGncbcadC2d3tPVTSnBSoCbo%2FxrHXKReFZURHCzSK&X-Amz-Signature=0841fe8ca9c21067e0be5934a6c46378d5e413715112e6f9288b0ac04adbdf45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYOHYPIR%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T024948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIAML%2F63%2F8TZiNVjq9w3pos%2BD8J9TkINt%2B4rsw52Jez%2BlAiAWeApahxY32%2BMHy0Vfb7sm%2FnSrxQmVthTC0SRbZF4VtiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMx5yvA92Fp%2BVZ%2FXoKtwDpP2Hs9Hr2kGN%2FngCe42dTWErOinesgoCoFIIGr9qJyCA%2BIUN4dsv8YVcH8S0AgqWIIZKe8tjU4UGI%2Fce3wDVz9CrqDN5X6dDMPAsFqQCB3IYOSrdB33pYSvpJb6%2FVUNXvt2iGc6i7d%2Fe5xN9IvRF6N2JTTivz4Ctzlp2TEgWtmeY%2FPX%2FbuZYHCc8cwy%2FnTxKW0ZCZzJN331yJzL2CgU60%2FcoXGZji1UmSHKkvrXSCUmya0kuMvRpE2M0FD%2FzSAjunOvW99lA52WVNzM1HX8%2B7TxybaGuI07naxpWV7Pq2tc2OMhhaOb5YYp7A0U28lOBzRQXGEK4xBjDNcg8gtIOavjGSe9Gc74ysUFRiW%2FUKDJi81wIZqV%2F5X61OQ8Q%2FGxwdyju1UeDXNDnwT%2FHB8BKSJLNyGEbM36e5X7QqASgkpvlZ6gh3nDZA6ePuI0zdrpMd%2BsaWrhBmsXEburgZm2YiynNPOr2s5zpniyILov2zd8rqOpUvxS5wctLAVLvK8wF7jjzOju1UjePupGUSfZe50OhcjBHGfrCRw03b8tr2tvOUHOeQk928kNQ%2F6Lw%2B54EPU7jHLeGgqvdEYUbAtueor49ZzXFugMUSDcwGipwAHpwf0rebDhfy4B4LCIwjLXEyAY6pgEFenfJ1mNIIe6q7KZuK%2BdGs1x%2FvZIWQC5V1xQVnptqtr48HONbZokQTraGoo%2BzIlW9kOlRRtFmwzNF%2FS3N6wxN6ug12IuUjKRbz5W7kcQnaJTltOJY%2F53AFq3%2FtfLh45oJ9Zm0DLDqHdH3%2FmenzS5HhIcZUJDQuMpxH6KU9Z8yYixVAXjyV8uwGncbcadC2d3tPVTSnBSoCbo%2FxrHXKReFZURHCzSK&X-Amz-Signature=a902cb4363a7aec8072e26060d37ab999cf4454de25b6f732d48a217a2c12be1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

