#Contains the logic behind the AI generating for the printer

#Imports 
import torch 
from diffusers import ShapEPipeline
from diffusers.utils import export_to_ply

#Checks if the (GPU) Graphics card is available and strong enough to run the building process, if not it will run on the CPU (processor).
class Modelgenerator:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.pipe = ShapEPipeline.from_pretrained("openai/shap-e", torch_dtype=torch.float16)
        self.pipe = self.pipe.to(self.device) 

    #The AI generates the 3D model/build and makes it a PLY file
    def generate(self, prompt):

        #If the prompt is very long this shortens the name down to 25 characters.
        safe_name = prompt[:25].replace(" ", "_")
        
        model = self.pipe(prompt, guidance_scale=10.0, num_inference_steps=80, output_type="mesh")
        export_to_ply(model.images[0], f"{safe_name}.ply")
        return f"{safe_name}.ply"


