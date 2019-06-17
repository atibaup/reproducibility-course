#!/bin/bash

ENV_EXISTS=$(conda env list | grep "{{ cookiecutter.project_slug }}")

preaction()
{
	if [[ $ENV_EXISTS ]]; then
      source /anaconda3/bin/activate {{ cookiecutter.project_slug }}
    fi
}

postaction()
{
	if [[ $ENV_EXISTS ]]; then
      deactivate 2> /dev/null || true
    fi
}

preaction && /bin/bash "$@" && postaction