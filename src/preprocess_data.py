"""Transform raw data to train / val datasets """
import argparse
import logging
import pandas as pd

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='log/preprocess_data.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s')


IN_FILES = ['data/raw/cian_flat_sale_1_50_moskva_26_Apr_2024_14_08_32_338904.csv',
            'data/raw/cian_flat_sale_1_50_moskva_26_Apr_2024_14_15_43_988750.csv',
            'data/raw/cian_flat_sale_1_50_moskva_26_Apr_2024_14_22_17_675082.csv']

OUT_TRAIN = 'data/proc/train.csv'
OUT_VAL = 'data/proc/val.csv'

TRAIN_SIZE = 0.9
<<<<<<< HEAD
PRICE_THRESHOLD = 30_000_000
=======
>>>>>>> 194c62d94fc5690fff1a5395b67bd68f18a20f98


def main(args):
    main_dataframe = pd.read_csv(args.input[0], delimiter=';')
    for i in range(1, len(args.input)):
        data = pd.read_csv(args.input[i], delimiter=';')
        df = pd.DataFrame(data)
        main_dataframe = pd.concat([main_dataframe, df], axis=0)

    main_dataframe['url_id'] = main_dataframe['url'].map(lambda x: x.split('/')[-2])
    new_dataframe = main_dataframe[['url_id', 'total_meters', 'price']].set_index('url_id')

<<<<<<< HEAD
    new_df = new_dataframe[new_dataframe['price'] < PRICE_THRESHOLD]

    border = int(args.split * len(new_df))
    train_df, val_df = new_df[0:border], new_df[border:-1]
    if args.split == 1:
        train_df.to_csv(OUT_TRAIN)
    elif args.split == 0:
        val_df.to_csv(OUT_VAL)
    elif 0 < args.split < 1:
        train_df.to_csv(OUT_TRAIN)
        val_df.to_csv(OUT_VAL)
    else:
        raise "Wrong split test size!"

=======
    new_df = new_dataframe[new_dataframe['price'] < 30_000_000]

    border = int(args.split * len(new_df))
    train_df, val_df = new_df[0:border], new_df[border:-1]
    train_df.to_csv(OUT_TRAIN)
    val_df.to_csv(OUT_VAL)
>>>>>>> 194c62d94fc5690fff1a5395b67bd68f18a20f98
    logger.info(f'Write {args.input} to train.csv and val.csv. Train set size: {args.split}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--split', type=float, 
<<<<<<< HEAD
                        help='Split data, test relative size, from 0 to 1',
=======
                        help='Split test size',
>>>>>>> 194c62d94fc5690fff1a5395b67bd68f18a20f98
                        default=TRAIN_SIZE)
    parser.add_argument('-i', '--input', nargs='+',
                        help='List of input files', 
                        default=IN_FILES)
    args = parser.parse_args()
    main(args)
