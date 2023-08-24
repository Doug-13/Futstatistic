import streamlit as st
import numpy as np

st.session_state["data"]  


st.header('**Example App showing Anchor links**')

st.sidebar.markdown('''
# Sections
- [Section 1](#section-1)
- [Section 2](#section-2)
''', unsafe_allow_html=True)

st.header('Section 1')
st.write('''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet volutpat consequat mauris nunc congue nisi vitae suscipit tellus. Amet mauris commodo quis imperdiet. In metus vulputate eu scelerisque. Facilisis gravida neque convallis a cras semper. Quis vel eros donec ac odio. Posuere urna nec tincidunt praesent semper feugiat nibh sed. Vitae et leo duis ut. Consectetur lorem donec massa sapien faucibus et molestie ac feugiat. Scelerisque varius morbi enim nunc faucibus a. Eget velit aliquet sagittis id consectetur purus ut. Massa eget egestas purus viverra. Libero justo laoreet sit amet cursus sit. Nibh nisl condimentum id venenatis a condimentum vitae sapien.

Dictumst vestibulum rhoncus est pellentesque. Egestas sed tempus urna et pharetra pharetra. Eget est lorem ipsum dolor sit amet consectetur. Tortor pretium viverra suspendisse potenti. Diam maecenas ultricies mi eget mauris pharetra. Ultrices mi tempus imperdiet nulla. Volutpat ac tincidunt vitae semper quis. Viverra accumsan in nisl nisi scelerisque eu. Ut aliquam purus sit amet luctus venenatis lectus magna fringilla. Velit ut tortor pretium viverra suspendisse potenti nullam ac.

Commodo sed egestas egestas fringilla phasellus faucibus scelerisque. Pulvinar mattis nunc sed blandit libero volutpat sed cras. Fringilla est ullamcorper eget nulla. Egestas sed tempus urna et pharetra pharetra massa massa. Nunc vel risus commodo viverra maecenas accumsan lacus. Justo donec enim diam vulputate ut pharetra. Metus aliquam eleifend mi in nulla posuere sollicitudin. Lobortis mattis aliquam faucibus purus. Massa tincidunt dui ut ornare lectus sit amet. Et molestie ac feugiat sed lectus vestibulum. Mattis ullamcorper velit sed ullamcorper. Quam adipiscing vitae proin sagittis nisl rhoncus mattis rhoncus. Pulvinar sapien et ligula ullamcorper malesuada. Orci phasellus egestas tellus rutrum tellus pellentesque. Ut venenatis tellus in metus vulputate eu scelerisque felis imperdiet. Etiam erat velit scelerisque in dictum non consectetur.
''')

st.header('Section 2')
st.write('''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet volutpat consequat mauris nunc congue nisi vitae suscipit tellus. Amet mauris commodo quis imperdiet. In metus vulputate eu scelerisque. Facilisis gravida neque convallis a cras semper. Quis vel eros donec ac odio. Posuere urna nec tincidunt praesent semper feugiat nibh sed. Vitae et leo duis ut. Consectetur lorem donec massa sapien faucibus et molestie ac feugiat. Scelerisque varius morbi enim nunc faucibus a. Eget velit aliquet sagittis id consectetur purus ut. Massa eget egestas purus viverra. Libero justo laoreet sit amet cursus sit. Nibh nisl condimentum id venenatis a condimentum vitae sapien.

Dictumst vestibulum rhoncus est pellentesque. Egestas sed tempus urna et pharetra pharetra. Eget est lorem ipsum dolor sit amet consectetur. Tortor pretium viverra suspendisse potenti. Diam maecenas ultricies mi eget mauris pharetra. Ultrices mi tempus imperdiet nulla. Volutpat ac tincidunt vitae semper quis. Viverra accumsan in nisl nisi scelerisque eu. Ut aliquam purus sit amet luctus venenatis lectus magna fringilla. Velit ut tortor pretium viverra suspendisse potenti nullam ac.

Commodo sed egestas egestas fringilla phasellus faucibus scelerisque. Pulvinar mattis nunc sed blandit libero volutpat sed cras. Fringilla est ullamcorper eget nulla. Egestas sed tempus urna et pharetra pharetra massa massa. Nunc vel risus commodo viverra maecenas accumsan lacus. Justo donec enim diam vulputate ut pharetra. Metus aliquam eleifend mi in nulla posuere sollicitudin. Lobortis mattis aliquam faucibus purus. Massa tincidunt dui ut ornare lectus sit amet. Et molestie ac feugiat sed lectus vestibulum. Mattis ullamcorper velit sed ullamcorper. Quam adipiscing vitae proin sagittis nisl rhoncus mattis rhoncus. Pulvinar sapien et ligula ullamcorper malesuada. Orci phasellus egestas tellus rutrum tellus pellentesque. Ut venenatis tellus in metus vulputate eu scelerisque felis imperdiet. Etiam erat velit scelerisque in dictum non consectetur.
''')

if st.button('Level 1'):
    st.write('Level 1 passed!')
    if st.button('Level 2'):
        st.write('Level 2 passed')


st.title("Selectbox")

contact_options = ["Email", "Phone", "Text"]

st.header("Selectbox from a list")

contact_selected = st.selectbox("How would you like to be contacted?",
                                options= contact_options)

st.write("Selectbox returns:", contact_selected,
         "of type", type(contact_selected))

if contact_selected == "Email":
    st.write("**Comfirm your email address by clicking the link sent to you**")
else:
    st.write("**Thank you, we will be in touch soon**")

st.header("Selectbox from a NumPy array")

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

col1, mid, col2 = st.columns([1, 0.1, 3])
with col1:
    st.write("My Array:")
    array

array_selection = st.selectbox("Choose an option", options = array, index=1)

st.write("Array selection returns:", array_selection,
         "of type", type(array_selection))
