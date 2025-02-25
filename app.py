import streamlit as st

st.set_page_config(page_title="AI Blog Generator", page_icon="✍", layout="wide")

def main():
    st.title("AI Blog Generator")

    topic = st.text_input("Enter Blog Topic", placeholder="e.g., AI in Healthcare")

    if st.button("Generate Blog"):
        if topic:
            # Simulated AI-generated blog content (Replace with your AI model's output)
            blog_content = f"### Blog: {topic}\n\nThis is an AI-generated blog about {topic}..."

            # Store blog content in session state
            st.session_state["generated_blog"] = blog_content
            
            # Redirect to blog page in a new tab
            blog_url = "http://localhost:8501/blog_page"  # Adjust URL if needed
            js = f"window.open('{blog_url}', '_blank')"
            st.markdown(f'<script>{js}</script>', unsafe_allow_html=True)
        else:
            st.warning("Please enter a blog topic before generating.")

if __name__ == "__main__":
    main()
