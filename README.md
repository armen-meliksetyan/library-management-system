## Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes. Follow these simple steps to set up your development environment.

### Prerequisites

Ensure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Setting Up a Virtual Environment

To isolate the project dependencies, use Python's built-in module `venv` to create a virtual environment. Here's how you can set it up:

1. **Navigate to Your Project Directory**:
   Open a terminal and navigate to the directory where your project is stored.

2. **Create the Virtual Environment**:
   Run the following command to create a virtual environment named `venv`. You can name it anything you prefer; `venv` is a common standard:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   Before installing dependencies and running the project, you need to activate the virtual environment. Activation varies by operating system:

   - **On Windows**:
     ```bash
     .\venv\Scripts\activate
     ```

   - **On macOS and Linux**:
     ```bash
     source venv/bin/activate
     ```
   When the virtual environment is activated, you'll see the environment name `(venv)` appear at the beginning of your terminal's command line.

### Installing Dependencies

With your virtual environment activated, install the project dependencies using `pip`, which is Python’s package installer:

```bash
pip install -r requirements.txt
```

This command reads the `requirements.txt` file in your project directory (make sure you have one), where all necessary packages are listed, and installs them into your virtual environment.

### Running the Application

Now that your environment is set up and dependencies are installed, you can run the application locally:

```bash
python src/main.py
```



