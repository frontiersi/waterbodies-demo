def last_sat_pass(df):
    df.sort_values(by='date', inplace=True, ascending=True)# ensures date values are in ascending order
    return df['date'].iloc[-1]# returns the date last passed

def last_wet_obs(df):
    df.sort_values(by='date', inplace=True, ascending=True)# ensures date values are in ascending order
    last_wet_obs=df.dropna(subset=['pc_wet','px_wet'], how='all')# drops nan values in 'pc_wet' 'px_wet' columns
    return last_wet_obs['date'].iloc[-1]# returns the last valid observation