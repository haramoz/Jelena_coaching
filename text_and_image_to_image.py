import requests
import json
import base64


card_data = {
    "Name": "Omnivore Specialist",
    "Condition": "Birds that eat [*]",
    "Explanatory text": "Any bird that specifically has a [*] symbol as part of its food cost.",
    "VP": "2[point] per bird"
}

# Serialize the JSON data into a string
card_details = json.dumps(card_data, indent=2)

prompt = f"I need you to generate a bonus card for popular game Wingspan game.\n Use the input image as template.\nBonus Card Details:\n{card_details}"


source_image_path = "sample.png"
strength = 0.95

with open(source_image_path, "rb") as source_image:
    #image_data = base64.b64encode(source_image.read()).decode("utf-8")

    files = {
        "image": source_image,
    }

    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
        headers={
            "authorization": f"Bearer",
            "accept": "image/*"
        },
        files=files,
        data={
            "prompt": prompt,
            "mode": "image-to-image",
            "strength": strength,
            "output_format": "jpeg",
            },
        )

    if response.status_code == 200:
        with open("./output1.jpeg", 'wb') as file:
            file.write(response.content)
        print("Image generated successfully! Saved as 'generated_image.jpeg'.")

    else:
        raise Exception(str(response.json()))