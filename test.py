# import pandas as pd
# from salads_dataset import create_salad_df_from_initial_df, save_df_csv, get_salad_dataset
# from dataset_helper import change_df_ingredients_column_to_list
# from dataset_analyzer import ingrident_counter, get_recipes_with_ingredients
# pd.set_option('display.max_columns', None)     
# pd.set_option('display.max_colwidth', None)     
# pd.set_option('display.width', None)  \

# #DATA_PATH = "/home/hboua/GitRepo/Data"
# DATA_PATH = "C:/Users/yassi/Desktop/Projet/CookBotProject/CookBotRecipes/Data"

# column_list = ['name', 'tags', 'description', 'ingredients']
# df = create_salad_df_from_initial_df(DATA_PATH,column_list)

# dic = ingrident_counter(df)

# def get_n_ingredients(n):
#     count = 0
#     ingredients_list = []
#     for elem in dic: 
#         count += 1
#         ingredients_list.append(elem)
#         if(count == n):
#             return ingredients_list
        

# keep_ingredients = ['salt', 'sugar', 'mayonnaise' , 'pepper', 'tomatoes', 'celery', 'onion', 'garlic', 'water', 'black pepper', 'honey', 'cucumber', 'balsamic vinegar', 'green onion', 'sour cream', 'vegetable oil', 'carrot', 'fresh lemon juice', 'fresh ground black pepper', 'fresh parsley', 'vinegar', 'bacon', 'parmesan cheese', 'red bell pepper', 'feta cheese', 'romaine lettuce', 'cider vinegar', 'soy sauce', 'white wine vinegar', 'garlic powder', 'parsley', 'cherry tomatoes', 'fresh cilantro', 'walnuts', 'hard-boiled eggs', 'lime juice', 'carrots', 'fresh basil', 'lettuce', 'avocado', 'paprika', 'white vinegar', 'black olives', 'kosher salt', 'green pepper', 'cilantro', 'sesame oil', 'pecans', 'dry mustard', 'eggs', 'rice vinegar', 'cucumbers', 'oil', 'fresh ground pepper', 'worcestershire sauce', 'scallions', 'cheddar cheese', 'fresh lime juice', 'canola oil', 'ground cumin', 'apple cider vinegar', 'salt & freshly ground black pepper', 'orange juice', 'red pepper', 'raisins', 'potatoes', 'black beans', 'blue cheese', 'butter', 'cabbage', 'cayenne pepper', 'sea salt', 'celery seed', 'cooked chicken', 'onions', 'sesame seeds', 'brown sugar', 'dried oregano', 'ground black pepper', 'green bell pepper', 'fresh dill', 'mandarin oranges', 'of fresh mint', 'crushed pineapple', 'fresh ginger', 'lemon, juice of', 'shallot', 'slivered almonds', 'curry powder', 'capers']


# ingredient_keywords = ['lemon','almond', 'oil', 'onion', 'mustard','vinegar','garlic','black pepper', 'bell pepper', 'olives', 'salt','lettuce', 'lime','sugar','orange','pineapple']
# #for the oil there is sesamy oil that needs to stay as he is, see how to add this to the algo

# # passe secondaire enlever tous les mots descriptif
# # ex: fresh 
# # don't forget the space 
# descriptive_keywords = ['fresh']

# #This step needs to be done after the one above 
# replace_ingredients = {
#     'salt and pepper':['black pepper', 'salt'],
#     'salt & freshly ground black pepper':['black pepper', 'salt'],
#     'lime':'lemon',
#     'kosher salt':'salt',
#     'green pepper':'bell pepper',
#     'ground pepper':'black pepper'

# }

# keywords = ['onion']
# for index, row in df.iterrows():
#     recipe_ingredients = row['ingredients']
#     modified_ingredients = []
#     for ingredient in recipe_ingredients:
#         words = ingredient.split()
#         for keyword in keywords:
#             if(keyword in words):
#                 modified_ingredients.append(keyword)
#                 break
#         modified_ingredients.append(ingredient)
#     break



# dict_old_new_value = {
#     'salt and pepper':['black pepper', 'salt'],
#     'salt & freshly ground black pepper':['black pepper', 'salt'],
#     'lime':'lemon',
#     'kosher salt':'salt',
#     'green pepper':'bell pepper',
#     'ground pepper':'black pepper'

# }
keywords = ['fresh']
recipe_ingredients = ['london broil beef','salt and fresh pepper','fresh salt & freshly ground black pepper','lime fresh'] #,'kosher salt', 'red potatoes', 'purple onion', 'scallions', 'butter lettuce', 'olive oil', 'red onion','onion onion', 'kjdsnfiqsdfj djfnjwxf xwhjcvcx onio onion dsfjnqsif dsjfnis wxnjfn ']
modified_ingredients = []
for ingredient in recipe_ingredients:
    words = ingredient.split()
    was_replaced = False
    for keyword in keywords:
        if(keyword in words):
            new_words = []
            for word in words:
                if word != keyword:
                    new_words.append(word)
            final_word = new_sentence = ' '.join(new_words).strip()
            modified_ingredients.append(final_word)
            was_replaced = True
            break
    if not was_replaced:
        modified_ingredients.append(ingredient)
    
            
print(modified_ingredients)