import streamlit as st


BAD_CODE = """public class Example{
public static void main(String[] args){
int x=10;
if(x>5){
System.out.println("Too tight!");
}
}
}"""

GOOD_CODE = """public class Example {
    public static void main(String[] args) {
        int x = 10;
        if (x > 5) {
            System.out.println("Readable and consistent!");
        }
    }
}"""

st.set_page_config(page_title="Java Checkstyle Tutor", page_icon="✅", layout="wide")

st.title("✅ Java Checkstyle Tutor")
st.write(
    "This tutor app turns the Checkstyle lab into a code-quality coach by showing what style rules improve and why they matter."
)

left, right = st.columns(2)

with left:
    st.subheader("Before")
    st.code(BAD_CODE, language="java")

with right:
    st.subheader("After")
    st.code(GOOD_CODE, language="java")

rule = st.selectbox(
    "Choose a style concept",
    ["Indentation", "Spacing", "Braces", "Naming", "Readability"],
)

tips = {
    "Indentation": "Indentation makes control flow easier to scan, especially in nested conditions and loops.",
    "Spacing": "Spaces around operators, keywords, and braces reduce visual friction and make code easier to read quickly.",
    "Braces": "Consistent brace placement helps teams read code predictably and prevents logic mistakes during edits.",
    "Naming": "Clear names make code self-explanatory and reduce the need for extra comments.",
    "Readability": "Checkstyle is not just about rules; it encourages habits that make collaboration and maintenance easier.",
}

st.info(tips[rule])

st.markdown("### Quick Self-Check")
checks = [
    "Are braces aligned consistently?",
    "Are blocks indented clearly?",
    "Is spacing around operators readable?",
    "Would another student understand the code fast?",
]

for item in checks:
    st.write(f"- {item}")
