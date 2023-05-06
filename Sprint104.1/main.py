movies = [
    {'title': 'The Shawshank Redemption', 'rank': 1},
    {'title': 'The Godfather', 'rank': 2},
    {'title': 'The Dark Knight', 'rank': 3},
    {'title': 'Schindler\'s List', 'rank': 4},
    {'title': 'The Lord of the Rings: The Return of the King', 'rank': 5}
]

def get_title_by_rank(rank):
    for movie in movies:
        if movie['rank'] == rank:
            return movie['title']
    return None

def get_rank_by_title(title):
    for movie in movies:
        if movie['title'] == title:
            return movie['rank']
    return None