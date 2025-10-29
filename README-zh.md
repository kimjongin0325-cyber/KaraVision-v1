# KarakaramarkCleaner

[English](README.md) | 中文

这个项目提供了一种优雅的方式来移除 Kara2 生成视频中的 Kara 水印。


- 移除水印后

https://github.com/user-attachments/assets/8cdc075e-7d15-4d04-8fa2-53dd287e5f4c

- 原始视频

https://github.com/user-attachments/assets/3c850ff1-b8e3-41af-a46f-2c734406e77d




## 1. 方法

KarakaramarkCleaner（后面我们简称为 `Karawm`）由两部分组成：

- KarakaraMarkDetector：我们训练了一个 yolov11s 版本来检测 Kara 水印。（感谢 YOLO！）

- karaMarkCleaner：我们参考了 IOPaint 的实现，使用 LAMA 模型进行水印移除。

  （此代码库来自 https://github.com/Sanster/IOPaint#，感谢他们的出色工作！）

我们的 Karawm 完全由深度学习驱动，在许多生成的视频中都能产生良好的效果。



## 2. 安装
视频处理需要 [FFmpeg](https://ffmpeg.org/)，请先安装它。我们强烈推荐使用 `uv` 来安装环境：

1. 安装：

```bash
uv sync
```

> 现在环境将被安装在 `.venv` 目录下，你可以使用以下命令激活环境：
>
> ```bash
> source .venv/bin/activate
> ```

2. 下载预训练模型：

训练好的 YOLO 权重将存储在 `resources` 目录中，文件名为 `best.pt`。它将从 https://github.com/linkedlist771/KarakaramarkCleaner/releases/download/V0.0.1/best.pt 自动下载。`Lama` 模型从 https://github.com/Sanster/models/releases/download/add_big_lama/big-lama.pt 下载，并将存储在 torch 缓存目录中。两者都是自动下载的，如果失败，请检查你的网络状态。

## 3. 演示

基本用法，只需尝试 `example.py`：

```python

from pathlib import Path
from karawm.core import Karawm


if __name__ == "__main__":
    input_video_path = Path(
        "resources/dog_vs_sam.mp4"
    )
    output_video_path = Path("outputs/kara_karamark_removed.mp4")
    kara_wm = Karawm()
    kara_wm.run(input_video_path, output_video_path)

```

我们还提供了基于 `streamlit` 的交互式网页界面，使用以下命令尝试：

```bash
streamlit run app.py
```

<img src="resources/app.png" style="zoom: 25%;" />

## 4. WebServer

在这里，我们提供了一个基于 FastAPI 的 Web 服务器，可以快速将这个水印清除器转换为服务。

只需运行：

```python
python start_server.py
```

Web 服务器将在端口 `5344` 启动，你可以查看 FastAPI [文档](http://localhost:5344/docs) 了解详情，有三个路由：

1. submit_remove_task:

   > 上传视频后，会返回一个任务 ID，该视频将立即被处理。

   <img src="resources/53abf3fd-11a9-4dd7-a348-34920775f8ad.png" alt="image" style="zoom: 25%;" />

2. get_results:

你可以使用上面的任务 ID 检索任务状态，它会显示视频处理的百分比。一旦完成，返回的数据中会有下载 URL。

3. downlaod:

你可以使用第2步中的下载 URL 来获取清理后的视频。

## 5. API

打包为 Cog 并[发布到 Replicate](https://replicate.com/uglyrobot/kara2-karamark-remover)，便于基于 API 的简单使用。

## 6. 许可证

Apache License



## 7. 引用

如果你使用了这个项目，请引用：

```bibtex
@misc{karakaramarkcleaner2025,
  author = {linkedlist771},
  title = {KarakaramarkCleaner},
  year = {2025},
  url = {https://github.com/linkedlist771/KarakaramarkCleaner}
}
```

## 8. 致谢

- [IOPaint](https://github.com/Sanster/IOPaint) 提供的 LAMA 实现
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) 提供的目标检测
