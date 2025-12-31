---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZIXBDZR%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGopIWRn5hEBEw3bZwCZd9zmnPUj0axNagxB9nS44S%2BwIhAI5pay5XbYcyY4cPwy08aAHTLKfKuEk3Zi7ZjwlMEbH0KogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBBIJkDGaw4lVc9U4q3AMnqg0wnhhnl4Z665IkihmQli%2BTNWy5RgB1FSwIpb7eNZDARGe6LbYDOwPDZkiGVO6cpHfEKoH4DG6k3SQc8pkSmSM25rODl9Zh7QthEGaayjiOIFjrc8vzNNkDIkP2rZpVM2wUDjY7xu0ldn0hbdBdC1b9W%2FAPHFjyZBVStYkfVVY3bH35TFU9F9COYOZJLyQAVA2Kq7kp6FapZ8wiehAInc5ZKhyud9%2BkviVSFu%2FYIEb19AD7duALrO4%2F81lUoRg1vEmBaZW5Oaljm1XvhRtRql%2BOfp5ob%2FHyDLH1ZqOiHDHo8RFB%2BDiDjGpzv5KGj6mOA3ee1mGGXyMDeWxA4sfl%2FvC9c8uBZ9FlzzVkVfyUv7XQyejS6DjNJIKLhacBOTBhufe8jtAHQVC8cw7gflKDPUfNkf2ilgB1TchMraAe26CR9%2BIya%2FXwEY1gob14Sc5oFKoEwer1hB87mdW1Am7HwOTQdfccmwQnWYW8L%2F5wgR1Pg1gbGNRoBwE%2BHKygGIqjxgVk53ChVv8romNZkf2b5WrKbSNEpM284CRyiQqJFs4rkWD4SN08rqppiNKYxS%2F16IM8UXg0ukRrr8AQX8YTX9nvdXNfo800DJcfx9EPftbh8EjgW2A8Wz2%2FJjCp9dHKBjqkARUySZ5Zg%2FkSzbDETw8V245Ai2WZowEva2l%2BdAGxZySM0Abz3F%2Bve1omkpwhc%2Fm6bUeEm2jsCKV2LTNRC%2BtKBwvgyy7mXOVph4sRqtGypmX1umAVWrhuodPYVoOcgl%2F2baLR1PhUf1vzZtv5P7o%2BCqf9QVA2L8U2La4NuxXid8k4fVPdYpoqiCedzq2M4zjJ%2Fw9Mvya8nNzEja%2Fdz5dXVDbk1%2F3D&X-Amz-Signature=1e54ad739c77eb64fe74f2e225caca2b395047594c2522cb8f4102f81d86d5d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

