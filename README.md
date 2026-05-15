# 照片自动分类工具

智能检测损坏、空镜、闭眼、模糊、遮挡等缺陷照片，一键整理您的相册。

## 功能特性

- **5 种缺陷检测**：损坏、空镜、闭眼、模糊、遮挡
- **双端支持**：PyQt5 桌面端 + Flask Web 端
- **两种模式**：自动模式（一键处理）/ 手动确认（逐张审核）
- **批量处理**：支持文件夹批量扫描
- **灵活操作**：自动将废片按缺陷类型分类到子文件夹

## 支持的图片格式

JPG、JPEG、PNG、BMP、TIFF、WebP、GIF、HEIC、HEIF

## 安装

### 从源码运行

```bash
# 克隆仓库
git clone https://github.com/shenglihalisen/photo-classifier.git
cd photo-classifier

# 安装依赖
pip install -r requirements.txt

# 运行桌面端
python run_desktop.py

# 运行 Web 端
python run_web.py
```

Web 端启动后访问 http://localhost:5000

### 下载发行版

前往 [Releases](https://github.com/shenglihalisen/photo-classifier/releases) 页面下载对应平台的可执行文件。

- `PhotoClassifier-Desktop.exe` — 桌面端
- `PhotoClassifier-Web.exe` — Web 端

## 使用方法

### Web 端

1. 打开浏览器访问 `http://localhost:5000`
2. 选择「上传文件」或「选择文件夹」
3. 选择扫描模式（自动 / 手动确认）
4. 点击「开始扫描」
5. 查看结果，对废片进行移动或删除操作

### 桌面端

1. 运行 `PhotoClassifier-Desktop.exe` 或 `python run_desktop.py`
2. 选择要扫描的文件夹
3. 等待扫描完成
4. 查看分类结果并处理废片

## 项目结构

```
photo-classifier/
├── classifiers/          # 缺陷检测器
│   ├── base.py           # 基类和类型定义
│   ├── corrupted.py      # 损坏检测
│   ├── empty.py          # 空镜检测
│   ├── blink.py          # 闭眼检测
│   ├── blur.py           # 模糊检测
│   └── obstruction.py    # 遮挡检测
├── engine/               # 分类引擎
│   └── classifier.py     # 统一分类引擎
├── desktop/              # 桌面端
│   └── app.py            # PyQt5 界面
├── web/                  # Web 端
│   ├── app.py            # Flask 应用
│   └── templates/        # HTML 模板
├── run_desktop.py        # 桌面端入口
├── run_web.py            # Web 端入口
├── requirements.txt      # Python 依赖
└── CHANGELOG.md          # 更新日志
```

## 技术栈

- **图像处理**：OpenCV、MediaPipe、Pillow、NumPy
- **桌面端**：PyQt5
- **Web 端**：Flask + Layui
- **打包**：PyInstaller

## 更新日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解详细更新记录。

## 许可证

MIT License
