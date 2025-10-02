import math

def rate_monotonic(tasks):
    tasks_sorted = sorted(tasks, key=lambda x: x["T"])
    print("Prioridade RM (menor T = maior prioridade):")
    for t in tasks_sorted:
        print(f"Tarefa {t['name']} : Período = {t['T']} | C = {t['C']} | D = {t['D']}")

    utilization = sum(t["C"] / t["T"] for t in tasks_sorted)
    print(f"\nUtilização Total: {utilization:.4f}")
    
    n = len(tasks_sorted)
    threshold = n * (2**(1/n) - 1)
    print(f"Limite de Escalonabilidade: {threshold:.4f}")
    
    if utilization > threshold:
        print("Sistema NÃO garantidamente escalonável pelo teste de utilização.")
        return False
    else:
        print("Sistema escalonável pelo teste de utilização!")
        return True

def deadline_monotonic(tasks):
    tasks_sorted = sorted(tasks, key=lambda x: x["D"])
    print("Prioridade DM (menor deadline = maior prioridade):")
    for t in tasks_sorted:
        print(f"Tarefa {t['name']} : Período = {t['T']} | C = {t['C']} | D = {t['D']}")
    
    return True

def earliest_deadline_first(tasks):
    tasks_sorted = sorted(tasks, key=lambda x: x["D"]) 
    print("Prioridade EDF (menor deadline = maior prioridade):")
    for t in tasks_sorted:
        print(f"Tarefa {t['name']} : Período = {t['T']} | C = {t['C']} | D = {t['D']}")
    
    utilization = sum(t["C"] / t["T"] for t in tasks_sorted)
    if utilization <= 1:
        print("Sistema escalonável pelo teste de utilização!")
        return True
    else:
        print("Sistema NÃO escalonável pelo teste de utilização.")
        return False

def least_laxity(tasks):
    tasks_sorted = sorted(tasks, key=lambda x: (x["D"] - x["C"]))
    print("Prioridade Least Laxity (menor laxity = maior prioridade):")
    for t in tasks_sorted:
        print(f"Tarefa {t['name']} : Período = {t['T']} | C = {t['C']} | D = {t['D']}")
    
    return True

def print_schedule(tasks, algorithm_name):
    TCP = math.lcm(*[t["T"] for t in tasks]) 
    schedule = ['Idle' for _ in range(TCP)]
    
    tasks_sorted = sorted(tasks, key=lambda x: x["T"] if algorithm_name == "RM" else x["D"])
    for t in tasks_sorted:
        t["next_release"] = 0
        t["remaining"] = 0
    
    for time in range(TCP):
        for t in tasks_sorted:
            if time == t["next_release"]:
                t["remaining"] = t["C"]
                t["next_release"] += t["T"]
        
        ready_tasks = [t for t in tasks_sorted if t["remaining"] > 0]
        if ready_tasks:
            current = min(ready_tasks, key=lambda x: x["T"] if algorithm_name == "RM" else x["D"])
            current["remaining"] -= 1
            executed = f"{current['name']}"
        else:
            executed = "Idle"

        schedule[time] = f"{executed}"

    print(f"\nGantt Chart ({algorithm_name}):")
    print(" --> ".join([f"Time {time}: {task}" for time, task in enumerate(schedule)]))

def main():
    print("Escolha o algoritmo de escalonamento:")
    print("1. Rate Monotonic (RM)")
    print("2. Deadline Monotonic (DM)")
    print("3. Earliest Deadline First (EDF)")
    print("4. Least Laxity (LL)")
    choice = int(input("Digite o número do algoritmo desejado: "))

    tasks = [
        {"name": "T1", "T": 10, "C": 3, "D": 10},
        {"name": "T2", "T": 10, "C": 3, "D": 10},
        {"name": "T3", "T": 10, "C": 3, "D": 10},
        {"name": "T4", "T": 100, "C": 2, "D": 100},
    ]

    if choice == 1:
        if rate_monotonic(tasks):
            print_schedule(tasks, "RM")
    elif choice == 2:
        if deadline_monotonic(tasks):
            print_schedule(tasks, "DM")
    elif choice == 3:
        if earliest_deadline_first(tasks):
            print_schedule(tasks, "EDF")
    elif choice == 4:
        if least_laxity(tasks):
            print_schedule(tasks, "LL")
    else:
        print("Opção inválida!")

main()
