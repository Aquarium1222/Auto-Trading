import numpy as np
import matplotlib.pyplot as plt

from config import *
from dataset.preprocessor import Preprocessor
from dataset.stock_dataset import StockDataset
from dataset.data_slicer import DataSlicer
from model.svr_stock import SVRStock
from strategy.stock_context import StockContext
from strategy.stock_state import *


# You can write code above the if-main block.
def predict_2_step(model, x):
    if len(x.shape) == 1:
        x = np.expand_dims(x, axis=0)
    pred_step1 = model.predict(x)
    x_step2 = np.insert(x, Hp.SVR_X_LEN, pred_step1, axis=1)
    x_step2 = np.delete(x_step2, 0, axis=1)
    pred_step2 = model.predict(x_step2)
    return [pred_step1, pred_step2]


def reverse_2_step(preprocessor, preds):
    r_preds = [np.squeeze(preprocessor.reverse(np.expand_dims(pred, axis=1))) for pred in preds]
    return r_preds


if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                        default='training_data.csv',
                        help='input training data file name')
    parser.add_argument('--testing',
                        default='testing_data.csv',
                        help='input testing data file name')
    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')
    args = parser.parse_args()

    preprocessor = Preprocessor(Constant.Method.SVR)
    dataset = StockDataset(preprocessor, 'data/training.csv', 'data/testing.csv')
    data_slicer = DataSlicer(dataset)
    model = SVRStock(dataset, data_slicer)
    model.train()
    val_x, val_y = data_slicer.val_datas
    pred_y = model.predict(val_x)
    val_y = preprocessor.reverse(np.expand_dims(val_y, axis=1))
    pred_y = preprocessor.reverse(np.expand_dims(pred_y, axis=1))

    preds = []
    for x in val_x:
        preds.append(reverse_2_step(preprocessor, predict_2_step(model, x)))

    stock_context = StockContext()

    val_x = preprocessor.reverse(val_x)
    profit = 0
    prev_pred = 0
    for i, (pred_2_step, today_price, real_tmr_price) in enumerate(zip(preds, np.array(val_x)[:, -1], val_y)):
        base_price = today_price if stock_context.state == Constant.State.Nothing else stock_context.stock_price
        action = stock_context.action(base_price, pred_2_step[0], pred_2_step[1])
        if action == Constant.Action.Sell:
            profit += real_tmr_price
        if action == Constant.Action.Buy:
            profit -= real_tmr_price
        if action == Constant.Action.Buy or action == Constant.Action.Sell:
            stock_context.stock_price = real_tmr_price

        if i == len(preds) - 1 and stock_context.state == Constant.State.Hold:
            profit += 153.42
        if i == len(preds) - 1 and stock_context.state == Constant.State.Short:
            profit -= 153.42

        print('Base price: {}\n'
              'Real tomorrow price: {}\n'
              'Predict tomorrow price: {}\n'
              'Predict after tomorrow price: {}\n'
              'Action: {}\n'
              'Profit: {}\n'
              'State: {}\n\n'.format(base_price, real_tmr_price, pred_2_step[0], pred_2_step[1], action, profit, stock_context.state))

        plt.plot(range(i, i + 2), pred_2_step)

    plt.plot(range(len(val_y)), val_y)
    plt.plot(range(len(val_y)), pred_y)
    plt.show()

    # The following part is an example.
    # You can modify it at will.
    # training_data = load_data(args.training)
    # trader = Model()
    # trader.train(training_data)
    #
    # testing_data = load_data(args.testing)
    # with open(args.output, 'w') as output_file:
    #     for row in testing_data:
    #         # We will perform your action as the open price in the next day.
    #         action = trader.predict_action(row)
    #         output_file.write(action)
    #
    #         # this is your option, you can leave it empty.
    #         trader.re_training(i)

