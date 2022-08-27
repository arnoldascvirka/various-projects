# Template veikimas


from string import Template

sablonas = Template('Sveiki, $vardas, jus laimėjote $suma')

param = [{'vardas': 'Adomas', 'suma': '100'},
         {'vardas': 'Almantas', 'suma': '101'}
         ]

for zod in param:
    print(sablonas.substitute(zod))
