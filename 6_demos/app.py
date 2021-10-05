import gradio as gr

title = "BERTIN, tengo una pregunta"
description = "BERTIN large fine-tuned con el corpus SQAC (Spanish Question-Answering Corpus)"
examples = [
    ["BERTIN es un conjunto de modelos de NLP tipo RoBERTa entrenados durante el evento JAX/Flax organizado por Hugging Face.", "¿Qué es BERTIN?"],
    ["El corpus SQAC fue creado por un equipo del Barcelona Supercomputing Center y la sigla proviene de Spanish Question-Answering Corpus.", "¿Qué significa SQAC?"]
]
article = """
<p style="text-align: center">
    NLP en ES 🤗 | <a target=”_blank” href="https://nlp-en-es.org"> nlp-en-es.org </a>
</p>
"""

gr.Interface.load(
    name="huggingface/nlp-en-es/bertin-large-finetuned-sqac",
    inputs=[gr.inputs.Textbox(label="Contexto"), gr.inputs.Textbox(label="Pregunta")],   
    outputs=gr.outputs.Textbox(label="Respuesta"),
    title=title,
    description=description,
    article=article,
    examples=examples,
    theme="huggingface",
    allow_screenshot=True,
    allow_flagging=True,
    flagging_dir="flagged",
    enable_queue=True
).launch()
