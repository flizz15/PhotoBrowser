import justpy as jp
from glob import glob


def photo_browser():
    all_container_classes = 'm-2 p-2 bg-gray-500'
    small_img_container_classes = all_container_classes + ' inline-flex'
    main_img_style = f'width: {1920 / 2.4}px; display: block; margin-left: auto; margin-right: auto;'
    small_img_style = f'width: {1920 / 2.4 / 4}px;'

    wp = jp.WebPage()

    main_img_container = jp.Div(a=wp, classes=all_container_classes)
    main_img = jp.Img(src='/static/photos/B9ARSkuWrMA.jpg', a=main_img_container, style=main_img_style)

    images_container = jp.Div(a=wp, classes=all_container_classes)
    small_images = glob('photos/*')
    for i in range(len(small_images)):
        small_img_container = jp.Div(a=images_container, classes=small_img_container_classes, style='background-color: gray;')
        jp.Img(src=f'/static/{small_images[i]}', a=small_img_container, style=small_img_style)

    return wp


jp.justpy(photo_browser)
