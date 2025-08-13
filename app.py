import streamlit as st
from PIL import Image
from rembg import remove
import io

# App title and subtitle
st.title(" Clean Frame App")
st.write("**Cut it out. Color it in.** — Remove and replace photo backgrounds easily!")

# File uploader
uploaded_file = st.file_uploader("📤 Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Open image
    image = Image.open(uploaded_file).convert("RGB")

    # Show original
    st.subheader("📷 Original Image")
    st.image(image)

    # Remove background
    st.subheader("✨ Removing Background...")
    bg_removed = remove(image)

    # Convert to RGBA to preserve transparency
    bg_removed = bg_removed.convert("RGBA")

    st.subheader("✅ Background Removed")
    st.image(bg_removed)

    # Choose action
    option = st.radio("Choose an option:", ["Download Transparent", "Add Background Color"])

    if option == "Download Transparent":
        buf = io.BytesIO()
        bg_removed.save(buf, format="PNG")
        st.download_button(
            label="⬇ Download Transparent Image",
            data=buf.getvalue(),
            file_name="background_removed.png",
            mime="image/png"
        )

    else:
        color = st.color_picker("🎨 Pick a background color", "#ffffff")
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)

        # Add chosen background
        colored_bg = Image.new("RGBA", bg_removed.size, (r, g, b, 255))
        colored_bg.paste(bg_removed, mask=bg_removed.split()[3])

        st.subheader("🌈 New Background Applied")
        st.image(colored_bg)

        buf = io.BytesIO()
        colored_bg.save(buf, format="PNG")
        st.download_button(
            label="⬇ Download Image with Background",
            data=buf.getvalue(),
            file_name="background_colored.png",
            mime="image/png"
        )

else:
    st.info("Please upload an image to start.")
