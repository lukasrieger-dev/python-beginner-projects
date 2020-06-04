%matplotlib inline

import re
import matplotlib.pyplot as plt


def load_mu_data(path):
    mu_data = dict()
    with open(path, 'r') as file:
        for line in file:
            if re.match(r'(^ *$|^#.*$)', line):
                # omit empty lines and comments
                continue
                
            *gas, C, T_0, mu_0 = line.split()
            gas = ''.join(gas) # for names with more than one word
            data = {'C':float(C), 'T_0':float(T_0), 'mu_0':float(mu_0)}
            mu_data[gas] = data
    return mu_data


def mu(T, gas, mu_data):
    if not gas in mu_data:
        raise ValueError
        
    data = mu_data[gas]
    T_0 = data['T_0']
    C = data['C']
    mu_0 = data['mu_0']
    mu_T = mu_0 * (T_0-C)/(T+C) * (T/T_0)
    
    return mu_T


path = 'viscosity_of_gases.dat'
mu_data = load_mu_data(path)
Ts = list(range(223, 374))

for gas in mu_data:
    mu_values = [mu(T, gas, mu_data) for T in Ts]
    plt.plot(Ts, mu_values)

plt.legend(list(mu_data))
plt.xlabel('temperatures')
plt.ylabel('viscosity')
plt.show()