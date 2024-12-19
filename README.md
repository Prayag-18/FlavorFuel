# **FlavorFuel: Recipe Exploration Platform**  

## **Overview**  
FlavorFuel is an engaging recipe exploration platform that helps users discover and curate recipes tailored to their needs. By integrating powerful APIs and adding interactive features, it provides recipes across diverse categories such as health-conscious diets, culinary exploration, and fitness-focused meals. Additionally, it features mini-games for an engaging and educational experience.

---

## **Features**  

1. **Recipe Discovery**  
   - Fetch recipes based on user preferences such as **ingredients**, **categories**, and **regions**.  
   - Integrated with external APIs([FlavourDB](https://documenter.getpostman.com/view/13496956/TVev55ME) and [RecipeDB](https://documenter.getpostman.com/view/16532608/2sAY4uD4Gb)) for dynamic recipe recommendations.  

2. **User Categories**  
   - Tailored recipes for:  
     - **Culinary Explorers**  
     - **Health-Conscious Individuals**  
     - **Fitness Enthusiasts**  
     - **Dietitians and Nutritionists**  

3. **Interactive Games**  
   - **Higher or Lower:** Guess the recipe with higher or lower calories.  
   - **Guess the Continent:** Identify the continent or region of a random recipe based on its attributes.  

4. **User Authentication**  
   - Basic login functionality with a sample admin account:  
     - **Username:** `admin`  
     - **Password:** `pass123`  

---

## **Technologies Used**  
- **Python** (Flask Backend, APIs, and Logic)  
- **Flask** (Web Framework)  
- **HTML/CSS** (Frontend Templates)  
- **APIs:**  
  - **RecipeDB API**  
  - **FlavorDB API**  
- **Libraries:**  
  - `requests` for API calls  
  - `random` for game logic  

---

## **Setup and Installation**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/Prayag-18/flavorfuel.git
cd flavorfuel
```

### **2. Install Dependencies**  
Ensure Python 3.x is installed. Then, install the required libraries:  
```bash
pip install flask requests
```

### **3. Run the Application**  
Start the Flask server:  
```bash
python app.py
```
The app will run on `http://127.0.0.1:5000/`.

---

## **Usage**  

1. **Login Page**  
   - Access the login page at `/` or `/login`.  
   - Use the admin credentials for testing:  
     - Username: `admin`  
     - Password: `pass123`  

2. **Explore Recipes**  
   - Select categories like **Culinary Explorers**, **Health-Conscious Individuals**, etc., to view curated recipes.  

3. **Play Mini-Games**  
   - Visit `/test` to play interactive games:  
     - Guess calorie values with **Higher or Lower**.  
     - Identify continents or regions with **Guess the Continent**.  

---

## **Project Structure**  
```plaintext
FlavorFuel/
│
├── app.py              # Main Flask application
├── flavorfuel.py       # Recipe fetching and processing functions
├── flavorgames.py      # Mini-games logic
├── templates/          # HTML templates for pages
├── static/             # Static files (CSS, images, etc.)
└── README.md           # Project documentation
```

---

## **Example API Response**  
### **Recipe Fetch Example:**  
```json
{
  "Recipe_title": "Pasta Primavera",
  "Calories": "350",
  "img_url": "https://example.com/pasta.jpg",
  "url": "https://example.com/full-recipe"
}
```

---

## **Future Enhancements**  
- **User Authentication:** Add user registration and personalized dashboards.  
- **Advanced Filtering:** Allow filtering based on nutrition, region, or cooking time.  
- **Interactive Features:** Include more games and personalized recipe suggestions.  

---

## **Contributors**  
- **Prayag Parashar**  
- **Tarandeep Singh**
- **Pradumme Attri**
- **Aayu Singh**  

---

## **License**  
This project is licensed under the MIT License.  
