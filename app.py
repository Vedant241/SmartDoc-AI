import os
import tempfile
import streamlit as st
from rag import load_document, create_vector_store, get_answer

st.set_page_config(page_title="SmartDoc AI", page_icon="📄")
st.title("📄 SmartDoc AI — Document Q&A")
st.write("Upload a PDF or text file and ask questions about it.")

uploaded_file = st.file_uploader("Upload your document", type=["pdf", "txt"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    if "vector_store" not in st.session_state or st.session_state.get("file_name") != uploaded_file.name:
        with st.spinner("Reading and processing document..."):
            documents = load_document(tmp_path)
            st.session_state.vector_store = create_vector_store(documents)
            st.session_state.file_name = uploaded_file.name
        st.success(f"✅ '{uploaded_file.name}' processed successfully!")

    question = st.text_input("Ask a question about your document:")

    if question:
        with st.spinner("Thinking..."):
            answer = get_answer(st.session_state.vector_store, question)
        st.markdown("### Answer:")
        st.write(answer)

    os.unlink(tmp_path)
