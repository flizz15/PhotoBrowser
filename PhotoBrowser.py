import justpy as jp
from glob import glob


def photo_browser():
    all_container_classes = 'm-8 p-4'
    small_img_container_classes = all_container_classes + ' bg-gray-700'
    images_container_style = 'display:flex; justify-content:space-evenly; flex-wrap: wrap;' \
                             'position: absolute; top: 500px;'
    main_img_style = 'width: 800px; display: block; margin-left: auto; margin-right: auto; position: fixed;' \
                     'z-index: 2; left: 0; right: 0; margin: 2% auto;'
    small_img_style = 'width: 200px;'

    def small_container_mouseenter(self, msg):
        msg.page.main_img.src = self.child.src
        self.child.style += ' transform: scale(.85);'

    def small_container_mouseleave(self, msg):
        self.child.style = small_img_style
        msg.page.main_img.src = msg.page.default_img

    def select_default_img(self, msg):
        msg.page.default_img = self.child.src
        for img_cont in msg.page.all_image_containers:
            img_cont.set_class('bg-gray-700')
        self.set_class('bg-red-700')

    wp = jp.WebPage()
    wp.body_classes = 'bg-gray-600'

    small_images = glob('photos/*')
    default_img = 'static/' + small_images[0]
    main_img = jp.Img(src=default_img, a=wp, style=main_img_style)

    jp.Div(text="Click on picture to set default", a=wp, classes='text-3xl p-2 m-2',
           style='position: absolute; top: 500px')
    images_container = jp.Div(a=wp, classes=all_container_classes, style=images_container_style)
    all_image_containers = []

    wp.main_img = main_img
    wp.default_img = default_img
    wp.all_image_containers = all_image_containers

    for i in range(len(small_images)):
        small_img_container = jp.Div(a=images_container, classes=small_img_container_classes, click=select_default_img,
                                     mouseenter=small_container_mouseenter, mouseleave=small_container_mouseleave,)
        small_img = jp.Img(src=f'/static/{small_images[i]}', a=small_img_container, style=small_img_style,)
        small_img_container.child = small_img
        all_image_containers.append(small_img_container)

    all_image_containers[0].set_class('bg-red-700')

    return wp


jp.justpy(photo_browser)
