# DS Template

This is a simple Cookiecutter template and the solution to the Playtime exercise from the
"Environment Management" section of the Reproducibility part of the course.
 
 
## Requirements
* conda (for example: miniconda3)
* cookiecutter

Alternatively, you can just use the provided `ml_in_prod` course environment, which include
the above dependencies among others.

## Usage

```bash
cookiecutter ds_template
```
This will prompt a number of questions, namely:

```bash
project_name [My New Project]: 
project_description [Description of my New Project]: 
project_slug [my-new-project]: 
conda_channels [conda-forge defaults]: 
python_version [3.7]: 
dependencies []: 
```

This will create a directory with the `project_slug` name, in the same folder (unless you pass the `-o` parameter). The 
directory will contain a number of directories and files, among which a `Makefile` 
with a few preset targets. To view them, run:

```bash
# cd into the project folder
make
```

If you want to start working on your project, first run

```bash
make setup
```

which will create a conda environment with the specified dependencies and register a jupyter kernel
with that environment. Once the environment is created, you can add packages

```bash
conda activate $YOUR_PROJECT_SLUG
conda install ...
```
and then export the environment for future use via:
```bash
make export_env
```
