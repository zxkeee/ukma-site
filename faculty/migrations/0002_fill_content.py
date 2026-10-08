from django.db import migrations


def fill_content(apps, schema_editor):
    FacultyInfo = apps.get_model('faculty', 'FacultyInfo')
    Department = apps.get_model('faculty', 'Department')
    Discipline = apps.get_model('faculty', 'Discipline')
    Program = apps.get_model('faculty', 'Program')
    Teacher = apps.get_model('faculty', 'Teacher')

    FacultyInfo.objects.create(
        name='Факультет економічних наук',
        description="""Створений у серпні 2000 року на основі Департаменту економічних наук НаУКМА, Факультет економічних наук готує фахівців-економістів на програмах бакалавра і магістра, а також має аспірантуру. Освітні програми відповідають державним стандартам вищої освіти України, а також сучасним західним стандартам вищої економічної освіти.

Випускники факультету мають високу професійну репутацію на вітчизняних і закордонних ринках праці: працюють у престижних іноземних та вітчизняних фірмах, аудиторських і консалтингових компаніях, провідних банках, науково-дослідних інституціях. Багато з них продовжують навчання в північноамериканських та європейських університетах.

До складу факультету входять три кафедри, на яких працюють визнані в Україні викладачі, переважна більшість яких мають ступені докторів і кандидатів наук. Для практичної роботи студентів створені Лабораторія фінансово-економічних досліджень, навчально-дослідницька лабораторія «Іннолаб» та Креативний маркетинговий центр.""",
        dean='Глущенко Світлана Василівна',
        deputy_dean='Бугрова Олена Олександрівна',
        address='корпус 6, кімната 406',
        phone='(044) 425 60 42, 425 77 37 (факс)',
        email='gluschenkosv@ukma.edu.ua',
    )

    economics = Department.objects.create(
        name='Кафедра економічної теорії',
        head='Біла Ірина Сергіївна',
    )
    finance = Department.objects.create(
        name='Кафедра фінансів',
        head="Лук'яненко Ірина Григорівна",
    )
    management = Department.objects.create(
        name='Кафедра менеджменту, маркетингу та підприємництва',
        head='Пічик Катерина Валеріївна',
    )

    micro = Discipline.objects.create(name='Мікроекономіка')
    macro = Discipline.objects.create(name='Макроекономіка')
    econometrics = Discipline.objects.create(name='Економетрика')
    statistics = Discipline.objects.create(name='Статистика')
    corp_finance = Discipline.objects.create(name='Фінанси підприємств')
    banking = Discipline.objects.create(name='Банківська справа')
    org_management = Discipline.objects.create(name='Менеджмент організацій')
    marketing_d = Discipline.objects.create(name='Маркетинг')

    economy = Program.objects.create(
        name='Економіка',
        code='051',
        description=(
            'Спеціальність «Економіка» є українським аналогом найпоширенішої у світі '
            'економічної спеціальності Economics. Кафедра економічної теорії з 1992 року '
            'формує програму, орієнтуючись на міжнародний освітній канон, тому багато '
            'випускників продовжують навчання в провідних європейських та американських '
            'університетах. Студенти вивчають мікро- та макроекономіку, економетрику, '
            'статистику та методи економічного аналізу. Випускники працюють у міжнародних '
            'організаціях, органах державної влади, консалтингових компаніях, банках '
            'і науково-дослідних інституціях.'
        ),
        coordinator_name='Колосова Ніна Василівна',
        coordinator_contact='(044) 425 60 42',
        department=economics,
    )
    economy.disciplines.add(micro, macro, econometrics, statistics)

    finance_program = Program.objects.create(
        name='Фінанси, банківська справа та страхування',
        code='072',
        description=(
            "Кафедра фінансів готує фінансистів-аналітиків, здатних розв'язувати "
            'нестандартні завдання, приймати ефективні рішення та креативно мислити. '
            'Навчання поєднується з науковою роботою, а кафедра співпрацює '
            'з університетами Норвегії, Франції та Німеччини.'
        ),
        coordinator_name='Донкоглова Наталія Анатоліївна',
        coordinator_contact='(044) 425 60 42',
        department=finance,
    )
    finance_program.disciplines.add(corp_finance, banking, econometrics)

    management_program = Program.objects.create(
        name='Менеджмент',
        code='073',
        description=(
            'Програма готує управлінців, які вміють організовувати роботу команд, '
            'ухвалювати стратегічні рішення та розвивати бізнес. Студенти поєднують '
            'теорію менеджменту з практичними проєктами для підприємств та організацій.'
        ),
        coordinator_name='Ісаєнко Анна Михайлівна',
        coordinator_contact='(044) 425 77 87',
        department=management,
    )
    management_program.disciplines.add(org_management, micro)

    marketing_program = Program.objects.create(
        name='Маркетинг',
        code='075',
        description=(
            'Програма готує маркетологів, які розуміють поведінку споживачів, вміють '
            'досліджувати ринок і будувати маркетингові стратегії. При кафедрі діє '
            'Креативний маркетинговий центр, де студенти виконують реальні проєкти.'
        ),
        coordinator_name='Ісаєнко Анна Михайлівна',
        coordinator_contact='(044) 425 77 87',
        department=management,
    )
    marketing_program.disciplines.add(marketing_d, statistics)

    Teacher.objects.create(name='Біла Ірина Сергіївна', position='завідувач кафедри, доцент', degree='кандидат економічних наук', department=economics)
    Teacher.objects.create(name='Шевченко Олена Олександрівна', position='заступник завідувача, доцент', degree='кандидат економічних наук', department=economics)
    Teacher.objects.create(name='Бажал Юрій Миколайович', position='професор', degree='доктор економічних наук', department=economics)
    Teacher.objects.create(name='Бураковський Ігор Валентинович', position='професор', degree='доктор економічних наук', department=economics)
    Teacher.objects.create(name='Новікова Наталя Леонідівна', position='професор', degree='доктор економічних наук', department=economics)
    Teacher.objects.create(name='Бугрова Олена Олександрівна', position='доцент, заступник декана', degree='кандидат економічних наук', department=economics)
    Teacher.objects.create(name='Іванова Наталя Юріївна', position='доцент', degree='кандидат економічних наук', department=economics)
    Teacher.objects.create(name='Палієнко Тетяна Петрівна', position='старший викладач', degree='доктор філософії з економіки', department=economics)

    Teacher.objects.create(name="Лук'яненко Ірина Григорівна", position='завідувач кафедри, професор', degree='доктор економічних наук', department=finance)
    Teacher.objects.create(name='Івахненков Сергій Володимирович', position='професор', degree='доктор економічних наук', department=finance)
    Teacher.objects.create(name='Кужелєв Михайло Олександрович', position='професор', degree='доктор економічних наук', department=finance)
    Teacher.objects.create(name='Долінський Леонід Борисович', position='професор', degree='доктор економічних наук', department=finance)
    Teacher.objects.create(name='Котіна Ганна Михайлівна', position='доцент', degree='кандидат економічних наук', department=finance)
    Teacher.objects.create(name="Слав'юк Наталія Ростиславівна", position='доцент', degree='кандидат економічних наук', department=finance)
    Teacher.objects.create(name='Сова Євгеній Станіславович', position='старший викладач', degree='доктор філософії (PhD)', department=finance)

    Teacher.objects.create(name='Пічик Катерина Валеріївна', position='завідувач кафедри, доцент', degree='кандидат економічних наук', department=management)
    Teacher.objects.create(name='Боднар Ольга Василівна', position='професор', degree='доктор економічних наук', department=management)
    Teacher.objects.create(name='Ковшова Ірина Олегівна', position='професор', degree='доктор економічних наук', department=management)
    Teacher.objects.create(name='Россоха Володимир Васильович', position='професор', degree='доктор економічних наук', department=management)
    Teacher.objects.create(name='Гавриленко Тетяна Володимирівна', position='доцент', degree='кандидат економічних наук', department=management)
    Teacher.objects.create(name='Сербенівська Аліна Юріївна', position='доцент', degree='кандидат економічних наук', department=management)
    Teacher.objects.create(name='Демчук Зоя Олегівна', position='старший викладач', degree='кандидат економічних наук', department=management)


def remove_content(apps, schema_editor):
    FacultyInfo = apps.get_model('faculty', 'FacultyInfo')
    Department = apps.get_model('faculty', 'Department')
    Discipline = apps.get_model('faculty', 'Discipline')

    FacultyInfo.objects.all().delete()
    Department.objects.all().delete()
    Discipline.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fill_content, remove_content),
    ]