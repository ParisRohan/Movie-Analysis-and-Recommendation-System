import streamlit as st
import pandas as pd

from PIL import Image

#Set title

st.title('Movie Recommendation and Analysis')
image = Image.open('data2.png')
st.image(image,use_column_width=True)

def main():
	activities=['EDA','About us']
	option=st.sidebar.selectbox('Selection option:',activities)


#DEALING WITH THE EDA PART

	if option=='EDA':
		st.subheader("Exploratory Data Analysis")

		data=st.file_uploader("Upload dataset:",type=['csv','xlsx'])
		st.success("Data successfully loaded")
		if data is not None:
			df=pd.read_csv(data)
			st.dataframe(df.head(50))

			if st.checkbox("Display shape"):
				st.write(df.shape)
			if st.checkbox("Display columns"):
				st.write(df.columns)
			if st.checkbox("Select multiple columns"):
				selected_columns=st.multiselect('Select preferred columns:',df.columns)
				df1=df[selected_columns]
				st.dataframe(df1)

#DEALING WITH THE ABOUT US PAGE



	elif option=='About us':

		st.markdown('This is an interactive web page developed by Rohan Paris :)'
			)


		st.balloons()
	# 	..............


if __name__ == '__main__':
	main() 
