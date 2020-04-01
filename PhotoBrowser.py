import justpy as jp
from glob import glob


def photo_browser():
    all_container_classes = 'm-2 p-2 bg-gray-500'
    images_container_style = 'display:flex; justify-content:space-evenly; flex-wrap: wrap;'
    small_img_container_style = 'background-color: gray;'
    main_img_style = f'width: {1920 / 2.4}px; display: block; margin-left: auto; margin-right: auto;'
    small_img_style = f'width: {1920 / 2.4 / 4}px;'

    def small_container_mouseenter(self, msg):
        msg.page.main_img.src = self.child.src
        self.child.style += ' transform: scale(.85);'

    def small_container_mouseleave(self, msg):
        self.child.style = small_img_style

    def show_main_container_mouseleave(self, msg):
        msg.page.main_img.src = msg.page.default_img

    wp = jp.WebPage()

    default_img = '/static/photos/B9ARSkuWrMA.jpg'
    main_img_container = jp.Div(a=wp, classes=all_container_classes)
    main_img = jp.Img(src=default_img, a=main_img_container, style=main_img_style)

    images_container = jp.Div(a=wp, classes=all_container_classes, mouseleave=show_main_container_mouseleave,
                              style=images_container_style)
    small_images = glob('photos/*')

    wp.main_img = main_img
    wp.default_img = default_img

    for i in range(len(small_images)):
        small_img_container = jp.Div(a=images_container, classes=all_container_classes,
                                     mouseenter=small_container_mouseenter, mouseleave=small_container_mouseleave,
                                     style=small_img_container_style)
        small_img = jp.Img(src=f'/static/{small_images[i]}', a=small_img_container, style=small_img_style, )
        small_img_container.child = small_img

    return wp


jp.justpy(photo_browser)
