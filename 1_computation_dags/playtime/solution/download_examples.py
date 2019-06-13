""" Downloads image samples for each car model via querying Google Images """

if __name__== '__main__':
    import pandas as pd
    from time import time
    from google_images_download import google_images_download
    from os import path
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('car_data_path', type=str)
    parser.add_argument('output_directory', type=str)
    parser.add_argument('n_samples', type=int)
    parser.add_argument('n_images_per_sample', type=int)

    args = parser.parse_args()

    car_make_data = pd.read_csv(args.car_data_path)

    # now we retrieve images from google images using the
    # `google_images_download` python package

    client = google_images_download.googleimagesdownload()

    sample_queries = car_make_data['queries'].sample(args.n_samples,
        random_state=42)

    query_to_paths = {}
    for (i, (_, query)) in enumerate(sample_queries.iteritems()):
        arguments = {
            "keywords": query,
            "limit": args.n_images_per_sample,
            "size": "medium",
            "format": "png",
            "output_directory": args.output_directory
        }
        start_time = time()
        paths, n_downloaded = client.download(arguments)

        query_to_paths[query] = [p for path_list in paths.values() for p in path_list]

        print('Downloaded {} images for `{}` ({}/{}) in {:.2f}s'.format(
            n_downloaded, query, i, args.n_samples, time() - start_time))

    pd.DataFrame.from_records(
        [(k, v) for k in query_to_paths.keys() for v in query_to_paths[k]]
    ).to_csv(path.join(args.output_directory, 'examples_paths.csv'))