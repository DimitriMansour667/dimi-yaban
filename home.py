import streamlit as st
from anime import search, info, episodes
from episode import Episode
from streamlit import components


st.title('Dimi-Yaban')

funcOption = st.selectbox('Function', ['Search', 'Info','Episode'])

if funcOption == 'Search':
    title = st.text_input('Title')
    num = st.slider('Number of Results', 1, 100, 1)
    type = st.selectbox('Search Type', ['anime', 'manga', 'novel'])
    if st.button('Search'):
        results = search(type, title, num)
        st.write(results)

if funcOption == 'Info':
    id = st.text_input('ID')
    if st.button('Search'):
        data = info(id)
        st.write(data)

if funcOption == 'Episode':
    id = st.text_input('ID')
    if st.button('Search'):
        data = episodes(id)
        if data:
            st.session_state["data"] = data
    if "data" in st.session_state:
        epSelector = st.selectbox("Select an episode:", [x.episodeNumber for x in st.session_state["data"]],index=None,placeholder="pls select un bahabagay")
        if epSelector:
            source = st.session_state["data"][epSelector].source()['sources']
            url = source[len(source)-1]['url']
            html_code = f"""
            <video id="video" controls></video>
            <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
            <script>
            var video = document.getElementById('video');
            if(Hls.isSupported()) {{
                var hls = new Hls();
                hls.loadSource('{url}');
                hls.attachMedia(video);
                hls.on(Hls.Events.MANIFEST_PARSED,function() {{
                video.play();
                }});
            }}
            </script>
            """
            components.v1.html(html_code, height=600)
    
