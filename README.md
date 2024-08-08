# Image to Story Generator

## Overview

The Image to Story Generator is a Streamlit application that generates short stories based on images. It uses a pre-trained GPT-2 model to create imaginative narratives inspired by the given image. While the application currently uses placeholder text for image features, the goal is to integrate real image feature extraction in the future.

## Features

- **Image Upload**: Upload an image in JPG or PNG format.
- **Story Generation**: Generate a short story based on the uploaded image using the GPT-2 model.
- **Display**: View the uploaded image and the generated story.

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

- Python 3.7+
- pip

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/image-to-story-generator.git
    cd image-to-story-generator
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

    Ensure `requirements.txt` contains the following dependencies:

    ```txt
    streamlit
    torch
    transformers
    ```

4. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

## Usage

1. **Run the application** using the command provided in the setup instructions.

2. **Upload an image**: Use the sidebar to upload an image file (.jpg or .png).

3. **Generate a story**: After uploading the image, the application will generate and display a short story based on the image.

## File Structure

- `app.py`: Main application file containing the Streamlit code.
- `README.md`: This README file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.

## Contact

For any questions or inquiries, please contact [njnagaraj007@gmail.com].
