import requests, pymysql

MOVIE = input("Enter the name of the film: ")

API_KEY = "5d9df2b8"

url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={MOVIE}"



get = requests.get(url)
data = get.json()
# print(data)
dict = {}




connection = pymysql.connect(   
    host = '127.0.0.1',
    user = 'root',
    password= '12345',
    db='Movies',
    port = 3306,
    charset = 'utf8mb4', 
    cursorclass= pymysql.cursors.DictCursor
)
            

if data["Response"] == 'True':
    Title = get.json()["Title"]
    Released = get.json()["Released"]
    Genre = get.json()["Genre"]
    Director = get.json()["Director"]

  
    dict["Title"] = Title
    dict["Released"] = Released
    dict["Genre"] = Genre
    dict["Director"] = Director


    def Add(Title,Released,Genre,Director):
        with connection:
            with connection.cursor() as cursor:
                sql_command = """Insert into Movie_info(title,released,director,Genre)
                                Values
                                (%s,%s,%s,%s);"""
                cursor.execute(sql_command,(Title,Released,Genre,Director))
            connection.commit()


    Add(dict["Title"],dict["Released"],dict["Genre"],dict["Director"])

    
else:
    print("Movie not found")


