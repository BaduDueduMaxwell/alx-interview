# 0x06. Star Wars API

## Project Overview
The "0. Star Wars Characters" project requires interacting with the Star Wars API to fetch and display information about characters from a specific movie, based on the provided movie ID. This project demonstrates how to work with external APIs, handle asynchronous operations in JavaScript, and retrieve and display JSON data effectively.

### Key Concepts
1. **HTTP Requests in JavaScript**:
   - Learn to make HTTP requests to external services using the `request` module or alternatives like `fetch` in Node.js.
   - [Guide to Making HTTP Requests in Node.js](https://www.example.com)

2. **Working with APIs**:
   - Understand RESTful APIs, JSON parsing, and how to handle API responses.
   - [Working with APIs in JavaScript](https://www.example.com)

3. **Asynchronous Programming**:
   - Manage asynchronous operations with callbacks, promises, and async/await.
   - [Asynchronous Programming in JavaScript](https://www.example.com)

4. **Command Line Arguments in Node.js**:
   - Access command-line arguments in a Node.js script using `process.argv`.
   - [Parsing Command Line Arguments in Node.js](https://www.example.com)

5. **Array Manipulation and Iteration**:
   - Iterate over arrays and manipulate data to format and display character names.
   - [JavaScript Array Methods](https://www.example.com)

### Requirements
- **Editors**: `vi`, `vim`, `emacs`
- **Execution Environment**: Files are interpreted on Ubuntu 20.04 LTS using Node.js (version 10.14.x).
- **File Standards**:
  - Files must end with a new line.
  - First line must be `#!/usr/bin/node`.
  - Code must follow the `semistandard` style (Standard + semicolons).
  - Files must be executable.
  - Avoid using `var`.
- **Installations**:
  - **Node.js 10**:
    ```bash
    $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    $ sudo apt-get install -y nodejs
    ```
  - **Semi-Standard**:
    ```bash
    $ sudo npm install semistandard --global
    ```
  - **Request Module**:
    ```bash
    $ sudo npm install request --global
    $ export NODE_PATH=/usr/lib/node_modules
    ```

## Task: Star Wars Characters

Write a script to print all characters from a Star Wars movie:
- **Arguments**: The first positional argument is the movie ID (e.g., `3` for “Return of the Jedi”).
- **Output**: Display one character name per line in the order specified in the `/films/` endpoint.
- **Requirements**:
  - Use the Star Wars API.
  - Use the `request` module for API calls.

### Example Usage
```bash
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

### Repository Structure
- **GitHub Repository**: `alx-interview`
- **Directory**: `0x06-starwars_api`
- **File**: `0-starwars_characters.js`
