import streamlit as st


def render_attachments_tab():
    st.header("📂 Upload Supporting Documents")

    st.markdown("_Upload any notices or documents received from Court or Landlord._")

    uploaded_files = st.file_uploader(
        label="Upload evidence files (PDF, PNG, JPG, DOCX)",
        type=["pdf", "png", "jpg", "jpeg", "docx"],
        accept_multiple_files=True
    )

    if uploaded_files:
        st.success(f"{len(uploaded_files)} file(s) uploaded.")
        st.markdown("### 📎 Uploaded Files")
        for file in uploaded_files:
            st.markdown(f"- {file.name}")
    else:
        st.info("No files uploaded yet.")
