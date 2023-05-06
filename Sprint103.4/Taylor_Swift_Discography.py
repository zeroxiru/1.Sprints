# initiazing the new string with the raw discography data

raw_data ="""\ ###Taylor Swift (2006)
1. Tim McGraw (03:54)
2. Picture to Burn (2:55)
3. Teardrops on My Guitar (03:33)
4. A Place in This World (03:22)
5. Cold as You (04:02)
6. The Outside (03:28)
7. Tied Together with a Smile (04:11)
8. Stay Beautiful (03:57)
9. Should've Said No (04:05)
10. Mary's Song (Oh My My My) (03:35)
11. Our Song (03:24)
12. I'm Only Me When I'm with You (03:35)
13. Invisible (03:24)
14. A Perfectly Good Heart (03:42)
###Fearless (2008)
1. Fearless (04:01)
2. Fifteen (04:54)
3. Love Story (03:56)
4. Hey Stephen (04:14)
5. White Horse (03:55)
6. You Belong with Me (03:52)
7. Breathe (feat. Colbie Caillat) (04:23)
8. Tell Me Why (03:20)
9. You're Not Sorry (04:22)
10. The Way I Loved You (04:04)
11. Forever & Always (03:45)
12. The Best Day (04:05)
13. Change (04:39)
###Speak Now (2010)
1. Mine (03:51)
2. Sparks Fly (04:20)
3. Back to December (04:53)
4. Speak Now (04:00)
5. Dear John (06:43)
6. Mean (03:58)
7. The Story of Us (04:25)
8. Never Grow Up (04:50)
9. Enchanted (05:52)
10. Better Than Revenge (03:37)
11. Innocent (05:03)
12. Haunted (04:06)
13. Last Kiss (06:08)
14. Long Live (05:18)
###Red (2012)
1. State of Grace (04:55)
2. Red (03:43)
3. Treacherous (04:02)
4. I Knew You Were Trouble (03:39)
5. All Too Well (05:29)
6. 22 (03:52)
7. I Almost Do (04:04)
8. We Are Never Ever Getting Back Together (03:13)
9. Stay Stay Stay (03:25)
10. The Last Time (feat. Gary Lightbody) (04:59)
11. Holy Ground (03:22)
12. Sad Beautiful Tragic (04:44)
13. The Lucky One (04:00)
14. Everything Has Changed (feat. Ed Sheeran) (04:05)
15. Starlight (03:40)
16. Begin Again (03:57)
###1989 (2014)
1. Welcome to New York (03:32)
2. Blank Space (03:51)
3. Style (03:51)
4. Out of the Woods (03:55)
5. All You Had to Do Was Stay (03:13)
6. Shake It Off (03:39)
7. I Wish You Would (03:27)
8. Bad Blood (feat. Kendrick Lamar) (03:31)
9. Wildest Dreams (03:40)
10. How You Get the Girl (04:07)
11. This Love (04:10)
12. I Know Places (03:15)
13. Clean (04:31)
###Reputation (2017)
1. ...Ready for It? (03:28)
2. End Game (feat. Ed Sheeran & Future) (04:04)
3. I Did Something Bad (03:58)
4. Don't Blame Me (03:56)
5. Delicate (03:52)
6. Look What You Made Me Do (03:31)
7. So It Goes... (03:47)
8. Gorgeous (03:29)
9. Getaway Car (03:53)
10. King of My Heart (03:34)
11. Dancing with Our Hands Tied (03:31)
12. Dress (03:50)
13. This Is Why We Can't Have Nice Things (03:27)
14. Call It What You Want (03:23)
15. New Year's Day (03:55)
###Lover (2019)
1. I Forgot That You Existed (2:50)
2. Cruel Summer (2:58)
3. Lover (03:41)
4. The Man (03:10)
5. The Archer (03:31)
6. I Think He Knows (2:53)
7. Miss Americana & The Heartbreak Prince (03:54)
8. Paper Rings (03:42)
9. Cornelia Street (04:47)
10. Death by a Thousand Cuts (03:18)
11. London Boy (03:10)
12. Soon You'll Get Better (feat. Dixie Chicks) (03:21)
13. False God (03:20)
14. You Need to Calm Down (2:51)
15. Afterglow (03:43)
16. ME! (feat. Brendon Urie) (03:13)
17. It's Nice to Have a Friend (2:30)
18. Daylight (04:53)
###Folklore (2020)
1. the 1 (03:30)
2. cardigan (04:00)
3. the last great american dynasty (03:51)
4. exile (feat. Bon Iver) (04:45)
5. my tears ricochet (04:16)
6. mirrorball (03:29)
7. seven (03:29)
8. august (04:21)
9. this is me trying (03:15)
10. illicit affairs (03:10)
11. invisible string (04:13)
12. mad woman (03:57)
13. epiphany (05:01)
14. betty (04:54)
15. peace (03:54)
16. hoax (03:40)
###Evermore (2020)
1. willow (03:34)
2. champagne problems (04:03)
3. gold rush (03:05)
4. 'tis the damn season (03:49)
5. tolerate it (04:05)
6. no body, no crime (feat. HAIM) (03:35)
7. happiness (05:15)
8. dorothea (03:28)
9. coney island (feat. The National) (04:35)
10. ivy (04:20)
11. cowboy like me (04:35)
12. long story short (03:35)
13. marjorie (04:17)
14. closure (03:01)
15. evermore (feat. Bon Iver) (05:05)"""

# Initialize the empty dictionary to store the discography data
discography = {}

# split the raw data string by newline characters to create a list of strings
lines = raw_data.split("\n")

# Initialize the empty variables to store the current album and song info
current_album = None
Current_song = None
for line in lines:
 # check if the line starts with "###", indicating a new album
if line.startswith("###"):
    #Extract the album name and year from the line and store them in variables
    album_info = line.strip('#').split(" (")
    album_name = album_info[0]
    album_year = album_info[1].strip(")")

    #Create a new dictionary to store the album information and add it to the discography dictionary
    album = {"year": album_year, "songs": {}}
    discography[album_name] = album

    #update the current album variable to the new album
    current_album = album_name

    # reset the current song variable None, for starting a new album
    current_song = None

    # the line starts with a number, indicating a new song
elif line[0].isdigit():
    # Extract the song number, name and duration from the each line and storing it in variables
    song_info = line.split(". ")[1].strip("(")
    song_number = int(line.split(". ")[0])
    song_name =  song_info[0]
    song_duration = song_info[1].strip(")")

    #create a new dictionary to store the song information and add it to the current album dictionary
    song = {"number":song_number, "duration":song_duration }
    discography[current_album]["songs"][song_name] = song

    #update the current song variable to the new song
    current_song =  song_name



