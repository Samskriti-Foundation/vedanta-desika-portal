# Vedanta Desika Portal

## Overview

**Vedanta Desika Portal** is a web app built by **Samskriti Foundation, Mysore.**
<br>
<br>
**Vedanta Desika** was an Indian polymath who wrote philosophical, religious, and poetical works in several languages, including Sanskrit, Manipravaḷam (a Sanskritised form of literary Tamil), Tamil, and Prakrit.
<br>
<br>
This app utilizes **D3.js, HTMX, Tailwind CSS,** and **Flask**.
<br>
- **D3.js:** Used for creating interactive and dynamic tree visualizations.
- **HTMX:** Enhances HTML with AJAX to enable seamless server-side interactions without the need for JavaScript.
- **Tailwind CSS:** Provides utility-first CSS classes for rapid and responsive styling.
- **Flask:** Serves as the backend framework, handling server-side logic, APIs, and routing.

## Installation

To get started with the Vedanta Desika Portal, follow these steps:

### Prerequisites

- Python 3.10 or higher
- Node.js and yarn
- Git

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Samskriti-Foundation/vedanta-desika-portal.git
   ```

2. **Navigate to the project directory:**
  
    ```bash
    cd vedanta-desika-portal
    ```

3. **Install Python and its dependencies using a virtual environment:**

   a. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

   b. Activate the virtual environment:

   - **Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```
   - **Windows:**
     ```bash
      venv\Scripts\activate
     ```
     
   c. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
   
4.  **Install frontend dependencies:**

    a. Install yarn if not already installed

    ```bash
    npm i -g yarn
    ```
    
    b. Install dependencies through yarn

      ```bash
      yarn install
      ```

## Run the server

1. Navigate to app directory

   ```bash
   cd app
   ```

3. Run the Flask development server:

   ```bash
   flask run
   ```
