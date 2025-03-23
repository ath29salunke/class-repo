from flask import Flask, render_template, request
from vertexai.preview.vision_models import ImageGenerationModel
import vertexai
import io
import base64

app = Flask(__name__)

# Initialize Vertex AI
vertexai.init(project="tt-sandbox-001", location="us-central1")
generation_model = ImageGenerationModel.from_pretrained("imagen-3.0-fast-generate-001")

def generate_images(prompt, num_images=4):
    """Generate multiple images from the given prompt."""
    try:
        images = generation_model.generate_images(
            prompt=prompt,
            number_of_images=num_images,  # Generate 3-4 images
            aspect_ratio="1:1",
            add_watermark=True,
        )

        base64_images = []
        for img in images:
            # Convert PIL image to base64
            pil_image = img._pil_image
            img_io = io.BytesIO()
            pil_image.save(img_io, format="PNG")
            img_io.seek(0)
            base64_image = base64.b64encode(img_io.getvalue()).decode("utf-8")
            base64_images.append(base64_image)

        return base64_images

    except Exception as e:
        print(f"Error generating images: {e}")
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    images_data = []
    error_message = None

    if request.method == "POST":
        prompt = request.form.get("prompt")

        if prompt and prompt.strip():
            images_data = generate_images(prompt.strip(), num_images=4)
            if not images_data:
                error_message = "Failed to generate images. Please try again."
        else:
            error_message = "Please enter a valid prompt."

    return render_template("index.html", images_data=images_data, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
