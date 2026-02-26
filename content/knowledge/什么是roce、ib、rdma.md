---
title: 什么是RoCE、IB、RDMA
date: '2024-11-16T12:19:00.000Z'
lastmod: '2024-11-20T03:23:00.000Z'
draft: false
tags:
- Knowledge
categories:
- 知识
---

> 💡 在分布式存储网络中，我们使用的协议有RoCE、Infiniband（IB）和TCP/IP。其中RoCE和IB属于RDMA(RemoteDirect Memory Access)技术，他和传统的TCP/IP有什么区别呢，接下来我们将做详细对比。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4c1086e4-df1f-4fa1-b626-cc1719e9c885/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKV4GGO7%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIDnYNZHk2xypN%2BKmaiIg2UMk5SCFS1SKV2371wViHbjyAiEAk8cPu2jKmf5SkbkCLVUuNc%2BEVkWALvk5BQq4I2lBVhQq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDFAExcQ3pUgGu8GrayrcA%2B5t7ywC9IIpkt0N5QbUh%2BLQ5Ek6xj%2FpvaV5qqnM1AQaiYSVQQDdHWf%2F%2B8kw6RDseUS3L4ftz1wOciPikMYhzbnYCp%2F8tRj%2B12%2Br2jFz8gaSwTQ2cSKZ6HsDeJEW3ADNlqL7Ldu45Dfa9K0FHbZ5H2pE3XpyuQtWucoceJCSzXXfTmy2MxJQnQpiQuPF3sARkEPHXY%2BS%2BiFgCHMOWeO5o%2FmHtA2vF8%2B8KsFWnhbExCI8f2vaxvbSiOnd8vxd6BJFUKRJpftzOu0bAyuuOxYeGHwsQs8gBzVH%2FxuUrmPcgtQvYyrBiRO6EAe4mnkU7NSRgkW6pcqghrBXiOo1Q5SA6oWgdy01jfBgmf7JxKfRLiUb5FrZNwMnUrW%2BexyJHKmBSsoPc7F%2FzO94Qf164soXfv55SUA9qGlMSWqo8Zebj%2BtxEQUIQZvxFeowCRwhQmvxocFCI1ayeLNgEqX9nHY1BGdfXlgG%2BK3TfbMD09O3K67ksdGqZAsMdVRWyiAamirG5tab0eHxfXpfhZOefSCZGWBx0kVxGZxlwYZgA5h5dFl%2BDD9Vrc6XDp6DtVdrke20dggqSf%2BCHgv2p%2Bm8rFGL9ELQTusxwD7kCjFPNfdh2V1CTTGGSCR8Yb%2BcIVuOMKz1%2FswGOqUBaYcUrmyAgcwDFKQ1N7nz05FwOhShoVY0Sxeu4S16IE2VVIrBPk3D3l4MR0c5tM1pvRVO1Tym%2BKIqJLqdnaRY%2Fm2hiq%2BIqSITszJcefdjvGE8d9qMX2Atao8yfzbFF60qiuY1ciptj4H7iQf8XMaGuKYN5KIv3uoGfa2sDZMDOnUIjnoQxVl6GzgtRB%2FdTej89fIP431M4dLMV0I%2BJKAMz1eTk22Z&X-Amz-Signature=f8c8316c91a0c50901c9101083f64e7135449abde9843bc0c8ac4bdfd132aba0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## RoCE和IB，RDMA通述

### 什么是RoCE

- RoCE (译为”基于融合以太网的RDMA”, 英文全称: RDMA over Converged Ethernet)是一个网络协议,允许在一个以太网网络上使用远程直接内存访问（RDMA）。RoCE有RoCE v1和RoCE v2两个版本。RoCE v1是一个以太网链路层协议，因此允许同一个以太网广播域中的任意两台主机间进行通信。RoCE v2是一个网络层协议，因而RoCE v2数据包可以被路由。虽然RoCE协议受益于融合以太网网络的特征，但该协议也可用于传统或非融合的以太网网络。
### 什么是IB

- InfiniBand (直译为“无限带宽”技术，缩写为IB) 是一个用于高性能计算的计算机网络通信标准，它具有极高的吞吐量和极低的延迟，用于计算机与计算机之间的数据互连。InfiniBand也用作服务器与存储系统之间的直接或交换互连，以及存储系统之间的互连。
### 什么是RDMA

- RDMA (译为”远程直接内存访问”, 英文全称：remote direct memory access)是一种绕过远程主机操作系统内核访问其内存中数据的技术。由于不经过操作系统，不仅节省了大量CPU资源，同样也提高了系统吞吐量、降低了系统的网络通信延迟，尤其适合在大规模并行计算机集群中有广泛应用。
> 拓展

---

## RoCE优缺点及关键技术

### 使用RoCE的优势

- 成本效益：
- 兼容性和灵活性：
- 易于管理：
### RoCE的缺点

- 性能：
- 可靠性：
### RoCE对比IB总结

- IB和RoCE的区别为链路层一个为IB协议，一个为Ethernet协议，其中Ethernet协议更具有普适性，且大部分场景RoCE时延更低、带宽更高。
### RoCE的关键技术

- 由于RDMA要求承载网络无丢包，否则效率就会急剧下降，所以RoCE技术如果选用以太网进行承载，就需要通过PFC，ECN以及DCQCN等技术对传统以太网络改造，打造无损以太网络，以确保零丢包。
- PFC:
- ECN：
---

## RoCE应用趋势

- 当比较RoCE与其他类似的策略时，例如iWARP（Internet Wide Area RDMA Protocol）和传统的InfiniBand网络，我们可以看到一些显著的区别。
- iWARP是一种通过TCP/IP协议栈实现RDMA的技术。虽然它可以在标准的三层网络中运行，但它的实现通常比RoCE复杂，并且可能需要更多的CPU资源来处理额外的软件堆栈。此外，iWARP在网络性能方面可能不如RoCE，尤其是在低延迟和高带宽的应用场景中。
- InfiniBand是一种专为高性能计算设计的网络技术，它提供了极低的延迟和非常高的带宽。尽管InfiniBand在性能上优于RoCE，但它通常也更昂贵，并且需要专用的硬件。相比之下，RoCE可以在现有的以太网基础设施上运行，降低了部署成本。
- 随着RoCEv2的成熟和普及，它已成为数据中心网络中的一个主要趋势。越来越多的企业开始采用RoCEv2来支持高性能计算、机器学习和大规模存储集群等应用。RoCEv2的优势在于它能够在标准以太网上实现低延迟和高带宽的RDMA通信，同时保持较低的成本。
- 未来，随着对数据密集型应用需求的增长，RoCEv2将继续在其核心市场中发挥重要作用。随着技术的进步和新的应用场景的出现，RoCEv2可能会进一步优化以支持更广泛的用例，包括边缘计算和物联网（IoT）领域中的实时数据处理。
- RoCEv2凭借其在性能和成本之间的平衡，正在成为数据中心网络架构中的关键技术之一，而RoCEv1则由于其局限性而在实际应用中逐渐被淘汰。随着网络技术和市场需求的不断发展，RoCEv2有望在未来的数据中心和高性能计算环境中扮演更加重要的角色。
