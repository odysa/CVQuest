# CVQuest

让 AI 为您生成面试问题！
<br>
<br>
这个命令行界面（CLI）工具旨在通过根据候选人的简历自动生成面试问题，帮助面试官和招聘人员。该工具使用简历解析器从简历中提取信息，并结合面试问题生成器来创建相关问题。

CVQuest 还提供了一个基于 Gradio 的用户界面，允许用户以 PDF 格式上传他们的简历，并按类别接收面试问题列表。

## 特点 ✨
* 解析 PDF 格式的简历文件并将其转换为 JSON 格式
* 根据从简历中提取的信息生成面试问题
* 基于 Gradio 的用户界面，用于生成个性化面试问题

## 您可能还会喜欢我们的 AI 简历生成器：baynana.co 🚀

[Baynana.co](https://baynana.co) 是一个 AI 驱动的简历生成器，可以帮助您创建专业的、针对您所在行业的简历。使用 Baynana AI，您可以：

- 通过与 Baynana AI 聊天，零努力地创建您的简历，它会成为您的个人简历助手
- 在编辑时获取实时 ATS 反馈，确保您的简历对 ATS 友好
- 将简历导出为 PDF、LaTex 甚至网站支持的 HTML 格式

👉 [立即开始使用 Baynana.co！](https://baynana.co)

## 依赖项
* Python 3.8 或更高版本
* typer
* OpenAI
* Gradio

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/odysa/CVQuest-CLI
```

2. 安装依赖项
```bash
pip install -r requirements.txt
```
3. 该应用程序依赖于 OpenAI。请设置您的 API 密钥
```bash
export OPENAI_API_KEY = <you-api-key>
```

## 使用

### 从简历生成面试问题（Gradio UI）

要启动基于 Gradio 的用户界面，根据用户的简历生成个性化面试问题，请在终端中执行以下命令：
```bash
python3 server.py
```
运行命令后，Gradio UI 将在您的默认网络浏览器中启动，允许您上传 PDF 格式的简历并生成面试问题。

预览
<img width="1422" alt="image" src="https://user-images.githubusercontent.com/61036578/226255002-a1a661fa-86a8-4a82-9b29-3da68b088920.png">


### 使用CLI

CLI 中有两个主要命令：
1. q：根据从简历中提取的信息生成面试问题
2. json：将简历 PDF 文件解析为 JSON 格式

### 从简历生成面试问题（CLI）
```bash
python main.py q <file_path>
```
```json
{
  "technical_questions": [
    "您能讨论一下您在基于 LSM 的存储引擎方面的经验吗？这种方法的主要优点是什么，以及您如何在 AgateDB 项目中应用它？",
    "在针对 TerarkDB 的区域感知垃圾收集工作中，您用来评估实施效果的关键性能指标是什么？与其他方法相比如何？"
    ......
  ],
  "behavior_questions": [
    "您如何看待在团队环境中工作？您能提供一个与团队成员在一个具有挑战性的项目上成功合作的例子吗？",
    "作为 RisingLight 项目的维护者，您如何平衡维护者的职责和其他承诺？您如何确保在满足项目和社区的需求的同时，也能管理好自己的工作负载？"
  ]
  ......
}
```

### 从简历生成 Json 输出（CLI）
```bash
python main.py json <file_path>
```
示例：

即将推出