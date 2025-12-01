# Super Mario Streamlit Fun Hub
# Author: Fernando Macias
# Course: CSC 280 – Python Library Demonstration
# Library Focus: Streamlit (Web Development) Mario Video Game Theme
# -----------------------------
# HOW THIS FILE CONNECTS TO the ASSIGNMENT DIRECTIONS:
# - Step 1: Select a library → I selected Streamlit (Web Development).
# - Step 2: Propose a problem → My “problem” is that people don’t have
#   a simple, interactive place to explore the Mario universe and test their knowledge.
# - Step 3: Provide a solution → This Streamlit app is the solution.
#   It includes a strong visual component (webpage with text, tables, and images)
#   and demonstrates multiple Streamlit capabilities.
# -----------------------------
# STREAMLIT FEATURES DEMONSTRATED IN THIS FILE:
# 1. st.set_page_config → set page title and layout
# 2. st.title, st.header, st.subheader → page titles and section headers
# 3. st.sidebar.radio → navigation menu between sections
# 4. st.table / st.dataframe → display tables of characters, locations, power-ups
# 5. st.selectbox → choose characters / locations / quiz answers
# 6. st.button → submit quiz answers, move to next question, try again
# 7. st.image → display Mario-themed images (placeholder paths)
# 8. st.session_state → remember quiz score, question index, and answer submitted flag
# 9. st.text_input → let the user type their name
# 10. st.sidebar.slider → Mario fan level slider
# 11. st.checkbox → control how many fun facts are shown
# -----------------------------
# NOTE ABOUT AI USE (for eventual AI Use Statement section):
# -----------------------------
# This project was mainly designed and coded by me. I used outside resources
# only to learn Streamlit, get ideas for structure, fix specific problems,
# and follow the assignment guidelines. I used these tools only when needed
# and always rewrote or adapted everything myself.
#
# 1. Class Slides
#    I relied on our CSC 280 lecture slides notes (especially "CSC280_ProgLang_13.2"),
#    along with the other Python lectures that I learned in class, to help me understand how to set up
#    Streamlit, such as create the environment, and find official Streamlit example links, especially the ones
#    that were already provided in the CSC 280 lecture slides notes.
#    These slides gave me ideas for how to organize the app, what features to try,
#    and how Streamlit works. They also helped me start the initial layout and
#    structure of the project.
#
# 2. ChatGPT (GenAI)
#    I used ChatGPT in a limited way based on assignment instruction. 
#    I use it, only when I struggled with certain errors or when
#    I needed help understanding how to undo mistakes I made in the code.
#    ChatGPT also provided occasional suggestions on improving a few features
#    (for example, debugging quiz logic or solving layout issues). There were a few
#    times I took the suggestions, and most times I did not, because I needed to learn
#    how to fix most things on my own and follow the assignment instruction. Furthermore, 
#    I rewrote or adapted everything myself, so it followed my design and class requirements.
#
# 3. Google
#    When the Streamlit links from the slides were not enough, I followed the
#    assignment instruction that said I could use Google and GenAI resources.
#    I searched for short code snippets, documentation, and widget examples only
#    (such as how st.selectbox or st.session_state works). I used these examples
#    to learn the features and then rewrote them for my Mario project, instead of
#    copying any full app or complete code from the internet.
#
# 4. Mario Content and Basic Python Structures
#    The Mario facts, wording, and the simple Python data structures (lists,
#    dictionaries, and classes) are based on:
#    - my earlier Python assignment,
#    - my own class notes,
#    - w3schools Python Tutorial examples.
#    The way I defined the lists of dictionaries for characters, locations,
#    power-ups, and quiz questions follows the same style I learned from
#    w3schools and our class notes—only with my own Mario-themed data.

import streamlit as st
from typing import List, Dict

# -----------------------------
# BASIC PAGE SETUP
# -----------------------------
# layout="wide" so the tables (especially Characters) show more columns on screen.
# This uses Streamlit's built-in page configuration function to control the
# browser tab title, emoji icon, and overall layout for the whole app.
st.set_page_config(
    page_title="Super Mario Streamlit Fun Hub",
    page_icon="🍄",
    layout="wide"
)

# st.title is a Streamlit function that draws a big title at the top of the web app.
st.title("🍄 Super Mario Streamlit Fun Hub")

# st.text_input is a Streamlit widget that lets the user type their name.
# This shows how user input from a web form can be captured in Python.
player_name = st.text_input("Enter your name (optional):")
if player_name:
    # st.success shows a green success message box in the app.
    st.success(f"Welcome to the Mushroom Kingdom, {player_name}! 🌟")
else:
    # st.info shows an informational blue message box.
    st.info("Enter your name above to get a personalized greeting.")

# -----------------------------
# DATA SECTION
# -----------------------------
# The lists of dictionaries below (characters, power_ups, locations, quiz_questions)
# use basic Python data structures similar to examples from w3schools Python Tutorial
# and my class notes (e.g., how to store data in lists and dictionaries).
# I reused that style here but filled in my own Mario-based content.

characters: List[Dict] = [
    {"name": "Mario", "role": "Hero / Main Protagonist", "personality": "Brave, cheerful, always ready to save the day.", "first_appearance": "Donkey Kong (1981)", "image_path": "mario.png"},
    {"name": "Luigi", "role": "Mario's Younger Brother", "personality": "Shy but loyal, great jumper, sometimes scared.", "first_appearance": "Mario Bros. (1983)", "image_path": "luigi.png"},
    {"name": "Princess Peach", "role": "Princess of the Mushroom Kingdom", "personality": "Kind, graceful, sometimes captured by Bowser.", "first_appearance": "Super Mario Bros. (1985)", "image_path": "peach.png"},
    {"name": "Bowser", "role": "King of the Koopas / Main Villain", "personality": "Aggressive, stubborn, loves kidnapping Peach.", "first_appearance": "Super Mario Bros. (1985)", "image_path": "bowser.png"},
    {"name": "Toad", "role": "Mushroom Kingdom Helper", "personality": "Energetic, loyal, often helps Mario and friends.", "first_appearance": "Super Mario Bros. (1985)", "image_path": "toad.png"},
    {"name": "Yoshi", "role": "Friendly Dino Companion", "personality": "Cheerful, hungry, helps Mario with long jumps and eating enemies.", "first_appearance": "Super Mario World (1990)", "image_path": "yoshi.png"},
    {"name": "Bowser Jr.", "role": "Bowser's Son / Mini Villain", "personality": "Mischievous, stubborn, tries to impress his dad.", "first_appearance": "Super Mario Sunshine (2002)", "image_path": "bowser_jr.png"},
    {"name": "Toadette", "role": "Energetic Toad from the Mushroom Kingdom", "personality": "Friendly, cheerful, often appears as a helpful NPC.", "first_appearance": "Mario Kart: Double Dash!! (2003)", "image_path": "toadette.png"},
    {"name": "Princess Rosalina", "role": "Cosmic Princess / Luma Guardian", "personality": "Calm, mysterious, kind-hearted.", "first_appearance": "Super Mario Galaxy (2007)", "image_path": "rosalina.png"},
    {"name": "Princess Daisy", "role": "Princess of Sarasaland", "personality": "Energetic, tomboyish, confident, and competitive.", "first_appearance": "Super Mario Land (1989)", "image_path": "daisy.png"},
    {"name": "Kamek", "role": "Magikoopa / Bowser’s Servant", "personality": "Cunning, magical, loyal to Bowser.", "first_appearance": "Super Mario World 2: Yoshi’s Island (1995)", "image_path": "kamek.png"},
    {"name": "The Koopalings", "role": "Bowser’s Children / Mini-Bosses", "personality": "Mischievous, competitive among themselves.", "first_appearance": "Super Mario Bros. 3 (1988)", "image_path": "koopalings.png"},
    {"name": "Donkey Kong", "role": "Strong Gorilla Hero/Villain", "personality": "Powerful, friendly, loves bananas.", "first_appearance": "Donkey Kong (1981)", "image_path": "donkey_kong.png"},
    {"name": "Diddy Kong", "role": "DK’s Sidekick", "personality": "Cheeky, agile, good at driving karts.", "first_appearance": "Donkey Kong Country (1994)", "image_path": "diddy_kong.png"},
    {"name": "Cranky Kong", "role": "Elder Kong / Former Hero (Original Donkey Kong)", "personality": "Grumpy, wise, sarcastic, often gives advice or criticism and complains about modern games.", "first_appearance": "Donkey Kong Country (1994)", "image_path": "cranky_kong.png"},
    {"name": "Dixie Kong", "role": "Kong Heroine / DK Crew Member / Diddy’s Partner", "personality": "Brave, upbeat, adventurous, known for her spinning ponytail glide ability.", "first_appearance": "Donkey Kong Country 2: Diddy’s Kong Quest (1995)", "image_path": "dixie_kong.png"},
    {"name": "Koopas", "role": "Common Soldier Koopa Troopas", "personality": "Green and red shells, loyal to Bowser.", "first_appearance": "Super Mario Bros. (1985)", "image_path": "koopa_troopa.png"},
    {"name": "Dry Bones", "role": "Skeletal / Undead Koopa Troopa", "personality": "Silent, tough, collapses into bones and reforms after being defeated.", "first_appearance": "Super Mario Bros. 3 (1988)", "image_path": "dry_bones.png"},
    {"name": "Goombas", "role": "Weakest Common Enemy", "personality": "Simple, walking mushroom-like creatures.", "first_appearance": "Super Mario Bros. (1985)", "image_path": "goomba.png"},
    {"name": "Piranha Plant", "role": "Plant Enemy in Pipes", "personality": "Aggressive when Mario gets close.", "first_appearance": "Super Mario Bros. (1985)", "image_path": "piranha_plant.png"},
    {"name": "Chain Chomp", "role": "Metal Ball Enemy on a Chain", "personality": "Wild, strong, rattles its chain when angry.", "first_appearance": "Super Mario 64 (1996)", "image_path": "chain_chomp.png"},
    {"name": "Shy Guys", "role": "Masked Troop Enemy", "personality": "Quiet, often red-masked, follow orders.", "first_appearance": "Yoshi’s Island (1995)", "image_path": "shy_guys.png"},
    {"name": "Spiny", "role": "Spiked Shell Enemy", "personality": "Harder to stomp because of the spikes.", "first_appearance": "Super Mario Bros. (1985)", "image_path": "spiny.png"},
    {"name": "Hammer Bros", "role": "Hammer-Throwing Koopa Brothers", "personality": "Throw hammers at Mario from platforms.", "first_appearance": "Super Mario Bros. (1985)", "image_path": "hammer_bros.png"},
    {"name": "Bob-omb", "role": "Walking Bomb Enemy", "personality": "Marches around calmly until it’s ready to explode.", "first_appearance": "Super Mario Bros. 2 (1988)", "image_path": "bob_omb.png"},
    {"name": "King Bomb Omb", "role": "Boss Bomb King", "personality": "Huge bomb-like villain you defeat in Super Mario 64.", "first_appearance": "Super Mario 64 (1996)", "image_path": "king_bomb_omb.png"},
    {"name": "King Boo", "role": "Ghost King / Haunted House Villain", "personality": "Sneaky, loves scaring Mario and Luigi.", "first_appearance": "Luigi’s Mansion (2001)", "image_path": "king_boo.png"},
    {"name": "Luma", "role": "Star Companion", "personality": "Cute, loyal star-creatures that travel with Rosalina and Mario.", "first_appearance": "Super Mario Galaxy (2007)", "image_path": "luma.png"},
    {"name": "Boom Boom", "role": "Fortress Boss", "personality": "Strong, charges at Mario and swings his arms to attack.", "first_appearance": "Super Mario Bros. 3 (1988)", "image_path": "boom_boom.png"},
    {"name": "Pauline", "role": "Mayor of New Donk City / Mario's Old Friend", "personality": "Confident and stylish, originally the damsel from Donkey Kong.", "first_appearance": "Donkey Kong (1981)", "image_path": "pauline.png"},
    {"name": "Wario", "role": "Mario's Rival", "personality": "Rude, greedy, loves money and garlic.", "first_appearance": "Super Mario Land 2: 6 Golden Coins (1992)", "image_path": "wario.png"},
    {"name": "Waluigi", "role": "Luigi's Rival", "personality": "Sneaky, dramatic, often appears in sports and party games.", "first_appearance": "Mario Tennis (2000)", "image_path": "waluigi.png"},
    {"name": "Pom Pom", "role": "Boom Boom's sister", "personality": "Energetic, uses boomerangs and clones in battle.", "first_appearance": "Super Mario 3D Land (2011)", "image_path": "pom_pom.png"},
    {"name": "Boo", "role": "Shy Ghost Enemy", "personality": "Covers its face when Mario looks, chases when he turns away.", "first_appearance": "Super Mario Bros. 3 (1988)", "image_path": "boo.png"},
    {"name": "Cappy", "role": "Sentient Cap / Mario's Hat Partner", "personality": "Helpful, brave, lets Mario capture enemies and objects.", "first_appearance": "Super Mario Odyssey (2017)", "image_path": "cappy.png"},
    {"name": "Cappy's Sister (Tiara)", "role": "Sentient Crown / Peach's Friend", "personality": "Gentle and supportive, helps Peach in Super Mario Odyssey.", "first_appearance": "Super Mario Odyssey (2017)", "image_path": "tiara.png"},
    {"name": "Toadsworth", "role": "Elder Toad / Princess Peach's Steward", "personality": "Polite, worried, often gives advice and looks after Peach.", "first_appearance": "Super Mario Sunshine (2002)", "image_path": "toadsworth.png"},
]

power_ups: List[Dict] = [
    {"name": "Super Mushroom", "effect": "Makes Mario grow bigger and take an extra hit.", "image_path": "super_mushroom.png"},
    {"name": "Fire Flower", "effect": "Lets Mario throw fireballs at enemies.", "image_path": "fire_flower.png"},
    {"name": "Super Star", "effect": "Gives temporary invincibility.", "image_path": "super_star.png"},
    {"name": "1-Up Mushroom", "effect": "Gives an extra life.", "image_path": "one_up_mushroom.png"},
    {"name": "Ice Flower", "effect": "Lets Mario throw ice balls and freeze enemies.", "image_path": "ice_flower.png"},
    {"name": "Mini Mushroom", "effect": "Shrinks Mario so he can fit in tiny places.", "image_path": "mini_mushroom.png"},
    {"name": "Cat Suit", "effect": "Gives Mario a cat costume with climbing and scratch attack.", "image_path": "cat_suit.png"},
    {"name": "Tanooki Suit", "effect": "Gives Mario a raccoon tail and ability to fly or turn into statue.", "image_path": "tanooki_suit.png"},
]

locations: List[Dict] = [
    {"name": "Mushroom Kingdom", "description": "The main world where Princess Peach rules.", "image_path": "mushroom_kingdom.png"},
    {"name": "Bowser’s Castle", "description": "A dangerous fortress full of lava and traps.", "image_path": "bowser_castle.png"},
    {"name": "Rainbow Road", "description": "A colorful, difficult racetrack in the Mario Kart games.", "image_path": "rainbow_road.png"},
    {"name": "Donkey Kong’s Construction Site", "description": "The place where Mario first appeared.", "image_path": "dk_construction_site.png"},
    {"name": "Ice Kingdom", "description": "A frosty world ruled by penguins, with slippery ice platforms and frozen lakes.", "image_path": "ice_kingdom.png"},
    {"name": "Jungle Kingdom", "description": "A lush jungle world ruled by the Kongs; their king is Cranky Kong.", "image_path": "jungle_kingdom.png"},
    {"name": "Yoshi Island", "description": "A peaceful island inhabited by Yoshis, full of vibrant greenery and eggs.", "image_path": "yoshi_island.png"},
    {"name": "Dry Dry Desert", "description": "A hot, arid desert world with quicksand, cacti, and ancient temples.", "image_path": "dry_dry_desert.png"},
    {"name": "Dark Lands", "description": "Bowser’s desolate realm, filled with lava, ominous skies, and danger at every turn.", "image_path": "dark_lands.png"},
]

fun_facts: List[str] = [
    "Mario was originally called 'Jumpman' in Donkey Kong.",
    "Luigi's name comes from the Japanese word 'ruiji', meaning 'similar'.",
    "Princess Peach was known as 'Princess Toadstool' in early English games.",
    "Bowser is also known as 'King Koopa' in some versions.",
    "Mario is a plumber who first appeared in Donkey Kong (1981).",
    "Luigi is Mario's younger brother, known for being taller and jumpier.",
    "Princess Peach rules over the Mushroom Kingdom and is often rescued by Mario.",
    "Bowser, the King of Koopas, is Mario’s main enemy and loves kidnapping Princess Peach.",
    "Yoshi first appeared in Super Mario World (1990) and was Nintendo’s first attempt at a rideable character.",
    "The Super Star power-up grants temporary invincibility and changes Mario’s colors in older games.",
    "The Ice Flower was introduced in New Super Mario Bros. Wii (2009).",
    "Tanooki Suit first appeared in Super Mario Bros. 3 (1988), and allows Mario to turn into a statue.",
    "Goombas were originally cheap enemies added to make Super Mario Bros. easier to program.",
    "Shy Guys first appeared in Yoshi’s Island (1995) and are actually from the Mario universe’s spin-offs.",
    "The Chain Chomp is loosely inspired by the Shiba-Inu dog hitting a chain in Mario creator’s childhood.",
    "Yoshi Island’s background music is considered one of the most memorable in the SNES era.",
    "Bowser Jr. first appeared in Super Mario Sunshine (2002) and often uses his Junior Clown Car.",
    "King Boo is the main antagonist of Luigi’s Mansion (2001) and has a recurring role in Mario Kart series.",
    "Princess Rosalina appears in Super Mario Galaxy (2007) and helps guide Mario through space with the Luma.",
]

# 26 quiz questions total
quiz_questions: List[Dict] = [
    {
        "question": "What is Mario's job?",
        "options": ["Carpenter", "Plumber", "Chef", "Teacher"],
        "answer_index": 1,
        "fact": "Mario was first a carpenter in Donkey Kong, then later became famous as a plumber."
    },
    {
        "question": "Who is Mario's brother?",
        "options": ["Toad", "Bowser", "Luigi", "Wario"],
        "answer_index": 2,
        "fact": "Luigi is taller and can often jump higher than Mario."
    },
    {
        "question": "What does the Super Star do?",
        "options": ["Makes Mario invisible", "Gives Mario temporary invincibility", "Takes away a life", "Slows Mario down"],
        "answer_index": 1,
        "fact": "When Mario gets a Super Star, he flashes colors and can defeat most enemies on touch."
    },
    {
        "question": "Who usually kidnaps Princess Peach?",
        "options": ["Yoshi", "Bowser", "Luigi", "Donkey Kong"],
        "answer_index": 1,
        "fact": "Bowser has been trying to capture Peach since the original Super Mario Bros."
    },
    {
        "question": "Which item gives Mario an extra life?",
        "options": ["Super Mushroom", "Super Star", "1-Up Mushroom", "Fire Flower"],
        "answer_index": 2,
        "fact": "The green 1-Up Mushroom gives Mario an extra life."
    },
    {
        "question": "Which character is the princess of the Mushroom Kingdom?",
        "options": ["Rosalina", "Princess Peach", "Toadette", "Daisy"],
        "answer_index": 1,
        "fact": "Princess Peach rules over the Mushroom Kingdom in many Mario games."
    },
    {
        "question": "Which power-up lets Mario throw fireballs?",
        "options": ["Fire Flower", "Ice Flower", "Cat Suit", "Tanooki Suit"],
        "answer_index": 0,
        "fact": "The Fire Flower turns Mario into Fire Mario, who can throw fireballs."
    },
    {
        "question": "Which character is a friendly dinosaur that Mario can ride?",
        "options": ["Yoshi", "Bowser", "Chain Chomp", "King Boo"],
        "answer_index": 0,
        "fact": "Yoshi is Mario’s dinosaur friend and first appeared in Super Mario World."
    },
    {
        "question": "Which of these is NOT a common Mario enemy?",
        "options": ["Goomba", "Koopa Troopa", "Shy Guy", "Pikachu"],
        "answer_index": 3,
        "fact": "Pikachu is from the Pokémon series, not from the Mario universe."
    },
    {
        "question": "Which location is known as a difficult racetrack in Mario Kart?",
        "options": ["Mushroom Kingdom", "Rainbow Road", "Dark Lands", "Dry Dry Desert"],
        "answer_index": 1,
        "fact": "Rainbow Road is famous for its tricky turns and lack of guardrails."
    },
    {
        "question": "What does the Mini Mushroom do to Mario?",
        "options": ["Makes him huge", "Makes him tiny", "Gives him a cape", "Turns him invisible"],
        "answer_index": 1,
        "fact": "The Mini Mushroom shrinks Mario so he can fit into tiny passages."
    },
    {
        "question": "Which character is Bowser's son?",
        "options": ["Kamek", "Bowser Jr.", "King Boo", "Diddy Kong"],
        "answer_index": 1,
        "fact": "Bowser Jr. often appears with his dad in boss fights and uses the Junior Clown Car."
    },
    {
        "question": "Which power-up gives Mario a cat costume?",
        "options": ["Cat Suit", "Tanooki Suit", "Ice Flower", "Super Star"],
        "answer_index": 0,
        "fact": "The Cat Suit appears in Super Mario 3D World and lets Mario climb walls."
    },
    {
        "question": "Which character is known for throwing hammers at Mario?",
        "options": ["Hammer Bros", "Goombas", "Piranha Plant", "Shy Guys"],
        "answer_index": 0,
        "fact": "Hammer Bros are Koopa enemies that attack by throwing hammers from platforms."
    },
    {
        "question": "Which game first introduced Rosalina?",
        "options": ["Super Mario Galaxy", "Super Mario 64", "Super Mario Bros. 3", "Mario Kart 8"],
        "answer_index": 0,
        "fact": "Princess Rosalina is introduced in Super Mario Galaxy and lives on the Comet Observatory."
    },
    {
        "question": "Which enemy is a metal ball chained to a post?",
        "options": ["Goomba", "Chain Chomp", "Spiny", "Koopa"],
        "answer_index": 1,
        "fact": "Chain Chomps are inspired by dogs on chains from the creator’s childhood."
    },
    {
        "question": "Which kingdom is ruled by the penguins in the Mario movie?",
        "options": ["Ice Kingdom", "Jungle Kingdom", "Dark Lands", "Mushroom Kingdom"],
        "answer_index": 0,
        "fact": "In the Mario movie, the Ice Kingdom is defended by penguin soldiers."
    },
    {
        "question": "Who is the ruler of the Jungle Kingdom in the movie?",
        "options": ["Mario", "Cranky Kong", "Donkey Kong", "Daisy"],
        "answer_index": 1,
        "fact": "Cranky Kong is presented as the king of the Jungle Kingdom in the movie."
    },
    {
        "question": "Which character often appears with a magic broom and casts spells?",
        "options": ["Kamek", "Toad", "Yoshi", "Luigi"],
        "answer_index": 0,
        "fact": "Kamek is a Magikoopa who uses magic to help Bowser and Bowser Jr."
    },
    {
        "question": "Which location is known for sand, ruins, and quicksand?",
        "options": ["Yoshi Island", "Dry Dry Desert", "Dark Lands", "Rainbow Road"],
        "answer_index": 1,
        "fact": "Dry Dry Desert is a desert area featured in both Mario platformers and Mario Kart."
    },
    {
        "question": "Which ghost king often fights Luigi in haunted mansions?",
        "options": ["King Boo", "King Bomb Omb", "Bowser", "Kamek"],
        "answer_index": 0,
        "fact": "King Boo is the main villain in Luigi’s Mansion and also appears in Mario Kart."
    },
    {
        "question": "What do Goombas look like?",
        "options": ["Turtles with shells", "Round bombs with feet", "Mushroom-like creatures", "Flying fish"],
        "answer_index": 2,
        "fact": "Goombas are small mushroom-like enemies that often appear in large groups."
    },
    {
        "question": "Which power-up allows Mario to fly or float using a tail?",
        "options": ["Super Star", "Cat Suit", "Tanooki Suit", "Mini Mushroom"],
        "answer_index": 2,
        "fact": "The Tanooki Suit gives Mario a tail to spin-attack and briefly fly or glide."
    },
    {
        "question": "Which character helps Mario capture enemies and objects in Super Mario Odyssey?",
        "options": ["Luigi", "Cappy", "Bowser Jr.", "Toad"],
        "answer_index": 1,
        "fact": "In Super Mario Odyssey, Cappy lets Mario take control of enemies and objects by throwing the cap at them."
    },
    {
        "question": "What is the name of the city world based on New York in Super Mario Odyssey?",
        "options": ["Toad Town", "New Donk City", "Mushroom City", "Koopa City"],
        "answer_index": 1,
        "fact": "New Donk City is a sprawling urban world in Super Mario Odyssey, inspired by New York City and ruled by Pauline."
    },
    {
        "question": "Which console was Super Mario Odyssey originally released on?",
        "options": ["Nintendo Switch", "Wii", "GameCube", "Nintendo 64"],
        "answer_index": 0,
        "fact": "Super Mario Odyssey was released in 2017 for the Nintendo Switch."
    },
]

# -----------------------------
# SESSION STATE INITIALIZATION
# -----------------------------
# st.session_state is a Streamlit feature that lets me store variables between
# reruns of the script (for example, current quiz question and score).
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False
if "answer_submitted" not in st.session_state:
    st.session_state.answer_submitted = False
# New: track remaining attempts per question (2 tries max)
if "attempts_left" not in st.session_state:
    st.session_state.attempts_left = 2

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def show_characters_page():
    st.header("🧑‍🔧 Mario Characters")
    st.subheader("Character Overview Table")

    # I show a table for a quick overview, and then use a selectbox, so the user
    # can choose one character and see more details + an image without overcrowding the page.
    #
    # NOTE ABOUT THE SMALL ICONS ON THE TABLE:
    # When Streamlit renders st.dataframe, it automatically adds small icons
    # (for example, a column menu icon or sort indicators) inside the table
    # header. These icons are built-in Streamlit UI controls for the interactive
    # table. They let the user do things like scroll horizontally, resize columns,
    # or open column options (depending on the version of Streamlit).
    # I did NOT manually code those icons; they are part of the Streamlit library’s
    # default styling for dataframes so the table is easier to use.
    #
    # These are the icons on the table:
    # 👁️ **View / data options** – controls how the table is displayed.
    # ⬇️ **Download** – lets the user download the table data (usually as CSV).
    # 🔍 **Search** – lets the user search/filter within the table.
    # ⛶ **Fullscreen** – pops the table out to a larger/fullscreen view.
    #
    # So again, I didn’t “add” them manually in my code, 
    # they just come for free from Streamlit when I use `st.dataframe`.

    st.dataframe(
        {
            "Name": [c["name"] for c in characters],
            "Role": [c["role"] for c in characters],
            "First Appearance": [c["first_appearance"] for c in characters],
        },
        use_container_width=True,
    )

    st.subheader("Learn More About a Character")
    # st.selectbox is a Streamlit widget that shows a drop-down list so the user
    # can pick one character name at a time.
    selected_name = st.selectbox("Choose a character:", [c["name"] for c in characters])
    # Using next(...) with a generator expression to find the selected character
    # is a pattern I practiced from my Python notes and w3schools examples on loops.
    selected_char = next(c for c in characters if c["name"] == selected_name)
    st.write(f"**Role:** {selected_char['role']}")
    st.write(f"**Personality:** {selected_char['personality']}")
    st.write(f"**First Appearance:** {selected_char['first_appearance']}")

    # Originally, all character images was going to use the same width so that they appear roughly the same size.
    # However, due to size issues, most of character images normally use width=260, but a few characters (such as
    # Kamek, The Koopalings, Chain Chomp, Boom Boom, Pom Pom) have images that are naturally smaller, so I manually 
    # increase their display width so that it would make them easier to see.
    # st.image is a Streamlit function that displays an image file in the web app.
    larger_image_characters = [
        "Kamek", "The Koopalings", "Chain Chomp", "Boom Boom", "Pom Pom"
    ]
 
    if selected_char["image_path"]:
        if selected_char["name"] in larger_image_characters:
            st.image(selected_char["image_path"], caption=selected_char["name"], width=440)
        else:
            st.image(selected_char["image_path"], caption=selected_char["name"], width=260)
    else:
        st.info("Image for this character will be added later.")

def show_powerups_page():
    st.header("🍄 Power-Ups")
    # This st.dataframe call also shows the same kind of Streamlit icons as the
    # Characters table (built-in interactive header controls). Again, they are
    # part of Streamlit's dataframe component—not custom images I added.
    st.dataframe(
        {
            "Power-Up": [p["name"] for p in power_ups],
            "Effect": [p["effect"] for p in power_ups],
        },
        use_container_width=True,
    )
    st.subheader("See Power-Up Icon")
    selected_pu_name = st.selectbox("Choose a power-up:", [p["name"] for p in power_ups])
    selected_pu = next(p for p in power_ups if p["name"] == selected_pu_name)

    # Show a small icon for the selected power-up if the file is available.
    if selected_pu.get("image_path"):
        st.image(selected_pu["image_path"], caption=selected_pu["name"], width=250)
    else:
        st.info(f"Image for {selected_pu_name} can be added with st.image when the file is ready.")

def show_locations_page():
    st.header("🌍 Locations in the Mario Universe")
    # This table uses st.dataframe as well, so the same auto-generated UI icons
    # appear on top of the table. They provide Streamlit’s interactive features
    # like scrolling and column controls.
    st.dataframe(
        {
            "Location": [loc["name"] for loc in locations],
            "Description": [loc["description"] for loc in locations],
        },
        use_container_width=True,
    )
    st.subheader("Explore a Location")
    selected_loc_name = st.selectbox("Choose a location:", [loc["name"] for loc in locations])
    loc = next(l for l in locations if l["name"] == selected_loc_name)
    st.write(f"**Description:** {loc['description']}")

    # Show images for the selected location if the file is available.
    if loc.get("image_path"):
        st.image(loc["image_path"], caption=loc["name"], width=580)
    else:
        st.info("Location images can be added here using st.image().")

def show_comparison_page():
    """Displays a simple Mario vs. Luigi comparison based on selected category."""
    st.header("⚔️ Mario vs. Luigi Comparison")

    st.write("Choose a category to compare Mario and Luigi:")

    categories = ["Speed", "Jump Height", "Personality", "Game History"]
    # st.radio creates a group of radio buttons so the user can pick exactly one category.
    selected_category = st.radio("Comparison Category:", categories)

    # Very simple text-based comparison. Images are also shown after a choice is selected.
    if selected_category == "Speed":
        st.write("🏃 **Speed**: Mario is usually balanced; Luigi can feel a bit lighter or slippery in some games.")
        # One combined image that shows both Mario and Luigi for speed.
        st.image("mario_luigi_speed.png", caption="Mario & Luigi – speed comparison", width=560)
    elif selected_category == "Jump Height":
        st.write("🦘 **Jump Height**: Luigi often jumps higher but can be harder to control.")
        # One combined image that shows both Mario and Luigi for jump height.
        st.image("mario_luigi_jump.png", caption="Mario & Luigi – jump comparison", width=560)
    elif selected_category == "Personality":
        st.write("🙂 **Personality**: Mario is confident and brave; Luigi is loyal but more easily scared.")
        # One combined image that shows both Mario and Luigi for personality.
        st.image("mario_luigi_personality.png", caption="Mario & Luigi – personality comparison", width=560)
    elif selected_category == "Game History":
        st.write("🎮 **Game History**: Mario appears in more main titles; Luigi stars in games like 'Luigi’s Mansion'.")
        # Shows two images for history, because it was hard to find one combined.
        st.image("mario_history.png", caption="Mario – history timeline", width=600)
        st.image("luigi_history.png", caption="Luigi – history timeline", width=650)

def show_movie_vs_game_page():
    """Displays differences between movie and game versions of some characters."""
    st.header("🎬 Movie vs. Game")

    st.write(
        """
        Here I list a few simple differences between the Mario movie
        and the classic video games, so when you either play one of the
        Mario Games or watch the movie, you can tell the difference or
        how they are both similiar to each other.
        """
    )

    # Mario
    st.subheader("Mario")
    st.write("- **Game:** Focused mostly on jumping, platforming, and saving Peach.")
    st.write("- **Movie:** Shows more of Mario's life in Brooklyn and his relationship with Luigi.")
    st.image("mario_game.png", caption="Mario – Game version", width=260)
    st.image("mario_movie.png", caption="Mario – Movie version", width=200)

    # Bowser
    st.subheader("Bowser")
    st.write("- **Game:** Mostly a strong, boss-like enemy who breathes fire.")
    st.write("- **Movie:** Still a villain, but also has a funny crush on Peach and sings songs.")
    st.image("bowser_game.png", caption="Bowser – Game version", width=260)
    st.image("bowser_movie.png", caption="Bowser – Movie version", width=260)

    # Peach
    st.subheader("Peach")
    st.write("- **Game:** Often captured and rescued by Mario.")
    st.write("- **Movie:** More active fighter who helps train Mario and joins the action directly.")
    st.image("peach_game.png", caption="Peach – Game version", width=260)
    st.image("peach_movie.png", caption="Peach – Movie version", width=190)

    # Luigi
    st.subheader("Luigi")
    st.write("- **Game:** Mario’s brother and sidekick, featured in many main and spin-off games.")
    st.write("- **Movie:** Shows more of Luigi’s fears and his relationship with Mario and the Soquet family.")
    st.image("luigi_game.png", caption="Luigi – Game version", width=260)
    st.image("luigi_movie.png", caption="Luigi – Movie version", width=190)

    # Toad
    st.subheader("Toad")
    st.write("- **Game:** A loyal helper from the Mushroom Kingdom who often gives Mario items or advice.")
    st.write("- **Movie:** Acts as Peach’s brave guide and musician, helping Mario navigate the Mushroom Kingdom.")
    st.image("toad_game.png", caption="Toad – Game version", width=280)
    st.image("toad_movie.png", caption="Toad – Movie version", width=190)

    # Donkey Kong
    st.subheader("Donkey Kong")
    st.write("- **Game:** A strong gorilla hero/villain from Nintendo’s classic arcade era.")
    st.write("- **Movie:** Still powerful, appears in the Mario movie with a voice and big personality.")
    st.image("donkey_kong_game.png", caption="Donkey Kong – Game version", width=260)
    st.image("donkey_kong_movie.png", caption="Donkey Kong – Movie version", width=260)

    # Kamek & General Koopa
    st.subheader("Kamek & General Koopa")
    st.write("- **Game (Kamek):** A Magikoopa who often serves Bowser or his children.")
    st.write("- **Movie (Kamek):** Brings a magical presence and adds depth to Bowser’s plan.")
    st.write("- **Movie (General Koopa):** Loyal to Bowser, a strong army leader who is not always in older games.")
    st.image("kamek_game.png", caption="Kamek – Game version", width=260)
    st.image("kamek_movie.png", caption="Kamek – Movie version", width=260)
    st.image("general_koopa_movie.png", caption="General Koopa – Movie version", width=180)

def show_funfacts_page():
    st.header("⭐ Mario Fun Facts")
    st.write("Here are some fun facts about the Mario universe:")
    # Checkbox gives the user control to see all 20 fun facts or just a few;
    # this shows interactivity and keeps the page from feeling too long at first.
    # st.checkbox is another Streamlit input widget.
    show_all = st.checkbox("Show all fun facts (uncheck to show just a few)", value=True)
    # This simple if-else slicing is also based on patterns from my Python notes and w3schools.
    facts_to_show = fun_facts if show_all else fun_facts[:4]
    for fact in facts_to_show:
        st.write(f"- {fact}")
    st.write("\nThanks for learning some fun facts about the Super Mario universe!")

def reset_quiz_state():
    # This helper resets all the state variables for the quiz. It uses st.session_state
    # so that pressing "Restart Quiz" correctly starts from question 1 again.
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_finished = False
    st.session_state.answer_submitted = False
    st.session_state.attempts_left = 2  # reset attempts on full restart

def show_quiz_page():
    st.header("❓ Mario Quiz")
    if st.session_state.quiz_finished:
        st.subheader("Quiz Finished!")
        st.write(f"Your final score: **{st.session_state.score} / {len(quiz_questions)}**")
        if st.session_state.score == len(quiz_questions):
            st.success("Perfect score! You are a true Mario expert! 🍄")
        elif st.session_state.score >= len(quiz_questions) // 2:
            st.info("Nice job! You know quite a bit about Mario. ⭐")
        else:
            st.warning("You might be new to the Mushroom Kingdom. Keep exploring and try again!")
        if st.button("Restart Quiz"):
            reset_quiz_state()
        return

    q_index = st.session_state.current_question
    question_data = quiz_questions[q_index]
    st.subheader(f"Question {q_index + 1} of {len(quiz_questions)}")
    st.write(question_data["question"])

    # The selectbox now uses Streamlit's "disabled" option so that after the
    # user has either answered correctly OR used both attempts, the drop-down
    # is locked and they cannot change their answer anymore for this question.
    user_answer = st.selectbox(
        "Choose your answer:",
        question_data["options"],
        key=f"q_{q_index}",
        # Disable answer choices once the question is finished:
        # - answer_submitted is True (correct or 2 wrong tries), OR
        # - attempts_left == 0 (used both attempts).
        disabled=st.session_state.answer_submitted or st.session_state.attempts_left == 0,
    )

    # st.columns creates three side-by-side columns for the quiz buttons.
    col1, col2, col3 = st.columns(3)
    with col1:
        # Only show the "Try Again" button while the player still has attempts left
        # and I have NOT fully submitted/locked this question.
        # After the second wrong attempt, attempts_left == 0 and answer_submitted == True,
        # so this button disappears and the user cannot try a third time.
        if st.session_state.attempts_left > 0 and not st.session_state.answer_submitted:
            if st.button("Try Again", key=f"try_{q_index}"):
                # Just clear the submitted flag; let the user pick again.
                st.session_state.answer_submitted = False
                st.rerun()

    with col2:
        # "Submit Answer" only works while I haven't already submitted a final result
        # for this question (either correct or 2 failed attempts).
        if st.button("Submit Answer", key=f"submit_{q_index}") and not st.session_state.answer_submitted:
            correct_index = question_data["answer_index"]
            correct_text = question_data["options"][correct_index]
            if user_answer == correct_text:
                st.success("Correct! 🎉")
                st.session_state.score += 1
                st.info(f"Fun fact: {question_data['fact']}")
                st.session_state.answer_submitted = True
                st.session_state.attempts_left = 2  # ready for next question
            else:
                # First wrong attempt → let them try again without revealing the answer.
                if st.session_state.attempts_left > 1:
                    st.session_state.attempts_left -= 1
                    st.error(f"Not quite. Try again! You have {st.session_state.attempts_left} attempt(s) left.")
                else:
                    # Second wrong attempt → show correct answer and fact, then lock question.
                    # I keep the correct answer and fun fact on screen so the user can read them,
                    # and they must move on to the next question using the Next Question button.
                    st.session_state.attempts_left = 0
                    st.error(f"Not quite. The correct answer was: **{correct_text}**")
                    st.info(f"Fun fact: {question_data['fact']}")
                    st.session_state.answer_submitted = True

    with col3:
        # "Next Question" is only allowed once the current question is finished
        # (either the user got it correct OR they used both attempts).
        if st.button("Next Question", key=f"next_{q_index}") and st.session_state.answer_submitted:
            if q_index + 1 < len(quiz_questions):
                st.session_state.current_question += 1
                st.session_state.answer_submitted = False
                st.session_state.attempts_left = 2  # reset attempts for new question
                st.rerun()
            else:
                st.session_state.quiz_finished = True
                st.rerun()

# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------
# st.sidebar lets me place widgets on the left sidebar instead of the main page.
st.sidebar.title("Navigation")

# The slider is another Streamlit widget; it returns an integer 0–10.
fan_level = st.sidebar.slider(
    "How big of a Mario fan are you? (0 = New, 10 = Super Fan)",
    min_value=0,
    max_value=10,
    value=5
)
if fan_level <= 3:
    fan_label = "Mushroom Kingdom Rookie"
elif fan_level <= 7:
    fan_label = "Mushroom Kingdom Adventurer"
else:
    fan_label = "Super Mario Expert"
st.sidebar.write(f"Fan Level: **{fan_level}** – {fan_label}")

# st.sidebar.radio gives a simple navigation menu for switching between pages.
page = st.sidebar.radio(
    "Go to:",
    [
        "Characters", "Power-Ups", "Locations",
        "Mario vs. Luigi", "Movie vs. Game",
        "Fun Facts", "Quiz"
    ],
)

# Based on the chosen page, call the matching function. This if-elif structure
# is a basic Python control flow pattern that I also practiced in my notes and
# w3schools examples, and here I combined it with Streamlit.
if page == "Characters":
    show_characters_page()
elif page == "Power-Ups":
    show_powerups_page()
elif page == "Locations":
    show_locations_page()
elif page == "Mario vs. Luigi":
    show_comparison_page()
elif page == "Movie vs. Game":
    show_movie_vs_game_page()
elif page == "Fun Facts":
    show_funfacts_page()
elif page == "Quiz":
    show_quiz_page()
