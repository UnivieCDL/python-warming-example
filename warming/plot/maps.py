import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pb
import numpy as np

class World:
    """This class contains all the methods to visualize data on a world map"""

    def __init__(self):
        self._world = gpd.read_file(
            gpd.datasets.get_path('naturalearth_lowres')
        )

    def show(self, data, column):
        """Opens a world map plot.

        The map shows the specified data, which also needs to be
        set with the `column` parameter.

        :param data: The data that will be shown on the world map.
        :type data: pandas.core.series.Series
        :param column: The index of the data to show.
        :type column: str
        """

        vis_data = self._world.join(data, on="name")
        vis_data.plot(column=column, cmap='OrRd')

        plt.show()

    def get_data(self):
        """Getter to retreive the geopandas 'naturalearth_lowres' data set

        :return: World data, filled with information of a country's population, GDP, geometry
        :rtype: geopandas.geodataframe.GeoDataFrame
        """
        return self._world


class Europe(World):
    """This class contains all the methods to visualize data on a world map"""

    def __init__(self):
        super().__init__()

    def filter_Europe(self):
        """

        :return:
        """
        self._filepaath = "./data/41558_2023_1605_MOESM2_ESM.xlsx"
        europe_contry_arr = pb.read_excel(self._filepath, sheet_name="Europe")
        europe_contry_arr = europe_contry_arr[~np.isnan(europe_contry_arr)]
        self.europe_list = list()
        for k, item in enumerate(europe_contry_arr):
            if isinstance(item, str):
                self.europe_list.append(item)

    def show(self, data, column):
        """Opens a world map plot.

        The map shows the specified data, which also needs to be
        set with the `column` parameter.

        :param data: The data that will be shown on the world map.
        :type data: pandas.core.series.Series
        :param column: The index of the data to show.
        :type column: str
        """
        self.filter_Europe()

        index_list = list()
        for k, name in enumerate(data.index):
            if name in self.europe_list:
                index_list.append(k)

        new_data = pb.Series(data=data.values[index_list], index=data.index[index_list])


        vis_data = self._world.join(new_data, on="name")
        vis_data.plot(column=column, cmap='OrRd')

        plt.show()



if __name__ == '__main__':
    a = World
    print(type(a))