# Compas usage Map

This automatic deployed application displays information and icons for companies. It loads company data from JSON configuration files and serves it via static routes. The app is designed to be statically frozen using `Flask-Frozen`, allowing it to be deployed easily.

## Table of Contents
- [How It Works](#how-it-works)
- [Embedding as an Iframe](#embedding-as-an-iframe)
- [Adding New Companies](#adding-new-companies)
- [Setup](#setup)
- [Running the App](#running-the-app)
- [Freezing the App](#freezing-the-app)
- [License](#license)

## How It Works

The app serves company information, including images (icons and their backgrounds), by reading data from a structured directory. Each company has a folder containing a JSON configuration file and two images (`icon.png` and `icon_bg.png`). The app dynamically generates routes to serve each company’s icon and background images.

### Directory Structure

```
.
├── templates
│   ├── index.html
│   └── company
│       ├── company1
│       │   ├── config.json
│       │   ├── icon.png
│       │   └── icon_bg.png
│       └── company2
│           ├── config.json
│           ├── icon.png
│           └── icon_bg.png
```

- **config.json**: Contains the metadata for the company.
- **icon.png**: The icon for the company.
- **icon_bg.png**: The background image for the company.

### Key Features
- Dynamically loads and serves company data.
- Supports freezing the application with `Flask-Frozen` for easy deployment as a static site.
- Includes company-specific URLs for icons and backgrounds, such as `/company/<name>/icon.png`.

## Embedding as an Iframe

To embed this application into a website as an iframe, you can use the following HTML code. 

```html
<iframe src="https://hslu-dc.github.io/compas_rrc_map/" width="100%" height="600" frameborder="0">
  Your browser does not support iframes.
</iframe>
```
You can adjust the `width` and `height` attributes to fit your website’s layout.

## Adding New Companies

To add a new company to the app, follow these steps:

1. **Create a Directory for the Company:**
   Inside the `templates/company/` directory, create a new folder named after the company. For example, if the company name is `new_company`, create the following structure:

   ```
   templates/company/new_company/
   ```

2. **Add a JSON Configuration File:**
   Inside the new company directory, create a file named `config.json` with the following structure:

   ```json
   {
        "name": "new_company",
        "namenice": "New Company",
        "coordinates": [52.5200, 13.4050],
        "contact": {"Max Mustermann": "mm@test.com"},
        "path": "https://test/company/test",
        "description": "Quaerat consequatur dolorem libero enim. Architecto officia enim ducimus error et voluptatem. Ut molestias ab recusandae et qui at aperiam",
        "projects": [
            {"name": "Project 1", "description": "Description of Project 1", "path": "https://test/companies/company1/projects/project1.html"},
            {"name": "Project 2", "description": "Description of Project 2", "path": "https://test/companies/company1/projects/project2.html"}
        ]
        }
   ```

3. **Add Company Images:**
   - Add the company's icon as `icon.png`.
   - Add the company's background image as `icon_bg.png`.

   Ensure both images are placed in the same directory as the `config.json` file:
   
   ```
   templates/company/new_company/
   ├── config.json
   ├── icon.png
   └── icon_bg.png
   ```
    You can use the exmaple files in the ```./icon``` folder to create your custom icons

4. **Deploy the Changes:**
   After adding the company add all new files to the repo and commit them to the main branch, to trigger the automatic recreation of the main page.

## Local Tests

### Setup

To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/company-map-app.git
   cd company-map-app
   ```

2. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the directory structure as shown above in the [Directory Structure](#directory-structure) section.

### Running the App

To run the app in development mode:

1. Activate the virtual environment (if not already activated):
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Run the Flask app:
   ```bash
   python app.py
   ```

3. Open a browser and navigate to `http://localhost:8080` to see the app.

### Freezing the App

To freeze the app and generate static HTML pages:

1. Ensure the virtual environment is activated.
   
2. Run the freeze command:
   ```bash
   python app.py freeze
   ```

3. The frozen site will be generated inside the `build/` directory. You can now host these static files on any static hosting platform (e.g., GitHub Pages, Netlify).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This README provides clear instructions on how the app works, how to add new companies, how to embed it as an iframe, and how to run and freeze the app. Let me know if you need further adjustments or details!