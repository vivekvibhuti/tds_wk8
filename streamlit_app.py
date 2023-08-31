import streamlit as st
st.set_page_config(
    page_title="Find the Largest Number",
    layout="wide",
    initial_sidebar_state="expanded",
    # theme={"primary": "#F63366", "backgroundColor": "#0E1117", "secondaryBackgroundColor": "#31333F", "textColor": "#FFFFFF"}
)
st.markdown("""
<style>
body {
    color: #fff;
    background-color: #000;
}
</style>
    """, unsafe_allow_html=True)
def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Find the Largest Number")
    
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")
    
    if st.button("Find Largest"):
        largest = find_largest(num1, num2, num3)
        st.write(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
