---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OILG67U%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID%2B8UwYt567OpdPJ5AEjqFkZBA4t%2FftGnTLJa29bbqgvAiAD385WQDeqSg6UWYS5dXMKcHMSJLK4dxVCsaG9M2RHZSr%2FAwhTEAAaDDYzNzQyMzE4MzgwNSIMIbm7%2FEJRvLgfECy5KtwD0%2BcYPq2excYGPrYT4w94LbGRGY33j3eVpdwS8S98Ilui7oa6cq9hZKfEB1AV2N2kebIHRgohZQTjkKrZT8r%2Be7NY%2BqDc%2FCSkXT42USVXmg2wOHkDKIMmxq7Jz4a%2F%2B0MsReAuExdNT0jYDxq6%2FQvOWYmdFV6IGZ8dlDAFk9YYlvALen%2BZcpBzGWhgb8QW99n52wS15cZHI4UYx0kC2f7B%2FrvSy9cheL%2BQ0hY87qJfjEuklHJxdWDUDzxzwVgnyXagFKiOrV%2FFRjj%2FiTFN23cxcymJ0sh5ACQUqKGw2qFSZf%2FbDXhZqmDzFvn1%2F3DEfIgd%2B1WHfNbr3SZUlMMd1yYZlsf9p8%2BPF%2F7tz1KeAGnEKG4OLdeGnfNiBUFk4kATyt%2FOaTt2akp5isM7Fx4tb9ynNOweCbcrI18WbdCiGKdBP0rCj86x54UE2DSTGpf3HKB%2BDZaspxmAc%2BQvt0uWGI%2F6c8ZoOngU5bnTZd%2BjpI7ce82irnP2gZjs4RU%2F3S1B7%2BtE1TtPBcQdyWwTkFnmdBkrMXGRuGLwmp03cFs3kKnoxaGGTgdxtuS673LOx3IKbS7kE0Ii6DUCmhLPi36qdSAm3tOgetgJC%2Ff%2B3ir9oDUQ0PhP4kzjEFx5%2Bc5YgVswocSazAY6pgF1BL%2BDiPQ0gVDgHh8maLWnk9mg%2BUzYX3WryvS8%2FiK1iu%2BMrsmVLCIxVQ4fHmF5w5x%2BdimpjNPl8GSdlS%2Fhqrh56HcmmXupxA3sN2vnpKbaLOTlPFU0bJG%2BNCREOLvONPRBO8LfM5qcAOSJoky5LvM6cL7I6Ym2YcgAA%2FSgz%2FQk5ZjBM6k46qL8XUD0hkUd2o32IzdTeLcTtayPbd5FlhbISFeucEW1&X-Amz-Signature=d8f792f5f8ca49d2bdb5f01a7da0214ee31e54a31e8640d1085da2aa8251e0a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OILG67U%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID%2B8UwYt567OpdPJ5AEjqFkZBA4t%2FftGnTLJa29bbqgvAiAD385WQDeqSg6UWYS5dXMKcHMSJLK4dxVCsaG9M2RHZSr%2FAwhTEAAaDDYzNzQyMzE4MzgwNSIMIbm7%2FEJRvLgfECy5KtwD0%2BcYPq2excYGPrYT4w94LbGRGY33j3eVpdwS8S98Ilui7oa6cq9hZKfEB1AV2N2kebIHRgohZQTjkKrZT8r%2Be7NY%2BqDc%2FCSkXT42USVXmg2wOHkDKIMmxq7Jz4a%2F%2B0MsReAuExdNT0jYDxq6%2FQvOWYmdFV6IGZ8dlDAFk9YYlvALen%2BZcpBzGWhgb8QW99n52wS15cZHI4UYx0kC2f7B%2FrvSy9cheL%2BQ0hY87qJfjEuklHJxdWDUDzxzwVgnyXagFKiOrV%2FFRjj%2FiTFN23cxcymJ0sh5ACQUqKGw2qFSZf%2FbDXhZqmDzFvn1%2F3DEfIgd%2B1WHfNbr3SZUlMMd1yYZlsf9p8%2BPF%2F7tz1KeAGnEKG4OLdeGnfNiBUFk4kATyt%2FOaTt2akp5isM7Fx4tb9ynNOweCbcrI18WbdCiGKdBP0rCj86x54UE2DSTGpf3HKB%2BDZaspxmAc%2BQvt0uWGI%2F6c8ZoOngU5bnTZd%2BjpI7ce82irnP2gZjs4RU%2F3S1B7%2BtE1TtPBcQdyWwTkFnmdBkrMXGRuGLwmp03cFs3kKnoxaGGTgdxtuS673LOx3IKbS7kE0Ii6DUCmhLPi36qdSAm3tOgetgJC%2Ff%2B3ir9oDUQ0PhP4kzjEFx5%2Bc5YgVswocSazAY6pgF1BL%2BDiPQ0gVDgHh8maLWnk9mg%2BUzYX3WryvS8%2FiK1iu%2BMrsmVLCIxVQ4fHmF5w5x%2BdimpjNPl8GSdlS%2Fhqrh56HcmmXupxA3sN2vnpKbaLOTlPFU0bJG%2BNCREOLvONPRBO8LfM5qcAOSJoky5LvM6cL7I6Ym2YcgAA%2FSgz%2FQk5ZjBM6k46qL8XUD0hkUd2o32IzdTeLcTtayPbd5FlhbISFeucEW1&X-Amz-Signature=f4942737aa308b329005f9b7fc4cd99b0fad5ef944dc9400b80d5baa50f046dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OILG67U%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID%2B8UwYt567OpdPJ5AEjqFkZBA4t%2FftGnTLJa29bbqgvAiAD385WQDeqSg6UWYS5dXMKcHMSJLK4dxVCsaG9M2RHZSr%2FAwhTEAAaDDYzNzQyMzE4MzgwNSIMIbm7%2FEJRvLgfECy5KtwD0%2BcYPq2excYGPrYT4w94LbGRGY33j3eVpdwS8S98Ilui7oa6cq9hZKfEB1AV2N2kebIHRgohZQTjkKrZT8r%2Be7NY%2BqDc%2FCSkXT42USVXmg2wOHkDKIMmxq7Jz4a%2F%2B0MsReAuExdNT0jYDxq6%2FQvOWYmdFV6IGZ8dlDAFk9YYlvALen%2BZcpBzGWhgb8QW99n52wS15cZHI4UYx0kC2f7B%2FrvSy9cheL%2BQ0hY87qJfjEuklHJxdWDUDzxzwVgnyXagFKiOrV%2FFRjj%2FiTFN23cxcymJ0sh5ACQUqKGw2qFSZf%2FbDXhZqmDzFvn1%2F3DEfIgd%2B1WHfNbr3SZUlMMd1yYZlsf9p8%2BPF%2F7tz1KeAGnEKG4OLdeGnfNiBUFk4kATyt%2FOaTt2akp5isM7Fx4tb9ynNOweCbcrI18WbdCiGKdBP0rCj86x54UE2DSTGpf3HKB%2BDZaspxmAc%2BQvt0uWGI%2F6c8ZoOngU5bnTZd%2BjpI7ce82irnP2gZjs4RU%2F3S1B7%2BtE1TtPBcQdyWwTkFnmdBkrMXGRuGLwmp03cFs3kKnoxaGGTgdxtuS673LOx3IKbS7kE0Ii6DUCmhLPi36qdSAm3tOgetgJC%2Ff%2B3ir9oDUQ0PhP4kzjEFx5%2Bc5YgVswocSazAY6pgF1BL%2BDiPQ0gVDgHh8maLWnk9mg%2BUzYX3WryvS8%2FiK1iu%2BMrsmVLCIxVQ4fHmF5w5x%2BdimpjNPl8GSdlS%2Fhqrh56HcmmXupxA3sN2vnpKbaLOTlPFU0bJG%2BNCREOLvONPRBO8LfM5qcAOSJoky5LvM6cL7I6Ym2YcgAA%2FSgz%2FQk5ZjBM6k46qL8XUD0hkUd2o32IzdTeLcTtayPbd5FlhbISFeucEW1&X-Amz-Signature=2eed4daae48efd3586391bb4e58de9a51df1f0e32f6780510e66172391fc973c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

