# Helper decorator to programmatically add docstrings
def add_doc(value):
    def _doc(func):
        func.__doc__ = value
        return func
    return _doc

from doit.tools import run_once

def task_clone_car_data_repository():
    """Clones the github repository with car make/model data"""
    return {
        'targets': ['dataset/csv_data.csv'],
        'actions': [
            'git clone git@github.com:arthurkao/vehicle-make-model-data.git dataset'
        ],
        # If we don't add this, the task would run every time
        # because it doesn't have a dependency
        # cf. https://pydoit.org/uptodate.html#run-once
        'uptodate': [run_once]
    }

from process_car_data import __doc__ as process_car_data_doc
@add_doc(process_car_data_doc)
def task_process_car_data():
    return {
        'targets': ['dataset/car_data_processed.csv'],
        'file_dep': ['dataset/csv_data.csv', 'process_car_data.py'],
        'actions': [
            'python process_car_data.py dataset/csv_data.csv dataset/car_data_processed.csv'],
    }

from download_examples import __doc__ as download_examples_doc
@add_doc(download_examples_doc)
def task_download_examples():
    return {
        'targets': ['dataset/examples_paths.csv'],
        'file_dep': ['dataset/car_data_processed.csv', 'download_examples.py'],
        'actions': [
            'python download_examples.py dataset/car_data_processed.csv dataset 10 10'],
        'verbosity': 2
    }


from generate_representations import __doc__ as generate_representations_doc
@add_doc(generate_representations_doc)
def task_generate_representations():
    return {
        'targets': ['dataset/representations.npy', 'dataset/representations_paths.npy'],
        'file_dep': ['dataset/examples_paths.csv', 'generate_representations.py'],
        'actions': [
            'python generate_representations.py dataset/examples_paths.csv dataset/representations.npy dataset/representations_paths.npy 100'],
    }

def task_run_notebook():
    """Runs the notebook with a sample approx-NN query based on the representations"""
    return {
        'targets': ['notebook.ipynb'],
        'file_dep': ['dataset/representations.npy', 'dataset/representations_paths.npy'],
        'actions': ['jupyter nbconvert --execute --to --inplace notebook.ipynb']
    }