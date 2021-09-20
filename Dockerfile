FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit=2021.03.5
RUN pip install git+https://github.com/bp-kelley/descriptastorus==1.1.0
RUN pip install tqdm==4.62.2
RUN pip install typed-argument-parser==1.6.1
RUN pip install scikit-learn==0.22.2
RUN pip install torch==1.9.1
RUN pip install pandas==1.3.3

WORKDIR /repo
COPY . /repo
