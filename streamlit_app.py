import streamlit as st

# Page configuration
st.set_page_config(page_title="Mental Health Support", page_icon=":mortar_board:")

# Website title and description
st.title("Covid-19 Endemic Phase Mental Health Support Websites")
st.markdown("This website provides resources and support for people facing challenges during the Covid-19 endemic phase.")

# Section: Mental Health Support Websites
st.header("Mental Health Support Websites")
st.markdown("Here are some recommended websites to help with stress and mental health:")

websites = {
    "Website 1": {
        "link": "https://themighty.com/",
        "description": "If you enjoy writing or painting about your personal struggles or revelations, The Mighty accepts your work as well. Simply publish your words or photographs on the site for others to read and comment on. The Mighty is a diverse mental health support website."
    },
    "Website 2": {
        "link": "https://support.therapytribe.com/",
        "description": "Therapy Tribe elevates peer-to-peer mental health support to new heights. Aside from a variety of resources, it provides dedicated domains for a variety of topics, such as anxiety, depression, and more. Therapy Tribe is perfect for someone looking for specific help."
    },
    "Website 3": {
        "link": "https://www.calmsage.com/",
        "description": "If you appreciate the notion of sharing your personal tales and meeting people who have had similar experiences, check out Calm Sage. The website is more of an instructional resource than a social hub, but it does accept guest blogs highlighting mental health successes."
    }
}

for name, link in websites.items():
    st.markdown(f"- [{name}]({link})")

# Section: Additional Websites
st.header("Calm Your Nerves")
st.markdown("Here are some additional websites that could calm your nerves:")

additional_websites = {
    "Website 4": {
        "link": "https://thequietplaceproject.xyz/thequietplace",
        "description": ""The Quiet Place" is a one-of-a-kind online experience that offers a tranquil and calming respite from the noise and stress of regular life. It provides a basic, calm setting in which guests can disengage from technology, decompress, and find a moment of peace. "
    },
    "Website 5": {
        "link": "http://weavesilk.com/",
        "description": ""Weavesilk" is a therapeutic and relaxing digital art platform that offers users a serene and calming experience. It provides a virtual canvas where visitors can let their problems slip away while effortlessly creating beautiful, flowing designs."
    }
}

for name, data in additional_websites.items():
    st.markdown(f"**[{name}]({data['link']})**")
    st.write(data["description"])

# Footer
st.markdown("---")
st.markdown("Created by [Zahra Azalea binti Faizi (U2102264), for WIE2003 S2 22/23]")
