## Clean Frame

Remove and replace photo backgrounds easily with a simple web app.

### Features
- **Background removal**: Upload a JPG/PNG and remove the background using `rembg`.
- **Transparent download**: Save the cut-out as a transparent PNG.
- **Solid color backgrounds**: Pick any color and apply it as a new background.

### Tech stack
- **Streamlit** for the UI
- **Pillow (PIL)** for image handling
- **rembg** for background removal

### Getting started
#### Prerequisites
- Python 3.9 or newer

#### Setup
```bash
git clone <your-repo-url>
cd CleanFrame

# (Recommended) Create a virtual environment
python -m venv .venv

# Activate it
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
# macOS/Linux (bash/zsh)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run the app
```bash
streamlit run app.py
```

Open the URL printed in the terminal (usually `http://localhost:8501`).

### Usage
1. Upload a `png`, `jpg`, or `jpeg` image.
2. Choose between:
   - **Download Transparent**: exports a cut-out PNG with transparency.
   - **Add Background Color**: pick a color, preview, then download the result.

### Project structure
```
CleanFrame/
  ├─ app.py            # Streamlit app
  ├─ requirements.txt  # Python dependencies
  └─ README.md         # This file
```

### Troubleshooting
- If background removal is slow on first run, the model may be initializing; try again after the first image.
- If installation fails, upgrade `pip` and retry: `python -m pip install --upgrade pip`.
- If you have a dedicated GPU and want acceleration, consider installing a GPU-enabled `onnxruntime` build that matches your environment.

### License
Add a license of your choice (e.g., MIT) to the repository if you intend to share or distribute the project.

