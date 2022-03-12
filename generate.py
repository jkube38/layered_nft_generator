from PIL import Image
import os
import random
import prev_run
from datetime import datetime


'''
This was written to specifics of how the artwork was created and will need
alterations to accommodate any other usage.
Layered NFT Generator (generate.py) assembles NFT png's layer by layer with
the use of the Pillow library included in the requirements.txt file.
All files must be .png since they will be layered onto each other.
ALL images should be saved at the desired positions on the canvas.
'''

# Directory variables are absolute paths to each directory containing the
# image variations for each trait in you creation, each NFT will randomly
# select from these directories to assemble your image e.g. eye directory
# contains images of your art (only the eyes) with all possible eye variations.
# create your paths accordingly.
base_path = '../../NFTs/Originals/squatch/squatch_base/'
eye_path = '../../NFTs/Originals/squatch/eyes/'
acc_path = '../../NFTs/Originals/squatch/accessories/'
head_path = '../../NFTs/Originals/squatch/headwear/'
hold_path = '../../NFTs/Originals/squatch/hand_item/'
mouth_path = '../../NFTs/Originals/squatch/mouths/'
pierce_path = '../../NFTs/Originals/squatch/piercings/'
cap_path = '../../NFTs/Originals/squatch/backward_cap/'
dread_path = '../../NFTs/Originals/squatch/beard_dreads/'
vest_path = '../../NFTs/Originals/squatch/suit_vest/'
hand_path = '../../NFTs/Originals/squatch/hands/'
new_nft_path = '../../NFTs/Originals/squatch/drop_v3/'
doc_path = '../../NFTs/Originals/squatch/docs/'

# Generate a list for each trait to be randomly selected from
base_opts = [file for file in os.listdir(base_path) if '.DS' not in file]
eye_opts = [file for file in os.listdir(eye_path) if '.DS' not in file]
acc_opts = [file for file in os.listdir(acc_path) if '.DS' not in file]
head_opts = [file for file in os.listdir(head_path) if '.DS' not in file]
hold_opts = [file for file in os.listdir(hold_path) if '.DS' not in file]
mouth_opts = [file for file in os.listdir(mouth_path) if '.DS' not in file]
pierce_opts = [file for file in os.listdir(pierce_path) if '.DS' not in file]

# list of lists of selected traits for each nft
trait_selections = []

# importing prev generated list to avoid duplicates
prev_gen = prev_run.test
for traits in prev_gen:
    if traits not in trait_selections:
        trait_selections.append(traits)


def trait_selection(nft_total):

    for count in range(nft_total):
        # Random selection of traits
        # base color
        base = random.choice(base_opts)
        # head accessory
        head_acc = random.choice(head_opts)
        # eye style
        eyes = random.choice(eye_opts)
        # mouth style
        mouth = random.choice(mouth_opts)
        # Accessory
        accessory = random.choice(acc_opts)
        # holding item
        holding = random.choice(hold_opts)
        # piercing type
        piercing = random.choice(pierce_opts)

        # list of current trait selection
        decision = [base, head_acc, eyes, mouth, accessory, holding, piercing]

        # verifies the selection is not already in the trait selection list
        # and adds one to count if it is to avoid duplicates and assures
        # correct count
        if decision not in trait_selections:
            trait_selections.append(decision)
        else:
            nft_total += 1


trait_selection(5)
# nft_total currently is the total amount you want to add the collection


def generate_pngs(filename):
    total_nfts = len(trait_selections) + 1
    for choice in range(306, total_nfts):
        traits = trait_selections[choice - 1]
        color = traits[0].split('_')[2]

        # Base color and image
        new_nft = Image.open(base_path + traits[0])

        # Accessory Image
        if traits[4] == 'dreads.png':
            acc = f'{color}_beard_dreads.png'
            acc_img = Image.open(dread_path + acc)
            new_nft.paste(acc_img, (0, 0), acc_img)
        elif traits[4] == 'vest.png':
            acc = f'{color}_vest.png'
            acc_img = Image.open(vest_path + acc)
            new_nft.paste(acc_img, (0, 0), acc_img)
        else:
            acc_img = Image.open(acc_path + traits[4])
            new_nft.paste(acc_img, (0, 0), acc_img)

        # Piercing Image
        piercing_img = Image.open(pierce_path + traits[6])
        new_nft.paste(piercing_img, (0, 0), piercing_img)

        # Eye Image
        eye_img = Image.open(eye_path + traits[2])
        new_nft.paste(eye_img, (0, 0), eye_img)

        # Headwear Image
        if traits[1] == 'backward_cap.png':
            head_acc = f'backward_cap_{color}_fur.png'
            head_acc_img = Image.open(cap_path + head_acc)
            new_nft.paste(head_acc_img, (0, 0), head_acc_img)
        else:
            head_acc_img = Image.open(head_path + traits[1])
            new_nft.paste(head_acc_img, (0, 0), head_acc_img)

        # Holding Image
        holding_img = Image.open(hold_path + traits[5])
        new_nft.paste(holding_img, (0, 0), holding_img)

        # Mouth Image
        mouth_img = Image.open(mouth_path + traits[3])
        new_nft.paste(mouth_img, (0, 0), mouth_img)

        # Hand Image
        hand_img = Image.open(hand_path + f'{color}_hand.png')
        new_nft.paste(hand_img, (0, 0), hand_img)

        # Save the new nft
        new_nft.save(f'{new_nft_path}{filename}{choice}.png')

    now = datetime.now()
    with open(f'{doc_path}{now}.txt', 'w') as f:
        for selection in trait_selections:
            f.write(str(f'{selection},\n'))


generate_pngs('Crypto Squatch')
