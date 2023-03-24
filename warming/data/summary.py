import pandas as pb

class Summary:

    def __init__(self):
        self._filepath = "./data/41558_2023_1605_MOESM2_ESM.xlsx"
        self._data = self.prepare_data()

    def prepare_data(self):
        """Here comes the documentation.

        Some more docs.
        """
        data = pb.read_excel(self._filepath, sheet_name="Country Summaries")
        data = data.set_index("Country Name")
        return data[2:]

    def countries(self):
        """Returns an index of the countries available in the dataset.

        :return: Returns an index of countries of the dataset.
        :rtype: pandas.core.indexes.base.Index
        """
        return self._data.keys()

    def co2(self):
        """Returns the data of `CO2` values per capita per country.

        :return: The `CO2` data per capita per country.
        :rtype: pandas.core.series.Series
        """
        return self._data["CO2C"]

    def ch4c(self):
        """Returns the data of `CH4C` values per capity per country.

        :return: The `CH4C` data per capita per country.
        :rtype: pandas.core.series.Series
        """
        return self._data["CH4C"]

    def n2oc(self):
        """Returns the data of `N2OC` values per capity per country.

        :return: The `N2OC` data per capita per country.
        :rtype: pandas.core.series.Series
        """
        return self._data["N2OC"]

    def co2y(self):
        """Returns the data of `CO2Y` values per capita per country per year

        :return: The `CO2Y` data per capity per country per year.
        :rtype: pandas.core.series.Series
        """
        return self._data["CO2Y"]

    def ch4y(self):
        """Returns the data of `CH4Y` values per capita per country per year.

        :return: The `CH4Y` data per capita per country per year.
        :rtype: pandas.core.series.Series
        """
        return self._data["CH4Y"]

    def n2oy(self):
        """Returns the data of `N2OY` values per capita per country per year.

        :return: The `N2OY` data per capita per country per year.
        :rtype: pandas.core.series.Series
        """
        return self._data["N2OY"]
