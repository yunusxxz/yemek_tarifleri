import requests as req

url = 'https://dummyjson.com/recipes?limit=0'

response = req.get(url)

match response.status_code:
    case 200: # Ok
        data = response.json() # JavaScript Object Notation
        print(data.keys())
        recipes = data['recipes']
        #print(recipes)
        cuisines = {r['cuisine'] for r in recipes}
        print(cuisines)
    case 404: # Not Found
        print("page not found")



    case 500:
        pass



