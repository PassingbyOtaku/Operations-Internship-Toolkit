# 文本差异比对工具

一个本地运行的文本比对工具，能够可视化展示两个文本文件之间的增删改差异。

## 功能特点
- 本地运行，无需联网
- 直观的差异可视化界面
- 支持多种文本文件格式（.txt, .md, .html, .py等）
- 可下载完整比对报告
- 既可以通过Python脚本运行，也可以直接打开HTML文件使用

## 项目结构
```
text_comparison_tool/
├── app.py           # Python后端服务，提供比对功能
├── template.html    # 前端界面
├── requirements.txt # 依赖包列表
└── README.md        # 说明文档
```

## 安装说明

### 前提条件
- Python 3.6 或更高版本
- pip（Python包管理工具）

### 安装步骤
1. 克隆或下载本项目到本地
2. 打开命令行，进入项目目录：
   ```
   cd text_comparison_tool
   ```
3. 安装依赖包：
   ```
   pip install -r requirements.txt
   ```

## 使用方法

### 方法一：通过Python脚本运行（推荐）
1. 在项目目录下运行命令：
   ```
   python app.py
   ```
2. 程序会自动打开浏览器，显示比对界面
3. 选择两个要比对的文件，点击"比对文件"按钮
4. 查看比对结果，可选择"下载报告"保存结果

### 方法二：直接打开HTML文件
1. 双击打开`template.html`文件
2. 系统会在默认浏览器中显示界面
3. **注意**：此方式需要本地服务器已运行（即已通过方法一启动app.py）

## 常见问题

### Q: 为什么打开HTML文件后提示"本地服务器未运行"？
A: 直接打开HTML文件时，仍需要后台运行Python服务器。请先执行`python app.py`启动服务器，再刷新HTML页面。

### Q: 支持哪些文件类型的比对？
A: 目前支持所有文本类型文件，包括但不限于：.txt, .md, .html, .py, .java, .cpp, .js, .css等。

### Q: 比对报告保存在哪里？
A: 通过"下载报告"按钮保存的报告会存储在您的浏览器默认下载目录中。

## 技术实现
- 后端：Python + Flask
- 前端：HTML + CSS + JavaScript
- 差异比对：difflib库
- 跨域支持：Flask-CORS

## 许可证
本项目采用MIT许可证 - 详情参见LICENSE文件