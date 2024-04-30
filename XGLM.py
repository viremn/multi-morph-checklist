# Use a pipeline as a high-level helper
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("facebook/xglm-564M")
model = AutoModelForCausalLM.from_pretrained("facebook/xglm-564M")

text = 'This is a test'






