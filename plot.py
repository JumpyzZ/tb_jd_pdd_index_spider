import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.serif'] = ['SimHei']

import seaborn as sns
sns.set_style("darkgrid", {"font.sans-serif": ['simhei', 'Arial']})


def histPlot(good_list):
    """
    :param good_list: list of dict {"keyword":"XX", "platform":"XX", "price":10.1}
    :return: None, save plot to hist.png
    """
    data_for_pd = [[i["keyword"], i["platform"], i["price"]] for i in good_list]
    df = pd.DataFrame(np.array(data_for_pd), columns=["keyword", "platform", "price"])
    df.price = df.price.astype(float)
    df.platform = df.platform.astype(str)
    df.keyword = df.keyword.astype(str)
    df = df[:-int(len(good_list)*0.05)]

    sns.histplot(data=df, x="price", hue="platform", element="step")
    plt.title('价格分布直方图 ({k})'.format(k=good_list[0]["keyword"]))
    plt.savefig('hist.png', bbox_inches='tight', pad_inches=0.1)


def boxPlot(good_list):
    """
    :param good_list: list of dict {"keyword":"XX", "platform":"XX", "price":10.1}
    :return: None, save plot to hist.png
    """
    data_for_pd = [[i["keyword"], i["platform"], i["price"]] for i in good_list]
    df = pd.DataFrame(np.array(data_for_pd), columns=["keyword", "platform", "price"])
    df.price = df.price.astype(float)
    df.platform = df.platform.astype(str)
    df.keyword = df.keyword.astype(str)
    df = df[:-int(len(good_list)*0.05)]

    sns.boxplot(x="platform", y="price", data=df, palette=sns.color_palette("husl", 3))
    sns.swarmplot(x="platform", y="price", data=df, color=".25")
    plt.title('价格箱型图 ({k})'.format(k=good_list[0]["keyword"]))
    plt.savefig('box.png', bbox_inches='tight', pad_inches=0.1)


if __name__ == '__main__':
    pass
