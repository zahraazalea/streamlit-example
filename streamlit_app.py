import streamlit as st
from textblob import TextBlob


# Page configuration
st.set_page_config(page_title="Mental Health Support", page_icon=":mortar_board:")

# Website title and description
st.title("Covid-19 Endemic Phase Mental Health Support Websites")
st.markdown("This website provides resources and support for people facing challenges during the Covid-19 endemic phase.")

additional_link = {
    "Link": "https://www.who.int/teams/mental-health-and-substance-use/mental-health-and-covid-19",
    "Description": "Here's some information about mental health and its correlation to Covid-19."
}

st.markdown(f"**[{additional_link['Description']}]({additional_link['Link']})**")

# Section: Mental Health Support Websites
st.header("Mental Health Support Websites")
st.markdown("Here are some recommended websites to help with stress and mental health:")

websites = {
    "The Mighty": {
        "Link": "https://themighty.com/",
        "Description": "If you enjoy writing or painting about your personal struggles or revelations, The Mighty accepts your work as well. Simply publish your words or photographs on the site for others to read and comment on. The Mighty is a diverse mental health support website."
    },
    "Therapy Tribe": {
        "Link": "https://support.therapytribe.com/",
        "Description": "Therapy Tribe elevates peer-to-peer mental health support to new heights. Aside from a variety of resources, it provides dedicated domains for a variety of topics, such as anxiety, depression, and more. Therapy Tribe is perfect for someone looking for specific help."
    },
    "Calm Sage": {
        "Link": "https://www.calmsage.com/",
        "Description": "If you appreciate the notion of sharing your personal tales and meeting people who have had similar experiences, check out Calm Sage. The website is more of an instructional resource than a social hub, but it does accept guest blogs highlighting mental health successes."
    }
}

for name, data in websites.items():
    st.markdown(f"**[{name}]({data['Link']})**")
    st.write(data["Description"])

# Section: Additional Websites
st.header("Calm Your Nerves")
st.markdown("Here are some additional websites that could calm your nerves:")

additional_websites = {
    "The Quiet Place": {
        "link": "https://thequietplaceproject.xyz/thequietplace",
        "description": "The Quiet Place is a one-of-a-kind online experience that offers a tranquil and calming respite from the noise and stress of regular life. It provides a basic, calm setting in which guests can disengage from technology, decompress, and find a moment of peace. "
    },
    "Weavesilk": {
        "link": "http://weavesilk.com/",
        "description": "Weavesilk is a therapeutic and relaxing digital art platform that offers users a serene and calming experience. It provides a virtual canvas where visitors can let their problems slip away while effortlessly creating beautiful, flowing designs."
    }
}

for name, data in additional_websites.items():
    st.markdown(f"**[{name}]({data['link']})**")
    st.write(data["description"])

# User Feedback and Sentiment Analysis
st.header("User Feedback and Sentiment Analysis")
feedback = st.text_input("Enter your feedback:")

if feedback:
    blob = TextBlob(feedback)
    sentiment_score = blob.sentiment.polarity
    sentiment_label = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
    
    st.markdown(f"**Feedback:** {feedback}")
    st.markdown(f"**Sentiment Score:** {sentiment_score:.2f}")
    st.markdown(f"**Sentiment:** {sentiment_label}")
else:
    st.info("Enter your feedback in the text box above to see the sentiment analysis results.")

# # Define image data with descriptions
# images = [
#     {
#         "url": "https://example.com/image1.jpg",
#         "description": "Image 1 description"
#     },
#     {
#         "url": "https://example.com/image2.jpg",
#         "description": "Image 2 description"
#     },
#     {
#         "url": "https://example.com/image3.jpg",
#         "description": "Image 3 description"
#     }
# ]

# # Display images with descriptions
# for image in images:
#     st.image(image["url"], use_column_width=True)
#     st.write(image["description"])

# Footer
st.markdown("---")
st.markdown("Created by [Zahra Azalea binti Faizi (U2102264), for WIE2003 S2 22/23]")
