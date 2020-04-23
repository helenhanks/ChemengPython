def lmdt(T_hot_in, T_hot_out, T_cold_in, T_cold_out, direction="countercurrent"):
    "This function returns the log mean temperature of a heat exchanger given four temperatures and a direction"
    
    import math

    # Set up delta_T based on direction. Countercurrent direction is default.
    if direction == "cocurrent":
        delta_T_1 = T_hot_in - T_cold_in
        delta_T_2 = T_hot_out - T_cold_out
    else:
        delta_T_1 = T_hot_in - T_cold_out
        delta_T_2 = T_hot_out - T_cold_in

    # Calculate LMTD, check feasibility
    if delta_T_1 > 0 and delta_T_2 > 0:
        log_mean_delta_T = (delta_T_1 - delta_T_2)/math.log(delta_T_1 / delta_T_2)
    else:
        log_mean_delta_T = 0
        
    return log_mean_delta_T

def PipeTransitTime(Flow_MMSCD, Pressure_PSIG, Pipe_Length_Miles, Pipe_Diameter_Inches, Min_Forced_Flow_MMSCFD = 0.001):
    "This functon returns the transit time of an ideal gas through a pipe given molar flow, pressure, pipe length and diameter."

    import math
    PI = math.pi

    # Physical Properties
    P_STP = 14.7                                #PSIA

    # Pipeline Geometry Calculations
    PIPELINE_CROSS_SECTION_AREA = PI*((Pipe_Diameter_Inches/12/2)**2)  #FT^2
    PIPLEINE_LENGTH_FEET = 5280*Pipe_Length_Miles

    # Force flow to tiny positive number to avoid negative transit times and divide zero errors
    VSTP_MMSCFD = max(Min_Forced_Flow_MMSCFD,Flow_MMSCD)

    # Convert from MMSCFD to SCFH
    VSTP_SCFS = (VSTP_MMSCFD*1000000)/24

    # Convert guage pressure to absolute
    ABSOLUTE_PRESSURE = Pressure_PSIG + 14.7

    # Use ideal gas law to covert standard volume flow to actual volume flow
    ACTUAL_VOLUMETRIC_FLOW = VSTP_SCFS*(P_STP/ABSOLUTE_PRESSURE)

    # Calculate transit time
    TRANSIT_TIME_HOURS = PIPLEINE_LENGTH_FEET*PIPELINE_CROSS_SECTION_AREA/ACTUAL_VOLUMETRIC_FLOW

    return TRANSIT_TIME_HOURS
       
