from text import animals_id, animals_text

animals = []


async def question_answer_1(answer):
    global animals
    animals = []
    if answer == 'Индия':
        return animals.append('слон')
    if answer == 'Вьетнам':
        return animals.extend(['попугай', 'тигр'])
    if answer == 'Испания':
        return animals.extend(['альпака', 'саламандра'])
    if answer == 'Китай':
        return animals.extend(['кот', 'медоед'])
    if answer == 'Канада':
        return animals.extend(['волк', 'медведь'])


async def question_answer_2(answer):
    if answer == 'Светлый лес':
        return animals.extend(['лемур', 'медоед', 'саламандра'])
    if answer == 'Горы в гималаях':
        return animals.extend(['слон', 'саламандра'])
    if answer == 'У водоёма':
        return animals.extend(['сова', 'попугай', 'капибара'])
    if answer == 'Широкое поле':
        return animals.extend(['волк', 'тигр'])


async def question_answer_3(answer):
    if answer == 'Мощь и сила':
        return animals.extend(['слон', 'волк', 'медведь'])
    if answer == 'Миролюбивость':
        return animals.extend(['попугай', 'лемур'])
    if answer == 'Осторожность и любознательность':
        return animals.extend(['кот', 'сова'])
    if answer == 'Застенчивость':
        return animals.extend(['альпака', 'капибара'])
    if answer == 'Грациозность':
        return animals.append('тигр')


async def question_answer_4(answer):
    if answer == 'Фрукты':
        return animals.extend(['слон', 'капибара'])
    if answer == 'Орехи':
        return animals.extend(['попугай', 'лемур'])
    if answer == 'Винегрет':
        return animals.append('альпака')
    if answer == 'Мясо':
        return animals.extend(['кот', 'тигр', 'волк', 'медоед'])


async def question_answer_5(answer):
    if answer == 'В коллективе, люблю общение':
        return animals.extend(['слон', 'капибара', 'лемур'])
    if answer == 'В одиночестве, предпочитаю оставаться наедине со своими мыслями':
        return animals.extend(['кот', 'медоед', 'саламандра'])


async def question_answer_6(answer):
    if answer == 'В холоде со снежком':
        return animals.append('попугай')
    if answer == 'В тепле мне куда лучше':
        return animals.extend(['кот', 'саламандра', 'капибара'])
    if answer == 'Не имеет значения, везде хорошо':
        return animals.extend(['волк', 'сова'])


async def question_answer_7(answer):
    if answer == 'Белый':
        return animals.append('медведь')
    if answer == 'Серый':
        return animals.extend(['слон', 'капибара', 'лемур', 'медоед'])
    if answer == 'Зеленый':
        return animals.append('попугай')
    if answer == 'Оранжевый':
        return animals.extend(['кот', 'тигр', 'саламандра'])


async def question_answer_8(answer):
    if answer == 'Искусный рыболов это про меня':
        return animals.extend(['медведь', 'тигр'])
    if answer == 'Рыбалка не моё':
        return animals.extend(['сова', 'альпака', 'попугай'])


async def question_answer_9(answer):
    if answer == 'Люблю вставать пораньше, чтобы побольше успеть':
        return animals.append('лемур')
    if answer == 'По душе поспать, а потом всю ночь бодрствовать':
        return animals.extend(['саламандра', 'сова'])
    if answer == 'Живу в обычном ритме, не отдавая предпочтений':
        return animals.extend(['медведь', 'волк'])


async def question_answer_10(answer):
    if answer == 'Люблю поваляться, чем меньше дел тем лучше':
        return animals.extend(['медведь', 'сова'])
    if answer == 'Стараюсь не сидеть на месте, хочу везде и сразу':
        return animals.extend(['лемур', 'медоед'])


def result_animal():
    n = 0
    animal_result = ''
    for i in (tuple(animals)):
        if animals.count(i) > n:
            animal_result = i
            n = animals.count(i)
    animal_result_id = animals_id[animal_result]
    return animal_result, animal_result_id


#animal, animal_id = result_animal()
#text_share = animals_text[animal]
