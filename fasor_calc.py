'''
@author: NicolasQueiroga
'''
# python /Users/nicolasqueiroga/Desktop/Codes/Python/py/fasor_calc.py

import numpy as np
from math import *

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def Z(R, L, C, w):
    if L == 0 and C == 0:
        return R + 0*1j
    elif R == 0 and C == 0:
        ans = round(L*w, 3)
        return 0 + ans*1j
    elif L == 0 and R == 0:
        ans = round(1/(C*w), 3)
        return 0 - ans*1j

def polar2rect(rho, theta):
    Z = rho*cos(radians(theta)) + rho*sin(radians(theta))*1j
    return Z

def polar(phasors):
    polarized = {}
    for name, z in phasors.items():
        a = z.real
        b = z.imag
        rho = hypot(b, a)
        theta = degrees(atan2(b, a))
        polarized[name] = '{0:.3f} /__ {1:.2f}º'.format(rho, theta)
    return polarized

def Z_serie(phasors):
    Zeq = sum(phasors.values())
    return Zeq

def pot(Zeq, rho, theta):
    V = polar2rect(rho, theta)
    I = V/Zeq
    pot_complx = V*np.conj(I)/2
    pot_ap = np.absolute(pot_complx)
    pot_ativa = pot_complx.real
    pot_reativa = pot_complx.imag
    fator_de_pot = atan2(pot_complx.imag, pot_complx.real)
    results = [pot_complx, pot_ap, pot_ativa, pot_reativa, fator_de_pot, I]
    return results

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

phasors = {}
ans = input('\nFoi dado velocidade ângular ou frequência(w/f)? ')
if ans == 'w':
    w = float(input('\nQual é a velocidade ângular w(rad/s)? '))
elif ans == 'f':
    f = float(input('\nQual é a freqência f(1/s)? '))
    w = 2*pi*f

while True:
    ans = input('\nCapacitor = C\nResistor = R\nIndutor = L\n--> ')
    if ans == 'end':
        break
    if 'R' not in ans:
        R = 0
        if 'L' in ans:
            C = 0
            L = float(input('\nQual é a indutância? '))
        elif 'C' in ans:
            L = 0
            C = float(input('\nQual é a capacitância? '))
    else:
        L = 0
        C = 0
        R = float(input('\nQual é a resistência? '))
    phasors[ans] = Z(R, L, C, w)
    print('\nDigite end para concluir')
print('\nOs fasores são:\n{}'.format(phasors))
print('\nSuas representações polares são:\n{}\n'.format(polar(phasors)))


ans1 = input('\nOs componentes estão em SERIE(y/n, or skip)? ')
eq = {}
if ans1 == 'y':
    eq['Zeq'] = Z_serie(phasors)
    print('\nZeq = {:.3f} ohms\n'.format(eq['Zeq']))
    print('Zeq = {} ohms\n'.format(polar(eq)))
elif ans1 == 'n':
    eq['Zeq'] = phasors['R'] + (phasors['L']*phasors['C'])/(phasors['L']+phasors['C'])
    print('\nZeq = {:.3f} ohms\n'.format(eq['Zeq']))
    print('Zeq = {} ohms\n'.format(polar(eq)))


if ans1 != 'skip':
    ans = input('\nQuer calcular potência (y/n)? ')
    if ans == 'y':
        ans = input('\nO valor da DDP é o eficaz ou de pico-a-pico (ef/pp)? ')
        if ans == 'pp':
            rho = float(input('\nDigite o valor de Vpp: '))
        elif ans == 'ef':
            Vef = float(input('\nDigite o valor de Vef: '))
            rho = Vef*sqrt(2)
        theta = float(input('\nQual é o ângulo de fase? '))
        potência = pot(eq['Zeq'], rho, theta)
        
        i = {'I':potência[5]}
        print('\n\nCorrente = {:.3f} A'.format(potência[5]))
        print('Corrente = {} A'.format(polar(i)))

        p = {'S':potência[0]}
        print('\nPotência Complexa = {:.3f} V.A'.format(potência[0]))
        print('Potência Complexa = {} V.A'.format(polar(p)))

        print('\nPotência Aparente = {:.3f} V.A'.format(potência[1]))
        print('\nPotência Ativa = {:.3f} W'.format(potência[2]))
        print('\nPotência Reativa = {:.3f} V.A'.format(potência[3]))
        print('\nFator de Potência = {:.3f}\n'.format(potência[4]))

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------