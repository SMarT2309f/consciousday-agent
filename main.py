import streamlit as st
import sqlite3
import datetime

st.title("📝 ConsciousDay Journal Assistant")

# Input form
journal = st.text_area("Morning Journal")
dream = st.text_area("Dream")
intention = st.text_input("Intention of the Day")
priorities = st.text_area("Top 3 Priorities")

if st.button("Reflect & Plan"):
    st.success("Processing your reflection...")

    # Static demo output (replace with LangChain logic later)
    st.subheader("📘 Inner Reflection")
    st.write("You seem stressed but calmness is your intention.")

    st.subheader("💤 Dream Interpretation")
    st.write("Dream of falling shows fear of losing control.")

    st.subheader("🧠 Mindset Insight")
    st.write("Focus on clarity today.")

    st.subheader("📅 Suggested Strategy")
    st.write("Morning: Deep work | Afternoon: Meetings | Evening: Gym")

    # Save to SQLite
    conn = sqlite3.connect("entries.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        journal TEXT,
        intention TEXT,
        dream TEXT,
        priorities TEXT,
        reflection TEXT,
        strategy TEXT
    )""")

    today = str(datetime.date.today())
    c.execute("INSERT INTO entries (date, journal, intention, dream, priorities, reflection, strategy) VALUES (?, ?, ?, ?, ?, ?, ?)", 
              (today, journal, intention, dream, priorities, "You seem stressed but calmness is your intention.", "Morning: Deep work | Afternoon: Meetings | Evening: Gym"))
    conn.commit()
    conn.close()

# View by date
st.markdown("---")
st.subheader("🔍 View Previous Entry")
date = st.date_input("Select a date")
if st.button("Show Entry"):
    conn = sqlite3.connect("entries.db")
    c = conn.cursor()
    c.execute("SELECT * FROM entries WHERE date=?", (str(date),))
    data = c.fetchone()
    if data:
        st.write("📘 Journal:", data[2])
        st.write("🎯 Intention:", data[3])
        st.write("💤 Dream:", data[4])
        st.write("📌 Priorities:", data[5])
        st.write("🧠 Reflection:", data[6])
        st.write("📅 Strategy:", data[7])
    else:
        st.warning("No entry found.")
