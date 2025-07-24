# 🎬 Movie Recommender System

This is a simple web application built with **Streamlit** that recommends movies similar to the one you select from the dropdown. It uses a **content-based filtering** approach by analyzing movie features and computing similarities between them.

---

## 📌 Features

- Select a movie from a list
- Get the top 5 similar movie recommendations
- Built using Python and Streamlit
- Lightweight and runs locally without external APIs

---

## ⚙️ Project Mechanism

This recommender system uses **content-based filtering** with **cosine similarity**. Here's how it works internally:

1. **Preprocessing in Colab:**
   - Movie data is processed and converted into feature vectors.
   - Cosine similarity is calculated between each pair of movies.
   - A dictionary of movie titles (`movies_dic.pkl`) and a similarity matrix (`similarity_1.pkl`) are saved using `pickle`.

2. **Main Logic in `app.py`:**
   - The user selects a movie from a dropdown.
   - The app retrieves the index of the selected movie.
   - Using the similarity matrix, it finds the most similar movies (highest cosine similarity scores).
   - The top 5 most similar movies (excluding the selected one) are displayed as recommendations.

3. **Web Interface:**
   - Streamlit is used to build a simple UI with dropdowns and buttons.
   - Results are displayed instantly in the browser.
  
   - <img width="1099" height="671" alt="image" src="https://github.com/user-attachments/assets/37205f4a-695e-4585-b98e-3aa38223ba09" />


---

## 📂 Project Structure

```
movie_recommender_system/
├── app.py                 # Streamlit web app code
├── movies_dic.pkl         # Movie title dictionary
├── similarity_1.pkl       # Cosine similarity matrix (excluded from GitHub due to size)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```



---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.7 or later installed

### 🔧 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/movie-recommender.git
cd movie-recommender

# Create and activate virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py


### 🔗 Download Required File

Please manually download the file below and place it in the project root directory:

🔸 [Download similarity_1.pkl from Google Drive](https://https://drive.google.com/drive/folders/1u5496NoOirvcWjehaddIp--Wzjq_-cpk)

