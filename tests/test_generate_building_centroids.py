import pandas as pd
from open_geo_engine.src.generate_building_centroids import GenerateBuildingCentroids


def test_get_boundaries_from_place():
    countries = ["ES"]
    place = "Parque El Retiro, Madrid"
    tags = {"leisure": "park"}

    generate_building_centroids = GenerateBuildingCentroids(countries, place, tags)
    assert len(generate_building_centroids.execute()) == len(
        pd.read_csv("tests/test_data/test_osm.csv", index_col=False)
    )
    assert generate_building_centroids._get_boundaries_from_place().shape == (1, 20)
    assert generate_building_centroids.get_representative_building_point().shape == (
        1,
        21,
    )
