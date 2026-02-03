# sumi-video-converter
小苏米表盘专用视频处理工具  
解决「自定义视频替换原表盘jar文件后无法播放」的问题（适配表盘加密规则+视频参数规范）


##  核心功能
1. **视频标准化转换**：自动将视频调整为小苏米表盘兼容的参数（454x454分辨率、30帧率、2M码率）
2. **表盘视频加密**：通过异或算法加密视频，适配小苏米表盘的解析规则（解密与加密逻辑一致）
3. **批量处理**：支持多视频文件的批量加密/解密
4. **灵活操作**：支持「单文件处理（转换+加密）」「仅转换视频」「自定义参数配置」


##  环境要求
1. **Python 3.6+**：脚本基于Python标准库开发，无需额外安装第三方依赖
2. **FFmpeg**：视频转换功能依赖FFmpeg，需提前安装：
   - **Windows**：下载[FFmpeg安装包](https://ffmpeg.org/download.html)，并将其路径添加到系统环境变量
   - **Linux**：执行 `sudo apt install ffmpeg`
   - **macOS**：执行 `brew install ffmpeg`
   - **Android（Termux）**：执行 `pkg install ffmpeg`


##  快速使用
1. **克隆仓库**（或直接下载脚本）：
   ```bash
   git clone https://github.com/JinBeiCN/sumi-video-converter.git
   cd sumi-video-converter
