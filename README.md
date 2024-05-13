# Cafee83 - Cyber Cafe Management System

Cafee83 is a comprehensive Cyber Cafe Management System developed using Django, a high-level Python web framework. The system aims to provide efficient management of cyber cafes, including user authentication, profile management, computer management, and more.

## Checkout the Project on Deployement - [Deployment Project](https://cafee83.pythonanywhere.com/home/)


## Project Features:
| # | Feature                  | Description                                    |
|---|--------------------------|------------------------------------------------|
| 1 | User Authentication      | Secure login and registration for users        |
| 2 | Profile Management       | Allow users to update their profiles           |
| 3 | Computer Management      | Manage computers in the cyber cafe             |
| 4 | Celery Based Model Update | Asynchronous updates using Celery            |
| 5 | Custom User Permissions | Assign specific permissions to users            |

## Custom User-Based Permissions:
| # | Permission Type   | Description                               |
|---|-------------------|-------------------------------------------|
| 1 | Computer Editor   | Can create, delete, and update computers |
| 2 | Admin Access      | Limited access reserved for administrators|

## Profile Address:
The system utilizes an API-based location feature to fetch the user's address based on their browser's geolocation.

## Connect with Us:
- **Instagram:** [Instagram](https://www.instagram.com/itsmohit.codes/)
- **YouTube:** [YouTube Channel](https://www.youtube.com/@itsmohitcodes)
- **GitHub:** [GitHub Repository](https://github.com/mohitprajapat2001)

## Technologies Used:
- Django Framework
- Bootstrap CSS Framework
- Celery for asynchronous task execution
- PostgreSQL Database
- HTML, CSS, JavaScript

## Installation:
To install Cafee83 and set up Celery with Redis, follow these steps:

1. **Clone the repository**:
```
git clone https://github.com/mohitprajapat2001/Cafee83.git
```

2. **Navigate to the project directory**:
```
cd Cafee83
```

3. **Create and activate a virtual environment** (if not already activated):
```
python -m venv venv
source venv/bin/activate # For Linux/macOS
venv\Scripts\activate # For Windows
```

4. **Install dependencies**:
```
pip install -r requirements.txt
```

5. **Install Redis**:
- On Linux:
  ```
  sudo apt update
  sudo apt install redis-server
  ```
- On macOS using Homebrew:
  ```
  brew install redis
  ```
- On Windows:
  Download and install Redis from the [official website](https://redis.io/download).

6. **Run Redis Server**:
- On Linux or macOS:
  ```
  redis-server
  ```
- On Windows:
  Start the Redis Server application.

7. **Start Celery**:
In a new terminal or console, ensure that you are in the same virtual environment and project directory. Then run:
```
celery -A Cafee83 worker -l info --pool=solo
```

8. **Run Django Development Server**:
In the original terminal or console (where your virtual environment is activated), navigate to the project directory and run:

Now, your Cafee83 project should be up and running with Celery using Redis as the message broker.


## Conclusion:
Cafee83 is an open-source project aimed at providing a comprehensive solution for managing cyber cafes efficiently. It incorporates modern technologies and follows best practices in software development.
