import colorama
from colorama import Fore
import os
import time
import subprocess

#хуи типе а ни кад

Blue = Fore.BLUE
Reset = Fore.RESET
White = Fore.WHITE

def print_with_delay1(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    
print_with_delay1("""
    ВНИМАНИЕ: Данный программный продукт создан исключительно в образовательных и исследовательских целях. Мы настоятельно рекомендуем использовать его только в рамках закона и с соблюдением всех юридических норм и этических стандартов.

Дисклеймер: Использование данной программы для нарушения прав и свобод личности, включая, но не ограничиваясь, stalking, преследованием или шпионством, строго запрещено. Несанкционированный сбор или использование личной информации может привести к серьезным юридическим последствиям. В России, в соответствии со статьей 137 Уголовного кодекса РФ, незаконный сбор и распространение персональных данных может повлечь за собой уголовную ответственность и наказания в виде штрафов или лишения свободы на срок до 2 лет.

Мы призываем всех пользователей ответственности относиться к использованию данной программы и уважать права других людей.""")

def print_with_delay2(text, delay=0.0001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    
print_with_delay2(f"""{Blue}
S.       .S       S.    .S_sSSs     .S_SSSs     .S_sSSs    
SS.     .SS       SS.  .SS~YS%%b   .SS~SSSSS   .SS~YS%%b   
S%S     S%S       S%S  S%S   `S%b  S%S   SSSS  S%S   `S%b  
S%S     S%S       S%S  S%S    S%S  S%S    S%S  S%S    S%S  
S&S     S&S       S&S  S%S    S&S  S%S SSSS%S  S%S    d*S  
S&S     S&S       S&S  S&S    S&S  S&S  SSS%S  S&S   .S*S  
S&S     S&S       S&S  S&S    S&S  S&S    S&S  S&S_sdSSS   {Reset}""") 
print_with_delay2(f"""{White}
S&S     S&S       S&S  S&S    S&S  S&S    S&S  S&S~YSY%b   
S*b     S*b       d*S  S*S    S*S  S*S    S&S  S*S   `S%b  
S*S.    S*S.     .S*S  S*S    S*S  S*S    S*S  S*S    S%S  
 SSSbs   SSSbs_sdSSS   S*S    S*S  S*S    S*S  S*S    S&S  
  YSSP    YSSP~YSSY    S*S    SSS  SSS    S*S  S*S    SSS  
                       SP                 SP   SP          
                       Y                  Y    Y           
----------------------------------------------------------
#  <1> Посик по базе     <2> Сносер      <3> ДДОС АТАКА  #
----------------------------------------------------------{Reset}""")

choose = input(f"{Blue}</>Выбирай: {Reset}")

if choose == '1':
    subprocess.run(['python', 'search.py'])
    
elif choose == '2':
    subprocess.run(['python', 'snos.py'])
    
elif choose == '3':
    subprocess.run(['python', 'snos.py'])