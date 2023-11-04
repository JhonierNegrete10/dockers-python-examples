FROM python:3.9-slim-buster

# Install all OS dependencies for fully functional Server
RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
#     # Common useful utilities
#     curl \
    git \
#     nano-tiny \
#     tzdata \
#     unzip \
#     vim-tiny \
#     # git-over-ssh
#     openssh-client \
#     # less is needed to run help in R
#     # see: https://github.com/jupyter/docker-stacks/issues/1588
#     less \
#     # nbconvert dependencies
#     # https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex
#     texlive-xetex \
#     texlive-fonts-recommended \
#     texlive-plain-generic \
#     # Enable clipboard on Linux host systems
#     xclip && \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# # Create alternative for nano -> nano-tiny
# RUN update-alternatives --install /usr/bin/nano nano /bin/nano-tiny 10

WORKDIR /app

COPY src/requirements.txt .

# Enable venv
# ENV PATH="/build/venv/bin:$PATH"
# Install Jupyter lab
RUN pip install jupyter ipywidgets jupyterlab

RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 8888 para el acceso a Jupyter
EXPOSE 8888

# Iniciar el servidor de Jupyter
CMD ["jupyter", "lab", "--port=8888", "--ip=0.0.0.0", "--allow-root","--no-browser"]