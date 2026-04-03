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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUHCPB7D%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB13CCyRweR2FSpIclYaR0pJs%2BHOjvZl%2BV%2FfCTjh7BiqAiEA%2FdAK3FZA21AyY07DYrzjTv48GqlhUzGYgZstyrvF6LAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDLqn0FBFW24z9aK2SCrcAw56YMCvJ8R63aaTmwfJIyF%2Fmkd4Zf1c0CmjBPUTfKLofhbs6k5rkiykUGuTP%2F2j7V3T4JAoMgEgzyNZOtDSIZAn5mRNhIJf%2FkZ9WGk44D6XZCzV3Y%2BqfxhKKtBQh2u1QOsjNu8WlKkqOM4ueBNKHfsyRbzNVkhgA7BZzqPZLNZ0eTY4kduNv9vRfSyrnOlE2iAhuP2gwdkOOr4v7iSjvdnaU1MFj2UFNOsOnW5bCGFhAzqoMi7bh68Na8gOZp%2BO%2B%2BbrJYL4%2FJXQpHBm2uH7HwXVR5IhV5y5t2B1rUGRNQR9hFnkF%2BPwLjagAX0FQDpLz%2FDQomWnTzHqvdbY5T8W1ByTPLPY1uywn5mTTyHnnC7ueuiRLq8aTfe9hH5TxOtZPTCana8zznpuZUdhb0AV5UB8r8oB1YKxdpl4Wha8ZcVRn7xHAa%2BkhWINPYhhWmYOmRDhD2Hkgsf962dCd8Eq5uH9qP6KHGR8fWxWCCd8UfbFN6cALFq4R3KyaxdcpoDamVYbGJ0K6PVBer6evEvg%2FPBpJSMb6%2BUJYjktAxWb3DlLUo9T3SJLHVSUwRZ2KHyxncxljQipHhd7KsvBdlnzFFnWB5aDoK0vSK7xQ1Dx%2FzbGX8drV6saFUUXC77eMOCtvc4GOqUBwhB9zEAqRtTGZYHdhWimRL2nxbYtnblVBH%2FeLe4Oaq89jKj3U4Hgm273g8fm4GHRUYPYfQyX9uzhrn5lO3pog19f%2Fg5JvAU9YZTnh3jhInBp4mt7xKelncLzqxtGzkqWdBpypbCP2PfOPpupK5Gexs7DbosLgYbKmR%2BcVPho9FlnaZtZaeaTq9%2FpDKZdb%2FlA63nm4uSmbLwUvv16XDQXEE3B1STS&X-Amz-Signature=c393bc26746f3ed1f4a463057089cbf33857e45d97577c1d031b6ac1f0755279&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUHCPB7D%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB13CCyRweR2FSpIclYaR0pJs%2BHOjvZl%2BV%2FfCTjh7BiqAiEA%2FdAK3FZA21AyY07DYrzjTv48GqlhUzGYgZstyrvF6LAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDLqn0FBFW24z9aK2SCrcAw56YMCvJ8R63aaTmwfJIyF%2Fmkd4Zf1c0CmjBPUTfKLofhbs6k5rkiykUGuTP%2F2j7V3T4JAoMgEgzyNZOtDSIZAn5mRNhIJf%2FkZ9WGk44D6XZCzV3Y%2BqfxhKKtBQh2u1QOsjNu8WlKkqOM4ueBNKHfsyRbzNVkhgA7BZzqPZLNZ0eTY4kduNv9vRfSyrnOlE2iAhuP2gwdkOOr4v7iSjvdnaU1MFj2UFNOsOnW5bCGFhAzqoMi7bh68Na8gOZp%2BO%2B%2BbrJYL4%2FJXQpHBm2uH7HwXVR5IhV5y5t2B1rUGRNQR9hFnkF%2BPwLjagAX0FQDpLz%2FDQomWnTzHqvdbY5T8W1ByTPLPY1uywn5mTTyHnnC7ueuiRLq8aTfe9hH5TxOtZPTCana8zznpuZUdhb0AV5UB8r8oB1YKxdpl4Wha8ZcVRn7xHAa%2BkhWINPYhhWmYOmRDhD2Hkgsf962dCd8Eq5uH9qP6KHGR8fWxWCCd8UfbFN6cALFq4R3KyaxdcpoDamVYbGJ0K6PVBer6evEvg%2FPBpJSMb6%2BUJYjktAxWb3DlLUo9T3SJLHVSUwRZ2KHyxncxljQipHhd7KsvBdlnzFFnWB5aDoK0vSK7xQ1Dx%2FzbGX8drV6saFUUXC77eMOCtvc4GOqUBwhB9zEAqRtTGZYHdhWimRL2nxbYtnblVBH%2FeLe4Oaq89jKj3U4Hgm273g8fm4GHRUYPYfQyX9uzhrn5lO3pog19f%2Fg5JvAU9YZTnh3jhInBp4mt7xKelncLzqxtGzkqWdBpypbCP2PfOPpupK5Gexs7DbosLgYbKmR%2BcVPho9FlnaZtZaeaTq9%2FpDKZdb%2FlA63nm4uSmbLwUvv16XDQXEE3B1STS&X-Amz-Signature=35234dab5558633fb32d92c831dd985de33147462eca3e8863a0253c83248eb6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUHCPB7D%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB13CCyRweR2FSpIclYaR0pJs%2BHOjvZl%2BV%2FfCTjh7BiqAiEA%2FdAK3FZA21AyY07DYrzjTv48GqlhUzGYgZstyrvF6LAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDLqn0FBFW24z9aK2SCrcAw56YMCvJ8R63aaTmwfJIyF%2Fmkd4Zf1c0CmjBPUTfKLofhbs6k5rkiykUGuTP%2F2j7V3T4JAoMgEgzyNZOtDSIZAn5mRNhIJf%2FkZ9WGk44D6XZCzV3Y%2BqfxhKKtBQh2u1QOsjNu8WlKkqOM4ueBNKHfsyRbzNVkhgA7BZzqPZLNZ0eTY4kduNv9vRfSyrnOlE2iAhuP2gwdkOOr4v7iSjvdnaU1MFj2UFNOsOnW5bCGFhAzqoMi7bh68Na8gOZp%2BO%2B%2BbrJYL4%2FJXQpHBm2uH7HwXVR5IhV5y5t2B1rUGRNQR9hFnkF%2BPwLjagAX0FQDpLz%2FDQomWnTzHqvdbY5T8W1ByTPLPY1uywn5mTTyHnnC7ueuiRLq8aTfe9hH5TxOtZPTCana8zznpuZUdhb0AV5UB8r8oB1YKxdpl4Wha8ZcVRn7xHAa%2BkhWINPYhhWmYOmRDhD2Hkgsf962dCd8Eq5uH9qP6KHGR8fWxWCCd8UfbFN6cALFq4R3KyaxdcpoDamVYbGJ0K6PVBer6evEvg%2FPBpJSMb6%2BUJYjktAxWb3DlLUo9T3SJLHVSUwRZ2KHyxncxljQipHhd7KsvBdlnzFFnWB5aDoK0vSK7xQ1Dx%2FzbGX8drV6saFUUXC77eMOCtvc4GOqUBwhB9zEAqRtTGZYHdhWimRL2nxbYtnblVBH%2FeLe4Oaq89jKj3U4Hgm273g8fm4GHRUYPYfQyX9uzhrn5lO3pog19f%2Fg5JvAU9YZTnh3jhInBp4mt7xKelncLzqxtGzkqWdBpypbCP2PfOPpupK5Gexs7DbosLgYbKmR%2BcVPho9FlnaZtZaeaTq9%2FpDKZdb%2FlA63nm4uSmbLwUvv16XDQXEE3B1STS&X-Amz-Signature=7110164e11cb6412aca1f71bcdae3d9b4d785d609a4773581a37369cee89be29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

