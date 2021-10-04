'''
@author: NicolasQueiroga
'''

import numpy as np
from math import *

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------


def Z(R, L, C, w):
    if L == 0 and C == 0:
        return R + 0*1j
    elif R == 0 and C == 0:
        ans = round(L*w, 4)
        return 0 + ans*1j
    elif L == 0 and R == 0:
        ans = round(1/(C*w), 4)
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
    fator_de_pot = pot_ativa/pot_ap
    results = [pot_complx, pot_ap, pot_ativa, pot_reativa, fator_de_pot, I]
    return results

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------


phasors = {}
print('\n--------------------------------------------------------')
ans = input('Foi dado velocidade ângular ou frequência(w/f)? ')
if ans == 'w':
    w = float(input('Qual é a velocidade ângular w(rad/s)? '))
elif ans == 'f':
    f = float(input('Qual é a freqência f(1/s)? '))
    w = 2*pi*f
print('--------------------------------------------------------\n')

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------


def main():
    values = {}
    while True:
        print('--------------------------------------------------------')
        ans = input(
            'Capacitor = C\nResistor = R\nIndutor = L\nend = concluir\n--> ')
        if ans == 'end':
            break
        if 'R' not in ans:
            R = 0
            if 'L' in ans:
                C = 0
                L = float(input('\nQual é a indutância? '))
                values[ans] = L
            elif 'C' in ans:
                L = 0
                C = float(input('\nQual é a capacitância? '))
                values[ans] = C
        else:
            L = 0
            C = 0
            R = float(input('\nQual é a resistência? '))
            values[ans] = R
        phasors[ans] = Z(R, L, C, w)
        print('\n', values)
        print('--------------------------------------------------------')
    print('--------------------------------------------------------')
    print('\n--------------------------------------------------------')
    print('Os fasores são:\n{}'.format(phasors))
    print('\nSuas representações polares são:\n{}'.format(polar(phasors)))
    print('--------------------------------------------------------')

    # -------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------

    print('\n--------------------------------------------------------')
    ans1 = input('Os componentes estão em SERIE(y/n, or skip)? ')
    eq = {}
    if ans1 == 'y':
        eq['Zeq'] = Z_serie(phasors)
        print('\nA impedância equivalente é:')
        print('Zeq = {:.3f} ohms\n'.format(eq['Zeq']))
        print('Sua representação polar é:')
        print('Zeq = {} ohms'.format(polar(eq)))
    elif ans1 == 'n':
        try:
            # Altere aqui a equação que calcula a impedância equivalente
            eq['Zeq'] = None
            # ----------------------------------------------------------
            print('\nA impedância equivalente é:')
            print('Zeq = {:.3f} ohms\n'.format(eq['Zeq']))
            print('Sua representação polar é:')
            print('Zeq = {} ohms'.format(polar(eq)))
        except:
            print(
                '\n--->Altere a linha 111 do código com a equação que calcula a impedância equivalente!<---')
            ans1 = 'skip'
    print('--------------------------------------------------------')

    # -------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------

    if ans1 != 'skip':
        print('\n--------------------------------------------------------')
        ans = input('Quer calcular potência (y/n)? ')
        if ans == 'y':
            ans = input(
                '\nO valor da DDP é o eficaz ou de pico-a-pico (ef/pp)? ')
            if ans == 'pp':
                rho = float(input('Digite o valor de Vpp: '))
            elif ans == 'ef':
                Vef = float(input('Digite o valor de Vef: '))
                rho = Vef*sqrt(2)
            theta = float(input('Qual é o ângulo de fase? '))
            potência = pot(eq['Zeq'], rho, theta)
            print('--------------------------------------------------------\n')
            i = {'I': potência[5]}
            print('Corrente nas formas retângular e polar:')
            print('Corrente = {:.3f} A'.format(potência[5]))
            print('Corrente = {} A'.format(polar(i)))

            p = {'S': potência[0]}
            print('\nPotência (S) nas formas retângular e polar:')
            print('{:.3f} V.A'.format(potência[0]))
            print('{} V.A'.format(polar(p)))

            print('\nOutras análises da potência (S):')
            print('Potência Aparente = {:.3f} V.A'.format(potência[1]))
            print('Potência Ativa = {:.3f} W'.format(potência[2]))
            print('Potência Reativa = {:.3f} V.A'.format(potência[3]))
            print('Fator de Potência = {:.3f}'.format(potência[4]))
            print('\n--------------------------------------------------------')
    print('-------------------------end----------------------------\n')


if __name__ == '__main__':
    main()
