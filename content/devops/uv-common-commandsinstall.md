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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3PD76ME%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQD5R7eFMobLMXuia2P6K67Z174JKoUNwa1U8QYtPK5R9AIgdll7DIhtRKVYQEZS499cXKevOf%2FkaXRNjqdfNorV7U0q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDGfZc5Mu3u1qNCso%2ByrcA1sL%2FFYv1fU87iCWKmp8Fe%2Bx0z7lS6cKbYtkRygPAuCAVoKuwt0rlHCDaVZQ1hyCrBTVeeGX5MOKGPApuU7vQHr4ugIQ6grNJbkkjkpsmU1rFXtBvY7C9%2BV8AN1p9uhvnJh%2BF5LLqal8P39I%2BWsJEqAMOnDg%2FZzwSL0bkTOxM%2Bhsz4RdvmpyzKQzBi1%2BLkwGO9Fad%2B4Z0X0oUdmXO4qws1%2Bi5WGuD1TABhnSlrBKhOPLssT0Niu66KxF25dEG34p6ZP0W3n6xG3lgFsv4LQYD6aiWdDPKeSNPTJv6kU1iVu7gMpim4GmgftuTiMXtJ5tXb02oVQC7XqNvPNoV%2F1lbM6Q%2Fxaz9N65kYQBDzfjXJtKGthLePW07EgSulFDnMupakpOIDyGTDKitQ3EMJAHjrerq0ntGro%2BjqdEjpTCDD9eg2xB7%2Bmm%2B4KftFBtho5qUcd%2B5uyhzZCCscGhd%2BCcHQGbwntXRpKrroeGSlvS1tJCTslVlbXORVmCqRJmt%2BUmutsFGtp9xAksWEJjc4nmJbctO8vfsGy9CU9zJfPCnhhDNtu7kEQgXT%2Fo%2BWUwLhvN%2FZaczAcAh1WrFEDfak15trhXH6FHismhAG1YlYyxMaS460VW%2BeL20HoAGU6aMO%2B48s0GOqUBBqBWY9Q6ydnti1SkV6XAzfMYlejRV8ZFHAhQh8V5oD6Ra06lyQYxoeWshInbR4Ph%2Bb8oNS4o0GHd0VF9iigxFRpk8TNfHPgQtHb82U5Q1D4xtQKSpssQpCYu4DuTNHVCpnt3ZEGj1gSOllqbN0HPx8zIyvBwtc5CJGVI%2BeuQCKPcam3pVG%2BxdWPXiq7MED5dWzraFTalrdYkI%2BbOfd0z%2BLLyRTte&X-Amz-Signature=ddcf83d9addf5973b9239c8618d5f3ebeacabd08c37a03a885364ec00f69dca3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3PD76ME%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQD5R7eFMobLMXuia2P6K67Z174JKoUNwa1U8QYtPK5R9AIgdll7DIhtRKVYQEZS499cXKevOf%2FkaXRNjqdfNorV7U0q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDGfZc5Mu3u1qNCso%2ByrcA1sL%2FFYv1fU87iCWKmp8Fe%2Bx0z7lS6cKbYtkRygPAuCAVoKuwt0rlHCDaVZQ1hyCrBTVeeGX5MOKGPApuU7vQHr4ugIQ6grNJbkkjkpsmU1rFXtBvY7C9%2BV8AN1p9uhvnJh%2BF5LLqal8P39I%2BWsJEqAMOnDg%2FZzwSL0bkTOxM%2Bhsz4RdvmpyzKQzBi1%2BLkwGO9Fad%2B4Z0X0oUdmXO4qws1%2Bi5WGuD1TABhnSlrBKhOPLssT0Niu66KxF25dEG34p6ZP0W3n6xG3lgFsv4LQYD6aiWdDPKeSNPTJv6kU1iVu7gMpim4GmgftuTiMXtJ5tXb02oVQC7XqNvPNoV%2F1lbM6Q%2Fxaz9N65kYQBDzfjXJtKGthLePW07EgSulFDnMupakpOIDyGTDKitQ3EMJAHjrerq0ntGro%2BjqdEjpTCDD9eg2xB7%2Bmm%2B4KftFBtho5qUcd%2B5uyhzZCCscGhd%2BCcHQGbwntXRpKrroeGSlvS1tJCTslVlbXORVmCqRJmt%2BUmutsFGtp9xAksWEJjc4nmJbctO8vfsGy9CU9zJfPCnhhDNtu7kEQgXT%2Fo%2BWUwLhvN%2FZaczAcAh1WrFEDfak15trhXH6FHismhAG1YlYyxMaS460VW%2BeL20HoAGU6aMO%2B48s0GOqUBBqBWY9Q6ydnti1SkV6XAzfMYlejRV8ZFHAhQh8V5oD6Ra06lyQYxoeWshInbR4Ph%2Bb8oNS4o0GHd0VF9iigxFRpk8TNfHPgQtHb82U5Q1D4xtQKSpssQpCYu4DuTNHVCpnt3ZEGj1gSOllqbN0HPx8zIyvBwtc5CJGVI%2BeuQCKPcam3pVG%2BxdWPXiq7MED5dWzraFTalrdYkI%2BbOfd0z%2BLLyRTte&X-Amz-Signature=acfee7958dd1887456061c96b7f43247aa1118599d1f373214a0796cc507a7d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3PD76ME%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQD5R7eFMobLMXuia2P6K67Z174JKoUNwa1U8QYtPK5R9AIgdll7DIhtRKVYQEZS499cXKevOf%2FkaXRNjqdfNorV7U0q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDGfZc5Mu3u1qNCso%2ByrcA1sL%2FFYv1fU87iCWKmp8Fe%2Bx0z7lS6cKbYtkRygPAuCAVoKuwt0rlHCDaVZQ1hyCrBTVeeGX5MOKGPApuU7vQHr4ugIQ6grNJbkkjkpsmU1rFXtBvY7C9%2BV8AN1p9uhvnJh%2BF5LLqal8P39I%2BWsJEqAMOnDg%2FZzwSL0bkTOxM%2Bhsz4RdvmpyzKQzBi1%2BLkwGO9Fad%2B4Z0X0oUdmXO4qws1%2Bi5WGuD1TABhnSlrBKhOPLssT0Niu66KxF25dEG34p6ZP0W3n6xG3lgFsv4LQYD6aiWdDPKeSNPTJv6kU1iVu7gMpim4GmgftuTiMXtJ5tXb02oVQC7XqNvPNoV%2F1lbM6Q%2Fxaz9N65kYQBDzfjXJtKGthLePW07EgSulFDnMupakpOIDyGTDKitQ3EMJAHjrerq0ntGro%2BjqdEjpTCDD9eg2xB7%2Bmm%2B4KftFBtho5qUcd%2B5uyhzZCCscGhd%2BCcHQGbwntXRpKrroeGSlvS1tJCTslVlbXORVmCqRJmt%2BUmutsFGtp9xAksWEJjc4nmJbctO8vfsGy9CU9zJfPCnhhDNtu7kEQgXT%2Fo%2BWUwLhvN%2FZaczAcAh1WrFEDfak15trhXH6FHismhAG1YlYyxMaS460VW%2BeL20HoAGU6aMO%2B48s0GOqUBBqBWY9Q6ydnti1SkV6XAzfMYlejRV8ZFHAhQh8V5oD6Ra06lyQYxoeWshInbR4Ph%2Bb8oNS4o0GHd0VF9iigxFRpk8TNfHPgQtHb82U5Q1D4xtQKSpssQpCYu4DuTNHVCpnt3ZEGj1gSOllqbN0HPx8zIyvBwtc5CJGVI%2BeuQCKPcam3pVG%2BxdWPXiq7MED5dWzraFTalrdYkI%2BbOfd0z%2BLLyRTte&X-Amz-Signature=074885536e12a7f9537661e8d68a08675295ee231848d22ed959d152ff893d94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

