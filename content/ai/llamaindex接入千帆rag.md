---
title: LlamaIndex接入千帆RAG
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- RAG
categories:
- AI
---

记录从使用Llama-index框架, 基于在线文心千帆大模型ERNIE-4.0, 构建实现本地知识检索.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YZQAPEW%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2B6AFgiBo4HO3kKkwmBfcNOuX%2BF%2FK%2F55UIhZXXPQK5nQIhAP9VNMa4nzeMCIkTKgJChq%2FB8DxQVuBPMehZBP7k7HYIKv8DCHQQABoMNjM3NDIzMTgzODA1Igy6b8tJac9cNMopY7kq3AN1zbuUo2PbGW9bm%2BGJSLuEDFrVCzSFr%2FqeSVwcq%2BfNx85L%2Fq6oC3jlifGFheJa04lbzkiUC7gaJQxCUMaN85zqaLeS9%2Bo5e8ylwzMAnIkyBIJPAEgE%2BNTtlXdzZGFvzXLz%2FFVsMqlUcR%2FDxHNua3OGfZjGmJBfXJ5pYV0MYJc8FsujZdR8DIwTHQp2cc6fOR9ICaruA9R7LdS68aTz%2FZnokLpX5i4GF1X%2F2tJLF9Y1tH6phDLUWYxymufNEBh9vkumeuwpyNh64YQ4VJo0nynOiZ5D0821U2ACPUbvD0MmCrIyF5rDjvkvgq9%2FDCrn6k9IjbtGjTEQwSSrfE12ap%2FEqVyzksw8le%2FV%2FTKg1n%2FhGjdIHZJkMH8DLkUt%2BdIZ6bUAO0E66GzRGzF8jNYuxzUPnCOcUbYcDzul1G%2BV0xFH9WhUFUzRt15VX7BIqvNc03bhZjE8nzLyLFuIP2fQIW01s2GjXgStz%2BwYqlCvAAB4dkTqA2AowxyKfmsc%2FSrpucKK2%2FXKWWL63qa5Yhesrw8NBojR7pXatVl8jLY4y6ElIOUTjh6nJTlnUKPwijEf8%2FY9oOxADSMtQGRjyD2cQSJMeyRsZ7kzwcwdAlubyc7j2Cku5lH%2BQt0Q9TfZkjC28dnMBjqkAa%2B9%2F6BNnWwia5ABzuA0ntx7FWcMnyF0EYlm364aL3otHEvvRNDgWQQRAJSAN86czZHLj4EWULEQkIZgX0Fd2QAUB3CqQ%2BVatqIbq9dhF2g74ORjGDxBrNFJfZKKoKkwuKTmdK%2B3Oj9sWCj28rLtNU%2FQy4a2K%2FGi1CDYGMeIMmiPFmB9U1c7dTkQ9vVQmBHzlTUs%2FSnDae9zwbIgY2A27PjMVC%2FQ&X-Amz-Signature=611cda8f2fca1a98588a12e0b9345598e993f3c80006f13072ff5e66dae8b721&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YZQAPEW%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2B6AFgiBo4HO3kKkwmBfcNOuX%2BF%2FK%2F55UIhZXXPQK5nQIhAP9VNMa4nzeMCIkTKgJChq%2FB8DxQVuBPMehZBP7k7HYIKv8DCHQQABoMNjM3NDIzMTgzODA1Igy6b8tJac9cNMopY7kq3AN1zbuUo2PbGW9bm%2BGJSLuEDFrVCzSFr%2FqeSVwcq%2BfNx85L%2Fq6oC3jlifGFheJa04lbzkiUC7gaJQxCUMaN85zqaLeS9%2Bo5e8ylwzMAnIkyBIJPAEgE%2BNTtlXdzZGFvzXLz%2FFVsMqlUcR%2FDxHNua3OGfZjGmJBfXJ5pYV0MYJc8FsujZdR8DIwTHQp2cc6fOR9ICaruA9R7LdS68aTz%2FZnokLpX5i4GF1X%2F2tJLF9Y1tH6phDLUWYxymufNEBh9vkumeuwpyNh64YQ4VJo0nynOiZ5D0821U2ACPUbvD0MmCrIyF5rDjvkvgq9%2FDCrn6k9IjbtGjTEQwSSrfE12ap%2FEqVyzksw8le%2FV%2FTKg1n%2FhGjdIHZJkMH8DLkUt%2BdIZ6bUAO0E66GzRGzF8jNYuxzUPnCOcUbYcDzul1G%2BV0xFH9WhUFUzRt15VX7BIqvNc03bhZjE8nzLyLFuIP2fQIW01s2GjXgStz%2BwYqlCvAAB4dkTqA2AowxyKfmsc%2FSrpucKK2%2FXKWWL63qa5Yhesrw8NBojR7pXatVl8jLY4y6ElIOUTjh6nJTlnUKPwijEf8%2FY9oOxADSMtQGRjyD2cQSJMeyRsZ7kzwcwdAlubyc7j2Cku5lH%2BQt0Q9TfZkjC28dnMBjqkAa%2B9%2F6BNnWwia5ABzuA0ntx7FWcMnyF0EYlm364aL3otHEvvRNDgWQQRAJSAN86czZHLj4EWULEQkIZgX0Fd2QAUB3CqQ%2BVatqIbq9dhF2g74ORjGDxBrNFJfZKKoKkwuKTmdK%2B3Oj9sWCj28rLtNU%2FQy4a2K%2FGi1CDYGMeIMmiPFmB9U1c7dTkQ9vVQmBHzlTUs%2FSnDae9zwbIgY2A27PjMVC%2FQ&X-Amz-Signature=5d9c4820e7aa08df8b6212453f0ff05ff7e42454bddea8df9162560e92fda272&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 导入本地Embedding

- 下载Embedding模型
```python
from modelscope import snapshot_download
model_dir = snapshot_download('Xorbits/bge-m3', cache_dir='/data/LLMs')
```

- 加载本地Embedding模型
```python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
cache_folder = r"embed_model/m3e-large"embed_model = HuggingFaceEmbedding(cache_folder=cache_folder)
```

---

### 构建本地知识库

```python
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
directory = "/data/documents" #文档路径vector_index = VectorStoreIndex.from_documents(documents)
```

---

### 构建查询引擎

```python
query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=llm)
```

> similarity_top_k可根据经验自行调整, 推荐设置3, 5.

---

### 构建RAG Agent

- 构建工具
```python
import os
def get_tool(name, full_name, documents=None):
    if not os.path.exists(f"./data/{name}"):
        # build vector index        vector_index = VectorStoreIndex.from_documents(documents)
        vector_index.storage_context.persist(persist_dir=f"./data/{name}")
    else:
        vector_index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=f"./data/{name}"),
        )
    query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=llm)
    query_engine_tool = QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name=name,
            description=(
                "Provides information about Uber quarterly financials ending"                f" {full_name}"            ),
        ),
    )
    return query_engine_tool
```

- 设置Agent
```python
from llama_index.core.agent import AgentRunner, ReActAgent
agent = ReActAgent.from_tools(
    query_engine_tools, llm=agent_llm, verbose=True, max_iterations=20)
```

- 运行
```python
response = agent.chat("您的问题")
```

### 整体代码

```python
from llama_index.core import Settings
import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.qianfan import Qianfan
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# 初始化Qianfan模型class Rag:
    def __init__(self):
        self.access_key = ""        self.secret_key = ""        self.model_name = "ERNIE-4.0-8K-Latest"        self.url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"        self.llm = Qianfan(self.access_key, self.secret_key, self.model_name, self.url, context_window=8192)
        self.cache_folder = r"embed_model/m3e-large"        self.directory = r"/data/documents"  # 数据目录路径    def get_tool(self, name, full_name, documents=None):
        embed_model = HuggingFaceEmbedding(cache_folder=self.cache_folder)
        Settings.embed_model = embed_model
        vector_index = VectorStoreIndex.from_documents(documents)
        persist_path = f"{self.directory}/{name}"        if not os.path.exists(persist_path):
            vector_index.storage_context.persist(persist_dir=persist_path)
        query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=self.llm)
        query_engine_tool = QueryEngineTool(query_engine=query_engine, metadata=ToolMetadata(name=name, description=f"Provides information from document {full_name}"))
        return query_engine_tool
    def parse_args(self):
        query_engine_tools = []
        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):
                filepath = os.path.join(self.directory, filename)
                documents = SimpleDirectoryReader(input_files=[filepath]).load_data()
                tool_name = filename[:-4]  # 去除'.txt'得到工具名称                tool = self.get_tool(tool_name, tool_name, documents=documents)
                query_engine_tools.append(tool)
        return query_engine_tools
    def query_engine(self, query):
        from llama_index.core.agent import ReActAgent
        tools = self.parse_args()
        agent = ReActAgent.from_tools(tools, llm=self.llm, verbose=True, max_iterations=20)
        response = agent.chat(query)
        return response
# 创建 Rag 实例并执行查询if __name__ == "__main__":
    rag = Rag()
    print(rag.query_engine(query="问题"))
```

> 参考链接

