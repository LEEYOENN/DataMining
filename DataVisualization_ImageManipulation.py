import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
##20210193 이연
#####문제 1#####

# df = pd.read_csv("homework2.csv")
# ##print(df)


# country_sal = df.groupby('Country')['Salary'].mean()

# print(country_sal)

# label = ['Canada', 'UK', 'USA']
# index = np.arange(len(label))

# plt.bar(index, country_sal, width=0.5, alpha=0.7)
# plt.title('Average Salary by Country', fontsize=20)
# plt.xlabel('country', fontsize=13)
# plt.ylabel('average salary', fontsize=13)
# plt.xticks(index, label, fontsize=13)
# plt.show()


# x = df['Salary']
# y = df['Age']
# plt.scatter(x,y, alpha=0.7)
# plt.title("Age ~ Salary")
# plt.xlabel('Salary')
# plt.ylabel('Age')
# plt.show()


#####문제 2#####

from PIL import Image


for i in range(1,11):
    img = Image.open('images/dog%d.jpg' %i)

f = open("list.txt", 'r')
lines = f.readlines()
cnt = 1
directory_name = 'images/' 
for line in lines :
    file_name = directory_name + line.strip()
    img = Image.open(file_name) 
    if cnt % 2 == 1 :
        rotate_image = img.rotate(30, expand=True)
        new_name = file_name.replace('dog', 'rot30_dog')
        rotate_image.save(new_name)
        cnt+=1
    else :
        x1 = img.size[0] / 10
        y1 = (img.size[1] / 10) *2
        x2 = (img.size[0] / 10) *3
        y2 = (img.size[1] / 10) *5

        crop_image = img.crop((x1, y1, x2, y2))
        new_name = file_name.replace('dog', 'crop_dog')
        crop_image.save(new_name)
        cnt+=1
f.close()