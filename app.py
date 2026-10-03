import streamlit as st
from main import resolve_ticket


st.set_page_config(
    page_title="AI IT Ticket Resolver",
    page_icon="🛠️"
)

st.title("🛠️ AI IT Ticket Resolver")

st.write(
    "Describe your IT issue and the AI will classify it "
    "and provide a relevant solution."
)

ticket = st.text_area(
    "Describe your IT issue",
    placeholder="Example: I am unable to connect to the VPN."
)

if st.button("Resolve Ticket"):

    if not ticket.strip():
        st.warning("Please enter your IT issue.")

    else:
        with st.spinner("Analyzing your ticket..."):

            result = resolve_ticket(ticket)

        st.session_state["ticket"] = ticket
        st.session_state["classification"] = result["classification"]
        st.session_state["solution"] = result["solution"]
        st.session_state["resolved"] = False
        st.session_state["show_feedback"] = True


# ---------------------------------------
# DISPLAY RESULT
# ---------------------------------------

if "classification" in st.session_state:

    st.subheader("📋 Classification")
    st.write(st.session_state["classification"])

    st.subheader("💡 Recommended Solution")
    st.write(st.session_state["solution"])


# ---------------------------------------
# ASK IF ISSUE WAS RESOLVED
# ---------------------------------------

if st.session_state.get("show_feedback", False):

    st.divider()

    st.subheader("Did this solve your issue?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Yes, my issue is resolved"):

            st.session_state["resolved"] = True
            st.session_state["show_feedback"] = False

    with col2:
        if st.button("❌ No, I still need help"):

            st.session_state["resolved"] = False
            st.session_state["show_feedback"] = False
            st.session_state["needs_ticket"] = True


# ---------------------------------------
# RESOLVED
# ---------------------------------------

if st.session_state.get("resolved", False):

    st.success("🎉 Great! We're glad we could resolve your issue.")

    st.write("Thank you for using AI IT Ticket Resolver! 😊")


# ---------------------------------------
# CREATE SUPPORT TICKET
# ---------------------------------------

if st.session_state.get("needs_ticket", False):

    st.divider()

    st.subheader("🎫 Create a Support Ticket")

    st.write(
        "Sorry that the suggested solution didn't solve your issue. "
        "Please provide your email and we'll create a support ticket."
    )

    email = st.text_input(
        "Your email address",
        placeholder="example@gmail.com"
    )

    if st.button("Create Support Ticket"):

        if not email.strip():
            st.warning("Please enter your email address.")

        elif "@" not in email or "." not in email:
            st.warning("Please enter a valid email address.")

        else:
            st.success(
                "Your support ticket has been created. "
                "We'll contact you at your email address."
            )