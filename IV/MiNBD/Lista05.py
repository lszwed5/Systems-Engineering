import pandas as pd
import numpy as np
from sklearn import preprocessing, decomposition
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
from sklearn import datasets


# ----------------------------------- DRY ----------------------------------- #

"------------------------------------ DRY ------------------------------------"


def stand_and_pca_to_2_dim_df(X, Y):
    stand_X = np.array(preprocessing.StandardScaler().fit_transform(X))

    pca = decomposition.PCA(n_components=2)
    new_X = pca.fit_transform(stand_X)
    new_X_df = pd.DataFrame(data=new_X, columns=['Component 1', 'Component 2'])
    final_df = pd.concat([new_X_df, Y], axis=1)

    return final_df


def stand_and_lda_to_data_and_classes(X, Y, fit='Y'):
    stand_target = preprocessing.StandardScaler().fit_transform(
        Y.to_numpy().reshape(-1, 1)).T[0]

    names = [str(i) for i in range(1, 11)]
    classes, quantiles = pd.cut(stand_target, bins=10,
                                labels=names, retbins=True)

    lda = LinearDiscriminantAnalysis()

    if fit == 'Y':
        data_plot = lda.fit_transform(X, Y)
    else:
        data_plot = lda.fit_transform(X, classes)

    return data_plot, classes, names


def svd_to_2_dim_df(X, Y):
    svd = decomposition.TruncatedSVD(n_components=2, random_state=42)
    new_X = svd.fit_transform(X)
    new_X_df = pd.DataFrame(data=new_X, columns=['Component 1', 'Component 2'])
    final_df = pd.concat([new_X_df, Y], axis=1)

    return final_df


def targets_to_bins(df, bins_card, target_name='target'):
    target = df[[target_name]].to_numpy()
    stand_target = preprocessing.StandardScaler().fit_transform(
        target).T[0]

    names = [str(i) for i in range(1, bins_card + 1)]
    classes, quantiles = pd.cut(stand_target, bins=bins_card,
                                labels=names, retbins=True)

    classes = pd.DataFrame(classes, columns=[target_name])
    final_df = pd.concat([df[['Component 1', 'Component 2']],
                                   classes], axis=1)

    return final_df, names


def plot_2_dim_df(dataframe, classes_names, colors=None, name='',
                  target_name='target', method='PCA'):
    if colors:
        if len(classes_names) != len(colors):
            raise IndexError("The size of classes_names and colors "
                             "parameters must be the same")

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('Component 1')
    ax.set_ylabel('Component 2')
    ax.set_title(f'2 Component {name} {method}')

    classes = [i for i in range(len(classes_names))]
    if colors:
        for target, color in zip(classes, colors):
            i = dataframe[target_name] == target
            ax.scatter(dataframe.loc[i, 'Component 1'],
                       dataframe.loc[i, 'Component 2'],
                       c=color, s=50)
    else:
        for target in classes_names:
            i = dataframe[target_name] == target
            ax.scatter(dataframe.loc[i, 'Component 1'],
                       dataframe.loc[i, 'Component 2'])

    ax.legend(classes_names)
    ax.grid()
    plt.show()


def plot_lda_2_dim(plot_data, Y, colors=None, names=None, title_name='',
                   target_names=[]):
    plt.figure()
    if colors and names:
        for color, i, name in zip(colors, [0, 1, 2], names):
            plt.scatter(plot_data[Y == i, 0], plot_data[Y == i, 1],
                        alpha=.8,
                        color=color, label=name)
    else:
        for target in target_names:
            plt.scatter(plot_data[Y == target, 0],
                        plot_data[Y == target, 1],
                        alpha=.8, label=target)

    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.title(f'2 Component {title_name} LDA')
    plt.grid()
    plt.show()


"----------------------------------- Zad 1 -----------------------------------"

# ---------------------------------- Iris ---------------------------------- #

iris_X, iris_Y = datasets.load_iris(return_X_y=True, as_frame=True)

iris_df = stand_and_pca_to_2_dim_df(iris_X, iris_Y)

plot_2_dim_df(iris_df,
              classes_names=['Iris Setoza', 'Iris Versicolor',
                             'Iris Virginica'],
              colors=('r', 'g', 'b'),
              name='Iris')

# ---------------------------------- Wine ---------------------------------- #

wine_X, wine_Y = datasets.load_wine(return_X_y=True, as_frame=True)

wine_df = stand_and_pca_to_2_dim_df(wine_X, wine_Y)

plot_2_dim_df(wine_df, classes_names=[0, 1, 2], colors=('r', 'g', 'b'),
              name='Wine')

# -------------------------------- Diabetes -------------------------------- #

diabetes_X, diabetes_Y = datasets.load_diabetes(return_X_y=True, as_frame=True)

diabetes_df = stand_and_pca_to_2_dim_df(diabetes_X, diabetes_Y)

diabetes_final_df, db_names = targets_to_bins(diabetes_df, bins_card=10)

plot_2_dim_df(diabetes_final_df, classes_names=db_names, name='Diabetes')


"----------------------------------- Zad 2 -----------------------------------"

# --------------------------- California Housing --------------------------- #

housing_X, housing_Y = datasets.fetch_california_housing(
    return_X_y=True, as_frame=True)

housing_df = stand_and_pca_to_2_dim_df(housing_X, housing_Y)

housing_final_df, h_names = targets_to_bins(housing_df, bins_card=10,
                                            target_name='MedHouseVal')

plot_2_dim_df(housing_final_df, classes_names=h_names, name='Housing',
              target_name='MedHouseVal')

# --------------------------- Forest Cover types --------------------------- #

forest_X, forest_Y = datasets.fetch_covtype(return_X_y=True, as_frame=True)

forest_df = stand_and_pca_to_2_dim_df(forest_X, forest_Y)

# print(set([float(val) for val in forest_df[['Cover_Type']].to_numpy()]))
plot_2_dim_df(forest_df, classes_names=[1, 2, 3, 4, 5, 6, 7], name='Forest',
              target_name='Cover_Type')


"----------------------------------- Zad 3 -----------------------------------"

# ---------------------------------- Iris ---------------------------------- #

iris_X, iris_Y = datasets.load_iris(return_X_y=True, as_frame=True)

# stand_X = np.array(preprocessing.StandardScaler().fit_transform(iris_X))

lda = LinearDiscriminantAnalysis()
data_plot = lda.fit_transform(iris_X, iris_Y)
target_names = ['Iris Setoza', 'Iris Versicolor', 'Iris Virginica']

plot_lda_2_dim(data_plot, iris_Y, colors=('r', 'g', 'b'), names=target_names,
               title_name='Iris')

# ---------------------------------- Wine ---------------------------------- #

wine_X, wine_Y = datasets.load_wine(return_X_y=True, as_frame=True)

# stand_X = np.array(preprocessing.StandardScaler().fit_transform(wine_X))

lda = LinearDiscriminantAnalysis()
data_plot = lda.fit_transform(wine_X, wine_Y)
target_names = [0, 1, 2]

plot_lda_2_dim(data_plot, wine_Y, colors=('r', 'g', 'b'), names=target_names,
               title_name='Wine')

# -------------------------------- Diabetes -------------------------------- #

diabetes_X, diabetes_Y = datasets.load_diabetes(return_X_y=True, as_frame=True)

data_plot, classes, names = stand_and_lda_to_data_and_classes(diabetes_X,
                                                              diabetes_Y)

plot_lda_2_dim(data_plot, classes, title_name='Diabetes', target_names=names)

# --------------------------- California Housing --------------------------- #

housing_X, housing_Y = datasets.fetch_california_housing(
    return_X_y=True, as_frame=True)

data_plot, classes, names = stand_and_lda_to_data_and_classes(housing_X,
                                                              housing_Y,
                                                              fit='classes')

plot_lda_2_dim(data_plot, classes, title_name='Housing', target_names=names)

# --------------------------- Forest Cover types --------------------------- #

forest_X, forest_Y = datasets.fetch_covtype(return_X_y=True, as_frame=True)

data_plot, classes, names = stand_and_lda_to_data_and_classes(forest_X,
                                                              forest_Y,
                                                              fit='classes')

plot_lda_2_dim(data_plot, classes, title_name='Forest', target_names=names)


"----------------------------------- Zad 4 -----------------------------------"

# ---------------------------------- Iris ---------------------------------- #

iris_X, iris_Y = datasets.load_iris(return_X_y=True, as_frame=True)

iris_df = svd_to_2_dim_df(iris_X, iris_Y)

plot_2_dim_df(iris_df,
              classes_names=['Iris Setoza', 'Iris Versicolor',
                             'Iris Virginica'],
              colors=('r', 'g', 'b'),
              name='Iris', method='SVD')

# ---------------------------------- Wine ---------------------------------- #

wine_X, wine_Y = datasets.load_wine(return_X_y=True, as_frame=True)

wine_df = svd_to_2_dim_df(wine_X, wine_Y)

plot_2_dim_df(wine_df, classes_names=[0, 1, 2], colors=('r', 'g', 'b'),
              name='Wine', method='SVD')

# -------------------------------- Diabetes -------------------------------- #

diabetes_X, diabetes_Y = datasets.load_diabetes(return_X_y=True, as_frame=True)

diabetes_df = svd_to_2_dim_df(diabetes_X, diabetes_Y)

diabetes_final_df, db_names = targets_to_bins(diabetes_df, bins_card=10)

plot_2_dim_df(diabetes_final_df, classes_names=db_names,
              name='Diabetes', method='SVD')

# --------------------------- California Housing --------------------------- #

housing_X, housing_Y = datasets.fetch_california_housing(
    return_X_y=True, as_frame=True)

housing_df = svd_to_2_dim_df(housing_X, housing_Y)

housing_final_df, h_names = targets_to_bins(housing_df, bins_card=10,
                                            target_name='MedHouseVal')

plot_2_dim_df(housing_final_df, classes_names=h_names, name='Housing',
              target_name='MedHouseVal', method='SVD')

# --------------------------- Forest Cover types --------------------------- #

forest_X, forest_Y = datasets.fetch_covtype(return_X_y=True, as_frame=True)

forest_df = svd_to_2_dim_df(forest_X, forest_Y)

plot_2_dim_df(forest_df, classes_names=[1, 2, 3, 4, 5, 6, 7], name='Forest',
              target_name='Cover_Type', method='SVD')

"-----------------------------------------------------------------------------"
