animals = []
animals_id = {
    'слон': 'CgACAgQAAxkBAAPEZn_ADDdRPwenF-kj-jr0H_3E0-wAAtwCAAJ9GwxTaNnqYwZS5q81BA',
    'волк': 'CgACAgQAAxkBAAPjZn_C5XcW8tEIEBlbezOIrbdb8PkAAsoDAAJ0vr1TBLUgr1mGCdI1BA',
    'сова': 'CgACAgQAAxkBAAPnZn_DLLiOyFn8KeihmklSL8YZPJUAAkEDAAL4TwRTKIxYiSchRKc1BA',
    'попугай': 'CgACAgQAAxkBAAIBtmaGM9DsdYQiUzTOehTvFcCz0pOiAAJXAwACcf98U913WFXs7viyNQQ',
    'тигр': 'CgACAgQAAxkBAAIBt2aGNBf2Igx7dAJvIdlAyjDfx0ggAAKOBAACRFL0UqRfM-L-WeHSNQQ',
    'альпака': 'CgACAgQAAxkBAAIBuGaGNEmlyZvQvSJT_3zHhf20e5XQAAK4AgAClH1MUx3EbUUB2gVQNQQ',
    'саламандра': 'CgACAgQAAxkBAAIBuWaGNIuItN6EbX1__aJH96TuEebBAALHBAACsCn8UxU-yEbZ0v6bNQQ',
    'кот': 'CgACAgQAAxkBAAIBumaGNL3R2vdeeq8VFVo_jjfloUMFAAIdAwACgtUEUwUmdX38GQFGNQQ',
    'медоед': 'CgACAgQAAxkBAAIBu2aGNOJ9GafCpZyUAXYFw1kOBQINAAL-AgAC21oNU-fAx0THMgkINQQ',
    'медведь': 'CgACAgQAAxkBAAIBvGaGNPpw0U_H88HmOtbDk6YAAfHAFgACWAMAAsevJFN-_3Yp9IQnfzUE',
    'лемур': 'CgACAgQAAxkBAAIBvWaGNT-vlCHUF4S1m7rvvvgZ9WqQAAKuAwACSNHEUWzNpIwzIjozNQQ',
    'капибара': 'CgACAgQAAxkBAAIBvmaGNVHJoiQ-o9uyy1OWbn1P3n0iAAJGBAACQT08UD64C7HJNhoVNQQ'
}
link_text = 'https://moscowzoo.ru/about/guardianship'


def question_answer_1(answer):
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


def question_answer_2(answer):
    if answer == 'Светлый лес':
        return animals.extend(['лемур', 'медоед', 'саламандра'])
    if answer == 'Горы в гималаях':
        return animals.extend(['слон', 'саламандра'])
    if answer == 'У водоёма':
        return animals.extend(['сова', 'попугай', 'капибара'])
    if answer == 'Широкое поле':
        return animals.extend(['волк', 'тигр'])


def question_answer_3(answer):
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


def question_answer_4(answer):
    if answer == 'Фрукты':
        return animals.extend(['слон', 'капибара'])
    if answer == 'Орехи':
        return animals.extend(['попугай', 'лемур'])
    if answer == 'Винегрет':
        return animals.append('альпака')
    if answer == 'Мясо':
        return animals.extend(['кот', 'тигр', 'волк', 'медоед'])


def question_answer_5(answer):
    if answer == 'В коллективе, люблю общение':
        return animals.extend(['слон', 'капибара', 'лемур'])
    if answer == 'В одиночестве, предпочитаю оставаться наедине со своими мыслями':
        return animals.extend(['кот', 'тигр', 'медоед', 'саламандра'])


def question_answer_6(answer):
    if answer == 'В холоде со снежком':
        return animals.extend(['попугай', 'тигр'])
    if answer == 'В тепле мне куда лучше':
        return animals.extend(['кот', 'саламандра', 'капибара'])
    if answer == 'Не имеет значения, везде хорошо':
        return animals.extend(['волк', 'сова'])


def question_answer_7(answer):
    if answer == 'Белый':
        return animals.extend(['альпака', 'медведь'])
    if answer == 'Серый':
        return animals.extend(['слон', 'капибара', 'лемур', 'медоед'])
    if answer == 'Зеленый':
        return animals.append('попугай')
    if answer == 'Оранжевый':
        return animals.extend(['кот', 'тигр', 'саламандра'])


def question_answer_8(answer):
    if answer == 'Искусный рыболов это про меня':
        return animals.extend(['медведь', 'тигр'])
    if answer == 'Рыбалка не моё':
        return animals.extend(['сова', 'альпака', 'попугай'])


def question_answer_9(answer):
    if answer == 'Люблю вставать пораньше, чтобы побольше успеть':
        return animals.append('лемур')
    if answer == 'По душе поспать, а потом всю ночь бодрствовать':
        return animals.extend(['саламандра', 'сова'])
    if answer == 'Живу в обычном ритме, не отдавая предпочтений':
        return animals.extend(['медведь', 'волк'])


def question_answer_10(answer):
    if answer == 'Люблю поваляться, чем меньше дел тем лучше':
        return animals.extend(['слон', 'медведь', 'сова'])
    if answer == 'Стараюсь не сидеть на месте, хочу везде и сразу':
        return animals.extend(['лемур', 'медоед'])


def result_animal():
    global animals
    print(animals)
    n = 0
    animal = ''
    for i in (tuple(animals)):
        if animals.count(i) > n:
            animal = i
    animal_id = animals_id[animal]
    animals = []
    return animal, animal_id
