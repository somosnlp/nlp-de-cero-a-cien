import gradio as gr

title = "RoBERTa, tengo una pregunta"
description = "Modelo tipo RoBERTa pre-entrenado por BSC-TeMU con la base de datos de la Bibliotecha Nacional de España y fine-tuned con el corpus SQAC (Spanish Question-Answering Corpus)."
examples = [
    ["¡Hola, mundo! Somos NLP en ES 🤗 la comunidad de hispanohablantes de la iniciativa “Languages at HuggingFace” y queremos democratizar el NLP en nuestro idioma. Somos una red internacional y nuestro objetivo es crear y compartir recursos que posibiliten y aceleren el avance del NLP en español.", "¿Quiénes somos?"]
]
article = """
<p style="text-align: center">
    NLP en ES 🤗 | <a target=”_blank” href="https://nlp-en-es.org"> nlp-en-es.org </a>
</p>
"""

gr.Interface.load(
    name="huggingface/nlp-en-es/roberta-base-bne-finetuned-sqac",
    inputs=[gr.inputs.Textbox(label="Contexto", lines=5), gr.inputs.Textbox(label="Pregunta")],   
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
