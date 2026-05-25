# The-Print-collective-
---------------
This project uses Shap-E for generating 3D models ready for printing in both a .PLY and .GLB file. Keep in mind the process of entering the local website takes time, and a good graphics card is suggested.

# System requirements
- Python 3.9 + 
- Recommended: NVIDIA GPU with CUDA support (4GB+ VRAM)
- Minimum RAM: 8GB
- If GPU is not available, the program will run on CPU and generation will be significantly slower. 

The website is in **NORWEGIAN** but prompts are advised to be written in English for best possible result.

- Material options

1. Metall - Meant for heavy-duty parts
2. Plastikk - Quick and lighter parts
3. Kompositt - Meant for light and solid parts.

- Shap-E 
For best results when generating models, write prompts in english.
# Example - "Simple Chair", "Detailed green shoes" ...

--------------
!!! Installation guide !!!

# Step 1
Create a virtual environment
 - python -m venv venv 

To activate the (venv) - 
 - venv\Scripts\activate      - Windows 
 - source venv\bin\activate   - Linux


# Step 2 (Optional but recommended - GPU support)
If you have an NVIDIA GPU, install PyTorch with CUDA support for significantly faster generation:
- pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128

If you dont have an NVIDIA GPU skip this step. 

# Step 3
Install packages 
- pip install -r requirements.txt


# Step 4
Run the program
 - Python App.py     - Windows
 - Python3 App.py    - Linux

# When the website is ready two links will appear in the terminal.
 - Open this link with (ctrl + click)


# Tips

 - If the 3D model is not showing up in the showcase window, try switching to another browser.
  - Example: If Chrome is not working, try Microsoft Edge.

# Loading
If the process takes to long, or the models is not very good try lowering/ highten settings below directly in the "ai_logic.py" file - 

## guidance_scale - For the AI creativity. if you want it more strict.
 - Lower number = creative
 - Higher number = Strict

## num_inference_steps - Details and polish for the 3D model
- Lower number = Quick process, result might be blurry (not very detailed)
- Higher number = Slower, requires more power, Results will be more detailed and clear.

# Recommended values -
---------------
 - Guidance_scale - 15 (standard)                    -  Quick test (7)
 - Num_inference_steps - 70 (standard) <64 - 128>    -  Quick test (20)