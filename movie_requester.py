

def get_tmdb_img(movie,year):
    import requests
    API_key = open('api_key', 'r').read()
    response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={API_key}&language=en-US&query={movie}&page=1&include_adult=false&year={year}")
    print(response)
    if response.status_code == 200:
        backdrop_path = response.json()
        if len(backdrop_path['results'])>0:
            backdrop_path = backdrop_path['results'][0]['backdrop_path']
            if backdrop_path is not None:
                img_path = "https://image.tmdb.org/t/p/w500/"+backdrop_path
                print(img_path)
                return img_path
    return ""

#