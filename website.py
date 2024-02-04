# The website

import streamlit as st
import math
from PIL import Image


def composite(base_img, overlay1_img, overlay2_img):
    # Open the base and overlay images

    # overlay1_img = Image.open('barbie1.png')
    # overlay2_img = Image.open('matthew.png')

    # Convert the overlay images to RGBA mode
    overlay1_img = overlay1_img.convert('RGBA')
    overlay2_img = overlay2_img.convert('RGBA')

    # Define the position where the overlay images will be pasted
    position1 = (600, 270)
    position2 = (850, 262)

    # Overlay the images over the base image
    base_img.paste(overlay1_img, position1, overlay1_img)
    base_img.paste(overlay2_img, position2, overlay2_img)

    # Save the resulting image
    # base_img.save('comp_1.png')

    return base_img


def background_img(background):
    if background == 'UT Tower':
        bg_img = Image.open('tower.jpeg')

    elif background == 'DKR Stadium':
        bg_img = Image.open('stadium.jpeg')

    elif background == 'Gregory Gym':
        bg_img = Image.open('greg.jpg')

    elif background == 'Blanton Museum of Art':
        bg_img = Image.open('art.jpeg')

    elif background == 'PCL':
        bg_img = Image.open('PCL.jpeg')

    elif background == 'Jester Java':
        bg_img = Image.open('jester.jpeg')

    elif background == 'Bates Recital Hall':
        bg_img = Image.open('Bates.jpg')

    elif background == 'Barbie Field':
        bg_img = Image.open('barbiefield.jpg')

    return bg_img


def glow_filter(base_img):
    pixels = base_img.getdata()
    new_pixels = []
    for p in pixels:
        r = p[0]
        g = p[1]
        b = p[2]

        newr = min(r+100, 255)
        newg = max(g-50, 0)
        newb = max(b-50, 0)
        new_pixels.append((newr, newg, newb))

    # Create a new image with the same size as the base image
    newImage = Image.new("RGB", base_img.size)

    # Put flattened pixel data into the new image
    newImage.putdata(new_pixels)

    # Save the resulting image
    newImage.save('glow_1.jpg')

    return newImage

def nostalgic_filter(base_img):
    pixels = base_img.getdata()
    new_pixels = []
    for p in pixels:
        r = p[0]
        g = p[1]
        b = p[2]

        newr = math.floor(0.393 * r + 0.769 * g + 0.189 * b)
        newg = math.floor(0.349 * r + 0.686 * g + 0.168 * b)
        newb = math.floor(0.272 * r + 0.534 * g + 0.131 * b)
        new_pixels.append((newr, newg, newb))

    # Create a new image with the same size as the base image
    newImage = Image.new("RGB", base_img.size)

    # Put flattened pixel data into the new image
    newImage.putdata(new_pixels)

    # Save the resulting image
    newImage.save('nostalgic_1.jpg')
    return newImage

def radiant_filter(base_img):
    pixels = base_img.getdata()
    new_pixels = []
    for p in pixels:
        r = p[0]
        g = p[1]
        b = p[2]

        newr = min(r+50, 255)
        newg = max(g-30, 0)
        newb = max(b-30, 0)
        new_pixels.append((newr, newg, newb))

    # Create a new image with the same size as the base image
    newImage = Image.new("RGB", base_img.size)

    # Put flattened pixel data into the new image
    newImage.putdata(new_pixels)

    # Save the resulting image
    newImage.save('radiant_1.jpg')
    return newImage

def watercolor_filter(base_img):
    pixels = base_img.getdata()
    new_pixels = []
    for p in pixels:
        r = p[0]
        g = p[1]
        b = p[2]

        newr = int(int(abs(g-b+g+r)*r/256))
        newg = int(int(abs(b-g+b+r)*r/256))
        newb = int(int(abs(b-g+b+r)*g/256))
        new_pixels.append((newr, newg, newb))

    # Create a new image with the same size as the base image
    newImage = Image.new("RGB", base_img.size)

    # Put flattened pixel data into the new image
    newImage.putdata(new_pixels)

    # Save the resulting image
    newImage.save('watercolor_1.jpg')
    return newImage

# def glow_filter(base_img): 
#     pixels = base_img.getdata()
#     new_pixels = []
#     pixels2 = []
#     for p in pixels:
#         pixels2.append(p)
#     for i in pixels2:
#         new_pixels.insert(0, i)

#     location = 0
#     while location < len(new_pixels):
#         p = new_pixels[location]
#         r = 255 - p[0]
#         g = 255 - p[1]
#         b = 255 - p[2]

#         newr = int(r*1.5)
#         newg = int(g*1.5)
#         newb = int(b*1.5)
        
#         if r>200 and b>200 and g>200:
#             newr -= 50
#             newg -= 50
#             newb -= 50
#         new_pixels[location] = (newr, newg, newb)
#         location += 1
    

#     # Create a new image with the same size as the base image
#     newImage = Image.new("RGB", base_img.size)

#     # Put flattened pixel data into the new image
#     newImage.putdata(new_pixels)

#     # Save the resulting image
#     newImage.save('glow_1.jpg')
#     return newImage



def filter(_img, effect):
    if effect == 'Nostalgic':
        new_img = nostalgic_filter(_img)
    elif effect == 'Radiant':
        new_img = radiant_filter(_img)
    elif effect == 'Watercolor':
        new_img = watercolor_filter(_img)
    # elif effect == 'Outline':
    #     new_img = outline_filter(_img)
    elif effect == 'Glow':
        new_img = glow_filter(_img)
    elif effect == 'None':
        new_img = _img
    
    return new_img

def change_alpha(_img, a):
    # adjust the transparency of the image
    img_with_alpha = _img.convert("RGBA")
    alpha = int(a * 255 / 100)  # Convert percentage to 0-255 scale
    img_with_alpha.putalpha(alpha)

    img_rgb = img_with_alpha.convert("RGB")
    img_rgb.save('alpha_1.jpg')

    return img_with_alpha

def main():
    st.title("Selfie with a Barbie at UT")

    st.header('Please customize your photo with the choices below:')

    st.subheader('1: Barbie')
    barbie_category = st.selectbox('Pick a barbie', ['barbie1', 'barbie2', 'barbie3', 'barbie4', 'barbie5'])

    st.subheader('2: Background')
    background = st.selectbox('Choose your background', ['UT Tower', 'DKR Stadium', 'Gregory Gym', 'Blanton Museum of Art', 
                                                         'PCL', 'Jester Java', 'Bates Recital Hall', 
                                                         'Barbie Field'])
   
    # set default background to UT Tower image
    base_img = background_img(background)

    st.subheader('3: Filter Effect')
    filter_effect = st.radio('Pick a filter effect', ['None', 'Nostalgic', 'Watercolor', 'Radiant', 'Glow'])

    # a slider bar for barbie's positions:
    st.subheader('4: Adjust the transparency of the image')
    alpha = st.slider('Slide to adjust alpha value', min_value = 50, max_value = 100, value = 100)
    st.write('Current alpha value:', alpha)


    st.header('Generated Image:')

    new_img = filter(base_img, filter_effect)

    new_img.save('middle.jpg')

    overlay1_img = Image.open(f'{barbie_category}.png')
    overlay2_img = Image.open('matthew.png')

    composite_img = composite(new_img, overlay1_img, overlay2_img)

    final_img = change_alpha(composite_img, alpha)

    st.image(final_img, caption = 'Generated Image')

    final_img.save('final.jpg')

    # st.download_button(
    #     label = 'Download image',
    #     data = composite_img,
    #     file_name = 'generated_selfie.png',
    #     mime = 'image/png'
    # )


if __name__ == '__main__':
    main()

