---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2S6XO2P%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFrVYBpkHhxEm1YXAxAB6BtBGrFB7dTAiUMmzCFYyN%2FzAiA0QGJ39W7mxEBGEMK1SzjdCnXgdFIQdwC5MFWd2kn4FSr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMgu7PKrlluE43nslSKtwD%2BHu9NFAhRAJJAthz9R5msGRsVZ6CFbmEAErep%2FI9QvJD%2FeQhwqDEtnXDgI4GK1WkXRHnvrIcK7NM%2FuI3oMvpMbR7b1e7Gg5W5S%2FtbH%2BPa4uijEtyFht%2FlrdyfD7D6zxyri8oWZgohRWRvav2Q220Q16KbEQ6DTVdgLbXyihk1aepcoApTDPdEv7QFCMxvtBR8GDJMDzJyzAaVX1kzbSbQGaKF5K%2Fw2yRpVfDXP%2BVJi6fnPJEqZCwfq3UbktBAFjdxKVZOErT4iKpm9jbBtrza7eAo3iiH8H27%2B0kY4hvMU9uisnW%2Ft5iF7rippHt99gWwvPJVEVHBEujWoFIsj3UkdmJqIco7bZj6fw51CsG2CrEYNHsiqV2cKw7VFbcNBEHzDoL%2B0ywE7vqCvhN3ZLAK4ZnHHe4wLzGax00OwSq%2BorLdce0PH7%2FvPSj%2FFQ6vGP0oHqquyiKzlUrSmoi1rR94YVx0hsre7UlMNqHyhwIHNWuFzF9f4mw9eurvgejBt%2F8dxc8TOJ87s%2BReH1JNkJFezomNKvglWMO%2BA%2BneoPn6lhq018qfEHn7gAT8TkqtIs3mukI%2FhMFMHcPCUW9NxJboYoiZ5oUiZekoVH3kD2C2nLczHFLpGnlAL1numgwxIWEzQY6pgFh8Ih3n%2Fxu2wbMHnxo1XjMzzZGZ9FKOr38bDOlyzK%2FOBYAGm8tJToQl1r3w3wbmcBo1x7t%2B0yi7%2FVVxmijeKs8QAf0gFFnzWAREmLyQXQ24iekPCGOli3MKmCBr9sea8VnG95qAIQIC%2FyefSFqo6QbMoUPmUWg8bZOMoboD4FlD6ivGb4lOqbJKy8TLw862lt0DxJAhakaaVu9az9KjUR2AjoVgz8G&X-Amz-Signature=9a489cb277ce4632cd0313a2fc0cbb322604ead2f90791833ebb4599d3bc7b24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2S6XO2P%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFrVYBpkHhxEm1YXAxAB6BtBGrFB7dTAiUMmzCFYyN%2FzAiA0QGJ39W7mxEBGEMK1SzjdCnXgdFIQdwC5MFWd2kn4FSr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMgu7PKrlluE43nslSKtwD%2BHu9NFAhRAJJAthz9R5msGRsVZ6CFbmEAErep%2FI9QvJD%2FeQhwqDEtnXDgI4GK1WkXRHnvrIcK7NM%2FuI3oMvpMbR7b1e7Gg5W5S%2FtbH%2BPa4uijEtyFht%2FlrdyfD7D6zxyri8oWZgohRWRvav2Q220Q16KbEQ6DTVdgLbXyihk1aepcoApTDPdEv7QFCMxvtBR8GDJMDzJyzAaVX1kzbSbQGaKF5K%2Fw2yRpVfDXP%2BVJi6fnPJEqZCwfq3UbktBAFjdxKVZOErT4iKpm9jbBtrza7eAo3iiH8H27%2B0kY4hvMU9uisnW%2Ft5iF7rippHt99gWwvPJVEVHBEujWoFIsj3UkdmJqIco7bZj6fw51CsG2CrEYNHsiqV2cKw7VFbcNBEHzDoL%2B0ywE7vqCvhN3ZLAK4ZnHHe4wLzGax00OwSq%2BorLdce0PH7%2FvPSj%2FFQ6vGP0oHqquyiKzlUrSmoi1rR94YVx0hsre7UlMNqHyhwIHNWuFzF9f4mw9eurvgejBt%2F8dxc8TOJ87s%2BReH1JNkJFezomNKvglWMO%2BA%2BneoPn6lhq018qfEHn7gAT8TkqtIs3mukI%2FhMFMHcPCUW9NxJboYoiZ5oUiZekoVH3kD2C2nLczHFLpGnlAL1numgwxIWEzQY6pgFh8Ih3n%2Fxu2wbMHnxo1XjMzzZGZ9FKOr38bDOlyzK%2FOBYAGm8tJToQl1r3w3wbmcBo1x7t%2B0yi7%2FVVxmijeKs8QAf0gFFnzWAREmLyQXQ24iekPCGOli3MKmCBr9sea8VnG95qAIQIC%2FyefSFqo6QbMoUPmUWg8bZOMoboD4FlD6ivGb4lOqbJKy8TLw862lt0DxJAhakaaVu9az9KjUR2AjoVgz8G&X-Amz-Signature=933d69b9ef532e1cbaad519242214f4efb0371aeff8eb9e8916010f9e6207a9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



