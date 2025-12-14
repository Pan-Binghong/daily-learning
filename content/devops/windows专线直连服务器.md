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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FKGNHG2%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T030054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIB2DPjTtHETYPpne%2Fq95hgYLcAcY9MLoBAxcpMBfJh7vAiEAqatUbqpK8tANzlApIPk1WBTXtVKdTu%2F4wD84uZCD5dUq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDN6GSF8jX8PYmV1P%2FyrcA%2FQmjePTcSuVoNU8yx9s%2FjgnFLYpzbl0KsXAmJEcXQ8E9d3%2B44%2BKDUa2owBrwvjPAvDhk7AtrtpmUSfU1OHWKol%2FSRfCorgxrWWol6BYxJwVszpD2EwbnGTmKHJGpbC6%2BxWCJe%2BWvYdvslN7DcoLqF77uMWxzkVuMO%2FigFTUBW%2FmlxZRGCqb5DQmJwzioSka65BceBlNCqHHfpFWWybfPe56OP6n8A6N23m%2F7TKxFJAxXVJdfgB1%2FPB0ObwCwolx%2BKezNhpF7H7vURKnra208hGDP7mk4oXmww9wyQX3R29Hn8nVeYb3GXc0WSf3Mz8WgijXGfSvcGKlIsRptrLbMrL4HqMrns%2FbS%2FnqIymJabIVZyJQaAteEnTCIWgnL4m6JoPw4tStfJdv6Kxreth3hYYBKuT1W9JqY15rPkGiKmMi9BnGkGp6cjnw%2F%2FQy3ww0kWghheEmYdGGOiKL37AcaGrDGRLNX3YJSLBelpb305xrKY43e1ipVash0zb1eI1svstTHCUDdW4RV6UMsmEXOBzCS86tlQuvRgnkW2JFt5ezTZR%2F%2BhpSuf9DDCVMgPSMdCMWNRI4F%2B290aCczHPzx5PmOvUYL6Vf0N2%2FKNgeEvUqW32tnYdLlr5%2FuC9ZMLiw%2BMkGOqUBLu2TB6IRZY3ZqWhOHcuCRJ2BsDDF3djUx%2B%2B7Tz0akVFP5j1jgBgeY1GdcPqsYN1ibIQF4gsd%2FZHZFQH4H5O49lEH3xUedNJ8mmHlwIdRfsrzhbQetHXknDN7z4dwzOVcQzUXwfd037GQTT7rp3LYSiDOBNjmJ1ra76vjMlscyhQ%2FzlF3xDVG66wU05wfjPOFjO8u5%2FvZU9dtfbQD9mhZNFndLW1E&X-Amz-Signature=100667564688bc0bf9321df11b283a92e6054d0cb13de4c3ab4490cca14144a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

