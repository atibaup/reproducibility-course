"""Takes a csv data file and adds a queries column"""

if __name__== '__main__':
    import pandas as pd
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('car_data_file_in', type=str)
    parser.add_argument('car_data_file_out', type=str)


    args = parser.parse_args()

    car_make_data = pd.read_csv(args.car_data_file_in)

    # we build the queries we will use to search google images
    def cols_to_query(row):
        return ' '.join([str(row['year']), row['make'], row['model']]).lower()
                         
    car_make_data['queries'] = car_make_data.apply(cols_to_query, axis=1)

    car_make_data.to_csv(args.car_data_file_out)
