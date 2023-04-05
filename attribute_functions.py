"""
Functions for calculating date attributes
"""
import pandas as pd


def last_sat_pass(df):
    """
    Identify the last date that the satellite passed over
    """
    # sort date values into ascending order
    df.sort_values(by="date", inplace=True, ascending=True)

    satpass_date = pd.to_datetime(df["date"].iloc[-1]).to_pydatetime()

    return satpass_date


def last_wet_obs(df):
    """
    Identify the last date where the waterbody was clearly observed
    """
    #  sort date values into ascending order
    df.sort_values(by="date", inplace=True, ascending=True)

    # drops rows where nan values appear in 'pc_wet' 'px_wet' columns
    df_wet_obs = df.dropna(subset=["pc_wet", "px_wet"], how="all")

    if len(df_wet_obs.index) == 0:
        lastwet_date = None
    else:
        lastwet_date = pd.to_datetime(df_wet_obs["date"].iloc[-1]).to_pydatetime()

    return lastwet_date  # returns the last valid observation


def last_wet_area(df, area_value):
    """
    Calculates wet area of waterbody at last valid observation
    """
    #  sort date values into ascending order
    df.sort_values(by="date", inplace=True, ascending=True)

    # drops rows where nan values appear in 'pc_wet' 'px_wet' columns
    df_wet_obs = df.dropna(subset=["pc_wet", "px_wet"], how="all")

    if len(df_wet_obs.index) == 0:
        lastwet_area = None
    else:
        # calculates wet area from area and wet percentage
        lastwet_area = (area_value * df_wet_obs["pc_wet"].iloc[-1]) / 100

    return lastwet_area
