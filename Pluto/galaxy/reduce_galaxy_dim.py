import os, sys
import traceback
import numpy as np
from PIL import Image
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from keras.layers import Input, Dense, Dropout
from keras.models import Model, load_model
from keras.optimizers import SGD, Adam


class galaxy():
    DIR_NAME = '/Users/SiriusR/Documents/Pluto/galaxy/galaxy/'
    GRAY_SCALE_DIR = DIR_NAME + 'gsd/'
    TRAIN_DIR = GRAY_SCALE_DIR + 'train/'
    VAL_DIR = GRAY_SCALE_DIR + 'val/'
    TEST_DIR = GRAY_SCALE_DIR + 'test/'

    def convert_to_grayscale(self):
        dirname = self.DIR_NAME
        gray_scale_dir = dirname + 'gsd/'
        data_name = ['val']
        for data in data_name:
            dirname += data
            imgs = []
            for imgname in os.listdir(dirname):
                try:
                    img = Image.open(os.path.join(dirname, imgname))
                except Exception:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    traceback.print_exception(exc_type, exc_value, exc_traceback)
                    continue
                img = img.convert('LA')  # conver to grayscale
                img = img.resize([20, 20])
                img = np.squeeze(np.array(img)[:, :, 0])
                img = Image.fromarray(img)
                img.save(os.path.join(gray_scale_dir + data, imgname))
                imgs.append(img)
            dirname -= data

    def pca(self):
        pca = PCA(n_components=25, svd_solver='randomized')
        img_shape = (20, 20)
        train_data = galaxy.load_data(self.TRAIN_DIR)
        val_data = galaxy.load_data(self.VAL_DIR)
        test_data = galaxy.load_data(self.TEST_DIR)

        # training pca model reduced images to 25 dimensions
        pca.fit(train_data)

        # obtains the projection onto components
        projected_train_data = galaxy.get_projected_data(train_data, pca)
        projected_val_data = galaxy.get_projected_data(val_data, pca)
        projected_test_data = galaxy.get_projected_data(test_data, pca)
        train_mse = galaxy.calculate_mse(train_data, projected_train_data)
        galaxy.display_mse_stat(train_mse, 'train')
        val_mse = galaxy.calculate_mse(val_data, projected_val_data)
        galaxy.display_mse_stat(val_mse, 'val')
        test_mse = galaxy.calculate_mse(test_data, projected_test_data)
        galaxy.display_mse_stat(test_mse, 'test')
        return projected_test_data

    @staticmethod
    def get_projected_data(data, pca):
        train_pca = pca.transform(data)
        projected_data = pca.inverse_transform(train_pca)
        return projected_data

    @staticmethod
    def calculate_mse(data, projected_data):
        mse = []
        for i in range(len(data)):
            mse.append(mean_squared_error(projected_data[i], data[i]))
        return mse

    @staticmethod
    def display_mse_stat(mse, name):
        max_value = max(mse)
        max_index = [i for i, j in enumerate(mse) if j == max_value]
        min_value = min(mse)
        min_index = [i for i, j in enumerate(mse) if j == min_value]
        mean = sum(mse) / len(mse)
        print("--------{0}---------".format(name))
        print("max is {0} indexed{1}\nmin is {2} indexed {3}\nmean is {4}\n----------------------".format(max_value,
                                                                                                          max_index,
                                                                                                          min_value,
                                                                                                          min_index,
                                                                                                          mean))

    @staticmethod
    def load_data(data_dir):
        img_list = []
        for img_name in os.listdir(data_dir):
            try:
                img = Image.open(os.path.join(data_dir, img_name))
                img = np.asarray(img) / 255
                img_list.append(img)
            except Exception:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback)
                continue
        img_list = np.array(img_list)
        data_size = len(img_list)
        data = img_list.reshape(data_size, -1)
        return data

    @staticmethod
    def show_image(data, img_shape, index):
        comp = data[index]
        comp = comp.reshape(img_shape)
        plt.imshow(comp, cmap='gray')
        plt.show()

    @staticmethod
    def display_auto_vs_pca(pca_output, autoencoder_output, input_data, index, index_pca_better):
        f, axarr = plt.subplots(6)

        axarr[0].imshow(input_data[index].reshape(20, 20), cmap='gray')
        axarr[0].set_title('input image')
        axarr[1].imshow(autoencoder_output[index].reshape(20, 20), cmap='gray')
        axarr[1].set_title('autoencoder output image')
        axarr[2].imshow(pca_output[index].reshape(20, 20), cmap='gray')
        axarr[2].set_title('PCA output image')

        axarr[3].imshow(input_data[index_pca_better].reshape(20, 20), cmap='gray')
        axarr[3].set_title('input image')
        axarr[4].imshow(autoencoder_output[index_pca_better].reshape(20, 20), cmap='gray')
        axarr[4].set_title('autoencoder output image')
        axarr[5].imshow(pca_output[index_pca_better].reshape(20, 20), cmap='gray')
        axarr[5].set_title('PCA output image')
        plt.show()

    def autoencoder(self):
        input_img = Input(shape=(400,))
        dropout = Dropout(0.1)(input_img)
        encoded = Dense(100, activation='linear')(dropout)
        encoded = Dense(50, activation='tanh')(encoded)
        encoded = Dense(25, activation='linear')(encoded)
        decoded = Dense(50, activation='tanh')(encoded)
        decoded = Dense(100, activation='tanh')(decoded)
        decoded = Dense(400, activation='linear')(decoded)

        autoencoder = Model(input=input_img, output=decoded)
        sgd = SGD(lr=0.5, decay=10e-6, momentum=0.9, nesterov=True)
        adam = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
        autoencoder.compile(optimizer=adam, loss='mean_squared_error')
        autoencoder.save('/Users/SiriusR/SiriusPlanet.Alpha/Pluto/galaxy/autoencoder.h5')
        train_data = galaxy.load_data(self.TRAIN_DIR)
        test_data = galaxy.load_data(self.TEST_DIR)
        autoencoder.fit(train_data, train_data, nb_epoch=5, batch_size=256, shuffle=True,
                        validation_data=(train_data, train_data))
        test_decoded_img = autoencoder.predict(test_data)
        print(test_decoded_img)
        test_mse = galaxy.calculate_mse(test_data, test_decoded_img)
        galaxy.display_mse_stat(test_mse, 'auto-encoder_train')
        return test_decoded_img

    def display(self, n, orig_img, decoded_img):
        for i in range(n):
            # display original
            ax = plt.subplot(2, n, i + 1)
            plt.imshow(orig_img[i].reshape(20, 20), cmap='gray')
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)

            # display reconstruction
            ax = plt.subplot(2, n, i + 1 + n)
            plt.imshow(decoded_img[i].reshape(20, 20), cmap='gray')
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
        plt.show()

    @staticmethod
    def compare_mse(autoencoder_mse, pca_mse):
        autoencoder_better_index = []
        pca_better_index = []
        mse_stat_set = {'auto_better': [], 'pca_better': [], 'auto_minus_pca': {}}
        auto_minus_pca = {'max': 0, 'min': 0, 'max_index': 0, 'min_index': 0}  # max and min
        for i in range(0, len(autoencoder_mse)):
            delta = autoencoder_mse[i] - pca_mse[i]
            if delta < auto_minus_pca['max']:
                auto_minus_pca['max'] = delta
                auto_minus_pca['max_index'] = i
            if delta > auto_minus_pca['min']:
                auto_minus_pca['min'] = delta
                auto_minus_pca['min_index'] = i
            if autoencoder_mse[i] <= pca_mse[i]:
                autoencoder_better_index.append(i)
            else:
                pca_better_index.append(i)
        mse_stat_set['auto_better'] = autoencoder_better_index
        mse_stat_set['pca_better'] = pca_better_index
        mse_stat_set['auto_minus_pca'] = auto_minus_pca
        return mse_stat_set

    def autoencoder_vs_pca(self):
        test_data = galaxy.load_data(self.TEST_DIR)
        pca_test_output = self.pca()
        autoencoder_test_output = self.autoencoder()
        autoencoder_mse = galaxy.calculate_mse(test_data, autoencoder_test_output)
        pca_mse = galaxy.calculate_mse(test_data, pca_test_output)
        galaxy.display_mse_stat(autoencoder_mse, 'autoencoder_test_mse')
        galaxy.display_mse_stat(pca_mse, 'PCA_test_mse')
        mse_stat_set = galaxy.compare_mse(autoencoder_mse, pca_mse)
        autoencoder_better_index_list = mse_stat_set['auto_better']

        auto_beats_pca_most = mse_stat_set['auto_minus_pca']['max_index']
        pca_beats_auto_most = mse_stat_set['auto_minus_pca']['min_index']
        print(
            "\nThe Autoencoder beats PCA most on image indexed {0}\n "
            "The mse of autoencoder:{1}\n The mse of PCA:{2}\n MSE_a - MSE_p = {3}\n".format(
                auto_beats_pca_most, autoencoder_mse[auto_beats_pca_most], pca_mse[auto_beats_pca_most],
                mse_stat_set['auto_minus_pca']['max']))
        print('---------------------------------------------')
        print(
            "\nThe PCA beats Autoencoder most on image indexed {0}\n "
            "The mse of autoencoder:{1}\n The mse of PCA:{2}\n MSE_a - MSE_p = {3}\n".format(
                pca_beats_auto_most, autoencoder_mse[pca_beats_auto_most], pca_mse[pca_beats_auto_most],
                mse_stat_set['auto_minus_pca']['min']))
        print('---------------------------------------------')
        print("\nThe MSE of autoencoder for Pictures indexed with {0} has smaller MSE than PCA. ".format(
            autoencoder_better_index_list))
        galaxy.display_auto_vs_pca(pca_test_output, autoencoder_test_output, test_data, auto_beats_pca_most,
                                   pca_beats_auto_most)


if __name__ == '__main__':
    ga = galaxy()
    ga.autoencoder_vs_pca()
