---
title: 论文精读_寻找RAG最优策略
date: '2024-11-28T07:08:00.000Z'
lastmod: '2024-12-02T01:20:00.000Z'
draft: false
tags:
- Knowledge
- RAG
categories:
- 知识
---

> 💡  这篇真的全是干货…论文的实验部分，我就不写了。看看就行。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/78127f49-5326-457b-85b3-9e146b9c399f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7FRXWQF%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFrMJor0BQPAoKf%2BMoxDISYvq5pVJm6Z6sdDrkiQdViiAiEAi9l4ql1mSMhUHQDy2XV46CSOkIQfB3F2GQ4PqPnxNfkq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDDqqZ6hBfp49SyPOhyrcAwKnExUIweB056kVEqqLh80hWTq5j7wiAmN9xbzgR7EqtMGT5NoT8MCO1LupFp13StALCClXX5nnnpB204R%2F745tLSVz4mrg5yr9j%2FpFgiX3mxbdIan07FNNCEJ9bKdyImWS7lLX9zO7UEOXfLSE5640pejYddnAVQMtlr28b1FhN9eNVjIRSEzIBhArvzH0UGbKFfQ3ozfJUO9CRHNMdURO2piXmJTRv4vMSLGO%2B9rPfIyPNOZhCbP0XH%2FAFpDPi2NeOccZwIgIEAoQJuNOnkomYDZFr2ifaLZzeDYHdWSrzh%2FgH6hBam%2FaN8K2uo%2FeyYgPd0w3r6meH5p43f60iMp8ZPifX7E%2ByhAhplqpjcOeEMA9bF72JAHbqj8JqhMI14H7ggRfEX5yV8eSC7gJ%2F8jem6XN9hShCdQxp3Jm9DHBDSbLphfRn8R5g%2FVuO9%2BXvte40bypeyDGVP6lUd6laH6fT4MxRLixy7A0Lhs76WZHjt%2FPeTE2ZeqG4wHYCu%2BJo7ckbcUl3J8avvdFXstOnyitB%2BChIgQ2xyLNJMhv5g2hTTeBazzut5aR4%2FE0BSwl3Dm8%2BqWxPkadUrE6BFzDUbMzSuZrtCZrhjN0Iy3pEFC2kbA5KU74fL0p6gU%2BMOinzskGOqUBHzOi3m7shMDNHvQzxli2feVS3YGq9S4CPG7c9h44ZgHG3su9EO8yR1SxjJpjZnrQgXjoqQc7OWrKhjd9F%2F61pu1wVQ3%2F400Q%2F9NzolGhHAYOSDSAbg6pzBAlUyGdSJhiIVcGe6WQA8dz4lvr5AtO75UDfg2BLKmeSvvbEjuObxOy54aUM9Awaic6oGmtoErqBHuEmHOa6C5PCDRQd5pWmbLKSrv8&X-Amz-Signature=6ec2ade4eba0ee23bd61c88ebd5fc291c7574bec87a2d1aee0f0b219c06f0bb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 相关工作|查询检索层面

确保大型语言模型（LLMs）如ChatGPT和LLaMA生成的回应准确性至关重要。然而，简单地增加模型大小并不能从根本上解决“幻觉”问题，这在知识密集型任务和专业领域尤为明显。检索增强生成（RAG）通过从外部知识库检索相关文档，为LLMs提供准确、实时、领域特定的上下文，以解决这些挑战。先前的工作通过查询和检索转换优化了RAG流程，提高了检索器的性能，并对检索器和生成器进行了微调。这些优化改善了输入查询、检索机制与生成过程之间的互动，确保了回应的准确性和相关性。

## RAG工作流

在本节中，我们将详细介绍RAG工作流程的各个组件。针对每个模块，我们回顾常用的方法，并为我们的最终流程选择了默认和备选方法。

### 查询分类

并非所有的查询都需要通过检索增强，因为大型语言模型（LLMs）本身就具备一定的处理能力。尽管检索增强生成（RAG）可以提高信息的准确性并减少虚构内容，但频繁的检索可能会增加响应时间。因此，我们首先通过对查询进行分类来确定是否需要检索。需要检索的查询会经过RAG模块处理；其他则直接由LLMs处理。通常，在需要超出模型参数范围的知识时推荐使用检索。然而，检索的必要性根据任务的不同而有所变化。例如，一个训练至2023年的LLM可以处理“Sora是由OpenAI开发的”这一翻译请求而无需检索。相反，对于同一主题的介绍请求则需要检索来提供相关信息。



因此，我们建议按类型对任务进行分类，以确定查询是否需要检索。对于完全基于用户提供信息的任务，我们标记为“充分”，不需要检索；否则，我们标记为“不足”，可能需要检索。我们训练了一个分类器来自动化这一决策过程。

---

### Chunking

将文档分块成更小的段落对于提高检索的准确性和避免在大型语言模型（LLMs）中出现长度问题至关重要。这个过程可以在不同的粒度级别上应用，比如令牌（token）、句子和语义级别。

- 令牌级别的分块很直接，但可能会分割句子，影响检索质量。
- 语义级别的分块利用大型语言模型来确定分割点，能保持上下文不变，但是耗时。
- 句子级别的分块在保留文本语义的同时，平衡了简单性和效率。
在这项研究中，我们使用句子级别的分块，平衡了简单性和语义保留。我们从四个维度考察了分块方法。

向量数据库存储着带有元数据的嵌入向量，通过各种索引和近似最近邻（ANN）方法，能够高效地检索与查询相关的文档。为了为我们的研究选择一个合适的向量数据库，我们基于四个关键标准对几个选项进行了评估：多种索引类型、支持十亿级别的向量、混合搜索以及云原生能力。这些标准因其对于灵活性、可扩展性以及在现代云基础设施中部署的便捷性的影响而被选中。多种索引类型提供了基于不同数据特性和用例优化搜索的灵活性。十亿级别的向量支持对于处理LLM应用中的大型数据集至关重要。混合搜索将向量搜索与传统关键词搜索结合起来，提高了检索准确性。最后，云原生能力确保了在云环境中的无缝集成、可扩展性和管理。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c4ac03c-4cd8-4e84-aa5e-b0d35bd8c0fa/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7FRXWQF%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFrMJor0BQPAoKf%2BMoxDISYvq5pVJm6Z6sdDrkiQdViiAiEAi9l4ql1mSMhUHQDy2XV46CSOkIQfB3F2GQ4PqPnxNfkq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDDqqZ6hBfp49SyPOhyrcAwKnExUIweB056kVEqqLh80hWTq5j7wiAmN9xbzgR7EqtMGT5NoT8MCO1LupFp13StALCClXX5nnnpB204R%2F745tLSVz4mrg5yr9j%2FpFgiX3mxbdIan07FNNCEJ9bKdyImWS7lLX9zO7UEOXfLSE5640pejYddnAVQMtlr28b1FhN9eNVjIRSEzIBhArvzH0UGbKFfQ3ozfJUO9CRHNMdURO2piXmJTRv4vMSLGO%2B9rPfIyPNOZhCbP0XH%2FAFpDPi2NeOccZwIgIEAoQJuNOnkomYDZFr2ifaLZzeDYHdWSrzh%2FgH6hBam%2FaN8K2uo%2FeyYgPd0w3r6meH5p43f60iMp8ZPifX7E%2ByhAhplqpjcOeEMA9bF72JAHbqj8JqhMI14H7ggRfEX5yV8eSC7gJ%2F8jem6XN9hShCdQxp3Jm9DHBDSbLphfRn8R5g%2FVuO9%2BXvte40bypeyDGVP6lUd6laH6fT4MxRLixy7A0Lhs76WZHjt%2FPeTE2ZeqG4wHYCu%2BJo7ckbcUl3J8avvdFXstOnyitB%2BChIgQ2xyLNJMhv5g2hTTeBazzut5aR4%2FE0BSwl3Dm8%2BqWxPkadUrE6BFzDUbMzSuZrtCZrhjN0Iy3pEFC2kbA5KU74fL0p6gU%2BMOinzskGOqUBHzOi3m7shMDNHvQzxli2feVS3YGq9S4CPG7c9h44ZgHG3su9EO8yR1SxjJpjZnrQgXjoqQc7OWrKhjd9F%2F61pu1wVQ3%2F400Q%2F9NzolGhHAYOSDSAbg6pzBAlUyGdSJhiIVcGe6WQA8dz4lvr5AtO75UDfg2BLKmeSvvbEjuObxOy54aUM9Awaic6oGmtoErqBHuEmHOa6C5PCDRQd5pWmbLKSrv8&X-Amz-Signature=e77ac6444803dd57387eae049771f4d3e6788a1837d24cec8f4f0da45b56b684&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### Retrieval方式

针对用户查询，检索模块从预建的语料库中选择与查询和文档的相似度最高的前k个相关文档。然后，生成模型使用这些文档来制定针对查询的适当响应。然而，原始查询由于表达不佳和缺乏语义信息，通常会表现不佳，这对检索过程产生了负面影响。为了解决这些问题，我们评估了三种查询转换方法，使用推荐的LLM-Embedder作为查询和文档编码器：

- 查询改写：查询改写通过改进查询来更好地匹配相关文档。受到Rewrite-Retrieve-Read框架的启发，我们促使一个LLM重写查询以提升性能。
- 查询分解：这种方法涉及到基于从原始查询中派生的子问题来检索文档，这比理解和处理更复杂的查询要困难。
- 伪文档生成：这种方法基于用户查询生成一个假想的文档，并使用假想答案的嵌入来检索相似文档。一个值得注意的实现是HyDE。
最近的研究表明结合基于词汇的搜索与向量搜索可以显著提高性能。在本研究中，我们使用BM25进行稀疏检索和Contriever，一个无监督对比编码器，进行密集检索。

---

### Reranking

在最初的检索之后，将采用重排序阶段来提高检索到的文档的相关性，确保最相关的信息出现在列表的顶部。这一阶段采用更精确、耗时更长的方法有效地重新排序文档，增加查询与排名最高的文档之间的相似度。

在我们的重排序模块中，我们考虑了两种方法：DLM重排序和TILDE重排序。DLM重排序采用分类方法，而TILDE重排序则侧重于查询可能性。这些方法分别优先考虑性能和效率。

- DLM重排方法：这种方法利用深度语言模型（DLMs）进行重排。这些模型被微调用以将文档与查询的相关性分类为“真”或“假”。在微调过程中，模型通过将查询和文档输入连接起来，并根据相关性进行标记来进行训练。在推理时，文档根据“真”标记的概率进行排名。
- TILDE重排：TILDE通过预测模型词汇表中的各个词项的概率来独立计算每个查询词项的可能性。通过对查询词项的预计算对数概率求和，为文档打分，从而在推理时快速重排。TILDEv2通过仅索引文档中存在的词项，使用NCE损失，并扩展文档，从而提高效率并减小索引大小。
我们的实验是在MS MARCO Passage排名数据集上进行的，这是一个大规模的机器阅读理解数据集。我们遵循并对PyGaggle和TILDE提供的实现进行了修改，使用了模型monoT5、monoBERT、RankLLaMA和TILDEv2。重排结果显示在表中。我们推荐monoT5作为一种综合性的方法，平衡了性能和效率。RankLLaMA适合于实现最佳性能，而TILDEv2是在固定集合上获得最快体验的理想选择。实验设置和结果的详细信息在附录中呈现。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/100cf766-c92f-4387-8745-20b0e94296e4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7FRXWQF%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFrMJor0BQPAoKf%2BMoxDISYvq5pVJm6Z6sdDrkiQdViiAiEAi9l4ql1mSMhUHQDy2XV46CSOkIQfB3F2GQ4PqPnxNfkq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDDqqZ6hBfp49SyPOhyrcAwKnExUIweB056kVEqqLh80hWTq5j7wiAmN9xbzgR7EqtMGT5NoT8MCO1LupFp13StALCClXX5nnnpB204R%2F745tLSVz4mrg5yr9j%2FpFgiX3mxbdIan07FNNCEJ9bKdyImWS7lLX9zO7UEOXfLSE5640pejYddnAVQMtlr28b1FhN9eNVjIRSEzIBhArvzH0UGbKFfQ3ozfJUO9CRHNMdURO2piXmJTRv4vMSLGO%2B9rPfIyPNOZhCbP0XH%2FAFpDPi2NeOccZwIgIEAoQJuNOnkomYDZFr2ifaLZzeDYHdWSrzh%2FgH6hBam%2FaN8K2uo%2FeyYgPd0w3r6meH5p43f60iMp8ZPifX7E%2ByhAhplqpjcOeEMA9bF72JAHbqj8JqhMI14H7ggRfEX5yV8eSC7gJ%2F8jem6XN9hShCdQxp3Jm9DHBDSbLphfRn8R5g%2FVuO9%2BXvte40bypeyDGVP6lUd6laH6fT4MxRLixy7A0Lhs76WZHjt%2FPeTE2ZeqG4wHYCu%2BJo7ckbcUl3J8avvdFXstOnyitB%2BChIgQ2xyLNJMhv5g2hTTeBazzut5aR4%2FE0BSwl3Dm8%2BqWxPkadUrE6BFzDUbMzSuZrtCZrhjN0Iy3pEFC2kbA5KU74fL0p6gU%2BMOinzskGOqUBHzOi3m7shMDNHvQzxli2feVS3YGq9S4CPG7c9h44ZgHG3su9EO8yR1SxjJpjZnrQgXjoqQc7OWrKhjd9F%2F61pu1wVQ3%2F400Q%2F9NzolGhHAYOSDSAbg6pzBAlUyGdSJhiIVcGe6WQA8dz4lvr5AtO75UDfg2BLKmeSvvbEjuObxOy54aUM9Awaic6oGmtoErqBHuEmHOa6C5PCDRQd5pWmbLKSrv8&X-Amz-Signature=9b8b9354770f1a1c1f93f026238912f1d92ce74c88aa8e97458ad93e8dd7fb8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 文档重组

文档重组后续过程的表现，比如LLM响应生成，可能会受到提供文档的顺序影响。为了解决这个问题，在重新排名之后的工作流程中，我们加入了一个紧凑的重组模块，包含三种重组方法：“前向”、“反向”和“两侧”。“前向”方法通过降序重新排名阶段的相关性得分来重组文档，而“反向”则按升序排列它们。对于LLM，当相关信息放在输入的头部或尾部时，可以达到最佳性能，我们也加入了“两侧”选项。

---

> Reference



