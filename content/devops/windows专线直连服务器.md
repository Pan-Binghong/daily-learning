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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HZZFVBZ%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkLM7y%2FXmRn2wM6Pvs26q9pbWsR2JVpwESt9Fx1IeaxAiBIOEeAU2kwa0VkYXZsA0EibsdLlvaoSc7rYWkpWKhCCCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpz9JLcEzP%2BbXYGpvKtwDMHmJcRtjSC3WeQCZHVvkrfMjbJhNmc%2Fpi9LhLrlk0urr2zIv3mhJ2njDhGGmXxWCNyYsjq2KP0bK9hhupScx5OZ8my4HfYxsj7hkikF6CaLI6sPJNlc%2BxaQtyv7Ewa2rPxA3Tswgu4Flw9sU6NmV37QWByBObf1v1u9wq6Tkm4Yp4oR0jkIwPWfjyEG%2FJIxnpGQyz9lge4mpVEeE3fgbuPj%2B6qqSJ5wr7VEUY6knVIoFnN%2BXv3NxVGbq4jtSpDcyJeBJDUtaZS1pw1joOIHq%2BQ2dLWJKO3sfYoFshaYgLB9pCGyw9fxlTZGiJLMxa8tIt6JYFNTBTSSpmeg6of6FqHGkmofw2BdyOyUn%2BbAWWDGy3ZfY6DsauNIPLqFyc122eG39%2FUso5CjjI3nY%2Ftd5B4wKb8PeErhTpmB65n1YKx3k%2B3JZjFpyBHqytrlfPssvyChuwxdopqO876sRXPq%2BP0YxGwYjzdeTFO8bsyKmrZoY7mEAmYjegDPhVRaa0ndaWtbp2A4eL1n%2BWP8FiwTYHyGdMWtpVjA3JqRJ%2BSBv0jNsTgsE03DMLU3Lmf0QiTOWTixS%2FEMFzwl4mb67tW2cWsOWXQRXo2Pa6pCVrY%2Fq07eEe52bRG3S6h%2F339Qw4cSBywY6pgGteYF4FTqwUM14mkKuO6P6pWTH1EEd1mNGEqnu%2Bn1SVC19txp0geCPIcEZhNfyG5c6qafOoW%2BwurrOF8M54X8GgpCMEE8uwlmaHeW%2BfZQ%2BciZD5QMwvQ8vM00eZuvesgBhJdDMKgrN24Zf5U2cK2HYSyw%2FOVOWuj16ZRw0GGXu1u9ioN31nN4cnoYaGLK4w3%2BEEYAIlWaqeoudN5PQ7PSxrmdyud0w&X-Amz-Signature=9bab38ef930bc28f4e95900d73aa66d44dd05525fba3c8e30b7cb5e57e12688c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

