---
title: 基于Easy DataSet创建自定义数据集
date: '2025-03-27T03:06:00.000Z'
lastmod: '2025-03-27T05:53:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 前几天看视频发现一个开源的构建数据集项目，打算复现玩一下。这里记录全流程。

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FJO4N4O%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCFRhs1WtE45UkUWL%2F3nVsV8Ic5w98d%2FKuGKw0bRY9fBwIgaQAuQf%2FBaLuCl5HpMJuHcppUW0mTNCje0gjitDH5Y4cqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIjKGOhJ294sEmg0RircA%2BU8ctbXuQ%2FIsBa%2FIGjmWBzz%2Bjn%2B9nQfNihIrvzu33Q6l6HKLcmkXSSsFVhrefHCIgR4cojVFzdXJNPsVHAKk1RbuUeegU86ZfSlB%2BYFOCskchs3WoZS0LYq18D2KvDeoatzXkzn6Z%2B%2BD8vAiajJhtwmEEFg0Uqdd63sYZL%2BSZaxmCjpitf9KBTkOhtcJB%2Fzfv84PwQ5XKlOXf0LsH6jZvgW3y0z5PwFyIBkY8nBY9A%2F4QDkJvRYMiNCyCiyHbZ9vSq6uFRmoE%2FiTODry9%2FcmyZWd9uwDvwOM%2FjMSC%2BJwgDp6TprsvW%2BsdTmQY3L1IYUESbKzU85RlIrDPQ2wvxzsKN62w3A6dCs7X4xlhuOLea7i2UvS83LKGR0kOxmZIARRoNPyhW%2Bo1B30hVLIEj4BtCVQLbnvGNafHWEYXpV57kChhG7lwJEOITKjRcvmcmOMCaWcawx38G9m11EL%2BytcFx3E5f7PEqWyoBmYHqv3ySOziTb%2BhSsZw6GftnXA%2BgcBB%2FDoOcG%2Boi13Rxx96p8yMXDtpn3WLXLOTWM44RIXyVa3xkVmLLy%2BiprGObhcHsGng7M6GLMz9Uz5ZxrMu2NM6iHXL8dlMVycMDcG3eQS%2F7lSynbRPr8przKRzh7MKyvy8sGOqUBeXe208A4T5US6cjo%2BDCeuwFB6auJ0JhytliKwA%2B70W6vznrbU%2FDpgfTOAOP%2BdVB00BtD3QmmJe%2FMUuskZ8X4JMyKWDAOlXTBCcp7zR3UJOC%2F1hI3VZSQRNuSBFyJ7Z9QTA%2FpA%2FHDlXMPfjF1ZV%2FhXEyLcJx9bJchZKPSwm9KWYDCM%2BvvaqK0V%2FveqULE%2B9fDye3aN43EFqPEVr8kzflybBdwQFkO&X-Amz-Signature=5d634f183e9f10224a0108139aa86acc7174379bd1b1529a77112d2545b1d42b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 环境安装

本人使用Ubuntu系统。首先安装node.js以及npm。

1. 使用nvm，安装nodejs以及npm
1. 安装pnpm
1. 检查安装是否正确
---

# Easy DataSet平台安装

1. 使用github下载源代码
1. 安装代码所需依赖包
> 使用pnpm的特点:

---

# Easy DataSet启动

1. 基于代码构建项目
1. 启动应用程序
---

# 怎么使用Easy DataSet

1. 新建项目
1. 配置大模型
1. 上传数据
1. 基于分割的文本，构建问题
1. 构建数据集
1. 导出数据集
---

> References

