'''
Dict --> Mutable {"name": "Shivam", "Age" : 28}
- we can change the value for a particular key 
- we can add more entries
- we can remove some of the entries

Remember the key should be immutable 

'''

word_dict = {'Intelligent' : "Bhudhimaan",
             'Fool' : 'Bewakoof',
             'Rich' : "Ameer",
             'Car' : 'Gaadi'
            }

print(word_dict)

for key , value in word_dict.items():
    print(f'English : {key} \nHindi : {value}' )


