import streamlit as st

Logo = st.empty()
button_box = st.empty()

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0rem;
        }
        .centered-title-wrapper {
            text-align: center;
            color: OrangeRed;
            margin: 0;
        }
        .centered-title-wrapper h1 {
            font-size: 215px;
            line-height: 1.1;
            margin: 0;
        }
        .stButton>button {
            font-size: 24px;
            padding: 0.5em 2em;
            color: white;
            background-color: OrangeRed;
            display: block;
            margin: 50px auto 0 auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)


if "Clicksv" not in st.session_state:
    st.session_state.Clicksv = False


if not st.session_state.Clicksv:
    with Logo:
        st.markdown("""
            <div class='centered-title-wrapper'>
                <h1>ONE</h1>
                <h1>MEAL</h1>
                <h1>BOT</h1>
            </div>
        """, unsafe_allow_html=True)

    with button_box:
        if st.button("시작하기 ▶"):
            st.session_state.Clicksv = True
            st.rerun()
