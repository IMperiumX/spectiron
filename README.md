<a name="readme-top"></a>

<div align="center">

<img src="./assets/logo.png" alt="logo" alt="logo" width="200" height="auto" />

<details closes>
  <summary><h1>specitron</h1></summary>
  It blends "spec" (short for specification) with "tron" (a reference to electronic and futuristic concepts), giving a tech-forward and modern impression.
</details>

<p>
    seamlessly generate comprehensive and dynamically updated API documentation.
  </p>

<!-- Badges -->

<p>
  <a href="https://github.com/imperiumx/specitron/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/imperiumx/specitron" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/imperiumx/specitron" alt="last update" />
  </a>
  <a href="https://github.com/imperiumx/specitron/network/members">
    <img src="https://img.shields.io/github/forks/imperiumx/specitron" alt="forks" />
  </a>
  <a href="https://github.com/imperiumx/specitron/stargazers">
    <img src="https://img.shields.io/github/stars/imperiumx/specitron" alt="stars" />
  </a>
  <a href="https://github.com/imperiumx/specitron/issues/">
    <img src="https://img.shields.io/github/issues/imperiumx/specitron" alt="open issues" />
  </a>
  <a href="https://github.com/imperiumx/specitron/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/imperiumx/specitron.svg" alt="license" />
  </a>
</p>

<h4>
    <a href="https://github.com/imperiumx/specitron/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/imperiumx/specitron">Documentation</a>
  <span> · </span>
    <a href="https://github.com/imperiumx/specitron/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/imperiumx/specitron/issues/">Request Feature</a>
  </h4>

</div>

<br/>

<!-- Table of Contents -->

# :notebook_with_decorative_cover: Table of Contents

- [:notebook\_with\_decorative\_cover: Table of Contents](#notebook_with_decorative_cover-table-of-contents)
  - [:star2: About specitron](#star2-about-specitron)
    - [:camera: Screenshots](#camera-screenshots)
    - [:space\_invader: Tech Stack](#space_invader-tech-stack)
  - [:toolbox: Getting Started](#toolbox-getting-started)
    - [:bangbang: Prerequisites](#bangbang-prerequisites)
    - [:gear: Installation](#gear-installation)
    - [Type checks](#type-checks)
    - [:test\_tube: Running Tests](#test_tube-running-tests)
    - [Test coverage](#test-coverage)
      - [Running tests with pytest](#running-tests-with-pytest)
    - [:running: Run Locally](#running-run-locally)
  - [:eyes: Usage](#eyes-usage)
  - [:compass: Roadmap](#compass-roadmap)
  - [:wave: Contributing](#wave-contributing)
  - [Commiting your code](#commiting-your-code)
    - [:scroll: Code of Conduct](#scroll-code-of-conduct)
  - [:grey\_question: FAQ](#grey_question-faq)
  - [:warning: License](#warning-license)
  - [:handshake: Contact](#handshake-contact)
  - [:gem: Acknowledgements](#gem-acknowledgements)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- About the Project -->

## :star2: About specitron

Automate API documentation generation through advanced code analysis, ensuring accurate and up-to-date documentation. Utilize intelligent source code examination to produce precise and synchronized API documentation, saving time and guaranteeing accuracy. Enable developers to focus on core tasks while maintaining a well-documented API ecosystem.

Note: This project is still in development and is not ready for production use.

<!-- Screenshots -->

### :camera: Screenshots

<div align="center">
  <img src="./assets/logo-plus.png" alt="screenshot" />
</div>

<!-- TechStack -->

### :space_invader: Tech Stack

<details closes>
  <summary>Client</summary>
  <ul>
    <li><a href="https://www.typescriptlang.org/">Typescript</a></li>
    <li><a href="https://nextjs.org/">Next.js</a></li>
    <li><a href="https://reactjs.org/">React.js</a></li>
    <li><a href="https://tailwindcss.com/">TailwindCSS</a></li>
  </ul>
</details>

<details closes>
  <summary>Server</summary>
  <ul>
    <li><a href="https://www.djangoproject.com/">Django</a></li>
    <li><a href="https://www.django-rest-framework.org/">Django REST Framework</a></li>
    <li><a href="https://channels.readthedocs.io/en/stable/">Django Channels</a></li>
    <li><a href="https://www.graphene-python.org/">Graphene</a></li>
  </ul>
</details>

<details closes>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.mysql.com/">MySQL</a></li>
    <li><a href="https://www.postgresql.org/">PostgreSQL</a></li>
    <li><a href="https://redis.io/">Redis</a></li>
    <li><a href="https://neo4j.com/">Neo4j</a></li>
    <li><a href="https://www.mongodb.com/">MongoDB</a></li>
  </ul>
</details>

<details closes>
<summary>DevOps</summary>
  <ul>
    <li><a href="https://www.docker.com/">Docker</a></li>
    <li><a href="https://www.jenkins.io/">Jenkins</a></li>
    <li><a href="https://circleci.com/">CircleCLI</a></li>
  </ul>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Getting Started -->

## :toolbox: Getting Started

<!-- Prerequisites -->

### :bangbang: Prerequisites

activate virtualenv and install requirements

```sh
  pip install -r requirements/local.txt
```

### :gear: Installation

Via pip into a `virtualenv`:

```sh
  pip install specitron
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Running Tests -->

### Type checks

Running type checks with mypy:

```bash
  mypy specitron
```

### :test_tube: Running Tests

To run tests, run the following command

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

```bash
  coverage run -m pytest\
  coverage html\
  open htmlcov/index.html\
```

#### Running tests with pytest

```basg
  pytest
```

<!-- Run Locally -->

### :running: Run Locally

Clone the project

```bash
  git clone https://github.com/imperiumx/specitron.git
```

Go to the project directory

```bash
  cd specitron
```

Install dependencies

```bash
  pip install -r requirements/local.txt
```

Start the server

```bash
  python mananage.py migrate\
  python manage.py runserver
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Usage -->

## :eyes: Usage

```python
from openapi_spec_generator import OpenAPISpecGenerator

# Create an instance of the OpenAPI specification generator
generator = OpenAPISpecGenerator()

# Define your API endpoints and their corresponding methods
generator.add_path('/users', 'GET', 'Get a list of users')
generator.add_path('/users/{id}', 'GET', 'Get a user by ID')
generator.add_path('/users', 'POST', 'Create a new user')
generator.add_path('/users/{id}', 'PUT', 'Update a user by ID')
generator.add_path('/users/{id}', 'DELETE', 'Delete a user by ID')

# Generate the OpenAPI specification in JSON format
specification = generator.generate_spec()

# Save the specification to a file
with open('openapi.json', 'w') as f:
    f.write(specification)

# Alternatively, you can also print the specification
print(specification)
```

<!-- Roadmap -->

## :compass: Roadmap

- ### Phase 1: Basic Functionality
  
  - [ ] Parsing Source Code: Implement the ability to parse the source code of API projects written in one or more programming languages.
  - [ ] Endpoint Extraction: Extract API endpoints, HTTP methods, URL paths, query parameters, and request/response headers from the parsed source code.
  - [ ] Data Model Extraction: Identify data structures, request/response bodies, data types, required fields, and basic validation rules from the source code.
  - [ ] Documentation Generation: Generate an initial OpenAPI specification document based on the extracted information and provide options for customization.

- ### Phase 2: Enhanced Extraction and Documentation
  
  - [ ] Advanced Endpoint Analysis: Improve endpoint extraction by handling more complex scenarios like route parameters, nested routes, and route patterns.
  - [ ] Request/Response Body Analysis: Enhance data model extraction to support nested objects, arrays, and more advanced validation rules.
  - [ ] Code Annotation Support: Introduce support for code annotations or comments that allow developers to provide additional information for the generator to use in the documentation.
  - [ ] Customization Options: Expand customization options to allow developers to specify details like response examples, API descriptions, and error handling.

- ### Phase 3: Language and Framework Support
  
  - [ ] Support for Multiple Programming Languages: Add support for additional programming languages commonly used for API development.
  - [ ] Framework Integration: Integrate with popular web frameworks (e.g., Express.js, Django, Ruby on Rails) to enhance extraction capabilities specific to those frameworks.

- ### Phase 4: Developer Experience and Tooling
  
  - [ ] Command-Line Interface (CLI): Develop a CLI tool for easy configuration and execution of the OpenAPI generator.
  - [ ] Graphical User Interface (GUI): Create a user-friendly GUI for configuring and running the generator.
  - [ ] Build Process Integration: Provide seamless integration with common build tools and CI/CD pipelines for automatic generation of documentation during the development lifecycle.

- ### Phase 5: Advanced Features
  
  - [ ] Authentication and Authorization Support: Extend the generator to extract and document authentication mechanisms (e.g., OAuth, JWT) and authorization requirements.
  - [ ] Error Handling Documentation: Automatically extract error handling logic from the source code and include it in the generated documentation.
  - [ ] Versioning Support: Add support for documenting multiple versions of an API and handling version-specific endpoints and data models.
  - [ ] API Testing Integration: Integrate with API testing frameworks or tools to automatically generate test cases based on the OpenAPI specification.

- ### Phase 6: Updates and Maintenance
  
  - [ ] Stay Up-to-Date with OpenAPI Specification: Regularly update the generator to support the latest version of the OpenAPI specification.
  - [ ] Monitor Language and Framework Updates: Keep track of updates in programming languages and frameworks to ensure compatibility and make necessary adjustments.

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Contributing -->

## :wave: Contributing

<a href="https://github.com/imperiumx/specitron/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=imperiumx/specitron" />
</a>

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

See `contributing.md` for ways to get started.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Commiting your code

Before sending patches please make sure you have [pre-commit](https://pre-commit.com/) activated in your local git repository:

```sh
pre-commit install
```

This will ensure that your code is cleaned before you commit it.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Code of Conduct -->

### :scroll: Code of Conduct

Please read the [Code of Conduct](https://github.com/imperiumx/specitron/blob/master/CODE_OF_CONDUCT.md)

<!-- FAQ -->

## :grey_question: FAQ

<details closes>
  <summary>What is an OpenAPI specification?</summary>
  <p>An OpenAPI specification is a standardized way to describe and document RESTful APIs. It defines the endpoints, request/response formats, parameters, and other details required to interact with an API.</p>
</details>

<details closes>
  <summary>How does an OpenAPI specification generator work?</summary>
  <p>OpenAPI specification generators typically analyze source code or API endpoints to extract information about the available endpoints, request/response formats, parameters, and other relevant details. They use this information to automatically generate the OpenAPI specification file, usually in JSON or YAML format.</p>
</details>

<details closes>
  <summary>Can an OpenAPI specification generator support multiple programming languages?</summary>
  <p>Yes, many OpenAPI specification generators are designed to support multiple programming languages. They can analyze code written in various languages such as Python, JavaScript, Java, Ruby, and more, and generate the corresponding OpenAPI specification.</p>
</details>

<details closes>
  <summary>Can an OpenAPI specification generator be integrated into existing workflows or tools?</summary>
  <p>Yes, most OpenAPI specification generators offer integrations with popular development tools and workflows. They can be integrated into build systems, continuous integration/continuous deployment (CI/CD) pipelines, documentation platforms, and API management systems to automate the process of generating and updating API specifications.</p>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- License -->

## :warning: License

Distributed under the no License. See LICENSE.txt for more information.

<!-- Contact -->

## :handshake: Contact

Your Name - [@imperiumxx](https://twitter.com/imperiumxx) - <imperiumx.dev@gmail.com>

LinkedIn: [https://www.linkedin.com/in/imperiumx/](https://www.linkedin.com/in/imperiumx/)

Project Link: [https://github.com/imperiumx/specitron](https://github.com/imperiumx/specitron)

<!-- Acknowledgments -->

## :gem: Acknowledgements

Use this section to mention useful resources and libraries that you have used in your projects.

- [Shields.io](https://shields.io/)
- [Awesome README](https://github.com/matiassingers/awesome-readme)
- [Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md#travel--places)
- [Readme Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
