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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UW6T5PU%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEPuoNsJF%2BXINkzGulDkmXroGjeYOtpgudLAM2GrvbzgIhAOOhSWwXB0%2BeFMBK%2F610B9FkxzPFISrtv1YfBOSkFWulKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxdlsGujmpjUEZKUFMq3ANPaGVFXKAXlLGriJ4WtujBu9P6ScOewABqqbvXpLrFNWAH0ahS3n0EqfzC9JPatbNEBJn1WSoh1q32XIghTSuLtnxGfdVEad7UzPnK2g5ilql2pqfEW6TToF8U%2B5deyKEnZYn8KEdfE2HMYXBou%2F4F7t6ReRTnVdQkP7BMqwjTuuby1aDHVPpWKzF8fXKvfYtBYn7tSgcBickDmj686J7TcqfE4mUDViP042uP8Cx8Wz6QRVIoGgkui5nR39ZDdeudUwvjJeC6U1K%2B7Etw%2Brb5UnsPk8%2B0KbTGjcnwDIj77AQf6kM2TeTBbzMsuY7rXiL4LTd%2Fop8tyZM%2BrzCQ1RQgTKnOgyI3svQD8qk9uyDdHCLzKwghQmdn41K17cFv%2FFiPVLx3%2Ba%2F%2BxKYIXoQP5sqCzUb%2Fi8VQzx3aB7MCNu4oenzQ2j496GvsV12TvtkQxdxE3DFD6xrDemMFpWVxkClt2PV4dyV5GP7pOSJFY5pJRY4XvZ7Gm7ABayQbH6E0ECCkyIUeGbr%2FDzstWrK5tjpNrHmP8e8p5GrM4PtyPwc%2FOvnvcEkDQur4c78m0JYcJ%2FWs3E5ABisoXH2wgHzKmbxnJv%2BVZPFy2ZenCDkxGcbIll9yATgyzlYs9xCCizCA2MDLBjqkAWf1GMH1AhQuQuSfCwh4Pjtc257j8NPfYOSdaMCQEXjnG%2B8sdNOk5ZV18Wlh9l%2BNq0rtNIMAwWCKUNMb2TT%2BxK2jEjGvLi1U24qrNi0ouxzNpNEo6X4oviaPQDUiBNCYgb9MkxD9W0yWpiVRJZ%2FrMHe2qZp0%2FGRyb0xq%2FvDkeKbk3Si9OYC6QBf7%2Bsza7dnMXen8vZxEXSdR5%2BW8k87yCeB6ehVI&X-Amz-Signature=ee9980bb6707d0fa4de6a4691c677efe4ebfd21327a4fc6baa0dbbc0ffdbb471&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UW6T5PU%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEPuoNsJF%2BXINkzGulDkmXroGjeYOtpgudLAM2GrvbzgIhAOOhSWwXB0%2BeFMBK%2F610B9FkxzPFISrtv1YfBOSkFWulKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxdlsGujmpjUEZKUFMq3ANPaGVFXKAXlLGriJ4WtujBu9P6ScOewABqqbvXpLrFNWAH0ahS3n0EqfzC9JPatbNEBJn1WSoh1q32XIghTSuLtnxGfdVEad7UzPnK2g5ilql2pqfEW6TToF8U%2B5deyKEnZYn8KEdfE2HMYXBou%2F4F7t6ReRTnVdQkP7BMqwjTuuby1aDHVPpWKzF8fXKvfYtBYn7tSgcBickDmj686J7TcqfE4mUDViP042uP8Cx8Wz6QRVIoGgkui5nR39ZDdeudUwvjJeC6U1K%2B7Etw%2Brb5UnsPk8%2B0KbTGjcnwDIj77AQf6kM2TeTBbzMsuY7rXiL4LTd%2Fop8tyZM%2BrzCQ1RQgTKnOgyI3svQD8qk9uyDdHCLzKwghQmdn41K17cFv%2FFiPVLx3%2Ba%2F%2BxKYIXoQP5sqCzUb%2Fi8VQzx3aB7MCNu4oenzQ2j496GvsV12TvtkQxdxE3DFD6xrDemMFpWVxkClt2PV4dyV5GP7pOSJFY5pJRY4XvZ7Gm7ABayQbH6E0ECCkyIUeGbr%2FDzstWrK5tjpNrHmP8e8p5GrM4PtyPwc%2FOvnvcEkDQur4c78m0JYcJ%2FWs3E5ABisoXH2wgHzKmbxnJv%2BVZPFy2ZenCDkxGcbIll9yATgyzlYs9xCCizCA2MDLBjqkAWf1GMH1AhQuQuSfCwh4Pjtc257j8NPfYOSdaMCQEXjnG%2B8sdNOk5ZV18Wlh9l%2BNq0rtNIMAwWCKUNMb2TT%2BxK2jEjGvLi1U24qrNi0ouxzNpNEo6X4oviaPQDUiBNCYgb9MkxD9W0yWpiVRJZ%2FrMHe2qZp0%2FGRyb0xq%2FvDkeKbk3Si9OYC6QBf7%2Bsza7dnMXen8vZxEXSdR5%2BW8k87yCeB6ehVI&X-Amz-Signature=3604be072a9d9424e80048eda88abcfb541a7090b0704dec4f83d7e6f2f0d246&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



