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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4NZDQ3L%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI2nIanmxnbnKGxx2eO8ijyM55%2FWNd2UVl7zRg54mOmgIhANfBNMgTaHkj1ZqnRzEKjsyflwJcVE0%2FeglaVRdnmyKJKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwxW8xZ%2Fqc4E8BbR6Iq3AO2O4xIIRnGP6FDJbKTgRIW%2BX6jdxiyDpq1%2FqV3r8JteTbhS6FtbdE21uWBoVZDPpRukMXwMdSlN6ectwO7OpWmf0rqQcjaFpUJsi0mTqrJWdlm9IMPMAuzQXXIOgmSSYb1r1rp6l4xSHpBxs2VbbKEc9c%2Fwbd9upujZbF2IriygmGbrZdXoorkPO0yH6QWktOH9tKrVT8y7mrnyASmA2PtMNtrN7Qe97t7HRxnuseeiD%2BkEBQj4RG9f91BeVwSC5MWkIkBBe3JAdhw4LuFwFWwANJxPYzPf9xLs1A%2FkOhOkCgEVVCALe5KJf3ghXZaAVCdJN6qBZSQdWHznBQG%2Fz3tYDhljzqPGvC%2BXzoXQJFaEPOvF6pYUdwCesdEWu5IlY3pX0K3%2FGRUDpqcCDEY3uqPm76S1bNC2jBbLP5lPp64sfnv%2BFwZgij49vs%2BgoXPACw%2FpoJU7SVKXlDaxgt9hvabfOi5nTot4RJDZeRYSn0t1uAP2qQYGwDpy%2BcUmUbikE4a3gV%2FXtH%2B9NpE7OPulLlk98CvWbzreyPn9dKPKoESE2PbrNkq13J%2FbdvNsdHXlvgso6VpP06vTZEqv0Q7gzrGu0%2FoXTFqWFd3lflzvNlh%2Fc09fiL19B%2FQGMUxVjDwjt7JBjqkAd9QoC2olrA18XL1Qsc7x%2FUE90djOzcVecGNJBYfXHd1a9t7%2BEJup73zxpK9lCmYsyJoZsx9fAGo880DQgS7wmkSgvvpz%2FZu%2Bz4fF2Q8rmH1apbV9x%2FgPFWzsnXWBwm0GRioHjkbWDIqE3fv7AlL%2FpkVGIsvmdjRXwHcQhknGmEvCiSYZgF6g9TPVEHdsHDa0eKjm3Ri2X%2F%2FhOHiNOShlSiJmdin&X-Amz-Signature=c21e8996acee83d5e1eefc150311ac64ab2421d2baf7dee48a5643917830fe40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4NZDQ3L%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI2nIanmxnbnKGxx2eO8ijyM55%2FWNd2UVl7zRg54mOmgIhANfBNMgTaHkj1ZqnRzEKjsyflwJcVE0%2FeglaVRdnmyKJKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwxW8xZ%2Fqc4E8BbR6Iq3AO2O4xIIRnGP6FDJbKTgRIW%2BX6jdxiyDpq1%2FqV3r8JteTbhS6FtbdE21uWBoVZDPpRukMXwMdSlN6ectwO7OpWmf0rqQcjaFpUJsi0mTqrJWdlm9IMPMAuzQXXIOgmSSYb1r1rp6l4xSHpBxs2VbbKEc9c%2Fwbd9upujZbF2IriygmGbrZdXoorkPO0yH6QWktOH9tKrVT8y7mrnyASmA2PtMNtrN7Qe97t7HRxnuseeiD%2BkEBQj4RG9f91BeVwSC5MWkIkBBe3JAdhw4LuFwFWwANJxPYzPf9xLs1A%2FkOhOkCgEVVCALe5KJf3ghXZaAVCdJN6qBZSQdWHznBQG%2Fz3tYDhljzqPGvC%2BXzoXQJFaEPOvF6pYUdwCesdEWu5IlY3pX0K3%2FGRUDpqcCDEY3uqPm76S1bNC2jBbLP5lPp64sfnv%2BFwZgij49vs%2BgoXPACw%2FpoJU7SVKXlDaxgt9hvabfOi5nTot4RJDZeRYSn0t1uAP2qQYGwDpy%2BcUmUbikE4a3gV%2FXtH%2B9NpE7OPulLlk98CvWbzreyPn9dKPKoESE2PbrNkq13J%2FbdvNsdHXlvgso6VpP06vTZEqv0Q7gzrGu0%2FoXTFqWFd3lflzvNlh%2Fc09fiL19B%2FQGMUxVjDwjt7JBjqkAd9QoC2olrA18XL1Qsc7x%2FUE90djOzcVecGNJBYfXHd1a9t7%2BEJup73zxpK9lCmYsyJoZsx9fAGo880DQgS7wmkSgvvpz%2FZu%2Bz4fF2Q8rmH1apbV9x%2FgPFWzsnXWBwm0GRioHjkbWDIqE3fv7AlL%2FpkVGIsvmdjRXwHcQhknGmEvCiSYZgF6g9TPVEHdsHDa0eKjm3Ri2X%2F%2FhOHiNOShlSiJmdin&X-Amz-Signature=19863ac4e39517984a20375e58dedca00c6100be4e7f34150c2105f03fc410ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4NZDQ3L%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI2nIanmxnbnKGxx2eO8ijyM55%2FWNd2UVl7zRg54mOmgIhANfBNMgTaHkj1ZqnRzEKjsyflwJcVE0%2FeglaVRdnmyKJKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwxW8xZ%2Fqc4E8BbR6Iq3AO2O4xIIRnGP6FDJbKTgRIW%2BX6jdxiyDpq1%2FqV3r8JteTbhS6FtbdE21uWBoVZDPpRukMXwMdSlN6ectwO7OpWmf0rqQcjaFpUJsi0mTqrJWdlm9IMPMAuzQXXIOgmSSYb1r1rp6l4xSHpBxs2VbbKEc9c%2Fwbd9upujZbF2IriygmGbrZdXoorkPO0yH6QWktOH9tKrVT8y7mrnyASmA2PtMNtrN7Qe97t7HRxnuseeiD%2BkEBQj4RG9f91BeVwSC5MWkIkBBe3JAdhw4LuFwFWwANJxPYzPf9xLs1A%2FkOhOkCgEVVCALe5KJf3ghXZaAVCdJN6qBZSQdWHznBQG%2Fz3tYDhljzqPGvC%2BXzoXQJFaEPOvF6pYUdwCesdEWu5IlY3pX0K3%2FGRUDpqcCDEY3uqPm76S1bNC2jBbLP5lPp64sfnv%2BFwZgij49vs%2BgoXPACw%2FpoJU7SVKXlDaxgt9hvabfOi5nTot4RJDZeRYSn0t1uAP2qQYGwDpy%2BcUmUbikE4a3gV%2FXtH%2B9NpE7OPulLlk98CvWbzreyPn9dKPKoESE2PbrNkq13J%2FbdvNsdHXlvgso6VpP06vTZEqv0Q7gzrGu0%2FoXTFqWFd3lflzvNlh%2Fc09fiL19B%2FQGMUxVjDwjt7JBjqkAd9QoC2olrA18XL1Qsc7x%2FUE90djOzcVecGNJBYfXHd1a9t7%2BEJup73zxpK9lCmYsyJoZsx9fAGo880DQgS7wmkSgvvpz%2FZu%2Bz4fF2Q8rmH1apbV9x%2FgPFWzsnXWBwm0GRioHjkbWDIqE3fv7AlL%2FpkVGIsvmdjRXwHcQhknGmEvCiSYZgF6g9TPVEHdsHDa0eKjm3Ri2X%2F%2FhOHiNOShlSiJmdin&X-Amz-Signature=cf60be744faf2191e3d45caf2e33a03076fcca896105b85bf2f99bf5a6122a6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

