# Visual Search conda environment

In the playtime exercise from the [previous section](../../../1_computation_dags/playtime/visual_search), 
we built a simple Visual Search pipeline. That pipeline relied on a number of
dependencies that at the time we probably installed directly on the 
course's environment (`ml_in_prod`).

This is not usually a good practice - it is preferable to have isolated environments
for each project so that dependency resolutions are performed on a smaller subset
of packages.

Let's build a dedicated environment for that project:

```bash
conda create -n visual_search python=3 numpy keras tensorflow pillow notebook
```

One of the packages (faiss) is only available at the `pytorch` channel,
so the simplest way to install it is to run:

```bash
conda activate visual_search
conda install -c pytorch faiss-cpu
``` 

There's one more package that is only available via pip, so we install it last
to reduce the risk of breaking of

```bash
conda activate visual_search
pip install google_images_download
```

We now register a ipython kernel so that the notebooks run on a kernel within the created environment:

```bash
conda activate visual_search
ipython kernel install --user --name="visual_search"
```

Now we're ready to export the environment:
```bash
conda env export --no-builds > visual_search.yml
```

Remember that if you want to remove the environment at some point, it suffices to run:

```bash
conda deactivate # if env is active we won't be able to remove it :)
conda env remove -n visual_search
```