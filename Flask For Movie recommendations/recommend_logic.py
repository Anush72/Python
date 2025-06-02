def recommend_movies(watched_movie, rules_df, top_n=5):
    print(f"Searching recommendations for: {watched_movie}")

    matching_rules = rules_df[rules_df['antecedents'].apply(lambda x: watched_movie.strip().lower() in[i.lower() for i in x])]
    print(f"Found {len(matching_rules)} matching rules")

    if matching_rules.empty:
        return ["No recommendation found for this movie."]

    sorted_rules = matching_rules.sort_values(by='confidence', ascending=False)
    recommend_movies = []

    for _, row in sorted_rules.iterrows():
        recommend_movies.extend(list(row['consequents']))

    recommend_movies = list(dict.fromkeys(recommend_movies))[:top_n]

    print(f"Recommendations: {recommend_movies}")
    return recommend_movies
