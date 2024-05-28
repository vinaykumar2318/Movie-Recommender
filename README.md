# Movie Recommendation System

This project implements a movie recommendation system using Flask for the backend and JavaScript for the frontend. It recommends similar movies based on user input.

## Features

- **Search**: Users can input a movie name to get recommendations.
- **Dynamic UI**: The recommendations are displayed dynamically without page refresh.
- **Movie Posters**: Along with movie titles, posters are also displayed.
- **Error Handling**: Errors are gracefully handled and displayed to the user.

## Technologies Used

- **Flask**: Used for the backend server to handle requests.
- **Pandas**: Used for data manipulation and loading movie data.
- **Scikit-learn**: Used for computing similarity scores between movies.
- **JavaScript**: Used for the frontend to dynamically update UI.
- **HTML/CSS**: Used for structuring and styling the frontend.
- **The Movie Database (TMDb) API**: Used for fetching movie posters.

## Installation

1. Clone the repository:
  git clone https://github.com/your-username/movie-recommendation-system.git

2. Run the python notebok and generate movie.pkl ans similarity.pkl files and then save them in the same directory.

3. Install dependencies:
  pip install -r requirements.txt

4. Run the Flask server:
  python app.py

5. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Enter the name of a movie in the input field.
2. Click on the "Get Recommendations" button.
3. The system will display recommendations along with movie posters.
