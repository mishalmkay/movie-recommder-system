The recommender_system.ipynb file implements a movie recommender system using the TMDB 5000 dataset. It begins by data cleaning and feature extraction of key columns like genres, cast, crew, keywords, and overview. These features are combined into a "tags" column, preprocessed (e.g., tokenization, stemming, and lowercasing), and converted into numerical vectors using CountVectorizer. The system calculates movie similarities using cosine similarity on these vectors and defines a recommend() function to suggest movies based on a given title. 
After the data cleaning, a Streamlit-based movie recommendation app that integrates with the TMDb API to fetch movie details and posters is built using python. It uses pre-trained recommendation data or models loaded via pickle to suggest movies. Users can select a movie through the Streamlit interface, and the app displays recommended movies along with their posters.





