import math
from datetime import date

# ---- DATA ----
client_name = 'Brian'
weight_kg = 84
height_m = 1.78
weekly_steps = [9201, 7700, 10560, 8890, 6870, 11232, 9605]
protocols = ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD", "2MAD", "OMAD"]
step_goal = 8000

# BMI CALCULATOR
import math
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

def bmi_category(bmi):
    if bmi < 18.5:
       return 'Underweight'
    elif bmi < 25:
        return 'Normal weight'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

# Input Data
weight = 84
height = 1.78
bmi = calculate_bmi(weight, height)
print(f' Weight: {weight} kg')
print(f' Height: {height} m')
print(f' BMI :{bmi}')
print(f' Status: {bmi_category(bmi)}')

#STEP GOAL CHECKER
def weekly_step_summary(step_list, goal= 8000):
    days_hit = len([s for s in step_list if s >= goal])
    avg = sum(step_list)/ len(step_list)
    best = max(step_list)
    worst = min(step_list)
    return{
        'days_on_goal' : days_hit,
        'total_days' : len(step_list),
        'average' : round(avg),
        'best_day' : best,
        'worst_day' : worst
    }

weekly = [9201, 7700, 10560, 8890, 6870, 11232, 9605]
result = weekly_step_summary(weekly)
print('Step Summary:')
print(f' Days on goal:{result['days_on_goal']}/{result['total_days']}')
print(f' Average: {result['average']} steps')
print(f' Best day: {result[ 'best_day']} steps')
print(f' Worst day: {result['worst_day']} steps')

# CALORIES ESTIMATE
def estimate_calories(steps, calorie_per_step = 0.04):
    calories = steps * calorie_per_step
    return math.floor(calories)

weekly_steps = [9201, 7700, 10560, 8890, 6870, 11232, 9605]
daily_cal = [ estimate_calories (s) for s in  weekly_steps]

print('Estimated calories burned from walking:')
days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
for day, cals in zip(days, daily_cal):
    print(f' {day}: {cals} kcal')
print(f' Total: {sum(daily_cal)} kcal')

# Protocol summary
def protocol_summary(protocol_list):
    unique = list(set(protocol_list))
    summary = {}
    for p in unique:
        summary[p] = protocol_list.count(p)
    return summary
protocols = ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD", "2MAD", "OMAD"]
result = protocol_summary(protocols)
print('Protocol Breakdown:')
for protocol, days in result.items():
    print(f' {protocol} : {days} day (s)')
today = date.today().strftime("%d %B %Y")
steps_report = weekly_step_summary(weekly_steps, step_goal)
total_cals = sum(estimate_calories(s) for s in weekly_steps)
proto_report = protocol_summary(protocols)
print('=' * 42)
print(f' WEEKLY REPORT: {client_name.upper()}')
print(f' Date: {today}')
print('=' * 42)
print(f' \nBODY')
print(f' Weight: {weight_kg} kg')
print(f' BMI  : {bmi}({bmi_category(bmi)})')
print(f' \nSTEPS (Goal: {step_goal})')
print(f' Days on goal : {steps_report['days_on_goal']}/7')
print(f' Average : {steps_report['average']} steps/ day')
print(f' Cals burned : [total_cals] kcal ')
print(f' \nPROTOCOL BREAKDOWN')
for p, d in proto_report.items():
    print(f' {p} : {d} day (s)')
print('\n' + '=' * 42)
