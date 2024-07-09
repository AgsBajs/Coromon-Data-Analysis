# Add you code here
# Lab 8 and random module 4.3
import random
with open ('CoromonDataset.csv','r') as f:
    lines = f.readlines()
    coromon_count = 0
    
    #Heading is index 0 - data starts after
    header = lines[0]
    heading = header.strip().split(',')
    
    #Creating a split in the file to announce Coromon - A
    for line in lines[1:]:
        coromon_count += 1

    print('Total Coromon that Exist-> ',coromon_count)

    #Making a random Coromon and Information Appear - B
    rand_coromon = random.randint(0,coromon_count-1)
    random_coromon = lines[rand_coromon+1]

    print('A Random Coromon:',random_coromon)
    print('Types of Coromon:')

    # Different Types of Coromon - C
    type_index = heading.index('Type')
    all_types = []
    for line in lines[1:]:
        data_for_type = line.strip().split(',')
        coromon_types = data_for_type[type_index]
        if coromon_types not in all_types:
            all_types.append(coromon_types)

    print(all_types)

    # Each Coromon Type and Average value for each property - D
    average_coromon_type = {}

    for line in lines[1:]:
        data = line.strip().split(',')
        coromon_name = data[0]
        coromon_type = data[1]

        if coromon_type not in average_coromon_type:
            average_coromon_type[coromon_type] = {'total_health': 0, 'total_attack': 0, 'total_special_attack': 0, 'total_defense':0,'total_special_defense':0, 'total_speed':0, 'total_stamina':0, 'count':0}

        health = int(data[2])
        attack = int(data[3])
        special_attack = int(data[4])
        defense = int(data[5])
        special_defense = int(data[6])
        speed = int(data[7])
        stamina = int(data[8])

        average_coromon_type[coromon_type]['total_health'] += health
        average_coromon_type[coromon_type]['total_attack'] += attack
        average_coromon_type[coromon_type]['total_special_attack'] += special_attack
        average_coromon_type[coromon_type]['total_defense'] += defense
        average_coromon_type[coromon_type]['total_special_defense'] += special_defense
        average_coromon_type[coromon_type]['total_speed'] += speed
        average_coromon_type[coromon_type]['total_stamina'] += stamina
        average_coromon_type[coromon_type]['count'] += 1

# Displaying average values for each property for each Common type
    for coromon_type, properties in average_coromon_type.items():
        print(f'Average properties for {coromon_type}:')
        print(f'Average Health: {properties["total_health"] / properties["count"]}')
        print(f'Average Attack: {properties["total_attack"] / properties["count"]}')
        print(f'Average Special Attack: {properties["total_special_attack"] / properties["count"]}')
        print(f'Average Defense: {properties["total_defense"] / properties["count"]}')
        print(f'Average Special Defense: {properties["total_special_defense"] / properties["count"]}')
        print(f'Average Speed: {properties["total_speed"] / properties["count"]}')
        print(f'Average Stamina: {properties["total_stamina"] / properties["count"]}')
        print()

    #Coromon with highest average Health Points - E
    coromon_health_dict = {}
    
    for line in lines[1:]:
        data = line.strip().split(',')
        coromon_type = data[1]
        health_points = int(data[2])
        if coromon_type not in coromon_health_dict:
            coromon_health_dict[coromon_type] = {'total_health': 0, 'count': 0}

        coromon_health_dict[coromon_type]['total_health'] += health_points
        coromon_health_dict[coromon_type]['count'] += 1

    highest_average_coromon = None
    highest_average = 0

    for coromon_type, data in coromon_health_dict.items():
        average_health = data['total_health'] / data['count']
        if average_health > highest_average:
            highest_average = average_health
            highest_average_coromon = coromon_type

    print('\nCoromon with the highest average Health Points:', highest_average_coromon)
    print('Highest average Health Points:', highest_average,)
        
    # Coromon Lowest Average Health - F
    lowest_coromon_health = {}

    lowest_coromon_average = None
    lowest_average = float(1000000000)

    for coromon_type, data in coromon_health_dict.items():
        average_health = data['total_health'] / data['count']
        if average_health < lowest_average:
            lowest_average = average_health
            lowest_coromon_average = coromon_type

    print('Coromon with the lowest average Health Points:', lowest_coromon_average)
    print('Lowest average Health Points:', lowest_average,'\n')

    #Highest Average Attack Points - G
    highest_average_attack_dict = {}

    for line in lines[1:]:
        data = line.strip().split(',')
        coromon_type = data[1]
        attack_points = int(data[3])
        if coromon_type not in highest_average_attack_dict:
            highest_average_attack_dict[coromon_type] = {'total_attack': 0, 'count': 0}

        highest_average_attack_dict[coromon_type]['total_attack'] += attack_points
        highest_average_attack_dict[coromon_type]['count'] += 1

    highest_average__attack_coromon = None
    highest_average_attack = 0

    for coromon_type, data in highest_average_attack_dict.items():
        average_attack = data['total_attack'] / data['count']
        if average_attack > highest_average_attack:
            highest_average_attack = average_attack
            highest_average_attack_coromon = coromon_type
    
    print('Coromon with the highest average Attack Points:', highest_average_attack_coromon)
    print('Highest average Attack Points:', highest_average_attack)

    #Lowest Average Attack Points - H
    lowest_average_attack_dict = {}

    for line in lines[1:]:
        data = line.strip().split(',')
        coromon_type = data[1]
        attack_points = int(data[3])
        if coromon_type not in lowest_average_attack_dict:
            lowest_average_attack_dict[coromon_type] = {'total_attack': 0, 'count': 0}

        lowest_average_attack_dict[coromon_type]['total_attack'] += attack_points
        lowest_average_attack_dict[coromon_type]['count'] += 1

    lowest_attack_average = None
    lowest_attack_average_num = float(1000000000)

    for coromon_type, data in lowest_average_attack_dict.items():
        average_attack = data['total_attack'] / data['count']
        if average_attack < lowest_attack_average_num:
            lowest_attack_average_num = average_attack
            lowest_average_attack_coromon = coromon_type

    print('Coromon with the lowest average Attack Points:',lowest_average_attack_coromon)
    print('Lowest average Attack Points:',lowest_attack_average_num,'\n')

    #Highest Average Special Attack Points - I
    highest_average_special_dict = {}

    for line in lines[1:]:
        data = line.strip().split(',')
        coromon_type = data[1]
        special_points = int(data[4])
        if coromon_type not in highest_average_special_dict:
            highest_average_special_dict[coromon_type] = {'total_special': 0, 'count': 0}

        highest_average_special_dict[coromon_type]['total_special'] += special_points
        highest_average_special_dict[coromon_type]['count'] += 1

    highest_average__special_coromon = None
    highest_average_special = 0

    for coromon_type, data in highest_average_special_dict.items():
        average_special = data['total_special'] / data['count']
        if average_special > highest_average_special:
            highest_average_special = average_special
            highest_average_special_coromon = coromon_type
    
    print('Coromon with the highest average Special Attack Points:', highest_average_special_coromon)
    print('Highest average Special Attack Points:', highest_average_special)

    #Lowest Average Special Attack Points - J
    lowest_average_special_dict = {}

    for line in lines[1:]:
        data = line.strip().split(',')
        coromon_type = data[1]
        special_points = int(data[4])
        if coromon_type not in lowest_average_special_dict:
            lowest_average_special_dict[coromon_type] = {'total_special': 0, 'count': 0}

        lowest_average_special_dict[coromon_type]['total_special'] += special_points
        lowest_average_special_dict[coromon_type]['count'] += 1

    lowest_average__special_coromon = None
    lowest_average_special = float(1000000)

    for coromon_type, data in lowest_average_special_dict.items():
        average_special = data['total_special'] / data['count']
        if average_special < lowest_average_special:
            lowest_average_special = average_special
            lowest_average_special_coromon = coromon_type
    
    print('Coromon Type with the lowest average Special Attack Points:',lowest_average_special_coromon)
    print('Lowest average Special Attack Points:', lowest_average_special,'\n')

    #Highest Average Defense Points - K
    highest_average_defense_dict = {}

    for line in lines [1:]:
        data = line.strip().split(',')
        coromon_type = data[1]
        defense_points = int(data[5])
        if coromon_type not in highest_average_defense_dict:
            highest_average_defense_dict[coromon_type] = {'total_defense': 0, 'count': 0}

        highest_average_defense_dict[coromon_type]['total_defense'] += defense_points
        highest_average_defense_dict[coromon_type]['count'] += 1

    highest_average__defense_coromon = None
    highest_average_defense = 0

    for coromon_type, data in highest_average_defense_dict.items():
        average_defense = data['total_defense'] / data['count']
        if average_defense > highest_average_defense:
            highest_average_defense = average_defense
            highest_average_defense_coromon = coromon_type
    
    print('Coromon with the highest average Defense Points:', highest_average_defense_coromon)
    print('Highest average Defense Points:', highest_average_defense)

    #Lowest Average Defense Points - L
    lowest_average_defense_dict = {}

    for line in lines[1:]:
        data = line.strip().split(',')
        coromon_type = data[1]
        defense_points = int(data[5])
        if coromon_type not in lowest_average_defense_dict:
            lowest_average_defense_dict[coromon_type] = {'total_defense': 0, 'count': 0}

        lowest_average_defense_dict[coromon_type]['total_defense'] += special_points
        lowest_average_defense_dict[coromon_type]['count'] += 1

    lowest_average__defense_coromon = None
    lowest_average_defense = float(1000000)

    for coromon_type, data in lowest_average_defense_dict.items():
        average_defense = data['total_defense'] / data['count']
        if average_defense < lowest_average_defense:
            lowest_average_defense = average_defense
            lowest_average_defense_coromon = coromon_type
    
    print('Coromon with the lowest average Defense Points:',lowest_average_defense_coromon)
    print('Lowest average Defense Points:', lowest_average_defense,'\n')

    #Highest Average Special Defense Points - M
    highest_average_special_defense_dict = {}

    for line in lines [1:]:
        data = line.strip().split(',')
        coromon_type = data[1]
        special_defense_points = int(data[6])
        if coromon_type not in highest_average_special_defense_dict:
            highest_average_special_defense_dict[coromon_type] = {'total_special_defense': 0, 'count': 0}

        highest_average_special_defense_dict[coromon_type]['total_special_defense'] += special_defense_points
        highest_average_special_defense_dict[coromon_type]['count'] += 1

    highest_average__special_defense_coromon = None
    highest_average_special_defense = 0

    for coromon_type, data in highest_average_special_defense_dict.items():
        average_special_defense = data['total_special_defense'] / data['count']
        if average_special_defense > highest_average_special_defense:
            highest_average_special_defense = average_special_defense
            highest_average_special_defense_coromon = coromon_type
    
    print('Coromon with the highest average Special Defense Points:', highest_average_special_defense_coromon)
    print('Highest average Special Defense Points:', highest_average_special_defense)

    #Lowest Average Special Defense Points - N
    lowest_average_special_defense_dict = {}

    for line in lines[1:]:
        data = line.strip().split(',')
        coromon_type = data[1]
        special_defense_points = int(data[6])
        if coromon_type not in lowest_average_special_defense_dict:
            lowest_average_special_defense_dict[coromon_type] = {'total_special_defense': 0, 'count': 0}

        lowest_average_special_defense_dict[coromon_type]['total_special_defense'] += special_defense_points
        lowest_average_special_defense_dict[coromon_type]['count'] += 1

    lowest_average__special_defense_coromon = None
    lowest_average_special_defense = float(1000000)

    for coromon_type, data in lowest_average_special_defense_dict.items():
        average_special_defense = data['total_special_defense'] / data['count']
        if average_special_defense < lowest_average_special_defense:
            lowest_average_special_defense = average_special_defense
            lowest_average_special_defense_coromon = coromon_type
    
    print('Coromon with the lowest average Special Defense Points:',lowest_average_special_defense_coromon)
    print('Lowest average Special Defense Points:', lowest_average_special_defense,'\n')

    #Highest Average Speed Points - O
    highest_average_speed_dict = {}

    for line in lines [1:]:
        data = line.strip().split(',')
        coromon_type = data[1]
        speed_points = int(data[7])
        if coromon_type not in highest_average_speed_dict:
            highest_average_speed_dict[coromon_type] = {'total_speed': 0, 'count': 0}

        highest_average_speed_dict[coromon_type]['total_speed'] += speed_points
        highest_average_speed_dict[coromon_type]['count'] += 1

    highest_average__speed_coromon = None
    highest_average_speed = 0

    for coromon_type, data in highest_average_speed_dict.items():
        average_speed = data['total_speed'] / data['count']
        if average_speed > highest_average_speed:
            highest_average_speed = average_speed
            highest_average_speed_coromon = coromon_type
    
    print('Coromon with the highest average Speed:', highest_average_speed_coromon)
    print('Highest average Speed:', highest_average_speed)

    #Lowest Average Speed Points - P
    lowest_average_speed_dict = {}

    for line in lines[1:]:
        data = line.strip().split(',')
        coromon_type = data[1]
        speed_points = int(data[7])
        if coromon_type not in lowest_average_speed_dict:
            lowest_average_speed_dict[coromon_type] = {'total_speed': 0, 'count': 0}

        lowest_average_speed_dict[coromon_type]['total_speed'] += speed_points
        lowest_average_speed_dict[coromon_type]['count'] += 1

    lowest_average__speed_coromon = None
    lowest_average_speed = float(1000000)

    for coromon_type, data in lowest_average_speed_dict.items():
        average_speed = data['total_speed'] / data['count']
        if average_speed < lowest_average_speed:
            lowest_average_speed = average_speed
            lowest_average_speed_coromon = coromon_type
    
    print('Coromon with the lowest average Speed Points:',lowest_average_speed_coromon)
    print('Lowest average Speed Points:', lowest_average_speed)
