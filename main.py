def calculate_power(wind_speed, rated_power=15, cut_in=3,
                    rated_speed=11, cut_out=25, interpolation="linear"):
 """
Calculate the power output of a wind turbine.

Parameters
----------
wind_speed : float
    Wind speed in m/s.
rated_power : float, optional
    Rated power of the turbine in MW.
cut_in : float, optional
    Cut-in wind speed in m/s.
rated_speed : float, optional
    Rated wind speed in m/s.
cut_out : float, optional
    Cut-out wind speed in m/s.
interpolation : str, optional
    Interpolation method, either "linear" or "cubic".
Returns
-------
float
    Power output of the wind turbine in MW.
"""
    
 if interpolation not in ["linear", "cubic"]:
        raise ValueError("Interpolation must be 'linear' or 'cubic'.")
    # No power below cut-in speed or at/above cut-out speed.
 if wind_speed < cut_in or wind_speed >= cut_out:
        power = 0
    # Calculate power between cut-in and rated speed.
 elif wind_speed < rated_speed:
        if interpolation == "linear":
            g = (wind_speed - cut_in) / (rated_speed - cut_in)
        else:
            g = wind_speed**3 / rated_speed**3
        power = g * rated_power
    # Produce rated power between rated and cut-out speed.
 else:
        power = rated_power
 return power

if __name__ == "__main__":
    wind_speed = 8.0
    power = calculate_power(wind_speed)
    print(f"Wind speed: {wind_speed} m/s")
    print(f"Power output: {power:.2f} MW")