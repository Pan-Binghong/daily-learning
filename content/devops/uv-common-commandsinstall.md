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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJS4S5CY%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0DPaFdtCX1i6R%2FMRENvyuZaxQslsQoP5S9cA88bBLDQIgb%2FOaxiSuuzhq3%2BLhHQdgVUgq8KSVfwDqxIx%2BIAbwKMMq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDBxeMLlWFwmkBH7TAyrcA1SkpjpoJ7OPO4QIYMmm%2FAPWLF%2BpiNNZh2OCtSN0bloVWDimw5Zd5sz2Zdum5ey3nJ47SAIAdkQWl2AI7iKPr7%2BF01zqJUEEws8s0pZyXImv6eNZOxNbDxBB%2B9T1O%2BjcsV8%2FXOLg%2BFtf1%2Bn%2B65K93J7aw3%2BJn%2FErGBMM7LQOGas4UJZ2GkM8qant2xI3fUmMT9jw1vD8jek940YVHRhOgwZuG4TxtaMIPi8UzxzcbiA9OUHbFAsZko9Oth%2BD0VJUK8Xk1yxUGJBIBmbifvpkAVgKsqUHw3qJP3YeJOM7kIGJgozKDZ1HM8xWmd5RPTMM79LhrJb8STFRIECwdC9UZT0Q%2B43GdDMd19bg62Xec7ZIhEpGEuL3sBN2RiwVAmlVyPdvbqm7dcU3lV%2F5kDq9jXnVMkn7GdWHbtDWVu2RZJFsKpYityeF0HxLnubQsLDDmYP%2BfvkJARnEt7D4DzA4deyIF8zKhF9NW06XS1TEPnsYL3fBOmJg4Rsq3KV1HqMLV8%2FMSTllGmXLO9laPDpbT4ZeA%2BoNg%2Fdc0iiLGNo3a282e2lbvgb5DXSP9XNIe78EvCDGwI0auD%2BKFUnMntzrcFZiitcdcY5oR2XVAzhEhICnhTfmL3zqeee3kWtYMMmi68sGOqUBoie3zPfA%2BS%2FGso1%2F8S98kAY5u3J97Yx82wXgmODfICR7CkDlFfU94rqtREvCXjU3tce0SDN6OEM9Tk2KwQoSXyBPSsyQLZzW3vbWDKHtLqYkNc5Z2YTAhEM%2BmPzRnMEGFqD9mVRX5K9rXlRsaqw3Y49P0YtKS4Hxl3GjmFeLsjH2Is2i3qhOQpYXpRFqKY5UBNEkcV6Te97jMNNWPDe%2BjdFgtD0E&X-Amz-Signature=f9fc4b15d1019c3bc30fc9c9e90406a359256bdd8bfd61fd697fb6c3ceb31bef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJS4S5CY%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0DPaFdtCX1i6R%2FMRENvyuZaxQslsQoP5S9cA88bBLDQIgb%2FOaxiSuuzhq3%2BLhHQdgVUgq8KSVfwDqxIx%2BIAbwKMMq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDBxeMLlWFwmkBH7TAyrcA1SkpjpoJ7OPO4QIYMmm%2FAPWLF%2BpiNNZh2OCtSN0bloVWDimw5Zd5sz2Zdum5ey3nJ47SAIAdkQWl2AI7iKPr7%2BF01zqJUEEws8s0pZyXImv6eNZOxNbDxBB%2B9T1O%2BjcsV8%2FXOLg%2BFtf1%2Bn%2B65K93J7aw3%2BJn%2FErGBMM7LQOGas4UJZ2GkM8qant2xI3fUmMT9jw1vD8jek940YVHRhOgwZuG4TxtaMIPi8UzxzcbiA9OUHbFAsZko9Oth%2BD0VJUK8Xk1yxUGJBIBmbifvpkAVgKsqUHw3qJP3YeJOM7kIGJgozKDZ1HM8xWmd5RPTMM79LhrJb8STFRIECwdC9UZT0Q%2B43GdDMd19bg62Xec7ZIhEpGEuL3sBN2RiwVAmlVyPdvbqm7dcU3lV%2F5kDq9jXnVMkn7GdWHbtDWVu2RZJFsKpYityeF0HxLnubQsLDDmYP%2BfvkJARnEt7D4DzA4deyIF8zKhF9NW06XS1TEPnsYL3fBOmJg4Rsq3KV1HqMLV8%2FMSTllGmXLO9laPDpbT4ZeA%2BoNg%2Fdc0iiLGNo3a282e2lbvgb5DXSP9XNIe78EvCDGwI0auD%2BKFUnMntzrcFZiitcdcY5oR2XVAzhEhICnhTfmL3zqeee3kWtYMMmi68sGOqUBoie3zPfA%2BS%2FGso1%2F8S98kAY5u3J97Yx82wXgmODfICR7CkDlFfU94rqtREvCXjU3tce0SDN6OEM9Tk2KwQoSXyBPSsyQLZzW3vbWDKHtLqYkNc5Z2YTAhEM%2BmPzRnMEGFqD9mVRX5K9rXlRsaqw3Y49P0YtKS4Hxl3GjmFeLsjH2Is2i3qhOQpYXpRFqKY5UBNEkcV6Te97jMNNWPDe%2BjdFgtD0E&X-Amz-Signature=683884140043bfd3c0fc7de57e5bd4d0ab192cb43e16d97438fd8162481be22e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJS4S5CY%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0DPaFdtCX1i6R%2FMRENvyuZaxQslsQoP5S9cA88bBLDQIgb%2FOaxiSuuzhq3%2BLhHQdgVUgq8KSVfwDqxIx%2BIAbwKMMq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDBxeMLlWFwmkBH7TAyrcA1SkpjpoJ7OPO4QIYMmm%2FAPWLF%2BpiNNZh2OCtSN0bloVWDimw5Zd5sz2Zdum5ey3nJ47SAIAdkQWl2AI7iKPr7%2BF01zqJUEEws8s0pZyXImv6eNZOxNbDxBB%2B9T1O%2BjcsV8%2FXOLg%2BFtf1%2Bn%2B65K93J7aw3%2BJn%2FErGBMM7LQOGas4UJZ2GkM8qant2xI3fUmMT9jw1vD8jek940YVHRhOgwZuG4TxtaMIPi8UzxzcbiA9OUHbFAsZko9Oth%2BD0VJUK8Xk1yxUGJBIBmbifvpkAVgKsqUHw3qJP3YeJOM7kIGJgozKDZ1HM8xWmd5RPTMM79LhrJb8STFRIECwdC9UZT0Q%2B43GdDMd19bg62Xec7ZIhEpGEuL3sBN2RiwVAmlVyPdvbqm7dcU3lV%2F5kDq9jXnVMkn7GdWHbtDWVu2RZJFsKpYityeF0HxLnubQsLDDmYP%2BfvkJARnEt7D4DzA4deyIF8zKhF9NW06XS1TEPnsYL3fBOmJg4Rsq3KV1HqMLV8%2FMSTllGmXLO9laPDpbT4ZeA%2BoNg%2Fdc0iiLGNo3a282e2lbvgb5DXSP9XNIe78EvCDGwI0auD%2BKFUnMntzrcFZiitcdcY5oR2XVAzhEhICnhTfmL3zqeee3kWtYMMmi68sGOqUBoie3zPfA%2BS%2FGso1%2F8S98kAY5u3J97Yx82wXgmODfICR7CkDlFfU94rqtREvCXjU3tce0SDN6OEM9Tk2KwQoSXyBPSsyQLZzW3vbWDKHtLqYkNc5Z2YTAhEM%2BmPzRnMEGFqD9mVRX5K9rXlRsaqw3Y49P0YtKS4Hxl3GjmFeLsjH2Is2i3qhOQpYXpRFqKY5UBNEkcV6Te97jMNNWPDe%2BjdFgtD0E&X-Amz-Signature=bc080bead1f24db1712e173de6e359a6763f12046c70ecc716f7070e27c730d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

