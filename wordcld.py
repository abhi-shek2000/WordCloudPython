from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as pPlot
import numpy as npy

source = open('Sample.txt', 'r').read()
def convert_cloud(string):
    maskArray = npy.array(Image.open('heart.jpg'))
    # cloud
    cloud = WordCloud(background_color='black', max_words=500, mask=maskArray, stopwords= set(STOPWORDS), contour_color='red', contour_width=3)
    # generate
    cloud.generate( string )
    cloud.to_file('python.png')


convert_cloud( source.lower() )



