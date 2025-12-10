---
title: Ngrok安装 | 运行方法
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-29T12:21:00.000Z'
draft: false
tags:
- Ngrok
categories:
- DevOps
---

> 💡 前几天帮人微调模型的时候，使用的LlamaFactory的WebUI，由于服务部署到他的内网环境内，做了内网穿透使得可以让多人访问。刚好想着了解一下，在此背景下，撰写了本文章。

## 内网穿透

### 原理

又称为NAT穿透。NAT穿透技术是让NAT背后的设备，先访问指定的外网服务器，由指定的外网服务器搭建桥梁，打通内、外网设备的访问通道，最终实现外网设备访问到内网设备。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYZNZ7O4%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQDmxgSbhcioMCeUbEtBCcSXmaw51xJCC42KEbfqEqG04wIgJggAatrqw4sILLb%2BC0AOM8RnJr7Fq5BrhW1tb3QnxGcqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMfw9ZCxvWTszAVLXyrcAzfxgH1bmhpb2kEEDZxrYmYw6XpK5me2Aa1VhOC9aL0xHzu5WfEvxQ3IAcdjl9g5Mq2%2B%2FI7z4C%2FEyXlm%2Bb%2B6CWc6MwOmMKIzV0XDbSmmTsg2ywzMdRBpVVgO3060meug5yKOt1jwrGHJ2QtCT9oF%2FmLqVPn3ZbfjmGPLkaz4QE%2FmJ%2BFGyWa4V3kw2P%2Fm%2FaXiTPazvWwnFpeFr4N8ObZ4ED2FsLdvkLgCKqpZ8ByYE%2B88Xv7kpf4qISL0hvI8Q6Y0YkyXDedvRk%2Bt7V42OTZ3vKaAMgDVRLLf6%2BwZ2dM0VNYHtWfdYnQMVSgn0F61maaIjlxz3wxy9tHK4UAGKbjMZNJ9cOH05NwRLwumrm1%2FgAu%2BFWgviqq%2BmYMVz%2FBKaUATp6eVz5T0LfAlSc7StB22T%2BNLLuVjYPzpGVhgxtvOlkQPLjYmLj4NoVCd9UxtDl4hOwQOCywoZNNl0IDrPnCq0pEZw4otgzs6Zp%2FaWB6VhHrPeak9SDvinNO298SATbe2dYBSkJhnOzaFMEdcMjhW8p%2FjLg98QPX45%2BmWcUabjAgW0tJbNWjO%2F%2BsaqvOc%2BtaOqYXsYGul7jXwh0WUnEABcgSZJdjmUr7jYWc5u4adZPYL7clOjqHVVhonlygKMKG%2F48kGOqUB9B0sf%2F21xbZR6%2BdCaRaF51EJnNJT2V%2Fy4aMnjc77O2EKSxQbsx%2BvrYfOSm7C9JiKFwf1Dek96BFsvn4bzxxKHnbgHHfnNEiQTAEPZBW%2Be6KhAttX3yhOzGuwqw5AeRxvLasZRSvcvtADQtX1rikO3vKWI1AO8EXaIAPBIG%2FbVeISAH7nEweZuPROMZKrwqxz9veGaIud%2FeEwhg2yntrP4ippYKNq&X-Amz-Signature=7379f9efd0c41d96a29261e55ad5cb87ad636b52a1ffdaf90112d656bee745ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 常用工具

参考各大论坛关于内网穿透工具的评论区。

- Ngrok
- frp
- 花生壳
- ZEROTIER
- 樱花FRP
## Ngrok

ngrok的极其简单，官网写的很清楚，下面是官方的安装教程。为了加深记忆，我就复制一下吧。

[https://dashboard.ngrok.com/get-started/setup/windows](https://dashboard.ngrok.com/get-started/setup/windows)

### 安装

安装前需要在该网站进行账号的注册，用于登陆。

1. 根据自身情况，选择合适的安装方式。
1. 假设选择是在Windows内安装，打开终端，输入：
---

### 使用

在终端输入：

```json
ngrok http http://localhost:80
```

> 表示将本地的80端口映射到ngrok的服务器内。

---

> Reference

