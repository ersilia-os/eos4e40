FROM bentoml/model-server:0.11.0-py39
MAINTAINER ersilia

RUN pip install rdkit
RUN pip install git+https://github.com/bp-kelley/descriptastorus.git@d552f934757378a61dd1799cdb589a864032cd1b
RUN pip install tqdm>=4.62.2
RUN pip install typed-argument-parser==1.6.1
RUN pip install scikit-learn
RUN pip install torch
RUN pip install pandas==2.2.2
RUN pip install scipy==1.7.1
RUN pip install numpy==1.22.4
RUN pip install xarray==2022.3.0

WORKDIR /repo
COPY . /repo
