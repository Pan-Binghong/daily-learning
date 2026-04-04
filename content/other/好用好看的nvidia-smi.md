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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XASCTP4T%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKwpHMlAhWw42vSymErM2ZwOzRwC1euxMpPB7L%2F%2BPSzQIgW6rbIuwLCF9YJgf%2FQ%2F5JNgrKU7JXUsWJ0j33dU%2FySboqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMtw2bvQ6V%2FaGnvyPSrcA2u4m3w0DkXpomdfKzfvdrCCekgO00aM%2Bzkl9ZwyyPT2wel%2BXIYMbcamkcrA1Je8nAGlE4ax9vL9M%2FIi36QvWSQOPEpy0u7TYsPNxLoR9faoJxAW5HkxoVmHFCnwNUZWaTkyiCvA0CsLMHXv3iLeieScnYuEnM0msc%2Fnwa7ZfsHLGTc%2BLFQ%2B3kjVOjfMDT3CV1p8cNF7COdBhrsGxRSJuM7D8UdB1QtTIugHZcNheClJsRrps3ONrTKpdCYwmaoUV0bgjOHviWDGJzsRtpYOeGqA8SOehJE%2FhgR%2F74lshqFXNzib169zelr6PLs6igkyejazl%2FwluJ%2FGBvHrDV2IK165Fd%2FVAMzk2KrvIXE7joSduvSzQsbeAgzUtyCBcvwNp7y%2Fl%2Fu4m0ZrqW99cRUuBkPRH9iUtsy%2BvaPJEUsvthYyRcjXMslqI3S0%2BH8uj3ta4M51W3MLdYVd2ahbihMXOd4dbXA6e0IWIh%2FRoS82VbXlHFXsQKURuB5XApQQjwNJwKxeIazYfid8lmcE7%2FpuFCm4W2X0OqXPHWLNDmD4eZ9mqCdm2uNHzCEMK4o%2FjN1Pe4Xk30%2Fi8P0rgmzrtcSdSfz6geW2OhB%2FJFWVsaSgFHEi%2FL9O21Fvl%2FmRHGUdMK%2Fmwc4GOqUB80vOI8cl54iTFMu8hHwo0p1kQXKBIaRoMsmlEblCS1zRNuJxyJ7A1L6dbeLT8vLmGpjXCLMe5LGdLCp3RgaPROx6suGH%2BnQg9AyBE9uS0GcJr8Rhd7rCzDDzuPuGZmt5BL%2Bt3KSNgAfNJnCpB%2BnWMjutgHc%2BoRx5XeF3m9%2BTqAWt3eGLeqFqHmLfefQnqO0JXUD%2B5kz%2FyK%2FmRbeR19FQCO8I0%2B7q&X-Amz-Signature=083224b9a05bfc7ad28f4759d0ef9e0e3605ba3cb006fb4a6c9c5d6c28a55066&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XASCTP4T%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKwpHMlAhWw42vSymErM2ZwOzRwC1euxMpPB7L%2F%2BPSzQIgW6rbIuwLCF9YJgf%2FQ%2F5JNgrKU7JXUsWJ0j33dU%2FySboqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMtw2bvQ6V%2FaGnvyPSrcA2u4m3w0DkXpomdfKzfvdrCCekgO00aM%2Bzkl9ZwyyPT2wel%2BXIYMbcamkcrA1Je8nAGlE4ax9vL9M%2FIi36QvWSQOPEpy0u7TYsPNxLoR9faoJxAW5HkxoVmHFCnwNUZWaTkyiCvA0CsLMHXv3iLeieScnYuEnM0msc%2Fnwa7ZfsHLGTc%2BLFQ%2B3kjVOjfMDT3CV1p8cNF7COdBhrsGxRSJuM7D8UdB1QtTIugHZcNheClJsRrps3ONrTKpdCYwmaoUV0bgjOHviWDGJzsRtpYOeGqA8SOehJE%2FhgR%2F74lshqFXNzib169zelr6PLs6igkyejazl%2FwluJ%2FGBvHrDV2IK165Fd%2FVAMzk2KrvIXE7joSduvSzQsbeAgzUtyCBcvwNp7y%2Fl%2Fu4m0ZrqW99cRUuBkPRH9iUtsy%2BvaPJEUsvthYyRcjXMslqI3S0%2BH8uj3ta4M51W3MLdYVd2ahbihMXOd4dbXA6e0IWIh%2FRoS82VbXlHFXsQKURuB5XApQQjwNJwKxeIazYfid8lmcE7%2FpuFCm4W2X0OqXPHWLNDmD4eZ9mqCdm2uNHzCEMK4o%2FjN1Pe4Xk30%2Fi8P0rgmzrtcSdSfz6geW2OhB%2FJFWVsaSgFHEi%2FL9O21Fvl%2FmRHGUdMK%2Fmwc4GOqUB80vOI8cl54iTFMu8hHwo0p1kQXKBIaRoMsmlEblCS1zRNuJxyJ7A1L6dbeLT8vLmGpjXCLMe5LGdLCp3RgaPROx6suGH%2BnQg9AyBE9uS0GcJr8Rhd7rCzDDzuPuGZmt5BL%2Bt3KSNgAfNJnCpB%2BnWMjutgHc%2BoRx5XeF3m9%2BTqAWt3eGLeqFqHmLfefQnqO0JXUD%2B5kz%2FyK%2FmRbeR19FQCO8I0%2B7q&X-Amz-Signature=24044ad9e46e9577b0a277d7ac7a0e289ad545cf66327357ca7d3788f3c12ae8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









