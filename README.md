# MultiModel-RAG-ColPali-Qdrant-Qwen

本仓库包含两个notebook，演示了基于视觉的检索增强生成（RAG）流水线，使用 ColPali、Qdrant 和 Qwen 模型构建。项目专注于高效的图像检索，并基于检索结果生成用户查询的详细回答。

## 项目结构

```
MultiModel-RAG-ColPali-Qdrant-Qwen-main/
│
├── multimodel.ipynb          # 双GPU部署的完整RAG流水线（ColPali检索 + Qwen2VL生成）
├── colpali_qdrand.ipynb      # 集成Qdrant的检索流水线
├── check_env.py              # 环境依赖检查脚本
├── download_models.py        # 模型下载脚本
│
├── pdf_files/
│   └── rav_4.pdf             # 示例PDF文件（丰田RAV4用户手册）
├── assets/
│   └── similarity_map.png    # 相似度可视化图示
└── .idea/                    # IDE配置文件（可忽略）
```

## 核心模型介绍

### ColPali — 文档检索
**[ColPali](https://github.com/illuin-tech/colpali)** 是一种先进的视觉语言模型（VLM），用于文档检索。通过将每个PDF页面视为图像，ColPali 跳过了复杂的OCR和版面检测流水线。它为每个页面生成多向量嵌入，在多个基准测试中表现出显著优于传统方法的性能。

### Qdrant — 向量数据库
**[Qdrant](https://qdrant.tech/)** 是一个快速且可扩展的向量数据库。Qdrant 支持多向量嵌入，非常适合 ColPali，因为嵌入是为每个图像块创建的。它是开源解决方案，提供免费层级，能够高效处理大规模相似性搜索。

### Qwen2-VL — 视觉语言生成
**[Qwen2-VL](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct)** 是阿里巴巴开发的知名视觉语言模型，集成到流水线中用于从检索到的图像生成详细且上下文丰富的回答。

## 文件说明

| 文件 | 说明 |
|------|------|
| `multimodel.ipynb` | 完整的双GPU RAG流水线。在 cuda:0 上使用 ColPali 进行文档检索（PDF→图像→嵌入→相似度检索），在 cuda:1 上使用 Qwen2VL 生成回答。包含可解释性可视化，展示模型在token级别上的关注区域。 |
| `colpali_qdrand.ipynb` | 集成 Qdrant 向量数据库的检索流水线。演示如何将 ColPali 嵌入存入 Qdrant，并基于用户查询检索相关文档页面，最后通过 Qwen2VL 生成回答。 |
| `check_env.py` | 环境检查工具，检测项目所需的全部依赖包是否已安装（PyTorch、Transformers、ColPali Engine 等），并显示各包版本。 |
| `download_models.py` | 模型下载脚本，自动从 Hugging Face 下载项目所需的三个模型：`colpaligemma-3b-pt-448-base`、`colpali-v1.2` 和 `Qwen2-VL-2B-Instruct`。 |

## 快速开始

```bash
# 1. 检查环境依赖
python check_env.py

# 2. 下载所需模型
python download_models.py

# 3. 安装额外依赖（如缺失）
pip install colpali-engine==0.3.4 pdf2image qwen-vl-utils transformers
```