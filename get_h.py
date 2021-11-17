import math as m


def calc_discharge(b, h, k_st, m_bank, S):
    A = h * (b+ h*m_bank)
    P = b + (2*h*((m_bank**2)+1)**0.5)
    Q = k_st*(S**0.5)*((A/P)**(2/3))*A
    return Q


def interpolate_h(*args, **kwargs):
    pass


if __name__ == '__main__':
    # input parameters
    Q = 15.5        # discharge in (m3/s)
    b = 5.1         # bottom channel width (m)
    m_bank = 2.5    # bank slope
    k_st = 20       # Strickler value
    n_m = 1 / k_st  # Manning's n
    S_0 = 0.005     # channel slope
    discharge = calc_discharge(b,2,k_st,m_bank,S_0)
    print("The calculate discharge is %0.2f m3/s" %discharge)
    # call the solver with user-defined channel geometry and discharge
    h_n = interpolate_h(Q, b, n_m=n_m, m_bank=m_bank, S0=S_0)
