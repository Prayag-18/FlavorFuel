import requests
import json
import random

request_names=[
    "recipeOftheDay",
    "recipeld",
    "regions",
    "sub-regions",
    "continents",
    "recipe-title",
    "ingredients",
    "categories",
    "processes",
    "utensils",
    "recipesAdvanced",
    "recipesByNutrition",
    "recipesByIngredient"
]

url = "https://cosylab.iiitd.edu.in/recipe/recipeOftheDay"

# Sending the GET request
def request_api(url, params={}, post_data=None):
    try:
        # Determine the request type based on `post_data`
        if post_data is None:
            response = requests.get(url, params=params)
        else:
            response = requests.post(url, json=post_data)

        # Check for HTTP errors (4xx and 5xx responses)
        if response.status_code != 200:
            print(f"Request failed with status code: {response.status_code}")
            print(f"Response text: {response.text}")
            return None

        # Try to parse the JSON response
        try:
            response_data = response.json()
        except ValueError:
            print("Failed to parse response as JSON.")
            return None

        # Check if the "payload" key exists in the JSON response
        if "payload" in response_data:
            return response_data["payload"]
        else:
            print("Key 'payload' not found in the response.")
            return None

    except requests.exceptions.RequestException as re:
        # Handle network-related errors like connection issues, timeouts, etc.
        print(f"Network error occurred: {re}")
        return None
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


def get_recipes(page=1,page_size=10,continent="",region="",sub_region="",recipie_title="",
               ingredient_used="",ingredient_not_used="",utensil="",cooking_process="",
               energy_min=0,energy_max=0,carb_min=0,carb_max=0,fat_min=0,fat_max=0,protien_min=0,protien_max=0):
    
    base_url = "https://cosylab.iiitd.edu.in/recipe-search/recipesAdvanced"

    # Variables for page and pageSize

    # Construct the full URL with query parameters
    url = f"{base_url}?page={page}&pageSize={page_size}"

    format={
    "continent": continent,
    "region": region,
    "subRegion": sub_region,
    "recipeTitle": recipie_title,
    "ingredientUsed": ingredient_used,
    "ingredientNotUsed": ingredient_not_used,
    "cookingProcess": cooking_process,
    "utensil": utensil,
    "energyMin": energy_min,
    "energyMax": energy_max,
    "carbohydratesMin": carb_min,
    "carbohydratesMax": carb_max,
    "fatMin": fat_min,
    "fatMax": fat_max,
    "proteinMin": protien_min,
    "proteinMax": protien_max
    }

    resp=request_api(url,post_data=format)

    recipes=[]
    for i in resp["data"]:
        recipes.append(i)

    return recipes


def get_recipie_full_info_from_id(recipie_id):
    url = "https://cosylab.iiitd.edu.in/recipe/"+str(recipie_id)
    resp=request_api(url)

    return resp

def getusefulinfo(recipie):

    #print(recipie)

    #instructions=recipie["instructions"]
    try:
        image=recipie["img_url"] 
        name=recipie["Recipe_title"]
        link=recipie["url"]
        energy=recipie["Calories"]

        finaldict= {"image":image,"name":name,"link":link,"calories":energy}

    except KeyError:

        finaldict= {}
    
    return finaldict

vegnon=["vegan","pescetarian","ovo_vegetarian","lacto_vegetarian","ovo_lacto_vegetarian"]

def sort_for(dataset,attrib):
        finaldat=[]
        for i in dataset:
            if i[attrib]!="0.0":
                print(f"found {attrib}")
                finaldat.append(i)

        return finaldat

def search_nonveg(dataset):
        finaldat=[]
        for i in dataset:
            nonveg=True
            for attrib in vegnon:
                if i[attrib]!="0.0":
                    nonveg=False
            if not nonveg:
                continue
            else:
                print(f"found nonveg")
                finaldat.append(i)

        return finaldat

def get_attributes(data, attributes):
    """
    Extract specified attributes from a dictionary.
    
    Parameters:
        data (dict): The dictionary containing data.
        attributes (list): A list of keys to extract values for.

    Returns:
        dict: A dictionary with the specified attributes and their values.
    """
    extracted_data = {}
    for attr in attributes:
        try:
            extracted_data[attr] = data[attr]
        except KeyError:
            # Skip if the attribute is not found
            continue
    return extracted_data

def get_random_recipe(data):
    num=random.randint(0,99)
    return data[num]



if __name__=="__main__":

    dats=get_recipes(page_size=100,page=1)

    d=sort_for(dats,vegnon[3])

    dn=search_nonveg(dats)


    for i in dn:
        print(getusefulinfo(i))

    print(len(dats))

    print(get_random_recipe(dats)["Recipe_title"])





    