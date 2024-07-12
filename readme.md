# Automatic MCQ Completion Project

This project automates the process of completing multiple-choice questions (MCQs) using Python and Selenium. It utilizes an AI service from Google AI Labs to generate answers and interacts with a web interface to fill in the answers automatically.
 ```diff
 -⚠️ Educational Use Disclaimer: This project is developed solely for educational purposes. 
 -Use of this code for personal or production purposes is not recommended. 
 -Any such use is at your own risk, and the author assumes no responsibility for any issues that may arise.
 -Read the Disclaimer at the end of the page.
```


## Features

- Automates the filling of MCQs on web-based platforms.
- Uses AI to generate answers for the MCQs.
- Simple configuration through environment variables.

## Prerequisites

- Python 3.8 or higher
- Google AI Labs API Key

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/knight7080/automatic-mcq-completion.git
cd automatic-mcq-completion
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

For Windows:
```bash
venv\Scripts\activate
```

For macOS/Linux:
```bash
source venv/bin/activate
```

### Step 4: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 5: Get Your API Key from Google AI Labs

1. Go to [Google AI Labs](https://ai.google.com).
2. Sign in with your Google account.
3. Navigate to the API section and generate a new API key.

### Step 6: Configure Environment Variables

Create a `.env` file in the project root directory and add your API key:

```dotenv
API_KEY=your_google_ai_labs_api_key
```

## Usage

Run the script to start the automation:

```bash
python main.py
```

Give the URL of the MCQ page as input in the prompt window:
```
Enter the Url for the MCQ: <your_url_input>
```
The script will automatically read the MCQs from the web interface, use the Google AI Labs API to generate answers, and fill them in.

## Disclaimer
This project has been developed exclusively for educational purposes to demonstrate certain concepts and techniques. It is not intended for personal, commercial, or production use. If you choose to use this code for purposes other than education, you do so at your own risk and assume full responsibility for any outcomes, including legal, technical, or operational issues. The author of this code disclaims any liability for damages or problems that may arise from its unauthorized use. Please ensure you understand and comply with all applicable laws and regulations before using this code in any non-educational context.


## Issues and Bug Fixes
1. If the program crashes, simply close the terminal and restart the program.
2. If it crashes again, doing it manually is advisable.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
