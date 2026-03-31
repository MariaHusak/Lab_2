FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-venv \
        python3-pip \
        libgl1 \
        libegl1 \
        libgles2 \
        libglib2.0-0 \
        libdbus-1-3 \
        libxkbcommon0 \
        libx11-xcb1 \
        libxcb1 \
        libxrender1 \
        libxi6 \
        libfontconfig1 \
        libasound2 \
        libpulse0 \
        libxcb-render0 \
        libxcb-shape0 \
        libxcb-xfixes0 \
        libxcb-keysyms1 \
        libxrandr2 \
        libxss1 \
        libxtst6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER jenkins
