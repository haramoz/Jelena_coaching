import streamlit as st
import random
import json
import base64
from streamlit.components.v1 import html

# Read JSON data from file
try:
    with open("bonus.json", "r") as file:
        cards = json.load(file)
except FileNotFoundError:
    st.error("The file 'bonus.json' was not found.")
    cards = []
except json.JSONDecodeError:
    st.error("The file 'bonus.json' contains invalid JSON.")
    cards = []

# Filter cards by expansion = "originalcore"
originalcore_cards = [card for card in cards if card.get("Expansion") == "originalcore"]

# Streamlit app setup
st.title("Wingspan Bonus Card Generator")

st.write("Click on the button below to reveal a randomly generated bonus card!")

# Function to display card details with animation
def display_card_details_with_animation(card):
    st.markdown(
        f"""<div style='animation: fade-in 1s;'>
        <h2>{card['Name']}</h2>
        <p><strong>Condition:</strong> {card['Condition']}</p>
        <p><strong>Explanatory Text:</strong> {card['Explanatory text']}</p>
        <p><strong>Victory Points (VP):</strong> {card['VP']}</p>
        </div>""",
        unsafe_allow_html=True
    )

# Add an image as a button using a custom HTML component
image_path = "bonus-background.jpg"
with open(image_path, "rb") as image_file:
    image_data = image_file.read()
    image_base64 = "data:image/jpg;base64," + base64.b64encode(image_data).decode()

# Add JavaScript and CSS for animation
animation_code = """
<style>
@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}
.fade-in {
  animation: fade-in 1s;
}
</style>
<script>
function revealCard() {
    const details = document.getElementById('card-details');
    if (details) {
        details.style.display = 'block';
        details.classList.add('fade-in');
    }
}
</script>
"""

st.markdown(animation_code, unsafe_allow_html=True)

html_code = f"""
<div style="">
    <img src="{image_base64}" alt="Bonus Card" style="width: 65px; height: 90px; cursor: pointer;">
</div>
"""
html(html_code, height=120)

# Check if the card should be revealed
if "Draw Bonus Card" not in st.session_state:
    st.session_state.reveal_card = False

if st.button("Draw Bonus Card"):
    st.session_state.reveal_card = True

if st.session_state.reveal_card:
    if originalcore_cards:
        random_card = random.choice(originalcore_cards)

        display_card_details_with_animation(random_card)
    else:
        st.write("No bonus cards available from the 'originalcore' expansion.")

st.write("Click the button below to randomly generate two distinct bonus cards!!")


html_code = f"""
<div style="">
    <img src="{image_base64}" alt="Bonus Card" style="width: 65px; height: 90px; cursor: pointer;">
    <img src="{image_base64}" alt="Bonus Card" style="width: 65px; height: 90px; cursor: pointer;">

</div>
"""
html(html_code, height=120)

if st.button("Draw Two Bonus Cards"):

    if len(originalcore_cards) >= 2:
        card1, card2 = random.sample(originalcore_cards, 2)

        col1, col2 = st.columns(2)

        with col1:
            display_card_details_with_animation(card1)

        with col2:
            display_card_details_with_animation(card2)
    else:
        st.write("Not enough bonus cards available from the 'originalcore' expansion to generate two distinct cards.")
