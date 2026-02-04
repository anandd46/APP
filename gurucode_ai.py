import streamlit as st

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="GuruCode AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 GuruCode AI")
st.subheader("AI Mentor for Learning & Developer Productivity")

st.markdown("---")

# -------------------------------
# Sidebar Options
# -------------------------------
option = st.sidebar.selectbox(
    "Choose Mode",
    ["Concept Explanation", "Code Debugging"]
)

language = st.sidebar.selectbox(
    "Explanation Language",
    ["English", "Hindi"]
)

# -------------------------------
# Concept Explanation Logic
# -------------------------------
def explain_concept(topic, language):
    explanations = {
        "Binary Search": {
            "English": "Binary Search is an efficient algorithm that finds an element in a sorted list by repeatedly dividing the search range into half.",
            "Hindi": "Binary Search ek efficient algorithm hai jo sorted list me element ko aadha-aadha divide karke dhoondta hai."
        },
        "Bubble Sort": {
            "English": "Bubble Sort repeatedly swaps adjacent elements if they are in the wrong order.",
            "Hindi": "Bubble Sort ek simple sorting technique hai jisme adjacent elements ko swap kiya jata hai."
        },
        "Recursion": {
            "English": "Recursion is a technique where a function calls itself to solve a problem.",
            "Hindi": "Recursion ek technique hai jisme function khud ko call karta hai."
        }
    }

    return explanations.get(topic, {}).get(language, "Explanation not available for this topic.")

# -------------------------------
# Code Debugging Logic
# -------------------------------
def analyze_code_error(code):
    if "IndexError" in code:
        return (
            "❌ Error Type: Index Error\n\n"
            "📌 Reason: You are accessing a list index that does not exist.\n\n"
            "✅ Solution: Check the list length before accessing elements."
        )

    elif "for i in range(10)" in code:
        return (
            "⚠️ Possible Logical Error\n\n"
            "📌 Reason: Loop runs fixed times regardless of list size.\n\n"
            "✅ Solution: Use range(len(list_name)) instead."
        )

    elif "==" in code and "=" not in code.replace("==", ""):
        return (
            "❌ Syntax Error\n\n"
            "📌 Reason: Assignment operator (=) is missing.\n\n"
            "✅ Solution: Use '=' for assignment and '==' for comparison."
        )

    else:
        return (
            "ℹ️ No syntax error detected.\n\n"
            "If output is incorrect, check logic or conditions."
        )

# -------------------------------
# UI – Concept Explanation
# -------------------------------
if option == "Concept Explanation":
    st.header("📘 Learn a Programming Concept")

    topic = st.selectbox(
        "Select Topic",
        ["Binary Search", "Bubble Sort", "Recursion"]
    )

    if st.button("Explain Concept"):
        explanation = explain_concept(topic, language)
        st.success("Explanation Generated")
        st.write(explanation)

# -------------------------------
# UI – Code Debugging
# -------------------------------
if option == "Code Debugging":
    st.header("🛠️ AI Code Debugger")

    code_input = st.text_area(
        "Paste your code here",
        height=200
    )

    if st.button("Analyze Code"):
        if code_input.strip() == "":
            st.warning("Please enter some code.")
        else:
            result = analyze_code_error(code_input)
            st.info("Analysis Result")
            st.text(result)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Built for AI for Bharat Hackathon | Student Track")
