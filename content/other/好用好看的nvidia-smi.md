---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
tags:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDT7HHA4%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIAf%2FgPjyESjQjQnEd8nNQ05lP2MXq4EFWm2jpzTUMTDQAiAz5Oo7xy8EnuyQ9q%2Be%2FeyhUWoOTkSnP%2B9KaG7VHD%2FoCSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmF3ZeDHj7yH2gBauKtwDWhh%2FBKbe5ILlZeQoN%2BshtOFnjGsRBZlPBflt0xFXh2kkcd83juwrafU8X7Y%2FnSLOjh1nR0R%2FK9zx4QwvbiEvi9KWZ%2FuAZvKtbPxq4dHgEP3cLbtMNzPFDMTKhPi8PtEbepdy0lAXK5LfjBKx5UaGCujbeKG221nDxK6XYpMHDay9LQgA1UuEsaOfwbzy2toN16MMkijPHmlZQbIv%2F1PjOWTlhFsBmqoo2AEeUn9KQ4tlzxFoIYasedl78gC1v9jb0rnw7Tk4ZaaM%2BdSYefuhkPeGsFVRWCp2dFmwJMX7zesDxZAgStjLbSymrYbTp3asC2jV%2FtkvHm%2FqhBY%2Bt3ya0v3FDMTfcaDOQuKIS272M4zV0lKDlZMU%2F3yCiPvLCUWCS8YfzQtcaBQsxslFazJO9Z5qo88BsT8fTH0s0o82pyH85WuLvV7T2PS1SlITyy7mVLTdP0A4rhNA7TrekDXKPGDDHITKnn3vrcF9ToGu65bZetwe1fvzocDfeEiKzyjOERF0FQNhb7eqTULjtDFRlw8VL%2BatYWRh7TTdomxyHj6PYfU7F4Fr70DiOsslNf%2BHHQvrIiysfylyipXkKV4xkxMbjIobC1E42t7biTx6VrWCh5Wyp6%2FWwXyB3CwwvfiQywY6pgGnph8Up6C%2FFz4IN7zxrsTbrl2VzGOiDnBX9kbL2tO8ak44XGbe3IuWYbpffQhkSske6UfGgCWpc8Cf7kHduimr2GXMDYCHnTLKuAjd1W98FebQsIjQ%2BGmpGaqPIZYaC89LX6BNP74sg2xgQu9QwZm1Snd7WHW2ftePS0e4qA9DrqVSRNpvVmKGA4aVU4dv6aTIYfZjgFz%2ByfTW8UtRkknWUk9WSVJm&X-Amz-Signature=c2ae743d1810aa9d0b2ca34fa67d0361506cd577320e609624d35ebc187584fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 安装

```python
pip install nvitop
```

---

## 查看gpu状态

```python
nvitop
```

> 查看更加详细的gpu内容

```python
nvitop -m full
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDT7HHA4%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIAf%2FgPjyESjQjQnEd8nNQ05lP2MXq4EFWm2jpzTUMTDQAiAz5Oo7xy8EnuyQ9q%2Be%2FeyhUWoOTkSnP%2B9KaG7VHD%2FoCSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmF3ZeDHj7yH2gBauKtwDWhh%2FBKbe5ILlZeQoN%2BshtOFnjGsRBZlPBflt0xFXh2kkcd83juwrafU8X7Y%2FnSLOjh1nR0R%2FK9zx4QwvbiEvi9KWZ%2FuAZvKtbPxq4dHgEP3cLbtMNzPFDMTKhPi8PtEbepdy0lAXK5LfjBKx5UaGCujbeKG221nDxK6XYpMHDay9LQgA1UuEsaOfwbzy2toN16MMkijPHmlZQbIv%2F1PjOWTlhFsBmqoo2AEeUn9KQ4tlzxFoIYasedl78gC1v9jb0rnw7Tk4ZaaM%2BdSYefuhkPeGsFVRWCp2dFmwJMX7zesDxZAgStjLbSymrYbTp3asC2jV%2FtkvHm%2FqhBY%2Bt3ya0v3FDMTfcaDOQuKIS272M4zV0lKDlZMU%2F3yCiPvLCUWCS8YfzQtcaBQsxslFazJO9Z5qo88BsT8fTH0s0o82pyH85WuLvV7T2PS1SlITyy7mVLTdP0A4rhNA7TrekDXKPGDDHITKnn3vrcF9ToGu65bZetwe1fvzocDfeEiKzyjOERF0FQNhb7eqTULjtDFRlw8VL%2BatYWRh7TTdomxyHj6PYfU7F4Fr70DiOsslNf%2BHHQvrIiysfylyipXkKV4xkxMbjIobC1E42t7biTx6VrWCh5Wyp6%2FWwXyB3CwwvfiQywY6pgGnph8Up6C%2FFz4IN7zxrsTbrl2VzGOiDnBX9kbL2tO8ak44XGbe3IuWYbpffQhkSske6UfGgCWpc8Cf7kHduimr2GXMDYCHnTLKuAjd1W98FebQsIjQ%2BGmpGaqPIZYaC89LX6BNP74sg2xgQu9QwZm1Snd7WHW2ftePS0e4qA9DrqVSRNpvVmKGA4aVU4dv6aTIYfZjgFz%2ByfTW8UtRkknWUk9WSVJm&X-Amz-Signature=29a16d2ae6747826a3b7bf70383a737f32b4c45c1702dd6749c92ebb339c6ea4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









