# 照片自动分类工具

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-orange.svg)](https://www.riverbankcomputing.com/software/pyqt/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 智能检测损坏、空镜、闭眼、模糊、遮挡等缺陷照片，一键整理您的相册

## ✨ 功能特性

| 检测类型 | 说明 |
|---------|------|
| 🔴 **损坏** | 检测文件损坏或无法读取的照片 |
| 🟡 **空镜** | 检测空文件或零字节文件 |
| 🔵 **闭眼** | 检测闭眼的人脸照片 |
| 🟣 **模糊** | 检测模糊或失焦的照片 |
| 🟢 **遮挡** | 检测有遮挡物的照片 |

### 核心功能
- 📤 **文件上传** - 支持点击或拖拽上传图片文件
- 📁 **文件夹扫描** - 批量扫描整个文件夹
- 🖼️ **缩略图预览** - 实时显示照片缩略图
- 📊 **分类统计** - 自动统计正常/废片数量
- 🗂️ **一键整理** - 自动将废片移动到单独文件夹
- 📄 **导出报告** - 生成详细的扫描报告

## 🚀 快速开始

### 方式一：下载即用（推荐）

从 [Releases](https://github.com/shenglihalisen/photo-classifier/releases) 下载最新版本：

| 版本 | 说明 | 下载 |
|------|------|------|
| Web端 | 浏览器访问，支持文件上传和拖拽 | [下载 v1.0.0](https://github.com/shenglihalisen/photo-classifier/releases/download/v1.0.0/-.zip) |

**使用步骤：**
1. 下载并解压 `照片分类工具-打包版.zip`
2. 进入 `照片分类工具-Web端` 文件夹
3. 双击 `照片分类工具-Web端.exe`
4. 浏览器自动打开 http://localhost:5000

### 方式二：源码运行

**环境要求：**
- Python 3.8+
- Windows 10/11

**安装依赖：**
```bash
pip install -r requirements.txt
```

**启动Web端：**
```bash
python run_web.py
```
访问 http://localhost:5000

**启动桌面端：**
```bash
python run_desktop.py
```

## 📖 使用指南

### Web端界面

1. **选择输入方式**
   - 📁 上传文件：点击或拖拽图片文件
   - 📂 文件夹路径：输入文件夹路径扫描

2. **选择模式**
   - 自动模式：自动处理所有废片
   - 手动确认：手动选择要处理的废片

3. **开始扫描**
   - 点击"开始扫描"按钮
   - 等待扫描完成

4. **查看结果**
   - 正常照片：显示在绿色区域
   - 废片：按类型分类显示在红色区域

5. **处理废片**
   - 移动废片：将废片移动到"废片"文件夹
   - 删除废片：永久删除废片（谨慎使用）

### 桌面端界面

1. 点击"选择文件夹"选择要扫描的照片文件夹
2. 程序自动开始扫描
3. 左侧显示正常照片，中间显示废片列表
4. 点击照片查看详情和预览
5. 双击照片打开大图预览
6. 使用工具栏移动废片或导出报告

## 🛠️ 技术栈

- **后端**：Python + Flask
- **前端**：HTML5 + CSS3 + JavaScript
- **桌面端**：PyQt5
- **图像处理**：OpenCV + Pillow
- **人脸检测**：MediaPipe
- **深度学习**：NumPy

## 📁 项目结构

```
photo-classifier/
├── classifiers/          # 分类器模块
│   ├── blink.py         # 闭眼检测
│   ├── blur.py          # 模糊检测
│   ├── corrupted.py     # 损坏检测
│   ├── empty.py         # 空文件检测
│   └── obstruction.py   # 遮挡检测
├── desktop/             # 桌面端界面
│   └── app.py
├── engine/              # 分类引擎
│   └── classifier.py
├── web/                 # Web端
│   ├── app.py
│   └── templates/
├── run_desktop.py       # 桌面端入口
├── run_web.py          # Web端入口
└── requirements.txt    # 依赖列表
```

## 📝 更新日志

### v1.0.0 (2025-05-14)
- ✨ 初始版本发布
- 📤 支持文件上传和拖拽
- 📁 支持文件夹批量扫描
- 🖼️ 添加照片缩略图预览
- 📊 添加分类统计功能
- 🗂️ 添加废片自动整理功能
- 📄 添加报告导出功能
- 🔧 修复桌面端预览闪退问题

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目采用 [MIT](LICENSE) 许可证。

## 👨‍💻 作者

- **shenglihalisen**

---

> 💡 **提示**：首次使用建议先用小批量照片测试，确保功能符合预期后再处理大量照片。
