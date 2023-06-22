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

---

Feel free to customize and expand on this document according to your specific requirements and add any additional information or explanations as needed.

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
