FROM jupyter/datascience-notebook:latest

# Create a Python 2.x environment using conda including at least the ipython kernel
# and the kernda utility.
RUN conda create --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 ipython kernda ipykernel && \
    conda clean -tipsy

USER root

# Create a global kernelspec in the image and modify it so that it properly activates
# the python2 conda environment.
RUN $CONDA_DIR/envs/python2/bin/python -m ipykernel install

RUN $CONDA_DIR/envs/python2/bin/pip install PyJWT==1.5.3

RUN $CONDA_DIR/envs/python2/bin/pip install websocket-client==0.47.0

USER $NB_USER
