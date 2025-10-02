import math
'''
    Student: Thiago Rodrigo Monteiro Salgado
    Professor: Dr. Lucas Cordeiro

    Federal University of Amazonas

    Real Time Systems - Master's degree subject

    t code implements periodic task scheduling using algorithms 
      Rate Monotonic (RM);
      Deadline Monotonic (DM);
      Earliest Deadline First (EDF) and; 
      Least Laxity (LL);
'''


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
        rate_monotonic(tasks)
    elif choice == 2:
        deadline_monotonic(tasks)
    elif choice == 3:
        earliest_deadline_first(tasks)
    elif choice == 4:
        least_laxity(tasks)
    else:
        print("Opção inválida!")

main()
