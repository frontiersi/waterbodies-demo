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

    satpass_date = pd.to_datetime(df["date"].iloc[-1]).date()

    return satpass_date


def last_wet_obs(df):
    """
    Identify the last date where the waterbody was clearly observed
    """
    #  sort date values into ascending order
    df.sort_values(by="date", inplace=True, ascending=True)

    # drops rows where nan values appear in 'pc_wet' 'px_wet' columns
    df_wet_obs = df.dropna(subset=["pc_wet", "px_wet"], how="all")

    lastwet_date = pd.to_datetime(df_wet_obs["date"].iloc[-1]).date()

    return lastwet_date  # returns the last valid observation


def pc_wet(df, area_value):
    """
    Calculates wet area of waterbody at last valid observation
    """
    #  sort date values into ascending order
    df.sort_values(by='date', inplace=True, ascending=True)
    
    # drops rows where nan values appear in 'pc_wet' 'px_wet' columns
    last_wet_obs=df.dropna(subset=['pc_wet','px_wet'], how='all')
    
    # calculates wet area from area and wet percentage
    last_wet_area= (area_value*last_wet_obs['pc_wet'].iloc[-1])/100 
    
    return last_wet_area 