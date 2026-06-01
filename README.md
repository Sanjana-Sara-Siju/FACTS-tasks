# Data Extraction from Image
This Python command-line utility extracts and digitizes interviewee data from an image and outputs the structured data into a JSON file.

## Features
* Dynamically accepts input image paths through command-line arguments using 'argparse'.
* Uses **OpenCV** for initial image loading and preprocessing.
* Uses **EasyOCR** for recognizing and extracting the text.
* Exports formatted data to a 'output.json' file.

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

## Limitations
- The formatted data in the JSON file does not make complete sense as it is in the image


