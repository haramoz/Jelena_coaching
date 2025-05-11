import requests
import json

card_data = {
    "Name": "Omnivore Specialist",
    "Condition": "Birds that eat [wild]",
    "Explanatory text": "Any bird that specifically has a [wild] symbol as part of its food cost.",
    "VP": "2[point] per bird"
}

# Serialize the JSON data into a string
card_details = json.dumps(card_data, indent=2)

prompt = f"I need you to generate a bonus card for popular game Wingspan game, with the following details, please change the final victory points (VP) as feathers.\n\nBonus Card Details:\n{card_details}"


response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/core",
    headers={
        "authorization": f"Bearer ...",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": prompt,
        "output_format": "jpeg",
    },
)

if response.status_code == 200:
    with open("generated_image.jpeg", "wb") as file:
        file.write(response.content)
    print("Image generated successfully! Saved as 'generated_image.jpeg'.")
else:
    print(f"Error: {response.status_code} - {response.text}")

