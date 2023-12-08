# DESAFIO 046: Faça um programa que mostre na tela uma contagem regressiva para
# o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

from time import sleep

print('\n\t\t\t\t\033[0;31mEXPL\033[m\033[0;33mOSÃO\033[m\033[0;32m DE FÓ\033[m\033[0;34mGOS!\033[m')
print('\033[0;31m**\033[m\033[0;33m**\033[m\033[0;32m**\033[m\033[0;34m**\033[m' * 6)
print()

for c in range(10, -1, -1):
    print('\t\t\t\t\t\t', c)
    sleep(1)

print('\n\033[0;31mBBU\033[m\033[0;33mUUU\033[m\033[0;32mUMM\033[m\033[0;34mMMM\033[m  \033[0;31mBBU\033[m\033[0;33mUUU\033[m\033[0;32mUMM\033[m\033[0;34mMMM\033[m  \033[0;31mBBU\033[m\033[0;33mUUU\033[m\033[0;32mUMM\033[m\033[0;34mMMM\033[m  \033[0;31mBBU\033[m\033[0;33mUUU\033[m\033[0;32mUMM\033[m\033[0;34mMMM\033[m')
