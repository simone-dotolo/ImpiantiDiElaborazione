import numpy as np

MTTF_CPU = 10000
MTTF_Terminal = 4500
MTTF_AHRS = 2000
MTTF_INS = 2000
MTTF_Doppler = 500
MTTF_Bus = 60000

t = 1
R_CPU = np.exp(-1/MTTF_CPU*t)
R_Terminal = np.exp(-1/MTTF_Terminal*t)
R_AHRS = np.exp(-1/MTTF_AHRS*t)
R_INS = np.exp(-1/MTTF_INS*t)
R_Doppler = np.exp(-1/MTTF_Doppler*t)
R_Bus = np.exp(-1/MTTF_Bus*t)

R_sistema = (1-(1-R_CPU)**2)*(1-(1-R_Terminal)**2)*(1-(1-R_Bus)**2)*(1-(1-R_Bus)**2)*(1-(1-R_INS)*(1-R_Doppler*(1-(1-R_AHRS)**3)))

print(R_sistema)

R_star = (1-(1-R_Terminal)**2)*(1-(1-R_Bus)**2)*(1-(1-R_Bus)**2)*(1-(1-R_INS)*(1-R_Doppler*(1-(1-R_AHRS)**3)))

C = (1-np.sqrt(1-0.99999/R_star))/R_CPU

print(C)
