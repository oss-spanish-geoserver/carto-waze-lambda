"""
Carto Waze Lambda Connector

Developed by Geographica, 2017-2018.
"""

import os


class Config:
    """
    Configuration parameters:
        - Carto API.
        - WAZE API
        - Traffico
    """

    # Carto API
    CARTO_API_KEY = os.environ.get('CARTO_API_KEY')
    CARTO_USER = os.environ.get('CARTO_USER')

    # Waze API
    _WAZE_API_URL = os.environ.get('WAZE_API_URL')
    _WAZE_TKN = os.environ.get('WAZE_TKN')
    _WAZE_PARTNER_NAME = os.environ.get('WAZE_PARTNER')
    _WAZE_FRMT = 'JSON'
    _WAZE_TYPES = 'traffic,alerts,irregularities'
    _WAZE_POLY = '-3.658447,40.538118;-3.769684,40.478080;-3.816376,40.406487;-3.773804,40.360460;-3.720245,40.317543;-3.647461,40.326442;-3.544464,40.382954;-3.535538,40.460842;-3.576736,40.516197;-3.658447,40.538118;-3.658447,40.538118'
    WAZE_GEORSS = (
        _WAZE_API_URL,
        _WAZE_TKN,
        _WAZE_PARTNER_NAME,
        _WAZE_FRMT,
        _WAZE_TYPES,
        _WAZE_POLY
        )

    # Traffico
    TRAFFICO_PREFIX = os.environ.get('TRAFFICO_PREFIX')
