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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGSACYNA%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T034856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDsnRFCGN1YVTr1%2F7%2Fy%2FTSkn0qlin9S1pTMVqQg8aWohwIgfIm1kjXS%2FeJhaDcBWgtwDMd4hGWIkj3WxFWplKiPaWQq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDFxnjSBZ7uLBRhR8pCrcA%2B3L6KU1fY1omrK1lEJ9uIL9RiLITR%2B0qEzuKK5nLa1YmQhMJVfOZiMya4ilTdE7%2BdQTmxZTcFc%2FdwwqCUxBqlMUWy4pU9Dl7ll6hsBL9xHz8masWLEZ4jmnY%2FBsAMuogDIFYsEW6Q7MJakFkP%2FWWCDKDRbru9fSr56XfaMp%2BJm4Qtia8uvmnXADYYEWWGC6H5nnxhEbErfSoYH5Op%2B3M6KeeAwmkVm3iux%2F3E%2Biy3avTJNabEtaye9hvbjBSjad5%2BuuVS0fxAgVIoJMiJL6D0DOMNSlHEIq5SZm6KG7CN%2BaeFs8I1g18ePgE3GHm92f%2B9vBRsTrYPppnrXlNtzNb7z%2FjLo1oNO91kV6scLbFQZNRi67ono%2FpG87tu81OrOUXdeOgPzI3E6tWRIfEB2Bpca4EMinel8Lj0lqV96TZ%2BPfrwHhkOSmiowtb1XIsYPo2bb07Z0%2FAo3XvLLNCMnxhQG3k%2BY3pOch6%2BDODgStF3XUjxQ8kMGahS5m4zuR1ly0oXdqWi5wfPMdonfQv8tr0qtc03BY3WyO1KIqIvBBJZ0Q1D1kN1KM5wT4NlNBoQ7Hn2ih5MBaa0i0P17a1ptofsidGRE%2BBC3pTQGZJ0bomoHdx%2Btt28z0D76aLjJjMMCy3M4GOqUBnv2iEJ0jYbm0xaRRFu%2BMKgc3aR8jEAVjdWG%2Bw1q6ZMaQIrieDcngQa%2Bem6miijD4xOnhBKGBGbIG%2Fz%2Fs3HRYH99MxjNg8KYqdunbQLmy8k8QVVru8Jcr%2FWpOMBz6MOut9CWPY9lyi8Gq7N0qJEIuBnPVg85GkxuhXKFJ0qSLdnwh%2FmdI6EilormrZtKVcGYCOvsDFiF8FZtKJxhpX2QUO8bfJmEv&X-Amz-Signature=a4766b9091cb9b585926c006290a4105917523a8b9e306c13c2e6e7bcaafcc43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGSACYNA%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T034856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDsnRFCGN1YVTr1%2F7%2Fy%2FTSkn0qlin9S1pTMVqQg8aWohwIgfIm1kjXS%2FeJhaDcBWgtwDMd4hGWIkj3WxFWplKiPaWQq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDFxnjSBZ7uLBRhR8pCrcA%2B3L6KU1fY1omrK1lEJ9uIL9RiLITR%2B0qEzuKK5nLa1YmQhMJVfOZiMya4ilTdE7%2BdQTmxZTcFc%2FdwwqCUxBqlMUWy4pU9Dl7ll6hsBL9xHz8masWLEZ4jmnY%2FBsAMuogDIFYsEW6Q7MJakFkP%2FWWCDKDRbru9fSr56XfaMp%2BJm4Qtia8uvmnXADYYEWWGC6H5nnxhEbErfSoYH5Op%2B3M6KeeAwmkVm3iux%2F3E%2Biy3avTJNabEtaye9hvbjBSjad5%2BuuVS0fxAgVIoJMiJL6D0DOMNSlHEIq5SZm6KG7CN%2BaeFs8I1g18ePgE3GHm92f%2B9vBRsTrYPppnrXlNtzNb7z%2FjLo1oNO91kV6scLbFQZNRi67ono%2FpG87tu81OrOUXdeOgPzI3E6tWRIfEB2Bpca4EMinel8Lj0lqV96TZ%2BPfrwHhkOSmiowtb1XIsYPo2bb07Z0%2FAo3XvLLNCMnxhQG3k%2BY3pOch6%2BDODgStF3XUjxQ8kMGahS5m4zuR1ly0oXdqWi5wfPMdonfQv8tr0qtc03BY3WyO1KIqIvBBJZ0Q1D1kN1KM5wT4NlNBoQ7Hn2ih5MBaa0i0P17a1ptofsidGRE%2BBC3pTQGZJ0bomoHdx%2Btt28z0D76aLjJjMMCy3M4GOqUBnv2iEJ0jYbm0xaRRFu%2BMKgc3aR8jEAVjdWG%2Bw1q6ZMaQIrieDcngQa%2Bem6miijD4xOnhBKGBGbIG%2Fz%2Fs3HRYH99MxjNg8KYqdunbQLmy8k8QVVru8Jcr%2FWpOMBz6MOut9CWPY9lyi8Gq7N0qJEIuBnPVg85GkxuhXKFJ0qSLdnwh%2FmdI6EilormrZtKVcGYCOvsDFiF8FZtKJxhpX2QUO8bfJmEv&X-Amz-Signature=7207b3e05020661beab9bc4a635eb196c5d7455516cb68c5ac5439334b7c5645&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

