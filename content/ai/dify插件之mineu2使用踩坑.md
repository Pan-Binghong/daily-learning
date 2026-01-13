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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSXLYEN4%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQC9OlaMX25baLOgXqh7sjXsP2zGyALABObCFq9whDuFzgIgaR8cpqlfvwPB1MqSDlvadoeZpQlYZQAbN9bXQ%2Fb4dPkqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGLTRR3zj8HixhxDCrcA8in%2BLKxDpZTefrQFlyr3YQ0iuoZfR72mT%2BiEKmCrB07ctwz1WVlfg3LMFQl2qX9hY%2BX53V%2BieN8fPP%2Fkh70%2Byz%2BJcwJ5iJ%2BHFTHSM7SRm3XufMkgECvqMJxJBaQUTf9yxRcQfW%2Fbl96ytFAcnNB9BC2sVEje65Bk9e%2F64L8CKSfPcYs8XglsLgKp8MAxlYo4fU%2B7V2XUVaHEpgFP8f3uOkClYhG7vernHG4BIDhzjfoN45kHF5JLtd7cOC0X3Rk6sPuQ0j3ynnU5EAdHyB06XCWOkvIvdssfJpv2Eh%2BHarhB3D4u9yw6%2FKhZVdTIyPkK4TAQZkY65VR346PxBM4dJGhElE8ldWkqOJB44rEEVpLAbWSSF9ybdtCpBIBvlnG0wjUzQXXVOVB8v44DZwM4zaViOnLQIlpyOyJ2%2F6WkFWeWWxmrY5Cf0zpHEgk7YOviBlO2KSyhmDjbyb1ptqWAuGcGrNUVRxyE%2BO1GdLMhDXBokdoOJeeMSWKfN2xGnJwp%2FXO9Em2%2FXV58qWLJvemMeBjZu%2Bgfzl45gGN9UY7kxP1tEr%2FCOcPrmyTHXPyZWzN2d2s7hjpqJ6%2FEkbQ9X09VVE5Xp5DSbff5IHtp6CeJbtwToJtcAMiYKYQy%2FHkMMTllssGOqUBd3FY8bD66%2F3Nee15N6l4MAVgFLvnEOMfmgLUkv%2FyAAwml3b5DMmM%2F0%2BzjPB6ZTGIFsUXUHzNQhFTkmkXVptfDuqu6wPFuL3tZ2cpZqxSwkiu9JNPeTjvMw7Z8uXuVApJtCema8bikhdlQQIW6tjMqDkonR2USwcXTXpS31okxIj6b8z%2BtRdY64zhM4vfrUkxFVsmm%2BLZtH6suZH8JY%2F%2BA6HqCRJe&X-Amz-Signature=3f69354e4ec86743d695f6492e2e405ead5b7d755351c3509e890f17d42d481b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSXLYEN4%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQC9OlaMX25baLOgXqh7sjXsP2zGyALABObCFq9whDuFzgIgaR8cpqlfvwPB1MqSDlvadoeZpQlYZQAbN9bXQ%2Fb4dPkqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGLTRR3zj8HixhxDCrcA8in%2BLKxDpZTefrQFlyr3YQ0iuoZfR72mT%2BiEKmCrB07ctwz1WVlfg3LMFQl2qX9hY%2BX53V%2BieN8fPP%2Fkh70%2Byz%2BJcwJ5iJ%2BHFTHSM7SRm3XufMkgECvqMJxJBaQUTf9yxRcQfW%2Fbl96ytFAcnNB9BC2sVEje65Bk9e%2F64L8CKSfPcYs8XglsLgKp8MAxlYo4fU%2B7V2XUVaHEpgFP8f3uOkClYhG7vernHG4BIDhzjfoN45kHF5JLtd7cOC0X3Rk6sPuQ0j3ynnU5EAdHyB06XCWOkvIvdssfJpv2Eh%2BHarhB3D4u9yw6%2FKhZVdTIyPkK4TAQZkY65VR346PxBM4dJGhElE8ldWkqOJB44rEEVpLAbWSSF9ybdtCpBIBvlnG0wjUzQXXVOVB8v44DZwM4zaViOnLQIlpyOyJ2%2F6WkFWeWWxmrY5Cf0zpHEgk7YOviBlO2KSyhmDjbyb1ptqWAuGcGrNUVRxyE%2BO1GdLMhDXBokdoOJeeMSWKfN2xGnJwp%2FXO9Em2%2FXV58qWLJvemMeBjZu%2Bgfzl45gGN9UY7kxP1tEr%2FCOcPrmyTHXPyZWzN2d2s7hjpqJ6%2FEkbQ9X09VVE5Xp5DSbff5IHtp6CeJbtwToJtcAMiYKYQy%2FHkMMTllssGOqUBd3FY8bD66%2F3Nee15N6l4MAVgFLvnEOMfmgLUkv%2FyAAwml3b5DMmM%2F0%2BzjPB6ZTGIFsUXUHzNQhFTkmkXVptfDuqu6wPFuL3tZ2cpZqxSwkiu9JNPeTjvMw7Z8uXuVApJtCema8bikhdlQQIW6tjMqDkonR2USwcXTXpS31okxIj6b8z%2BtRdY64zhM4vfrUkxFVsmm%2BLZtH6suZH8JY%2F%2BA6HqCRJe&X-Amz-Signature=df86943dbe8d382f4d70d7fdf5f71a39f84422e2ae3de5d9673b522713f3c501&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



