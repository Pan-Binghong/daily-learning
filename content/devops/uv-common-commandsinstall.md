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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCBK4PS4%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA6Wfq7zFBuAf3dAUZ28b7XS0hp29qzgAy2guba9JJonAiEA3N24y7ppIm7v7cBC9Sz8q0rRnGDD45dMBELFMbMomB8qiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKlJObASGJsPRr71SSrcAwhCgHpP85f2iWYue6jbUbVyCgpQGgJ6p4SqRX7v517bl9Vzp8muMSsU4PQz%2BfH5aTguk5lxSfG49AhJysaICOPKN%2Bc06V4ICdHp3KpFpfnV0byJ%2BmhCdGrAkbk8PAEOeFsL91HcKnnc3gI0QGvctpozKLj6UX4UVRkKnYs3gqfPN7MFjkH%2BwTFmbm%2FeKtD8pKOhGqvx0YGQt4qE6h6w0YKvghrHTVF6lW5X2vLE%2F0t0VH56PQ8%2FmCyDqXE%2Fwhtjfr3Jzj%2BT3o7Vu8zdsVM051k%2BB7p7mKecuMKZ%2BUzJWFk7foTi2JgWeYK69HVSwsPEn6PF2HkGe16tS2egrvcxJkibqwidhSzlk4jso%2BAUWg6M4VMomi3gBPwpWDtKSFseVLKEepQjTBB6SA2JzLpdBf6qDadBpoge1PwPdtClnPrs7KwcJ%2B8ILEJTVScol8JmeJQzjHpaWr%2BKLdwtsrcYxou6eRHACXPomirqZGsmbMWUJJXsfASOI7OmdAwtkJklXX0PXky0SxUp4b1I3P5s6gpF6djVv3Oq0ieuXvaEEODTYSu%2BqAiFt%2BjhqblCULr6no%2F4OXN7uWJIkfbcd2gA4IbgGoarPZfGqUtdmUQpootEWhS6A1cnynAvH3XrMNfeo80GOqUBbw0JeCvdtLVXpapDlcT6mW51Ch4F1uC8FvFvdgrJwaGPlgkM9v4yJuHLfwoDvz1rfusUgqaiuv93xScy5fgJZg0Sh7rv1amLuRSMB%2B4SIcF5jGQwT836xfjofYwjkWZ5aki2rBitCSrKr2KrkWjlDA3CfvlGGKtFDfWth%2FCSCToEICRG1Sr79jUdR7UQPk0Y15JvvWznYRktsBNVEtlY7GpwUGye&X-Amz-Signature=bf9f50fa9279555d57a812f52773243b27911a5da4d7dbdf1af732e7e50626b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCBK4PS4%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA6Wfq7zFBuAf3dAUZ28b7XS0hp29qzgAy2guba9JJonAiEA3N24y7ppIm7v7cBC9Sz8q0rRnGDD45dMBELFMbMomB8qiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKlJObASGJsPRr71SSrcAwhCgHpP85f2iWYue6jbUbVyCgpQGgJ6p4SqRX7v517bl9Vzp8muMSsU4PQz%2BfH5aTguk5lxSfG49AhJysaICOPKN%2Bc06V4ICdHp3KpFpfnV0byJ%2BmhCdGrAkbk8PAEOeFsL91HcKnnc3gI0QGvctpozKLj6UX4UVRkKnYs3gqfPN7MFjkH%2BwTFmbm%2FeKtD8pKOhGqvx0YGQt4qE6h6w0YKvghrHTVF6lW5X2vLE%2F0t0VH56PQ8%2FmCyDqXE%2Fwhtjfr3Jzj%2BT3o7Vu8zdsVM051k%2BB7p7mKecuMKZ%2BUzJWFk7foTi2JgWeYK69HVSwsPEn6PF2HkGe16tS2egrvcxJkibqwidhSzlk4jso%2BAUWg6M4VMomi3gBPwpWDtKSFseVLKEepQjTBB6SA2JzLpdBf6qDadBpoge1PwPdtClnPrs7KwcJ%2B8ILEJTVScol8JmeJQzjHpaWr%2BKLdwtsrcYxou6eRHACXPomirqZGsmbMWUJJXsfASOI7OmdAwtkJklXX0PXky0SxUp4b1I3P5s6gpF6djVv3Oq0ieuXvaEEODTYSu%2BqAiFt%2BjhqblCULr6no%2F4OXN7uWJIkfbcd2gA4IbgGoarPZfGqUtdmUQpootEWhS6A1cnynAvH3XrMNfeo80GOqUBbw0JeCvdtLVXpapDlcT6mW51Ch4F1uC8FvFvdgrJwaGPlgkM9v4yJuHLfwoDvz1rfusUgqaiuv93xScy5fgJZg0Sh7rv1amLuRSMB%2B4SIcF5jGQwT836xfjofYwjkWZ5aki2rBitCSrKr2KrkWjlDA3CfvlGGKtFDfWth%2FCSCToEICRG1Sr79jUdR7UQPk0Y15JvvWznYRktsBNVEtlY7GpwUGye&X-Amz-Signature=d9eebad99d440294ad2515089bd89047271772af2a81069e29ff00cd0f00682b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCBK4PS4%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA6Wfq7zFBuAf3dAUZ28b7XS0hp29qzgAy2guba9JJonAiEA3N24y7ppIm7v7cBC9Sz8q0rRnGDD45dMBELFMbMomB8qiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKlJObASGJsPRr71SSrcAwhCgHpP85f2iWYue6jbUbVyCgpQGgJ6p4SqRX7v517bl9Vzp8muMSsU4PQz%2BfH5aTguk5lxSfG49AhJysaICOPKN%2Bc06V4ICdHp3KpFpfnV0byJ%2BmhCdGrAkbk8PAEOeFsL91HcKnnc3gI0QGvctpozKLj6UX4UVRkKnYs3gqfPN7MFjkH%2BwTFmbm%2FeKtD8pKOhGqvx0YGQt4qE6h6w0YKvghrHTVF6lW5X2vLE%2F0t0VH56PQ8%2FmCyDqXE%2Fwhtjfr3Jzj%2BT3o7Vu8zdsVM051k%2BB7p7mKecuMKZ%2BUzJWFk7foTi2JgWeYK69HVSwsPEn6PF2HkGe16tS2egrvcxJkibqwidhSzlk4jso%2BAUWg6M4VMomi3gBPwpWDtKSFseVLKEepQjTBB6SA2JzLpdBf6qDadBpoge1PwPdtClnPrs7KwcJ%2B8ILEJTVScol8JmeJQzjHpaWr%2BKLdwtsrcYxou6eRHACXPomirqZGsmbMWUJJXsfASOI7OmdAwtkJklXX0PXky0SxUp4b1I3P5s6gpF6djVv3Oq0ieuXvaEEODTYSu%2BqAiFt%2BjhqblCULr6no%2F4OXN7uWJIkfbcd2gA4IbgGoarPZfGqUtdmUQpootEWhS6A1cnynAvH3XrMNfeo80GOqUBbw0JeCvdtLVXpapDlcT6mW51Ch4F1uC8FvFvdgrJwaGPlgkM9v4yJuHLfwoDvz1rfusUgqaiuv93xScy5fgJZg0Sh7rv1amLuRSMB%2B4SIcF5jGQwT836xfjofYwjkWZ5aki2rBitCSrKr2KrkWjlDA3CfvlGGKtFDfWth%2FCSCToEICRG1Sr79jUdR7UQPk0Y15JvvWznYRktsBNVEtlY7GpwUGye&X-Amz-Signature=9d0f25648b52e59fda3284a2da29e2fa412bc72dde3f7e6fc83bfafe42867dfe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

