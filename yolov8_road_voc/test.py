import numpy as np
import cv2

# image = 'image.png'
# image = cv2.imread(image)
# white = 255 * np.ones_like(image)
#  # 定义alpha和beta用于淡化图像
# alpha = 0.4
# beta = 1 - alpha
#  # 将原图像与白色图像混合，得到淡化的图像
# bgra = cv2.addWeighted(image, alpha, white, beta, 0)
# # bgra = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
# # bgra[..., 3] = 250
# cv2.imwrite('input.png', bgra)

image1 = 'pexels-pixabay-46160.jpg'
image1 = cv2.imread(image1)
white1 = 255 * np.ones_like(image1)
 # 定义alpha和beta用于淡化图像
alpha1 = 0.4
beta1 = 1 - alpha1
 # 将原图像与白色图像混合，得到淡化的图像
bgra1 = cv2.addWeighted(image1, alpha1, white1, beta1, 0)
# bgra = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
# bgra[..., 3] = 250
cv2.imwrite('bg.png', bgra1)

from ultralytics import YOLO
# Load a pretrained YOLOv8n model
model = YOLO('trained/weights/best.pt')
names = model.names
print(type(names))
names_list = []
for value in names.values():
    names_list.append(value)
print(names_list)