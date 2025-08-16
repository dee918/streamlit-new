import streamlit as st
import pandas as pd
import numpy as np

# Page settings
st.set_page_config(page_title="PIET College Portal", layout="wide")

# Sidebar menu
menu = st.sidebar.radio(
    "📌 Navigation",
    ["Home", "Events", "Placement Dashboard", "Bus Schedule", "Contact"]
)

# ------------------------------
# 1️⃣ HOME
# ------------------------------
if menu == "Home":
    st.title("Welcome to PIET College Portal 🎓")
    st.image("https://piet.co.in/wp-content/uploads/2020/01/PIET.png", width=300)
    st.markdown("""
    **Panipat Institute of Engineering & Technology (PIET)** is a premier engineering college in Haryana, 
    known for its academic excellence, industry collaborations, and vibrant campus life.

    ✅ AICTE Approved  
    ✅ NBA & NAAC Accredited  
    ✅ Industry-oriented curriculum
    """)
    st.success("Explore the portal to know more about PIET!")

# ------------------------------
# 2️⃣ EVENTS
# ------------------------------
elif menu == "Events":
    st.title("🏆 PIET Events & Activities")
    events = pd.DataFrame({
        "Event": ["Workshop on AI", "Annual Cultural Fest", "Sports Meet", "Hackathon 2024"],
        "Date": ["2024-08-15", "2024-09-10", "2024-10-05", "2024-11-20"],
        "Department": ["CSE", "All", "Sports Dept.", "CSE & AIML"]
    })
    st.table(events)

    st.subheader("Vote for Your Favourite Event")
    choice = st.radio("Select Event", events["Event"])
    if st.button("Vote"):
        st.success(f"Thanks for voting for {choice}!")

# ------------------------------
# 3️⃣ PLACEMENT DASHBOARD
# ------------------------------
elif menu == "Placement Dashboard":
    st.title("📊 Placement Dashboard - PIET")


    # Dummy placement data
    @st.cache_data
    def load_data():
        np.random.seed(42)
        data = {
            "Company": ["TCS", "Infosys", "Wipro", "Tech Mahindra", "Cognizant"],
            "Students Placed": np.random.randint(10, 50, 5),
            "Package(LPA)": np.random.choice([3.5, 4.2, 5.0, 6.5], 5)
        }
        return pd.DataFrame(data)


    df = load_data()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Students Placed per Company")
        st.bar_chart(df.set_index("Company")["Students Placed"])
    with col2:
        st.subheader("Average Package")
        st.bar_chart(df.set_index("Company")["Package(LPA)"])

    st.subheader("Placement Data")
    st.dataframe(df)

# ------------------------------
# 4️⃣ BUS SCHEDULE
# ------------------------------
elif menu == "Bus Schedule":
    st.title("🚌 PIET Bus Schedule")
    st.info("This is a demo schedule. Replace with real API when available.")

    stop = st.selectbox("Select your destination:", ["Karnal", "Panipat", "Delhi", "Chandigarh"])
    if st.button("Get Schedule"):
        st.success(f"Next bus to {stop} is at 4:30 PM")

# ------------------------------
# 5️⃣ CONTACT
# ------------------------------
elif menu == "Contact":
    st.title("📩 Contact Us")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    msg = st.text_area("Your Message")
    if st.button("Send"):
        if name and email and msg:
            st.success("Thank you! Your message has been sent.")
        else:
            st.error("Please fill all fields before submitting.")
