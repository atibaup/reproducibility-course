import matplotlib.pyplot as plt
import urllib.request


def display_from_url(url, ax=plt.gca()):
    with urllib.request.urlopen(url) as response:
        img = plt.imread(response, 0)
        return ax.imshow(img)


def display_from_path(path, ax=plt.gca()):
    with open(path, 'rb') as f:
        img = plt.imread(f, 0)
        return ax.imshow(img)