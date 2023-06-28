# BACKEND-CODING-TEST



Here's a document describing the API:

---

## Word Count API

This API allows you to count the number of occurrences of a word in a webpage.

### Endpoint

```
POST /wordcount
```

### Request Body

The API expects a JSON request body with the following fields:

- `word` (string): The word to be counted.
- `url` (string): The URL of the webpage where the word count should be performed.

Example Request Body:

```json
{
  "word": "fit",
  "url": "https://www.example.com"
}
```

### Response

The API returns a JSON response with the following fields:

- `count` (integer): The number of occurrences of the word in the webpage.

Example Response:

```json
{
  "count": 3
}
```

### Notes

- The API performs a case-insensitive search for the word in the webpage content.
- Words surrounded by dashes, such as `-fit-`, are not counted.
- The API retrieves the webpage source by sending a GET request to the specified URL.
- The word count is calculated by searching for the exact word boundaries in the webpage content.
- Optionally, the API can save the word count result to a database.

Certainly! Here's an example README file content that explains how to use Alembic for managing database migrations in your project:

---

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/project-name.git
   ```

2. Navigate to the project directory:

   ```
   cd project-name
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Database Migrations

1. Initialize Alembic: Run the following command to initialize Alembic in your project:

   ```
   alembic init alembic
   ```

   This command creates an `alembic` directory in your project, containing configuration files and a folder for storing migration scripts.

2. Configure the Database URL: Open the `alembic.ini` file and locate the `[alembic]` section. Set the `sqlalchemy.url` option to the database URL for your development environment.

3. Generate Initial Migration: To generate an initial migration script, run the following command:

   ```
   alembic revision --autogenerate -m "Initial migration"
   ```

   This command compares the current state of the database with the SQLAlchemy models defined in your project and generates a migration script in the `alembic/versions` directory.

4. Customize the Migration: Open the generated migration script in the `alembic/versions` directory and review its contents. Modify the script, if needed, to include additional database operations or changes specific to your project requirements.

5. Apply Migrations: To apply the migrations and update your database schema, run the following command:

   ```
   alembic upgrade head
   ```

   This command executes all pending migrations and brings your database up to the latest version.

6. Repeat Steps 3-5 for Test Database: Follow steps 3-5 again, but this time set the `sqlalchemy.url` option in the `alembic.ini` file to the database URL for your testing environment. This ensures that migrations are also applied to the test database.

## Additional Information

- The `alembic.ini` file contains configuration options for Alembic. Customize these options according to your project's requirements.

- The `alembic/env.py` file contains the Alembic environment setup. You can modify this file to include additional configuration or customization.

- Refer to the official Alembic documentation for more information on advanced features and commands: https://alembic.sqlalchemy.org/en/latest/

---

Feel free to modify and expand upon this template based on your specific project needs.

***

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
