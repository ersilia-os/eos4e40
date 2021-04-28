FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit
RUN pip install git+https://github.com/bp-kelley/descriptastorus
RUN pip install chemprop==1.3.0

WORKDIR /repo
COPY . /repo
