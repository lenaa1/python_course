import sqlite3

with sqlite3.connect("netflix_3.sqlite") as db:
    def normalize():
        cursor = db.cursor()
        cursor.execute("alter table netflix_titles drop column show_id")
        cursor.execute("alter table netflix_titles drop column director")
        cursor.execute("alter table netflix_titles drop column country")
        cursor.execute("alter table netflix_titles drop column date_added")
        cursor.execute("alter table netflix_titles drop column release_year")
        cursor.execute("alter table netflix_titles drop column rating")
        cursor.execute("alter table netflix_titles drop column listed_in")
        cursor.execute("alter table netflix_titles drop column description")
        cursor.close()

    def get_most_popular_actor():
        cursor = db.cursor()
        cursor.execute("""SELECT `cast` AS cast1 FROM netflix_titles""")
        casts = cursor.fetchall()

        times_actor_played: dict[str, int] = {}
        for cast in casts:
            for actor in cast[0].split(", "):
                if actor == "":
                    continue
                if actor in times_actor_played:
                    times_actor_played[actor] = times_actor_played[actor] + 1
                else:
                    times_actor_played[actor] = 1

        max_key = max(times_actor_played, key=times_actor_played.get)
        print("самый популярный актер:", max_key)


    def get_longest_movie():
        cursor = db.cursor()
        cursor.execute("""select * from netflix_titles where type='Movie' and duration!='' order by duration DESC""")
        res = cursor.fetchall()
        print(f"самый длинный фильм:", res[0][1])


    def get_longest_tv_show():
        cursor = db.cursor()
        cursor.execute("""select * from netflix_titles where type='TV Show' and duration!='' order by duration DESC""")
        res = cursor.fetchall()
        print(f"самый длинный сериал:", res[0][1])

    def get_actor_pairs():
        cursor = db.cursor()
        cursor.execute("""SELECT `cast` AS cast1 FROM netflix_titles""")
        casts = cursor.fetchall()

        pairs: dict[str, int] = {}

        for cast in casts:
            cast_array = cast[0].split(", ")
            for actor_one in cast_array:
                other_actors = filter(lambda x: x != actor_one, cast_array)
                for actor_two in other_actors:
                    key = actor_one + " and " + actor_two
                    if key in pairs:
                        pairs[key] = pairs[key] + 1
                    else:
                        pairs[key] = 1
        max_key: str = max(pairs, key=pairs.get)
        print("самая частовстречающаяся пара:", max_key)


    # normalize()
    get_most_popular_actor()
    get_longest_movie()
    get_longest_tv_show()
    get_actor_pairs()




