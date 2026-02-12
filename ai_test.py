import torch
from diffusers import ShapEPipeline
from diffusers.utils import export_to_ply

# Sjekk om GPU (RTX 5060) er tilgjengelig
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Bruker enhet: {device}")

# Last inn modellen (dette laster ned ca 2GB første gang)
print("Laster inn KI-modell...")
pipe = ShapEPipeline.from_pretrained("openai/shap-e", torch_dtype=torch.float16)
pipe = pipe.to(device)

# Generer en enkel test-figur
prompt = "a simple shark"
print(f"Genererer: {prompt}...")
images = pipe(prompt, guidance_scale=15.0, num_inference_steps=64, output_type="mesh").images

# Lagre resultatet som en 3D-fil
export_to_ply(images[0], "test_shark.ply")
print("Suksess! Filen 'test_shark.ply' er opprettet i mappen din.")
