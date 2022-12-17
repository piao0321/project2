from PIL import Image
from numpy import dot,linalg,average
# 对图片进行统一化处理
def get_thum(image, size=(64, 64), greyscale=False):
    # 利用image对图像大小重新设置, Image.ANTIALIAS为高质量的
    image = image.resize(size, Image.ANTIALIAS)
    if greyscale:
        # 将图片转换为L模式，其为灰度图，其每个像素用8个bit表示
        image = image.convert('L')
    return image
# 计算图片的余弦距离
def image_similarity_vectors_via_numpy(image1, image2):
    image1 = get_thum(image1)
    image2 = get_thum(image2)
    images = [image1, image2]
    vectors = []
    norms = []
    for image in images:
        vector = []
        for pixel_tuple in image.getdata():
            vector.append(average(pixel_tuple))
        vectors.append(vector)
        # linalg=linear（线性）+algebra（代数），norm则表示范数
        # 求图片的范数？？
        norms.append(linalg.norm(vector, 2))
    a, b = vectors
    a_norm, b_norm = norms
    # dot返回的是点积，对二维数组（矩阵）进行计算
    res = dot(a / a_norm, b / b_norm)
    return res
if __name__ == "__main__":
    img1 = Image.open('picture/9975.png')
    img1 = get_thum(img1)
    s = []
    for i in range(9975,10000):
        img2 = Image.open('picture/'+str(i)+'.png')
        img2 = get_thum(img2)
        s.append([i,image_similarity_vectors_via_numpy(img1, img2)])
    for i in range(0,len(s)-1):
        for j in range(0,len(s)-1-i):
            if s[j][1]<s[j+1][1]:
                s[j],s[j+1] = s[j+1],s[j]
    for i in range(0,len(s)):
        print(s[i])
