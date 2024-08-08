import streamlit as st
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def generate_story(image_url):
    # Step 1: Get image features (You'll need to implement this part)

    # For demonstration, we'll just use a placeholder text
    image_features = "Placeholder Image Features"

    # Step 2: Generate story using GPT-2
    prompt = f"Image: {image_url}\nFeatures: {image_features}\nGenerate a short story about this image:"
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Generate story
    with torch.no_grad():
        output = model.generate(input_ids, max_length=500, num_return_sequences=1, no_repeat_ngram_size=2)

    # Decode and return the generated story
    generated_story = tokenizer.decode(output[0], skip_special_tokens=True)

    # Clean up the story
    generated_story = generated_story.split("Image:", 1)[1]  # Removing text before the story
    generated_story = generated_story.split("Generated", 1)[0]  # Removing text after the story

    return generated_story.strip()

def main():
    st.title("Image to Story Generator")
    st.write("Upload an image and get a short story generated!")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Generating story...")

        # Convert image to URL
        image_url = uploaded_image.name
        story = generate_story(image_url)

        st.write("Generated Story:")
        st.write(story)

if __name__ == "__main__":
    main()
