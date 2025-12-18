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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSPO6YFD%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICfz6PpGn760qFUHj8dWFht2H1rzBDlVfiHy%2FPIKtKjWAiACI1kJYDlEbpqUtVI%2F%2Farvyxnm0vXMVqxINDe7LH%2FQDSqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUh786heWd5DRNFGLKtwDEXsUmCohMRW9S%2BMRtMAmaKIbavgBX5RDbAageRkQCQhhO5hRHvCQWl0j4POQ5YYH%2FXpn9l8abVrxNjce3Bmgrb3MISprlJ7yOFGWkLCqU23aMm0yg7yfUKWk%2FPFXknaUfjq9MvVIfwxBMvpu9Sd6oQflmOXtb%2BcD4m1%2BbfNmL5OJTWJiiAKYs05qZjiCNA6Xa867%2FmPU9sCVQVs9HpggvT4kLB%2FE0kAjfba%2BAOr%2FTfyruQthQrY%2Btvhjom1gyNc%2BYGBL3VtnEE13xhh8YVd2Hszn%2BBNOQiRZi2G0bPnMmvu7uX6gQXdBCtdWjcCD9RlzNFZhEB8dhID4aQ4wAQ10SHqda7DkqKClk4eFEZO2pcj%2FF56ul6iJkH6Rtu%2BdXkoQpYcH2wp23iDfEGuPnYEW8XCllFNbn%2Ba6WwgxkgfW0qlsZbTXptpU8RlZvjdowvJAfJpnSFV5Dmj0spD7Za6H82cw97uNuWorrCEDA%2B7bDpCeLzJcJTeCRJCt%2BG8y%2BdopQe07fhu5lTdzK0n7ASUAwreqQe6%2B3n3yU%2BWEGhr1xnwtkuQvcFfJS4JUX5T4qSkBbxViw30l1GAONhe5uGhz0Y%2BaT%2BFlap%2F5F4%2Bbna370wk723inHIa7PlFQ2GMwocmNygY6pgGzJ%2BWpIK877flu4e2V5pEU2JuJrohwcBMBY8vUnP9O3C2rez7kLg7CVwz9WeOsQA15hNikNaI%2F%2BjtbVbrNL2Wp%2FpVtLp5O0B8GkhZlfqRTpsfE9fYKMxg0qTzMY18znyFBTc7vTEKYTVxgdX2ZHwHBtri9KS%2BupCsDE7Qk5aW0ZsYFkL8JWYE9kP478tQuxG43QddkXkWpwI1AU5013xaswyUgVCmj&X-Amz-Signature=aa25ea40f481c1494c7760ded3370ce29e07650b453ca18bc42f70005f60c8eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSPO6YFD%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICfz6PpGn760qFUHj8dWFht2H1rzBDlVfiHy%2FPIKtKjWAiACI1kJYDlEbpqUtVI%2F%2Farvyxnm0vXMVqxINDe7LH%2FQDSqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUh786heWd5DRNFGLKtwDEXsUmCohMRW9S%2BMRtMAmaKIbavgBX5RDbAageRkQCQhhO5hRHvCQWl0j4POQ5YYH%2FXpn9l8abVrxNjce3Bmgrb3MISprlJ7yOFGWkLCqU23aMm0yg7yfUKWk%2FPFXknaUfjq9MvVIfwxBMvpu9Sd6oQflmOXtb%2BcD4m1%2BbfNmL5OJTWJiiAKYs05qZjiCNA6Xa867%2FmPU9sCVQVs9HpggvT4kLB%2FE0kAjfba%2BAOr%2FTfyruQthQrY%2Btvhjom1gyNc%2BYGBL3VtnEE13xhh8YVd2Hszn%2BBNOQiRZi2G0bPnMmvu7uX6gQXdBCtdWjcCD9RlzNFZhEB8dhID4aQ4wAQ10SHqda7DkqKClk4eFEZO2pcj%2FF56ul6iJkH6Rtu%2BdXkoQpYcH2wp23iDfEGuPnYEW8XCllFNbn%2Ba6WwgxkgfW0qlsZbTXptpU8RlZvjdowvJAfJpnSFV5Dmj0spD7Za6H82cw97uNuWorrCEDA%2B7bDpCeLzJcJTeCRJCt%2BG8y%2BdopQe07fhu5lTdzK0n7ASUAwreqQe6%2B3n3yU%2BWEGhr1xnwtkuQvcFfJS4JUX5T4qSkBbxViw30l1GAONhe5uGhz0Y%2BaT%2BFlap%2F5F4%2Bbna370wk723inHIa7PlFQ2GMwocmNygY6pgGzJ%2BWpIK877flu4e2V5pEU2JuJrohwcBMBY8vUnP9O3C2rez7kLg7CVwz9WeOsQA15hNikNaI%2F%2BjtbVbrNL2Wp%2FpVtLp5O0B8GkhZlfqRTpsfE9fYKMxg0qTzMY18znyFBTc7vTEKYTVxgdX2ZHwHBtri9KS%2BupCsDE7Qk5aW0ZsYFkL8JWYE9kP478tQuxG43QddkXkWpwI1AU5013xaswyUgVCmj&X-Amz-Signature=49cfd53495964e9dca3a97c29b651bf4e12246097fb2a647c697e1bad607d462&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









