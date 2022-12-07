#3 - В файле, содержащем фамилии студентов и их оценки, 
# изменить на прописные буквы фамилии тех студентов, 
# которые имеют средний балл более «4»



from typing import List

def get_list_data(filename: str) -> List[str]:
    with open(filename, encoding='utf-8') as file:
        return file.read().split('\n')
    
def elements_to_caps(lst: list, trigger_str: str) -> List[str]:
    for i in range(len(lst)):
        if trigger_str in lst[i]:
            lst[i].upper()
    return lst

lst = get_list_data('G:\Учеба\python dz\seminar 4\DZ4\DZ\DZ4-3.txt')

print(elements_to_caps(lst, '5'))

with open('G:\Учеба\python dz\seminar 4\DZ4\DZ\DZ4-3.txt', 'w', encoding='utf-8') as data:
    for i in range(len(lst)):
        data.writelines(f'{lst[i]}\n')