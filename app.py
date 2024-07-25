def main():
    st.title("Movie Recommendation System")
    ratings,movies=load_data()
    user_movie_matrix,data = prepare_data(ratings,movies)

    selected_movie=st.selectbox('Select a Movie:,movies['title'].unique()')

    if st.button('Get Recommendation'):
        recommendations=get_similar_movies(selected_movie,movies)
        if recommendations:
            st.write('Recommended Movies:')
            for movie in recommendations:
                st.write(movie)
        else:
            st.write('No recommendation available for the selected movie.')

if __name__ == "__main__":
    main()
