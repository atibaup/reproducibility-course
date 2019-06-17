.PHONY: setup_env
setup_env:
	conda env create -f {{cookiecutter.project_slug}}.yml

.PHONY: export_env
export_env: ## Exports conda environment
	conda activate {{ cookiecutter.project_slug }} && conda env export --no-builds > {{ cookiecutter.project_slug }}.yml

.PHONY: setup_jupyter_kernel
setup_jupyter_kernel: setup_env
	ipython kernel install --user --name="{{ cookiecutter.project_slug }}" && \
	echo "Jupyter kernel registered under the name: {{ cookiecutter.project_slug }}" ;

setup: setup_jupyter_kernel ## Sets up conda environment

.PHONY: test_setup
test_setup: ## Runs a few tests to check environment setup
	./scripts/test_env.sh

SHELL=./scripts/shell_w_env.sh

.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
