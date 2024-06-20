"""Train model and save checkpoint"""

import argparse
import logging
import pandas as pd
from catboost import CatBoostRegressor, Pool
from sklearn.metrics import mean_absolute_error
from joblib import dump

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='log/train_model.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s')

TRAIN_DATA = 'data/proc/train.csv'
VAL_DATA = 'data/proc/val.csv'
MODEL_SAVE_PATH = 'models/catboost_v01.joblib'


def main(args):
    df_train = pd.read_csv(TRAIN_DATA)
    x_train = df_train[['total_meters']]
    y_train = df_train['price']
    
    df_val = pd.read_csv(VAL_DATA)
    x_val = df_val[['total_meters']]
    y_val = df_val['price']

    catboost_model = CatBoostRegressor(
        iterations=1000,
        learning_rate=0.1,
        depth=6,
        loss_function='MAE',
        verbose=100
    )
    catboost_model.fit(x_train, y_train, eval_set=(x_val, y_val), use_best_model=True)
    dump(catboost_model, args.model)
    logger.info(f'Модель сохранена по пути {args.model}')

    r2 = catboost_model.score(Pool(x_train, y_train))
    y_pred = catboost_model.predict(x_val)
    mae = mean_absolute_error(y_pred, y_val)

    logger.info(f'R2 = {r2:.3f}     MAE = {mae:.0f}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model', 
                        default=MODEL_SAVE_PATH)
    args = parser.parse_args()
    main(args)
