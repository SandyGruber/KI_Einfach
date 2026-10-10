import streamlit as st

st.title("🧠 KI-Lernspiel: Essen oder Trinken?")

# 1. Speicher für die Wortlisten
if "ess" not in st.session_state:
    st.session_state.ess = ["apfel", "brot", "pizza"]

if "tri" not in st.session_state:
    st.session_state.tri = ["wasser", "saft", "tee"]

# 2. Satz eingeben
was = st.text_input(
    "Schreib einen Satz mit Essen oder Trinken drin:"
).lower()

if was:
    punkteEss = sum(1 for wort in st.session_state.ess if wort in was)
    punkteTri = sum(1 for wort in st.session_state.tri if wort in was)

    st.subheader("Auswertung")
    if punkteEss > punkteTri:
        st.success("essen! 🍎")
    elif punkteTri > punkteEss:
        st.success("trinken! 🥤")
    else:
        st.info("weiß nicht 🤔")

    st.divider()

    # 3. KI Lernen
    st.subheader("Bring der KI etwas bei 🧠")
    kategorie = st.radio(
        "Kategorie:", ["Nichts / Passt so", "Essen 🍎", "Trinken 🥤"]
    )
    neu = st.text_input("Welches Wort aus deinem Satz war das?").lower()

    if st.button("Wort speichern"):
        if neu and kategorie == "Essen 🍎":
            st.session_state.ess.append(neu)
            st.success(f"Gelernt! '{neu}' ist jetzt Essen 🍎")
        elif neu and kategorie == "Trinken 🥤":
            st.session_state.tri.append(neu)
            st.success(f"Gelernt! '{neu}' ist jetzt Trinken 🥤")

# Seitenleiste mit aktuellem Wissen
with st.sidebar:
    st.header("Aktuelles Wissen der KI")
    st.write("**Essen:**", ", ".join(st.session_state.ess))
    st.write("**Trinken:**", ", ".join(st.session_state.tri))
