from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import normalize
import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier
# from sklearn.svm import LinearSVC
# from sklearn.feature_selection import SelectFromModel

class DataProcessing:
    """
    This class reduces component numbers into 12.
    The total explain variance ratio of data after pca is 99.98281%.
    """
    # change the data path
    DATA_PATH = "/Users/SiriusR/Desktop/data2.csv"

    def __init__(self):
        pass

    def pca(self):
        """
        This method normalize data first, then implement
        pca to normalized data. Use the result of this method
        as input to your RNN.
        :return: projected_data
        """
        data = self.read_data()
        target = data[:,-1]
        data = np.delete(data, -1, 1)
        data = normalize(data)
        # data = self.read_data()
        num_component = 12
        pca = PCA(n_components=num_component)
        pca.fit(data)
        projected_data = pca.transform(data)
        inverse_pca_data = DataProcessing.inverse_pca_data(data, pca)
        mse = mean_squared_error(data, inverse_pca_data)
        com = pca.components_
        total_ratio = 0.0
        print(projected_data.shape)
        for ratio in pca.explained_variance_ratio_:
            ratio = round((ratio * 100), 5)
            total_ratio += ratio
            print("{0}%".format(ratio))
        print(total_ratio)
        print(projected_data[:, 0])
        plt.figure()
        plt.scatter(projected_data[:, 2], projected_data[:, 3])
        plt.show()
        return projected_data

    def get_eigenvalue(self, data, pca):
        """
        This method prints eigenvalues of components
        in PCA
        :param data: The raw data
        :param pca: The pca model
        :return: None
        """
        data_centered = data - np.mean(data, axis=0)
        cov_matrix = np.dot(data_centered.T, data_centered) / len(data)
        eigenvalues = pca.explained_variance_
        for eigenvalue, eigenvector in zip(eigenvalues, pca.components_):
            print(np.dot(eigenvector.T, np.dot(cov_matrix, eigenvector)))
            print(eigenvalue)

    @staticmethod
    def inverse_pca_data(data, pca):
        """
        This method does inverse_pca, inverse components to
        original dims.
        :param data: raw data
        :param pca: pca model
        :return: inverse_pca_data
        """
        train_pca = pca.transform(data)
        inverse_pca_data = pca.inverse_transform(train_pca)
        return inverse_pca_data

    def reduce_features(self):
        data = self.read_data()
        target = data[:,-1]
        data = np.delete(data, -1, 1)
        # lsvc = LinearSVC(C=0.01, penalty="l1", dual=False).fit(data,target)
        # model = SelectFromModel(lsvc, prefit=True)
        # data_new = model.transform(data)
        # print(data_new.shape)


    def read_data(self):
        """
        This method reads data from csv file.
        :return: data
        """
        with open(self.DATA_PATH, 'r') as csv_file:
            reader = csv.reader(csv_file)
            rows = [row[1:] for row in reader]
        data = rows[1:]
        data = np.asarray(data, dtype=float)
        data = np.delete(data, -1, 1)
        return data


if __name__ == '__main__':
    dp = DataProcessing()
    # after_process_data = dp.pca()
    # dp.read_data()
    # dp.randomized_lasso()
    dp.reduce_features()