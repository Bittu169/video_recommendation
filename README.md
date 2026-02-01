
# Movie Recommender System

An **Movie Recommender System** that suggests movies based on user preferences and viewing history. The system combines **content-based filtering and collaborative filtering techniques** to provide personalized recommendations through an **interactive Streamlit web application**.

---

## 🔹 Features

- **Personalized recommendations** based on user-selected movies or preferences
- Combines:
  - **Content-based filtering** (movie genres, keywords, description similarity)
  - **Collaborative filtering** (user ratings and interactions)
- **Interactive Streamlit UI** for easy movie exploration
- Live search and filtering of movies
- Lightweight and fast for small to medium datasets

---

## 🔹 Technology Stack

- **Python** – Core programming language
- **Streamlit** – Interactive web app interface
- **Pandas & NumPy** – Data processing and manipulation
- **Scikit-learn** – Machine learning and similarity computations
- **Surprise / Collaborative Filtering** – User-item recommendation modeling
- **JSON / CSV** – Movie dataset storage

---

## 🔹 How It Works

1. User opens the **Streamlit app** and selects favorite movies or inputs preferences.
2. The system computes **movie similarities** based on content features (genres, keywords) or user ratings.
3. Combines results from content-based and collaborative filtering to create **personalized recommendations**.
4. Displays recommended movies in a **user-friendly web interface**.
5. Users can search for movies and explore recommendations interactively.

---

## 🔹 Demo

Here’s how the Movie Recommender System works:

**1. Movie Selection & Search Interface**  
Select your favorite movies or input preferences to get recommendations.  

![Movie Selection Interface](https://github.com/user-attachments/assets/c7ec6494-5d3a-4067-9b8c-f7d3f0aca3d9)

**2. Recommended Movies Display**  
The system shows personalized movie recommendations based on content-based and collaborative filtering.  

![Recommended Movies Display](https://github.com/user-attachments/assets/1e74c256-6df3-4014-ae71-93a16efc2b67)  

---

## 🔹 Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
