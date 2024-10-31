# GoTech - Tech Word Search Engine


GoTech is a single-page application designed to help users search and learn definitions of technology-related terms. Built using React for the frontend and Django for the backend, GoTech provides a smooth user experience, complete with real-time search suggestions and audio pronunciation of terms.



## Project Overview
GoTech is a tech-focused word search engine designed to be fast, user-friendly, and informative. Users can search for specific tech words, view their definitions, and listen to audio pronunciations, making it ideal for learners and professionals wanting to enhance their tech vocabulary.

## Features

- Real-Time Search: Fast search with suggestions as users type.
- Comprehensive Definitions: Clear definitions of tech words, categorized by field.
- Audio Pronunciation: Listen to the correct pronunciation of tech terms.
- Responsive Design: Optimized for desktop, tablet, and mobile devices.


## Tech Stack

**Frontend**

- React: User interface components and real-time search experience.

- CSS Modules: Scoped styling for component-based design.

**Backend**

- Django: API for managing and serving tech word definitions.

- Django REST Framework: RESTful API endpoints for search functionality.

- PostgreSQL/MySQL: Database to store words, definitions, and audio data.



## Setup & Installation

To run the project locally, follow these steps:

1. **Clone the Repository**

```git clone 
https://github.com/your-username/goTech-search-engine.git
cd goTech-search-engine
```

2. **Backend Setup (Django)**

- Navigate to the backend folder:

```cd backend ```

- Create a virtual environment and install dependencies:

```python -m venv venv
source venv/bin/activate
# On Windows, `use venv\Scripts\activate`
pip install -r requirements.txt
```
c. Configure the database in settings.py and apply migrations:

```python manage.py migrate```

Start the Django server:

```python manage.py runserver```


3. **Frontend Setup (React)**

- Open a new terminal, navigate to the frontend folder:

```cd frontend```

- Initialize react app:

```npm create vite@latest GoTech-search-engine -- --template react```

- Steps After Initialization: 
  Navigate to the Project Directory:

```cd GoTech-search-engine```
- Install Dependencies:

```npm install```

- Run the Development Server:

```npm run dev```

4. Access the Application

- Frontend: 

- Backend API: 






    
## Usage


1. Search for Terms: Enter a tech term in the search bar to get the definition and related information.


2. Listen to Pronunciation: Click the audio icon next to a term to hear its pronunciation.


3. Explore Terms by Category: Discover tech words by categories like software, hardware, etc. (if implemented).



## Contributing

We welcome contributions to improve GoTech! Please follow these steps:

1. Fork the repository.


2. Create a feature branch (git checkout -b feature-name).


3. Commit your changes (git commit -m 'Add feature-name').


4. Push to the branch (git push origin feature-name).


5. Create a Pull Request.



Please ensure your code follows the style guidelines and is thoroughly tested.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Unique-Ade/GoTech-search-engine/blob/main/LICENSE.txt) 


## Demo

A live demo will be available soon


## Authors

- *Adeola Gabriel Olagbenro* - [Unique-Ade](https://github.com/Unique-Ade)
- *Collaborator 1 Name* - [GitHub username](https://github.com/username)
- *Collaborator 2 Name* - [GitHub username](https://github.com/username)



