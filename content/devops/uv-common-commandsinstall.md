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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UO6Y4PAT%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2Bxj%2Be%2Fi6wJ7Dcz0cGstHBDxRqx32zyTdmJsZuG7UT1AIgRUdIVk9eAAd6B4Jxs6gnBrOeN2Vr1k2sv4p1gSbBRbAqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPAJHM%2FnAx64V%2B9lOSrcAwu2no%2B%2FvKVAoIoK9%2BUhc3dSnrh20JLYFYxiH5A6kaMz6ban4URRoEySF3BEwk30F%2BOI68Jadjoevcp3CKPVSx6JKdGjq5bzohYO5%2FtFwpx6kQFnbi3Cff57FbUA%2Fdy9%2FLT%2F0u6katmlslDVxcG7R2aL29nf2vYovXxU33WBhmnyc%2FBBUW5JTn0YAzydiIhU4aJgStc7NM4yIijQ5srYgkcC0ORBagwPpH2r37NRmiyKN8bbxxDWxywZ6aGCSpA0RmW3UOGKSkNnQJOmT2qegoLtXo9AwmMvSddrx2ZK8ALIyxMr9AyzJq%2BJTbVl1RpkCVU3F0nEmc2aDZdcg8N5tO%2FwVSEDl9XQ1%2Bf4hPnGMwq2sX0PkGVfoeQEp6BPZFW6U4ytKE5n3OpZqVBdlzZoj03aiX1P3ceE%2BV6Cv67c%2BRyZgTqM25UyITw21P3LgdS6ShV%2By8nfiGqQdhD4uPHvhpysJ6v48lYXghLI%2B0HvENPKmuVENDuaGrY5ncpkkr%2FSzryL8qpbwKEij9EAthx08MaAyt1tmhq0Goq4rN2V1mmLU03eyMglFx%2BWtPxtzeg3cbhZ5AhcEL97f9i0Vxzklk8rHABrJwMLBjp3%2FBebRsHbuLkiCd%2FGQl%2Fz8j4FMMv5hssGOqUBL3G2SRbTSQ0dCzsQVr3vU2QBgYkmfxRl%2Bev5a0OzGUd7J5XwIHrPWq2lV3cSdFRDFcE8DIqTD5yCE94%2F9aRUeWn%2BkSbq5D9Jd6ys3CRNkvlP8wdWDLokngyxz5r%2BoRc7eRJWeIJftcT953TDrIeRVDYri1Jtq6TpGlaZHNRt8qZ32hlatSDeD%2F%2BR1FJQ%2Bb%2FN%2FPW6O%2F9U9ljbwLSc2gITa0LA3KR4&X-Amz-Signature=9ff66da20407d24da07390f48bb297a455cc5e88065f4f7daeff22b644ae12ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UO6Y4PAT%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2Bxj%2Be%2Fi6wJ7Dcz0cGstHBDxRqx32zyTdmJsZuG7UT1AIgRUdIVk9eAAd6B4Jxs6gnBrOeN2Vr1k2sv4p1gSbBRbAqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPAJHM%2FnAx64V%2B9lOSrcAwu2no%2B%2FvKVAoIoK9%2BUhc3dSnrh20JLYFYxiH5A6kaMz6ban4URRoEySF3BEwk30F%2BOI68Jadjoevcp3CKPVSx6JKdGjq5bzohYO5%2FtFwpx6kQFnbi3Cff57FbUA%2Fdy9%2FLT%2F0u6katmlslDVxcG7R2aL29nf2vYovXxU33WBhmnyc%2FBBUW5JTn0YAzydiIhU4aJgStc7NM4yIijQ5srYgkcC0ORBagwPpH2r37NRmiyKN8bbxxDWxywZ6aGCSpA0RmW3UOGKSkNnQJOmT2qegoLtXo9AwmMvSddrx2ZK8ALIyxMr9AyzJq%2BJTbVl1RpkCVU3F0nEmc2aDZdcg8N5tO%2FwVSEDl9XQ1%2Bf4hPnGMwq2sX0PkGVfoeQEp6BPZFW6U4ytKE5n3OpZqVBdlzZoj03aiX1P3ceE%2BV6Cv67c%2BRyZgTqM25UyITw21P3LgdS6ShV%2By8nfiGqQdhD4uPHvhpysJ6v48lYXghLI%2B0HvENPKmuVENDuaGrY5ncpkkr%2FSzryL8qpbwKEij9EAthx08MaAyt1tmhq0Goq4rN2V1mmLU03eyMglFx%2BWtPxtzeg3cbhZ5AhcEL97f9i0Vxzklk8rHABrJwMLBjp3%2FBebRsHbuLkiCd%2FGQl%2Fz8j4FMMv5hssGOqUBL3G2SRbTSQ0dCzsQVr3vU2QBgYkmfxRl%2Bev5a0OzGUd7J5XwIHrPWq2lV3cSdFRDFcE8DIqTD5yCE94%2F9aRUeWn%2BkSbq5D9Jd6ys3CRNkvlP8wdWDLokngyxz5r%2BoRc7eRJWeIJftcT953TDrIeRVDYri1Jtq6TpGlaZHNRt8qZ32hlatSDeD%2F%2BR1FJQ%2Bb%2FN%2FPW6O%2F9U9ljbwLSc2gITa0LA3KR4&X-Amz-Signature=d9528a70eec36818bf6fe35ee096b5a2e217583efc0188576394e8bb5fb91651&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UO6Y4PAT%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2Bxj%2Be%2Fi6wJ7Dcz0cGstHBDxRqx32zyTdmJsZuG7UT1AIgRUdIVk9eAAd6B4Jxs6gnBrOeN2Vr1k2sv4p1gSbBRbAqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPAJHM%2FnAx64V%2B9lOSrcAwu2no%2B%2FvKVAoIoK9%2BUhc3dSnrh20JLYFYxiH5A6kaMz6ban4URRoEySF3BEwk30F%2BOI68Jadjoevcp3CKPVSx6JKdGjq5bzohYO5%2FtFwpx6kQFnbi3Cff57FbUA%2Fdy9%2FLT%2F0u6katmlslDVxcG7R2aL29nf2vYovXxU33WBhmnyc%2FBBUW5JTn0YAzydiIhU4aJgStc7NM4yIijQ5srYgkcC0ORBagwPpH2r37NRmiyKN8bbxxDWxywZ6aGCSpA0RmW3UOGKSkNnQJOmT2qegoLtXo9AwmMvSddrx2ZK8ALIyxMr9AyzJq%2BJTbVl1RpkCVU3F0nEmc2aDZdcg8N5tO%2FwVSEDl9XQ1%2Bf4hPnGMwq2sX0PkGVfoeQEp6BPZFW6U4ytKE5n3OpZqVBdlzZoj03aiX1P3ceE%2BV6Cv67c%2BRyZgTqM25UyITw21P3LgdS6ShV%2By8nfiGqQdhD4uPHvhpysJ6v48lYXghLI%2B0HvENPKmuVENDuaGrY5ncpkkr%2FSzryL8qpbwKEij9EAthx08MaAyt1tmhq0Goq4rN2V1mmLU03eyMglFx%2BWtPxtzeg3cbhZ5AhcEL97f9i0Vxzklk8rHABrJwMLBjp3%2FBebRsHbuLkiCd%2FGQl%2Fz8j4FMMv5hssGOqUBL3G2SRbTSQ0dCzsQVr3vU2QBgYkmfxRl%2Bev5a0OzGUd7J5XwIHrPWq2lV3cSdFRDFcE8DIqTD5yCE94%2F9aRUeWn%2BkSbq5D9Jd6ys3CRNkvlP8wdWDLokngyxz5r%2BoRc7eRJWeIJftcT953TDrIeRVDYri1Jtq6TpGlaZHNRt8qZ32hlatSDeD%2F%2BR1FJQ%2Bb%2FN%2FPW6O%2F9U9ljbwLSc2gITa0LA3KR4&X-Amz-Signature=901d9383b0989882f09a375c0ba95bb9368022bf7314e075d2cfcde8394545a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

