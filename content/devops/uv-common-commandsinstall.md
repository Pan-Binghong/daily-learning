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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHESINJU%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T041106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQDDe4zcXe4C3n0Nr3ZgAQOtkcZw0xkDUDEBrK8sKHoQ3gIhAPXOtUBG4al0BIDn1o8PxbnquVnzHdTBdFXNG%2BOWmh3pKv8DCCQQABoMNjM3NDIzMTgzODA1Igy%2FvBz2ChjeAZ8fj0Yq3ANOtceM%2Bd41%2F5twYs5uvkMlJ%2FojGcDVsPieoMcjqupEGSM3vrz815A7yni%2FqdGAvlVa7j4jly4jvF2aZc%2FVXMGhgze%2FwUfZyTHhR5sEGof410pM17Hwuc5W0ZMRu70o4%2FZwBym1yj5XYqVNdsi%2FRVIe312W6kpYaRHbd%2Fwdv3QovTLcaN10mTeR9FBs6oaskgg3ch9olThOs%2BVVRQv8L%2BuqJzmmUwUp7gNg2%2Fc2CB%2BuxypmhPECql80DHJdlgMzudVifMt5pfYBpojexzTF6CptXaTvLODfVlTN7yp3FF5oFSeIsYu9GbSTKd5y0tV526bHOV0lch7qGyxamfK6kxrFY4Dchmhl1%2B%2Bjz9p71e%2B1%2FTeO14x9cVwjb6SIpVuiJKOoHQY3DQg%2BUjtLMBwGuS8aZJFqb1BQZ1qPsg4iSZ1K74gQwaOz8uah6u50wsrTSD8Ck4Vvik%2FgKxcoPb2NDjNiO4fpOeg%2By%2FdfRuA7cRR3P37q%2Fivcrj5Ht3MoLccwvk8Ug31y5xGkdrw5%2BZB4sKetdq5FKeg%2B%2FhNS%2Bl3tC4EbSeFUI4IKMy5ryuS4oQqx9hQplvd%2FslfNB920SbU8TKJxg4sCMF00P%2B%2B0ECDRttbCTgNnw26wB7lfUhjnjDC%2BxuHOBjqkARNTLQNmluJzh5pjacXFtlSIukC%2BQLSHhUyb3Ffx%2BeHRlq9p1QpLG%2B0xHZkHwZ5erBvKsFhrcbDQJRlijLGGeKKYNXxSheOa5PAaunam%2FcKAVUn1130QwMXP10RTPVLYK8tc8LG0Esndok%2B%2B%2BkQ3RsPLc85R4S6sSCGFjCnf2euIM7y%2BOCCPEq9Por4srH%2Fl0%2BkA0S62%2BNGd5Xq7fXbtY0%2BTGgM%2B&X-Amz-Signature=3d43f42dc2fbdeeeda7ff5e941eb390c2949118e15d745d760eff3fced0551fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHESINJU%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T041106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQDDe4zcXe4C3n0Nr3ZgAQOtkcZw0xkDUDEBrK8sKHoQ3gIhAPXOtUBG4al0BIDn1o8PxbnquVnzHdTBdFXNG%2BOWmh3pKv8DCCQQABoMNjM3NDIzMTgzODA1Igy%2FvBz2ChjeAZ8fj0Yq3ANOtceM%2Bd41%2F5twYs5uvkMlJ%2FojGcDVsPieoMcjqupEGSM3vrz815A7yni%2FqdGAvlVa7j4jly4jvF2aZc%2FVXMGhgze%2FwUfZyTHhR5sEGof410pM17Hwuc5W0ZMRu70o4%2FZwBym1yj5XYqVNdsi%2FRVIe312W6kpYaRHbd%2Fwdv3QovTLcaN10mTeR9FBs6oaskgg3ch9olThOs%2BVVRQv8L%2BuqJzmmUwUp7gNg2%2Fc2CB%2BuxypmhPECql80DHJdlgMzudVifMt5pfYBpojexzTF6CptXaTvLODfVlTN7yp3FF5oFSeIsYu9GbSTKd5y0tV526bHOV0lch7qGyxamfK6kxrFY4Dchmhl1%2B%2Bjz9p71e%2B1%2FTeO14x9cVwjb6SIpVuiJKOoHQY3DQg%2BUjtLMBwGuS8aZJFqb1BQZ1qPsg4iSZ1K74gQwaOz8uah6u50wsrTSD8Ck4Vvik%2FgKxcoPb2NDjNiO4fpOeg%2By%2FdfRuA7cRR3P37q%2Fivcrj5Ht3MoLccwvk8Ug31y5xGkdrw5%2BZB4sKetdq5FKeg%2B%2FhNS%2Bl3tC4EbSeFUI4IKMy5ryuS4oQqx9hQplvd%2FslfNB920SbU8TKJxg4sCMF00P%2B%2B0ECDRttbCTgNnw26wB7lfUhjnjDC%2BxuHOBjqkARNTLQNmluJzh5pjacXFtlSIukC%2BQLSHhUyb3Ffx%2BeHRlq9p1QpLG%2B0xHZkHwZ5erBvKsFhrcbDQJRlijLGGeKKYNXxSheOa5PAaunam%2FcKAVUn1130QwMXP10RTPVLYK8tc8LG0Esndok%2B%2B%2BkQ3RsPLc85R4S6sSCGFjCnf2euIM7y%2BOCCPEq9Por4srH%2Fl0%2BkA0S62%2BNGd5Xq7fXbtY0%2BTGgM%2B&X-Amz-Signature=38ee9dcfc3b07bf0c678f9fa439bc79f46d9c93965686db0d1267833d6566a9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHESINJU%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T041106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQDDe4zcXe4C3n0Nr3ZgAQOtkcZw0xkDUDEBrK8sKHoQ3gIhAPXOtUBG4al0BIDn1o8PxbnquVnzHdTBdFXNG%2BOWmh3pKv8DCCQQABoMNjM3NDIzMTgzODA1Igy%2FvBz2ChjeAZ8fj0Yq3ANOtceM%2Bd41%2F5twYs5uvkMlJ%2FojGcDVsPieoMcjqupEGSM3vrz815A7yni%2FqdGAvlVa7j4jly4jvF2aZc%2FVXMGhgze%2FwUfZyTHhR5sEGof410pM17Hwuc5W0ZMRu70o4%2FZwBym1yj5XYqVNdsi%2FRVIe312W6kpYaRHbd%2Fwdv3QovTLcaN10mTeR9FBs6oaskgg3ch9olThOs%2BVVRQv8L%2BuqJzmmUwUp7gNg2%2Fc2CB%2BuxypmhPECql80DHJdlgMzudVifMt5pfYBpojexzTF6CptXaTvLODfVlTN7yp3FF5oFSeIsYu9GbSTKd5y0tV526bHOV0lch7qGyxamfK6kxrFY4Dchmhl1%2B%2Bjz9p71e%2B1%2FTeO14x9cVwjb6SIpVuiJKOoHQY3DQg%2BUjtLMBwGuS8aZJFqb1BQZ1qPsg4iSZ1K74gQwaOz8uah6u50wsrTSD8Ck4Vvik%2FgKxcoPb2NDjNiO4fpOeg%2By%2FdfRuA7cRR3P37q%2Fivcrj5Ht3MoLccwvk8Ug31y5xGkdrw5%2BZB4sKetdq5FKeg%2B%2FhNS%2Bl3tC4EbSeFUI4IKMy5ryuS4oQqx9hQplvd%2FslfNB920SbU8TKJxg4sCMF00P%2B%2B0ECDRttbCTgNnw26wB7lfUhjnjDC%2BxuHOBjqkARNTLQNmluJzh5pjacXFtlSIukC%2BQLSHhUyb3Ffx%2BeHRlq9p1QpLG%2B0xHZkHwZ5erBvKsFhrcbDQJRlijLGGeKKYNXxSheOa5PAaunam%2FcKAVUn1130QwMXP10RTPVLYK8tc8LG0Esndok%2B%2B%2BkQ3RsPLc85R4S6sSCGFjCnf2euIM7y%2BOCCPEq9Por4srH%2Fl0%2BkA0S62%2BNGd5Xq7fXbtY0%2BTGgM%2B&X-Amz-Signature=62205ba8ddfc40df4c5b3e44f3a6b8a2494df18d6f2b10b44baa8edb24f1b6e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

