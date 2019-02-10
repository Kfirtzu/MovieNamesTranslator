Movie file names translator

1. Find movies in your disk - filenames in English
2. Check if it's only English (i.e. non-Hebrew letters) or mixed
3. for every movie name -
    a. Check if it's a movie (e.g. IMDB)
    b. Find this movie name in a site with Hebrew and English names
    c. Extract the movie name in Hebrew




Additional features:
1. scan the dir first
2. propose translations
3. mark match score (Perfect match/Multiple matches/Suspected match/No match)
4. allow manual translation/correction
5. build local db with ability to search for a movie. by genre/score/length...
6. ability to see description
7. find duplicates


Steps:
1. do the process manually
2. define what to automate first
    a. Movie verification
3. start with small building blocks
4. integrate building blocks

Building blocks:
1. Get directory with movies (include configuration options)
2. scan dir to extract names
2.1 get movie name(s) (see below)
3. Movie verification (see movie_verification.txt)
[4. Optional: Movie correction - for mistaken names]
5. find Hebrew name
6. rename source file name (keep original name / be able to revert)

Notes:



get_movie_name
--------------
1. supported movie file types (mp4, mkv, avi...)
[2. be assisted by subtitle file?]
3. use directory name
4. use year
5. remove codec words (



Sample movie names:
===================
dots.structure:
---------------
Tinker.Bell.And.The.Lost.Treasure.DVDRip.HebDub.iDown.me.avi
Tinkerbell.and.the.Pirate.Fairy.2014.HDTV.HebDub.XviD-Sweet-Star.mp4
שרק 4Shrek.Forever.After.2010.DVDRip.HebDub.XviD_Anthem_wWw.HoradoT.NeT.mp4
Robin.Hood.2018.720p.WEB.DL.mkv

Kodi download structure:
--------------------------
A Star Is Born (2018) - dir and inside: A Star Is Born (2018).mp4
The Lord of the Rings The Two Towers (2002) - dir and inside: The Lord of the Rings The Two Towers (2002).mp4

Others:
--------
Hayafeyfia_Hanirdemet.avi
SLEEPING_BEAUTY.avi
sinbad HEB.avi
