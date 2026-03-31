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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZV2EC2GU%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIBxnckNRaCpN9abizULgFMT1TVOJey7u51Z10CCilBc8AiAwf5yXLUSCVGKMSGZReIgXKeGHeOV27Y%2Fpv%2B%2BHpPQHjSr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMZ5f0wtB1dZoRWagTKtwDbDnv4SwS%2FZ3s8tZbNoHfUyu7D0p2ChNEPZ7cUnJY75VMx5aL3Agyqgdohj4rng7oMN0tuNhwoiEP6ckerUqbP9tK0G8bCnl2xE3NyWT88zGSiA2AoU%2F%2FmZqxYLb1cBW6ZtRpP2NEAEKhv9QgCJdgmd3Al2By0Yr6Yd%2F%2BNHOS3UBRxO8dsv4qkPpnq3fMrK2%2BJH5OvL92Drba0MTyaZFrewbPKBpvU9LQLPZn3x9j1rhwqklhVcc%2B8XFSQSVcDYnWx8RKtv3Ly1N8qnE91g04cNa7TlRyfeeJTlu7zDptquD12BNecBBFftfl5dmD%2BqjPR6Pg030uuIg2aAtGirtgHBMmvXarfKu1%2BuZQcuyZXPkyUE%2BKowznpgoL8lKugtkRcD84Q%2FnO7a5HubTgLKEP9zBBjh%2F4622D1G2tzM%2F4vPW%2FIol6AspGbeN7d%2BV9Wt6HnYc%2F1G16mSMN8Lomw0GdWgGLtXEwkHoBGAPfYBVcYnBGvfJOXYOmSd5B2NjYs918eZiJ%2FyPnTo9MvWVR45EPi1Qzot61%2FvsLXle7bL7gOhW34864fSxekEskkAcCoPhK6Au6W9q5muRtO8LteVme0qrDwrjSveREcuNpaNTpU2euINlfo3Ag0MrNimgw4u6szgY6pgFkWGNjqMlV1CWedmoH5EZUQ9jDwhH0GFM%2BX0hl65RsXQzkPNgHQYaJZS6%2BNncurSpk7AqPc%2BCH%2Bm5fd4zaFxctSRf31uV6AYGx%2BU7SrmFPl1GknQq2l1UG%2BhvsJg2jgnfngmM6x5zvrmVcdeFKLF05aUkMV1vTvZxl1L3ThRYU0sqEOsqiKO%2FO3NzFviE%2FlKC5Hzh0C%2FZtn2CnR7Gxf3TdRJa8noSW&X-Amz-Signature=8f5f04ad560211e9b273b425ef00a31041f833ab730bc2d4b02413fe591b5786&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZV2EC2GU%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIBxnckNRaCpN9abizULgFMT1TVOJey7u51Z10CCilBc8AiAwf5yXLUSCVGKMSGZReIgXKeGHeOV27Y%2Fpv%2B%2BHpPQHjSr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMZ5f0wtB1dZoRWagTKtwDbDnv4SwS%2FZ3s8tZbNoHfUyu7D0p2ChNEPZ7cUnJY75VMx5aL3Agyqgdohj4rng7oMN0tuNhwoiEP6ckerUqbP9tK0G8bCnl2xE3NyWT88zGSiA2AoU%2F%2FmZqxYLb1cBW6ZtRpP2NEAEKhv9QgCJdgmd3Al2By0Yr6Yd%2F%2BNHOS3UBRxO8dsv4qkPpnq3fMrK2%2BJH5OvL92Drba0MTyaZFrewbPKBpvU9LQLPZn3x9j1rhwqklhVcc%2B8XFSQSVcDYnWx8RKtv3Ly1N8qnE91g04cNa7TlRyfeeJTlu7zDptquD12BNecBBFftfl5dmD%2BqjPR6Pg030uuIg2aAtGirtgHBMmvXarfKu1%2BuZQcuyZXPkyUE%2BKowznpgoL8lKugtkRcD84Q%2FnO7a5HubTgLKEP9zBBjh%2F4622D1G2tzM%2F4vPW%2FIol6AspGbeN7d%2BV9Wt6HnYc%2F1G16mSMN8Lomw0GdWgGLtXEwkHoBGAPfYBVcYnBGvfJOXYOmSd5B2NjYs918eZiJ%2FyPnTo9MvWVR45EPi1Qzot61%2FvsLXle7bL7gOhW34864fSxekEskkAcCoPhK6Au6W9q5muRtO8LteVme0qrDwrjSveREcuNpaNTpU2euINlfo3Ag0MrNimgw4u6szgY6pgFkWGNjqMlV1CWedmoH5EZUQ9jDwhH0GFM%2BX0hl65RsXQzkPNgHQYaJZS6%2BNncurSpk7AqPc%2BCH%2Bm5fd4zaFxctSRf31uV6AYGx%2BU7SrmFPl1GknQq2l1UG%2BhvsJg2jgnfngmM6x5zvrmVcdeFKLF05aUkMV1vTvZxl1L3ThRYU0sqEOsqiKO%2FO3NzFviE%2FlKC5Hzh0C%2FZtn2CnR7Gxf3TdRJa8noSW&X-Amz-Signature=e0ff30b8e727c9a3ad539f7b21fc633d8ddf781f38c903591c86e80d93095e36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

