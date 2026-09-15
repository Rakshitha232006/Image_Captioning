# Image Captioning

An AI-powered image captioning application that analyzes an uploaded image, generates a natural-language caption, and converts the caption into audio.

## 🚀 Live Demo

https://imagecaptioning-4zxb9wortubtudlrss9ysu.streamlit.app/

## 📌 Features

- Upload an image through the Streamlit web interface
- Generate an AI-based description of the image
- Display the generated image caption
- Convert the caption into speech
- Play the generated audio directly in the application
- Supports JPG, JPEG, PNG, and WebP images

## 🛠️ Technologies Used

- Python
- Streamlit
- PyTorch
- Hugging Face Transformers
- BLIP
- VITS
- Pillow
- NumPy
- SciPy

## 🤖 Models Used

### Image Captioning

**Salesforce/blip-image-captioning-large**

BLIP is used to generate a natural-language description of the uploaded image.

### Text-to-Speech

**kakao-enterprise/vits-ljs**

VITS is used to convert the generated image caption into speech.

## 🔄 How It Works

```text
Upload Image
     ↓
BLIP Image Captioning
     ↓
Generated Caption
     ↓
VITS Text-to-Speech
     ↓
Generated Audio
```

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Rakshitha232006/Image_Captioning.git
```

### 2. Open the project

```bash
cd Image_Captioning
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

On Windows:

```powershell
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run main.py
```

## 📂 Project Structure

```text
Image_Captioning/
│
├── main.py
├── requirements.txt
├── packages.txt
├── .gitignore
└── README.md
```

## 🖼️ Application Workflow

```text
Input Image
     ↓
Image Processing
     ↓
BLIP Model
     ↓
Image Caption
     ↓
VITS Model
     ↓
Audio Description
```

## 📊 Output

The application provides:

- Uploaded image
- Generated image caption
- Audio version of the generated caption

## 🎯 Project Goal

The goal of this project is to combine computer vision and speech synthesis to create an application that can understand an image, describe its contents using natural language, and provide the description as audio.

## 🌐 Deployment

The application is deployed using Streamlit Cloud.

### Live Application

https://imagecaptioning-4zxb9wortubtudlrss9ysu.streamlit.app/

## 👩‍💻 Author

**Rakshitha**

GitHub: https://github.com/Rakshitha232006

## 📄 License

This project is intended for educational and project demonstration purposes.
