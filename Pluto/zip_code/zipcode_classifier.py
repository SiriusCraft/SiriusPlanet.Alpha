from sklearn import neighbors
from sklearn.naive_bayes import GaussianNB
from numpy import *


class zipcodeClassifier:
    def prepare_data(self):
        data = loadtxt('/Users/SiriusR/Downloads/zip.train')
        test_data = loadtxt('/Users/SiriusR/Downloads/zip.test')
        self.number = data[:, 0]
        self.grayscale = []
        self.validation_grayscale = []
        for _ in data:
            self.grayscale.append(_[1:256])
        validation_num = int(0.1 * len(self.number))
        self.validation_number = self.number[10:validation_num]
        for i in range(10, validation_num):
            self.validation_grayscale.append(self.grayscale[i])
        self.test_number = test_data[:, 0]
        self.test_grayscale = []
        for _ in test_data:
            self.test_grayscale.append(_[1:256])

    def getKey(self, item):
        return item[1]

    def get_knn_k(self):
        knn_result = []
        for k in range(1, 10):
            knn = neighbors.KNeighborsClassifier(n_neighbors=k)
            accuracy = knn.fit(self.grayscale, self.number).score(self.validation_grayscale, self.validation_number)
            k_reult = [k, accuracy]
            knn_result.append(k_reult)
        sk = sorted(knn_result, key=self.getKey)
        top5_k = []
        for i in range(1, 6):
            top5_k.append(sk[-i][0])
        return top5_k

    def knn_test(self):
        for k in self.get_knn_k():
            knn = neighbors.KNeighborsClassifier(n_neighbors=k)
            test_error = 1 - knn.fit(self.grayscale, self.number).score(self.test_grayscale, self.test_number)
            print('k = {0}   test error = {1}%'.format(k, test_error * 100))

    def knn(self):
        self.prepare_data()
        self.get_knn_k()
        self.knn_test()

    def gaussian(self):
        self.prepare_data()
        gaussian = GaussianNB()
        test_error = 1 - gaussian.fit(self.grayscale, self.number).score(self.test_grayscale, self.test_number)
        print('gaussian test_error = {0}%'.format(test_error * 100))


if __name__ == '__main__':
    zc = zipcodeClassifier()
    zc.knn()
    zc.gaussian()
