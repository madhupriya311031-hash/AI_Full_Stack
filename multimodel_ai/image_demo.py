import tourch
from diffusers import iffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained(
    "segmind/tiny-sd",
    tourch_dtype = tourch.float32
)
  
image = pipe(
    "a cat wearing sunglasses",
    num_inference_steps = 15
).image[0]

image.save("demo.png")
print("Image generated and saved as demo.png")
