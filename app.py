import streamlit as st
from PIL import Image
import io
import sys

# rembg comes with dependencies so we are trying to run in try block
try:
    from rembg import remove
    REMBG_AVAILABLE = True
except ImportError as e:
    st.error(f"⚠️ **Import Error**: The `rembg` library could not be imported. Error: {str(e)}")
    st.info("This usually happens when deploying to Streamlit Cloud. Please check the requirements.txt file and ensure all dependencies are properly installed.")
    REMBG_AVAILABLE = False

# App title and subtitle
st.title("Clean Frame App")
st.write("**Cut it out. Color it in.** — Remove and replace photo backgrounds easily!")

# Check if rembg is available
if not REMBG_AVAILABLE:
    st.error("🚫 **Background removal is currently unavailable**")
    st.info("Please check the deployment logs and ensure all dependencies are properly installed.")
    st.stop()

# File uploader 
uploaded_file = st.file_uploader("📤 Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    try:
        # Open original image
        image = Image.open(uploaded_file).convert("RGB")

        # Show original image
        st.subheader("📷 Original Image")
        st.image(image)

        # Remove background with progress indicator
        st.subheader("✨ Removing Background...")
        with st.spinner("Processing image... This may take a few seconds."):
            bg_removed = remove(image)

        # Convert to RGBA to preserve transparency
        bg_removed = bg_removed.convert("RGBA")

        st.subheader("✅ Background Removed")
        st.image(bg_removed)

        # Choose action either downloading or adding background color
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

    except Exception as e:
        st.error(f"❌ **Error processing image**: {str(e)}")
        st.info("Please try uploading a different image or check if the image format is supported.")
        st.exception(e)

else:
    st.info("Please upload an image to start.")

# Add system info for debugging
if st.checkbox("🔧 Show Debug Information"):
    st.subheader("System Information")
    st.write(f"**Python Version:** {sys.version}")
    st.write(f"**Streamlit Version:** {st.__version__}")
    st.write(f"**rembg Available:** {REMBG_AVAILABLE}")
    
    if REMBG_AVAILABLE:
        try:
            import rembg
            st.write(f"**rembg Version:** {rembg.__version__}")
        except:
            st.write("**rembg Version:** Unable to determine")
