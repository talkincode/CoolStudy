# 使用 Mambaforge 基础镜像
FROM condaforge/mambaforge:latest

# 设置非交互式前端，避免 apt-get 交互式提示
ENV DEBIAN_FRONTEND=noninteractive

# 设置时区
RUN echo "Asia/Shanghai" > /etc/timezone && \
    ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    apt-get update && \
    apt-get install -y tzdata && \
    dpkg-reconfigure --frontend noninteractive tzdata

# 安装 Tesseract-OCR、Graphviz、字体以及 FFMPEG
RUN apt-get update && \
    apt-get install -y tesseract-ocr tesseract-ocr-chi-sim graphviz fonts-wqy-microhei fonts-noto ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY ./CoolStudy.py ./CoolStudy.py
COPY ./pages ./pages
COPY ./libs ./libs
COPY ./apps ./apps
COPY ./config.toml ./.streamlit/config.toml
COPY ./components ./components
COPY requirements.txt ./requirements.txt

# 安装项目依赖以及 OpenCV
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 Streamlit 默认端口
EXPOSE 8501

# 环境变量设置为非缓冲模式，以便实时输出
ENV PYTHONUNBUFFERED=1

# 设置启动命令
CMD ["streamlit","run", "CoolStudy.py", "--server.port=8501"]
