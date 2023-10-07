from summarizer import TransformerSummarizer
def pdf_summary(body):
    
    GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")
    full = ''.join(GPT2_model(body, min_length=100))
    return full