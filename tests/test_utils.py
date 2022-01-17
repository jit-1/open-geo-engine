import datetime
import ee

from open_geo_engine.utils.utils import ee_array_to_df
from open_geo_engine.src.load_ee_data import LoadEEData
from open_geo_engine.src.generate_building_centroids import GenerateBuildingCentroids


def test_ee_array_to_df():
    countries = ["ES"]
    place = "Parque El Retiro, Madrid"
    tags = {"leisure": "park"}

    generate_building_centroids = GenerateBuildingCentroids(countries, place, tags)
    buildings_gdf = generate_building_centroids.execute()

    year = 2020
    mon_start = 1
    date_start = 1
    year_end = 2020
    mon_end = 1
    date_end = 31
    image_collection = "LANDSAT/LC08/C01/T1"
    image_band = ["B4", "B3", "B2"]
    folder = "/test_data"
    model_name = "LANDSAT"
    building_footprints_satellite_list = []

    load_ee_data = LoadEEData(
        countries,
        year,
        mon_start,
        date_start,
        year_end,
        mon_end,
        date_end,
        image_collection,
        image_band,
        folder,
        model_name,
        place,
    )
    buildings_gdf = load_ee_data._get_xy(buildings_gdf)
    for lon, lat in zip(buildings_gdf.x, buildings_gdf.y):
        s_date, e_date = load_ee_data._generate_start_end_date()
        assert (s_date, e_date) == (datetime.datetime(2020, 1, 1, 0, 0), datetime.datetime(2020, 1, 31, 0, 0))
