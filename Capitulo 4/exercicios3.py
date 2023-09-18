import numpy as np

dataset = np.loadtxt('arquivos/space.csv', delimiter=';', dtype=str, encoding='utf-8')
#print(dataset[0,:])
# Num      - Company Name   - Location     - Datum                     - Detail   - Status Rocket              - Cost  - Status Mission
# 0 a 4323 - US Navy        - Site 1/5 USA - Fri Aug 07 2020 05:12 UTC - Falcon 9 - StatusActive/StatusRetired - 29.75 - Success/Failure

# Apresente a porcentagem de quantas missões deram certo
print("---------- 1 ----------")

success_count = np.sum(dataset[:,7] == "Success")
total_missions = len(dataset) - 1
success_percentage = (success_count / total_missions) * 100

print(f"Porcentagem de missoes que deram certo: {success_percentage:.2f}%")

# Qual a média de gastos de uma missão espacial se baseando em missões que possuem valores disponíveis (>0)?
print("\n---------- 2 ----------")

mask = dataset[1:,6]
integer_mask = mask.astype(float)
cost_sum = np.sum(integer_mask[integer_mask > 0])
cost_avg = cost_sum / total_missions

print(f"Media dos gastos: {cost_avg:.2f}")

# Encontre quantas missões espaciais neste DataSet foram realizadas pelos Estados Unidos (USA).
print("\n---------- 3 ----------")

locations = dataset[:, 2]
result = np.char.find(locations, 'USA')
loc_sum = len(locations[result >= 0])

print("Numero de missoes pelos Estados Unidos: ", loc_sum)

# Encontre qual foi a missão mais cara realizada pela empresa "SpaceX".
print("\n---------- 4 ----------")

mission = dataset[dataset[:,1] == "SpaceX"]
costs = mission[1:,6].astype(float)
max_cost_mission = mission[np.argmax(costs) + 1]

print("Missão da SpaceX com maior custo:\n", max_cost_mission)

# Mostre o nome das empresas que já realizaram Missões Espaciais juntamente com suas respectivas quantidades de missões (use for para mostrar informações).
print("\n---------- 5 ----------")

mission_count = np.unique(dataset[1:,1], return_counts=True)
companies = mission_count[0]
amount = mission_count[1]

for i in range(len(companies)):
    print("Empresa: ", companies[i], " - Quantidade missoes: ", amount[i])