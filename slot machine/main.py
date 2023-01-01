from asyncio.subprocess import SubprocessStreamProtocol
from curses.ascii import isdigit
import random
from turtle import st

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbols = {
    'A':3,
    'B':6,
    'C':9,
    'D':12
}

values = {
    'A': 12,
    'B': 9,
    'C': 6,
    'D': 3
}

def deposit():
    while True:
        dep=input("Enter the deposit: $")
        if dep.isdigit():
            dep=int(dep)
            if dep>0:
                break
            else:
                print("Enter a value above zero.")
        else:
            print("Please enter a number.")
    return dep

def get_lines():
    while True:
        lines=input("Enter the number of lines(1+"+str(MAX_LINES)+"): ")
        if lines.isdigit():
            lines=int(lines)
            if lines in range(1, MAX_LINES+1):
                break
            else:
                print("Enter a value within 1 and "+str(MAX_LINES))
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        bet=input("Place your bet(between $"+str(MIN_BET)+" and $"+str(MAX_BET)+"): ")
        if bet.isdigit():
            bet=int(bet)
            if bet in range(1, MAX_BET):
                break
            else:
                print("Please enter a value within $"+str(MIN_BET)+" and $"+str(MAX_BET))
        else:
            print("Please enter a number.")
    return bet

def spin(rows, cols, symbols):
    all_symbols= []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns= []
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row], end=' | ')
            else:
                print(column[row], end='')
        print()
            
def winnings(lines, bet, columns, values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            check_symbol=column[line]
            if check_symbol!=symbol:
                break
        else:
            winning_lines.append(line+1)
            winnings+=(values[check_symbol]*bet)

    return winnings, winning_lines

def game(balance):
    lines=get_lines()
    while True:
        bet=get_bet()
        total_bet=lines*bet
        if total_bet>balance:
            print(f"You do not have enough balance to place that bet. Your current balance is ${balance}. Please place a valid bet.")
        else:
            break
    print(f"You are betting ${bet} on {lines}. Total bet is ${total_bet}. ")

    slots=spin(ROWS, COLS, symbols)
    print_slot_machine(slots)
    win, winning_lines=winnings(lines, bet, slots, values)
    print(f"You won ${win}")
    print("You won on the lines: ", winning_lines)
    return win-total_bet

def main():
    balance=deposit()
    while True:
        ans=input("Press Enter to play(Or q to quit): ")
        if ans.lower()=='q':
            break
        balance+=game(balance)
        print(f"Balance left: ${balance}")

    print(f"You left with ${balance}")


main()
