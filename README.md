# Qwen-CartoGrader 🌍✏️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

基于Qwen-VL模型的地图作业智能批改系统 | AI-powered Cartography Assignment Grading System

---

## 📌 项目概述 | Overview

**中文**
本工具利用Qwen-VL多模态大模型，自动化批改地图学课程作业。通过分析学生提交的地图图片，快速识别配色方案、要素完整性、文字标注等常见问题，输出标准化审查报告。

**English**
This tool leverages the Qwen-VL multimodal LLM to automatically grade cartography assignments. By analyzing student-submitted map images, it efficiently detects common issues like color schemes, element completeness, and text annotations, generating standardized evaluation reports.

---

## 🚀 核心功能 | Features

- **多维度审查** | Multi-dimensional Analysis
  ✅ 配色规范检查 | Color Scheme Validation
  ✅ 地图要素完整性验证 | Map Element Completeness Check
  ✅ 文字标注合规性检测 | Text Annotation Compliance
  ✅ 布局结构评估 | Layout Structure Evaluation
- **技术特性** | Technical Highlights
  🔹 Qwen-VL-Max视觉语言模型 | Qwen-VL-Max Vision-Language Model
  🔹 Base64图像流式处理 | Base64 Image Stream Processing
  🔹 异步API调用优化 | Asynchronous API Call Optimization
  🔹 文件批改后统一输出查看 |  Unified Output After Correction Optimization

## 🛠️ 快速开始 | Getting Started

### 安装依赖 | Installation

```bash
pip install openai python-dotenv
```

### 地图文件整理 | Map File Preparation

* 准备好你的地图文件 | Prepare Your Map
* 通过 **Filename.ipynb** 进行文件重命名（可选） |  File renaming via **Filename.ipynb** (Optional)

### 注册Qwen API |

* 在[阿里云百炼模型平台](https://bailian.console.aliyun.com//model-market#/home)注册，选择对应模型并获取相应模型API，需要多模态模型（如Qwen-Omni-Turbo, Qwen-Max)，填入代码文件中｜Register in [AliCloud Hundred Refined Models Platform](https://bailian.console.aliyun.com//model-market#/home), select the corresponding model and get the corresponding model API, need multimodal model (e.g. Qwen-Omni-Turbo, Qwen-Max), fill in the code file

### 地图批改 | Cartography Assignment Grading

```
python Qwen_CartoGrader.py
```
