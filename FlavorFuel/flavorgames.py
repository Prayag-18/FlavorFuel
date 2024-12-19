from flavorfuel import *

datamain=get_recipes(page_size=100)

def higher_or_lower(data):
    attrs=["img_url","Calories","Recipe_title","Continent","Sub_region"]


    r1=get_attributes(get_random_recipe(data),attrs)
    r2=get_attributes(get_random_recipe(data),attrs)

    while r1==r2:
        r2=get_random_recipe(data)

    return r1,r2
    
def guess_the_continent(data):
    attrs=["img_url","Recipe_title","Continent","Sub_region"]
    r1=get_attributes(get_random_recipe(data),attrs)

    return r1


r1,r2=higher_or_lower(datamain)
print(r1,r2)