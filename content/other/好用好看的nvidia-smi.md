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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IWF7IGW%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQC9b7SVK45kU3KXzuP4nH1PhjWGdnOxdVu8QK9DqH5yzwIgVXdXZrxUH8TX7%2BtVzcg3UpryL0C%2B7BJMVaHdCniv6pUq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDPGg14DgfXSD%2F2QWRSrcA%2FoZdWeOIvEqQiD%2B3A2mZLNeW8WcwKfYYIzjo3urAGuLxQLg0NB4pf0gnOuUktVqGAriD%2F95tCoDeJ%2BFKklbdFBMXHSiVYL2CgsDzdU3dbqX5GiQBC47CU6DqYAIyHdci4SdFDTnMlmuOfj11s3MtzAzQp4J4OJ0dNZ1GF%2BtN%2FbhctuDxMJxHBgHs%2FQqENYZX%2Bb%2BxXsimJ1hM22pT8tRMDUwpO%2B6Z6dwEZg46CRnF5vdCrq3dqJHrXepL4mMFMxPtviG2lqZ3YWPZmpIFOiW8ShuFSzONUquynTf6sAMge1hMDyJZT8j1psEqQkpDWf2JyyKEx1jJ5%2Bm1ngjECY0XqZroVBXA1LjIwTs1p4%2FyEXi6O1mmEZzJZpMoOCmQvqBopDMtgtDQZdgZjpUYqrSO8IP5yigNhamjxx1EqrDFnTXDv1bhY0R5M0n%2BuzyKPc6k8D4%2FItbUBrmUoTyFTXZoWDb6fFeX5%2BzZY5nDzWviYumUXXAZnjj%2BXCYXgbmXcjTTkq7NE79FtEz9M2PsqCCcu%2FzAkLs5sYu8KOJNEmgm%2F10mPniFQ2H9ymyq1s615onudnhrB4mMmVYHc3jb9iHHAEvu5erR7D467BgUTHC4uUaaNs4bG67TAxmHDBIMMCessoGOqUBg%2BjqkOMV2rhMg7vz%2FE96xp9Vm0OjX6Tn0wPy%2BzOeowPh5RyEmUxBiysYyerE5l3EK5WQeQxipU2AmSZhMqt2KsZA%2FH7H6%2FGm%2F4hwuO3%2FG8zINuD7U1B2442dBx6c7kOP8lFBqSz6MP99JhzuAFqrtgQOVNd0j9XP3hEHUmhdLK3c5HpmB%2BYNBfOQTJj4lIrGiHFNjU8HSoevmPfdBct%2Fy779vvA6&X-Amz-Signature=6b0382aa8575787dcbd6fa3696172abdefe6c830796c1788448effba0bbb21e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IWF7IGW%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQC9b7SVK45kU3KXzuP4nH1PhjWGdnOxdVu8QK9DqH5yzwIgVXdXZrxUH8TX7%2BtVzcg3UpryL0C%2B7BJMVaHdCniv6pUq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDPGg14DgfXSD%2F2QWRSrcA%2FoZdWeOIvEqQiD%2B3A2mZLNeW8WcwKfYYIzjo3urAGuLxQLg0NB4pf0gnOuUktVqGAriD%2F95tCoDeJ%2BFKklbdFBMXHSiVYL2CgsDzdU3dbqX5GiQBC47CU6DqYAIyHdci4SdFDTnMlmuOfj11s3MtzAzQp4J4OJ0dNZ1GF%2BtN%2FbhctuDxMJxHBgHs%2FQqENYZX%2Bb%2BxXsimJ1hM22pT8tRMDUwpO%2B6Z6dwEZg46CRnF5vdCrq3dqJHrXepL4mMFMxPtviG2lqZ3YWPZmpIFOiW8ShuFSzONUquynTf6sAMge1hMDyJZT8j1psEqQkpDWf2JyyKEx1jJ5%2Bm1ngjECY0XqZroVBXA1LjIwTs1p4%2FyEXi6O1mmEZzJZpMoOCmQvqBopDMtgtDQZdgZjpUYqrSO8IP5yigNhamjxx1EqrDFnTXDv1bhY0R5M0n%2BuzyKPc6k8D4%2FItbUBrmUoTyFTXZoWDb6fFeX5%2BzZY5nDzWviYumUXXAZnjj%2BXCYXgbmXcjTTkq7NE79FtEz9M2PsqCCcu%2FzAkLs5sYu8KOJNEmgm%2F10mPniFQ2H9ymyq1s615onudnhrB4mMmVYHc3jb9iHHAEvu5erR7D467BgUTHC4uUaaNs4bG67TAxmHDBIMMCessoGOqUBg%2BjqkOMV2rhMg7vz%2FE96xp9Vm0OjX6Tn0wPy%2BzOeowPh5RyEmUxBiysYyerE5l3EK5WQeQxipU2AmSZhMqt2KsZA%2FH7H6%2FGm%2F4hwuO3%2FG8zINuD7U1B2442dBx6c7kOP8lFBqSz6MP99JhzuAFqrtgQOVNd0j9XP3hEHUmhdLK3c5HpmB%2BYNBfOQTJj4lIrGiHFNjU8HSoevmPfdBct%2Fy779vvA6&X-Amz-Signature=cbdd616e3115db85c55c1dda703371525c8a5b299fef4f731ce0c6d6361c3447&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









