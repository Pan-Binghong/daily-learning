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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOGSROXQ%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA7PkqvqxAxMUX%2FXQQhRlojMBwAzBl396oSAzTaEMq%2BFAiEA%2BoQLdM2ziSubAb%2FIFSgv%2FZcrJDwLHSL8hap4fVFw%2BKIqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCn3Dgp%2B%2FzUa9E%2BfSCrcAyPL8kf1DF6lyLY%2Bb6dU%2FxauPWM0uo%2FO%2BuNdbuivrFlbFMWlTcX1D4uZopUSlZD9HgGtAj5%2BLJF7Z0J%2FHAIiAucax2f%2FkIaHEYG3T3Z6CRBy3yuCSmW01XwQj0P4%2B3AW95hcscBsMhjdetwc5MuzkmNls%2BI8aQ2HWZzm2BFkSbllRmlIT42Le8Bo1Ac3lS0D2BXdwg4cW8GYhMylduXrmrTA5ZiIXRJOaQ5qzrgAtjcH63FsODSdkHoVowaGnimju0g5FKZ%2FRLuGDQG4VTRxV74G%2FpvS56mIb9LJ1uS0VnPUQSVzs7YWdjThOYmSZcyTqUmpBkACq4OqmtAkZtJBhR%2FVelwaiQUBjUjEaHcv7uTWoCibc9eQ6ChXQe6HQni8fwgBChM%2BAbDJDlFK1olGqaTLhPgWA8v3lTVDt0oEK%2FRUnY3vVcT7SJUHuTbgah7AZEUfnWI2nCeMSBXxGZQH33Blvfw2h5lo7CWpBsjjmqbaYxl1GtTcM1zwYFduAAi%2FJaxxVfpKFsXiR%2F4FrdkQHFlqjTc9aNiNv4qTGBvXzvlVG9%2B2kPR0w3JST4aityZGh0hR3DyMzp0qKEU%2Ba43x2Pz%2BhjZC4%2BM%2BtA516FUQxlvo15A3ihgKE9vWukM9MMaS%2B8sGOqUBWx8uV1M07z%2BmH7fwIYOCSd6Z2IBV0FHdPZ5oMlvTTYod7%2BNNGlKYuMV57QwqzoLQ04hQ3U6JuP8OvFSPTzYoXEoODRFFThGidgZucKVcdhiYJBOVpbRDyo4cOleZMXXQKPZliKIJBvKlWDR3Wwk1FMoQvxDPLvj5rbA96%2BxONk0ZclPm7aatV0vVnc%2FgQdofptxUx6%2B3jZ%2FAWfHBakPEGPw48OcV&X-Amz-Signature=3ec22b9e1709eaf0c59104a4bd8913d6a0c7901af6c01126837753f8c4715e23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOGSROXQ%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA7PkqvqxAxMUX%2FXQQhRlojMBwAzBl396oSAzTaEMq%2BFAiEA%2BoQLdM2ziSubAb%2FIFSgv%2FZcrJDwLHSL8hap4fVFw%2BKIqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCn3Dgp%2B%2FzUa9E%2BfSCrcAyPL8kf1DF6lyLY%2Bb6dU%2FxauPWM0uo%2FO%2BuNdbuivrFlbFMWlTcX1D4uZopUSlZD9HgGtAj5%2BLJF7Z0J%2FHAIiAucax2f%2FkIaHEYG3T3Z6CRBy3yuCSmW01XwQj0P4%2B3AW95hcscBsMhjdetwc5MuzkmNls%2BI8aQ2HWZzm2BFkSbllRmlIT42Le8Bo1Ac3lS0D2BXdwg4cW8GYhMylduXrmrTA5ZiIXRJOaQ5qzrgAtjcH63FsODSdkHoVowaGnimju0g5FKZ%2FRLuGDQG4VTRxV74G%2FpvS56mIb9LJ1uS0VnPUQSVzs7YWdjThOYmSZcyTqUmpBkACq4OqmtAkZtJBhR%2FVelwaiQUBjUjEaHcv7uTWoCibc9eQ6ChXQe6HQni8fwgBChM%2BAbDJDlFK1olGqaTLhPgWA8v3lTVDt0oEK%2FRUnY3vVcT7SJUHuTbgah7AZEUfnWI2nCeMSBXxGZQH33Blvfw2h5lo7CWpBsjjmqbaYxl1GtTcM1zwYFduAAi%2FJaxxVfpKFsXiR%2F4FrdkQHFlqjTc9aNiNv4qTGBvXzvlVG9%2B2kPR0w3JST4aityZGh0hR3DyMzp0qKEU%2Ba43x2Pz%2BhjZC4%2BM%2BtA516FUQxlvo15A3ihgKE9vWukM9MMaS%2B8sGOqUBWx8uV1M07z%2BmH7fwIYOCSd6Z2IBV0FHdPZ5oMlvTTYod7%2BNNGlKYuMV57QwqzoLQ04hQ3U6JuP8OvFSPTzYoXEoODRFFThGidgZucKVcdhiYJBOVpbRDyo4cOleZMXXQKPZliKIJBvKlWDR3Wwk1FMoQvxDPLvj5rbA96%2BxONk0ZclPm7aatV0vVnc%2FgQdofptxUx6%2B3jZ%2FAWfHBakPEGPw48OcV&X-Amz-Signature=049f838bf92d550c62f62beea268f58516fbf740c537941656b3ae1356bfc449&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









