# Data Extraction from Image
This Python command-line utility extracts and digitizes interviewee data from an image and outputs the structured data into a JSON file.

## Features
* Dynamically accepts input image paths through command-line arguments using 'argparse'.
* Initially uses **OpenCV** for initial image loading and preprocessing.
* Initially uses **EasyOCR** for recognizing and extracting the text.
* Exports formatted data to a 'output.json' file.

**Update:**

* Used Pillow for directly opening the image.
* Used Gemini API for recognizing and extracting the text automatically.

## Setup Instructions

1. **Clone the repository:**

git clone [https://github.com/Sanjana-Sara-Siju/image-data-extraction.git](https://github.com/Sanjana-Sara-Siju/image-data-extraction.git)

cd image-data-extraction.git

2. **Create and activate a virtual environment**

python -m venv venv

venv\Scripts\activate

3. **Install the required dependencies**

pip install -r requirements.txt

4. **Run the script from the terminal by providing the image path using --image**

python dataExtraction.py --image "Interview Cover Sheet.jpeg"


**Note:** You must create a .env file in the root directory and add your GEMINI_API_KEY for the script to authenticate.


## Limitations
- The formatted data in the JSON file does not make complete sense as it is in the image


