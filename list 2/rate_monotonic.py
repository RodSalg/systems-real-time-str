import math

'''
    Student: Thiago Rodrigo Monteiro Salgado
    Professor: Dr. Lucas Cordeiro

    Federal University of Amazonas

    Real Time Systems - Master's degree subject

    Here the algorithm is rate monotonic. For first we gonna make a test to know if is able to schedule.
'''

tasks = [
    {"name": "A", "T": 7, "C": 3, "D": 7},
    {"name": "B", "T": 12, "C": 2, "D": 12},
    {"name": "C", "T": 20, "C": 2, "D": 20},
]

tasks = [
    {"name": "A", "T": 4, "C": 1, "D": 4},
    {"name": "B", "T": 6, "C": 2, "D": 6},
    {"name": "C", "T": 10, "C": 3, "D": 7},
]



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
        print("Verificando escalonabilidade usando tempo de resposta...\n")

        response_times = [t["C"] for t in tasks_sorted]
        iterations = 0
        max_iterations = 100

        while iterations < max_iterations:
            new_response_times = []
            for i, t in enumerate(tasks_sorted):
                interference = sum(
                    math.ceil(response_times[i] / tasks_sorted[j]["T"]) * tasks_sorted[j]["C"]
                    for j in range(i)
                )
                new_response_time = t["C"] + interference
                new_response_times.append(new_response_time)

                print(f"Tarefa {t['name']}: Tempo de resposta = {new_response_time} (Deadline={t['D']})")

                if new_response_time > t["D"]:
                    print(f"Tarefa {t['name']} perdeu deadline. Sistema não escalonável.")
                    return False

            if new_response_times == response_times:
                break
            response_times = new_response_times
            iterations += 1

        print("Todas as tarefas respeitaram os deadlines pelo teste de tempo de resposta.")
        return True
    else:
        print("Sistema escalonável pelo teste de utilização!")
        return True


rate_monotonic(tasks)

TCP = math.lcm(*[t["T"] for t in tasks])
schedule = []

tasks_sorted = sorted(tasks, key=lambda x: x["T"])

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
        current = min(ready_tasks, key=lambda x: x["T"])
        current["remaining"] -= 1
        executed = f"{current['name']}"
    else:
        executed = "Idle"

    schedule.append(f"[Time {time}: {executed}]")

print()
print("Gantt Chart (Rate Monotonic):")
print(" --> ".join(schedule))
