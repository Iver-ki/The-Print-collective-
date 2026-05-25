import gradio as gr
import os
from ai_logic import Modelgenerator


#Loading the AI model -
ai_motor = Modelgenerator()

def generate_3d(objekt_tekst, materiale, progress=gr.Progress()):
    if not objekt_tekst.strip():
        return None, "Vennligst skriv inn noe i tekstfeltet."

    progress(0, desc="Starter opp...")
    prompt = f"{objekt_tekst} made of {materiale.lower()}"

    try:
        # Runs the generation process -
        filnavn = ai_motor.generate(prompt)

        if os.path.exists(filnavn):
            return str(filnavn), f"Suksess! Genererte {objekt_tekst} i {materiale}."
        else:
            return None, "Kunne ikke finne den genererte filen."
    except Exception as e:
        return None, f"En feil har oppstått: {str(e)}"

# Creates the website interface -
with gr.Blocks(title="AI 3D Studio") as demo:
    gr.Markdown("# The Print Collective ")
    gr.Markdown("AI 3D Studio")

    with gr.Row():
        with gr.Column():
            input_tekst = gr.Textbox(label="Hva vil du lage? (Skriv på engelsk for best resultat)", placeholder="Eks: A simple chair")
            input_mat = gr.Dropdown(choices=["Kompositt", "Metall", "Plastikk"], label="Materiale", value="Plastikk")
            btn = gr.Button("Generere 3D-modell", variant="primary")

        with gr.Column():
            # 3D viewer -
            output_3d = gr.Model3D(label="3D Visning")
            output_msg = gr.Textbox(label="Status")

    # Connects the button to the function -
    btn.click(fn=generate_3d, inputs=[input_tekst, input_mat], outputs=[output_3d, output_msg])

# Starts the app -
if __name__ == "__main__":
    demo.launch(show_error=True, debug=False, share= True)