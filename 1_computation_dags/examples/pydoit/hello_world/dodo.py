def task_hello_world():
	"""Creates a `hello.txt` file"""
	return {
	    'targets': ['hello.txt'],
	    'actions': ['echo "Hello world!" > %(targets)s'],
	}
